# -*- coding: utf-8 -*-
"""Revision 1 analyses (added after pre-submission review; post hoc).

1. Evaluation-period-specific composition of CCVD approvals (FY2017-2025), using the
   separate 1-month and 2-6-month tables: annual counts and pre/post means.
2. Within-category contrasts defined within evaluation periods:
   - target defined exactly (1-month <100 h or 2-6-month <80 h) vs the rest
   - 1-month <100 h vs 1-month >=100 h
   - 2-6-month <80 h vs 2-6-month >=80 h
   - 2-6-month 80-100 h vs 2-6-month >=100 h (former 'specificity' contrast within one period)
   - combined-table contrasts restricted to the same years, for comparison
3. Alternative inference for the main contrast (<80 vs >=80 h, FY2009-2025):
   year-clustered standard errors, and OLS of the annual log ratio with a linear trend
   and Newey-West standard errors.
Output: output/results_v4_revision1.txt
"""
import pandas as pd, numpy as np, statsmodels.api as sm, statsmodels.formula.api as smf
D = 'data/'; O = 'output/'
ex = np.exp
out = []
def P(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)
def fmt(m, k):
    c = m.conf_int().loc[k]; return f'{ex(m.params[k]):.2f} ({ex(c[0]):.2f}-{ex(c[1]):.2f})'

LO = ['lt45', '45_60', '60_80']; HI = ['100_120', '120_140', '140_160', 'ge160']
ot = pd.read_csv(D + 'cvd_overtime_bands.csv')

# ---- 1. composition by evaluation period ----
def grp(r):
    if r.band == 'other': return 'other'
    if r.period == 'm1': return 'm1_lt100' if r.band in LO + ['80_100'] else 'm1_ge100'
    if r.band == '80_100': return 'm26_80_100'
    return 'm26_lt80' if r.band in LO else 'm26_ge100'
e = ot[(ot.fy >= 2017) & ot.period.isin(['m1', 'm26', 'm1+m26'])].copy(); e['g'] = e.apply(grp, axis=1)
T = e.groupby(['fy', 'g']).n.sum().unstack()[['m1_ge100', 'm1_lt100', 'm26_ge100', 'm26_80_100', 'm26_lt80', 'other']]
T['m1_total'] = T.m1_ge100 + T.m1_lt100; T['m26_total'] = T.m26_ge100 + T.m26_80_100 + T.m26_lt80
T['below_either_%'] = (100 * (T.m1_lt100 + T.m26_lt80) / T[['m1_ge100', 'm1_lt100', 'm26_ge100', 'm26_80_100', 'm26_lt80', 'other']].sum(1)).round(1)
P('== 1. CCVD approvals by evaluation period and overtime (FY2017-2025)')
P(T.to_string())
P('   mean FY2017-2020:', T.loc[2017:2020].drop(columns='below_either_%').mean().round(2).to_dict())
P('   mean FY2022-2025:', T.loc[2022:2025].drop(columns='below_either_%').mean().round(2).to_dict())
b = ot[(ot.band == '80_100') & ot.period.isin(['m1', 'm26']) & (ot.fy >= 2017)].pivot_table(index='fy', columns='period', values='n')
P('   share of combined 80-100 h band from the 1-month table (%):', (100 * b.m1 / (b.m1 + b.m26)).round(0).astype(int).to_dict())

# ---- 2. contrasts within evaluation periods (FY2017-2020 vs FY2022-2025; FY2021 excluded) ----
d = ot[(ot.fy >= 2017) & (ot.fy != 2021) & ot.period.isin(['m1', 'm26'])].copy(); d['post'] = (d.fy >= 2022).astype(int)
c = ot[(ot.period == 'combined') & (ot.fy >= 2017) & (ot.fy != 2021)].copy(); c['post'] = (c.fy >= 2022).astype(int)
def rr(data, tg, rf):
    x = data.copy(); x['tg'] = x.apply(tg, axis=1).astype(int); x['rf'] = x.apply(rf, axis=1).astype(int)
    x = x[(x.tg == 1) | (x.rf == 1)].groupby(['fy', 'tg', 'post']).n.sum().reset_index()
    return fmt(smf.glm('n ~ C(fy)+tg+tg:post', data=x, family=sm.families.Poisson()).fit(scale='X2'), 'tg:post')
P('\n== 2. Ratio changes within evaluation periods, FY2022-2025 vs FY2017-2020 (quasi-Poisson, year fixed effects)')
P('   exact target (1-month <100 h or 2-6-month <80 h) vs rest:',
  rr(d, lambda r: (r.period == 'm1' and r.band in LO + ['80_100']) or (r.period == 'm26' and r.band in LO),
        lambda r: (r.period == 'm1' and r.band in HI) or (r.period == 'm26' and r.band in HI + ['80_100'])))
P('   1-month <100 h vs 1-month >=100 h:', rr(d, lambda r: r.period == 'm1' and r.band in LO + ['80_100'], lambda r: r.period == 'm1' and r.band in HI))
P('   2-6-month <80 h vs 2-6-month >=80 h:', rr(d, lambda r: r.period == 'm26' and r.band in LO, lambda r: r.period == 'm26' and r.band in HI + ['80_100']))
P('   2-6-month <80 h vs 2-6-month >=100 h:', rr(d, lambda r: r.period == 'm26' and r.band in LO, lambda r: r.period == 'm26' and r.band in HI))
P('   2-6-month 80-100 h vs 2-6-month >=100 h:', rr(d, lambda r: r.period == 'm26' and r.band == '80_100', lambda r: r.period == 'm26' and r.band in HI))
P('   combined table, same years: <80 vs >=80 h:', rr(c, lambda r: r.band in LO, lambda r: r.band in HI + ['80_100']))
P('   combined table, same years: 80-100 vs >=100 h:', rr(c, lambda r: r.band == '80_100', lambda r: r.band in HI))

# ---- 3. alternative inference for the main contrast (FY2009-2025) ----
S = 2009
oc = ot[(ot.period == 'combined') & (ot.fy >= S) & (ot.fy != 2021) & (ot.band != 'other')].copy()
oc['tg'] = oc.band.isin(LO).astype(int); oc['post'] = (oc.fy >= 2022).astype(int); oc['t'] = oc.fy - S
g = oc.groupby(['fy', 'tg', 'post', 't']).n.sum().reset_index()
P('\n== 3. Alternative inference, <80 vs >=80 h, FY2022-2025 vs FY2009-2020')
for lab, f in [('year fixed effects', 'n ~ C(fy)+tg+tg:post'), ('plus group-specific trends', 'n ~ C(fy)+tg+tg:t+tg:post')]:
    m = smf.glm(f, data=g, family=sm.families.Poisson()).fit(cov_type='cluster', cov_kwds={'groups': g.fy})
    P(f'   {lab}, standard errors clustered by year:', fmt(m, 'tg:post'))
W = g.pivot_table(index='fy', columns='tg', values='n'); y = np.log(W[1] / W[0])
X = sm.add_constant(pd.DataFrame({'t': W.index - S, 'post': (W.index >= 2022).astype(int)}, index=W.index))
for L in [1, 2]:
    P(f'   annual log ratio, OLS with linear trend, Newey-West (lag {L}):', fmt(sm.OLS(y, X).fit(cov_type='HAC', cov_kwds={'maxlags': L}), 'post'))
open(O + 'results_v4_revision1.txt', 'w').write('\n'.join(out)); print('done')

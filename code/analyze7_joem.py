# -*- coding: utf-8 -*-
"""Additional analyses for the JOEM version (after critical review, November 2026).
1. Leave-one-year-out for the main contrast (<80 h vs >=80 h, combined tables).
2. Placebo revisions, two definitions, full results.
3. 80-<100 h vs >=100 h in the combined tables with two pre-revision windows.
4. Dispersion estimates; ITS for decisions.
5. Pooled approval percentages for Table 1.
"""
import pandas as pd, numpy as np, statsmodels.api as sm, statsmodels.formula.api as smf
D='data/'; O='output/'; S=2009; out=[]
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.append(s)
ex=np.exp
def ci(m,k): c=m.conf_int().loc[k]; return f'{ex(m.params[k]):.2f} ({ex(c[0]):.2f}-{ex(c[1]):.2f})'
def qp(f,d): return smf.glm(f,data=d,family=sm.families.Poisson()).fit(scale='X2')
ot=pd.read_csv(D+'cvd_overtime_bands.csv'); oc=ot[(ot.period=='combined')&(ot.fy>=S)].copy()
oc['g']=oc.band.map({'lt45':'lt80','45_60':'lt80','60_80':'lt80','other':'oth'}).fillna('ge80')
base=oc[oc.fy!=2021].copy(); base['post']=(base.fy>=2022).astype(int)
dd=base[base.g!='oth'].copy(); dd['tg']=(dd.g=='lt80').astype(int); dd=dd.groupby(['fy','tg','post']).n.sum().reset_index()
m=qp('n ~ C(fy)+tg+tg:post',dd)
P('== 1. Main contrast:',ci(m,'tg:post'),' dispersion (Pearson chi2/df):',round(m.scale,2),' df_resid:',int(m.df_resid))
vals=[]
for y in sorted(dd.fy.unique()):
    mm=qp('n ~ C(fy)+tg+tg:post',dd[dd.fy!=y]); vals.append(ex(mm.params['tg:post'])); P(f'   excluding FY{y}: {ci(mm,"tg:post")}')
P(f'   leave-one-year-out range: {min(vals):.2f} to {max(vals):.2f}')
P('   pre-revision FY2015-2020:',ci(qp('n ~ C(fy)+tg+tg:post',dd[dd.fy>=2015]),'tg:post'))
P('== 2a. Placebo, 4-year window (FY k to k+3 vs all earlier years from FY2009; data through k+3, <=FY2020)')
pre=dd[dd.fy<=2020]
v=[]
for k in range(2012,2018):
    d=pre[pre.fy<=k+3].copy(); d['post']=d.fy.between(k,k+3).astype(int); mm=qp('n ~ C(fy)+tg+tg:post',d); v.append(ex(mm.params['tg:post'])); P(f'   FY{k}-{k+3}: {ci(mm,"tg:post")}')
P(f'   range {min(v):.2f} to {max(v):.2f}')
P('== 2b. Placebo, step (FY k onward vs earlier years; all of FY2009-2020; at least 3 years each side)')
v=[]
for k in range(2012,2019):
    d=pre.copy(); d['post']=(d.fy>=k).astype(int); mm=qp('n ~ C(fy)+tg+tg:post',d); v.append(ex(mm.params['tg:post'])); P(f'   from FY{k}: {ci(mm,"tg:post")}')
P(f'   range {min(v):.2f} to {max(v):.2f}')
P('== 3. 80-<100 h vs >=100 h, combined tables')
b=base[base.band.isin(['80_100','100_120','120_140','140_160','ge160'])].copy(); b['tg']=(b.band=='80_100').astype(int); b=b.groupby(['fy','tg','post']).n.sum().reset_index()
P('   pre FY2009-2020:',ci(qp('n ~ C(fy)+tg+tg:post',b),'tg:post'))
P('   pre FY2017-2020:',ci(qp('n ~ C(fy)+tg+tg:post',b[b.fy>=2017]),'tg:post'))
w=b.pivot(index='fy',columns='tg',values='n'); w.columns=['ge100','b80_100']
for a,c in [(2009,2020),(2017,2020),(2022,2025)]: P(f'   mean FY{a}-{c}:',w.loc[a:c].mean().round(1).to_dict())
P('== 4. ITS incl. decisions, with dispersion')
for nm,f,steps,tr in [('CCVD','cvd_national.csv',[('s',2022)],(2021,)),('Mental','mental_national.csv',[('s2012',2012),('s2020',2020),('s2024',2024)],(2023,))]:
    df=pd.read_csv(D+f); d=df[df.fy.between(S,2025)].copy(); d['t']=d.fy-S; cols=['t']
    for k,y0 in steps: d[k]=(d.fy>=y0).astype(float); cols.append(k)
    d=d[~d.fy.isin(tr)]; X=sm.add_constant(d[cols])
    for yv in ['claims','decisions','approvals']:
        mm=sm.GLM(d[yv],X,family=sm.families.Poisson()).fit(scale='X2')
        P(f'   {nm} {yv}: '+'; '.join(f'{k} {ci(mm,k)}' for k,_ in steps)+f'; dispersion {mm.scale:.2f}')
    mm=sm.GLM(d.approvals/d.decisions,X,family=sm.families.Binomial(),var_weights=d.decisions).fit(scale='X2')
    P(f'   {nm} approval proportion: '+'; '.join(f'{k} {ci(mm,k)}' for k,_ in steps)+f'; dispersion {mm.scale:.2f}')
P('== 5. Pooled approval % (sum approvals / sum decisions)')
for nm,f,ws in [('CCVD','cvd_national.csv',[(2009,2020),(2022,2025)]),('Mental','mental_national.csv',[(2009,2011),(2012,2014),(2017,2019),(2020,2022),(2024,2025)])]:
    df=pd.read_csv(D+f)
    for a,c in ws:
        g=df[df.fy.between(a,c)]; P(f'   {nm} FY{a}-{c}: pooled {100*g.approvals.sum()/g.decisions.sum():.1f}%, mean of annual {100*(g.approvals/g.decisions).mean():.1f}%')
open(O+'results_v5_joem.txt','w').write('\n'.join(out))

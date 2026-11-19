# -*- coding: utf-8 -*-
"""Mental disorders: decisions, approved claims and approval proportions by event group, FY2017-2025.
Descriptive tables by period and the same year fixed-effects (quasi-Poisson) contrast used for the overtime
categories: change in the ratio of counts in one event group to counts in all other groups after the 2020
revision (FY2020 onward) and further after the 2023 revision (FY2024 onward); FY2023 is a transition year.
Output: output/results_v6_events.txt
"""
import pandas as pd, numpy as np, statsmodels.api as sm, statsmodels.formula.api as smf
E=pd.read_csv('data/mental_events.csv'); out=[]
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.append(s)
G=['harassment','conflict','workload','accident','failure','role','special','none']
LAB=dict(harassment='Harassment, bullying, assault',conflict='Other interpersonal conflicts',workload='Workload',
         accident='Accidents and disasters',failure='Failures and responsibility',role='Changes in role or position',
         special='Special events',none='No assessable event')
T=E.groupby(['fy','group'])[['decisions','approvals']].sum().reset_index()
W=T.pivot(index='fy',columns='group',values=['decisions','approvals'])
P('== 1. Annual counts by event group (decisions / approved claims)')
P('fy   '+'  '.join(f'{g[:10]:>12}' for g in G)+'        total')
for fy in W.index:
    P(fy,'  '.join(f"{int(W.loc[fy,('decisions',g)]):>5}/{int(W.loc[fy,('approvals',g)]):<6}" for g in G),
      f"  {int(W.loc[fy,'decisions'].sum())}/{int(W.loc[fy,'approvals'].sum())}")
P('\n== 2. Period summaries: mean annual decisions, mean annual approved claims, pooled approval %, share of approved claims %')
PER=[('FY2017-2019',2017,2019),('FY2020-2022',2020,2022),('FY2024-2025',2024,2025)]
for g in G+['all']:
    row=[]
    for lab,a,b in PER:
        t=T[T.fy.between(a,b)]; x=t if g=='all' else t[t.group==g]; n=b-a+1
        d=x.decisions.sum(); ap=x.approvals.sum(); row.append(f'{lab}: dec {d/n:.1f}, appr {ap/n:.1f}, appr% {100*ap/d:.1f}, share of appr {100*ap/t.approvals.sum():.1f}%, share of dec {100*d/t.decisions.sum():.1f}%')
    P(f'{LAB.get(g,"All claims")}\n   '+'\n   '.join(row))
P('\n== 3. Annual shares and approval proportions')
for fy in W.index:
    td=W.loc[fy,'decisions'].sum(); ta=W.loc[fy,'approvals'].sum()
    P(fy,'harassment: share of approved claims',f"{100*W.loc[fy,('approvals','harassment')]/ta:.1f}%",
      'approval %',f"{100*W.loc[fy,('approvals','harassment')]/W.loc[fy,('decisions','harassment')]:.1f}",
      '| conflict: share of decisions',f"{100*W.loc[fy,('decisions','conflict')]/td:.1f}%",
      'approval %',f"{100*W.loc[fy,('approvals','conflict')]/W.loc[fy,('decisions','conflict')]:.1f}",
      '| workload approval %',f"{100*W.loc[fy,('approvals','workload')]/W.loc[fy,('decisions','workload')]:.1f}",
      '| all approval %',f"{100*ta/td:.1f}")
def rr(col,tg):
    d=T[T.fy!=2023].copy(); d['tg']=d.group.isin(tg).astype(int)
    d=d.groupby(['fy','tg'])[col].sum().reset_index(); d['p20']=(d.fy>=2020).astype(int); d['p24']=(d.fy>=2024).astype(int)
    m=smf.glm(f'{col} ~ C(fy)+tg+tg:p20+tg:p24',data=d,family=sm.families.Poisson()).fit(scale='X2')
    def ci(k): c=m.conf_int().loc[k]; return f'{np.exp(m.params[k]):.2f} ({np.exp(c[0]):.2f}-{np.exp(c[1]):.2f})'
    return ci('tg:p20'),ci('tg:p24'),m.scale
P('\n== 4. Relative change in count ratios, quasi-Poisson with year fixed effects, FY2017-2025 excluding FY2023')
P('   (after the 2020 revision; further change after the 2023 revision; dispersion)')
for lab,col,tg in [('Approved claims: harassment group vs all other groups','approvals',['harassment']),
                   ('Decisions: harassment group vs all other groups','decisions',['harassment']),
                   ('Decisions: other interpersonal conflicts vs all other groups','decisions',['conflict']),
                   ('Approved claims: other interpersonal conflicts vs all other groups','approvals',['conflict']),
                   ('Approved claims: workload group vs all other groups','approvals',['workload'])]:
    a,b,s=rr(col,tg); P(f'   {lab}: {a}; {b}; dispersion {s:.2f}')
P('\n== 5. Selected items (decisions / approved claims)')
for it in ['power_harassment','bullying_assault','sexual_harassment','customer_misconduct','trouble_superior','overtime_80h']:
    x=E[E.item==it].set_index('fy'); P(f'   {it}: '+', '.join(f'{fy}: {int(r.decisions)}/{int(r.approvals)}' for fy,r in x.iterrows()))
ob=pd.read_csv('data/mental_overtime_bands.csv'); oth=ob[ob.band=='other'].set_index('fy').n
P('\n== 6. "Other" overtime category (approved claims) beside approved claims in the harassment group')
for fy in W.index: P(f"   {fy}: Other overtime category {int(oth[fy])}; harassment group {int(W.loc[fy,('approvals','harassment')])}; harassment + accidents + special events {int(W.loc[fy,('approvals','harassment')]+W.loc[fy,('approvals','accident')]+W.loc[fy,('approvals','special')])}")
open('output/results_v6_events.txt','w',encoding='utf-8').write('\n'.join(out)+'\n')

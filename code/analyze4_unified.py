# -*- coding: utf-8 -*-
"""解析期間をFY2009-2025に統一した再推定と、精神障害の時間外労働区分別の比較
起点FY2009の理由：精神障害の決定件数がFY2009から、精神障害の判断指針が2009年4月に改正（以後の期間で統一）。
精神障害の区分別支給決定はFY2017以降のみ公表。
"""
import pandas as pd, numpy as np, itertools, statsmodels.api as sm, statsmodels.formula.api as smf
D='data/'; O='output/'; S=2009
out=[]
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.append(s)
ex=np.exp
def ci(m,k): c=m.conf_int().loc[k]; return f'{ex(m.params[k]):.2f} ({ex(c[0]):.2f}-{ex(c[1]):.2f})'
cvd=pd.read_csv(D+'cvd_national.csv'); mn=pd.read_csv(D+'mental_national.csv')

def its(df,steps,years,trans=(),slope=None):
    d=df[df.fy.between(*years)].dropna(subset=['decisions']).copy(); d['t']=d.fy-d.fy.min(); cols=['t']
    for nm,y0 in steps: d[nm]=(d.fy>=y0).astype(float); cols.append(nm)
    if slope: d['sl']=np.clip(d.fy-slope+1,0,None); cols.append('sl')
    d=d[~d.fy.isin(trans)]; X=sm.add_constant(d[cols])
    r=sm.GLM(d.approvals/d.decisions,X,family=sm.families.Binomial(),var_weights=d.decisions).fit(scale='X2')
    c=sm.GLM(d.claims,X,family=sm.families.Poisson()).fit(scale='X2'); a=sm.GLM(d.approvals,X,family=sm.families.Poisson()).fit(scale='X2')
    return r,c,a
P(f'== 統一期間 FY{S}-2025')
P('-- A. 年平均（請求・決定・支給決定・認定率）')
for nm,df,pre,post in [('脳・心 2021',cvd,(S,2020),(2022,2025))]:
    for lab,(a,b) in [('前',pre),('後',post)]:
        g=df[df.fy.between(a,b)]; P(f'   {nm} {lab} FY{a}-{b}: 請求 {g.claims.mean():.1f} 決定 {g.decisions.mean():.1f} 支給決定 {g.approvals.mean():.1f} 認定率 {100*g.approvals.sum()/g.decisions.sum():.1f}%')
P('-- B. ITS')
r,c,a=its(cvd,[('s',2022)],(S,2025),(2021,))
P(f'   脳・心 2021: 請求 {ci(c,"s")}／支給決定 {ci(a,"s")}／認定率 {ci(r,"s")}')
d=cvd[cvd.fy.between(S,2025)&(cvd.fy!=2021)].copy(); d['s']=(d.fy>=2022).astype(float); X=sm.add_constant(d[['s']])
P(f"   脳・心 2021（トレンドなし）: 請求 {ci(sm.GLM(d.claims,X,family=sm.families.Poisson()).fit(scale='X2'),'s')}／支給決定 {ci(sm.GLM(d.approvals,X,family=sm.families.Poisson()).fit(scale='X2'),'s')}／認定率 {ci(sm.GLM(d.approvals/d.decisions,X,family=sm.families.Binomial(),var_weights=d.decisions).fit(scale='X2'),'s')}")
r,c,a=its(mn,[('s2012',2012),('s2020',2020),('s2024',2024)],(S,2025),(2023,))
for k,lab in [('s2012','精神 2011'),('s2020','精神 2020'),('s2024','精神 2023')]:
    P(f'   {lab}: 請求 {ci(c,k)}／支給決定 {ci(a,k)}／認定率 {ci(r,k)}')
r,c,a=its(mn,[('s2012',2012),('s2020',2020),('s2024',2024)],(S,2025),(2023,),slope=2020)
P(f'   精神 2023（2020年以降の傾き変化を追加）: 請求 {ci(c,"s2024")}／支給決定 {ci(a,"s2024")}／認定率 {ci(r,"s2024")}')

# ---- C. 脳・心 区分内比較 ----
ot=pd.read_csv(D+'cvd_overtime_bands.csv'); oc=ot[(ot.period=='combined')&(ot.fy>=S)].copy()
oc['g']=oc.band.map({'lt45':'lt80','45_60':'lt80','60_80':'lt80','other':'oth'}).fillna('ge80')
base=oc[oc.fy!=2021].copy(); base['post']=(base.fy>=2022).astype(int); base['t']=base.fy-S
def rr(tg,ref,trend=False):
    d=base[base.band.isin(tg+ref)].copy(); d['tg']=d.band.isin(tg).astype(int); d=d.groupby(['fy','tg','post','t']).n.sum().reset_index()
    f='n ~ C(fy)+tg+tg:post'+('+tg:t' if trend else '')
    m=smf.glm(f,data=d,family=sm.families.Poisson()).fit(scale='X2'); return ci(m,'tg:post')
LT=['lt45','45_60','60_80']; GE=['80_100','100_120','120_140','140_160','ge160']
P('-- C. 脳・心 区分内比較（改正後FY2022-25 vs 改正前FY2009-20）')
P('   80h未満/80h以上:', rr(LT,GE), '｜群別トレンド:', rr(LT,GE,True))
P('   80-100h/100h以上（標的外）:', rr(['80_100'],GE[1:]))
P('   短期・異常な出来事/80h以上:', rr(['other'],GE))
W=base.groupby(['fy','g']).n.sum().unstack(); W['lr']=np.log(W.lt80/W.ge80); yrs=W.index.values; pm=yrs>=2022
obs=W.lr[pm].mean()-W.lr[~pm].mean(); diffs=[]
for cmb in itertools.combinations(range(len(yrs)),pm.sum()):
    mm=np.zeros(len(yrs),bool); mm[list(cmb)]=True; diffs.append(W.lr[mm].mean()-W.lr[~mm].mean())
diffs=np.array(diffs); P(f'   置換検定：観測比 {ex(obs):.2f}、{len(diffs)}通り中 {int((diffs>=obs-1e-12).sum())}通り、p={np.mean(diffs>=obs-1e-12):.4f}')
pre=W[~pm]; pl=[]
for k in range(S+3,2018):
    d=base[(base.g!='oth')&(base.fy<=k+3)&(base.fy<=2020)].copy(); d['tg']=(d.g=='lt80').astype(int); d['post']=d.fy.between(k,k+3).astype(int)
    d=d.groupby(['fy','tg','post']).n.sum().reset_index()
    pl.append(f'FY{k}-{k+3}: {ex(smf.glm("n ~ C(fy)+tg+tg:post",data=d,family=sm.families.Poisson()).fit(scale="X2").params["tg:post"]):.2f}')
P('   時間プラセボ：', ', '.join(pl))
avg=lambda a,b: W.loc[a:b,['lt80','ge80','oth']].mean().round(1).to_dict()
P('   年平均 FY2009-20:', avg(S,2020), ' FY2022-25:', avg(2022,2025))
dt=pd.read_csv(D+'cvd_by_type.csv'); g=dt[(dt.fy>=S)&(dt.fy!=2021)].copy(); g['post']=(g.fy>=2022).astype(int); g['tg']=(g.type=='虚血性心疾患等').astype(int)
m=smf.glm('approvals ~ C(fy)+tg+tg:post',data=g,family=sm.families.Poisson()).fit(scale='X2'); P('   病型 心疾患/脳血管:', ci(m,'tg:post'))
g['t']=g.fy-S
m=smf.glm('approvals ~ C(fy)+tg+tg:t+tg:post',data=g,family=sm.families.Poisson()).fit(scale='X2'); P('   病型 心疾患/脳血管（病型別トレンド）:', ci(m,'tg:post'))
# 期間・年の除外・区分定義の感度分析（Table 2）
dd=base[base.g!='oth'].copy(); dd['tg']=(dd.g=='lt80').astype(int); dd=dd.groupby(['fy','tg','post']).n.sum().reset_index()
def rr2(d):
    m=smf.glm('n ~ C(fy)+tg+tg:post',data=d,family=sm.families.Poisson()).fit(scale='X2'); return ci(m,'tg:post')
P('   改正前をFY2015-20に限定:', rr2(dd[dd.fy>=2015]))
for y in [2013,2020,2022]: P(f'   FY{y}を除外:', rr2(dd[dd.fy!=y]))
d2=base[base.band!='other'].copy(); d2['tg']=d2.band.isin(LT+['80_100']).astype(int); d2=d2.groupby(['fy','tg','post']).n.sum().reset_index()
P('   区分を100h未満 vs 100h以上に変更:', rr2(d2))

# ---- D. 精神 区分内比較（FY2017-2025のみ公表）----
mo=pd.read_csv(D+'mental_overtime_bands.csv')
mo['g']=mo.band.map({'lt20':'lt80','20_40':'lt80','40_60':'lt80','60_80':'lt80','other':'oth'}).fillna('ge80')
M=mo.groupby(['fy','g']).n.sum().unstack()
M['調査せず割合%']=(100*M.oth/M[['lt80','ge80','oth']].sum(1)).round(1)
P('\n-- D. 精神 支給決定の時間外労働区分（1か月平均）'); P(M.to_string())
for a,b,lab in [((2017,2019),(2020,2022),'2020年改正'),((2020,2022),(2024,2025),'2023年改正')]:
    P(f'   {lab} 年平均 前FY{a[0]}-{a[1]}:', M.loc[a[0]:a[1],['ge80','lt80','oth']].mean().round(1).to_dict(), f' 後FY{b[0]}-{b[1]}:', M.loc[b[0]:b[1],['ge80','lt80','oth']].mean().round(1).to_dict())
L=mo[mo.fy!=2023].groupby(['fy','g']).n.sum().reset_index()
L['p20']=L.fy.between(2020,2022).astype(int)+0; L['p24']=(L.fy>=2024).astype(int)
L['s20']=(L.fy>=2020).astype(int)
for tg,ref,lab in [('oth','ge80','調査せず/80h以上'),('lt80','ge80','80h未満/80h以上')]:
    d=L[L.g.isin([tg,ref])].copy(); d['tg']=(d.g==tg).astype(int)
    m=smf.glm('n ~ C(fy)+tg+tg:s20+tg:p24',data=d,family=sm.families.Poisson()).fit(scale='X2')
    P(f'   {lab}: 2020年改正 {ci(m,"tg:s20")}、2023年改正（追加の変化）{ci(m,"tg:p24")}')
open(O+'results_v3_unified.txt','w').write('\n'.join(out)); print('done')

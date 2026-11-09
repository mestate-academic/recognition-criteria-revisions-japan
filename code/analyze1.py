# -*- coding: utf-8 -*-
"""予備解析 v1：認定基準改正（脳・心 2021年9月、精神 2011年12月・2020年5月・2023年9月）と認定動向。
A 分解（請求・決定・支給決定・認定率）／B 認定率と請求のITS／C 脳・心の時間外労働区分別（改正の標的 vs 非標的）
D 精神の「労働時間を調査するまでもなく認定」区分／E・F 業種別DiD（探索的）
"""
import pandas as pd, numpy as np, statsmodels.api as sm, statsmodels.formula.api as smf
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
for f in fm.findSystemFonts():
    if 'NotoSansCJK-Regular' in f: fm.fontManager.addfont(f); plt.rcParams['font.family']=fm.FontProperties(fname=f).get_name()
D='data/'; O='output/'
out=[]
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.append(s)

cvd=pd.read_csv(D+'cvd_national.csv'); mn=pd.read_csv(D+'mental_national.csv')
cvd['rate']=cvd.approvals/cvd.decisions; mn['rate']=mn.approvals/mn.decisions

# ---------- A. 分解 ----------
def window(df,a,b): return df[(df.fy>=a)&(df.fy<=b)]
def summ(df,label,pre,post):
    r=[]
    for nm,(a,b) in [('前',pre),('後',post)]:
        w=window(df,a,b)
        r.append(dict(改正=label,期間=f'{nm} FY{a}-{b}',請求=w.claims.mean(),決定=w.decisions.mean(),支給決定=w.approvals.mean(),
                      認定率=100*w.approvals.sum()/w.decisions.sum(),請求に対する支給決定=100*w.approvals.sum()/w.claims.sum()))
    return r
A=[]
A+=summ(cvd,'脳・心 2021年9月',(2014,2020),(2022,2025))
A+=summ(mn,'精神 2011年12月',(2009,2011),(2012,2014))
A+=summ(mn,'精神 2020年5月',(2017,2019),(2020,2022))
A+=summ(mn,'精神 2023年9月',(2020,2022),(2024,2025))
A=pd.DataFrame(A).round(1); A.to_csv(O+'A_decomposition.csv',index=False,encoding='utf-8-sig')
P('== A. 年平均（請求・決定・支給決定）と認定率（決定に占める支給決定、%）'); P(A.to_string(index=False))

# ---------- B. ITS ----------
def its_rate(df, steps, years, trans=None, label=''):
    d=df[df.fy.between(*years)].dropna(subset=['decisions']).copy()
    d['t']=d.fy-d.fy.min()
    for k,(nm,y0) in enumerate(steps): d[nm]=(d.fy>=y0).astype(float)
    if trans:  # 移行年は除外
        d=d[~d.fy.isin(trans)]
    X=sm.add_constant(d[['t']+[s for s,_ in steps]])
    m=sm.GLM(d.approvals/d.decisions,X,family=sm.families.Binomial(),var_weights=d.decisions).fit(scale='X2')
    mc=sm.GLM(d.claims,sm.add_constant(d[['t']+[s for s,_ in steps]]),family=sm.families.Poisson()).fit(scale='X2')
    ma=sm.GLM(d.approvals,sm.add_constant(d[['t']+[s for s,_ in steps]]),family=sm.families.Poisson()).fit(scale='X2')
    P(f'-- {label}（FY{years[0]}-{years[1]}、移行年除外={trans}、準尤度：過分散を補正）')
    for s,_ in steps:
        for nm,mm,eff in [('認定率 OR',m,'OR'),('請求 RR',mc,'RR'),('支給決定 RR',ma,'RR')]:
            b=mm.params[s]; ci=mm.conf_int().loc[s]
            P(f'   {s}: {nm} {np.exp(b):.2f} ({np.exp(ci[0]):.2f}-{np.exp(ci[1]):.2f}) p={mm.pvalues[s]:.3f}')
    P(f'   trend/年: 認定率OR {np.exp(m.params["t"]):.3f}, 請求RR {np.exp(mc.params["t"]):.3f}, 分散φ(認定率)={m.scale:.1f}')
    return m
P('\n== B. 分断時系列（ITS）：水準変化（level change）、共通の線形トレンド')
its_rate(cvd,[('step2021',2022)],(2014,2025),trans=[2021],label='脳・心 2021年改正')
its_rate(cvd,[('step2021',2022)],(2008,2025),trans=[2021],label='脳・心 2021年改正（FY2008-、決定件数を延長）')
its_rate(mn,[('step2012',2012),('step2020',2020),('step2024',2024)],(2009,2025),trans=[2023],label='精神 3改正同時モデル')
its_rate(mn,[('step2024',2024)],(2016,2025),trans=[2023],label='精神 2023年改正のみ（FY2016-）')

# ---------- C. 脳・心 時間外労働区分 ----------
ot=pd.read_csv(D+'cvd_overtime_bands.csv'); oc=ot[ot.period=='combined']
grp={'lt45':'80h未満','45_60':'80h未満','60_80':'80h未満','other':'短期・異常な出来事'}
oc=oc.assign(g=oc.band.map(grp).fillna('80h以上'))
G=oc.groupby(['fy','g']).n.sum().unstack(); G['合計']=G.sum(1); G['80h未満の割合%']=(100*G['80h未満']/G['合計']).round(1)
P('\n== C. 脳・心 支給決定の時間外労働区分（評価期間合算）'); P(G.to_string())
G.to_csv(O+'C_cvd_bands.csv',encoding='utf-8-sig')
# 1か月100h未満または2-6か月80h未満（改正の標的＝基準未満）を評価期間別表で
sep=ot[ot.period.isin(['m1','m26'])]
def below(y):
    s=sep[sep.fy==y]; m1=s[(s.period=='m1')&s.band.isin(['lt45','45_60','60_80','80_100'])].n.sum()
    m26=s[(s.period=='m26')&s.band.isin(['lt45','45_60','60_80'])].n.sum(); return m1+m26
P('基準未満（1か月100h未満 or 2-6か月80h未満）の支給決定：'+', '.join(f'FY{y} {below(y)}/{int(cvd.set_index("fy").approvals[y])} ({100*below(y)/cvd.set_index("fy").approvals[y]:.1f}%)' for y in [2017,2018,2019,2020,2021,2022,2023,2024,2025]))
# Poisson：年固定効果＋群固定効果＋群×改正後（80h未満 vs 80h以上）
d=oc[(oc.g!='短期・異常な出来事')&(oc.fy!=2021)].groupby(['fy','g']).n.sum().reset_index()  # FY2021は移行年
d['post']=(d.fy>=2022).astype(int); d['tg']=(d.g=='80h未満').astype(int); d['t']=d.fy-2007
m=smf.glm('n ~ C(fy) + tg + tg:post',data=d,family=sm.families.Poisson()).fit(scale='X2')
m2=smf.glm('n ~ C(fy) + tg + tg:t + tg:post',data=d,family=sm.families.Poisson()).fit(scale='X2')
for nm,mm in [('群別トレンドなし',m),('群別線形トレンドあり',m2)]:
    b=mm.params['tg:post']; ci=mm.conf_int().loc['tg:post']
    P(f'C. 80h未満/80h以上 の比の変化（改正後FY2022-25 vs FY2007-20）[{nm}]: RR {np.exp(b):.2f} ({np.exp(ci[0]):.2f}-{np.exp(ci[1]):.2f}) p={mm.pvalues["tg:post"]:.4f}')
# 群別の水準（年平均）
for g in ['80h未満','80h以上','短期・異常な出来事']:
    pre=G.loc[2007:2020,g]; pre2=G.loc[2015:2020,g]; post=G.loc[2022:2025,g]
    P(f'   {g}: FY2007-20平均 {pre.mean():.1f}, FY2015-20平均 {pre2.mean():.1f} → FY2022-25平均 {post.mean():.1f}')

# ---------- D. 精神 時間外労働区分 ----------
mo=pd.read_csv(D+'mental_overtime_bands.csv')
mg={'other':'その他（労働時間を調査せず認定）','80_100':'80h以上','100_120':'80h以上','120_140':'80h以上','140_160':'80h以上','ge160':'80h以上'}
mo['g']=mo.band.map(mg).fillna('80h未満')
M=mo.groupby(['fy','g']).n.sum().unstack(); M['合計']=M.sum(1); M['その他の割合%']=(100*M['その他（労働時間を調査せず認定）']/M['合計']).round(1)
P('\n== D. 精神 支給決定の時間外労働区分（1か月平均）'); P(M.to_string()); M.to_csv(O+'D_mental_bands.csv',encoding='utf-8-sig')

# ---------- E. 業種別DiD（脳・心 2021：運輸 vs その他、FY2016-2023、2024年上限規制前） ----------
ci_=pd.read_csv(D+'rosai_cvd_by_industry.csv'); emp=pd.read_csv(D+'employment_by_industry.csv')
tot=ci_[ci_.industry=='合計'].set_index('fy'); tr=ci_[ci_.industry=='運輸業郵便業'].set_index('fy')
e=pd.DataFrame({'fy':tot.index})
dd=pd.concat([pd.DataFrame(dict(fy=tot.index,grp='運輸',appr=tr.cvd_approvals.values,claims=tr.cvd_claims.values)),
              pd.DataFrame(dict(fy=tot.index,grp='その他',appr=(tot.cvd_approvals-tr.cvd_approvals).values,claims=(tot.cvd_claims-tr.cvd_claims).values))])
dd=dd[dd.fy.between(2016,2023)&(dd.fy!=2021)]; dd['post']=(dd.fy>=2022).astype(int); dd['T']=(dd.grp=='運輸').astype(int)
for y in ['appr','claims']:
    mm=smf.glm(f'{y} ~ C(fy) + T + T:post',data=dd,family=sm.families.Poisson()).fit(scale='X2')
    b=mm.params['T:post']; c=mm.conf_int().loc['T:post']
    P(f'\nE. 脳・心 運輸 vs その他（FY2016-20 vs FY2022-23）{y}: RR {np.exp(b):.2f} ({np.exp(c[0]):.2f}-{np.exp(c[1]):.2f}) p={mm.pvalues["T:post"]:.3f}')

# ---------- F. 業種別DiD（精神 2023：顧客接点の多い業種 vs 少ない業種） ----------
mi=pd.read_csv(D+'rosai_mental_by_industry.csv')
hi=['卸売小売業','宿泊飲食','医療福祉','教育学習支援業']; lo=['製造業','情報通信業','金融保険業']
f=mi[mi.industry.isin(hi+lo)&mi.fy.between(2016,2025)].copy(); f['T']=f.industry.isin(hi).astype(int)
ec={i:i for i in hi+lo}
em=emp.set_index('year')
f['emp']=[em.loc[y,ec[i]] if ec[i] in em.columns else np.nan for y,i in zip(f.fy,f.industry)]
P('\nF. 精神 業種：雇用者列の有無', f.emp.isna().sum()==0)
f=f[f.fy!=2023]; f['post']=(f.fy>=2024).astype(int)
for y in ['approvals','claims']:
    g=f.dropna(subset=[y])
    mm=smf.glm(f'{y} ~ C(fy) + C(industry) + T:post',data=g,family=sm.families.Poisson(),offset=np.log(g.emp)).fit(scale='X2')
    b=mm.params['T:post']; c=mm.conf_int().loc['T:post']
    P(f'F. 精神 顧客接点業種 vs 低接点業種（FY2016-22 vs FY2024-25）{y}: RR {np.exp(b):.2f} ({np.exp(c[0]):.2f}-{np.exp(c[1]):.2f})［準ポアソン、7業種のため参考］')

open(O+'results_v1.txt','w').write('\n'.join(out))

# ---------- 図 ----------
fig,ax=plt.subplots(2,2,figsize=(13,9))
a=ax[0,0]; c=cvd[cvd.fy>=2002]
a.plot(c.fy,c.claims,'o-',label='請求'); a.plot(c.fy,c.decisions,'s-',label='決定'); a.plot(c.fy,c.approvals,'^-',label='支給決定')
a.axvline(2021.45,ls='--',c='k'); a.text(2021.6,1150,'2021.9 改正',fontsize=11); a.axvline(2001.95,ls=':',c='gray')
a.set_title('A 脳・心臓疾患：請求・決定・支給決定',fontsize=13); a.legend(fontsize=11,loc='center left'); a.set_ylabel('件')
a=ax[0,1]; Gp=G.reindex(range(2007,2026))
a.bar(Gp.index,Gp['80h以上'],label='80h以上',color='#4C72B0'); a.bar(Gp.index,Gp['80h未満'],bottom=Gp['80h以上'],label='80h未満（改正の主な標的）',color='#DD8452')
a.bar(Gp.index,Gp['短期・異常な出来事'],bottom=Gp['80h以上']+Gp['80h未満'],label='短期の過重業務・異常な出来事',color='#999999')
a.axvline(2021.45,ls='--',c='k')
a.set_title('B 脳・心臓疾患：支給決定の時間外労働区分',fontsize=13); a.legend(fontsize=10)
a=ax[1,0]; m=mn[mn.fy>=2002]
a.plot(m.fy,m.claims,'o-',label='請求'); a.plot(m.fy,m.decisions,'s-',label='決定'); a.plot(m.fy,m.approvals,'^-',label='支給決定')
for x,t in [(2009.0,'2009.4'),(2011.7,'2011.12'),(2020.1,'2020.5'),(2023.4,'2023.9')]: a.axvline(x,ls='--',c='k'); a.text(x+0.1,4600,t,fontsize=10)
a.set_title('C 精神障害：請求・決定・支給決定',fontsize=13); a.legend(fontsize=11,loc='center left'); a.set_ylabel('件')
a=ax[1,1]
a.plot(cvd.fy,100*cvd.rate,'o-',label='脳・心臓疾患'); a.plot(mn.fy,100*mn.rate,'s-',label='精神障害')
a.plot(mn.fy,100*mn.approvals_suicide/mn.decisions_suicide,'^:',label='精神障害（うち自殺）')
a.set_ylim(20,55); a.set_title('D 認定率（決定に占める支給決定）',fontsize=13); a.set_ylabel('%'); a.legend(fontsize=11)
for x in [2021.45]: a.axvline(x,ls='--',c='C0')
for x in [2011.7,2020.1,2023.4]: a.axvline(x,ls='--',c='C1')
from matplotlib.ticker import MaxNLocator
for a in ax.flat: a.tick_params(labelsize=11); a.set_xlabel('年度',fontsize=11); a.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.tight_layout(); plt.savefig(O+'Figure1_trends.png',dpi=150)
print('saved')

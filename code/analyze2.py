# -*- coding: utf-8 -*-
"""予備解析 v2：推論の強化と病型別の比較
G 病型別（脳血管疾患 vs 虚血性心疾患等；2021年改正で「重篤な心不全」を追加）
H 脳・心 時間外区分の比（80h未満/80h以上）の頑健性：正確な置換検定、時間プラセボ、期間・区分定義の変更
I 精神 ITS の感度分析：窓、移行年の扱い、トレンド、HAC、プラセボ改正年
J 精神2023 業種DiD の小クラスター推論：ワイルド・クラスター・スコア・ブートストラップ（Webb）、置換（35通り）
"""
import pandas as pd, numpy as np, statsmodels.api as sm, statsmodels.formula.api as smf, itertools
from scipy import stats
D='data/'; O='output/'
out=[]
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.append(s)
rng=np.random.default_rng(20261109)
ex=lambda b: np.exp(b)

cvd=pd.read_csv(D+'cvd_national.csv'); mn=pd.read_csv(D+'mental_national.csv')

# ================= G. 病型別 =================
dt=pd.read_csv(D+'cvd_by_type.csv')
pv=dt.pivot(index='fy',columns='type',values='approvals')
pv['心疾患の割合%']=(100*pv['虚血性心疾患等']/(pv.sum(1))).round(1)
P('== G. 病型別 支給決定（FY2021は白書から、移行年として比の推定から除外）'); P(pv.to_string())
g=dt[(dt.fy>=2007)&(dt.fy!=2021)].copy(); g['post']=(g.fy>=2022).astype(int); g['h']=(g.type=='虚血性心疾患等').astype(int); g['t']=g.fy-2007
for nm,f in [('年固定効果',"approvals ~ C(fy) + h + h:post"),('＋病型別トレンド',"approvals ~ C(fy) + h + h:t + h:post")]:
    m=smf.glm(f,data=g,family=sm.families.Poisson()).fit(scale='X2')
    P(f'G. 心疾患/脳血管 の比の変化（FY2022-25 vs FY2007-20）[{nm}]: RR {ex(m.params["h:post"]):.2f} ({ex(m.conf_int().loc["h:post",0]):.2f}-{ex(m.conf_int().loc["h:post",1]):.2f}) p={m.pvalues["h:post"]:.3f}')
post=dt[dt.fy>=2022].copy(); post['rate']=(100*post.approvals/post.decisions).round(1); post['death_share_claims']=(100*post.claims_death/post.claims).round(1)
P('改正後の病型別 請求・決定・支給決定・認定率：'); P(post[['fy','type','claims','decisions','approvals','rate','claims_death']].to_string(index=False))
for t in ['脳血管疾患','虚血性心疾患等']:
    a=post[post.type==t]; c=a[a.fy==2025].claims.iloc[0]/a[a.fy==2022].claims.iloc[0]
    P(f'   {t}: 請求 FY2022→2025 {c:.2f}倍、支給決定 {a[a.fy==2022].approvals.iloc[0]}→{a[a.fy==2025].approvals.iloc[0]}')

# ================= H. 脳・心 区分比の頑健性 =================
ot=pd.read_csv(D+'cvd_overtime_bands.csv'); oc=ot[ot.period=='combined'].copy()
oc['g']=oc.band.map({'lt45':'lt80','45_60':'lt80','60_80':'lt80','other':'oth'}).fillna('ge80')
W=oc.groupby(['fy','g']).n.sum().unstack()
W=W[W.index!=2021]  # 移行年除外
W['lr']=np.log(W.lt80/W.ge80); yrs=W.index.values; post_mask=yrs>=2022
obs=W.lr[post_mask].mean()-W.lr[~post_mask].mean()
# 正確な置換検定：17年から「改正後」4年を選ぶ全組合せ
diffs=[]
for c in itertools.combinations(range(len(yrs)),post_mask.sum()):
    m=np.zeros(len(yrs),bool); m[list(c)]=True; diffs.append(W.lr[m].mean()-W.lr[~m].mean())
diffs=np.array(diffs); p_perm=np.mean(diffs>=obs-1e-12)
P(f'\n== H. 80h未満/80h以上 の対数比：改正後−改正前 = {obs:.2f}（比 {ex(obs):.2f}倍）、正確な置換検定 p={p_perm:.4f}（{len(diffs)}通り中 {int((diffs>=obs-1e-12).sum())}通り）')
# 時間プラセボ：改正前データだけで、偽の「改正後」4年間を置いた推定
pre=oc[(oc.fy<=2020)&(oc.g!='oth')].groupby(['fy','g']).n.sum().reset_index(); pre['tg']=(pre.g=='lt80').astype(int)
pl=[]
for k in range(2010,2018):
    d=pre.copy(); d['post']=(d.fy>=k).astype(int)*(d.fy<=k+3)
    d=d[d.fy<=k+3]
    m=smf.glm('n ~ C(fy)+tg+tg:post',data=d,family=sm.families.Poisson()).fit(scale='X2'); pl.append((k,ex(m.params['tg:post'])))
P('   時間プラセボ（改正前の各4年間を偽の改正後とした比の変化）：'+', '.join(f'FY{k}-{k+3}: {r:.2f}' for k,r in pl))
# 期間・定義の変更
dd=oc[(oc.g!='oth')&(oc.fy!=2021)].groupby(['fy','g']).n.sum().reset_index(); dd['tg']=(dd.g=='lt80').astype(int); dd['post']=(dd.fy>=2022).astype(int); dd['t']=dd.fy-2007
def rr(d,f='n ~ C(fy)+tg+tg:post'):
    m=smf.glm(f,data=d,family=sm.families.Poisson()).fit(scale='X2'); c=m.conf_int().loc['tg:post']
    return f'{ex(m.params["tg:post"]):.2f} ({ex(c[0]):.2f}-{ex(c[1]):.2f})'
P('   改正前をFY2015-20に限定：', rr(dd[(dd.fy>=2015)]))
P('   FY2020（COVID-19）を除外：', rr(dd[dd.fy!=2020]))
P('   FY2013（80h未満31件の外れ値）を除外：', rr(dd[dd.fy!=2013]))
P('   FY2022（改正直後で80h未満が最多）を除外：', rr(dd[dd.fy!=2022]))
# 区分の定義を変える：60h未満 vs 60h以上 は標的外の確認（ほぼ0件）/ 「80-100h」も含めて100h未満 vs 100h以上
oc2=ot[ot.period=='combined'].copy(); oc2=oc2[(oc2.band!='other')&(oc2.fy!=2021)]
oc2['tg']=oc2.band.isin(['lt45','45_60','60_80','80_100']).astype(int)
d2=oc2.groupby(['fy','tg']).n.sum().reset_index(); d2['post']=(d2.fy>=2022).astype(int)
P('   区分を100h未満 vs 100h以上に変更：', rr(d2))
# 80-100h だけを標的とした場合（1か月評価で基準未満を含む帯）
oc3=oc2[oc2.band.isin(['80_100','100_120','120_140','140_160','ge160'])].copy(); oc3['tg']=(oc3.band=='80_100').astype(int)
d3=oc3.groupby(['fy','tg']).n.sum().reset_index(); d3['post']=(d3.fy>=2022).astype(int)
P('   80-100h帯 vs 100h以上（80h未満を除く）：', rr(d3))
# 「短期の過重業務・異常な出来事」（改正で判断基準を明確化）vs 80h以上
oc4=oc[(oc.g!='lt80')&(oc.fy!=2021)].groupby(['fy','g']).n.sum().reset_index(); oc4['tg']=(oc4.g=='oth').astype(int); oc4['post']=(oc4.fy>=2022).astype(int)
P('   短期・異常な出来事 vs 80h以上：', rr(oc4))

# ================= I. 精神 ITS 感度分析 =================
def its(df,steps,years,trans=(),code05=False,trend=True,slope=None):
    d=df[df.fy.between(*years)].dropna(subset=['decisions']).copy(); d['t']=d.fy-d.fy.min()
    cols=['t'] if trend else []
    for nm,y0 in steps:
        d[nm]=(d.fy>=y0).astype(float)
        if code05 and nm=='s2024': d.loc[d.fy==2023,nm]=0.5
        cols.append(nm)
    if slope:
        d['sl']=np.clip(d.fy-slope+1,0,None); cols.append('sl')
    d=d[~d.fy.isin(trans)]
    X=sm.add_constant(d[cols])
    rate=sm.GLM(d.approvals/d.decisions,X,family=sm.families.Binomial(),var_weights=d.decisions).fit(scale='X2')
    cl=sm.GLM(d.claims,X,family=sm.families.Poisson()).fit(scale='X2')
    ap=sm.GLM(d.approvals,X,family=sm.families.Poisson()).fit(scale='X2')
    return rate,cl,ap
def fmt(m,s): c=m.conf_int().loc[s]; return f'{ex(m.params[s]):.2f} ({ex(c[0]):.2f}-{ex(c[1]):.2f})'
P('\n== I. 精神 2023年改正の水準変化（請求RR／支給決定RR／認定率OR）')
specs=[('主解析：FY2009-25、3改正、FY2023除外',dict(steps=[('s2012',2012),('s2020',2020),('s2024',2024)],years=(2009,2025),trans=(2023,))),
       ('FY2023を0.5（半年分）として含める',dict(steps=[('s2012',2012),('s2020',2020),('s2024',2024)],years=(2009,2025),code05=True)),
       ('FY2023を改正後に含める（s2024をFY2023から）',dict(steps=[('s2012',2012),('s2020',2020),('s2024',2023)],years=(2009,2025))),
       ('窓 FY2012-25（2012改正は除く）',dict(steps=[('s2020',2020),('s2024',2024)],years=(2012,2025),trans=(2023,))),
       ('窓 FY2016-25、2023改正のみ',dict(steps=[('s2024',2024)],years=(2016,2025),trans=(2023,))),
       ('トレンドなし（前後比較）FY2020-25',dict(steps=[('s2024',2024)],years=(2020,2025),trans=(2023,),trend=False)),
       ('2020年以降の傾き変化を追加',dict(steps=[('s2012',2012),('s2020',2020),('s2024',2024)],years=(2009,2025),trans=(2023,),slope=2020))]
for nm,kw in specs:
    r,c,a=its(mn,**kw); P(f'   {nm}: 請求 {fmt(c,"s2024")}／支給決定 {fmt(a,"s2024")}／認定率 {fmt(r,"s2024")}')
# HAC（Newey-West, lag1）：対数件数のOLS
d=mn[mn.fy.between(2009,2025)&(mn.fy!=2023)].copy(); d['t']=d.fy-2009
for nm,y0 in [('s2012',2012),('s2020',2020),('s2024',2024)]: d[nm]=(d.fy>=y0).astype(float)
for y in ['claims','approvals']:
    m=smf.ols(f'np.log({y}) ~ t+s2012+s2020+s2024',data=d).fit(cov_type='HAC',cov_kwds={'maxlags':1})
    P(f'   HAC(lag1) OLS log {y}: 2012 {fmt(m,"s2012")}, 2020 {fmt(m,"s2020")}, 2024 {fmt(m,"s2024")}')
m=smf.ols('np.log(approvals/(decisions-approvals)) ~ t+s2012+s2020+s2024',data=d).fit(cov_type='HAC',cov_kwds={'maxlags':1})
P(f'   HAC(lag1) OLS 認定率のロジット: 2012 {fmt(m,"s2012")}, 2020 {fmt(m,"s2020")}, 2024 {fmt(m,"s2024")}')
# プラセボ改正年：改正のない年に偽の段差を置く（FY2009-2019、2012改正は投入）
pz=[]
for k in range(2014,2020):
    r,c,a=its(mn,steps=[('s2012',2012),('pk',k)],years=(2009,2019))
    pz.append((k,ex(c.params['pk']),ex(a.params['pk']),ex(r.params['pk'])))
P('   プラセボ改正年（FY2014-19、偽の段差）請求RR/支給決定RR/認定率OR：'+'; '.join(f'FY{k}: {x:.2f}/{y:.2f}/{z:.2f}' for k,x,y,z in pz))
# 脳・心 2021年 認定率の感度分析
P('\n== I2. 脳・心 2021年改正 認定率')
for nm,kw in [('FY2008-25 線形トレンド（決定件数を延長）',dict(years=(2008,2025),trans=(2021,))),('FY2008-25 トレンドなし',dict(years=(2008,2025),trans=(2021,),trend=False)),('主解析 FY2014-25 線形トレンド',dict(years=(2014,2025),trans=(2021,))),('トレンドなし（前後比較）',dict(years=(2014,2025),trans=(2021,),trend=False)),
              ('窓 FY2017-25 線形トレンド',dict(years=(2017,2025),trans=(2021,)))]:
    r,c,a=its(cvd,steps=[('s2022',2022)],**kw); P(f'   {nm}: 請求 {fmt(c,"s2022")}／支給決定 {fmt(a,"s2022")}／認定率 {fmt(r,"s2022")}')

# ================= J. 業種DiD 小クラスター推論 =================
mi=pd.read_csv(D+'rosai_mental_by_industry.csv'); emp=pd.read_csv(D+'employment_by_industry.csv').set_index('year')
hi=['卸売小売業','宿泊飲食','医療福祉','教育学習支援業']; lo=['製造業','情報通信業','金融保険業']; inds=hi+lo
f=mi[mi.industry.isin(inds)&mi.fy.between(2016,2025)&(mi.fy!=2023)].copy()
f['emp']=[emp.loc[y,i] for y,i in zip(f.fy,f.industry)]; f['post']=(f.fy>=2024).astype(int); f['tr']=f.industry.isin(hi).astype(int)
WEBB=np.array([-np.sqrt(1.5),-1,-np.sqrt(.5),np.sqrt(.5),1,np.sqrt(1.5)])
Wb=rng.choice(WEBB,size=(9999,len(inds)))
def X_of(df):
    X=pd.get_dummies(df[['industry','fy']].astype(str),drop_first=True).astype(float); X.insert(0,'const',1.0)
    X['D']=(df.tr*df.post).values.astype(float); return X.values,list(X.columns)
def scores(df,y,b0):
    X,cols=X_of(df); j=cols.index('D'); Xg=np.delete(X,j,axis=1)
    r=sm.GLM(df[y].values,Xg,family=sm.families.Poisson(),offset=np.log(df.emp.values)+b0*X[:,j]).fit()
    mu=r.mu; res=df[y].values-mu; H=(X*mu[:,None]).T@X; jo=[k for k in range(X.shape[1]) if k!=j]
    proj=H[j,jo]@np.linalg.pinv(H[np.ix_(jo,jo)]); gidx=pd.factorize(df.industry)[0]
    return np.array([ (X[gidx==k].T@res[gidx==k])[j]-proj@(X[gidx==k].T@res[gidx==k])[jo] for k in range(gidx.max()+1)])
def wp(df,y,b0):
    s=scores(df,y,b0); T=s.sum()/np.sqrt((s**2).sum()); Ws=Wb*s; Ts=Ws.sum(1)/np.sqrt((Ws**2).sum(1))
    return np.mean(np.abs(Ts)>=abs(T)-1e-12)
P('\n== J. 精神2023 顧客接点業種 vs 低接点業種（7業種、FY2016-22 vs FY2024-25）')
for y in ['approvals','claims']:
    g=f.dropna(subset=[y]).reset_index(drop=True)
    m=smf.glm(f'{y} ~ C(industry)+C(fy)+tr:post',data=g,family=sm.families.Poisson(),offset=np.log(g.emp)).fit()
    b=m.params['tr:post']
    mc=smf.glm(f'{y} ~ C(industry)+C(fy)+tr:post',data=g,family=sm.families.Poisson(),offset=np.log(g.emp)).fit(cov_type='cluster',cov_kwds={'groups':pd.factorize(g.industry)[0]})
    se=mc.bse['tr:post']; tc=stats.t.ppf(.975,6)
    grid=np.linspace(b-0.8,b+0.8,161); acc=[x for x in grid if wp(g,y,x)>0.05]
    # 置換：7業種から4業種を「顧客接点」とする35通り
    def bfor(S):
        z=g.assign(tt=g.industry.isin(S).astype(int)*g.post)
        return smf.glm(f'{y} ~ C(industry)+C(fy)+tt',data=z,family=sm.families.Poisson(),offset=np.log(z.emp)).fit().params['tt']
    bs=np.array([bfor(set(c)) for c in itertools.combinations(inds,4)])
    rank=int((bs>=b-1e-12).sum())
    P(f'   {y}: RR {ex(b):.2f}; CR1 t(6) {ex(b-tc*se):.2f}-{ex(b+tc*se):.2f}; ワイルド・スコア・ブートストラップ p={wp(g,y,0.0):.3f}, 95%CI {ex(min(acc)):.2f}-{ex(max(acc)):.2f}; 置換35通り中 実際以上 {rank}通り（片側p={rank/35:.3f}）')

open(O+'results_v2.txt','w').write('\n'.join(out)); print('done')

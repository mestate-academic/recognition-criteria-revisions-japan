# -*- coding: utf-8 -*-
"""AJIM英文原稿用の図（Figure 1-3, English labels）。色：dataviz既定パレット（青#2a78d6・橙#eb6834、検証済み）＋灰色（その他）"""
import pandas as pd, numpy as np, itertools, statsmodels.api as sm, statsmodels.formula.api as smf
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.ticker import MaxNLocator
for f in fm.findSystemFonts():
    if 'NotoSansCJK-Regular' in f: fm.fontManager.addfont(f); plt.rcParams['font.family']=fm.FontProperties(fname=f).get_name()
plt.rcParams.update({'font.size':14,'axes.titlesize':16,'axes.labelsize':14,'xtick.labelsize':13,'ytick.labelsize':13,'legend.fontsize':13,
                     'axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,'grid.color':'#e6e6e6','grid.linewidth':0.8,'axes.axisbelow':True})
BLUE,ORANGE,GRAY,INK='#2a78d6','#eb6834','#9a9a9a','#333333'
D='data/'; O='output/'; S=2009  # 全図の起点をFY2009に統一
AQUA='#1baf7a'
cvd=pd.read_csv(D+'cvd_national.csv'); mn=pd.read_csv(D+'mental_national.csv'); pt=pd.read_csv(D+'mental_processing_time.csv')
ot=pd.read_csv(D+'cvd_overtime_bands.csv'); oc=ot[(ot.period=='combined')&(ot.fy>=S)].copy()
oc['g']=oc.band.map({'lt45':'lt80','45_60':'lt80','60_80':'lt80','other':'oth'}).fillna('ge80')
G=oc.groupby(['fy','g']).n.sum().unstack().reindex(range(S,2026))
def rev(ax,x,label=None,y=None):
    ax.axvline(x,ls='--',lw=1.2,c=INK)
    if label: ax.text(x+0.15,y,label,fontsize=12,color=INK,va='top')

# ---------- 図1 脳・心臓疾患 ----------
fig,ax=plt.subplots(1,2,figsize=(15,5.8))
a=ax[0]; x=G.index.values; w=0.78
a.bar(x,G.ge80,w,color=BLUE,label='≥80 h/month',edgecolor='white',linewidth=1)
a.bar(x,G.lt80,w,bottom=G.ge80,color=ORANGE,label='<80 h/month (target of revision)',edgecolor='white',linewidth=1)
a.bar(x,G.oth,w,bottom=G.ge80+G.lt80,color=AQUA,label='Short-term overload / extraordinary event',edgecolor='white',linewidth=1)
rev(a,2021.5,'Revision (Sep 2021)',412)
a.set_title('A  Approved claims by overtime category',loc='left'); a.set_ylabel('Approved claims'); a.set_ylim(0,425)
h,l=a.get_legend_handles_labels(); a.legend(h[::-1],l[::-1],loc='upper right',frameon=False,bbox_to_anchor=(1.0,0.92),fontsize=12); a.grid(axis='x',visible=False)
a=ax[1]; sh=100*G.lt80/G.sum(1)
a.plot(x,sh,'-',color=ORANGE,lw=2); a.plot(x,sh,'o',color=ORANGE,ms=8,mec='white',mew=1.5)
pre=sh.loc[S:2020].mean(); post=sh.loc[2022:2025].mean()
a.hlines(pre,S-0.4,2020.4,colors=INK,lw=1,linestyles=':'); a.text(S,2.3,f'Pre-revision mean {pre:.1f}%',fontsize=12,color=INK)
a.hlines(post,2021.6,2025.4,colors=INK,lw=1,linestyles=':'); a.text(2022.1,post-5.6,f'Post mean {post:.1f}%',fontsize=12,color=INK)
rev(a,2021.5)
a.set_title('B  Share of approvals with <80 h/month',loc='left'); a.set_ylabel('%'); a.set_ylim(0,32)
for a in ax: a.set_xticks(range(2010,2026,2)); a.set_xlim(S-0.6,2025.6); a.set_xlabel('Fiscal year')
plt.tight_layout(); plt.savefig(O+'AJIM_Figure1.png',dpi=200); plt.close()

# ---------- 図2 精神障害 ----------
mo=pd.read_csv(D+'mental_overtime_bands.csv'); M=mo.groupby('fy').apply(lambda d: 100*d[d.band=='other'].n.sum()/d.n.sum())
fig,ax=plt.subplots(2,2,figsize=(15,10))
revs=[(2011.75,'2011.12'),(2020.15,'2020.5'),(2023.42,'2023.9')]
a=ax[0,0]; m=mn[mn.fy>=S]
for col,lab,c,mk in [('claims','Claims',BLUE,'o'),('decisions','Decisions',GRAY,'s'),('approvals','Approvals',ORANGE,'^')]:
    a.plot(m.fy,m[col],'-',color=c,lw=2); a.plot(m.fy,m[col],mk,color=c,ms=7,mec='white',mew=1.2,label=lab)
for xx,t in revs: rev(a,xx,t,5150)
a.set_title('A  Claims, decisions and approvals',loc='left'); a.set_ylabel('Number'); a.set_ylim(0,5300); a.legend(frameon=False,loc='center left')
a=ax[0,1]; r=100*m.approvals/m.decisions; rs=100*m.approvals_suicide/m.decisions_suicide
a.plot(m.fy,r,'-',color=ORANGE,lw=2); a.plot(m.fy,r,'o',color=ORANGE,ms=7,mec='white',mew=1.2,label='All approvals')
a.plot(m.fy,rs,'--',color=GRAY,lw=1.5); a.plot(m.fy,rs,'^',color=GRAY,ms=7,mec='white',mew=1.2,label='Suicide (incl. attempts)')
for xx,t in revs: rev(a,xx)
a.set_title('B  Approval rate (approvals / decisions)',loc='left'); a.set_ylabel('%'); a.set_ylim(20,52); a.legend(frameon=False,loc='lower left')
a=ax[1,0]
mo2=mo.copy(); mo2['g']=mo2.band.map({'lt20':'lt80','20_40':'lt80','40_60':'lt80','60_80':'lt80','other':'oth'}).fillna('ge80')
B=mo2.groupby(['fy','g']).n.sum().unstack(); xb=B.index.values
a.bar(xb,B.ge80,0.72,color=BLUE,label='≥80 h/month',edgecolor='white',linewidth=1)
a.bar(xb,B.lt80,0.72,bottom=B.ge80,color=ORANGE,label='<80 h/month',edgecolor='white',linewidth=1)
a.bar(xb,B.oth,0.72,bottom=B.ge80+B.lt80,color=AQUA,label='Approved without examining hours',edgecolor='white',linewidth=1)
for xx,v,tot in zip(xb,M.values,B.sum(1).values): a.text(xx,tot+18,f'{v:.0f}%',ha='center',fontsize=11,color=INK)
for xx,t in revs[1:]: rev(a,xx)
a.set_title('C  Approvals by monthly overtime category',loc='left'); a.set_ylabel('Approved claims'); a.set_ylim(0,1250); a.set_xlim(2016.4,2025.6)
h,l=a.get_legend_handles_labels(); a.legend(h[::-1],l[::-1],frameon=False,loc='upper left',fontsize=12); a.grid(axis='x',visible=False)
a=ax[1,1]; p=pt[pt.fy>=S]
a.plot(p.fy,p.days,'-',color=BLUE,lw=2); a.plot(p.fy,p.days,'o',color=BLUE,ms=7,mec='white',mew=1.2)
a.axhline(240,color=INK,lw=1,ls=':'); a.text(2020.4,232,'Standard: 240 days',fontsize=12,color=INK)
for xx,t in revs: rev(a,xx)
a.set_title('D  Mean days from claim to decision',loc='left'); a.set_ylabel('Days'); a.set_ylim(180,300)
for a in ax.flat: a.xaxis.set_major_locator(MaxNLocator(integer=True)); a.set_xlabel('Fiscal year')
ax[1,1].set_xlim(S-0.5,2025.5); ax[0,0].set_xlim(2008.5,2025.5); ax[0,1].set_xlim(2008.5,2025.5)
plt.tight_layout(); plt.savefig(O+'AJIM_Figure2.png',dpi=200); plt.close()

# ---------- 図3 頑健性 ----------
W=oc[oc.fy!=2021].groupby(['fy','g']).n.sum().unstack(); W['lr']=np.log(W.lt80/W.ge80); yrs=W.index.values; pm=yrs>=2022
obs=W.lr[pm].mean()-W.lr[~pm].mean(); diffs=[]
for c in itertools.combinations(range(len(yrs)),pm.sum()):
    mm=np.zeros(len(yrs),bool); mm[list(c)]=True; diffs.append(W.lr[mm].mean()-W.lr[~mm].mean())
diffs=np.exp(np.array(diffs))
fig,ax=plt.subplots(1,2,figsize=(15,5.8),gridspec_kw={'width_ratios':[1,1.15]})
a=ax[0]; a.hist(diffs,bins=40,color=BLUE,edgecolor='white',linewidth=0.8)
a.axvline(np.exp(obs),color=ORANGE,lw=2.5); a.text(np.exp(obs)-0.08,a.get_ylim()[1]*0.85,f'Actual revision\n{np.exp(obs):.1f}-fold',ha='right',fontsize=13,color=INK)
a.set_title('A  Permutation test: all choices of four post years',loc='left',fontsize=15); a.set_xlabel('Change in ratio, <80 h : ≥80 h (fold)'); a.set_ylabel('Number of assignments')
a.text(np.exp(obs)-0.08,a.get_ylim()[1]*0.62,f'Largest of {len(diffs):,}\np = {np.mean(diffs>=np.exp(obs)-1e-12):.4f}',ha='right',fontsize=13,color=INK)
a=ax[1]
def rr(d,f='n ~ C(fy)+tg+tg:post'):
    m=smf.glm(f,data=d,family=sm.families.Poisson()).fit(scale='X2'); c=m.conf_int().loc['tg:post']; return np.exp([m.params['tg:post'],c[0],c[1]])
base=oc[oc.fy!=2021].copy(); base['post']=(base.fy>=2022).astype(int)
def mk(tg_bands,ref_bands):
    d=base[base.band.isin(tg_bands+ref_bands)].copy(); d['tg']=d.band.isin(tg_bands).astype(int)
    return rr(d.groupby(['fy','tg','post']).n.sum().reset_index())
dt=pd.read_csv(D+'cvd_by_type.csv'); g=dt[(dt.fy>=S)&(dt.fy!=2021)].copy(); g['post']=(g.fy>=2022).astype(int); g['tg']=(g.type=='虚血性心疾患等').astype(int); g['n']=g.approvals
hi80=['80_100','100_120','120_140','140_160','ge160']
rows=[('<80 h vs ≥80 h\n(target of revision)',mk(['lt45','45_60','60_80'],hi80)),
      ('Short-term/extraordinary vs ≥80 h\n(criteria clarified)',mk(['other'],hi80)),
      ('80–100 h vs ≥100 h\n(not targeted: specificity)',mk(['80_100'],['100_120','120_140','140_160','ge160'])),
      ('Cardiac vs cerebrovascular\n(severe heart failure added)',rr(g[['fy','tg','post','n']]))]
yy=np.arange(len(rows))[::-1]
for (lab,(e,l,h)),y in zip(rows,yy):
    c=ORANGE if l>1 else BLUE
    a.plot([l,h],[y,y],color=c,lw=2.5); a.plot(e,y,'o',color=c,ms=10,mec='white',mew=1.5)
    a.text(h*1.08,y,f'{e:.2f} ({l:.2f}–{h:.2f})',va='center',fontsize=13,color=INK)
a.axvline(1,color=INK,lw=1); a.set_xscale('log'); a.set_xlim(0.6,14); a.set_xticks([0.7,1,2,4,8]); a.set_xticklabels(['0.7','1','2','4','8'])
a.set_yticks(yy); a.set_yticklabels([r[0] for r in rows]); a.grid(axis='y',visible=False)
a.set_title('B  Ratio change, FY2022–25 vs FY2009–20',loc='left',fontsize=15); a.set_xlabel('Ratio change (log scale, 95% CI)')
plt.tight_layout(); plt.savefig(O+'AJIM_Figure3.png',dpi=200); plt.close()
print('figs done', np.exp(obs), [ (r[0].split()[0], np.round(r[1],2)) for r in rows])

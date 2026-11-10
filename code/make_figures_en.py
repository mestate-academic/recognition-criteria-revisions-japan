# -*- coding: utf-8 -*-
"""AJIM英文原稿用の図（Figure 1-3, English labels）。色：dataviz既定パレット（青#2a78d6・橙#eb6834、検証済み）＋灰色（その他）"""
import pandas as pd, numpy as np, itertools, statsmodels.api as sm, statsmodels.formula.api as smf
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.ticker import MaxNLocator
plt.rcParams['font.family']=['Liberation Sans','Arial','DejaVu Sans']  # Arial-compatible sans serif
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
a.bar(x,G.lt80,w,bottom=G.ge80,color=ORANGE,label='<80 h/month',edgecolor='white',linewidth=1)
a.bar(x,G.oth,w,bottom=G.ge80+G.lt80,color=AQUA,label='Short-term overload / extraordinary event',edgecolor='white',linewidth=1)
rev(a,2021.5,'Revision\n(Sep 2021)',465)
a.set_title('A  Approved claims by overtime category',loc='left'); a.set_ylabel('Approved claims'); a.set_ylim(0,475)
h,l=a.get_legend_handles_labels(); a.legend(h[::-1],l[::-1],loc='upper left',frameon=False,fontsize=12); a.grid(axis='x',visible=False)
a=ax[1]; sh=100*G.lt80/G.sum(1)
a.plot(x,sh,'-',color=ORANGE,lw=2); a.plot(x,sh,'o',color=ORANGE,ms=8,mec='white',mew=1.5)
pre=sh.loc[S:2020].mean(); post=sh.loc[2022:2025].mean()
a.hlines(pre,S-0.4,2020.4,colors=INK,lw=1,linestyles=':'); a.text(S,2.3,f'Pre-revision mean {pre:.1f}%',fontsize=12,color=INK)
a.hlines(post,2021.6,2025.4,colors=INK,lw=1,linestyles=':'); a.text(2022.4,post-3.9,f'Post-revision\nmean {post:.1f}%',fontsize=12,color=INK,va='top')
rev(a,2021.5)
a.set_title('B  Share of approvals with <80 h/month',loc='left'); a.set_ylabel('Share of approvals (%)'); a.set_ylim(0,32)
for a in ax: a.set_xticks(range(2010,2026,2)); a.set_xlim(S-0.6,2025.6); a.set_xlabel('Fiscal year')
plt.tight_layout(); plt.savefig(O+'AJIM_Figure1.png',dpi=200); plt.savefig(O+'AJIM_Figure1.tif',dpi=600,pil_kwargs={'compression':'tiff_lzw'}); plt.close()

# ---------- 図2 精神障害 ----------
mo=pd.read_csv(D+'mental_overtime_bands.csv'); M=mo.groupby('fy').apply(lambda d: 100*d[d.band=='other'].n.sum()/d.n.sum())
fig,ax=plt.subplots(2,2,figsize=(15,10))
revs=[(2011.75,'Dec 2011'),(2020.15,'May 2020'),(2023.42,'Sep 2023')]
a=ax[0,0]; m=mn[mn.fy>=S]
for col,lab,c,mk in [('claims','Claims',BLUE,'o'),('decisions','Decisions',GRAY,'s'),('approvals','Approvals',ORANGE,'^')]:
    a.plot(m.fy,m[col],'-',color=c,lw=2); a.plot(m.fy,m[col],mk,color=c,ms=7,mec='white',mew=1.2,label=lab)
for xx,t in revs: rev(a,xx,t,5650)
a.set_title('A  Claims, decisions and approvals',loc='left'); a.set_ylabel('Number'); a.set_ylim(0,5800); a.legend(frameon=False,loc='center left')
a=ax[0,1]; r=100*m.approvals/m.decisions; rs=100*m.approvals_suicide/m.decisions_suicide
a.plot(m.fy,r,'-',color=ORANGE,lw=2); a.plot(m.fy,r,'o',color=ORANGE,ms=7,mec='white',mew=1.2,label='All approvals')
a.plot(m.fy,rs,'--',color=GRAY,lw=1.5); a.plot(m.fy,rs,'^',color=GRAY,ms=7,mec='white',mew=1.2,label='Suicide (incl. attempts)')
for xx,t in revs: rev(a,xx)
a.set_title('B  Approval rate (approvals / decisions)',loc='left'); a.set_ylabel('Approval rate (%)'); a.set_ylim(20,52); a.legend(frameon=False,loc='lower left')
a=ax[1,0]
mo2=mo.copy(); mo2['g']=mo2.band.map({'lt20':'lt80','20_40':'lt80','40_60':'lt80','60_80':'lt80','other':'oth'}).fillna('ge80')
B=mo2.groupby(['fy','g']).n.sum().unstack(); xb=B.index.values
a.bar(xb,B.ge80,0.72,color=BLUE,label='≥80 h/month',edgecolor='white',linewidth=1)
a.bar(xb,B.lt80,0.72,bottom=B.ge80,color=ORANGE,label='<80 h/month',edgecolor='white',linewidth=1)
a.bar(xb,B.oth,0.72,bottom=B.ge80+B.lt80,color=AQUA,label='Approved without examining hours',edgecolor='white',linewidth=1)
for xx,v,tot in zip(xb,M.values,B.sum(1).values): a.text(xx,tot+18,f'{v:.0f}%',ha='center',fontsize=11,color=INK)
for xx in (2019.5,2023.5): a.plot([xx,xx],[0,1190],ls='--',lw=1.2,c=INK)  # between bars: revisions of May 2020 (start of FY2020) and Sep 2023 (FY2023 = transition year)
a.set_title('C  Approvals by monthly overtime category',loc='left'); a.set_ylabel('Approved claims'); a.set_ylim(0,1500); a.set_xlim(2016.4,2025.6)
h,l=a.get_legend_handles_labels(); lg=a.legend(h[::-1],l[::-1],frameon=False,loc='upper left',fontsize=12); a.grid(axis='x',visible=False)
a=ax[1,1]; p=pt[pt.fy>=S]
a.plot(p.fy,p.days,'-',color=BLUE,lw=2); a.plot(p.fy,p.days,'o',color=BLUE,ms=7,mec='white',mew=1.2)
a.axhline(240,color=INK,lw=1,ls=':'); a.text(2012.4,242,'Standard: 8 months (≈240 days)',fontsize=12,color=INK,va='bottom')
for xx,t in revs: rev(a,xx)
a.set_title('D  Mean days from claim to decision',loc='left'); a.set_ylabel('Days'); a.set_ylim(180,300)
for a in ax.flat: a.xaxis.set_major_locator(MaxNLocator(integer=True)); a.set_xlabel('Fiscal year')
ax[1,1].set_xlim(S-0.5,2025.5); ax[0,0].set_xlim(2008.5,2025.5); ax[0,1].set_xlim(2008.5,2025.5)
plt.tight_layout(); plt.savefig(O+'AJIM_Figure2.png',dpi=200); plt.savefig(O+'AJIM_Figure2.tif',dpi=600,pil_kwargs={'compression':'tiff_lzw'}); plt.close()

# ---------- 図3 評価期間別の構成と比の変化（v4：並べ替え検定のパネルは削除） ----------
def save(fig,name):
    fig.savefig(O+name+'.png',dpi=200)
    fig.savefig(O+name+'.tif',dpi=600,pil_kwargs={'compression':'tiff_lzw'})
fig=plt.figure(figsize=(15,11))
LO=['lt45','45_60','60_80']; HI=['100_120','120_140','140_160','ge160']
e=ot[(ot.fy>=2017)&ot.period.isin(['m1','m26'])].copy()
def grp(r):
    if r.period=='m1': return 'm1_lt100' if r.band in LO+['80_100'] else 'm1_ge100'
    return 'm26_80_100' if r.band=='80_100' else ('m26_lt80' if r.band in LO else 'm26_ge100')
e['g']=e.apply(grp,axis=1); T=e.groupby(['fy','g']).n.sum().unstack()
a=fig.add_axes([0.08,0.585,0.62,0.365]); xs=T.index.values
ser=[('m26_80_100','2–6 months: 80–100 h',AQUA,'-','s'),('m26_lt80','2–6 months: <80 h',ORANGE,'-','o'),('m26_ge100','2–6 months: ≥100 h',BLUE,'-','D'),
     ('m1_ge100','1 month: ≥100 h',BLUE,'--','^'),('m1_lt100','1 month: <100 h',ORANGE,'--','v')]
for k,lab,c,ls,mk in ser:
    a.plot(xs,T[k],ls,color=c,lw=2.2,marker=mk,ms=8,mec='white',mew=1.2,label=lab)
rev(a,2021.5,'Revision (Sep 2021)',118)
a.set_title('A  Approvals by evaluation period, FY2017–2025',loc='left',fontsize=16); a.set_ylabel('Approved claims per year'); a.set_ylim(0,120)
a.set_xticks(range(2017,2026)); a.set_xlabel('Fiscal year')
a.legend(frameon=False,fontsize=13,loc='upper left',bbox_to_anchor=(1.01,1.0))
a=fig.add_axes([0.40,0.07,0.42,0.42])
def rr(d,f='n ~ C(fy)+tg+tg:post'):
    m=smf.glm(f,data=d,family=sm.families.Poisson()).fit(scale='X2'); c=m.conf_int().loc['tg:post']; return np.exp([m.params['tg:post'],c[0],c[1]])
base=oc[oc.fy!=2021].copy(); base['post']=(base.fy>=2022).astype(int)
def mk(tg_bands,ref_bands):
    d=base[base.band.isin(tg_bands+ref_bands)].copy(); d['tg']=d.band.isin(tg_bands).astype(int)
    return rr(d.groupby(['fy','tg','post']).n.sum().reset_index())
ep=ot[(ot.fy>=2017)&(ot.fy!=2021)&ot.period.isin(['m1','m26'])].copy(); ep['post']=(ep.fy>=2022).astype(int)
def mkp(tg,rf):
    x=ep.copy(); x['tg']=x.apply(tg,axis=1).astype(int); x['rf']=x.apply(rf,axis=1).astype(int)
    return rr(x[(x.tg==1)|(x.rf==1)].groupby(['fy','tg','post']).n.sum().reset_index())
dt=pd.read_csv(D+'cvd_by_type.csv'); g=dt[(dt.fy>=S)&(dt.fy!=2021)].copy(); g['post']=(g.fy>=2022).astype(int); g['tg']=(g.type=='虚血性心疾患等').astype(int); g['n']=g.approvals
hi80=['80_100']+HI
rows=[('<80 h vs ≥80 h (main)',mk(LO,hi80),ORANGE),
      ('Below vs above the threshold\nof each evaluation period*',mkp(lambda r:(r.period=='m1' and r.band in LO+['80_100']) or (r.period=='m26' and r.band in LO),
                                                lambda r:(r.period=='m1' and r.band in HI) or (r.period=='m26' and r.band in hi80)),ORANGE),
      ('2–6 months: <80 h vs ≥100 h*',mkp(lambda r:r.period=='m26' and r.band in LO,lambda r:r.period=='m26' and r.band in HI),ORANGE),
      ('Short-term overload or\nextraordinary event vs ≥80 h',mk(['other'],hi80),ORANGE),
      ('80–100 h vs ≥100 h\n(combined periods)',mk(['80_100'],HI),BLUE),
      ('2–6 months: 80–100 h vs ≥100 h*',mkp(lambda r:r.period=='m26' and r.band=='80_100',lambda r:r.period=='m26' and r.band in HI),BLUE),
      ('Cardiac vs cerebrovascular disease',rr(g[['fy','tg','post','n']]),BLUE)]
yy=np.arange(len(rows))[::-1]
for (lab,(e_,l,h),c),y in zip(rows,yy):
    a.plot([l,h],[y,y],color=c,lw=2.5); a.plot(e_,y,'o',color=c,ms=10,mec='white',mew=1.5)
    a.text(1.02,y,f'{e_:.2f} ({l:.2f}–{h:.2f})',va='center',fontsize=13,color=INK,transform=a.get_yaxis_transform())
a.axvline(1,color=INK,lw=1); a.set_xscale('log'); a.set_xlim(0.3,12); a.set_xticks([0.5,1,2,4,8]); a.set_xticklabels(['0.5','1','2','4','8'])
a.set_yticks(yy); a.set_yticklabels([r[0] for r in rows]); a.grid(axis='y',visible=False)
a.set_title('B  Change in the ratio after the revision (95% CI)',loc='left',fontsize=16); a.set_xlabel('Ratio change (log scale)')
save(fig,'AJIM_Figure3'); plt.close()
print('figs done', [ (r[0][:25], np.round(r[1],2)) for r in rows])

# ---------- 投稿用TIFF：RGB（アルファなし）・600 dpi に変換 ----------
from PIL import Image
for i in (1, 2, 3):
    f = O + f'AJIM_Figure{i}.tif'
    im = Image.open(f); bg = Image.new('RGB', im.size, (255, 255, 255)); bg.paste(im.convert('RGBA'), mask=im.convert('RGBA').split()[3])
    bg.save(f, dpi=(600, 600), compression='tiff_lzw')
print('tiff converted to RGB 600 dpi')

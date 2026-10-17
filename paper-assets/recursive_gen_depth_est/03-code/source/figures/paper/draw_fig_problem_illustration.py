import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],
    'font.size': 11,
    'figure.dpi': 300, 'savefig.dpi': 300,
    'savefig.bbox': 'tight', 'savefig.pad_inches': 0.08,
    'pdf.fonttype': 42, 'ps.fonttype': 42,
})

fig, ax = plt.subplots(figsize=(14, 6.0))
ax.set_xlim(0, 14)
ax.set_ylim(0, 6.0)
ax.axis('off')
fig.patch.set_facecolor('white')

C_D0='#7BA3C7'; C_D1='#D4A06A'; C_D2='#C0884A'; C_DK='#A06830'
C_CLS='#DDE3EA'; C_OUT='#F4F5F7'; C_ARR='#8C9AA8'
C_TXT='#2C3E50'; C_SUB='#5D6D7E'; C_ACC='#B94A3A'
C_OBG='#EDE8E0'; C_OBD='#C5B8A5'

def box(ax,x,y,w,h,fc,ec='#88888866',lw=1.2,z=3,shadow=True):
    if shadow:
        ax.add_patch(FancyBboxPatch((x+0.04,y-0.04),w,h,boxstyle="round,pad=0.08",
            facecolor='#00000008',edgecolor='none',zorder=z-1))
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.08",
        facecolor=fc,edgecolor=ec,linewidth=lw,zorder=z))

def doc(ax,cx,cy,scale=0.18,color='white',alpha=0.6,z=5):
    s=scale*3; w,h,f=0.28*s,0.36*s,0.09*s
    ax.fill([cx-w/2,cx-w/2,cx+w/2-f,cx+w/2,cx+w/2,cx-w/2],
            [cy-h/2,cy+h/2,cy+h/2,cy+h/2-f,cy-h/2,cy-h/2],
            color=color,alpha=alpha,zorder=z,linewidth=0)
    ax.fill([cx+w/2-f,cx+w/2-f,cx+w/2],[cy+h/2,cy+h/2-f,cy+h/2-f],
            color=color,alpha=alpha*0.5,zorder=z+1,linewidth=0)

def fa(ax,x1,y1,x2,y2,st='->',c=C_ARR,lw=1.3,z=2,ls='-'):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle=st,mutation_scale=12,
        color=c,linewidth=lw,linestyle=ls,zorder=z))

# ====== ROW 1 ======
ax.text(7,5.65,'Recursive Generation Chain',fontsize=16,fontweight='bold',
        color=C_TXT,ha='center',va='center')

bw,bh,by=1.5,1.05,4.05
bxs=[1.3,4.0,6.7,10.9]
bcs=[C_D0,C_D1,C_D2,C_DK]
bls=[r'$\mathcal{D}_0$',r'$\mathcal{D}_1$',r'$\mathcal{D}_2$',r'$\mathcal{D}_K$']
bss=['Human','Gen-1','Gen-2','Gen-K']

for i,(bx,bc,bl,bs) in enumerate(zip(bxs,bcs,bls,bss)):
    box(ax,bx,by,bw,bh,fc=bc)
    doc(ax,bx+bw-0.25,by+bh-0.19,scale=0.19,color='white',alpha=0.55)
    ax.text(bx+bw/2,by+bh/2+0.1,bl,fontsize=16,ha='center',va='center',
            color='white',fontweight='bold',zorder=6,
            path_effects=[pe.withStroke(linewidth=2.5,foreground=bc)])
    ax.text(bx+bw/2,by+0.17,bs,fontsize=9,ha='center',va='center',
            color='white',alpha=0.85,zorder=6,fontstyle='italic',
            path_effects=[pe.withStroke(linewidth=1.5,foreground=bc)])

aly=by+bh+0.12
for i in range(2):
    xs=bxs[i]+bw+0.1; xe=bxs[i+1]-0.1
    fa(ax,xs,by+bh/2,xe,by+bh/2,lw=1.2)
    ax.text((xs+xe)/2,aly,'LoRA ft + sample',fontsize=8,ha='center',color=C_SUB,fontstyle='italic')

xs2=bxs[2]+bw+0.1
fa(ax,xs2,by+bh/2,9.25,by+bh/2,lw=1.2)
ax.text(9.7,by+bh/2,'· · ·',fontsize=18,ha='center',va='center',color='#9EAAB5',fontweight='bold',zorder=4)
fa(ax,10.15,by+bh/2,bxs[3]-0.1,by+bh/2,lw=1.2)
ax.text((xs2+bxs[3]-0.1)/2,aly,'LoRA ft + sample',fontsize=8,ha='center',color=C_SUB,fontstyle='italic')

# ====== ROW 2 ======
dx,dy=1.6,2.7
fa(ax,bxs[0]+bw/2,by-0.05,dx+0.25,dy+0.6,st='->',c='#AABBCC',lw=0.9,ls='--')

doc(ax,dx+0.05,dy+0.2,scale=0.30,color=C_D0,alpha=0.4)
ax.text(dx+0.55,dy+0.2,r'Text passage $\mathbf{x}$',fontsize=11.5,ha='left',va='center',color=C_TXT)
ax.text(dx+0.55,dy-0.16,r'depth $d = \;$?',fontsize=10.5,ha='left',va='center',color=C_ACC,fontstyle='italic')

clx,cly,clw,clh=5.3,2.3,2.3,1.0
fa(ax,dx+2.55,dy+0.1,clx-0.1,cly+clh/2,st='->',lw=1.4,c=C_SUB)
box(ax,clx,cly,clw,clh,fc=C_CLS,ec='#A0AAB4',lw=1.3)
ax.text(clx+clw/2,cly+clh/2+0.13,'Depth Classifier',fontsize=12,fontweight='bold',
        ha='center',va='center',color=C_TXT,zorder=6)
ax.text(clx+clw/2,cly+clh/2-0.2,'(Statistical Features + RF)',fontsize=8.5,
        ha='center',va='center',color=C_SUB,zorder=6)

# Output panel
ox,oy,ow,oh=8.5,1.15,4.2,2.8
fa(ax,clx+clw+0.1,cly+clh/2,ox-0.1,oy+oh/2,st='->',lw=1.4,c=C_SUB)
box(ax,ox,oy,ow,oh,fc=C_OUT,ec='#C0C8D0',lw=1.0)
ax.text(ox+ow/2,oy+oh-0.2,'Estimated Depth Output',fontsize=11,fontweight='bold',
        ha='center',va='center',color=C_TXT,zorder=6)

# Bar chart
bcs2=[C_D0,C_D1,C_D2,C_DK]
bhs=[0.08,0.70,0.18,0.05]
bls2=[r'$d{=}0$',r'$d{=}1$',r'$d{=}2$',r'$d{=}K$']
bps=['','70%','15%','']
bx0=ox+0.35; bsp=0.92; bww=0.52
bbot=oy+1.05; bmaxh=1.0

ax.plot([bx0-0.05,bx0+3*bsp+bww+0.05],[bbot,bbot],color='#D0D0D0',linewidth=0.7,zorder=4)

for j,(h2,c2,l2,p2) in enumerate(zip(bhs,bcs2,bls2,bps)):
    x=bx0+j*bsp; h=h2*bmaxh
    ax.add_patch(FancyBboxPatch((x,bbot),bww,h,boxstyle="round,pad=0.02",
        facecolor=c2,edgecolor='none',zorder=5,alpha=0.9))
    ax.text(x+bww/2,bbot-0.2,l2,fontsize=8.5,ha='center',va='center',color=C_SUB,zorder=6)
    if p2:
        ax.text(x+bww/2,bbot+h+0.08,p2,fontsize=9.5,ha='center',va='bottom',
                color=c2,fontweight='bold',zorder=6)

# d_hat = 1: placed as a separate row below axis labels
# Small upward triangle at d=1 position
hx=bx0+1*bsp+bww/2
ax.plot(hx,bbot-0.08,marker='^',markersize=5,color=C_ACC,zorder=7,clip_on=False)
# Text below, well separated from axis labels
ax.text(hx,bbot-0.48,r'$\hat{d} = 1$',fontsize=10,fontweight='bold',
        color=C_ACC,ha='center',va='center',zorder=6)

# ====== BOTTOM ======
bot_y=0.65
ax.text(1.5,bot_y,'Binary:  real vs. synthetic',fontsize=10,ha='left',va='center',
        color='#B0B0B0',fontstyle='italic')

box(ax,5.2,bot_y-0.32,7.3,0.58,fc=C_OBG,ec=C_OBD,lw=1.2,shadow=False)
ax.text(5.5,bot_y-0.03,'Ours:',fontsize=11,fontweight='bold',ha='left',va='center',color=C_TXT,zorder=6)
ax.text(6.4,bot_y-0.03,r'$\hat{d} \in \{0, 1, \ldots, K\}$',fontsize=11,
        ha='left',va='center',color=C_TXT,zorder=6)
ax.text(9.4,bot_y-0.03,'(ordinal depth estimation)',fontsize=10,
        ha='left',va='center',color=C_SUB,zorder=6)

plt.savefig('/tmp/fig1_v6.png',dpi=300,facecolor='white')
plt.savefig('/tmp/fig1_v6.pdf',dpi=300,facecolor='white')
plt.close()
print('DONE v6')

"""Figure 2: Framework overview -- Gen-Depth Fingerprint (v3).
Three-panel: Chain Construction | Feature Extraction & DDR | Classification
Panel (b) includes horizontal bar chart of Spearman rho values.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Patch
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'axes.linewidth': 0.5,
})

BG       = '#F7F7F7'
DARK     = '#333333'
WHITE    = '#FFFFFF'
BOX_BLUE = '#4C72B0'
BOX_GREEN= '#55A868'
BOX_ORANGE='#DD8452'
DEPTH_FC = ['#DCEEFB', '#A6CCE3', '#5FA2CB', '#2171B5', '#084594']
DEPTH_EC = ['#9ECAE1', '#6BAED6', '#3182BD', '#08519C', '#063E78']
C_DRIFT  = '#2ca02c'
C_INTERM = '#9467bd'
C_STAT   = '#ff7f0e'

fig = plt.figure(figsize=(7.0, 3.0))
gs = GridSpec(1, 3, width_ratios=[2, 3, 2], wspace=0.22,
              left=0.005, right=0.995, top=0.92, bottom=0.02)

def rbox(ax, x, y, w, h, fc, ec='#CCC', lw=0.6, zorder=2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                       fc=fc, ec=ec, lw=lw, zorder=zorder,
                       transform=ax.transAxes, clip_on=False))

def tx(ax, x, y, s, **kw):
    d = dict(ha='center', va='center', fontsize=7, color=DARK,
             zorder=5, transform=ax.transAxes)
    d.update(kw)
    return ax.text(x, y, s, **d)

def arrow(ax, x0, y0, x1, y1, c='#555', lw=0.8, hw=0.06, hl=0.05):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle=f'->,head_width={hw},head_length={hl}',
                                color=c, lw=lw),
                xycoords='axes fraction', textcoords='axes fraction', zorder=3)

# ================================================================
# Panel (a): Chain Construction
# ================================================================
ax_a = fig.add_subplot(gs[0])
ax_a.set_xlim(0, 1); ax_a.set_ylim(0, 1); ax_a.axis('off')
ax_a.set_facecolor(BG); ax_a.patch.set_alpha(1.0)
ax_a.text(-0.02, 1.06, '(a)', fontsize=9, fontweight='bold', color=DARK,
          transform=ax_a.transAxes, ha='left', va='top')

cx = 0.48
rbox(ax_a, 0.07, 0.87, 0.78, 0.10, DEPTH_FC[0], DEPTH_EC[0], 0.8)
tx(ax_a, cx, 0.92, 'Wikipedia seed (gen-0)', fontsize=7, fontweight='bold')
arrow(ax_a, cx, 0.86, cx, 0.81)

rbox(ax_a, 0.15, 0.72, 0.62, 0.08, '#FFF3E0', '#E6550D', 0.8)
tx(ax_a, cx, 0.76, 'Generator $G$', fontsize=7, fontweight='bold', color='#BF360C')

lx = 0.81
ax_a.annotate('', xy=(lx, 0.805), xytext=(lx, 0.725),
              arrowprops=dict(arrowstyle='->,head_width=0.06,head_length=0.04',
                              connectionstyle='arc3,rad=-3.0',
                              color='#D84315', lw=0.9),
              xycoords='axes fraction', textcoords='axes fraction', zorder=4)
tx(ax_a, lx+0.12, 0.765, r'$\times 4$', fontsize=7, color='#D84315', fontweight='bold')
arrow(ax_a, cx, 0.71, cx, 0.64)

n_d=5; bw=0.145; bgap=0.005
tw=n_d*bw+(n_d-1)*bgap; sx0=cx-tw/2; sy=0.54; sh=0.085
for i in range(n_d):
    bx=sx0+i*(bw+bgap); tc=WHITE if i>=3 else DARK
    rbox(ax_a, bx, sy, bw, sh, DEPTH_FC[i], DEPTH_EC[i], 0.5)
    tx(ax_a, bx+bw/2, sy+sh/2, f'gen-{i}', fontsize=7, color=tc, fontweight='medium')

ax_a.annotate('', xy=(sx0+tw-0.02, sy-0.04), xytext=(sx0+0.02, sy-0.04),
              arrowprops=dict(arrowstyle='->,head_width=0.04,head_length=0.03',
                              color='#888', lw=0.6),
              xycoords='axes fraction', textcoords='axes fraction', zorder=3)
tx(ax_a, cx, sy-0.09, 'Generation depth $d$', fontsize=7, color='#666')
tx(ax_a, cx, 0.05, '8 base LLMs, 5 families, 0.6B–8B',
   fontsize=7, color='#888', style='italic')

# ================================================================
# Panel (b): Feature Extraction & DDR
# ================================================================
gs_b = GridSpecFromSubplotSpec(2, 1, subplot_spec=gs[1],
                                height_ratios=[1, 2.8], hspace=0.20)
ax_b_top = fig.add_subplot(gs_b[0])
ax_b_top.set_xlim(0, 1); ax_b_top.set_ylim(0, 1); ax_b_top.axis('off')
ax_b_bar = fig.add_subplot(gs_b[1])

ax_b_top.text(-0.03, 1.22, '(b)', fontsize=9, fontweight='bold', color=DARK,
              transform=ax_b_top.transAxes, ha='left', va='top')

# Upper flow
flow = [
    (0.005, 0.20, 0.15, 0.55, '#E8E8E8',  '#AAA',      'Text'),
    (0.20,  0.20, 0.23, 0.55, '#D6E8F5',  BOX_BLUE,    'Pythia-410M'),
    (0.48,  0.20, 0.28, 0.55, '#E0F0E0',  BOX_GREEN,   'NLL distribution'),
    (0.81,  0.20, 0.185,0.55, '#FDE8D0',  BOX_ORANGE,  '7 features'),
]
for (bx, by, bw_, bh, fc, ec, label) in flow:
    rbox(ax_b_top, bx, by, bw_, bh, fc, ec, 0.7)
    tx(ax_b_top, bx+bw_/2, by+bh/2, label, fontsize=7, fontweight='bold')
for i in range(len(flow)-1):
    x0=flow[i][0]+flow[i][2]; x1=flow[i+1][0]; ym=flow[i][1]+flow[i][3]/2
    arrow(ax_b_top, x0+0.005, ym, x1-0.005, ym, c='#555', lw=0.7, hw=0.08, hl=0.06)

# Bar chart
features = ['hapax_ratio','TTR','entropy_mean','entropy_min',
            'entropy_std','entropy_max','tail_decay']
rho_vals = [-0.640, -0.625, -0.598, -0.404, -0.157, +0.061, -0.041]
cats     = ['drifting','drifting','drifting','intermediate',
            'intermediate','stationary','stationary']
cmap_ = {'drifting':C_DRIFT,'intermediate':C_INTERM,'stationary':C_STAT}
colors = [cmap_[c] for c in cats]

order = sorted(range(len(rho_vals)), key=lambda i: abs(rho_vals[i]))
f_s=[features[i] for i in order]
r_s=[rho_vals[i] for i in order]
c_s=[colors[i] for i in order]

nice = {'hapax_ratio':'hapax ratio','TTR':'TTR','entropy_mean':'entropy mean',
        'entropy_min':'entropy min','entropy_std':'entropy std',
        'entropy_max':'entropy max','tail_decay':'tail decay'}

y_pos = np.arange(len(f_s))
bars = ax_b_bar.barh(y_pos, r_s, color=c_s, height=0.62, edgecolor='none', linewidth=0)

ax_b_bar.set_yticks(y_pos)
ax_b_bar.set_yticklabels([nice.get(f,f) for f in f_s], fontsize=7)
ax_b_bar.set_xlabel(r'Spearman $\rho$ with depth', fontsize=7, color=DARK)
ax_b_bar.set_xlim(-0.80, 0.25)
ax_b_bar.axvline(x=0, color='#999', lw=0.5, ls='-', zorder=1)
ax_b_bar.tick_params(axis='x', labelsize=7, colors='#666')
ax_b_bar.tick_params(axis='y', length=0)

for i, val in enumerate(r_s):
    if abs(val) >= 0.40:
        # Inside bar near left end (for negative bars)
        ax_b_bar.text(val + 0.03, i, f'{val:+.3f}', va='center', ha='left',
                      fontsize=7, color=WHITE, fontweight='bold')
    elif val < 0:
        ax_b_bar.text(val - 0.02, i, f'{val:+.3f}', va='center', ha='right',
                      fontsize=7, color=DARK, fontweight='medium')
    else:
        ax_b_bar.text(val + 0.02, i, f'{val:+.3f}', va='center', ha='left',
                      fontsize=7, color=DARK, fontweight='medium')

# Legend in upper right (empty area since bars extend left)
legend_elements = [
    Patch(facecolor=C_DRIFT, label='Drifting'),
    Patch(facecolor=C_INTERM, label='Intermediate'),
    Patch(facecolor=C_STAT, label='Stationary'),
]
ax_b_bar.legend(handles=legend_elements, fontsize=7,
                loc='upper right',
                framealpha=0.9, edgecolor='#CCC', handlelength=1.0,
                handletextpad=0.4, borderpad=0.3)

for sp in ['top','right','left']:
    ax_b_bar.spines[sp].set_visible(False)
ax_b_bar.spines['bottom'].set_color('#999')
ax_b_bar.spines['bottom'].set_linewidth(0.5)

# ================================================================
# Panel (c): Classification
# ================================================================
ax_c = fig.add_subplot(gs[2])
ax_c.set_xlim(0, 1); ax_c.set_ylim(0, 1); ax_c.axis('off')
ax_c.set_facecolor(BG); ax_c.patch.set_alpha(1.0)
ax_c.text(-0.02, 1.06, '(c)', fontsize=9, fontweight='bold', color=DARK,
          transform=ax_c.transAxes, ha='left', va='top')

cx_c = 0.5
rbox(ax_c, 0.10, 0.84, 0.80, 0.09, '#FDE8D0', BOX_ORANGE, 0.7)
tx(ax_c, cx_c, 0.885, '7 DDR features', fontsize=7, fontweight='bold')
arrow(ax_c, cx_c, 0.83, cx_c, 0.76)

rbox(ax_c, 0.05, 0.66, 0.90, 0.09, '#E8D4E8', '#6A3D6A', 0.8)
tx(ax_c, cx_c, 0.705, 'XGBoost (LOGO-CV)', fontsize=7,
   fontweight='bold', color='#4A2D4A')
arrow(ax_c, cx_c, 0.65, cx_c, 0.57)

cw_=0.22; ch_=0.08; cg_=0.03
ct_=3*cw_+2*cg_; cx0=cx_c-ct_/2; cy_=0.47
for k, (cls, col, tc) in enumerate([
    ('gen-0', DEPTH_FC[0], DARK),
    ('gen-1', DEPTH_FC[2], DARK),
    ('gen-2+', DEPTH_FC[4], WHITE)]):
    cxx=cx0+k*(cw_+cg_)
    rbox(ax_c, cxx, cy_, cw_, ch_, col, DEPTH_EC[k*2], 0.5)
    tx(ax_c, cxx+cw_/2, cy_+ch_/2, cls, fontsize=7, color=tc, fontweight='bold')
tx(ax_c, cx_c, cy_-0.05, '3-class output', fontsize=7, color='#888')

rbox(ax_c, 0.10, 0.12, 0.80, 0.13, '#F0F7F0', BOX_GREEN, 0.6)
tx(ax_c, cx_c, 0.185, r'LOGO $F_1$ = 0.694', fontsize=7.5,
   fontweight='bold', color='#2D6A2D')

# -- Save --
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart'
os.makedirs(out_dir, exist_ok=True)
fig.savefig(f'{out_dir}/fig2_framework.pdf', format='pdf')
fig.savefig(f'{out_dir}/fig2_framework.png', format='png')
print(f'Saved: {out_dir}/fig2_framework.pdf + .png')

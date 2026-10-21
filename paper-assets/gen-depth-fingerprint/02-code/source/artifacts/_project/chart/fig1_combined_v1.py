"""Figure 1: Combined method pipeline + DDR results (Option A, v2 layout fix).
Left panel (a): 4-stage compact pipeline. Right panel (b): DDR bar chart.
Full-width — empirical paper, results as hero."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.gridspec import GridSpec
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif'],
    'font.size': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'axes.linewidth': 0.5,
    'mathtext.fontset': 'cm',
})

DARK = '#333333'
WHITE = '#FFFFFF'
BG = '#F7F7F7'

DEPTH_FC = ['#DCEEFB', '#A6CCE3', '#5FA2CB', '#2171B5', '#084594']
DEPTH_EC = ['#9ECAE1', '#6BAED6', '#3182BD', '#08519C', '#063E78']

C_DRIFT = '#2ca02c'
C_INTERM = '#7b4ea3'
C_STAT = '#d97706'

C_GEN = '#FFF3E0'
C_REF = '#D6E8F5'
C_FEAT = '#FDE8D0'
C_CLASS = '#E8D4E8'

fig = plt.figure(figsize=(7.0, 3.2))
gs = GridSpec(1, 2, width_ratios=[0.9, 2.2], wspace=0.30,
              left=0.005, right=0.995, top=0.93, bottom=0.10)


def rbox(ax, x, y, w, h, fc, ec='#CCC', lw=0.6, zorder=2, rad=0.012):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad={rad}",
                       fc=fc, ec=ec, lw=lw, zorder=zorder,
                       transform=ax.transAxes, clip_on=False)
    ax.add_patch(p)
    return p


def tx(ax, x, y, s, **kw):
    d = dict(ha='center', va='center', fontsize=7, color=DARK,
             zorder=5, transform=ax.transAxes)
    d.update(kw)
    return ax.text(x, y, s, **d)


def arr(ax, x0, y0, x1, y1, c='#888', lw=0.8, hw=0.04, hl=0.03):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle=f'->,head_width={hw},head_length={hl}',
                                color=c, lw=lw),
                xycoords='axes fraction', textcoords='axes fraction', zorder=3)


# ================================================================
# Panel (a): 4-stage compact pipeline
# ================================================================
ax_a = fig.add_subplot(gs[0])
ax_a.set_xlim(0, 1); ax_a.set_ylim(0, 1); ax_a.axis('off')
ax_a.set_facecolor(BG); ax_a.patch.set_alpha(1.0)
tx(ax_a, 0.00, 1.06, '(a)', fontsize=9, fontweight='bold', ha='left', va='top')

cx = 0.48
bw = 0.88
bh = 0.11
gap = 0.045

# --- Stage 1: Chain construction (compound box) ---
y = 0.92
ch_h = 0.18
rbox(ax_a, cx-bw/2, y-ch_h, bw, ch_h, '#F5F5F5', '#BBB', 0.5, rad=0.010)

# Inner: 3 mini-boxes  gen-0 → G → gen-k
mw = 0.22; mh = 0.08; my = y - ch_h + 0.065
# gen-0
rbox(ax_a, 0.06, my, mw, mh, DEPTH_FC[0], DEPTH_EC[0], 0.5, rad=0.006)
tx(ax_a, 0.06+mw/2, my+mh/2, r'$x^{(0)}$', fontsize=7.5, fontweight='bold')
# arrow
arr(ax_a, 0.06+mw+0.01, my+mh/2, 0.38, my+mh/2, c='#888', lw=0.7)
# G
rbox(ax_a, 0.39, my, mw, mh, C_GEN, '#E6550D', 0.5, rad=0.006)
tx(ax_a, 0.39+mw/2, my+mh/2, r'$G$', fontsize=9, fontweight='bold', color='#BF360C')
# arrow
arr(ax_a, 0.39+mw+0.01, my+mh/2, 0.71, my+mh/2, c='#888', lw=0.7)
# gen-k
rbox(ax_a, 0.72, my, mw, mh, DEPTH_FC[3], DEPTH_EC[3], 0.5, rad=0.006)
tx(ax_a, 0.72+mw/2, my+mh/2, r'$x^{(k)}$', fontsize=7.5, fontweight='bold', color=WHITE)

# stage label
tx(ax_a, cx, y-ch_h+0.025, r'$x^{(k)}\!=\!G(x^{(k-1)})$',
   fontsize=6.5, color='#777')

arr(ax_a, cx, y-ch_h-0.005, cx, y-ch_h-gap+0.005)

# --- Stage 2: Reference model ---
y2 = y - ch_h - gap
rbox(ax_a, cx-bw/2, y2-bh, bw, bh, C_REF, '#4C72B0', 0.7)
tx(ax_a, cx, y2-bh/2+0.01, 'Pythia-410M', fontsize=7.5, fontweight='bold', color='#2C5290')
tx(ax_a, cx, y2-bh/2-0.02, 'per-token NLL', fontsize=5.5, color='#5A8AB0')

arr(ax_a, cx, y2-bh-0.005, cx, y2-bh-gap+0.005)

# --- Stage 3: DDR features ---
y3 = y2 - bh - gap
rbox(ax_a, cx-bw/2, y3-bh, bw, bh, C_FEAT, '#DD8452', 0.8)
tx(ax_a, cx, y3-bh/2, '7 DDR features', fontsize=8, fontweight='bold', color='#AA6030')

arr(ax_a, cx, y3-bh-0.005, cx, y3-bh-gap+0.005)

# --- Stage 4: Classifier ---
y4 = y3 - bh - gap
rbox(ax_a, cx-bw/2, y4-bh, bw, bh, C_CLASS, '#6A3D6A', 0.7)
tx(ax_a, cx, y4-bh/2, 'XGBoost (LOGO)', fontsize=7.5, fontweight='bold', color='#4A2D4A')

arr(ax_a, cx, y4-bh-0.005, cx, y4-bh-gap+0.005)

# --- 3-class output ---
y5 = y4 - bh - gap
ow = 0.26; oh = 0.06; og = 0.02
ot = 3*ow + 2*og
ox0 = cx - ot/2
for k, (cls, col, ec_idx, tc) in enumerate([
    ('gen-0', DEPTH_FC[0], 0, DARK),
    ('gen-1', DEPTH_FC[2], 2, DARK),
    ('gen-2+', DEPTH_FC[4], 4, WHITE)]):
    oxx = ox0 + k*(ow+og)
    rbox(ax_a, oxx, y5-oh, ow, oh, col, DEPTH_EC[ec_idx], 0.5, rad=0.006)
    tx(ax_a, oxx+ow/2, y5-oh/2, cls, fontsize=6.5, color=tc, fontweight='bold')

tx(ax_a, cx, y5-oh-0.035, '8 LLMs · 5 families · 0.6B–8B',
   fontsize=5, color='#999')


# ================================================================
# Panel (b): DDR tri-partition bar chart
# ================================================================
ax_b = fig.add_subplot(gs[1])

features = [
    ('hapax',              -0.647, 'drifting'),
    ('TTR',                -0.630, 'drifting'),
    (r'$\bar{H}$',        -0.610, 'drifting'),
    (r'$\sigma_H$',       -0.200, 'intermediate'),
    (r'$H_{\min}$$^{\dagger}$', -0.406, 'stationary'),
    (r'$H_{\max}$',        0.050, 'stationary'),
    ('tail dec.',          -0.040, 'stationary'),
]

zone_color = {'drifting': C_DRIFT, 'intermediate': C_INTERM, 'stationary': C_STAT}

n = len(features)
y_pos = np.arange(n)[::-1]

for i, (label, rho, zone) in enumerate(features):
    c = zone_color[zone]
    yi = y_pos[i]
    ax_b.barh(yi, rho, height=0.58, color=c, edgecolor='none', alpha=0.85, zorder=2)
    if abs(rho) >= 0.35:
        ax_b.text(rho + 0.025, yi, f'{rho:+.2f}', va='center', ha='left',
                  fontsize=6.5, color='#333', fontweight='bold')
    elif rho < 0:
        ax_b.text(rho - 0.015, yi, f'{rho:+.2f}', va='center', ha='right',
                  fontsize=6.5, color='#333')
    else:
        ax_b.text(rho + 0.015, yi, f'{rho:+.2f}', va='center', ha='left',
                  fontsize=6.5, color='#333')

ax_b.axvline(0, color='#aaa', linewidth=0.4, zorder=1)

sep_y_1 = y_pos[2] - 0.45
sep_y_2 = y_pos[3] - 0.45
ax_b.axhline(sep_y_1, color='#ccc', linewidth=0.5, linestyle='--', zorder=1)
ax_b.axhline(sep_y_2, color='#ccc', linewidth=0.5, linestyle='--', zorder=1)

ax_b.set_yticks(y_pos)
ax_b.set_yticklabels([f[0] for f in features], fontsize=7.5)
ax_b.set_xlabel(r'Spearman $\rho$ with generation depth', fontsize=8)
ax_b.set_xlim(-0.82, 0.28)
ax_b.set_ylim(-0.6, n - 0.4)
ax_b.tick_params(axis='y', length=0)
ax_b.tick_params(axis='x', labelsize=7, colors='#666')

for sp in ['top', 'right', 'left']:
    ax_b.spines[sp].set_visible(False)
ax_b.spines['bottom'].set_color('#999')
ax_b.spines['bottom'].set_linewidth(0.5)

zone_mid = {
    'drifting': (y_pos[0] + y_pos[2]) / 2,
    'intermediate': y_pos[3],
    'stationary': (y_pos[4] + y_pos[6]) / 2,
}
zone_labels = {
    'drifting': ('Drifting', r'$|\rho|>0.6$'),
    'intermediate': ('Intermediate', r'$|\rho|\approx 0.2$'),
    'stationary': ('Near-stationary', r'$|\rho|<0.1^{\dagger}$'),
}
for zone, ym in zone_mid.items():
    lbl, sub = zone_labels[zone]
    ax_b.text(0.25, ym + 0.15, lbl, fontsize=6.5, color=zone_color[zone],
              fontweight='bold', va='bottom', ha='right')
    ax_b.text(0.25, ym - 0.15, sub, fontsize=5.5, color=zone_color[zone],
              va='top', ha='right')

ax_b.text(-0.82, n + 0.1, '(b)', fontsize=9, fontweight='bold',
          color=DARK, va='top', ha='left')

# ================================================================
# Save
# ================================================================
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart'
os.makedirs(out_dir, exist_ok=True)
fig.savefig(f'{out_dir}/fig1_combined.pdf', format='pdf')
fig.savefig(f'{out_dir}/fig1_combined.png', format='png')
print(f'Saved fig1_combined to {out_dir}/')

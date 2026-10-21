"""Figure 2: Gen-Depth Fingerprint Framework (v4).
Three-panel: (a) Chain Construction, (b) Feature Extraction + DDR, (c) Classification.
Applies F1-F7 rules: real text anchoring, formula embedding, high density."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Patch
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
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
C_NLL = '#E0F0E0'
C_FEAT = '#FDE8D0'
C_CLASS = '#E8D4E8'

fig = plt.figure(figsize=(7.0, 3.3))
gs = GridSpec(1, 3, width_ratios=[2.0, 3.2, 1.8], wspace=0.25,
              left=0.005, right=0.995, top=0.93, bottom=0.02)


def rbox(ax, x, y, w, h, fc, ec='#CCC', lw=0.6, zorder=2):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.015",
                       fc=fc, ec=ec, lw=lw, zorder=zorder,
                       transform=ax.transAxes, clip_on=False)
    ax.add_patch(p)
    return p


def tx(ax, x, y, s, **kw):
    d = dict(ha='center', va='center', fontsize=7, color=DARK,
             zorder=5, transform=ax.transAxes)
    d.update(kw)
    return ax.text(x, y, s, **d)


def arrow(ax, x0, y0, x1, y1, c='#555', lw=0.8, hw=0.06, hl=0.04):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle=f'->,head_width={hw},head_length={hl}',
                                color=c, lw=lw),
                xycoords='axes fraction', textcoords='axes fraction', zorder=3)


# ================================================================
# Panel (a): Chain Construction with text examples
# ================================================================
ax_a = fig.add_subplot(gs[0])
ax_a.set_xlim(0, 1); ax_a.set_ylim(0, 1); ax_a.axis('off')
ax_a.set_facecolor(BG); ax_a.patch.set_alpha(1.0)
tx(ax_a, -0.02, 1.06, '(a)', fontsize=9, fontweight='bold', ha='left', va='top')

cx = 0.50

# gen-0
rbox(ax_a, 0.04, 0.82, 0.92, 0.15, DEPTH_FC[0], DEPTH_EC[0], 0.8)
tx(ax_a, 0.10, 0.94, 'gen-0', fontsize=6.5, fontweight='bold', ha='left')
tx(ax_a, 0.88, 0.94, '(human)', fontsize=5.5, color='#888', ha='right')
tx(ax_a, cx, 0.875, '"ATP is produced via oxidative',
   fontsize=5.5, color='#555', style='italic')
tx(ax_a, cx, 0.845, 'phosphorylation in the inner membrane."',
   fontsize=5.5, color='#555', style='italic')

# Arrow + Generator
arrow(ax_a, cx, 0.81, cx, 0.74)
rbox(ax_a, 0.15, 0.63, 0.70, 0.10, C_GEN, '#E6550D', 0.8)
tx(ax_a, cx, 0.68, 'Generator $G$', fontsize=7, fontweight='bold', color='#BF360C')

# Recurrence arrow
lx = 0.88
ax_a.annotate('', xy=(lx, 0.755), xytext=(lx, 0.63),
              arrowprops=dict(arrowstyle='->,head_width=0.05,head_length=0.04',
                              connectionstyle='arc3,rad=-2.5',
                              color='#D84315', lw=0.8),
              xycoords='axes fraction', textcoords='axes fraction', zorder=4)

# gen-1
arrow(ax_a, cx, 0.62, cx, 0.56)
rbox(ax_a, 0.04, 0.41, 0.92, 0.15, DEPTH_FC[2], DEPTH_EC[2], 0.8)
tx(ax_a, 0.10, 0.53, 'gen-1', fontsize=6.5, fontweight='bold', ha='left')
tx(ax_a, cx, 0.475, '"ATP is generated through oxidative',
   fontsize=5.5, color='#555', style='italic')
tx(ax_a, cx, 0.445, 'processes within the cell membrane."',
   fontsize=5.5, color='#555', style='italic')

# Arrow
arrow(ax_a, cx, 0.40, cx, 0.34)

# gen-2+
rbox(ax_a, 0.04, 0.20, 0.92, 0.13, DEPTH_FC[4], '#063E78', 0.8)
tx(ax_a, 0.10, 0.305, 'gen-2+', fontsize=6.5, fontweight='bold', color=WHITE, ha='left')
tx(ax_a, cx, 0.255, '"ATP is produced through important',
   fontsize=5.5, color='#B0CEE8', style='italic')
tx(ax_a, cx, 0.225, 'processes in the cell."',
   fontsize=5.5, color='#B0CEE8', style='italic')

# Formula
tx(ax_a, cx, 0.11, r'$x^{(k)} = G\!\left(x^{(k-1)}\right)$',
   fontsize=8.5, color=DARK, fontweight='bold')

# Generator info
tx(ax_a, cx, 0.02, '8 LLMs, 5 families, 0.6B–8B',
   fontsize=6, color='#888', style='italic')


# ================================================================
# Panel (b): Feature Extraction + DDR bar chart
# ================================================================
gs_b = GridSpecFromSubplotSpec(2, 1, subplot_spec=gs[1],
                                height_ratios=[1, 3.2], hspace=0.18)
ax_b_top = fig.add_subplot(gs_b[0])
ax_b_top.set_xlim(0, 1); ax_b_top.set_ylim(0, 1); ax_b_top.axis('off')
ax_b_bar = fig.add_subplot(gs_b[1])

tx(ax_b_top, -0.03, 1.28, '(b)', fontsize=9, fontweight='bold',
   ha='left', va='top', transform=ax_b_top.transAxes)

# Pipeline flow (compact, no overlap)
flow = [
    (0.00,  0.20, 0.14, 0.55, '#E8E8E8', '#AAA',     'Text $x^{(k)}$'),
    (0.17,  0.20, 0.24, 0.55, C_REF,     '#4C72B0',  'Pythia-410M'),
    (0.44,  0.20, 0.27, 0.55, C_NLL,     '#55A868',  'NLL sequence'),
    (0.74,  0.20, 0.25, 0.55, C_FEAT,    '#DD8452',  '7 features'),
]
for (bx, by, bw, bh, fc, ec, label) in flow:
    rbox(ax_b_top, bx, by, bw, bh, fc, ec, 0.7)
    tx(ax_b_top, bx + bw / 2, by + bh / 2, label, fontsize=6.5, fontweight='bold')

for i in range(len(flow) - 1):
    x0 = flow[i][0] + flow[i][2]
    x1 = flow[i + 1][0]
    ym = flow[i][1] + flow[i][3] / 2
    arrow(ax_b_top, x0 + 0.005, ym, x1 - 0.005, ym, c='#555', lw=0.7, hw=0.08, hl=0.05)

# Sub-labels for feature groups
tx(ax_b_top, 0.82, 0.05, '5 reference + 2 surface', fontsize=5, color='#888')

# Bar chart
features = ['hapax', 'TTR', r'$\bar{H}$', r'$H_{\min}$',
            r'$\sigma_H$', r'$H_{\max}$', 'tail dec.']
rho_vals = [-0.647, -0.630, -0.610, -0.406, -0.200, +0.050, -0.040]
cats = ['drifting', 'drifting', 'drifting', 'stationary',
        'intermediate', 'stationary', 'stationary']
cmap_ = {'drifting': C_DRIFT, 'intermediate': C_INTERM, 'stationary': C_STAT}
colors = [cmap_[c] for c in cats]

order = sorted(range(len(rho_vals)), key=lambda i: abs(rho_vals[i]))
f_s = [features[i] for i in order]
r_s = [rho_vals[i] for i in order]
c_s = [colors[i] for i in order]

y_pos = np.arange(len(f_s))
ax_b_bar.barh(y_pos, r_s, color=c_s, height=0.58, edgecolor='none', alpha=0.85)

ax_b_bar.set_yticks(y_pos)
ax_b_bar.set_yticklabels(f_s, fontsize=7)
ax_b_bar.set_xlabel(r'Spearman $\rho$ with depth', fontsize=7, color=DARK)
ax_b_bar.set_xlim(-0.82, 0.25)
ax_b_bar.axvline(x=0, color='#999', lw=0.4, zorder=1)
ax_b_bar.tick_params(axis='x', labelsize=6.5, colors='#666')
ax_b_bar.tick_params(axis='y', length=0)

for i, val in enumerate(r_s):
    offset = 0.02 if val >= 0 else -0.02
    ha = 'left' if val >= 0 else 'right'
    if abs(val) >= 0.35:
        ax_b_bar.text(val + 0.025, i, f'{val:+.2f}', va='center', ha='left',
                      fontsize=6, color='#333', fontweight='bold')
    else:
        ax_b_bar.text(val + offset, i, f'{val:+.2f}', va='center', ha=ha,
                      fontsize=6, color='#555')

legend_elements = [
    Patch(facecolor=C_DRIFT, label='Drifting'),
    Patch(facecolor=C_INTERM, label='Intermediate'),
    Patch(facecolor=C_STAT, label='Near-stationary'),
]
ax_b_bar.legend(handles=legend_elements, fontsize=6,
                loc='upper right', framealpha=0.9, edgecolor='#CCC',
                handlelength=0.8, handletextpad=0.3, borderpad=0.3)

for sp in ['top', 'right', 'left']:
    ax_b_bar.spines[sp].set_visible(False)
ax_b_bar.spines['bottom'].set_color('#999')
ax_b_bar.spines['bottom'].set_linewidth(0.5)


# ================================================================
# Panel (c): Classification Pipeline
# ================================================================
ax_c = fig.add_subplot(gs[2])
ax_c.set_xlim(0, 1); ax_c.set_ylim(0, 1); ax_c.axis('off')
ax_c.set_facecolor(BG); ax_c.patch.set_alpha(1.0)
tx(ax_c, -0.02, 1.06, '(c)', fontsize=9, fontweight='bold', ha='left', va='top')

cx_c = 0.50

# Input features
rbox(ax_c, 0.08, 0.85, 0.84, 0.09, C_FEAT, '#DD8452', 0.7)
tx(ax_c, cx_c, 0.895, '7 DDR features', fontsize=7, fontweight='bold')

# Arrow
arrow(ax_c, cx_c, 0.84, cx_c, 0.77)

# XGBoost
rbox(ax_c, 0.05, 0.66, 0.90, 0.10, C_CLASS, '#6A3D6A', 0.8)
tx(ax_c, cx_c, 0.71, 'XGBoost (LOGO-CV)', fontsize=7,
   fontweight='bold', color='#4A2D4A')

# Arrow
arrow(ax_c, cx_c, 0.65, cx_c, 0.57)

# 3-class output
cw = 0.24
ch = 0.08
cg = 0.02
ct = 3 * cw + 2 * cg
cx0 = cx_c - ct / 2
cy = 0.47
for k, (cls, col, ec_idx, tc) in enumerate([
    ('gen-0', DEPTH_FC[0], 0, DARK),
    ('gen-1', DEPTH_FC[2], 2, DARK),
    ('gen-2+', DEPTH_FC[4], 4, WHITE)]):
    cxx = cx0 + k * (cw + cg)
    rbox(ax_c, cxx, cy, cw, ch, col, DEPTH_EC[ec_idx], 0.5)
    tx(ax_c, cxx + cw / 2, cy + ch / 2, cls, fontsize=7, color=tc, fontweight='bold')

tx(ax_c, cx_c, cy - 0.05, '3-class depth prediction', fontsize=6, color='#888')

# Key metrics box
rbox(ax_c, 0.06, 0.10, 0.88, 0.22, '#F0F7F0', '#55A868', 0.6)
tx(ax_c, cx_c, 0.26, 'LOGO binary F1', fontsize=6.5, color='#555')
tx(ax_c, cx_c, 0.19, '(gen-1 vs. gen-2+)', fontsize=5.5, color='#888')
tx(ax_c, cx_c, 0.13, '0.694', fontsize=12, fontweight='bold', color='#2D6A2D')


# ================================================================
# Save
# ================================================================
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart'
os.makedirs(out_dir, exist_ok=True)
fig.savefig(f'{out_dir}/fig2_framework.pdf', format='pdf')
fig.savefig(f'{out_dir}/fig2_framework.png', format='png')
print(f'Saved fig2 to {out_dir}/')

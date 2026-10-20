"""Figure 2: Framework — column-width vertical layout (3 stacked panels)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif'],
    'font.size': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.linewidth': 0.5,
    'mathtext.fontset': 'cm',
})

DARK = '#333333'
WHITE = '#FFFFFF'
BG = '#F7F7F7'

C_DRIFT  = '#D6604D'
C_INTERM = '#7570B3'
C_STAT   = '#4393C3'
C_DRIFT_BG  = '#FADAD4'
C_INTERM_BG = '#DEDCEF'
C_STAT_BG   = '#D0E4F0'

DEPTH_FC = ['#DCEEFB', '#A6CCE3', '#5FA2CB', '#2171B5', '#084594']
DEPTH_EC = ['#9ECAE1', '#6BAED6', '#3182BD', '#08519C', '#063E78']

C_GEN = '#FFF3E0'
C_REF = '#D6E8F5'
C_NLL = '#E0F0E0'
C_CLASS = '#E8D4E8'
C_TRAIN = '#C8E6C9'
C_TEST = '#FFCDD2'


def rbox(ax, x, y, w, h, fc, ec='#CCC', lw=0.6, zorder=2, rad=0.012):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad={rad}",
                       fc=fc, ec=ec, lw=lw, zorder=zorder,
                       transform=ax.transAxes, clip_on=False)
    ax.add_patch(p)


def tx(ax, x, y, s, **kw):
    d = dict(ha='center', va='center', fontsize=6.5, color=DARK,
             zorder=5, transform=ax.transAxes)
    d.update(kw)
    return ax.text(x, y, s, **d)


def arrow(ax, x0, y0, x1, y1, c='#888', lw=0.7, hw=0.012, hl=0.008):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle=f'->,head_width={hw},head_length={hl}',
                                color=c, lw=lw),
                xycoords='axes fraction', textcoords='axes fraction', zorder=3)


fig, ax = plt.subplots(figsize=(3.25, 4.8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_facecolor('white')

# ======== Panel (a): Chain Construction (top third) ========
y_a_top = 0.97
tx(ax, 0.02, y_a_top, '(a)', fontsize=7.5, fontweight='bold', ha='left', va='top')
tx(ax, 0.17, y_a_top, 'Recursive Generation Chain', fontsize=7, ha='left', va='top',
   fontweight='bold', color='#555')

# gen-0
rbox(ax, 0.05, 0.885, 0.40, 0.055, DEPTH_FC[0], DEPTH_EC[0], 0.7)
tx(ax, 0.25, 0.912, 'gen-0 (human)', fontsize=6)

# Generator G
rbox(ax, 0.55, 0.885, 0.40, 0.055, C_GEN, '#E6550D', 0.7)
tx(ax, 0.75, 0.912, r'Generator $G$', fontsize=6.5, fontweight='bold', color='#BF360C')

arrow(ax, 0.25, 0.884, 0.25, 0.848)

# gen-1
rbox(ax, 0.05, 0.79, 0.40, 0.055, DEPTH_FC[2], DEPTH_EC[2], 0.7)
tx(ax, 0.25, 0.817, 'gen-1', fontsize=6, fontweight='bold')

arrow(ax, 0.25, 0.789, 0.25, 0.753)

# gen-2+
rbox(ax, 0.05, 0.695, 0.40, 0.055, DEPTH_FC[4], '#063E78', 0.7)
tx(ax, 0.25, 0.722, 'gen-2+', fontsize=6, fontweight='bold', color=WHITE)

# Recurrence arrow on right side
ax.annotate('', xy=(0.55, 0.885), xytext=(0.55, 0.75),
            arrowprops=dict(arrowstyle='->,head_width=0.01,head_length=0.008',
                            connectionstyle='arc3,rad=-1.5',
                            color='#D84315', lw=0.7),
            xycoords='axes fraction', textcoords='axes fraction', zorder=4)

# Formula + info
tx(ax, 0.75, 0.82, r'$x^{(k)} = G(x^{(k-1)})$', fontsize=7.5, color=DARK)
tx(ax, 0.75, 0.76, '8 LLMs | 5 families', fontsize=5.5, color='#999')
tx(ax, 0.75, 0.72, '0.6B–8B params', fontsize=5.5, color='#999')

# ======== Separator ========
ax.plot([0.03, 0.97], [0.67, 0.67], color='#ddd', lw=0.5, transform=ax.transAxes, zorder=1)

# ======== Panel (b): Feature Extraction (middle third) ========
tx(ax, 0.02, 0.655, '(b)', fontsize=7.5, fontweight='bold', ha='left', va='top')
tx(ax, 0.17, 0.655, 'Feature Extraction', fontsize=7, ha='left', va='top',
   fontweight='bold', color='#555')

# Input text
rbox(ax, 0.05, 0.58, 0.90, 0.045, '#E8E8E8', '#AAA', 0.6)
tx(ax, 0.50, 0.602, r'Input text $x^{(k)}$ → Pythia-410M (ref.) → NLL distribution',
   fontsize=5.5, color='#555')

# Arrows to 3 DDR zones
arrow(ax, 0.22, 0.578, 0.18, 0.545)
arrow(ax, 0.50, 0.578, 0.50, 0.545)
arrow(ax, 0.78, 0.578, 0.82, 0.545)

# Three DDR zone boxes
bw = 0.28
bh = 0.10

# Drifting
rbox(ax, 0.04, 0.44, bw, bh, C_DRIFT_BG, C_DRIFT, 0.8)
tx(ax, 0.04 + bw/2, 0.525, 'Drifting', fontsize=6, fontweight='bold', color=C_DRIFT)
tx(ax, 0.04 + bw/2, 0.485, r'$\bar{H}$, TTR', fontsize=5.5, color='#555')
tx(ax, 0.04 + bw/2, 0.455, 'hapax ratio', fontsize=5.5, color='#555')

# Intermediate
rbox(ax, 0.36, 0.44, bw, bh, C_INTERM_BG, C_INTERM, 0.8)
tx(ax, 0.36 + bw/2, 0.525, 'Intermediate', fontsize=6, fontweight='bold', color=C_INTERM)
tx(ax, 0.36 + bw/2, 0.48, r'$\sigma_H$', fontsize=6, color='#555')

# Near-stationary
rbox(ax, 0.68, 0.44, bw, bh, C_STAT_BG, C_STAT, 0.8)
tx(ax, 0.68 + bw/2, 0.525, 'Near-stat.', fontsize=6, fontweight='bold', color=C_STAT)
tx(ax, 0.68 + bw/2, 0.485, r'$H_{\max}$, $H_{\min}$', fontsize=5.5, color='#555')
tx(ax, 0.68 + bw/2, 0.455, 'tail decay', fontsize=5.5, color='#555')

# Merge arrows to output
arrow(ax, 0.18, 0.438, 0.40, 0.40)
arrow(ax, 0.50, 0.438, 0.50, 0.40)
arrow(ax, 0.82, 0.438, 0.60, 0.40)

# 7 DDR features box
rbox(ax, 0.20, 0.35, 0.60, 0.045, '#FDE8D0', '#DD8452', 0.7)
tx(ax, 0.50, 0.372, '7 DDR features', fontsize=6.5, fontweight='bold', color='#AA6030')

# ======== Separator ========
ax.plot([0.03, 0.97], [0.33, 0.33], color='#ddd', lw=0.5, transform=ax.transAxes, zorder=1)

# ======== Panel (c): LOGO Classification (bottom third) ========
tx(ax, 0.02, 0.315, '(c)', fontsize=7.5, fontweight='bold', ha='left', va='top')
tx(ax, 0.17, 0.315, 'LOGO Classification', fontsize=7, ha='left', va='top',
   fontweight='bold', color='#555')

# Generator grid (2 rows x 4 cols)
gen_names = ['Py2.8', 'Py1B', 'OLMo', 'Q1.7', 'Q0.6', 'Q8B', 'Llm3', 'Mis7']
gbw, gbh = 0.10, 0.035
ggap_x, ggap_y = 0.02, 0.015
total_gw = 4 * gbw + 3 * ggap_x
gx0 = 0.50 - total_gw / 2
held_out = 5

for gi in range(8):
    row = gi // 4
    col = gi % 4
    gx = gx0 + col * (gbw + ggap_x)
    gy = 0.24 - row * (gbh + ggap_y)
    if gi == held_out:
        rbox(ax, gx, gy, gbw, gbh, C_TEST, '#E53935', 0.6, rad=0.006)
        tx(ax, gx + gbw/2, gy + gbh/2, gen_names[gi], fontsize=4.5, fontweight='bold', color='#C62828')
    else:
        rbox(ax, gx, gy, gbw, gbh, C_TRAIN, '#388E3C', 0.4, rad=0.006)
        tx(ax, gx + gbw/2, gy + gbh/2, gen_names[gi], fontsize=4.5, color='#2E7D32')

# Legend
tx(ax, 0.30, 0.155, 'train (7)', fontsize=5, color='#388E3C')
tx(ax, 0.70, 0.155, 'test (1)', fontsize=5, color='#E53935')

# Arrow to classifier
arrow(ax, 0.50, 0.15, 0.50, 0.12)

# XGBoost box
rbox(ax, 0.20, 0.07, 0.60, 0.045, C_CLASS, '#6A3D6A', 0.7)
tx(ax, 0.50, 0.092, 'XGBoost Classifier', fontsize=6.5, fontweight='bold', color='#4A2D4A')

# Arrow to output
arrow(ax, 0.50, 0.068, 0.50, 0.04)

# 3-class output
cw = 0.16
cg = 0.015
ct = 3 * cw + 2 * cg
cx0 = 0.50 - ct / 2
for k, (cls, col, ec_idx, tc) in enumerate([
    ('gen-0', DEPTH_FC[0], 0, DARK),
    ('gen-1', DEPTH_FC[2], 2, DARK),
    ('gen-2+', DEPTH_FC[4], 4, WHITE)]):
    cxx = cx0 + k * (cw + cg)
    rbox(ax, cxx, 0.0, cw, 0.035, col, DEPTH_EC[ec_idx], 0.5, rad=0.006)
    tx(ax, cxx + cw/2, 0.017, cls, fontsize=5.5, color=tc, fontweight='bold')

plt.tight_layout(pad=0.1)

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart'
fig.savefig(f'{out_dir}/fig2_framework_col.pdf', format='pdf')
fig.savefig(f'{out_dir}/fig2_framework_col.png', format='png')
print(f'Saved column-width framework to {out_dir}/')

"""Figure 2: Gen-Depth Fingerprint Framework (v5).
Iconic redesign — no experimental results, visual-first, fewer words."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Arc
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

C_GEN = '#FFF3E0'
C_REF = '#D6E8F5'
C_NLL = '#E0F0E0'
C_FEAT = '#FDE8D0'
C_CLASS = '#E8D4E8'
C_TRAIN = '#C8E6C9'
C_TEST = '#FFCDD2'

# DDR zone colors (unified palette)
C_DRIFT  = '#D6604D'
C_INTERM = '#7570B3'
C_STAT   = '#4393C3'
C_DRIFT_BG  = '#FADAD4'
C_INTERM_BG = '#DEDCEF'
C_STAT_BG   = '#D0E4F0'

fig = plt.figure(figsize=(7.0, 3.0))
gs = GridSpec(1, 3, width_ratios=[2.2, 2.6, 2.2], wspace=0.22,
              left=0.005, right=0.995, top=0.92, bottom=0.02)


def rbox(ax, x, y, w, h, fc, ec='#CCC', lw=0.6, zorder=2, rad=0.015):
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


def arrow(ax, x0, y0, x1, y1, c='#888', lw=0.8, hw=0.05, hl=0.04):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle=f'->,head_width={hw},head_length={hl}',
                                color=c, lw=lw),
                xycoords='axes fraction', textcoords='axes fraction', zorder=3)


# ================================================================
# Panel (a): Chain Construction — iconic
# ================================================================
ax_a = fig.add_subplot(gs[0])
ax_a.set_xlim(0, 1); ax_a.set_ylim(0, 1); ax_a.axis('off')
ax_a.set_facecolor(BG); ax_a.patch.set_alpha(1.0)
tx(ax_a, 0.00, 1.07, '(a)', fontsize=9, fontweight='bold', ha='left', va='top')

cx = 0.48

# gen-0
rbox(ax_a, 0.04, 0.84, 0.88, 0.12, DEPTH_FC[0], DEPTH_EC[0], 0.8)
tx(ax_a, 0.14, 0.93, 'gen-0', fontsize=7, fontweight='bold', ha='left')
tx(ax_a, 0.82, 0.93, '(human)', fontsize=5.5, color='#999', ha='right')
tx(ax_a, cx, 0.87, '"...oxidative phosphorylation..."',
   fontsize=5.5, color='#555', style='italic')

# Arrow down
arrow(ax_a, cx, 0.83, cx, 0.77)

# Generator G box
rbox(ax_a, 0.12, 0.65, 0.72, 0.11, C_GEN, '#E6550D', 0.8)
tx(ax_a, 0.30, 0.705, r'$G$', fontsize=12, fontweight='bold', color='#BF360C')
tx(ax_a, 0.58, 0.705, 'Generator', fontsize=7, fontweight='bold', color='#BF360C')

# Recurrence arrow (right side loop)
lx = 0.88
ax_a.annotate('', xy=(lx, 0.78), xytext=(lx, 0.65),
              arrowprops=dict(arrowstyle='->,head_width=0.04,head_length=0.03',
                              connectionstyle='arc3,rad=-2.5',
                              color='#D84315', lw=0.8),
              xycoords='axes fraction', textcoords='axes fraction', zorder=4)

# gen-1
arrow(ax_a, cx, 0.64, cx, 0.56)
rbox(ax_a, 0.04, 0.44, 0.88, 0.12, DEPTH_FC[2], DEPTH_EC[2], 0.8)
tx(ax_a, 0.14, 0.53, 'gen-1', fontsize=7, fontweight='bold', ha='left')
tx(ax_a, cx, 0.47, '"...oxidative processes..."',
   fontsize=5.5, color='#555', style='italic')

# Arrow down
arrow(ax_a, cx, 0.43, cx, 0.37)

# gen-2+
rbox(ax_a, 0.04, 0.24, 0.88, 0.12, DEPTH_FC[4], '#063E78', 0.8)
tx(ax_a, 0.14, 0.33, 'gen-2+', fontsize=7, fontweight='bold', color=WHITE, ha='left')
tx(ax_a, cx, 0.27, '"...important processes..."',
   fontsize=5.5, color='#A8CCE8', style='italic')

# Formula + info
tx(ax_a, cx, 0.15, r'$x^{(k)} = G\!\left(x^{(k-1)}\right)$',
   fontsize=9, color=DARK)
tx(ax_a, cx, 0.04, '8 LLMs  |  5 families  |  0.6B–8B',
   fontsize=6, color='#999')


# ================================================================
# Panel (b): Feature Extraction — iconic pipeline
# ================================================================
ax_b = fig.add_subplot(gs[1])
ax_b.set_xlim(0, 1); ax_b.set_ylim(0, 1); ax_b.axis('off')
ax_b.set_facecolor(BG); ax_b.patch.set_alpha(1.0)
tx(ax_b, 0.00, 1.07, '(b)', fontsize=9, fontweight='bold', ha='left', va='top')

# --- Row 1: Text input ---
rbox(ax_b, 0.08, 0.84, 0.84, 0.10, '#E8E8E8', '#AAA', 0.7)
tx(ax_b, 0.18, 0.89, r'$x^{(k)}$', fontsize=9, fontweight='bold')
tx(ax_b, 0.55, 0.89, 'input text', fontsize=6.5, color='#666')

arrow(ax_b, 0.50, 0.83, 0.50, 0.77)

# --- Row 2: Reference model ---
rbox(ax_b, 0.08, 0.65, 0.84, 0.11, C_REF, '#4C72B0', 0.8)
tx(ax_b, 0.50, 0.705, 'Pythia-410M  (reference)', fontsize=7, fontweight='bold', color='#2C5290')

arrow(ax_b, 0.50, 0.64, 0.50, 0.58)

# --- Row 3: NLL distribution sketch ---
rbox(ax_b, 0.08, 0.44, 0.84, 0.13, C_NLL, '#55A868', 0.6)
tx(ax_b, 0.50, 0.555, 'per-token NLL distribution', fontsize=6.5, color='#3A7A4A')

# Small density curve sketch inside the box
curve_x = np.linspace(0.15, 0.85, 50)
curve_y = 0.46 + 0.04 * np.exp(-0.5 * ((curve_x - 0.45) / 0.12) ** 2)
ax_b.plot(curve_x, curve_y, color='#55A868', lw=1.2, zorder=4, transform=ax_b.transAxes)
ax_b.fill_between(curve_x, 0.455, curve_y, alpha=0.15, color='#55A868',
                   transform=ax_b.transAxes, zorder=4)

# --- Split arrow to three DDR groups ---
arrow(ax_b, 0.22, 0.43, 0.18, 0.37)
arrow(ax_b, 0.50, 0.43, 0.50, 0.37)
arrow(ax_b, 0.78, 0.43, 0.82, 0.37)

# --- Row 4: Three DDR zone boxes ---
# Drifting (left)
rbox(ax_b, 0.02, 0.20, 0.30, 0.16, C_DRIFT_BG, C_DRIFT, 0.8)
tx(ax_b, 0.17, 0.34, 'Drifting', fontsize=6.5, fontweight='bold', color=C_DRIFT)
tx(ax_b, 0.17, 0.285, r'$\bar{H}$, TTR', fontsize=6, color='#555')
tx(ax_b, 0.17, 0.235, 'hapax ratio', fontsize=6, color='#555')

# Intermediate (center)
rbox(ax_b, 0.35, 0.20, 0.30, 0.16, C_INTERM_BG, C_INTERM, 0.8)
tx(ax_b, 0.50, 0.34, 'Intermediate', fontsize=6.5, fontweight='bold', color=C_INTERM)
tx(ax_b, 0.50, 0.265, r'$\sigma_H$', fontsize=6.5, color='#555')

# Near-stationary (right)
rbox(ax_b, 0.68, 0.20, 0.30, 0.16, C_STAT_BG, C_STAT, 0.8)
tx(ax_b, 0.83, 0.34, 'Near-stat.', fontsize=6.5, fontweight='bold', color=C_STAT)
tx(ax_b, 0.83, 0.285, r'$H_{\max}$, $H_{\min}$', fontsize=6, color='#555')
tx(ax_b, 0.83, 0.235, r'tail decay', fontsize=6, color='#555')

# --- Merge arrows ---
arrow(ax_b, 0.17, 0.19, 0.40, 0.13)
arrow(ax_b, 0.50, 0.19, 0.50, 0.13)
arrow(ax_b, 0.83, 0.19, 0.60, 0.13)

# --- Row 5: Output ---
rbox(ax_b, 0.18, 0.02, 0.64, 0.10, C_FEAT, '#DD8452', 0.7)
tx(ax_b, 0.50, 0.07, '7 DDR features', fontsize=7.5, fontweight='bold', color='#AA6030')


# ================================================================
# Panel (c): LOGO-CV Evaluation — iconic
# ================================================================
ax_c = fig.add_subplot(gs[2])
ax_c.set_xlim(0, 1); ax_c.set_ylim(0, 1); ax_c.axis('off')
ax_c.set_facecolor(BG); ax_c.patch.set_alpha(1.0)
tx(ax_c, 0.00, 1.07, '(c)', fontsize=9, fontweight='bold', ha='left', va='top')

# --- LOGO concept: 8 generator boxes, 1 held out ---
gen_names = ['Py2.8', 'Py1B', 'OLMo', 'Q1.7', 'Q0.6', 'Q8B', 'Llm3', 'Mis7']
n_gen = 8
cols_per_row = 4
bw, bh = 0.18, 0.065
bgap_x, bgap_y = 0.04, 0.04
total_w = cols_per_row * bw + (cols_per_row - 1) * bgap_x
start_x = 0.50 - total_w / 2

held_out_idx = 5  # Qwen3-8B as example held-out

for gi in range(n_gen):
    row = gi // cols_per_row
    col = gi % cols_per_row
    bx = start_x + col * (bw + bgap_x)
    by = 0.82 - row * (bh + bgap_y)

    if gi == held_out_idx:
        rbox(ax_c, bx, by, bw, bh, C_TEST, '#E53935', 0.8, rad=0.008)
        tx(ax_c, bx + bw / 2, by + bh / 2, gen_names[gi],
           fontsize=5, fontweight='bold', color='#C62828')
    else:
        rbox(ax_c, bx, by, bw, bh, C_TRAIN, '#388E3C', 0.5, rad=0.008)
        tx(ax_c, bx + bw / 2, by + bh / 2, gen_names[gi],
           fontsize=5, color='#2E7D32')

# Labels
tx(ax_c, 0.26, 0.66, 'train (7)', fontsize=6, color='#388E3C', fontweight='bold')
tx(ax_c, 0.78, 0.66, 'test (1)', fontsize=6, color='#E53935', fontweight='bold')

# Small legend squares
rbox(ax_c, 0.12, 0.655, 0.04, 0.025, C_TRAIN, '#388E3C', 0.4, rad=0.003)
rbox(ax_c, 0.66, 0.655, 0.04, 0.025, C_TEST, '#E53935', 0.4, rad=0.003)

tx(ax_c, 0.50, 0.60, 'Leave-One-Generator-Out', fontsize=6.5,
   color='#555', style='italic')

# Arrow down
arrow(ax_c, 0.50, 0.57, 0.50, 0.50)

# XGBoost classifier
rbox(ax_c, 0.10, 0.38, 0.80, 0.11, C_CLASS, '#6A3D6A', 0.8)
tx(ax_c, 0.50, 0.435, 'XGBoost', fontsize=8, fontweight='bold', color='#4A2D4A')

# Arrow down
arrow(ax_c, 0.50, 0.37, 0.50, 0.30)

# 3-class output
cw = 0.24; ch_ = 0.07; cg = 0.02
ct = 3 * cw + 2 * cg
cx0 = 0.50 - ct / 2
cy = 0.21
for k, (cls, col, ec_idx, tc) in enumerate([
    ('gen-0', DEPTH_FC[0], 0, DARK),
    ('gen-1', DEPTH_FC[2], 2, DARK),
    ('gen-2+', DEPTH_FC[4], 4, WHITE)]):
    cxx = cx0 + k * (cw + cg)
    rbox(ax_c, cxx, cy, cw, ch_, col, DEPTH_EC[ec_idx], 0.5, rad=0.008)
    tx(ax_c, cxx + cw / 2, cy + ch_ / 2, cls, fontsize=7, color=tc, fontweight='bold')

tx(ax_c, 0.50, 0.15, 'depth prediction', fontsize=6.5, color='#888')

# Ordinal arrow under output
ax_c.annotate('', xy=(cx0 + ct - 0.02, 0.08), xytext=(cx0 + 0.02, 0.08),
              arrowprops=dict(arrowstyle='->,head_width=0.03,head_length=0.025',
                              color='#aaa', lw=0.5),
              xycoords='axes fraction', textcoords='axes fraction', zorder=3)
tx(ax_c, 0.50, 0.04, 'generation depth $d$', fontsize=6, color='#aaa')


# ================================================================
# Save
# ================================================================
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart'
os.makedirs(out_dir, exist_ok=True)
fig.savefig(f'{out_dir}/fig2_framework.pdf', format='pdf')
fig.savefig(f'{out_dir}/fig2_framework.png', format='png')
print(f'Saved fig2 v5 to {out_dir}/')

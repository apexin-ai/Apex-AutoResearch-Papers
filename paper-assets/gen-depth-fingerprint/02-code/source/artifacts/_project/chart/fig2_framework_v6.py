"""Figure 2: Gen-Depth Fingerprint Framework (v9).
Round 4: final polish — fix title wrapping, refine spacing."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif'],
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'axes.linewidth': 0.5,
    'mathtext.fontset': 'cm',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

DARK = '#333333'
WHITE = '#FFFFFF'

C_GEN0 = '#F5F0EB'; C_GEN0_EC = '#D5CFC9'
C_GEN1 = '#FDE8E0'; C_GEN1_EC = '#E8C8B8'
C_GEN2 = '#F4CCBC'; C_GEN2_EC = '#D4A898'

C_DRIFT = '#D6604D'; C_DRIFT_BG = '#FDF0ED'
C_INTERM = '#7570B3'; C_INTERM_BG = '#F0EDF5'
C_STAT = '#4393C3'; C_STAT_BG = '#EBF2F8'

C_REF = '#D4E6F1'; C_REF_EC = '#7BAED4'
C_INPUT = '#F0F0F0'; C_INPUT_EC = '#CCCCCC'
C_PILL = '#E8927C'
C_FEAT_BG = '#444444'
C_TRAIN = '#E8F5E9'; C_TRAIN_EC = '#A5D6A7'
C_TEST = '#FFEBEE'; C_TEST_EC = '#EF9A9A'
C_CLASS = '#E0E0E0'; C_CLASS_EC = '#BDBDBD'

shadow_fx = [pe.withSimplePatchShadow(offset=(1.2, -1.2), shadow_rgbFace='#888', alpha=0.10)]

fig = plt.figure(figsize=(7.2, 3.5), facecolor=WHITE)
from matplotlib.gridspec import GridSpec
gs = GridSpec(1, 3, width_ratios=[2.3, 3.2, 2.3], wspace=0.10,
              left=0.005, right=0.995, top=0.90, bottom=0.02)


def rbox(ax, x, y, w, h, fc, ec='#CCC', lw=0.6, zorder=2, rad=0.012, shadow=True):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad={rad}",
                       fc=fc, ec=ec, lw=lw, zorder=zorder,
                       transform=ax.transAxes, clip_on=False)
    if shadow:
        p.set_path_effects(shadow_fx)
    ax.add_patch(p)
    return p


def tx(ax, x, y, s, **kw):
    d = dict(ha='center', va='center', fontsize=7.5, color=DARK,
             zorder=5, transform=ax.transAxes)
    d.update(kw)
    return ax.text(x, y, s, **d)


def arrow(ax, x0, y0, x1, y1, c='#666666', lw=0.9, hw=0.04, hl=0.03):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle=f'->,head_width={hw},head_length={hl}',
                                color=c, lw=lw),
                xycoords='axes fraction', textcoords='axes fraction', zorder=3)


def pill(ax, x, y, text, bg=C_PILL, tc=WHITE, fs=7.5):
    p = FancyBboxPatch((x - 0.04, y - 0.026), 0.08, 0.052,
                       boxstyle="round,pad=0.012",
                       fc=bg, ec=bg, lw=0.3, zorder=4,
                       transform=ax.transAxes, clip_on=False)
    ax.add_patch(p)
    tx(ax, x, y, text, fontsize=fs, fontweight='bold', color=tc)


# ================================================================
# Panel (a): Recursive Generation Chain
# ================================================================
ax_a = fig.add_subplot(gs[0])
ax_a.set_xlim(0, 1); ax_a.set_ylim(0, 1); ax_a.axis('off')
ax_a.set_facecolor(WHITE)
tx(ax_a, 0.50, 1.05, '(a) Generation Chain',
   fontsize=8.5, fontweight='bold', ha='center', va='top')

cx = 0.50
bw, bh = 0.86, 0.12

# gen-0
rbox(ax_a, 0.07, 0.82, bw, bh, C_GEN0, C_GEN0_EC, 0.8)
tx(ax_a, 0.18, 0.905, 'gen-0', fontsize=8, fontweight='bold', ha='left')
tx(ax_a, 0.80, 0.905, '(human)', fontsize=5.5, color='#999', ha='right')
tx(ax_a, cx, 0.855, r'"...oxidative phosphorylation..."',
   fontsize=5, color='#888', style='italic')

arrow(ax_a, cx, 0.81, cx, 0.72)
pill(ax_a, cx, 0.765, r'$G$', fs=9)

# gen-1
rbox(ax_a, 0.07, 0.58, bw, bh, C_GEN1, C_GEN1_EC, 0.8)
tx(ax_a, 0.18, 0.665, 'gen-1', fontsize=8, fontweight='bold', ha='left')
tx(ax_a, cx, 0.615, r'"...oxidative processes..."',
   fontsize=5, color='#888', style='italic')

arrow(ax_a, cx, 0.57, cx, 0.48)
pill(ax_a, cx, 0.525, r'$G$', fs=9)

# gen-2+
rbox(ax_a, 0.07, 0.34, bw, bh, C_GEN2, C_GEN2_EC, 0.8)
tx(ax_a, 0.18, 0.425, 'gen-2+', fontsize=8, fontweight='bold', ha='left')
tx(ax_a, cx, 0.375, r'"...important processes..."',
   fontsize=5, color='#888', style='italic')

# Formula
tx(ax_a, cx, 0.21, r'$x^{(k)} = G\!\left(x^{(k-1)}\right)$',
   fontsize=10, color=DARK)
tx(ax_a, cx, 0.07, '8 LLMs  |  5 families  |  0.6B–8B',
   fontsize=5.5, color='#999')


# ================================================================
# Panel (b): Feature Extraction & DDR Partition
# ================================================================
ax_b = fig.add_subplot(gs[1])
ax_b.set_xlim(0, 1); ax_b.set_ylim(0, 1); ax_b.axis('off')
ax_b.set_facecolor(WHITE)
tx(ax_b, 0.50, 1.05, '(b) Feature Extraction & DDR Partition',
   fontsize=8.5, fontweight='bold', ha='center', va='top')

# Row 1: input text
rbox(ax_b, 0.20, 0.90, 0.60, 0.065, C_INPUT, C_INPUT_EC, 0.5)
tx(ax_b, 0.40, 0.932, r'$x^{(k)}$', fontsize=9, fontweight='bold')
tx(ax_b, 0.58, 0.932, 'input text', fontsize=6.5, color='#666')

arrow(ax_b, 0.50, 0.89, 0.50, 0.85)

# Row 2: reference model
rbox(ax_b, 0.12, 0.78, 0.76, 0.065, C_REF, C_REF_EC, 0.8)
tx(ax_b, 0.50, 0.812, 'Pythia-410M (reference)', fontsize=7.5, fontweight='bold', color='#2C5290')

arrow(ax_b, 0.50, 0.77, 0.50, 0.73)

# Row 3: NLL distribution
rbox(ax_b, 0.12, 0.64, 0.76, 0.08, WHITE, '#CCCCCC', 0.6)
tx(ax_b, 0.50, 0.698, 'per-token NLL distribution', fontsize=6.5, color='#555')

# Bell curve
curve_x = np.linspace(0.18, 0.82, 80)
curve_y = 0.655 + 0.020 * np.exp(-0.5 * ((curve_x - 0.46) / 0.10) ** 2)
ax_b.plot(curve_x, curve_y, color='#AAAAAA', lw=0.8, zorder=4, transform=ax_b.transAxes)
ax_b.fill_between(curve_x, 0.65, curve_y, alpha=0.10, color='#999',
                   transform=ax_b.transAxes, zorder=4)

# Split arrows — left and right
arrow(ax_b, 0.30, 0.63, 0.22, 0.57)
arrow(ax_b, 0.70, 0.63, 0.75, 0.57)

# DDR zone vertical extent
drift_top = 0.56
drift_h = 0.26

# LEFT: Drifting
rbox(ax_b, 0.02, drift_top - drift_h, 0.40, drift_h, C_DRIFT_BG, C_DRIFT, 1.0)
tx(ax_b, 0.22, drift_top - 0.035, 'Drifting', fontsize=7.5, fontweight='bold', color=C_DRIFT)
tx(ax_b, 0.22, drift_top - 0.09, r'$\bar{H}$ (entropy mean)', fontsize=6, color='#555')
tx(ax_b, 0.22, drift_top - 0.14, 'TTR', fontsize=6, color='#555')
tx(ax_b, 0.22, drift_top - 0.19, 'hapax ratio', fontsize=6, color='#555')

# RIGHT upper: Intermediate
int_top = 0.56
int_h = 0.10
rbox(ax_b, 0.57, int_top - int_h, 0.41, int_h, C_INTERM_BG, C_INTERM, 1.0)
tx(ax_b, 0.775, int_top - 0.035, 'Intermediate', fontsize=7, fontweight='bold', color=C_INTERM)
tx(ax_b, 0.775, int_top - 0.075, r'$\sigma_H$ (entropy std)', fontsize=6, color='#555')

# RIGHT lower: Near-stationary
stat_top = int_top - int_h - 0.02
stat_h = 0.14
rbox(ax_b, 0.57, stat_top - stat_h, 0.41, stat_h, C_STAT_BG, C_STAT, 1.0)
tx(ax_b, 0.775, stat_top - 0.035, 'Near-stationary', fontsize=7, fontweight='bold', color=C_STAT)
tx(ax_b, 0.775, stat_top - 0.08, r'$H_{\max}$,  $H_{\min}$', fontsize=6, color='#555')
tx(ax_b, 0.775, stat_top - 0.12, r'$\gamma$ (tail decay)', fontsize=6, color='#555')

# Merge arrows
feat_y = 0.12
arrow(ax_b, 0.22, drift_top - drift_h - 0.01, 0.40, feat_y + 0.02)
arrow(ax_b, 0.775, stat_top - stat_h - 0.01, 0.60, feat_y + 0.02)

# 7 DDR features box
rbox(ax_b, 0.22, 0.02, 0.56, 0.10, C_FEAT_BG, '#333', 0.8)
tx(ax_b, 0.50, 0.07, '7 DDR features', fontsize=8, fontweight='bold', color=WHITE)


# ================================================================
# Panel (c): LOGO Evaluation
# ================================================================
ax_c = fig.add_subplot(gs[2])
ax_c.set_xlim(0, 1); ax_c.set_ylim(0, 1); ax_c.axis('off')
ax_c.set_facecolor(WHITE)
tx(ax_c, 0.50, 1.05, '(c) LOGO Evaluation',
   fontsize=8.5, fontweight='bold', ha='center', va='top')

# 2x4 grid
gen_names = ['Py-2.8B', 'Py-1B', 'OLMo', 'Q-1.7B',
             'Q-0.6B', 'Q-8B', 'Llm-3', 'Mis-7']
held_out_idx = 5

bw_g, bh_g = 0.19, 0.07
gap_x, gap_y = 0.04, 0.04
total_w = 4 * bw_g + 3 * gap_x
start_x = 0.50 - total_w / 2

for gi in range(8):
    row = gi // 4
    col = gi % 4
    bx = start_x + col * (bw_g + gap_x)
    by = 0.86 - row * (bh_g + gap_y)

    if gi == held_out_idx:
        rbox(ax_c, bx, by, bw_g, bh_g, C_TEST, C_TEST_EC, 0.7, rad=0.008, shadow=False)
        tx(ax_c, bx + bw_g / 2, by + bh_g / 2, gen_names[gi],
           fontsize=5.5, color='#C62828')
    else:
        rbox(ax_c, bx, by, bw_g, bh_g, C_TRAIN, C_TRAIN_EC, 0.4, rad=0.008, shadow=False)
        tx(ax_c, bx + bw_g / 2, by + bh_g / 2, gen_names[gi],
           fontsize=5.5, color='#2E7D32')

# Legend
rbox(ax_c, 0.10, 0.69, 0.04, 0.025, C_TRAIN, C_TRAIN_EC, 0.3, rad=0.003, shadow=False)
tx(ax_c, 0.22, 0.702, 'train (7)', fontsize=5.5, color='#388E3C', fontweight='bold', ha='left')
rbox(ax_c, 0.58, 0.69, 0.04, 0.025, C_TEST, C_TEST_EC, 0.3, rad=0.003, shadow=False)
tx(ax_c, 0.70, 0.702, 'test (1)', fontsize=5.5, color='#E53935', fontweight='bold', ha='left')

tx(ax_c, 0.50, 0.64, 'Leave-One-Generator-Out', fontsize=6.5,
   color='#555', style='italic')

arrow(ax_c, 0.50, 0.60, 0.50, 0.55)

# XGBoost
rbox(ax_c, 0.12, 0.44, 0.76, 0.10, C_CLASS, C_CLASS_EC, 0.8)
tx(ax_c, 0.50, 0.49, 'XGBoost', fontsize=9, fontweight='bold', color='#555')

arrow(ax_c, 0.50, 0.43, 0.50, 0.37)

# 3-class output
cw = 0.24; ch_ = 0.08; cg = 0.02
ct = 3 * cw + 2 * cg
cx0 = 0.50 - ct / 2
cy = 0.27

for k, (cls, col, ec) in enumerate([
    ('gen-0', C_GEN0, C_GEN0_EC),
    ('gen-1', C_GEN1, C_GEN1_EC),
    ('gen-2+', C_GEN2, C_GEN2_EC)]):
    cxx = cx0 + k * (cw + cg)
    rbox(ax_c, cxx, cy, cw, ch_, col, ec, 0.6, rad=0.008, shadow=False)
    tx(ax_c, cxx + cw / 2, cy + ch_ / 2, cls, fontsize=7, fontweight='bold')

tx(ax_c, 0.50, 0.20, 'depth prediction', fontsize=6.5, color='#888')

ax_c.annotate('', xy=(cx0 + ct - 0.02, 0.12), xytext=(cx0 + 0.02, 0.12),
              arrowprops=dict(arrowstyle='->,head_width=0.03,head_length=0.025',
                              color='#aaa', lw=0.5),
              xycoords='axes fraction', textcoords='axes fraction', zorder=3)
tx(ax_c, 0.50, 0.07, r'generation depth $d$', fontsize=6, color='#aaa')


# ================================================================
# Panel separators
# ================================================================
for ax_left, ax_right in [(ax_a, ax_b), (ax_b, ax_c)]:
    bbox_l = ax_left.get_position()
    bbox_r = ax_right.get_position()
    sep_x = (bbox_l.x1 + bbox_r.x0) / 2
    fig.add_artist(plt.Line2D([sep_x, sep_x], [0.05, 0.90],
                              color='#CCCCCC', linewidth=0.5, linestyle='--',
                              transform=fig.transFigure, zorder=1))

# ================================================================
# Save
# ================================================================
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart'
os.makedirs(out_dir, exist_ok=True)
fig.savefig(f'{out_dir}/fig2_framework.pdf', format='pdf')
fig.savefig(f'{out_dir}/fig2_framework.png', format='png')
print(f'Saved fig2 v9 to {out_dir}/')

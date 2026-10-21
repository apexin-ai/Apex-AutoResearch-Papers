import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe

matplotlib.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

BLUE = '#2166ac'
BLUE_FILL = '#ECF1F8'
AMBER = '#B8860B'
AMBER_FILL = '#FFF8EC'
GRAY = '#666666'
GRAY_LIGHT = '#999999'
DARK = '#1a1a1a'
GREEN = '#2E7D32'
GREEN_FILL = '#ECF6EC'
RED = '#b2182b'
RED_FILL = '#FDECEC'
WHITE = '#FFFFFF'
ARROW_COLOR = '#555555'

FW = 3.25
FH = 3.85

fig, ax = plt.subplots(figsize=(FW, FH))
ax.set_xlim(0, FW)
ax.set_ylim(0, FH)
ax.axis('off')
fig.patch.set_facecolor('white')

M = 0.06
HGAP = 0.22
BW = (FW - 2*M - HGAP) / 2
BH_IO = 0.82
BH_MID = 1.08
VGAP = 0.30

y3 = M + 0.02
y2 = y3 + BH_IO + VGAP
y1 = y2 + BH_MID + VGAP

x_left = M
x_right = M + BW + HGAP
x_mid = M

def draw_box(x, y, w, h, fill, edge, lw=0.8):
    box = FancyBboxPatch((x, y), w, h,
                          boxstyle="round,pad=0.08,rounding_size=0.10",
                          facecolor=fill, edgecolor=edge, linewidth=lw,
                          zorder=2, clip_on=False)
    ax.add_patch(box)

def draw_arrow(x1, y1, x2, y2, color=ARROW_COLOR, lw=0.9):
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                             arrowstyle='->', mutation_scale=10,
                             linewidth=lw, color=color, zorder=3)
    ax.add_patch(arrow)

cx_l = x_left + BW/2
cx_r = x_right + BW/2
mid_w = FW - 2*M
cx_m = x_mid + mid_w/2

# ── ROW 1: INPUTS ──
draw_box(x_left, y1, BW, BH_IO, BLUE_FILL, BLUE)
ax.text(cx_l, y1 + BH_IO - 0.20, 'Target LLM', ha='center', va='center',
        fontsize=8, fontweight='bold', color=DARK)
ax.text(cx_l, y1 + BH_IO - 0.46, 'Binary responses only', ha='center', va='center',
        fontsize=6.5, color='#555555')
ax.text(cx_l, y1 + BH_IO - 0.67, r'$\mathbf{x} = (x_1, \ldots, x_n)$', ha='center', va='center',
        fontsize=7, color=BLUE)

draw_box(x_right, y1, BW, BH_IO, AMBER_FILL, AMBER)
ax.text(cx_r, y1 + BH_IO - 0.20, 'PSN-IRT Item Bank', ha='center', va='center',
        fontsize=8, fontweight='bold', color=DARK)
ax.text(cx_r, y1 + BH_IO - 0.46, 'Pre-calibrated 4PL', ha='center', va='center',
        fontsize=6.5, color='#555555')
ax.text(cx_r, y1 + BH_IO - 0.67, r'$(a_i, b_i, c_i, d_i)$', ha='center', va='center',
        fontsize=7, color=AMBER)

# ── ROW 2: PROCESSING ──
draw_box(x_mid, y2, mid_w, BH_MID, WHITE, BLUE, lw=1.1)
ax.text(cx_m, y2 + BH_MID - 0.19, r'$\ell_z^*$ Person-Fit Analysis', ha='center', va='center',
        fontsize=8.5, fontweight='bold', color=BLUE)
ax.text(cx_m, y2 + BH_MID - 0.46, r'$\hat{\theta}_{\mathrm{MLE}}$ ability estimation', ha='center', va='center',
        fontsize=6.5, color='#555555')
ax.text(cx_m, y2 + BH_MID - 0.72, r'$\Delta\ell_z^* = \ell_{z,\mathrm{test}}^* - \bar{\ell}_{z,\mathrm{clean}}^*$',
        ha='center', va='center', fontsize=7.5, color=DARK)
ax.text(cx_m, y2 + BH_MID - 0.95, 'Matched-difference design', ha='center', va='center',
        fontsize=6.5, color=GRAY_LIGHT, fontstyle='italic')

# ── ROW 3: OUTPUTS ──
draw_box(x_left, y3, BW, BH_IO, GREEN_FILL, GREEN)
ax.text(cx_l, y3 + BH_IO - 0.20, 'Detection', ha='center', va='center',
        fontsize=8, fontweight='bold', color=GREEN)
ax.text(cx_l, y3 + BH_IO - 0.46, r"Cohen's $d$ effect size", ha='center', va='center',
        fontsize=6.5, color='#555555')
ax.text(cx_l, y3 + BH_IO - 0.67, 'Bootstrap 95% CI', ha='center', va='center',
        fontsize=6.5, color='#555555')

draw_box(x_right, y3, BW, BH_IO, RED_FILL, RED)
ax.text(cx_r, y3 + BH_IO - 0.20, 'Diagnosis', ha='center', va='center',
        fontsize=8, fontweight='bold', color=RED)
ax.text(cx_r, y3 + BH_IO - 0.46, r'$\theta$-shift analysis', ha='center', va='center',
        fontsize=6.5, color='#555555')
ax.text(cx_r, y3 + BH_IO - 0.67, 'Seen/unseen decomposition', ha='center', va='center',
        fontsize=6.5, color='#555555')

# ── ARROWS ──
a_off = 0.06
converge_l = cx_m - 0.35
converge_r = cx_m + 0.35
draw_arrow(cx_l, y1 - a_off, converge_l, y2 + BH_MID + a_off)
draw_arrow(cx_r, y1 - a_off, converge_r, y2 + BH_MID + a_off)
draw_arrow(converge_l - 0.02, y2 - a_off, cx_l, y3 + BH_IO + a_off)
draw_arrow(converge_r + 0.02, y2 - a_off, cx_r, y3 + BH_IO + a_off)

# ── ANNOTATION ──
ann_y = y1 + BH_IO + 0.10
ax.text(FW/2, ann_y, r'No weights, logits, or training data required',
        ha='center', va='bottom', fontsize=6.5, color='#777777', fontstyle='italic',
        path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])

from pathlib import Path
out = Path(__file__).resolve().parent
fig.savefig(out / 'fig_method_pipeline.pdf', format='pdf')
fig.savefig(out / 'fig_method_pipeline.png', format='png')
plt.close()
print("Done. Files saved.")

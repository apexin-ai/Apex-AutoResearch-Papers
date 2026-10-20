"""Generate RASP method framework figure (Fig. 1)."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np

# === Colors ===
CKA_TEAL = '#009E73'
STD_PINK = '#CC79A7'
RAND_GOLD = '#E69F00'
RASP_RED = '#D55E00'

STAGE1_BG = '#EDE7F6'   # lavender
STAGE1_BD = '#9575CD'
STAGE2_BG = '#FFF3E0'   # peach
STAGE2_BD = '#FFB74D'
STAGE3_BG = '#E8F5E9'   # mint
STAGE3_BD = '#66BB6A'

ARROW_CLR = '#455A64'
TEXT_CLR = '#212121'
FORMULA_CLR = '#37474F'

fig, ax = plt.subplots(1, 1, figsize=(14, 5.5))
ax.set_xlim(0, 14)
ax.set_ylim(0, 5.5)
ax.axis('off')
fig.patch.set_facecolor('white')

# ── Helper ──
def rounded_box(ax, x, y, w, h, bg, bd, label, label_size=10):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                         facecolor=bg, edgecolor=bd, linewidth=1.5, zorder=2)
    ax.add_patch(box)
    ax.text(x + w/2, y + h - 0.22, label, ha='center', va='top',
            fontsize=label_size, fontweight='bold', color=TEXT_CLR, zorder=3)
    return box

def arrow(ax, x1, y1, x2, y2, color=ARROW_CLR, style='->', lw=1.8):
    a = FancyArrowPatch((x1, y1), (x2, y2),
                        arrowstyle=style, color=color, lw=lw,
                        mutation_scale=14, zorder=4)
    ax.add_patch(a)

# ══════════════ STAGE 1: Pruning Score Computation ══════════════
s1_x, s1_y, s1_w, s1_h = 0.3, 1.6, 4.0, 3.4
rounded_box(ax, s1_x, s1_y, s1_w, s1_h, STAGE1_BG, STAGE1_BD,
            'Stage 1: Pruning Score', label_size=10.5)

# Taylor Importance I(h)
ti_cx, ti_cy = 1.1, 3.8
ti_circle = plt.Circle((ti_cx, ti_cy), 0.42, fc='#BBDEFB', ec='#1976D2', lw=1.3, zorder=3)
ax.add_patch(ti_circle)
ax.text(ti_cx, ti_cy + 0.05, r'$I(h)$', ha='center', va='center', fontsize=11,
        fontweight='bold', color='#1565C0', zorder=4)
ax.text(ti_cx, ti_cy - 0.62, 'Taylor\nImportance', ha='center', va='top', fontsize=7.5,
        color='#1565C0', zorder=4)

# CKA Overlap F(h)
ck_cx, ck_cy = 2.7, 3.8
ck_circle = plt.Circle((ck_cx, ck_cy), 0.42, fc='#C8E6C9', ec=CKA_TEAL, lw=1.3, zorder=3)
ax.add_patch(ck_circle)
ax.text(ck_cx, ck_cy + 0.05, r'$F(h)$', ha='center', va='center', fontsize=11,
        fontweight='bold', color=CKA_TEAL, zorder=4)
ax.text(ck_cx, ck_cy - 0.62, 'CKA\nOverlap', ha='center', va='top', fontsize=7.5,
        color=CKA_TEAL, zorder=4)

# Merge arrows into composite score
merge_x, merge_y = 1.9, 2.55
# I(h) arrow
arrow(ax, ti_cx + 0.3, ti_cy - 0.42, merge_x - 0.15, merge_y + 0.25)
# F(h) arrow
arrow(ax, ck_cx - 0.3, ck_cy - 0.42, merge_x + 0.15, merge_y + 0.25)

# Composite score box
score_box = FancyBboxPatch((0.65, 1.9), 3.3, 0.65, boxstyle="round,pad=0.1",
                           facecolor='#FFF8E1', edgecolor='#F9A825', linewidth=1.2, zorder=3)
ax.add_patch(score_box)
ax.text(2.3, 2.22, r'$S(h) = I(h) \times \left(1 - F(h)\right)^{\alpha}$',
        ha='center', va='center', fontsize=11, color=FORMULA_CLR, zorder=4,
        math_fontfamily='cm')

# Alpha annotation
ax.text(3.7, 1.78, r'$\alpha$ controls balance', ha='center', va='top', fontsize=8.5,
        style='italic', color='#F57F17', zorder=4)

# ══════════════ STAGE 2: Structure Removal ══════════════
s2_x, s2_y, s2_w, s2_h = 5.0, 1.6, 3.8, 3.4
rounded_box(ax, s2_x, s2_y, s2_w, s2_h, STAGE2_BG, STAGE2_BD,
            'Stage 2: Structure Removal', label_size=10.5)

# Layer bars
n_layers = 28
bar_x0 = 5.35
bar_w = 3.1
bar_height = 0.07
bar_gap = 0.075
bar_y0 = 2.0

np.random.seed(42)
retain_fracs = np.clip(np.random.beta(3, 1.5, n_layers), 0.4, 1.0)

for i in range(n_layers):
    y = bar_y0 + i * bar_gap
    rf = retain_fracs[i]
    # retained portion
    ax.barh(y, rf * bar_w, height=bar_height, left=bar_x0,
            color=CKA_TEAL, alpha=0.75, edgecolor='none', zorder=3)
    # removed portion
    ax.barh(y, (1-rf) * bar_w, height=bar_height, left=bar_x0 + rf * bar_w,
            color='#BDBDBD', alpha=0.5, edgecolor='none', zorder=3)

# Floor line at 40%
floor_x = bar_x0 + 0.4 * bar_w
ax.plot([floor_x, floor_x], [bar_y0 - 0.05, bar_y0 + n_layers * bar_gap + 0.02],
        '--', color=RASP_RED, lw=1.0, alpha=0.8, zorder=4)
ax.text(floor_x - 0.05, bar_y0 - 0.15, r'$\tau \geq 40\%$', ha='center', va='top',
        fontsize=7.5, color=RASP_RED, zorder=4)

# Labels
ax.text(6.9, 4.55, 'Remove lowest $S(h)$ groups', ha='center', va='top',
        fontsize=8.5, color=TEXT_CLR, zorder=4)

# Legend for bars
ax.barh(0, 0, color=CKA_TEAL, alpha=0.75, label='Retained')
ax.barh(0, 0, color='#BDBDBD', alpha=0.5, label='Removed')
leg = ax.legend(loc='lower right', bbox_to_anchor=(8.6, 1.65), fontsize=7,
                frameon=False, ncol=1, handlelength=1.0,
                bbox_transform=ax.transData)

# ══════════════ STAGE 3: Recovery Training ══════════════
s3_x, s3_y, s3_w, s3_h = 9.5, 1.6, 4.1, 3.4
rounded_box(ax, s3_x, s3_y, s3_w, s3_h, STAGE3_BG, STAGE3_BD,
            'Stage 3: Recovery Training', label_size=10.5)

# SFT box
sft_box = FancyBboxPatch((10.0, 3.7), 1.2, 0.55, boxstyle="round,pad=0.08",
                         facecolor='#B2DFDB', edgecolor=CKA_TEAL, linewidth=1.2, zorder=3)
ax.add_patch(sft_box)
ax.text(10.6, 3.97, 'SFT', ha='center', va='center', fontsize=10,
        fontweight='bold', color=CKA_TEAL, zorder=4)

# GRPO box
grpo_box = FancyBboxPatch((10.0, 2.85), 1.2, 0.55, boxstyle="round,pad=0.08",
                          facecolor='#FFF9C4', edgecolor=RAND_GOLD, linewidth=1.2, zorder=3)
ax.add_patch(grpo_box)
ax.text(10.6, 3.12, 'GRPO', ha='center', va='center', fontsize=10,
        fontweight='bold', color='#E65100', zorder=4)

# Convergence point
conv_x, conv_y = 12.5, 3.4
conv_circle = plt.Circle((conv_x, conv_y), 0.35, fc='white', ec=STAGE3_BD,
                         lw=1.5, zorder=3)
ax.add_patch(conv_circle)
ax.text(conv_x, conv_y, '≈', ha='center', va='center', fontsize=18,
        fontweight='bold', color=STAGE3_BD, zorder=4)

# Arrows from SFT/GRPO to convergence
arrow(ax, 11.2, 3.97, conv_x - 0.35, conv_y + 0.12, color=CKA_TEAL)
arrow(ax, 11.2, 3.12, conv_x - 0.35, conv_y - 0.12, color=RAND_GOLD)

# Delta annotation
ax.text(conv_x, conv_y - 0.55, r'$|\Delta| \leq 0.61$ pp', ha='center', va='top',
        fontsize=9.5, color='#424242', style='italic', zorder=4,
        bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='#9E9E9E', alpha=0.8))

# "Decoupling" annotation
ax.text(conv_x, 2.15, 'Recovery method\n≈ interchangeable', ha='center', va='top',
        fontsize=9.5, color='#616161', style='italic', zorder=4)

# ══════════════ STAGE ARROWS ══════════════
arrow(ax, s1_x + s1_w + 0.05, 3.3, s2_x - 0.05, 3.3, lw=2.2)
arrow(ax, s2_x + s2_w + 0.05, 3.3, s3_x - 0.05, 3.3, lw=2.2)

# ══════════════ RECOVERY CAPACITY SPECTRUM ══════════════
grad_y, grad_h = 0.6, 0.35
grad_x0, grad_w = 0.5, 13.0
gradient = np.linspace(0, 1, 256).reshape(1, -1)

# Create colormap from teal to red-orange
from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list('recovery', [CKA_TEAL, '#BBBBBB', STD_PINK])
ax.imshow(gradient, aspect='auto', cmap=cmap,
          extent=[grad_x0, grad_x0 + grad_w, grad_y, grad_y + grad_h], zorder=3)

# Border
grad_rect = plt.Rectangle((grad_x0, grad_y), grad_w, grad_h, fill=False,
                           edgecolor='#9E9E9E', lw=0.8, zorder=4)
ax.add_patch(grad_rect)

# Labels
ax.text(grad_x0 + 0.15, grad_y + grad_h/2, '0.354', ha='left', va='center',
        fontsize=8.5, fontweight='bold', color='white', zorder=5,
        path_effects=[pe.withStroke(linewidth=2, foreground='black')])
ax.text(grad_x0 + grad_w - 0.15, grad_y + grad_h/2, '0.061', ha='right', va='center',
        fontsize=8.5, fontweight='bold', color='white', zorder=5,
        path_effects=[pe.withStroke(linewidth=2, foreground='black')])

ax.text(grad_x0, grad_y - 0.08, 'CKA-aware:\nDiverse', ha='left', va='top',
        fontsize=8, color=CKA_TEAL, fontweight='bold', zorder=4)
ax.text(grad_x0 + grad_w, grad_y - 0.08, 'Composite:\nCollapse', ha='right', va='top',
        fontsize=8, color=STD_PINK, fontweight='bold', zorder=4)
ax.text(grad_x0 + grad_w/2, grad_y + grad_h + 0.12, 'Recovery Capacity Spectrum',
        ha='center', va='bottom', fontsize=9, fontweight='bold', color=TEXT_CLR, zorder=4)

# Arrow showing direction
ax.annotate('', xy=(grad_x0 + grad_w - 0.3, grad_y - 0.02),
            xytext=(grad_x0 + 0.3, grad_y - 0.02),
            arrowprops=dict(arrowstyle='->', color='#757575', lw=1.0), zorder=4)
ax.text(grad_x0 + grad_w/2, grad_y - 0.12, 'Representational Diversity →',
        ha='center', va='top', fontsize=8, color='#757575', style='italic', zorder=4)

plt.tight_layout(pad=0.3)
out = '/root/recovery_aware_struct_prune/docs/paper/figures/paper/fig1_method_framework.png'
plt.savefig(out, dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.2)
plt.savefig(out.replace('.png', '.pdf'), bbox_inches='tight', facecolor='white', pad_inches=0.2)
print(f"Saved to {out}")
print(f"Saved to {out.replace('.png', '.pdf')}")

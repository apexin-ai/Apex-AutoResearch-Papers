#!/usr/bin/env python3
"""Fig 1 Version A: Information-dense 3-panel VLA concept figure with numerical annotations."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

OUTPUT_PATH = "/tmp/fig_overview_hybrid_vA.png"

# === Color palette ===
sky_blue = '#B8D4E8'
salmon = '#F4A582'
mint = '#A6DBA0'
gold = '#FDB863'
lavender = '#C7B8E8'
rose = '#E7B8D4'
light_gray = '#F0F0F0'
dark_gray = '#4A4A4A'
soft_red = '#E07070'
soft_green = '#7CB97C'
shadow_color = '#D0D0D0'

fig = plt.figure(figsize=(14, 4.8), dpi=300, facecolor='white')

def draw_shadow_box(ax, xy, width, height, color, boxstyle="round,pad=0.02",
                    linewidth=0.8, edgecolor='#CCCCCC', alpha=1.0, zorder=2):
    sx, sy = xy
    shadow = FancyBboxPatch((sx + 0.007, sy - 0.007), width, height,
                            boxstyle=boxstyle, facecolor=shadow_color, alpha=0.3,
                            edgecolor='none', zorder=zorder - 1,
                            transform=ax.transAxes)
    ax.add_patch(shadow)
    box = FancyBboxPatch((sx, sy), width, height,
                         boxstyle=boxstyle, facecolor=color, alpha=alpha,
                         edgecolor=edgecolor, linewidth=linewidth, zorder=zorder,
                         transform=ax.transAxes)
    ax.add_patch(box)
    return box

def draw_circle_number(ax, x, y, num, color, radius=0.025, fontsize=10, zorder=5):
    circle = Circle((x, y), radius, facecolor=color, edgecolor='white',
                    linewidth=1.2, zorder=zorder, transform=ax.transAxes)
    ax.add_patch(circle)
    ax.text(x, y, str(num), ha='center', va='center', fontsize=fontsize,
            fontweight='bold', color='white', zorder=zorder + 1, transform=ax.transAxes)

# ============================================================
# Panel (a): VLA sequence structure
# ============================================================
ax_a = fig.add_axes([0.02, 0.06, 0.28, 0.88])
ax_a.set_xlim(0, 1)
ax_a.set_ylim(0, 1)
ax_a.axis('off')
ax_a.text(0.02, 0.96, '(a)', fontsize=13, fontweight='bold', color=dark_gray,
          family='DejaVu Serif', transform=ax_a.transAxes)
ax_a.text(0.15, 0.96, 'VLA sequence structure', fontsize=10, color=dark_gray,
          family='DejaVu Serif', transform=ax_a.transAxes)

# Image tokens region (dashed border)
img_box = FancyBboxPatch((0.06, 0.76), 0.72, 0.16, boxstyle="round,pad=0.02",
                         facecolor=sky_blue, alpha=0.2, edgecolor=sky_blue,
                         linewidth=1.5, linestyle='--', zorder=2,
                         transform=ax_a.transAxes)
ax_a.add_patch(img_box)
ax_a.text(0.42, 0.89, 'Image tokens', ha='center', fontsize=9, fontweight='bold',
          color=dark_gray, family='DejaVu Sans', transform=ax_a.transAxes)
for i, xp in enumerate([0.14, 0.28, 0.42, 0.56]):
    sq = FancyBboxPatch((xp, 0.78), 0.08, 0.07, boxstyle="round,pad=0.005",
                        facecolor=sky_blue, edgecolor='#8BB8D4', linewidth=0.8,
                        zorder=3, transform=ax_a.transAxes)
    ax_a.add_patch(sq)

# image_mean label
ax_a.text(0.42, 0.73, 'image_mean (avg pooling)', ha='center', fontsize=7,
          fontstyle='italic', color='#888888', family='DejaVu Sans',
          transform=ax_a.transAxes)

# Downward arrow from image
ax_a.annotate('', xy=(0.42, 0.68), xytext=(0.42, 0.74),
              arrowprops=dict(arrowstyle='->', color='#AAAAAA', lw=1.2),
              transform=ax_a.transAxes)

# X mark + "cannot attend to instruction"
ax_a.text(0.12, 0.66, '✗', fontsize=13, color=soft_red, fontweight='bold',
          ha='center', va='center', transform=ax_a.transAxes, zorder=5)
ax_a.text(0.19, 0.66, 'cannot attend to instruction', fontsize=6.5,
          fontstyle='italic', color=soft_red, va='center', family='DejaVu Sans',
          transform=ax_a.transAxes)

# Instruction tokens region (dashed border)
inst_box = FancyBboxPatch((0.06, 0.47), 0.72, 0.14, boxstyle="round,pad=0.02",
                          facecolor=gold, alpha=0.2, edgecolor=gold,
                          linewidth=1.5, linestyle='--', zorder=2,
                          transform=ax_a.transAxes)
ax_a.add_patch(inst_box)
ax_a.text(0.42, 0.57, 'Instruction tokens', ha='center', fontsize=9,
          fontweight='bold', color=dark_gray, family='DejaVu Sans',
          transform=ax_a.transAxes)
ax_a.text(0.42, 0.50, 'pick up the red block', ha='center', fontsize=7.5,
          fontstyle='italic', color='#666666', family='DejaVu Sans',
          transform=ax_a.transAxes)

# Curved arrow on right side: "attends to all context"
ax_a.annotate('', xy=(0.80, 0.84), xytext=(0.80, 0.52),
              arrowprops=dict(arrowstyle='->', color=soft_green, lw=1.5,
                              connectionstyle='arc3,rad=-0.4'),
              transform=ax_a.transAxes)
ax_a.text(0.93, 0.70, 'attends\nto all\ncontext', fontsize=6, color=soft_green,
          fontstyle='italic', ha='center', va='center', family='DejaVu Sans',
          transform=ax_a.transAxes, linespacing=1.2)

# Downward arrow from instruction
ax_a.annotate('', xy=(0.42, 0.38), xytext=(0.42, 0.46),
              arrowprops=dict(arrowstyle='->', color='#AAAAAA', lw=1.2),
              transform=ax_a.transAxes)

# Bottom: R and Act boxes
draw_shadow_box(ax_a, (0.08, 0.17), 0.28, 0.17, lavender, linewidth=1.0, edgecolor='#A89CC8')
ax_a.text(0.22, 0.27, 'R', ha='center', va='center', fontsize=15, fontweight='bold',
          color='white', family='DejaVu Serif', transform=ax_a.transAxes)
ax_a.text(0.22, 0.12, 'readout\n(last pre-action)', ha='center', fontsize=6.5,
          fontstyle='italic', color='#888888', family='DejaVu Sans',
          transform=ax_a.transAxes, linespacing=1.2)

draw_shadow_box(ax_a, (0.48, 0.17), 0.28, 0.17, mint, linewidth=1.0, edgecolor='#7CB97C')
ax_a.text(0.62, 0.27, 'Act', ha='center', va='center', fontsize=15, fontweight='bold',
          color='white', family='DejaVu Serif', transform=ax_a.transAxes)
ax_a.text(0.62, 0.12, 'action', ha='center', fontsize=6.5,
          fontstyle='italic', color='#888888', family='DejaVu Sans',
          transform=ax_a.transAxes)

# Arrow R → Act
ax_a.annotate('', xy=(0.48, 0.255), xytext=(0.38, 0.255),
              arrowprops=dict(arrowstyle='->', color='#999999', lw=1.2),
              transform=ax_a.transAxes)

# ============================================================
# Panel (b): Three analysis methods
# ============================================================
ax_b = fig.add_axes([0.33, 0.06, 0.35, 0.88])
ax_b.set_xlim(0, 1)
ax_b.set_ylim(0, 1)
ax_b.axis('off')
ax_b.text(0.02, 0.96, '(b)', fontsize=13, fontweight='bold', color=dark_gray,
          family='DejaVu Serif', transform=ax_b.transAxes)
ax_b.text(0.12, 0.96, 'Three analysis methods', fontsize=10, color=dark_gray,
          family='DejaVu Serif', transform=ax_b.transAxes)

# --- Method 1: Layer-wise action probes ---
draw_circle_number(ax_b, 0.04, 0.88, '1', sky_blue, radius=0.022)
ax_b.text(0.09, 0.88, 'Layer-wise action probes', fontsize=9, fontweight='bold',
          va='center', color=dark_gray, family='DejaVu Sans', transform=ax_b.transAxes)

for i, (lbl, xp) in enumerate(zip(['L₁', 'L₂', 'L₃'], [0.06, 0.17, 0.28])):
    draw_shadow_box(ax_b, (xp, 0.76), 0.09, 0.07, sky_blue, linewidth=0.6)
    ax_b.text(xp + 0.045, 0.795, lbl, ha='center', va='center', fontsize=8,
              color=dark_gray, family='DejaVu Sans', transform=ax_b.transAxes)

ax_b.annotate('', xy=(0.42, 0.795), xytext=(0.38, 0.795),
              arrowprops=dict(arrowstyle='->', color='#999999', lw=1.0),
              transform=ax_b.transAxes)

draw_shadow_box(ax_b, (0.42, 0.76), 0.13, 0.07, 'white', linewidth=0.8, edgecolor='#AAAAAA')
ax_b.text(0.485, 0.795, 'Probe', ha='center', va='center', fontsize=8,
          color=dark_gray, family='DejaVu Sans', transform=ax_b.transAxes)

ax_b.annotate('', xy=(0.60, 0.795), xytext=(0.56, 0.795),
              arrowprops=dict(arrowstyle='->', color='#999999', lw=1.0),
              transform=ax_b.transAxes)

draw_shadow_box(ax_b, (0.60, 0.76), 0.13, 0.07, 'white', linewidth=0.8, edgecolor='#AAAAAA')
ax_b.text(0.665, 0.795, '7-DoF', ha='center', va='center', fontsize=8,
          color=dark_gray, family='DejaVu Sans', transform=ax_b.transAxes)

r2_circle = Circle((0.82, 0.795), 0.025, facecolor=salmon, edgecolor='white',
                    linewidth=1.0, zorder=5, transform=ax_b.transAxes)
ax_b.add_patch(r2_circle)
ax_b.text(0.82, 0.795, 'R²', ha='center', va='center', fontsize=7,
          fontweight='bold', color='white', zorder=6, transform=ax_b.transAxes)

ax_b.text(0.06, 0.72, 'Peak mid-layers → exit collapse (ΔR² = 0.15–0.69)',
          fontsize=7, fontstyle='italic', color='#888888', family='DejaVu Sans',
          transform=ax_b.transAxes)

ax_b.plot([0.04, 0.96], [0.68, 0.68], color='#E0E0E0', linewidth=0.6,
          transform=ax_b.transAxes, zorder=1)

# --- Method 2: Counterfactual perturbation ---
draw_circle_number(ax_b, 0.04, 0.60, '2', salmon, radius=0.022)
ax_b.text(0.09, 0.60, 'Counterfactual perturbation', fontsize=9, fontweight='bold',
          va='center', color=dark_gray, family='DejaVu Sans', transform=ax_b.transAxes)

pills = [
    ('✓ correct', mint),
    ('∅ empty', '#E8E8E8'),
    ('✗ wrong', salmon),
    ('◇ shuffle', gold),
    ('~ paraph.', lavender),
]
pill_x = 0.04
for label, color in pills:
    pw = 0.155
    draw_shadow_box(ax_b, (pill_x, 0.49), pw, 0.06, color,
                    boxstyle="round,pad=0.008", linewidth=0.5, edgecolor='#CCCCCC')
    ax_b.text(pill_x + pw / 2, 0.52, label, ha='center', va='center', fontsize=6.2,
              color=dark_gray, family='DejaVu Sans', transform=ax_b.transAxes)
    pill_x += pw + 0.015

ax_b.annotate('', xy=(0.92, 0.52), xytext=(0.87, 0.52),
              arrowprops=dict(arrowstyle='->', color='#999999', lw=1.0),
              transform=ax_b.transAxes)
ax_b.text(0.96, 0.52, 'Δact', ha='center', va='center', fontsize=7.5,
          fontweight='bold', color=dark_gray, family='DejaVu Sans',
          transform=ax_b.transAxes)

ax_b.text(0.06, 0.44, "Cohen's d = 0.45–1.52, ordered by semantic distance",
          fontsize=7, fontstyle='italic', color='#888888', family='DejaVu Sans',
          transform=ax_b.transAxes)

ax_b.plot([0.04, 0.96], [0.39, 0.39], color='#E0E0E0', linewidth=0.6,
          transform=ax_b.transAxes, zorder=1)

# --- Method 3: L1 attention profiling ---
draw_circle_number(ax_b, 0.04, 0.32, '3', gold, radius=0.022)
ax_b.text(0.09, 0.32, 'L1 attention profiling', fontsize=9, fontweight='bold',
          va='center', color=dark_gray, family='DejaVu Sans', transform=ax_b.transAxes)

# Mini heatmap — positioned within panel (b)
heatmap_data = np.array([
    [0.2, 0.4, 0.3, 0.5, 0.2],
    [0.3, 0.5, 0.2, 0.4, 0.3],
    [0.8, 0.9, 0.7, 0.6, 0.85],
    [0.15, 0.2, 0.85, 0.9, 0.7],
])
ax_hm = fig.add_axes([0.39, 0.165, 0.09, 0.135])
ax_hm.imshow(heatmap_data, cmap='Blues', aspect='auto', vmin=0, vmax=1)
ax_hm.set_yticks([0, 1, 2, 3])
ax_hm.set_yticklabels(['img', 'img', 'inst', 'ro'], fontsize=5.5, color=dark_gray,
                       family='DejaVu Sans')
ax_hm.set_xticks([])
ax_hm.tick_params(length=0, pad=1)
for spine in ax_hm.spines.values():
    spine.set_linewidth(0.5)
    spine.set_color('#CCCCCC')

# Legend
ax_b.plot([0.54, 0.61], [0.24, 0.24], color=sky_blue, linewidth=2.0,
          transform=ax_b.transAxes, zorder=3)
ax_b.text(0.62, 0.24, 'readout→instr.', fontsize=6.5, va='center',
          color=dark_gray, family='DejaVu Sans', transform=ax_b.transAxes)
ax_b.plot([0.54, 0.61], [0.18, 0.18], color=salmon, linewidth=2.0,
          transform=ax_b.transAxes, zorder=3)
ax_b.text(0.62, 0.18, 'readout→image', fontsize=6.5, va='center',
          color=dark_gray, family='DejaVu Sans', transform=ax_b.transAxes)

ax_b.text(0.06, 0.06, '24–32/32 heads instruction-dominant at L1',
          fontsize=7, fontstyle='italic', color='#888888', family='DejaVu Sans',
          transform=ax_b.transAxes)

# ============================================================
# Panel (c): Finding classification
# ============================================================
ax_c = fig.add_axes([0.71, 0.06, 0.27, 0.88])
ax_c.set_xlim(0, 1)
ax_c.set_ylim(0, 1)
ax_c.axis('off')
ax_c.text(0.02, 0.96, '(c)', fontsize=13, fontweight='bold', color=dark_gray,
          family='DejaVu Serif', transform=ax_c.transAxes)
ax_c.text(0.15, 0.96, 'Finding classification', fontsize=10, color=dark_gray,
          family='DejaVu Serif', transform=ax_c.transAxes)

def draw_finding_row(ax, y_center, num, num_color, finding_text, metric_text,
                     category_text, cat_color):
    y_box = y_center - 0.06
    draw_circle_number(ax, 0.06, y_center + 0.02, str(num), num_color,
                       radius=0.028, fontsize=9)
    draw_shadow_box(ax, (0.14, y_box), 0.38, 0.14, 'white', linewidth=0.8,
                    edgecolor='#CCCCCC')
    ax.text(0.33, y_center + 0.03, finding_text, ha='center', va='center',
            fontsize=7.5, fontweight='bold', color=dark_gray, family='DejaVu Sans',
            transform=ax.transAxes)
    ax.text(0.33, y_center - 0.03, metric_text, ha='center', va='center',
            fontsize=6.5, color='#888888', family='DejaVu Sans',
            transform=ax.transAxes)
    ax.annotate('', xy=(0.58, y_center), xytext=(0.53, y_center),
                arrowprops=dict(arrowstyle='->', color='#999999', lw=1.0),
                transform=ax.transAxes)
    cat_box = FancyBboxPatch((0.60, y_box + 0.01), 0.36, 0.12,
                             boxstyle="round,pad=0.01",
                             facecolor=cat_color, alpha=0.15,
                             edgecolor=cat_color, linewidth=0.5,
                             zorder=2, transform=ax.transAxes)
    ax.add_patch(cat_box)
    ax.plot([0.60, 0.60], [y_box + 0.02, y_box + 0.12], color=cat_color,
            linewidth=3.0, solid_capstyle='round', transform=ax.transAxes, zorder=3)
    ax.text(0.78, y_center, category_text, ha='center', va='center', fontsize=7,
            fontweight='bold', color=dark_gray, family='DejaVu Sans',
            transform=ax.transAxes, linespacing=1.3)

draw_finding_row(ax_c, 0.80, 1, sky_blue,
                 'Exit collapse', 'ΔR² = 0.15–0.69',
                 'Training-\nassociated', sky_blue)

draw_finding_row(ax_c, 0.50, 2, salmon,
                 'CF sensitivity', 'd = 0.45–1.52',
                 'Action-\nlinked', salmon)

draw_finding_row(ax_c, 0.20, 3, gold,
                 'L1 instr. attention', '24–32/32 heads',
                 'Inherited\nprior', gold)

plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches='tight', facecolor='white',
            edgecolor='none', pad_inches=0.05)
plt.close()
print(f"Saved to {OUTPUT_PATH}")

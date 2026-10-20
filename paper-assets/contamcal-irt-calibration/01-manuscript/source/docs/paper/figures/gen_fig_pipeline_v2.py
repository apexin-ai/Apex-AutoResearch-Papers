#!/usr/bin/env python3
"""Generate ContamCal three-stage pipeline diagram (Figure 2).

Publication-quality horizontal pipeline for single-column academic paper.
Uses matplotlib FancyBboxPatch for rounded rectangles and manual arrow drawing.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# ── Global style ──────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
    'text.usetex': False,
    'mathtext.default': 'it',
    'mathtext.fontset': 'dejavusans',
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'savefig.facecolor': 'white',
    'savefig.edgecolor': 'white',
})

# ── Colors ────────────────────────────────────────────────────────────────
NAVY = '#2C3E50'
SUBTITLE_GRAY = '#5D6D7E'
CONTENT_GRAY = '#34495E'
ARROW_COLOR = '#5D6D7E'

# Stage backgrounds and borders
STAGE1_BG = '#F0F4F8'
STAGE1_BORDER = '#B0BEC5'
STAGE2_BG = '#F5F0EB'
STAGE2_BORDER = '#C4B8A8'
STAGE3_BG = '#EEF4EE'
STAGE3_BORDER = '#A8C4A8'

# Badge colors for dose-response patterns
BADGE_IMMUNE = '#6c757d'
BADGE_COLLAPSE = '#c0392b'
BADGE_VRECOVERY = '#e67e22'
BADGE_BENEFIT = '#2e86ab'

# ── Figure dimensions ─────────────────────────────────────────────────────
fig_w, fig_h = 10, 3.5
fig, ax = plt.subplots(1, 1, figsize=(fig_w, fig_h), dpi=300)
ax.set_xlim(0, fig_w)
ax.set_ylim(0, fig_h)
ax.axis('off')
ax.set_aspect('equal')

# ── Layout parameters ─────────────────────────────────────────────────────
margin_x = 0.3
margin_y = 0.25
gap = 0.55  # gap between stages (for arrows)
box_w = (fig_w - 2 * margin_x - 2 * gap) / 3
box_h = fig_h - 2 * margin_y
corner_r = 0.15  # rounded corner radius

# Stage x positions
x1 = margin_x
x2 = x1 + box_w + gap
x3 = x2 + box_w + gap
y_bottom = margin_y


def draw_stage_box(ax, x, y, w, h, bg_color, border_color, shadow=True):
    """Draw a rounded rectangle with optional subtle shadow."""
    if shadow:
        # Double shadow for softer effect
        for offset, alpha_hex in [(0.04, '08'), (0.02, '06')]:
            shadow_box = FancyBboxPatch(
                (x + offset, y - offset), w, h,
                boxstyle=f"round,pad=0,rounding_size={corner_r}",
                facecolor=f'#000000{alpha_hex}',
                edgecolor='none',
                zorder=0
            )
            ax.add_patch(shadow_box)

    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={corner_r}",
        facecolor=bg_color,
        edgecolor=border_color,
        linewidth=1.0,
        zorder=1
    )
    ax.add_patch(box)
    return box


def draw_pill(ax, x_center, y_center, text, bg='#FFFFFF', border='#B0BEC5',
              fontsize=7, text_color=CONTENT_GRAY, width=None, use_math=False):
    """Draw a pill-shaped badge with text."""
    if width is None:
        width = len(text) * 0.085 + 0.4
    height = 0.34
    pill = FancyBboxPatch(
        (x_center - width / 2, y_center - height / 2), width, height,
        boxstyle="round,pad=0,rounding_size=0.12",
        facecolor=bg,
        edgecolor=border,
        linewidth=0.7,
        zorder=3
    )
    ax.add_patch(pill)
    ax.text(x_center, y_center, text, fontsize=fontsize,
            ha='center', va='center', color=text_color, zorder=4,
            fontfamily='sans-serif')


def draw_colored_badge(ax, x_center, y_center, text, color, fontsize=7.5):
    """Draw a colored badge with white text."""
    width = len(text) * 0.088 + 0.40
    height = 0.30
    badge = FancyBboxPatch(
        (x_center - width / 2, y_center - height / 2), width, height,
        boxstyle="round,pad=0,rounding_size=0.10",
        facecolor=color,
        edgecolor='none',
        linewidth=0,
        alpha=0.92,
        zorder=3
    )
    ax.add_patch(badge)
    ax.text(x_center, y_center, text, fontsize=fontsize,
            ha='center', va='center', color='white', zorder=4,
            fontweight='bold', fontfamily='sans-serif')


def draw_signal_icon(ax, x, y, icon_type):
    """Draw a small icon indicator for detection signals."""
    if icon_type == 'embedding':
        # Three connected dots (network/similarity)
        offsets = [(-0.08, 0.06), (0.08, 0.06), (0.0, -0.07)]
        for ox, oy in offsets:
            ax.plot(x + ox, y + oy, 'o', color=NAVY, markersize=3, zorder=5)
        for i in range(3):
            for j in range(i + 1, 3):
                ax.plot([x + offsets[i][0], x + offsets[j][0]],
                        [y + offsets[i][1], y + offsets[j][1]],
                        '-', color=NAVY, linewidth=0.6, zorder=4, alpha=0.5)
    elif icon_type == 'distribution':
        # Small bell curve
        xs = np.linspace(-0.1, 0.1, 30)
        ys = 0.08 * np.exp(-xs ** 2 / 0.002)
        ax.plot(x + xs, y + ys - 0.04, '-', color=NAVY, linewidth=1.0, zorder=5)
        ax.plot([x - 0.1, x + 0.1], [y - 0.04, y - 0.04], '-', color=NAVY,
                linewidth=0.6, zorder=5)
    elif icon_type == 'critique':
        # Magnifying glass / reflection symbol
        circle = plt.Circle((x - 0.01, y + 0.02), 0.06, fill=False,
                             edgecolor=NAVY, linewidth=0.9, zorder=5)
        ax.add_patch(circle)
        # Handle
        ax.plot([x + 0.035, x + 0.09], [y - 0.03, y - 0.08],
                '-', color=NAVY, linewidth=1.0, zorder=5)


# ── Draw stage boxes ──────────────────────────────────────────────────────
draw_stage_box(ax, x1, y_bottom, box_w, box_h, STAGE1_BG, STAGE1_BORDER)
draw_stage_box(ax, x2, y_bottom, box_w, box_h, STAGE2_BG, STAGE2_BORDER)
draw_stage_box(ax, x3, y_bottom, box_w, box_h, STAGE3_BG, STAGE3_BORDER)

# ── Stage 1: Multi-Signal Exposure Mapping ────────────────────────────────
s1_cx = x1 + box_w / 2
top1 = y_bottom + box_h

# Title
ax.text(s1_cx, top1 - 0.32, 'Stage 1', fontsize=12, fontweight='bold',
        ha='center', va='center', color=NAVY, zorder=5)
ax.text(s1_cx, top1 - 0.60, 'Multi-Signal Exposure Mapping', fontsize=7.5,
        ha='center', va='center', color=SUBTITLE_GRAY, zorder=5, style='italic')

# Thin separator line under title
ax.plot([x1 + 0.25, x1 + box_w - 0.25], [top1 - 0.78, top1 - 0.78],
        '-', color=STAGE1_BORDER, linewidth=0.5, zorder=2, alpha=0.6)

# Signal rows
signal_y_start = top1 - 1.05
signal_spacing = 0.48
signals = [
    ('S₁: Embedding Similarity', 'embedding'),
    ('S₂: Min-K%++', 'distribution'),
    ('S₄: Self-Critique', 'critique'),
]

for i, (label, icon) in enumerate(signals):
    sy = signal_y_start - i * signal_spacing
    icon_x = x1 + 0.38
    draw_signal_icon(ax, icon_x, sy, icon)
    ax.text(icon_x + 0.22, sy, label, fontsize=7.5,
            ha='left', va='center', color=CONTENT_GRAY, zorder=5)

# Output pill
pill_y = y_bottom + 0.40
draw_pill(ax, s1_cx, pill_y,
          r'RRF $\rightarrow$ $e_{ij}$ $\in$ [0, 1]',
          width=2.3, fontsize=7)

# ── Stage 2: Contamination-Augmented IRT ──────────────────────────────────
s2_cx = x2 + box_w / 2
top2 = y_bottom + box_h

ax.text(s2_cx, top2 - 0.32, 'Stage 2', fontsize=12, fontweight='bold',
        ha='center', va='center', color=NAVY, zorder=5)
ax.text(s2_cx, top2 - 0.60, 'Contamination-Augmented IRT', fontsize=7.5,
        ha='center', va='center', color=SUBTITLE_GRAY, zorder=5, style='italic')

# Separator
ax.plot([x2 + 0.25, x2 + box_w - 0.25], [top2 - 0.78, top2 - 0.78],
        '-', color=STAGE2_BORDER, linewidth=0.5, zorder=2, alpha=0.6)

# Key elements
ax.text(s2_cx, top2 - 1.15, r'2PL + $\gamma_k$ model', fontsize=8.5,
        ha='center', va='center', color=CONTENT_GRAY, zorder=5)
ax.text(s2_cx, top2 - 1.60, 'Bayesian NUTS', fontsize=8.5,
        ha='center', va='center', color=CONTENT_GRAY, zorder=5)

# Output pill
draw_pill(ax, s2_cx, pill_y,
          r'$\theta_j^{\mathrm{clean}}$, $\gamma_k$ + CIs',
          width=2.1, fontsize=7)

# ── Stage 3: Dose-Response Profiling ──────────────────────────────────────
s3_cx = x3 + box_w / 2
top3 = y_bottom + box_h

ax.text(s3_cx, top3 - 0.32, 'Stage 3', fontsize=12, fontweight='bold',
        ha='center', va='center', color=NAVY, zorder=5)
ax.text(s3_cx, top3 - 0.60, 'Dose-Response Profiling', fontsize=7.5,
        ha='center', va='center', color=SUBTITLE_GRAY, zorder=5, style='italic')

# Separator
ax.plot([x3 + 0.25, x3 + box_w - 0.25], [top3 - 0.78, top3 - 0.78],
        '-', color=STAGE3_BORDER, linewidth=0.5, zorder=2, alpha=0.6)

# Algorithm text
ax.text(s3_cx, top3 - 1.15, 'Algorithm 1', fontsize=8.5,
        ha='center', va='center', color=CONTENT_GRAY, zorder=5)
ax.text(s3_cx, top3 - 1.48, 'classification', fontsize=8.5,
        ha='center', va='center', color=CONTENT_GRAY, zorder=5)

# Four pattern badges (2x2 grid)
badge_y1 = y_bottom + 0.72
badge_y2 = y_bottom + 0.34
badge_x_left = s3_cx - 0.58
badge_x_right = s3_cx + 0.58

draw_colored_badge(ax, badge_x_left, badge_y1, 'Immune', BADGE_IMMUNE)
draw_colored_badge(ax, badge_x_right, badge_y1, 'Collapse', BADGE_COLLAPSE)
draw_colored_badge(ax, badge_x_left, badge_y2, 'V-recovery', BADGE_VRECOVERY)
draw_colored_badge(ax, badge_x_right, badge_y2, 'Benefit', BADGE_BENEFIT)

# ── Arrows between stages ────────────────────────────────────────────────
arrow_y = y_bottom + box_h / 2 + 0.15
arrow_style = "Simple,tail_width=2,head_width=8,head_length=5"

# Arrow 1→2
arrow1 = FancyArrowPatch(
    (x1 + box_w + 0.06, arrow_y),
    (x2 - 0.06, arrow_y),
    arrowstyle=arrow_style,
    color=ARROW_COLOR,
    linewidth=1.0,
    mutation_scale=1,
    zorder=6,
    alpha=0.75
)
ax.add_patch(arrow1)

# Arrow label e_ij
ax.text((x1 + box_w + x2) / 2, arrow_y + 0.22, '$e_{ij}$', fontsize=8.5,
        ha='center', va='center', color=ARROW_COLOR, zorder=7, style='italic')

# Arrow 2→3
arrow2 = FancyArrowPatch(
    (x2 + box_w + 0.06, arrow_y),
    (x3 - 0.06, arrow_y),
    arrowstyle=arrow_style,
    color=ARROW_COLOR,
    linewidth=1.0,
    mutation_scale=1,
    zorder=6,
    alpha=0.75
)
ax.add_patch(arrow2)

# Arrow label θ_j, γ_k
ax.text((x2 + box_w + x3) / 2, arrow_y + 0.22,
        r'$\theta_j$, $\gamma_k$',
        fontsize=8.5, ha='center', va='center', color=ARROW_COLOR, zorder=7,
        style='italic')

# ── Save ──────────────────────────────────────────────────────────────────
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures'

# PNG
png_path = os.path.join(out_dir, 'fig_pipeline.png')
fig.savefig(png_path, dpi=300, bbox_inches='tight', pad_inches=0.05)

# PDF
pdf_path = os.path.join(out_dir, 'fig_pipeline.pdf')
fig.savefig(pdf_path, dpi=300, bbox_inches='tight', pad_inches=0.05)

plt.close()
print(f"Saved PNG: {png_path}")
print(f"Saved PDF: {pdf_path}")

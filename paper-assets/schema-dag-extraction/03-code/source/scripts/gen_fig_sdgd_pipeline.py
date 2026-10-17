#!/usr/bin/env python3
"""Generate Figure 4: SDGD Pipeline — information-dense conceptual diagram.

Visual story: blue pipeline (intended path) vs red callouts (where it breaks).
Includes quantitative failure data and task labels for maximum information density.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# Color palette
C_FILL      = '#E8F0FE'
C_BORDER    = '#3B6CB5'
C_ARROW     = '#8C9BB5'
C_FAIL_BG   = '#FDF0EF'
C_FAIL_BD   = '#C0392B'
C_FAIL_TXT  = '#8B1A1A'
C_TEXT       = '#2C3E50'
C_GRAY      = '#7F8C8D'
C_GREEN     = '#27AE60'
C_DOT_BLUE  = '#5B9BD5'
C_DOT_ORANGE = '#ED7D31'
C_DOT_RED   = '#E74C3C'
C_DOT_GREEN = '#27AE60'

fig, ax = plt.subplots(figsize=(7.2, 4.8))
ax.set_xlim(-0.1, 7.3)
ax.set_ylim(-0.3, 4.9)
ax.axis('off')
fig.patch.set_facecolor('white')


def make_box(x, y, w, h, fill=C_FILL, border=C_BORDER, lw=1.3,
             shadow=True, dashed=False):
    ls = (0, (5, 3)) if dashed else '-'
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12",
                         facecolor=fill, edgecolor=border, linewidth=lw,
                         linestyle=ls, zorder=3)
    if shadow:
        box.set_path_effects([
            pe.withSimplePatchShadow(offset=(1.5, -1.5), shadow_rgbFace='#00000008',
                                     alpha=0.15),
            pe.Normal(),
        ])
    ax.add_patch(box)
    return box


def flow_arrow(x1, x2, y, label=None, label_y_offset=0.16):
    arr = FancyArrowPatch((x1, y), (x2, y),
                          arrowstyle='->', mutation_scale=12,
                          color=C_ARROW, linewidth=1.2, zorder=2)
    ax.add_patch(arr)
    if label:
        ax.text((x1 + x2) / 2, y + label_y_offset, label, ha='center', va='bottom',
                fontsize=7.5, color=C_GRAY, style='italic', zorder=4)


def fail_arrow(x, y1, y2):
    arr = FancyArrowPatch((x, y1), (x, y2),
                          arrowstyle='->', mutation_scale=12,
                          color=C_FAIL_BD, linewidth=1.3, zorder=2,
                          linestyle=(0, (4, 2)))
    ax.add_patch(arr)
    mid_y = (y1 + y2) / 2
    ax.plot(x, mid_y, 'x', color=C_FAIL_BD, markersize=7,
            markeredgewidth=2, zorder=4)


# ═══════════════════════════════════════════
# MAIN PIPELINE (center band)
# ═══════════════════════════════════════════
ROW_Y = 1.85
BH = 0.95

# Stage 1: Full Schema — richer 4×3 dot grid
make_box(0.05, ROW_Y, 1.15, BH)
ax.text(0.625, ROW_Y + 0.28, 'Full Schema', ha='center', va='center',
        fontsize=9.5, color=C_TEXT, fontweight='bold', zorder=5)
ax.text(0.625, ROW_Y + 0.10, '(k types)', ha='center', va='center',
        fontsize=7.5, color=C_GRAY, style='italic', zorder=5)
dot_colors_grid = [
    C_DOT_BLUE,  C_DOT_ORANGE, C_DOT_GREEN, C_DOT_RED,
    C_DOT_BLUE,  C_DOT_RED,    C_DOT_ORANGE, C_DOT_BLUE,
    C_DOT_GREEN, C_DOT_BLUE,   C_DOT_ORANGE, C_DOT_RED,
]
for idx, dc in enumerate(dot_colors_grid):
    col = idx % 4
    row = idx // 4
    dx = (col - 1.5) * 0.12
    dy = row * 0.13
    ax.plot(0.625 + dx, ROW_Y + 0.48 + dy, 'o', color=dc,
            markersize=3.8, zorder=5, alpha=0.85)

flow_arrow(1.20, 1.68, ROW_Y + BH / 2)
# Decompose label with SCS detail
ax.text(1.44, ROW_Y + BH / 2 + 0.16, 'Decompose', ha='center', va='bottom',
        fontsize=7.5, color=C_GRAY, style='italic', zorder=4)
ax.text(1.44, ROW_Y + BH / 2 - 0.18, '(SCS graph\ncoloring)', ha='center', va='top',
        fontsize=6, color=C_BORDER, zorder=4)

# Stage 2: Sub-schemas (fanned cards) — show type separation clearly
card_w, card_h = 0.55, 0.55
base_x, base_y = 1.72, ROW_Y + BH / 2
offsets = [(-0.06, -0.22), (0.0, 0.0), (0.06, 0.22)]
card_dot_sets = [
    (C_DOT_RED, C_DOT_GREEN),
    (C_DOT_ORANGE, C_DOT_ORANGE),
    (C_DOT_BLUE, C_DOT_BLUE),
]
for (ox, oy), dots in zip(offsets, card_dot_sets):
    cx = base_x + ox
    cy = base_y + oy - card_h / 2
    make_box(cx, cy, card_w, card_h, shadow=False, lw=0.9)
    for j, dc in enumerate(dots):
        ax.plot(cx + card_w / 2 + (j - 0.5) * 0.14, cy + card_h / 2,
                'o', color=dc, markersize=3, zorder=6, alpha=0.8)

ax.text(base_x + card_w / 2, ROW_Y - 0.12, 'sub-schemas', ha='center',
        va='top', fontsize=7, color=C_GRAY, style='italic', zorder=5)
# Green checkmark annotation
ax.text(base_x + card_w / 2 + 0.06, ROW_Y + BH + 0.08,
        'low confusability  ✓', ha='center', va='bottom',
        fontsize=6.5, color=C_GREEN, fontweight='semibold', zorder=5)

flow_arrow(2.38, 2.95, ROW_Y + BH / 2, 'Route')

# Stage 3: Route & Extract (red dashed border = problematic)
make_box(2.95, ROW_Y, 1.10, BH, dashed=True, border=C_FAIL_BD,
         fill='#FEF5F4')
ax.text(3.5, ROW_Y + BH / 2 + 0.10, 'Route &', ha='center', va='center',
        fontsize=9.5, color=C_TEXT, fontweight='bold', zorder=5)
ax.text(3.5, ROW_Y + BH / 2 - 0.10, 'Extract', ha='center', va='center',
        fontsize=9.5, color=C_TEXT, fontweight='bold', zorder=5)

flow_arrow(4.05, 4.55, ROW_Y + BH / 2)

# Stage 4: Merge (red dashed border = problematic)
make_box(4.55, ROW_Y, 0.95, BH, dashed=True, border=C_FAIL_BD,
         fill='#FEF5F4')
ax.text(5.025, ROW_Y + BH / 2 + 0.08, 'Merge', ha='center', va='center',
        fontsize=10, color=C_TEXT, fontweight='bold', zorder=5)
ax.text(5.025, ROW_Y + BH / 2 - 0.12, '(union)', ha='center', va='center',
        fontsize=7, color=C_GRAY, style='italic', zorder=5)

flow_arrow(5.50, 5.95, ROW_Y + BH / 2)

# Stage 5: Final Predictions
make_box(5.95, ROW_Y, 1.10, BH)
ax.text(6.50, ROW_Y + BH / 2 + 0.10, 'Final', ha='center', va='center',
        fontsize=10, color=C_TEXT, fontweight='bold', zorder=5)
ax.text(6.50, ROW_Y + BH / 2 - 0.10, 'Predictions', ha='center', va='center',
        fontsize=7.5, color=C_GRAY, zorder=5)


# ═══════════════════════════════════════════
# FAILURE CALLOUT A — Routing Failure (above) — with quantitative data
# ═══════════════════════════════════════════
fa_x, fa_w, fa_h = 2.0, 3.1, 1.05
fa_y = 3.55
make_box(fa_x, fa_y, fa_w, fa_h, fill=C_FAIL_BG, border=C_FAIL_BD, lw=1.5)

# Title with task label
ax.text(fa_x + 0.12, fa_y + fa_h - 0.14,
        'Routing Failure', ha='left', va='top',
        fontsize=10, color=C_FAIL_TXT, fontweight='bold', zorder=5)
ax.text(fa_x + fa_w - 0.12, fa_y + fa_h - 0.14,
        'RE', ha='right', va='top',
        fontsize=8, color='white', fontweight='bold', zorder=6,
        bbox=dict(boxstyle='round,pad=0.15', fc=C_FAIL_BD, ec='none', alpha=0.85))

# Quantitative details
details_a = [
    '73.4% instances → multiple sub-schemas',
    'oracle routing: 0.72  vs  single-pass: 0.50',
    'none-rate per sub-schema only 20–40%',
]
for i, line in enumerate(details_a):
    ax.text(fa_x + 0.12, fa_y + fa_h - 0.38 - i * 0.22,
            line, ha='left', va='top',
            fontsize=7, color=C_FAIL_TXT, zorder=5)

fail_arrow(3.5, fa_y, ROW_Y + BH)


# ═══════════════════════════════════════════
# FAILURE CALLOUT B — Merge Amplification (below) — with quantitative data
# ═══════════════════════════════════════════
fb_x, fb_w, fb_h = 3.1, 3.3, 1.05
fb_y = 0.0
make_box(fb_x, fb_y, fb_w, fb_h, fill=C_FAIL_BG, border=C_FAIL_BD, lw=1.5)

# Title with task label
ax.text(fb_x + 0.12, fb_y + fb_h - 0.14,
        'Merge Amplification', ha='left', va='top',
        fontsize=10, color=C_FAIL_TXT, fontweight='bold', zorder=5)
ax.text(fb_x + fb_w - 0.12, fb_y + fb_h - 0.14,
        'NER / ED', ha='right', va='top',
        fontsize=8, color='white', fontweight='bold', zorder=6,
        bbox=dict(boxstyle='round,pad=0.15', fc=C_FAIL_BD, ec='none', alpha=0.85))

# Quantitative details
details_b = [
    'union merge ×2 false positives',
    'precision: 0.56 → 0.21  |  F1: −19 pp',
    'voting merge sacrifices recall',
]
for i, line in enumerate(details_b):
    ax.text(fb_x + 0.12, fb_y + fb_h - 0.38 - i * 0.22,
            line, ha='left', va='top',
            fontsize=7, color=C_FAIL_TXT, zorder=5)

fail_arrow(5.025, fb_y + fb_h, ROW_Y)


# ═══════════════════════════════════════════
# SINGLE-PASS BASELINE ANNOTATION (below pipeline, left side)
# ═══════════════════════════════════════════
ax.annotate(
    '', xy=(5.95, ROW_Y - 0.05), xytext=(0.625, ROW_Y - 0.05),
    arrowprops=dict(
        arrowstyle='->', color=C_BORDER, lw=0.9,
        alpha=0.4, linestyle=(0, (6, 3)),
        connectionstyle='arc3,rad=-0.15',
    ),
    zorder=1,
)
ax.text(3.3, ROW_Y - 0.38, 'single-pass baseline (no decomposition)',
        ha='center', va='top', fontsize=6.5, color=C_BORDER, alpha=0.6,
        style='italic', zorder=2)


# ═══════════════════════════════════════════
# SAVE
# ═══════════════════════════════════════════
out_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                       'figures', 'paper')
os.makedirs(out_dir, exist_ok=True)

pdf_path = os.path.join(out_dir, 'fig_sdgd_pipeline.pdf')
png_path = os.path.join(out_dir, 'fig_sdgd_pipeline.png')
fig.savefig(pdf_path)
fig.savefig(png_path)
plt.close(fig)
print(f"Saved: {pdf_path}")
print(f"Saved: {png_path}")

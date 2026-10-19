#!/usr/bin/env python3
"""Concept overview figure for Introduction (Figure 1).

Horizontal 4-stage flowchart: Input → Metric Choice → Layer Divergence → Opposite Conclusions.
Two branches show how different metrics select different layers, leading to contradictory findings.

Output: docs/paper/figures/fig_concept_overview.{pdf,png}
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.path import Path
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Times'],
    'mathtext.fontset': 'dejavuserif',
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.06,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

fig, ax = plt.subplots(figsize=(7.0, 2.8))
ax.set_xlim(-0.15, 7.15)
ax.set_ylim(-0.45, 2.85)
ax.axis('off')

# ── Color palette ──
WARM       = '#FFF3E0'
WARM_EDGE  = '#E65100'
WARM_MID   = '#FB8C00'
COOL       = '#E3F2FD'
COOL_EDGE  = '#1565C0'
COOL_MID   = '#1E88E5'
FAIL_BG    = '#FFEBEE'
FAIL_EDGE  = '#C62828'
PASS_BG    = '#E8F5E9'
PASS_EDGE  = '#2E7D32'
NEUTRAL_BG = '#EFEBE9'
NEUTRAL_EDGE = '#5D4037'
GAP_COLOR  = '#B71C1C'
GRAY_TEXT  = '#616161'
DARK_TEXT  = '#212121'
SHADOW     = '#00000014'

# ── Helper: rounded box with drop shadow ──
def draw_box(ax, x, y, w, h, text, facecolor, edgecolor,
             fontsize=8, fontweight='normal', linestyle='-',
             linewidth=1.2, text_color=DARK_TEXT, shadow=True):
    if shadow:
        s = FancyBboxPatch((x + 0.04, y - 0.04), w, h,
                           boxstyle="round,pad=0.10",
                           facecolor=SHADOW, edgecolor='none',
                           linewidth=0, zorder=1)
        ax.add_patch(s)
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle="round,pad=0.10",
                         facecolor=facecolor, edgecolor=edgecolor,
                         linewidth=linewidth, linestyle=linestyle,
                         zorder=2)
    ax.add_patch(box)
    ax.text(x + w / 2, y + h / 2, text,
            ha='center', va='center', fontsize=fontsize,
            fontweight=fontweight, color=text_color,
            zorder=3, linespacing=1.25)

# ── Helper: curved arrow ──
def draw_arrow(ax, x1, y1, x2, y2, color, rad=0.0, lw=1.6):
    conn = f'arc3,rad={rad}' if rad != 0 else 'arc3,rad=0'
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='-|>',
                                color=color, linewidth=lw,
                                connectionstyle=conn,
                                mutation_scale=12),
                zorder=1)

# ── Layout constants ──
Y_UP   = 1.92
Y_DOWN = 0.38
Y_MID  = 1.15

# ── Stage headers ──
header_y = 2.72
headers = [
    (0.55, 'Input'),
    (2.37, 'Metric Choice'),
    (4.16, 'Layer Selected'),
    (6.12, 'Conclusion'),
]
for x_pos, label in headers:
    ax.text(x_pos, header_y, label, fontsize=8.5, ha='center', va='bottom',
            fontweight='bold', color='#455A64',
            fontstyle='italic')

# Column separators
# Iter 6: split the rightmost separator to avoid gap annotation area
for x_sep in [1.35, 3.32]:
    ax.plot([x_sep, x_sep], [0.02, 2.58], color='#BDBDBD',
            linestyle=(0, (4, 4)), linewidth=0.9, zorder=0)
# Right separator: upper segment and lower segment, skipping gap zone
ax.plot([5.15, 5.15], [Y_UP - 0.40, 2.58], color='#BDBDBD',
        linestyle=(0, (4, 4)), linewidth=0.9, zorder=0)
ax.plot([5.15, 5.15], [0.02, Y_DOWN + 0.40], color='#BDBDBD',
        linestyle=(0, (4, 4)), linewidth=0.9, zorder=0)

# ── Background bands ──
band_h = 0.72
ax.add_patch(FancyBboxPatch((-0.05, Y_UP - 0.36), 7.1, band_h,
             boxstyle="round,pad=0.05",
             facecolor='#FFF8E1', edgecolor='#FFE0B2', alpha=0.60,
             linewidth=0.5, zorder=0))
ax.add_patch(FancyBboxPatch((-0.05, Y_DOWN - 0.36), 7.1, band_h,
             boxstyle="round,pad=0.05",
             facecolor='#E8EAF6', edgecolor='#C5CAE9', alpha=0.55,
             linewidth=0.5, zorder=0))

# ════════════════════════════════════════════
# STAGE 1: Input — Hidden States
# ════════════════════════════════════════════
draw_box(ax, 0.0, Y_MID - 0.30, 1.1, 0.60,
         'Hidden\nStates', NEUTRAL_BG, NEUTRAL_EDGE,
         fontsize=9.5, fontweight='bold', linewidth=1.6)

# Diverging arrows from Hidden States
draw_arrow(ax, 1.1, Y_MID + 0.14, 1.62, Y_UP,
           color=WARM_MID, rad=-0.25, lw=1.6)
draw_arrow(ax, 1.1, Y_MID - 0.14, 1.62, Y_DOWN,
           color=COOL_MID, rad=0.25, lw=1.6)

# ════════════════════════════════════════════
# STAGE 2: Metric Choice
# ════════════════════════════════════════════
draw_box(ax, 1.62, Y_UP - 0.22, 1.50, 0.44,
         'Crossing-rate\nComposite', WARM, WARM_EDGE,
         fontsize=8.5, fontweight='bold')

draw_box(ax, 1.62, Y_DOWN - 0.22, 1.50, 0.44,
         'Threshold Metrics\n(Precision, Inv-FPR)', COOL, COOL_EDGE,
         fontsize=7.5, fontweight='bold')

# Arrows: Metric → Layer
draw_arrow(ax, 3.12, Y_UP, 3.50, Y_UP, color=WARM_MID, lw=1.5)
draw_arrow(ax, 3.12, Y_DOWN, 3.50, Y_DOWN, color=COOL_MID, lw=1.5)

# ════════════════════════════════════════════
# STAGE 3: Layer Selected
# ════════════════════════════════════════════
draw_box(ax, 3.50, Y_UP - 0.22, 1.32, 0.44,
         'Shallow Layers\nL0–L2  (0–3%)', WARM, WARM_EDGE,
         fontsize=8)

draw_box(ax, 3.50, Y_DOWN - 0.22, 1.32, 0.44,
         'Deep Layers\nL14–L63  (44–98%)', COOL, COOL_EDGE,
         fontsize=8)

# ── Layer gap annotation ──
# Iter 6: slightly larger gap text (7 → 7.5), position label to the right of arrow
gap_x = 4.16
ax.annotate('', xy=(gap_x, Y_UP - 0.26), xytext=(gap_x, Y_DOWN + 0.26),
            arrowprops=dict(arrowstyle='<|-|>',
                            color=GAP_COLOR, linewidth=1.6,
                            linestyle='--',
                            mutation_scale=10),
            zorder=2)
ax.text(gap_x + 0.32, Y_MID, '14–61\nlayer\ngap',
        fontsize=7.5, ha='left', va='center',
        color=GAP_COLOR, fontweight='bold', linespacing=1.05,
        bbox=dict(facecolor='white', edgecolor='none', alpha=0.92, pad=2.0),
        zorder=3)

# Arrows: Layer → Conclusion
draw_arrow(ax, 4.82, Y_UP, 5.24, Y_UP, color=FAIL_EDGE, lw=1.5)
draw_arrow(ax, 4.82, Y_DOWN, 5.24, Y_DOWN, color=PASS_EDGE, lw=1.5)

# ════════════════════════════════════════════
# STAGE 4: Conclusions
# ════════════════════════════════════════════
draw_box(ax, 5.24, Y_UP - 0.25, 1.76, 0.50,
         'HS ≈ Text\n$p = 0.83$,  NS', FAIL_BG, FAIL_EDGE,
         fontsize=9, fontweight='bold', linestyle='--',
         linewidth=2.2, text_color=FAIL_EDGE)

draw_box(ax, 5.24, Y_DOWN - 0.25, 1.76, 0.50,
         'HS >> Text\n$p < 0.005$,  +20 pp', PASS_BG, PASS_EDGE,
         fontsize=9, fontweight='bold', linestyle='-',
         linewidth=2.0, text_color=PASS_EDGE)

# ── Bottom tagline ──
ax.text(3.5, -0.32,
        'Same hidden states, same model  —  only the evaluation metric differs',
        fontsize=8.5, ha='center', va='top', color=GRAY_TEXT,
        fontstyle='italic', fontweight='medium')

# ── Save ──
out = '/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/figures/fig_concept_overview'
fig.savefig(f'{out}.pdf', format='pdf')
fig.savefig(f'{out}.png', format='png')
print(f'Saved: {out}.pdf and .png')
plt.close()

#!/usr/bin/env python3
"""Figure 2: G-Theory Crossed Experimental Design Diagram.

Center-radial layout showing the fully crossed structure:
Item (p) at center, 6 facets around it, all crossed.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['STIXGeneral', 'DejaVu Serif', 'Times New Roman'],
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# --- Layout constants ---
FIG_W, FIG_H = 7.0, 4.45
CENTER_X, CENTER_Y = 3.5, 2.25
RADIUS = 1.50

# Facets: (label, greek, detail_line1, detail_line2, fill, edge, angle_deg)
facets = [
    ('Model',       'M',  '4 models: Llama / Gemma',    'Mistral / Qwen',        '#d5e8d4', '#6aad5a', 90),
    ('Precision',   'π',  '3 levels',                    'BF16 / FP16 / FP32',    '#fff2cc', '#d6b656', 162),
    ('Prompt',      'δ',  '6 paraphrases',               '',                       '#f8cecc', '#c0504d', 198),
    ('Seed',        's',  '6 seeds: 42, 123, 456',      '789, 1024, 2048',       '#e1d5e7', '#8e6aab', 252),
    ('Temperature', 'τ',  '3 levels',                    '0.0 / 0.3 / 0.7',       '#d5e8f0', '#4a8ebd', 318),
    ('Ordering',    'o',  '4 rotations: ABCD',           'BCDA / CDAB / DABC',    '#fce5cd', '#b8834f', 342),
]

def get_node_pos(angle_deg):
    rad = np.radians(angle_deg)
    return CENTER_X + RADIUS * np.cos(rad), CENTER_Y + RADIUS * np.sin(rad)

# Precompute positions
node_positions = {'Item': (CENTER_X, CENTER_Y)}
for f in facets:
    node_positions[f[0]] = get_node_pos(f[6])

# --- Create figure ---
fig, ax = plt.subplots(1, 1, figsize=(FIG_W, FIG_H))
ax.set_xlim(0.15, 6.85)
ax.set_ylim(-0.55, 4.55)
ax.set_aspect('equal')
ax.axis('off')

# =============================================
# 1. GROUP BACKGROUND REGIONS (lowest z-order)
# =============================================

# Infrastructure group — around Precision
px, py = node_positions['Precision']
infra_bg = FancyBboxPatch(
    (px - 0.78, py - 0.50), 1.56, 1.00,
    boxstyle="round,pad=0.14",
    facecolor='#fff8e1', edgecolor='#c9a832',
    linewidth=0.8, linestyle=(0, (4, 3)), alpha=0.5, zorder=1
)
ax.add_patch(infra_bg)
ax.text(px, py - 0.60, 'Infrastructure',
        ha='center', va='top', fontsize=7.5, fontstyle='italic',
        color='#8d6e27', zorder=2)

# Methodology group — around Prompt, Seed, Temperature, Ordering
meth_indices = [2, 3, 4, 5]  # Prompt, Seed, Temp, Ordering
meth_pos = [node_positions[facets[i][0]] for i in meth_indices]
mx_min = min(p[0] for p in meth_pos) - 0.78
mx_max = max(p[0] for p in meth_pos) + 0.78
my_min = min(p[1] for p in meth_pos) - 0.50
my_max = max(p[1] for p in meth_pos) + 0.50
method_bg = FancyBboxPatch(
    (mx_min, my_min), mx_max - mx_min, my_max - my_min,
    boxstyle="round,pad=0.14",
    facecolor='#fce4ec', edgecolor='#c06060',
    linewidth=0.8, linestyle=(0, (4, 3)), alpha=0.25, zorder=1
)
ax.add_patch(method_bg)
ax.text((mx_min + mx_max) / 2, my_min - 0.06, 'Methodology',
        ha='center', va='top', fontsize=7.5, fontstyle='italic',
        color='#8b3a3a', zorder=2)

# =============================================
# 2. CROSSING LINES (behind nodes)
# =============================================
all_names = ['Item'] + [f[0] for f in facets]

for i in range(len(all_names)):
    for j in range(i + 1, len(all_names)):
        n1, n2 = all_names[i], all_names[j]
        x1, y1 = node_positions[n1]
        x2, y2 = node_positions[n2]

        if {n1, n2} == {'Item', 'Model'}:
            # Model × Item: thick line — largest interaction
            ax.plot([x1, x2], [y1, y2], color='#666666', linewidth=2.0,
                    zorder=3, solid_capstyle='round')
        elif 'Item' in {n1, n2}:
            # Center to facet lines
            ax.plot([x1, x2], [y1, y2], color='#aaaaaa', linewidth=0.7,
                    zorder=2, solid_capstyle='round')
        else:
            # Outer facet to outer facet — very subtle
            ax.plot([x1, x2], [y1, y2], color='#dddddd', linewidth=0.3,
                    zorder=1, alpha=0.5)

# "33.6%" annotation on Model-Item line
mx_m, my_m = node_positions['Model']
mid_x = (CENTER_X + mx_m) / 2
mid_y = (CENTER_Y + my_m) / 2
t = ax.text(mid_x + 0.28, mid_y, '33.6%',
            ha='left', va='center', fontsize=7.5,
            color='#c0392b', fontweight='bold', zorder=10)
t.set_path_effects([pe.withStroke(linewidth=3, foreground='white')])

# "×" crossed symbols on center-to-facet lines
for name, greek, d1, d2, fill, edge, angle in facets:
    nx, ny = node_positions[name]
    frac = 0.32
    sx = CENTER_X + frac * (nx - CENTER_X)
    sy = CENTER_Y + frac * (ny - CENTER_Y)
    t = ax.text(sx, sy, '×', ha='center', va='center',
                fontsize=8, color='#999999', fontweight='bold', zorder=4)
    t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# =============================================
# 3. CENTER NODE — Item (p)
# =============================================
CW, CH = 1.30, 0.72
center_box = FancyBboxPatch(
    (CENTER_X - CW/2, CENTER_Y - CH/2), CW, CH,
    boxstyle="round,pad=0.08",
    facecolor='#dae8fc', edgecolor='#4a7ab5',
    linewidth=2.0, zorder=6
)
ax.add_patch(center_box)
ax.text(CENTER_X, CENTER_Y + 0.10, 'Item (p)',
        ha='center', va='center', fontsize=11, fontweight='bold',
        color='#1a4a7a', zorder=7)
ax.text(CENTER_X, CENTER_Y - 0.15, '200 MMLU items, 10 subjects × 20',
        ha='center', va='center', fontsize=6, fontstyle='italic',
        color='#5a7a9a', zorder=7)

# Measurement label below center
ax.text(CENTER_X, CENTER_Y - CH/2 - 0.12, 'Measurement',
        ha='center', va='top', fontsize=7, fontstyle='italic',
        color='#3a6a8a',
        bbox=dict(boxstyle='round,pad=0.12', facecolor='#e3f2fd',
                  edgecolor='#6c8ebf', linewidth=0.5, alpha=0.8),
        zorder=8)

# =============================================
# 4. OUTER FACET NODES
# =============================================
NODE_W, NODE_H = 1.28, 0.82

for name, greek, detail1, detail2, fill, edge, angle in facets:
    nx, ny = node_positions[name]
    box = FancyBboxPatch(
        (nx - NODE_W/2, ny - NODE_H/2), NODE_W, NODE_H,
        boxstyle="round,pad=0.07",
        facecolor=fill, edgecolor=edge,
        linewidth=1.2, zorder=6
    )
    ax.add_patch(box)

    # Title
    ax.text(nx, ny + 0.22, f'{name} ({greek})',
            ha='center', va='center', fontsize=9, fontweight='bold',
            color='#222222', zorder=7)
    # Detail line 1
    ax.text(nx, ny + 0.02, detail1,
            ha='center', va='center', fontsize=6.5,
            color='#555555', zorder=7)
    # Detail line 2 (if any)
    if detail2:
        ax.text(nx, ny - 0.14, detail2,
                ha='center', va='center', fontsize=6.5,
                color='#555555', zorder=7)

# Model: quasi-random facet badge — positioned to the right
mx, my = node_positions['Model']
ax.annotate('quasi-random\nfacet',
            xy=(mx + NODE_W/2, my + 0.1),
            xytext=(mx + NODE_W/2 + 0.45, my + 0.38),
            ha='left', va='center', fontsize=6.5, fontstyle='italic',
            color='#4a7a4a',
            bbox=dict(boxstyle='round,pad=0.12', facecolor='#e8f5e9',
                      edgecolor='#6aad5a', linewidth=0.5, alpha=0.85),
            arrowprops=dict(arrowstyle='->', color='#6aad5a',
                            lw=0.8, connectionstyle='arc3,rad=-0.2'),
            zorder=8)

# =============================================
# 5. BOTTOM INFO BAR
# =============================================
bar_y = -0.40

ax.text(CENTER_X, bar_y,
        'exp-001 (MMLU): 4×6×6×3×4×200 = 345,600 (BF16 balanced subset)    |    exp-002 (4 benchmarks): Reduced design — 921,600 records',
        ha='center', va='center', fontsize=6.5, color='#444444',
        fontfamily='monospace', zorder=6,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#f5f5f5',
                  edgecolor='#cccccc', linewidth=0.5))

# =============================================
# 6. TITLE
# =============================================
ax.text(CENTER_X, 4.40, 'Fully Crossed G-Theory Design',
        ha='center', va='center', fontsize=12, fontweight='bold',
        color='#222222', zorder=6)

# --- Save ---
import os
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper'
os.makedirs(out_dir, exist_ok=True)

pdf_path = os.path.join(out_dir, 'fig2_design_diagram.pdf')
png_path = os.path.join(out_dir, 'fig2_design_diagram.png')

plt.savefig(pdf_path, format='pdf')
plt.savefig(png_path, format='png', dpi=300)
plt.close()

print(f'Saved: {pdf_path}')
print(f'Saved: {png_path}')

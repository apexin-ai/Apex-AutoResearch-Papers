#!/usr/bin/env python3
"""Figure 3: Causal DAG of the self-extraction pipeline — hand-drawn matplotlib."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
from pathlib import Path
import numpy as np

fig, ax = plt.subplots(figsize=(10, 4.0))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('white')

# --- Background regions ---
gen_rect = FancyBboxPatch((0.03, 0.05), 0.50, 0.90,
                           boxstyle="round,pad=0.015",
                           facecolor='#F0F4F8', edgecolor='#BDC3C7',
                           linewidth=0.5, linestyle='--', zorder=0)
ax.add_patch(gen_rect)
ax.text(0.055, 0.91, "Generation", fontsize=10, fontstyle='italic',
        fontfamily='serif', color='#95A5A6', va='top', zorder=1)

ver_rect = FancyBboxPatch((0.54, 0.05), 0.43, 0.90,
                           boxstyle="round,pad=0.015",
                           facecolor='#FDF8F0', edgecolor='#BDC3C7',
                           linewidth=0.5, linestyle='--', zorder=0)
ax.add_patch(ver_rect)
ax.text(0.565, 0.91, "Verification", fontsize=10, fontstyle='italic',
        fontfamily='serif', color='#95A5A6', va='top', zorder=1)

# --- Node definitions ---
r_std = 0.058
r_big = 0.064
main_y = 0.52
y_truth = 0.18

nodes = {
    'M': {'pos': (0.13, main_y), 'label': 'M', 'sub': 'Model',
           'fill': '#D6EAF8', 'edge': '#2C3E50', 'r': r_std, 'lw': 1.5, 'ls': '-'},
    'T': {'pos': (0.30, main_y), 'label': 'T', 'sub': 'Trace',
           'fill': '#E8DAEF', 'edge': '#6C3483', 'r': r_std, 'lw': 1.5, 'ls': '-'},
    'A': {'pos': (0.47, main_y), 'label': 'A', 'sub': 'Answer',
           'fill': '#FADBD8', 'edge': '#C0392B', 'r': r_big, 'lw': 2.5, 'ls': '-'},
    'Y': {'pos': (0.22, y_truth), 'label': 'Y', 'sub': 'Truth',
           'fill': '#D5F5E3', 'edge': '#27AE60', 'r': r_std, 'lw': 1.5, 'ls': '--'},
    'C': {'pos': (0.66, main_y), 'label': 'C', 'sub': 'Constraints',
           'fill': '#FDEBD0', 'edge': '#CA6F1E', 'r': r_std, 'lw': 1.5, 'ls': '-'},
    'S': {'pos': (0.85, main_y), 'label': 'S', 'sub': 'SICA',
           'fill': '#D1F2EB', 'edge': '#1A5276', 'r': r_std, 'lw': 1.5, 'ls': '-'},
}

# Draw nodes
for name, nd in nodes.items():
    circ = Circle(nd['pos'], nd['r'], facecolor=nd['fill'], edgecolor=nd['edge'],
                  linewidth=nd['lw'], linestyle=nd['ls'], zorder=3)
    ax.add_patch(circ)
    ax.text(nd['pos'][0], nd['pos'][1], nd['label'],
            ha='center', va='center', fontsize=15, fontfamily='serif',
            fontweight='bold', color=nd['edge'], zorder=4)
    ax.text(nd['pos'][0], nd['pos'][1] - nd['r'] - 0.035, nd['sub'],
            ha='center', va='top', fontsize=8.5, fontfamily='serif',
            color='#555555', zorder=4)

# --- Arrow helper ---
def circle_edge(center, r, angle_deg):
    a = np.radians(angle_deg)
    return (center[0] + r * np.cos(a), center[1] + r * np.sin(a))

def arrow_between(n1, n2, **kwargs):
    p1 = np.array(nodes[n1]['pos'])
    p2 = np.array(nodes[n2]['pos'])
    d = p2 - p1
    angle = np.degrees(np.arctan2(d[1], d[0]))
    start = circle_edge(p1, nodes[n1]['r'] + 0.006, angle)
    end = circle_edge(p2, nodes[n2]['r'] + 0.006, angle + 180)
    return FancyArrowPatch(start, end, arrowstyle='->', mutation_scale=13, **kwargs)

# --- Edges ---
ax.add_patch(arrow_between('M', 'T', color='#555555', linewidth=1.5, zorder=2))
ax.add_patch(arrow_between('T', 'A', color='#555555', linewidth=1.5, zorder=2))
ax.add_patch(arrow_between('A', 'C', color='#C0392B', linewidth=2.0, zorder=2))
ax.add_patch(arrow_between('C', 'S', color='#555555', linewidth=1.5, zorder=2))
ax.add_patch(arrow_between('Y', 'A', color='#27AE60', linewidth=1.2,
                            linestyle='--', zorder=2))

# --- Bottleneck label on A→C edge ---
ac_mid_x = (nodes['A']['pos'][0] + nodes['C']['pos'][0]) / 2
ax.text(ac_mid_x, main_y + 0.085, "bottleneck", ha='center', va='bottom',
        fontsize=8.5, fontweight='bold', fontstyle='italic',
        color='#C0392B', fontfamily='serif', zorder=5)

# --- Formula annotation (upper right, inside Verification region) ---
formula_x = 0.78
formula_y = 0.80
box_f = FancyBboxPatch((formula_x - 0.13, formula_y - 0.065), 0.26, 0.13,
                        boxstyle="round,pad=0.012",
                        facecolor='white', edgecolor='#CCCCCC',
                        linewidth=0.5, linestyle='--', zorder=2, alpha=0.85)
ax.add_patch(box_f)
ax.text(formula_x, formula_y + 0.01,
        r"$C \perp\!\!\!\perp Y \mid A$",
        ha='center', va='center', fontsize=13, fontfamily='serif',
        color='#333333', zorder=4)
ax.text(formula_x, formula_y - 0.04,
        "approx. conditional independence",
        ha='center', va='center', fontsize=7.5, fontstyle='italic',
        color='#999999', fontfamily='serif', zorder=4)

# --- DPI annotation (bottom right, clear of Y/Truth) ---
dpi_x = 0.66
dpi_y = 0.10
ax.text(dpi_x, dpi_y + 0.01,
        r"$I(C;\,Y) \leq I(A;\,Y)$",
        ha='center', va='center', fontsize=11, fontfamily='serif',
        color='#333333', zorder=4)
ax.text(dpi_x, dpi_y - 0.03,
        "Data Processing Inequality",
        ha='center', va='center', fontsize=7.5, fontstyle='italic',
        color='#999999', fontfamily='serif', zorder=4)

plt.subplots_adjust(left=0.02, right=0.98, top=0.97, bottom=0.03)
out = Path(__file__).parent
fig.savefig(out / "fig3_causal_dag_v7.png", dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
fig.savefig(out / "fig3_causal_dag_v7.pdf", bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Saved fig3_causal_dag_v7.png and .pdf")
plt.close()

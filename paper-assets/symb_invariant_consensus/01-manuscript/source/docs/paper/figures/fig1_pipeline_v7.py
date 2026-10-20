#!/usr/bin/env python3
"""Figure 1: SICA Pipeline diagram — hand-drawn with matplotlib FancyBboxPatch."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

fig, ax = plt.subplots(figsize=(14, 4.2))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('auto')
ax.axis('off')
fig.patch.set_facecolor('white')

# --- Main track: 6 boxes ---
boxes = [
    {"label": "Question $q$",           "fill": "#EBF5FB", "edge": "#2C3E50"},
    {"label": "Sample $K$\nCoT Traces", "fill": "#F4ECF7", "edge": "#6C3483"},
    {"label": "Extract FOL\nConstraints","fill": "#FDF2E9", "edge": "#CA6F1E"},
    {"label": "Dedup\n+ Weight",         "fill": "#EAFAF1", "edge": "#1E8449"},
    {"label": "MAX-SAT\n(Z3)",           "fill": "#D4E6F1", "edge": "#1A5276"},
    {"label": "Answer $a^*$",            "fill": "#FEF9E7", "edge": "#B7950B"},
]

n = len(boxes)
bw = 0.105
bh = 0.17
gap = 0.033
total_w = n * bw + (n - 1) * gap
x_start = (1 - total_w) / 2
y_main = 0.58

box_centers = []
box_lefts = []
for i, b in enumerate(boxes):
    x = x_start + i * (bw + gap)
    rect = FancyBboxPatch((x, y_main - bh / 2), bw, bh,
                          boxstyle="round,pad=0.012",
                          facecolor=b["fill"], edgecolor=b["edge"],
                          linewidth=1.5, zorder=3)
    ax.add_patch(rect)
    cx = x + bw / 2
    cy = y_main
    box_centers.append((cx, cy))
    box_lefts.append(x)
    ax.text(cx, cy, b["label"], ha='center', va='center',
            fontsize=10.5, fontfamily='serif', color=b["edge"],
            fontweight='normal', zorder=4, linespacing=1.3)

# --- Arrows between main boxes ---
for i in range(n - 1):
    x1 = box_centers[i][0] + bw / 2 + 0.004
    x2 = box_centers[i + 1][0] - bw / 2 - 0.004
    arr = FancyArrowPatch((x1, y_main), (x2, y_main),
                          arrowstyle='->', mutation_scale=12,
                          color='#555555', linewidth=1.2, zorder=2)
    ax.add_patch(arr)

# --- Independence Bottleneck (red dashed box around boxes 2 & 3 only) ---
pad_x = 0.008
pad_y = 0.018
bx1 = box_lefts[1] - pad_x
bx2 = box_lefts[2] + bw + pad_x
by1 = y_main - bh / 2 - pad_y
by2 = y_main + bh / 2 + pad_y
bottle_rect = FancyBboxPatch((bx1, by1), bx2 - bx1, by2 - by1,
                              boxstyle="round,pad=0.005",
                              facecolor='none', edgecolor='#C0392B',
                              linewidth=1.5, linestyle='--', zorder=5)
ax.add_patch(bottle_rect)
ax.text((bx1 + bx2) / 2, by2 + 0.022, "Independence Bottleneck",
        ha='center', va='bottom', fontsize=9.5, fontstyle='italic',
        color='#C0392B', fontfamily='serif', zorder=5)

# Small formula annotation under box 3
cx3 = box_centers[2][0]
ax.text(cx3, by1 - 0.015, r"$\forall x\,(P(x)\!\to\! Q(x))$",
        ha='center', va='top', fontsize=8.5, fontstyle='italic',
        color='#999999', zorder=4)

# --- SC branch (below, visually muted) — positioned under boxes 2-3 ---
sc_y = 0.18
sc_bw = 0.09
sc_bh = 0.11
sc_box1_cx = box_centers[1][0] + 0.04
sc_box2_cx = box_centers[2][0] + 0.04

# Arrow from box 2 down to SC track
sc_start_x = box_centers[1][0]
arr_down = FancyArrowPatch((sc_start_x, y_main - bh / 2 - pad_y - 0.001),
                           (sc_start_x, sc_y + 0.005),
                           arrowstyle='->', mutation_scale=10,
                           color='#AAAAAA', linewidth=1.0, zorder=2)
ax.add_patch(arr_down)

# SC label on arrow
ax.text(sc_start_x - 0.016, (y_main - bh / 2 - pad_y + sc_y) / 2,
        "SC", ha='right', va='center', fontsize=9, color='#999999',
        fontfamily='serif', fontstyle='italic', zorder=4)

# Horizontal line to first SC box
arr_sc_h = FancyArrowPatch((sc_start_x + 0.003, sc_y),
                           (sc_box1_cx - sc_bw / 2 - 0.004, sc_y),
                           arrowstyle='->', mutation_scale=10,
                           color='#AAAAAA', linewidth=1.0, zorder=2)
ax.add_patch(arr_sc_h)

sc_boxes = [
    {"label": "Majority\nVote", "cx": sc_box1_cx},
    {"label": "Answer",         "cx": sc_box2_cx},
]
for sb in sc_boxes:
    x = sb["cx"] - sc_bw / 2
    rect = FancyBboxPatch((x, sc_y - sc_bh / 2), sc_bw, sc_bh,
                          boxstyle="round,pad=0.01",
                          facecolor='#F2F3F4', edgecolor='#AAAAAA',
                          linewidth=1.0, zorder=3)
    ax.add_patch(rect)
    ax.text(sb["cx"], sc_y, sb["label"], ha='center', va='center',
            fontsize=9.5, fontfamily='serif', color='#777777',
            linespacing=1.2, zorder=4)

# Arrow between SC boxes
arr_sc = FancyArrowPatch((sc_boxes[0]["cx"] + sc_bw / 2 + 0.004, sc_y),
                         (sc_boxes[1]["cx"] - sc_bw / 2 - 0.004, sc_y),
                         arrowstyle='->', mutation_scale=10,
                         color='#AAAAAA', linewidth=1.0, zorder=2)
ax.add_patch(arr_sc)

# --- Oracle path (gray dashed arrows from above into boxes 4 & 5) ---
oracle_y_top = by2 + 0.06
for i_target in [3, 4]:
    cx_t = box_centers[i_target][0]
    arr_o = FancyArrowPatch((cx_t, oracle_y_top),
                            (cx_t, y_main + bh / 2 + 0.004),
                            arrowstyle='->', mutation_scale=10,
                            color='#BBBBBB', linewidth=0.9,
                            linestyle='--', zorder=2)
    ax.add_patch(arr_o)

oracle_label_x = (box_centers[3][0] + box_centers[4][0]) / 2
ax.text(oracle_label_x, oracle_y_top + 0.012, "oracle: gold FOL",
        ha='center', va='bottom', fontsize=8.5, fontstyle='italic',
        color='#999999', fontfamily='serif', zorder=4)

plt.subplots_adjust(left=0.02, right=0.98, top=0.95, bottom=0.04)
out = Path(__file__).parent
fig.savefig(out / "fig1_pipeline_v7.png", dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
fig.savefig(out / "fig1_pipeline_v7.pdf", bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Saved fig1_pipeline_v7.png and .pdf")
plt.close()

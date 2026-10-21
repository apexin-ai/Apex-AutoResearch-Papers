#!/usr/bin/env python3
"""Generate Fig 1: STA Overview (3-panel horizontal layout)."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np

# ── Okabe-Ito palette (colorblind-safe) ──
OI_BLUE    = "#0072B2"
OI_ORANGE  = "#E69F00"
OI_GREEN   = "#009E73"
OI_RED     = "#D55E00"
OI_PURPLE  = "#CC79A7"
OI_SKY     = "#56B4E9"
OI_YELLOW  = "#F0E442"
OI_BLACK   = "#000000"

LIGHT_GRAY = "#F2F2F2"
MID_GRAY   = "#CCCCCC"
DARK_GRAY  = "#444444"

# ── Global style ──
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Helvetica", "Arial"],
    "font.size": 10,
    "axes.linewidth": 0,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

fig, axes = plt.subplots(1, 3, figsize=(15, 4.5),
                         gridspec_kw={"width_ratios": [1.1, 1.15, 0.75],
                                      "wspace": 0.08})

for ax in axes:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")


# ═══════════════════════════════════════════
# Helper functions
# ═══════════════════════════════════════════
def draw_box(ax, xy, w, h, text, fc=LIGHT_GRAY, ec=DARK_GRAY,
             fontsize=9, fontweight="normal", text_color=OI_BLACK,
             boxstyle="round,pad=0.15", lw=1.2, zorder=3):
    x, y = xy
    box = FancyBboxPatch((x, y), w, h, boxstyle=boxstyle,
                         facecolor=fc, edgecolor=ec, linewidth=lw,
                         zorder=zorder)
    ax.add_patch(box)
    ax.text(x + w / 2, y + h / 2, text,
            ha="center", va="center", fontsize=fontsize,
            fontweight=fontweight, color=text_color, zorder=zorder + 1)
    return box


def arrow(ax, xy_start, xy_end, color=DARK_GRAY, lw=1.3,
          style="->", connectionstyle="arc3,rad=0", shrinkA=3, shrinkB=3):
    a = FancyArrowPatch(xy_start, xy_end,
                        arrowstyle=style, color=color,
                        lw=lw, connectionstyle=connectionstyle,
                        shrinkA=shrinkA, shrinkB=shrinkB,
                        zorder=5, mutation_scale=12)
    ax.add_patch(a)
    return a


# ═══════════════════════════════════════════
# Panel (a): Formalization Pipeline
# ═══════════════════════════════════════════
ax = axes[0]
ax.text(0.15, 9.5, "(a)", fontsize=12, fontweight="bold", va="top")
ax.text(5.0, 9.5, "Formalization Pipeline", fontsize=11,
        fontweight="bold", ha="center", va="top")

# Boxes – vertical flow, centered
bw, bh = 5.0, 1.0
cx = 2.5  # left edge so center is at 5.0
boxes_a = [
    ("NL Problem", OI_SKY + "44", OI_BLUE),
    ("LLM Formalizer", OI_ORANGE + "33", OI_ORANGE),
    ("Formal Logic\n(FOL / Prolog)", OI_SKY + "44", OI_BLUE),
    ("External Solver\n(Prover9 / SWI-Prolog)", MID_GRAY + "66", DARK_GRAY),
]

y_positions = [7.4, 5.6, 3.6, 1.4]

for i, (label, fc, ec) in enumerate(boxes_a):
    y = y_positions[i]
    draw_box(ax, (cx, y), bw, bh, label, fc=fc, ec=ec,
             fontsize=9, fontweight="bold" if i == 1 else "normal")

# Arrows between boxes
for i in range(len(y_positions) - 1):
    y_from = y_positions[i]
    y_to = y_positions[i + 1] + bh
    arrow(ax, (cx + bw / 2, y_from), (cx + bw / 2, y_to),
          color=DARK_GRAY, lw=1.5, shrinkA=5, shrinkB=5)

# Result labels at bottom
draw_box(ax, (1.0, 0.0), 3.0, 0.8, "Proved ✓", fc=OI_GREEN + "44",
         ec=OI_GREEN, fontsize=9, fontweight="bold", text_color=OI_GREEN)
draw_box(ax, (5.5, 0.0), 3.0, 0.8, "Failed ✗", fc=OI_RED + "33",
         ec=OI_RED, fontsize=9, fontweight="bold", text_color=OI_RED)

# Arrows to results
arrow(ax, (cx + bw / 2 - 0.8, y_positions[3]),
      (2.5, 0.8), color=OI_GREEN, lw=1.3, shrinkA=5, shrinkB=5,
      connectionstyle="arc3,rad=0.15")
arrow(ax, (cx + bw / 2 + 0.8, y_positions[3]),
      (7.0, 0.8), color=OI_RED, lw=1.3, shrinkA=5, shrinkB=5,
      connectionstyle="arc3,rad=-0.15")


# ═══════════════════════════════════════════
# Panel (b): STA Protocol
# ═══════════════════════════════════════════
ax = axes[1]
ax.text(0.15, 9.5, "(b)", fontsize=12, fontweight="bold", va="top")
ax.text(5.0, 9.5, "Solver Trace Ablation (STA)", fontsize=11,
        fontweight="bold", ha="center", va="top")

# Top box: proved formalization with components
draw_box(ax, (0.8, 7.3), 8.4, 1.3,
         "Proved formalization with $n$ clauses",
         fc=OI_GREEN + "22", ec=OI_GREEN, fontsize=9, fontweight="bold")

# Component visualization
comp_labels = ["$c_1$", "$c_2$", "$c_3$", "…", "$c_n$"]
comp_x = [1.5, 3.0, 4.5, 6.0, 7.5]
for i, (lbl, x) in enumerate(zip(comp_labels, comp_x)):
    if lbl == "…":
        ax.text(x, 6.4, "⋯", fontsize=14, ha="center", va="center",
                color=DARK_GRAY)
    else:
        draw_box(ax, (x - 0.5, 6.0, ), 1.0, 0.8, lbl,
                 fc=OI_BLUE + "22", ec=OI_BLUE, fontsize=9)

# LOO ablation examples
ax.text(0.5, 5.1, "Leave-One-Out:", fontsize=9, fontweight="bold",
        color=DARK_GRAY, va="center")

# Row 1: remove c1 → Failed ✓ (necessary)
row1_y = 4.2
ax.text(0.7, row1_y + 0.35, "Remove $c_1$:", fontsize=8.5, va="center",
        color=DARK_GRAY)
# mini components
mini_labels = ["╳", "$c_2$", "$c_3$", "…", "$c_n$"]
mini_x = [3.0, 3.9, 4.8, 5.7, 6.6]
for lbl, x in zip(mini_labels, mini_x):
    if lbl == "╳":
        draw_box(ax, (x - 0.35, row1_y, ), 0.7, 0.7, "",
                 fc=OI_RED + "22", ec=OI_RED, fontsize=8, lw=0.8)
        ax.text(x, row1_y + 0.35, "✕", fontsize=10, ha="center",
                va="center", color=OI_RED, fontweight="bold")
    elif lbl == "…":
        ax.text(x, row1_y + 0.35, "⋯", fontsize=11, ha="center",
                va="center", color=DARK_GRAY)
    else:
        draw_box(ax, (x - 0.35, row1_y), 0.7, 0.7, lbl,
                 fc=OI_BLUE + "22", ec=OI_BLUE, fontsize=8, lw=0.8)

# Arrow → result
arrow(ax, (7.3, row1_y + 0.35), (8.0, row1_y + 0.35),
      color=DARK_GRAY, lw=1.0, shrinkA=2, shrinkB=2)
ax.text(9.0, row1_y + 0.35, "Failed ✓", fontsize=8.5, ha="center",
        va="center", color=OI_GREEN, fontweight="bold")
ax.text(9.0, row1_y - 0.15, "necessary", fontsize=8, ha="center",
        va="center", color=OI_GREEN, fontstyle="italic")

# Row 2: remove c2 → Proved ✗ (redundant)
row2_y = 2.8
ax.text(0.7, row2_y + 0.35, "Remove $c_2$:", fontsize=8.5, va="center",
        color=DARK_GRAY)
mini_labels2 = ["$c_1$", "╳", "$c_3$", "…", "$c_n$"]
for lbl, x in zip(mini_labels2, mini_x):
    if lbl == "╳":
        draw_box(ax, (x - 0.35, row2_y), 0.7, 0.7, "",
                 fc=OI_RED + "22", ec=OI_RED, fontsize=8, lw=0.8)
        ax.text(x, row2_y + 0.35, "✕", fontsize=10, ha="center",
                va="center", color=OI_RED, fontweight="bold")
    elif lbl == "…":
        ax.text(x, row2_y + 0.35, "⋯", fontsize=11, ha="center",
                va="center", color=DARK_GRAY)
    else:
        draw_box(ax, (x - 0.35, row2_y), 0.7, 0.7, lbl,
                 fc=OI_BLUE + "22", ec=OI_BLUE, fontsize=8, lw=0.8)

arrow(ax, (7.3, row2_y + 0.35), (8.0, row2_y + 0.35),
      color=DARK_GRAY, lw=1.0, shrinkA=2, shrinkB=2)
ax.text(9.0, row2_y + 0.35, "Proved ✗", fontsize=8.5, ha="center",
        va="center", color=OI_RED, fontweight="bold")
ax.text(9.0, row2_y - 0.15, "redundant", fontsize=8, ha="center",
        va="center", color=OI_RED, fontstyle="italic")

# ISR formula at bottom
ax.text(5.0, 1.4, r"$\mathrm{ISR} = \frac{n_{\mathrm{necessary}}}{n}$",
        fontsize=13, ha="center", va="center", color=OI_BLACK,
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.4", facecolor=OI_YELLOW + "55",
                  edgecolor=OI_ORANGE, linewidth=1.2))

# Separator line
ax.text(5.0, 0.4, "ISR = 1 → every clause essential",
        fontsize=8, ha="center", va="center", color=DARK_GRAY,
        fontstyle="italic")


# ═══════════════════════════════════════════
# Panel (c): ISR Dual Role
# ═══════════════════════════════════════════
ax = axes[2]
ax.text(0.15, 9.5, "(c)", fontsize=12, fontweight="bold", va="top")
ax.text(5.0, 9.5, "ISR Dual Role", fontsize=11,
        fontweight="bold", ha="center", va="top")

# ISR box at top
draw_box(ax, (2.5, 7.5), 5.0, 1.2, "ISR Metric",
         fc=OI_YELLOW + "55", ec=OI_ORANGE, fontsize=10, fontweight="bold")

# Fork arrows
# Left path: post-hoc diagnostic
arrow(ax, (3.5, 7.5), (2.5, 6.3),
      color=OI_GREEN, lw=1.8, shrinkA=5, shrinkB=5,
      connectionstyle="arc3,rad=0.15")
# Right path: training reward
arrow(ax, (6.5, 7.5), (7.5, 6.3),
      color=OI_RED, lw=1.8, shrinkA=5, shrinkB=5,
      connectionstyle="arc3,rad=-0.15")

# Left branch: Post-hoc Diagnostic
draw_box(ax, (0.3, 4.8), 4.5, 1.5, "Post-hoc\nDiagnostic",
         fc=OI_GREEN + "22", ec=OI_GREEN, fontsize=9.5, fontweight="bold")

# Right branch: Training Reward
draw_box(ax, (5.2, 4.8), 4.5, 1.5, "Training\nReward",
         fc=OI_RED + "22", ec=OI_RED, fontsize=9.5, fontweight="bold")

# Left result: green check
draw_box(ax, (0.8, 2.6), 3.5, 1.5, "",
         fc=OI_GREEN + "11", ec=OI_GREEN, fontsize=9, lw=0.8)
ax.text(2.55, 3.6, "✓", fontsize=18, ha="center", va="center",
        color=OI_GREEN, fontweight="bold")
ax.text(2.55, 2.9, "Detects hacking", fontsize=8, ha="center",
        va="center", color=OI_GREEN, fontweight="bold")

arrow(ax, (2.55, 4.8), (2.55, 4.1),
      color=OI_GREEN, lw=1.3, shrinkA=3, shrinkB=3)

# Right result: red X
draw_box(ax, (5.7, 2.6), 3.5, 1.5, "",
         fc=OI_RED + "11", ec=OI_RED, fontsize=9, lw=0.8)
ax.text(7.45, 3.6, "✗", fontsize=18, ha="center", va="center",
        color=OI_RED, fontweight="bold")
ax.text(7.45, 2.9, "Goodhart Effect", fontsize=8, ha="center",
        va="center", color=OI_RED, fontweight="bold")

arrow(ax, (7.45, 4.8), (7.45, 4.1),
      color=OI_RED, lw=1.3, shrinkA=3, shrinkB=3)

# Annotation for Goodhart
ax.text(7.45, 1.8, "Model games the\ndiagnostic itself",
        fontsize=8, ha="center", va="center", color=OI_RED,
        fontstyle="italic",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                  edgecolor=OI_RED, linewidth=0.7, linestyle="--"))


# ═══════════════════════════════════════════
# Divider lines between panels
# ═══════════════════════════════════════════
for i in range(2):
    # Get boundary between axes[i] and axes[i+1]
    bbox_right = axes[i].get_position()
    bbox_left = axes[i + 1].get_position()
    x_mid = (bbox_right.x1 + bbox_left.x0) / 2
    fig.add_artist(plt.Line2D([x_mid, x_mid], [0.08, 0.92],
                              transform=fig.transFigure,
                              color=MID_GRAY, linewidth=0.8,
                              linestyle="--", zorder=0))


# ═══════════════════════════════════════════
# Save
# ═══════════════════════════════════════════
out = "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/fig1_sta_overview.pdf"
fig.savefig(out, format="pdf", dpi=300, bbox_inches="tight",
            pad_inches=0.15)
plt.close()
print(f"Saved: {out}")

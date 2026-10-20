#!/usr/bin/env python3
"""Generate Fig 2: STA Overview — 2-panel version for readability at paper scale."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe

# ── Palette ──
BLUE       = "#2166AC"
LIGHT_BLUE = "#D1E5F0"
RED        = "#B2182B"
LIGHT_RED  = "#FDDBC7"
GREEN      = "#4CAF50"
LIGHT_GREEN = "#E8F5E9"
DARK_GREEN = "#2E7D32"
GRAY       = "#636363"
LIGHT_GRAY = "#F5F5F5"
BORDER     = "#BDBDBD"
DARK       = "#1A1A1A"
WHITE      = "#FFFFFF"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["CMU Serif", "DejaVu Serif", "Times New Roman"],
    "mathtext.fontset": "cm",
    "font.size": 12,
    "axes.linewidth": 0,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

fig = plt.figure(figsize=(10, 4.8))

gs = fig.add_gridspec(1, 2, width_ratios=[1.3, 1.0],
                      wspace=0.10, left=0.02, right=0.98,
                      top=0.92, bottom=0.04)
axes = [fig.add_subplot(gs[0, i]) for i in range(2)]

for ax in axes:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")


def box(ax, x, y, w, h, text, fc=LIGHT_GRAY, ec=GRAY, lw=1.0,
        fontsize=11, fontweight="normal", text_color=DARK,
        style="round,pad=0.15", multiline=False):
    patch = FancyBboxPatch((x, y), w, h, boxstyle=style,
                           facecolor=fc, edgecolor=ec, linewidth=lw, zorder=3)
    ax.add_patch(patch)
    kw = dict(ha="center", va="center", fontsize=fontsize,
              fontweight=fontweight, color=text_color, zorder=4)
    if multiline:
        kw["linespacing"] = 1.4
    ax.text(x + w/2, y + h/2, text, **kw)


def arr(ax, x0, y0, x1, y1, color=GRAY, lw=1.4, style="-|>",
        conn="arc3,rad=0", shrA=5, shrB=5):
    a = FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=style,
                        color=color, lw=lw, connectionstyle=conn,
                        shrinkA=shrA, shrinkB=shrB, zorder=5,
                        mutation_scale=14)
    ax.add_patch(a)


def panel_title(ax, label, title, x_title=5.0):
    ax.text(0.15, 9.7, label, fontsize=15, fontweight="bold", va="top",
            color=DARK, family="sans-serif")
    ax.text(x_title, 9.7, title, fontsize=13.5,
            fontweight="bold", ha="center", va="top", color=DARK,
            family="sans-serif")


# ═══════════════════════════════════════════════════════════
# (a) STA Leave-One-Out
# ═══════════════════════════════════════════════════════════
ax = axes[0]
panel_title(ax, "(a)", "Solver Trace Ablation", x_title=5.2)

# Proved formalization header
box(ax, 0.3, 7.8, 9.4, 1.1,
    r"Proved formalization  $F = \{c_1, c_2, \ldots, c_n\}$",
    fc=LIGHT_GREEN, ec=GREEN, lw=1.5, fontsize=12.5, fontweight="bold",
    text_color=DARK_GREEN)

# Component boxes row
cw, ch = 1.10, 0.90
comp_x = [0.70, 2.15, 3.60, 5.05, 6.50, 7.95]
comp_labels = ["$c_1$", "$c_2$", "$c_3$", "$c_4$", r"$\cdots$", "$c_n$"]
cy = 6.35

for i, (lbl, x) in enumerate(zip(comp_labels, comp_x)):
    if r"\cdots" in lbl:
        ax.text(x + cw/2, cy + ch/2, r"$\cdots$", fontsize=16,
                ha="center", va="center", color=GRAY)
    else:
        box(ax, x, cy, cw, ch, lbl, fc=LIGHT_BLUE, ec=BLUE,
            lw=1.0, fontsize=12, text_color=BLUE)

# LOO section label
ax.text(0.05, 4.50, "LOO", fontsize=11, fontweight="bold",
        color=DARK, va="center", ha="center", family="sans-serif")
ax.text(0.05, 3.95, "test", fontsize=11, fontweight="bold",
        color=DARK, va="center", ha="center", family="sans-serif")

# Bracket
ax.plot([0.42, 0.42], [2.85, 5.65], color=BORDER, lw=1.2, zorder=2)
ax.plot([0.35, 0.42], [5.65, 5.65], color=BORDER, lw=1.2, zorder=2)
ax.plot([0.35, 0.42], [2.85, 2.85], color=BORDER, lw=1.2, zorder=2)


def draw_loo_row(ax, y, removed_idx, result_text, result_color, label):
    for i, x in enumerate(comp_x):
        if r"\cdots" in comp_labels[i]:
            ax.text(x + cw/2, y + ch/2, r"$\cdots$", fontsize=14,
                    ha="center", va="center", color=GRAY)
        elif i == removed_idx:
            box(ax, x, y, cw, ch, "", fc=LIGHT_RED, ec=RED, lw=1.0)
            margin = 0.20
            ax.plot([x+margin, x+cw-margin], [y+margin, y+ch-margin],
                    color=RED, lw=2.5, zorder=6, solid_capstyle="round")
            ax.plot([x+margin, x+cw-margin], [y+ch-margin, y+margin],
                    color=RED, lw=2.5, zorder=6, solid_capstyle="round")
        else:
            box(ax, x, y, cw, ch, comp_labels[i], fc=LIGHT_BLUE, ec=BLUE,
                lw=0.7, fontsize=11, text_color=BLUE)

    # Result
    x_end = comp_x[-1] + cw + 0.15
    arr(ax, x_end, y + ch/2, x_end + 0.55, y + ch/2,
        color=GRAY, lw=1.1)
    ax.text(x_end + 0.70, y + ch/2 + 0.15, result_text,
            fontsize=11, fontweight="bold", color=result_color, va="center")
    ax.text(x_end + 0.70, y + ch/2 - 0.28, label,
            fontsize=9, color=result_color, va="center", fontstyle="italic")


draw_loo_row(ax, 4.85, 0, "Fail", DARK_GREEN, "necessary")
draw_loo_row(ax, 3.45, 1, "Prove", RED, "redundant")
draw_loo_row(ax, 2.05, 3, "Fail", DARK_GREEN, "necessary")

# ISR formula
box(ax, 1.2, 0.20, 7.6, 1.45, "",
    fc=WHITE, ec=BLUE, lw=1.8, style="round,pad=0.2")
ax.text(5.0, 0.92,
        r"$\mathrm{ISR}(F) \;=\; \frac{|\{c_i : S(F\!\setminus\!\{c_i\}) = \mathrm{fail}\}|}{n}$",
        fontsize=16, ha="center", va="center", color=DARK)


# ═══════════════════════════════════════════════════════════
# (b) ISR Dual Role — Observe vs Optimize
# ═══════════════════════════════════════════════════════════
ax = axes[1]
panel_title(ax, "(b)", "Observe vs. Optimize")

# ISR metric at top
box(ax, 1.5, 7.7, 7.0, 1.3, "ISR Metric", fc=WHITE, ec=DARK,
    lw=2.0, fontsize=14, fontweight="bold")

# Fork arrows
arr(ax, 3.5, 7.7, 2.3, 6.65, color=GREEN, lw=1.8,
    conn="arc3,rad=0.12")
arr(ax, 6.5, 7.7, 7.7, 6.65, color=RED, lw=1.8,
    conn="arc3,rad=-0.12")

# Two role boxes
box(ax, 0.1, 4.85, 4.3, 1.8, "Post-hoc\nDiagnostic",
    fc=LIGHT_GREEN, ec=GREEN, lw=1.5, fontsize=13,
    fontweight="bold", text_color=DARK_GREEN, multiline=True)

box(ax, 5.6, 4.85, 4.3, 1.8, "Training\nReward",
    fc=LIGHT_RED, ec=RED, lw=1.5, fontsize=13,
    fontweight="bold", text_color=RED, multiline=True)

# Outcome arrows
arr(ax, 2.25, 4.85, 2.25, 3.65, color=GREEN, lw=1.5)
arr(ax, 7.75, 4.85, 7.75, 3.65, color=RED, lw=1.5)

# Outcome descriptions
box(ax, 0.1, 2.2, 4.3, 1.45, "Detects structural\ndegeneration",
    fc=LIGHT_GREEN, ec=GREEN, lw=0.9, fontsize=11,
    text_color=DARK_GREEN, multiline=True)

box(ax, 5.6, 2.2, 4.3, 1.45, "Goodhart effect:\nTS achieves ISR${=}1$",
    fc=LIGHT_RED, ec=RED, lw=0.9, fontsize=11,
    text_color=RED, multiline=True)

# Checkmark (drawn manually)
cx_v, cy_v = 2.25, 1.15
ax.plot([cx_v-0.35, cx_v-0.05, cx_v+0.45],
        [cy_v, cy_v-0.4, cy_v+0.45],
        color=GREEN, lw=3.5, solid_capstyle="round",
        solid_joinstyle="round", zorder=6)
ax.text(2.25, 0.30, "Informative", fontsize=12.5, ha="center", va="center",
        fontweight="bold", color=DARK_GREEN)

# X mark (drawn manually)
cx_x, cy_x = 7.75, 1.15
ax.plot([cx_x-0.32, cx_x+0.32], [cy_x-0.32, cy_x+0.32],
        color=RED, lw=3.5, solid_capstyle="round", zorder=6)
ax.plot([cx_x-0.32, cx_x+0.32], [cy_x+0.32, cy_x-0.32],
        color=RED, lw=3.5, solid_capstyle="round", zorder=6)
ax.text(7.75, 0.30, "Gameable", fontsize=12.5, ha="center", va="center",
        fontweight="bold", color=RED)

# Asymmetry arrow at bottom
ax.annotate("", xy=(6.5, -0.25), xytext=(3.5, -0.25),
            arrowprops=dict(arrowstyle="<->", color=DARK, lw=1.8))
ax.text(5.0, -0.02, "observe–optimize asymmetry",
        fontsize=10, ha="center", va="center", color=DARK,
        fontweight="bold", fontstyle="italic")


# ═══════════════════════════════════════════════════════════
# Panel divider
# ═══════════════════════════════════════════════════════════
fig.canvas.draw()
bbox_r = axes[0].get_position()
bbox_l = axes[1].get_position()
x_mid = (bbox_r.x1 + bbox_l.x0) / 2
fig.add_artist(plt.Line2D([x_mid, x_mid], [0.06, 0.94],
                          transform=fig.transFigure,
                          color=BORDER, linewidth=0.8, zorder=0))


# ═══════════════════════════════════════════════════════════
# Save
# ═══════════════════════════════════════════════════════════
base = "./fig1_sta_overview"
fig.savefig(base + ".pdf", format="pdf", dpi=300, bbox_inches="tight",
            pad_inches=0.10)
fig.savefig(base + ".png", format="png", dpi=250, bbox_inches="tight",
            pad_inches=0.10)
plt.close()
print(f"Saved: {base}.pdf and .png")

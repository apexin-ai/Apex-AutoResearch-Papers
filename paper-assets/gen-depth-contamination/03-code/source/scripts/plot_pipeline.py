#!/usr/bin/env python3
"""Generate Figure 1: Generational depth estimation pipeline diagram."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

plt.rcParams.update({
    "font.family": "serif",
    "mathtext.fontset": "cm",
})

fig, ax = plt.subplots(figsize=(14, 2.8))
ax.set_xlim(-0.3, 14.0)
ax.set_ylim(-0.3, 2.85)
ax.axis("off")

COLORS = {
    "seed":   ("#dae5f0", "#2c4a6b"),
    "gen":    ("#f7ecd1", "#6b5520"),
    "feat":   ("#d9edd5", "#2e5e28"),
    "obd":    ("#e2d6ec", "#4a2d6b"),
    "output": ("#f5dbd0", "#6b3525"),
}

BOX_W = 2.30
BOX_H = 2.05
BOX_Y = 0.0
GAP = 0.50
CORNER = "round,pad=0.10"

boxes = [
    {"x": 0.0,               "key": "seed",   "title": "Seed Text",
     "lines": ["(C4 / arXiv / Wiki)", "256 tokens"]},
    {"x": BOX_W + GAP,       "key": "gen",    "title": "Recursive\nGeneration",
     "lines": [r"$G_\delta = \mathrm{LLM}(\delta)$",
               r"$X \!\to\! Y_1 \!\to\! \cdots \!\to\! Y_K$"]},
    {"x": 2*(BOX_W + GAP),   "key": "feat",   "title": "15D Feature\nExtraction",
     "lines": ["· Surprisal moments",
               "· Surprisal derivatives",
               "· Vocab diversity",
               "· Frequency tail"]},
    {"x": 3*(BOX_W + GAP),   "key": "obd",    "title": "OBD\nLightGBM",
     "lines": [r"$K$ binary classifiers",
               r"$P(\mathrm{depth} > k)$"]},
    {"x": 4*(BOX_W + GAP),   "key": "output", "title": "Output",
     "lines": [r"Depth $\hat{d}$",
               r"$K^*_{\mathrm{empirical}}$"]},
]

for b in boxes:
    bg, fg = COLORS[b["key"]]

    shadow = FancyBboxPatch(
        (b["x"] + 0.035, BOX_Y - 0.035), BOX_W, BOX_H,
        boxstyle=CORNER, facecolor="#00000010", edgecolor="none", zorder=1)
    ax.add_patch(shadow)

    box = FancyBboxPatch(
        (b["x"], BOX_Y), BOX_W, BOX_H,
        boxstyle=CORNER, facecolor=bg, edgecolor=fg, linewidth=1.0, zorder=2)
    ax.add_patch(box)

    cx = b["x"] + BOX_W / 2
    title_lines = b["title"].split("\n")
    title_y = BOX_Y + BOX_H - 0.25
    for i, tl in enumerate(title_lines):
        ax.text(cx, title_y - i * 0.30, tl,
                ha="center", va="top", fontsize=11, fontweight="bold",
                color=fg, zorder=3)

    body_top = title_y - len(title_lines) * 0.30 - 0.08
    for j, line in enumerate(b["lines"]):
        ax.text(cx, body_top - j * 0.27, line,
                ha="center", va="top", fontsize=8.5, color=fg, zorder=3)

for i in range(len(boxes) - 1):
    x_start = boxes[i]["x"] + BOX_W + 0.04
    x_end = boxes[i + 1]["x"] - 0.04
    y_mid = BOX_Y + BOX_H / 2
    ax.annotate("", xy=(x_end, y_mid), xytext=(x_start, y_mid),
                arrowprops=dict(arrowstyle="-|>", color="#555555",
                                lw=1.8, mutation_scale=14),
                zorder=4)

gen = boxes[1]
gcx = gen["x"] + BOX_W / 2
import matplotlib.patches as mpatches
from matplotlib.path import Path as MPath
arrow_y_base = BOX_Y + BOX_H + 0.02
arrow_y_peak = BOX_Y + BOX_H + 0.42
x_left = gen["x"] + 0.25
x_right = gen["x"] + BOX_W - 0.25
verts = [
    (x_right, arrow_y_base),
    (x_right, arrow_y_peak),
    (x_left, arrow_y_peak),
    (x_left, arrow_y_base),
]
codes = [MPath.MOVETO, MPath.CURVE4, MPath.CURVE4, MPath.CURVE4]
path = MPath(verts, codes)
arrow = mpatches.FancyArrowPatch(
    path=path, arrowstyle="-|>", color="#555555", lw=1.3,
    mutation_scale=11, zorder=4)
ax.add_patch(arrow)
ax.text(gcx, arrow_y_peak + 0.06, r"depth $0 \to K$",
        ha="center", va="bottom", fontsize=7.5, fontstyle="italic",
        color="#555555", zorder=4)

out_dir = Path(__file__).resolve().parent.parent / "docs" / "paper" / "figures"
out_dir.mkdir(parents=True, exist_ok=True)

fig.savefig(out_dir / "pipeline.pdf", dpi=300, bbox_inches="tight",
            pad_inches=0.06, facecolor="white")
fig.savefig(out_dir / "pipeline.png", dpi=300, bbox_inches="tight",
            pad_inches=0.06, facecolor="white")
plt.close(fig)
print(f"PDF: {out_dir / 'pipeline.pdf'}")
print(f"PNG: {out_dir / 'pipeline.png'}")

#!/usr/bin/env python3
"""Evidence-Grounded DocRE Task + FREIGE Pipeline overview figure."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

BLUE = "#0072B2"
GRAY = "#999999"
LIGHT_BLUE = "#D0E8F2"
WHITE = "#FFFFFF"
BLACK = "#333333"
ENT_BLUE = "#0072B2"
ENT_GREEN = "#009E73"
ENT_ORANGE = "#E69F00"
ENT_PURPLE = "#CC79A7"
SHADOW = "#D0D0D0"
RSFT_BG = "#FFF8F0"
RSFT_BORDER = "#D4A574"
RSFT_ACCENT = "#8B6914"

matplotlib.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica"],
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})


def draw_box(ax, xy, w, h, facecolor=WHITE, edgecolor=BLACK,
             lw=1.2, ls="-", pad=0.02, zorder=2, shadow=False,
             shadow_alpha=0.30):
    if shadow:
        sh = FancyBboxPatch((xy[0] + 0.03, xy[1] - 0.03), w, h,
                            boxstyle=f"round,pad={pad}",
                            facecolor=SHADOW, edgecolor="none",
                            linewidth=0, zorder=zorder - 1, alpha=shadow_alpha)
        ax.add_patch(sh)
    box = FancyBboxPatch(xy, w, h,
                         boxstyle=f"round,pad={pad}",
                         facecolor=facecolor, edgecolor=edgecolor,
                         linewidth=lw, linestyle=ls, zorder=zorder)
    ax.add_patch(box)
    return box


def arr(ax, xy_a, xy_b, color=BLACK, lw=1.2, cs="arc3,rad=0", zorder=3,
        style="->", shrinkA=0, shrinkB=0, ms=9):
    a = FancyArrowPatch(xy_a, xy_b, arrowstyle=style, color=color,
                        lw=lw, connectionstyle=cs,
                        zorder=zorder, mutation_scale=ms,
                        shrinkA=shrinkA, shrinkB=shrinkB)
    ax.add_patch(a)


def colored_text(ax, x, y, pieces, fontsize=7, va="top"):
    fig = ax.get_figure()
    renderer = fig.canvas.get_renderer()
    cx = x
    for txt, col, bold in pieces:
        t = ax.text(cx, y, txt, fontsize=fontsize, va=va, color=col,
                    fontweight="bold" if bold else "normal")
        fig.canvas.draw()
        bb = t.get_window_extent(renderer=renderer)
        bb_data = bb.transformed(ax.transData.inverted())
        cx = bb_data.x1 - 0.008
    return cx


fig, ax = plt.subplots(figsize=(7.2, 4.0), dpi=300)
ax.set_xlim(-0.15, 7.35)
ax.set_ylim(-0.15, 4.05)
ax.axis("off")
fig.patch.set_facecolor("white")

# ===== Document Panel =====
doc_x, doc_y, doc_w, doc_h = 0.0, 1.62, 1.62, 1.60
draw_box(ax, (doc_x, doc_y), doc_w, doc_h, facecolor="#FAFAFA",
         edgecolor="#CCCCCC", lw=0.8, shadow=True)
ax.text(doc_x + doc_w / 2, doc_y + doc_h - 0.10, "Document",
        ha="center", va="top", fontsize=9, fontweight="bold", color=BLACK)

sx = doc_x + 0.10
fs = 7.5
lh = 0.28
s_top = doc_y + doc_h - 0.42

colored_text(ax, sx, s_top, [
    ("[S1] ", GRAY, False), ("John", ENT_BLUE, True),
    (" was born in ", BLACK, False), ("London", ENT_GREEN, True),
    (".", BLACK, False)
], fontsize=fs)

colored_text(ax, sx, s_top - lh, [
    ("[S2] ", GRAY, False), ("He", BLACK, False),
    (" studied at ", BLACK, False), ("Oxford", ENT_ORANGE, True),
    (".", BLACK, False)
], fontsize=fs)

colored_text(ax, sx, s_top - 2 * lh, [
    ("[S3] ", GRAY, False), ("London", ENT_GREEN, True),
    (" is in ", BLACK, False), ("England", ENT_PURPLE, True),
    (".", BLACK, False)
], fontsize=fs)

lx = sx
legend_y = doc_y + 0.16
for name, col in [("John", ENT_BLUE), ("London", ENT_GREEN),
                   ("Oxford", ENT_ORANGE), ("England", ENT_PURPLE)]:
    ax.plot(lx, legend_y, "s", color=col, markersize=3.5, zorder=4)
    t = ax.text(lx + 0.06, legend_y, name, fontsize=6, va="center", color=col,
                fontweight="bold")
    fig.canvas.draw()
    bb = t.get_window_extent(renderer=fig.canvas.get_renderer())
    bb_data = bb.transformed(ax.transData.inverted())
    lx = bb_data.x1 + 0.06

# ===== LLM Box =====
llm_x, llm_y, llm_w, llm_h = 2.10, 1.98, 1.15, 0.82
draw_box(ax, (llm_x, llm_y), llm_w, llm_h, facecolor=LIGHT_BLUE,
         edgecolor=BLUE, lw=1.6, shadow=True)
ax.text(llm_x + llm_w / 2, llm_y + llm_h / 2 + 0.12, "LLM",
        ha="center", va="center", fontsize=11, fontweight="bold", color=BLUE)
ax.text(llm_x + llm_w / 2, llm_y + llm_h / 2 - 0.14, "(Qwen3 / LLaMA)",
        ha="center", va="center", fontsize=6.5, color="#4A90C4")

# Arrow: Document → LLM
arr(ax, (doc_x + doc_w + 0.04, doc_y + doc_h / 2 + 0.02),
    (llm_x - 0.04, llm_y + llm_h / 2),
    color="#888888", lw=1.2, cs="arc3,rad=0.06")

# ===== Output Boxes =====
out_x = 3.75
out_w = 3.40

# Standard DocRE (dashed, de-emphasized)
std_y, std_h = 2.80, 0.62
draw_box(ax, (out_x, std_y), out_w, std_h,
         facecolor="#F9F9F9", edgecolor="#BBBBBB", lw=0.9, ls="--")
ax.text(out_x + 0.12, std_y + std_h - 0.08, "Standard DocRE",
        ha="left", va="top", fontsize=8.5, fontweight="bold", color=GRAY)

tx = out_x + 0.14
ax.text(tx, std_y + std_h - 0.27,
        "(John, place_of_birth, London)", fontsize=6, va="top",
        color="#777777", family="monospace")
ax.text(tx, std_y + std_h - 0.44,
        "(John, educated_at, Oxford)", fontsize=6, va="top",
        color="#777777", family="monospace")

# Evidence-Grounded DocRE (Ours) — most prominent element
evi_y, evi_h = 1.50, 1.15
draw_box(ax, (out_x, evi_y), out_w, evi_h,
         facecolor="#EAF4FB", edgecolor=BLUE, lw=2.2, shadow=True,
         shadow_alpha=0.40)
ax.text(out_x + 0.12, evi_y + evi_h - 0.08,
        "Evidence-Grounded DocRE (Ours)",
        ha="left", va="top", fontsize=8.5, fontweight="bold", color=BLUE)

tfs = 6.5
ev_offset = 2.10
trip_y_start = evi_y + evi_h - 0.34
trip_spacing = 0.25

triplets = [
    ("(John, place_of_birth, London)", "| Evidence: [S1]"),
    ("(John, educated_at, Oxford)", "| Evidence: [S2]"),
    ("(London, country, England)", "| Evidence: [S1][S3]"),
]
for i, (trip, evi) in enumerate(triplets):
    y = trip_y_start - i * trip_spacing
    ax.text(tx, y, trip, fontsize=tfs, va="top", color=BLACK, family="monospace")
    ax.text(tx + ev_offset, y, evi, fontsize=tfs, va="top",
            color=BLUE, fontweight="bold", family="monospace")

# Arrows: LLM → Outputs
arr(ax, (llm_x + llm_w + 0.04, llm_y + llm_h * 0.78),
    (out_x - 0.04, std_y + std_h / 2),
    color="#AAAAAA", lw=0.9, cs="arc3,rad=-0.10")
arr(ax, (llm_x + llm_w + 0.04, llm_y + llm_h * 0.30),
    (out_x - 0.04, evi_y + evi_h / 2),
    color=BLUE, lw=1.6, cs="arc3,rad=0.06")

# ===== RSFT Pipeline Strip =====
pipe_y = 0.08
pipe_h = 1.05
pipe_w = 7.2
draw_box(ax, (0.0, pipe_y), pipe_w, pipe_h,
         facecolor=RSFT_BG, edgecolor=RSFT_BORDER, lw=1.0, pad=0.03,
         shadow=True)

ax.text(0.14, pipe_y + pipe_h - 0.06,
        "Rejection Sampling Fine-Tuning (RSFT)",
        ha="left", va="top", fontsize=7.5, fontweight="bold", color=RSFT_ACCENT)

steps = ["SFT Model", "Sample\nN responses", "CED / NLI\nScore", "Select\nTop-K", "Fine-tune"]
box_w = 1.05
box_h = 0.42
gap = 0.30
total_w = len(steps) * box_w + (len(steps) - 1) * gap
sx_start = (pipe_w - total_w) / 2
cy = pipe_y + 0.22

for i, label in enumerate(steps):
    bx = sx_start + i * (box_w + gap)
    if i in (0, 4):
        fc, ec, lw_b = LIGHT_BLUE, BLUE, 1.2
    else:
        fc, ec, lw_b = WHITE, "#888888", 0.8
    draw_box(ax, (bx, cy), box_w, box_h, facecolor=fc, edgecolor=ec,
             lw=lw_b, shadow=True, pad=0.015)
    ax.text(bx + box_w / 2, cy + box_h / 2, label,
            ha="center", va="center", fontsize=6.5, color=BLACK,
            linespacing=0.9)
    if i < len(steps) - 1:
        arr(ax, (bx + box_w + 0.02, cy + box_h / 2),
            (bx + box_w + gap - 0.02, cy + box_h / 2),
            lw=1.0, color="#888888")

# Feedback loop: Fine-tune → SFT Model (dashed arc below)
ft_cx = sx_start + 4 * (box_w + gap) + box_w / 2
sft_cx = sx_start + box_w / 2
ax.annotate("", xy=(sft_cx, cy - 0.01), xytext=(ft_cx, cy - 0.01),
            arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.0,
                            connectionstyle="arc3,rad=0.45",
                            linestyle="--", mutation_scale=9))
ax.text((sft_cx + ft_cx) / 2, cy - 0.19, "iterate",
        ha="center", va="top", fontsize=6, color=BLUE, fontstyle="italic",
        fontweight="bold")

fig.tight_layout(pad=0.1)
out_base = "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_overview"
fig.savefig(f"{out_base}.pdf", dpi=300, bbox_inches="tight", pad_inches=0.03)
fig.savefig(f"{out_base}.png", dpi=300, bbox_inches="tight", pad_inches=0.03)
print(f"Saved: {out_base}.pdf / .png")

#!/usr/bin/env python3
"""Generate forest plot of HS precision advantage over text probes (Figure 3).

Data source: Table 2 (tab:hs_vs_text) in experiments.tex.
Output: docs/paper/figures/fig_forest_precision.{pdf,png}
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# ── Unified rcParams ────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Times'],
    'mathtext.fontset': 'dejavuserif',
    'font.size': 8,
    'axes.titlesize': 9,
    'axes.labelsize': 8.5,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 7.5,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.5,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.2,
})

# ── Color-blind safe palette (Okabe-Ito) ────────────────────────────
COLOR_384D  = '#0072B2'   # blue
COLOR_1024D = '#E69F00'   # orange

# ── Data ────────────────────────────────────────────────────────────
models = ["R1-8B", "OT-7B", "QwQ-32B", "R1-32B"]

data_384d = {
    "delta": [20.1, 21.9, 19.2, 15.4],
    "ci_lo": [12.4, 14.4, 9.3, 8.7],
    "ci_hi": [28.3, 29.6, 33.5, 22.6],
    "hb":    [True, True, True, True],
}

data_1024d = {
    "delta": [5.8, 18.1, 9.4, 11.7],
    "ci_lo": [-7.4, 8.4, -7.1, -0.2],
    "ci_hi": [19.5, 29.0, 27.7, 24.3],
    "hb":    [False, True, False, False],
}

# ── Build figure ────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(3.4, 2.2))

y_positions = np.arange(len(models)) * 0.65  # compact row spacing
offset = 0.13  # vertical offset between paired points

# Equivalence band: +/-5pp shaded region
ax.axvspan(-5, 5, color='0.93', zorder=0, label='_nolegend_')
ax.axvline(0, color="0.5", linewidth=0.6, linestyle="-", zorder=1)
# Label the equivalence band edge
ax.text(5.3, y_positions[0] - 0.35, r"$\pm$5 pp", fontsize=4.5,
        color="0.55", va="top", ha="left", style="italic")

for i, model in enumerate(models):
    for enc_idx, (enc_data, color) in enumerate([
        (data_384d, COLOR_384D),
        (data_1024d, COLOR_1024D),
    ]):
        y = y_positions[i] + (offset if enc_idx == 0 else -offset)
        delta = enc_data["delta"][i]
        lo = enc_data["ci_lo"][i]
        hi = enc_data["ci_hi"][i]
        hb = enc_data["hb"][i]

        facecolor = color if hb else "white"

        # CI whiskers
        ax.errorbar(
            delta, y,
            xerr=[[delta - lo], [hi - delta]],
            fmt="none", ecolor=color, capsize=2.0, capthick=0.7, linewidth=0.7,
            zorder=3,
        )
        # Diamond marker
        ax.plot(
            delta, y,
            marker="D", markersize=4.5,
            color=color, markerfacecolor=facecolor,
            markeredgewidth=0.9, markeredgecolor=color,
            zorder=5,
        )
        # Inline delta value — place to right of CI upper bound
        label_text = f"+{delta:.1f}"
        ax.annotate(
            label_text,
            xy=(hi + 0.8, y),
            fontsize=5, color=color, ha="left", va="center",
            fontweight="bold",
        )

ax.set_yticks(y_positions)
ax.set_yticklabels(models, fontsize=8)
ax.set_xlabel(r"$\Delta$ Precision (pp, HS $-$ Text)", fontsize=8.5)

# ── Legend ──────────────────────────────────────────────────────────
legend_elements = [
    Line2D([0], [0], marker="D", color=COLOR_384D, markerfacecolor=COLOR_384D,
           markersize=4.5, linewidth=0.8, label="vs. MiniLM-384d"),
    Line2D([0], [0], marker="D", color=COLOR_1024D, markerfacecolor=COLOR_1024D,
           markersize=4.5, linewidth=0.8, label="vs. BGE-1024d"),
    Line2D([0], [0], marker="D", color="0.5", markerfacecolor="white",
           markeredgewidth=1.0, markersize=4.5, linestyle="None",
           label="Hollow = fails HB"),
]
ax.legend(
    handles=legend_elements,
    fontsize=6,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.28),
    ncol=3,
    framealpha=0.9,
    edgecolor="0.8",
    columnspacing=0.8,
    handletextpad=0.3,
)

ax.invert_yaxis()
ax.set_xlim(-15, 42)
# Tighten y-axis
ax.set_ylim(y_positions[-1] + 0.38, y_positions[0] - 0.38)

plt.tight_layout()

# ── Save ────────────────────────────────────────────────────────────
out_path = "docs/paper/figures/fig_forest_precision.pdf"
fig.savefig(out_path, bbox_inches="tight", dpi=300)
print(f"Saved: {out_path}")

out_png = out_path.replace(".pdf", ".png")
fig.savefig(out_png, bbox_inches="tight", dpi=300)
print(f"Saved: {out_png}")

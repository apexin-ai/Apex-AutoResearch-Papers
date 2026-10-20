#!/usr/bin/env python3
"""Regenerate Figure 2 (AUC decay) with column-width-optimized layout.

Fixes: x-axis label overlap at \columnwidth by shortening labels and
sizing the figure for direct column-width embedding (no scaling).

Data hardcoded from registry (verified against Table 1 / Table S2).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# ── Data from registry ──
MODELS = {
    "Qwen-rw": {
        "auc": [0.9956, 0.6955, 0.5893, 0.5435, 0.5340],
        "ci_lo": [0.993, 0.686, 0.580, 0.534, 0.524],
        "ci_hi": [0.998, 0.704, 0.599, 0.553, 0.544],
    },
    "Pythia": {
        "auc": [0.9932, 0.6539, 0.5514, 0.5152, 0.5136],
        "ci_lo": [0.991, 0.645, 0.542, 0.505, 0.504],
        "ci_hi": [0.996, 0.663, 0.563, 0.525, 0.524],
    },
    "OLMo": {
        "auc": [0.9860, 0.5080, 0.4973, 0.5024, 0.4942],
        "ci_lo": [0.983, 0.496, 0.486, 0.492, 0.484],
        "ci_hi": [0.989, 0.519, 0.509, 0.513, 0.505],
    },
    "Qwen-cont": {
        "auc": [0.9971, 0.6112, 0.5609, 0.5409, 0.5141],
        "ci_lo": [0.996, 0.602, 0.551, 0.531, 0.504],
        "ci_hi": [0.999, 0.621, 0.571, 0.551, 0.524],
    },
    r"Qwen-7B$^{\ddagger}$": {
        "auc": [0.9638, 0.6168, 0.5492, 0.5276, 0.5085],
        "ci_lo": [0.961, 0.608, 0.539, 0.517, 0.499],
        "ci_hi": [0.967, 0.626, 0.559, 0.538, 0.519],
    },
    "LLaMA-8B": {
        "auc": [0.9225, 0.6123, 0.5274, 0.5138, 0.5097],
        "ci_lo": [0.917, 0.603, 0.517, 0.506, 0.505],
        "ci_hi": [0.927, 0.622, 0.538, 0.528, 0.527],
    },
    "Mistral-7B": {
        "auc": [0.9843, 0.5935, 0.5402, 0.5232, 0.5181],
        "ci_lo": [0.981, 0.584, 0.530, 0.513, 0.508],
        "ci_hi": [0.988, 0.603, 0.550, 0.533, 0.528],
    },
}

DECODING = {
    "Greedy": {
        "auc": [0.9992, 0.8838, 0.5342, 0.5228, 0.5162],
    },
    r"Nuc $p\!=\!0.9$": {
        "auc": [0.9948, 0.6770, 0.5549, 0.5299, 0.5013],
    },
    r"$T\!=\!0.7$": {
        "auc": [0.9965, 0.7265, 0.5941, 0.5698, 0.5284],
    },
    r"$T\!=\!1.2$": {
        "auc": [0.9933, 0.6172, 0.5226, 0.5170, 0.5051],
    },
}

TABLEAU = [
    "#4e79a7", "#e15759", "#76b7b2", "#59a14f",
    "#b07aa1", "#ff9da7", "#9c755f",
]
MARKERS = ["o", "s", "^", "D", "v", "P", "X"]
DECODE_COLORS = ["#edc948", "#f28e2b", "#bab0ac", "#76b7b2"]
DECODE_MARKERS = ["*", "h", "<", ">"]

x_labels = ["0v1", "1v2", "2v3", "3v4", "4v5"]
x = np.arange(len(x_labels))

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 8,
    "axes.linewidth": 0.6,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "lines.linewidth": 1.2,
    "lines.markersize": 4,
})

fig, ax = plt.subplots(figsize=(3.5, 2.8), constrained_layout=True)

# K* boundary shading
ax.axvspan(0.5, 1.5, color="#fff9c4", alpha=0.55, zorder=0)
ax.text(1.0, 1.02, r"$K^*$ boundary", ha="center", va="bottom",
        fontsize=7, fontstyle="italic", color="#8d6e00")

# Reference lines
ax.axhline(0.60, color="grey", ls="--", lw=0.6, zorder=1)
ax.text(4.45, 0.607, r"$\theta\!=\!0.60$", fontsize=6.5, color="grey",
        va="bottom", ha="right")
ax.axhline(0.50, color="lightgrey", ls="--", lw=0.6, zorder=1)
ax.text(4.45, 0.506, "chance", fontsize=6.5, color="silver",
        va="bottom", ha="right")

# Plot models (solid)
model_handles = []
for i, (label, info) in enumerate(MODELS.items()):
    color = TABLEAU[i]
    marker = MARKERS[i]
    y = np.array(info["auc"])
    line, = ax.plot(x, y, "-", color=color, lw=1.4, marker=marker,
                    markersize=4, label=label, zorder=3)
    if "ci_lo" in info:
        lo = np.array(info["ci_lo"])
        hi = np.array(info["ci_hi"])
        ax.fill_between(x, lo, hi, color=color, alpha=0.12, zorder=2)
    model_handles.append(line)

# Plot decoding (dashed)
decode_handles = []
for i, (label, info) in enumerate(DECODING.items()):
    color = DECODE_COLORS[i]
    marker = DECODE_MARKERS[i]
    y = np.array(info["auc"])
    line, = ax.plot(x, y, "--", color=color, lw=1.4, marker=marker,
                    markersize=4, label=label, zorder=3)
    decode_handles.append(line)

ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.set_xlabel("Depth Pair", fontsize=8)
ax.set_ylabel("Pairwise AUC (5-fold CV)", fontsize=8)
ax.set_ylim(0.45, 1.05)
ax.set_xlim(-0.25, len(x_labels) - 0.75)
ax.tick_params(direction="in", labelsize=7)

# Legends
leg1 = ax.legend(handles=model_handles, title="Models", title_fontsize=7,
                 fontsize=6.5, loc="upper right", bbox_to_anchor=(1.0, 0.98),
                 framealpha=0.9, edgecolor="0.8", handlelength=1.8,
                 borderpad=0.3, labelspacing=0.25)
ax.add_artist(leg1)
ax.legend(handles=decode_handles, title="Decoding", title_fontsize=7,
          fontsize=6.5, loc="center right", bbox_to_anchor=(1.0, 0.42),
          framealpha=0.9, edgecolor="0.8", handlelength=1.8,
          borderpad=0.3, labelspacing=0.25)

# Save
out_dir = Path(__file__).resolve().parent.parent.parent / "docs" / "paper" / "figures"
out_path = out_dir / "fig2_auc_decay.pdf"
fig.savefig(out_path, dpi=300, bbox_inches="tight")
png_path = out_path.with_suffix(".png")
fig.savefig(png_path, dpi=300, bbox_inches="tight")
plt.close(fig)

print(f"PDF: {out_path} ({out_path.stat().st_size / 1024:.1f} KB)")
print(f"PNG: {png_path} ({png_path.stat().st_size / 1024:.1f} KB)")
assert out_path.stat().st_size > 5 * 1024, "PDF too small"
print("OK")

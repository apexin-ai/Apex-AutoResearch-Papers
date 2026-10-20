#!/usr/bin/env python3
"""Figure 1: DDR Partition Bar Chart — v3 with correct zone colors and legend."""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif", "Nimbus Roman"],
    "font.size": 10,
    "axes.linewidth": 0.8,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "mathtext.fontset": "cm",
})

with open("/root/gen-depth-fingerprint/results/8gen_per_gen_spearman.json") as f:
    data = json.load(f)

pooled = data["_median"]
generators = data["_generators"]

FEATURES = [
    ("hapax_ratio",  "Drifting"),
    ("ttr",          "Drifting"),
    ("entropy_mean", "Drifting"),
    ("entropy_min",  "Near-stationary"),
    ("entropy_std",  "Intermediate"),
    ("entropy_max",  "Near-stationary"),
    ("tail_decay",   "Near-stationary"),
]

FEAT_LABELS = {
    "entropy_mean": r"$\bar{H}$ (Entropy Mean)",
    "entropy_std":  r"$\sigma_H$ (Entropy Std)",
    "entropy_min":  r"$H_{\min}$ (Entropy Min)",
    "entropy_max":  r"$H_{\max}$ (Entropy Max)",
    "ttr":          "TTR",
    "hapax_ratio":  "Hapax Ratio",
    "tail_decay":   "Tail Decay",
}

ZONE_COLORS = {
    "Drifting":        "#2ca02c",
    "Intermediate":    "#9467bd",
    "Near-stationary": "#ff7f0e",
}

n = len(FEATURES)
fig, ax = plt.subplots(figsize=(3.4, 3.5))
rng = np.random.default_rng(42)

for i, (feat, group) in enumerate(FEATURES):
    y = n - 1 - i
    rho = pooled[feat]
    ax.barh(y, rho, color=ZONE_COLORS[group], height=0.6, alpha=0.85, zorder=2)
    gen_rhos = [data[g][feat] for g in generators]
    jitter = rng.uniform(-0.15, 0.15, len(gen_rhos))
    ax.scatter(gen_rhos, [y + j for j in jitter],
               color="#666666", s=8, alpha=0.5, zorder=3, edgecolors="none")

yticks = list(range(n))
ylabels = [FEAT_LABELS[FEATURES[n - 1 - i][0]] for i in range(n)]
ax.set_yticks(yticks)
ax.set_yticklabels(ylabels, fontsize=8.5)

ax.set_xlabel(r"Spearman $\rho$")
ax.xaxis.grid(True, color="#eeeeee", linewidth=0.5, zorder=0)
ax.set_ylim(-0.5, n - 0.5)

legend_patches = [
    mpatches.Patch(color="#2ca02c", alpha=0.85, label="Drifting"),
    mpatches.Patch(color="#9467bd", alpha=0.85, label="Intermediate"),
    mpatches.Patch(color="#ff7f0e", alpha=0.85, label="Near-stationary"),
]
ax.legend(handles=legend_patches, loc="lower right", fontsize=7,
          frameon=True, framealpha=0.9, edgecolor="#cccccc", fancybox=False)

outdir = Path("/root/gen-depth-fingerprint/artifacts/_project/chart")
outdir.mkdir(parents=True, exist_ok=True)
fig.savefig(outdir / "fig1_differential_response.pdf",
            bbox_inches="tight", dpi=300, pad_inches=0.02)
fig.savefig(outdir / "fig1_differential_response.png",
            bbox_inches="tight", dpi=300, pad_inches=0.02)

for i, (feat, group) in enumerate(FEATURES):
    print(f"  y={n-1-i}: {feat:15s} rho={pooled[feat]:+.4f}  -> {group:18s} color={ZONE_COLORS[group]}")
print("Saved fig1_differential_response.pdf + .png")

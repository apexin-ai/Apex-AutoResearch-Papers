#!/usr/bin/env python3
"""b* distribution — 4-bin bar chart with mean/median markers."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pathlib

bins = ["[0, 0.5)", "[0.5, 1)", "[1, 2)", "[2, 20]"]
pcts = [20.9, 35.7, 27.3, 16.1]
colors = ["#d1e5f0", "#6baed6", "#2171b5", "#08306b"]

mean_val = 1.399
median_val = 0.871

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 9,
    "axes.labelsize": 10,
    "legend.fontsize": 8,
    "figure.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
})

fig, ax = plt.subplots(figsize=(3.5, 2.4))

x = np.arange(len(bins))
bars = ax.bar(x, pcts, color=colors, edgecolor="white", width=0.7, zorder=2)

for bar, pct in zip(bars, pcts):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.8,
            f"{pct:.1f}%", ha="center", va="bottom", fontsize=8, fontweight="bold")

median_x = 1 + (median_val - 0.5) / 0.5 * 0.7 - 0.35
mean_x = 2 + (mean_val - 1.0) / 1.0 * 0.7 - 0.35

def bin_to_x(val):
    if val < 0.5:
        return 0 + val / 0.5 * 0.7 - 0.35
    elif val < 1.0:
        return 1 + (val - 0.5) / 0.5 * 0.7 - 0.35
    elif val < 2.0:
        return 2 + (val - 1.0) / 1.0 * 0.7 - 0.35
    else:
        return 3 + (val - 2.0) / 18.0 * 0.7 - 0.35

med_x = bin_to_x(median_val)
mean_x = bin_to_x(mean_val)

ax.axvline(med_x, color="#e41a1c", linestyle="--", linewidth=1.2, zorder=3)
ax.axvline(mean_x, color="#ff7f00", linestyle="-.", linewidth=1.2, zorder=3)

ax.annotate(f"median={median_val:.2f}", xy=(med_x, 38), fontsize=7,
            color="#e41a1c", ha="left", va="top", rotation=0,
            xytext=(med_x + 0.15, 38))
ax.annotate(f"mean={mean_val:.2f}", xy=(mean_x, 35), fontsize=7,
            color="#ff7f00", ha="left", va="top", rotation=0,
            xytext=(mean_x + 0.15, 35))

ax.set_xticks(x)
ax.set_xticklabels(bins)
ax.set_xlabel("$b^*$ range")
ax.set_ylabel("Percentage of batches (%)")
ax.set_ylim(0, 42)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.tight_layout()

out = pathlib.Path(__file__).resolve().parent.parent.parent / "artifacts" / "figures"
out.mkdir(parents=True, exist_ok=True)
fig.savefig(out / "bstar_distribution.pdf")
fig.savefig(out / "bstar_distribution.png", dpi=300)
print(f"Saved to {out / 'bstar_distribution.pdf'} and .png")

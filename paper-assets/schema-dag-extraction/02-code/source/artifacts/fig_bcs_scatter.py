#!/usr/bin/env python3
"""BCS range compression across count levels for FewRel RE.

Single-column figure showing how BCS variance narrows at higher counts.
"""
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from collections import defaultdict

DATA = "artifacts/d051_fewrel_n25_s42/eval_results.json"

with open(DATA) as f:
    raw = json.load(f)

by_count = defaultdict(list)
for k, v in raw.items():
    by_count[v["num_types"]].append(v["bcs"])

counts = sorted(by_count.keys())
bcs_data = [by_count[c] for c in counts]

# Paul Tol Bright-derived sequential: Steel Blue → Burnt Orange gradient via count
COLORS = {
    4: "#4477AA", 8: "#5599BB", 16: "#66CCEE",
    32: "#CCBB44", 40: "#EE7733", 64: "#CC6677", 80: "#AA3377",
}

fig, ax = plt.subplots(figsize=(3.4, 2.4))

positions = list(range(len(counts)))
bp = ax.boxplot(
    bcs_data, positions=positions, widths=0.5,
    patch_artist=True, showfliers=False,
    medianprops=dict(color="white", lw=1.2),
    whiskerprops=dict(color="#888888", lw=0.8),
    capprops=dict(color="#888888", lw=0.8),
)
for i, (patch, count) in enumerate(zip(bp["boxes"], counts)):
    patch.set_facecolor(COLORS[count])
    patch.set_edgecolor("#2D2D2D")
    patch.set_linewidth(0.6)
    patch.set_alpha(0.75)
    jitter = np.random.default_rng(42).uniform(-0.15, 0.15, len(bcs_data[i]))
    ax.scatter(
        np.full(len(bcs_data[i]), positions[i]) + jitter,
        bcs_data[i],
        c=COLORS[count], s=6, alpha=0.45, edgecolors="none", zorder=3,
    )

ranges = [max(d) - min(d) for d in bcs_data]
for i, (pos, rng) in enumerate(zip(positions, ranges)):
    if counts[i] in [4, 16, 64]:
        ax.text(pos, max(bcs_data[i]) + 0.012, f"$\\Delta$={rng:.2f}",
                ha="center", va="bottom", fontsize=5.5, color="#555555")  # Text Mid

ax.set_xticks(positions)
ax.set_xticklabels([str(c) for c in counts], fontsize=7)
ax.set_xlabel("Number of schema types ($k$)", fontsize=8)
ax.set_ylabel("Batch Confusability Score", fontsize=8)
ax.tick_params(labelsize=7)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout(pad=0.4)
out = "figures/paper/fig_bcs_scatter.pdf"
plt.savefig(out, dpi=300, bbox_inches="tight")
print(f"Saved to {out}")
plt.close()

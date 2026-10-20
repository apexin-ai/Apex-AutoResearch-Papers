#!/usr/bin/env python3
"""Seed divergence bar chart — bimodal Goodhart effect under ISR beta=0.1."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "font.size": 9,
    "axes.labelsize": 9,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.6,
    "xtick.major.width": 0.5,
    "ytick.major.width": 0.5,
    "xtick.major.size": 3,
    "ytick.major.size": 3,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
})

C_GAMING = "#B8605A"
C_GENUINE = "#5A9E72"

seeds = ["s42", "s43", "s44", "s45", "s46"]
nh_pct = [17, 0, 0, 55, 55]
colors = [C_GAMING] * 3 + [C_GENUINE] * 2

fig, ax = plt.subplots(figsize=(3.25, 1.85))

ax.axvspan(-0.55, 2.5, color="#F5EDED", zorder=0)
ax.axvspan(2.5, 4.55, color="#EDF5F0", zorder=0)
ax.axvline(x=2.5, color="#DDDDDD", linewidth=0.5, zorder=0.5)

bars = ax.bar(range(5), nh_pct, color=colors,
              edgecolor="white", linewidth=0.6, width=0.62, zorder=3)

for i, (v, bar) in enumerate(zip(nh_pct, bars)):
    if v > 5:
        ax.text(bar.get_x() + bar.get_width() / 2, v + 1.5, f"{v}%",
                ha="center", va="bottom", fontsize=8, fontweight="bold",
                color=colors[i])
    else:
        ax.text(bar.get_x() + bar.get_width() / 2, 2.5, f"{v}%",
                ha="center", va="bottom", fontsize=7.5,
                color=colors[i], alpha=0.75)

ax.text(1, 68, "Gaming (3/5)", ha="center", fontsize=7.5,
        color=C_GAMING, fontweight="bold")
ax.text(3.5, 68, "Genuine (2/5)", ha="center", fontsize=7.5,
        color=C_GENUINE, fontweight="bold")

ax.yaxis.grid(True, alpha=0.1, linewidth=0.3, zorder=0)
ax.axhline(y=10, color="#AAAAAA", linestyle=":", linewidth=0.5, zorder=1)

ax.set_xticks(range(5))
ax.set_xticklabels(seeds)
ax.set_ylabel("Non-hacking (%)")
ax.set_ylim(0, 75)
ax.set_xlim(-0.55, 4.55)
ax.set_yticks([0, 20, 40, 60])
ax.tick_params(axis="both", length=3)

plt.tight_layout(pad=0.3)
base = "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/fig_seed_divergence"
fig.savefig(f"{base}.pdf", dpi=300, bbox_inches="tight", pad_inches=0.05)
fig.savefig(f"{base}.png", dpi=300, bbox_inches="tight", pad_inches=0.05)
plt.close()
print(f"Saved: {base}.pdf and .png")

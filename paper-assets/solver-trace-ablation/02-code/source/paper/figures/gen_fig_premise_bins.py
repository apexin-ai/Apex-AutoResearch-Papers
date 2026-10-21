#!/usr/bin/env python3
"""Grouped stacked bar chart: mode composition by premise-count bin (ISR vs Random)."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

plt.rcParams.update({
    "pdf.fonttype": 42, "ps.fonttype": 42,
    "font.family": "DejaVu Sans", "font.size": 8,
    "axes.labelsize": 8, "axes.titlesize": 9,
    "xtick.labelsize": 8, "ytick.labelsize": 8,
})

C_TS = "#D55E00"
C_CE = "#E69F00"
C_GEN = "#009E73"
C_OTHER = "#BBBBBB"

bins = ["≤3", "4–6", "≥7"]
x = np.arange(len(bins))
bar_w = 0.30
gap = bar_w / 2

isr_n = [8, 61, 12]
isr_ce = [50.0, 47.5, 75.0]
isr_ts = [12.5, 19.7, 0.0]
isr_gen = [12.5, 14.8, 25.0]
isr_other = [25.0, 18.0, 0.0]

rnd_n = [6, 58, 15]
rnd_ce = [50.0, 72.4, 86.7]
rnd_ts = [0.0, 0.0, 0.0]
rnd_gen = [50.0, 22.4, 13.3]
rnd_other = [0.0, 5.2, 0.0]

fig, ax = plt.subplots(figsize=(3.25, 2.5))
kw = dict(width=bar_w, edgecolor="white", linewidth=0.4, zorder=3)

def stack(pos, ce, ts, gen, other):
    b = np.zeros(len(pos))
    ax.bar(pos, ts, bottom=b, color=C_TS, **kw)
    b = np.array(ts, dtype=float)
    ax.bar(pos, ce, bottom=b, color=C_CE, **kw)
    b += np.array(ce)
    ax.bar(pos, gen, bottom=b, color=C_GEN, **kw)
    b += np.array(gen)
    ax.bar(pos, other, bottom=b, color=C_OTHER, **kw)

stack(x - gap, isr_ce, isr_ts, isr_gen, isr_other)
stack(x + gap, rnd_ce, rnd_ts, rnd_gen, rnd_other)

for i in range(len(bins)):
    ax.text(x[i] - gap, 104, f"$n$={isr_n[i]}", ha="center", va="bottom",
            fontsize=6, color="#555555")
    ax.text(x[i] + gap, 104, f"$n$={rnd_n[i]}", ha="center", va="bottom",
            fontsize=6, color="#555555")

ax.annotate("TS=19.7%", xy=(1 - gap, 10), xytext=(1 - gap + 0.38, 8),
            fontsize=7, fontweight="bold", color=C_TS, ha="left", va="center",
            arrowprops=dict(arrowstyle="->", color=C_TS, lw=0.8))

for i in range(len(bins)):
    ax.text(x[i] - gap, -6, "I", ha="center", va="top", fontsize=6.5,
            fontweight="bold", color="#444444")
    ax.text(x[i] + gap, -6, "R", ha="center", va="top", fontsize=6.5,
            fontweight="bold", color="#444444")

legend_elements = [
    Patch(facecolor=C_TS, edgecolor="white", label="TS"),
    Patch(facecolor=C_CE, edgecolor="white", label="CE"),
    Patch(facecolor=C_GEN, edgecolor="white", label="Genuine"),
    Patch(facecolor=C_OTHER, edgecolor="white", label="Other"),
]
ax.legend(handles=legend_elements, fontsize=7, loc="upper center",
          bbox_to_anchor=(0.5, -0.17), frameon=False, ncol=4,
          columnspacing=0.8, handletextpad=0.3, handlelength=1.2)

ax.set_xticks(x)
ax.set_xticklabels(bins)
ax.set_xlabel("Premise count  (I = ISR,  R = Random)")
ax.set_ylabel("Percentage (%)")
ax.set_ylim(-2, 118)
ax.set_yticks([0, 25, 50, 75, 100])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

base = "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/fig_premise_bins"
fig.savefig(f"{base}.pdf", dpi=300, bbox_inches="tight", pad_inches=0.05)
fig.savefig(f"{base}.png", dpi=300, bbox_inches="tight", pad_inches=0.05)
plt.close()
print(f"Saved: {base}.pdf and .png")

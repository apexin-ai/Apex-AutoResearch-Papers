#!/usr/bin/env python3
"""Hacking composition across reward conditions — horizontal stacked bars."""
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

C_TS = "#B8605A"
C_CE = "#D4ACA8"
C_PG = "#B0B8C0"
C_GEN = "#5A9E72"

conditions = [
    "ISR $\\beta$=0.3",
    "ISR $\\beta$=0.1",
    "Rand $\\beta$=0.3",
    "Rand $\\beta$=0.1",
    "Exec-only",
    "SFT",
]

raw = {
    "ce":      [73, 42, 149, 180, 81, 3],
    "tsa":     [99, 149, 11, 36, 0, 0],
    "tsb":     [0, 14, 0, 0, 0, 0],
    "pg":      [6, 12, 0, 21, 5, 0],
    "genuine": [21, 14, 3, 25, 7, 36],
}

totals = [sum(raw[k][i] for k in raw) for i in range(len(conditions))]

ts = [(raw["tsa"][i] + raw["tsb"][i]) / totals[i] * 100 for i in range(len(conditions))]
ce = [raw["ce"][i] / totals[i] * 100 for i in range(len(conditions))]
pg = [raw["pg"][i] / totals[i] * 100 for i in range(len(conditions))]
genuine = [raw["genuine"][i] / totals[i] * 100 for i in range(len(conditions))]

y = np.arange(len(conditions))
bar_h = 0.52

fig, ax = plt.subplots(figsize=(3.25, 2.6))
kw = dict(height=bar_h, edgecolor="white", linewidth=0.4, zorder=3)

left = np.zeros(len(conditions))
ax.barh(y, ts, left=left, color=C_TS, label="TS (tautological)", **kw)
left += ts
ax.barh(y, ce, left=left, color=C_CE, label="CE (shortcut)", **kw)
left += ce
ax.barh(y, pg, left=left, color=C_PG, label="PG (degenerate)", **kw)
left += pg
ax.barh(y, genuine, left=left, color=C_GEN, label="Genuine", **kw)
left += genuine

for i, g in enumerate(genuine):
    ax.text(left[i] + 1.0, y[i], f"{g:.0f}%", va="center", ha="left",
            fontsize=7.5, color=C_GEN, fontweight="bold")

for i in range(len(conditions)):
    if ts[i] >= 10:
        ax.text(ts[i] / 2, y[i], f"{ts[i]:.0f}%", ha="center", va="center",
                fontsize=6.5, color="white", fontweight="bold", zorder=4)

ax.axhline(y=1.5, color="#E0E0E0", linewidth=0.4, zorder=0)
ax.axhline(y=3.5, color="#E0E0E0", linewidth=0.4, zorder=0)

ax.set_yticks(y)
ax.set_yticklabels(conditions)
ax.set_xlabel("Percentage of proved samples (%)")
ax.set_xlim(0, 112)
ax.set_xticks([0, 20, 40, 60, 80, 100])

ax.legend(fontsize=7, loc="upper center", bbox_to_anchor=(0.5, -0.15),
          frameon=False, ncol=4, columnspacing=0.6,
          handletextpad=0.3, handlelength=1.0)

base = "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/fig3_hacking_composition"
fig.savefig(f"{base}.pdf", dpi=300, bbox_inches="tight", pad_inches=0.05)
fig.savefig(f"{base}.png", dpi=300, bbox_inches="tight", pad_inches=0.05)
plt.close()
print(f"Saved: {base}.pdf and .png")

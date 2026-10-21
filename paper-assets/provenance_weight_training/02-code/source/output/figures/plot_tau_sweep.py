#!/usr/bin/env python3
"""τ Sensitivity Sweep — dual Y-axis plot."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pathlib

tau = [0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
ppl = [17.688, 17.6805, 17.6793, 17.6527, 17.712, 17.723]
bstar_mean = [0.3923, 0.5899, 0.8943, 1.399, 2.36, 3.0775]

uniform_ppl = 17.694
best_idx = ppl.index(min(ppl))

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 9,
    "axes.labelsize": 10,
    "legend.fontsize": 8,
    "figure.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
})

fig, ax1 = plt.subplots(figsize=(3.5, 2.6))

ax1.axhspan(min(ppl) - 0.01, max(ppl) + 0.01, xmin=0, xmax=(0.8 - 0.45) / (1.0 - 0.45),
            alpha=0.08, color="green", zorder=0)
safe_left, safe_right = 0.5, 0.8
ax1.axvspan(safe_left, safe_right, alpha=0.10, color="green", zorder=0, label="Safe range")

ax1.axhline(y=uniform_ppl, color="grey", linestyle="--", linewidth=0.8, zorder=1)
ax1.annotate("Uniform baseline", xy=(0.95, uniform_ppl), fontsize=7, color="grey",
             ha="right", va="bottom", xycoords=("data", "data"))

ln1 = ax1.plot(tau, ppl, "o-", color="#2166ac", markersize=5, linewidth=1.5,
               label="Held-out PPL", zorder=3)
ax1.annotate(f"best τ={tau[best_idx]}",
             xy=(tau[best_idx], ppl[best_idx]),
             xytext=(tau[best_idx] + 0.06, ppl[best_idx] - 0.015),
             fontsize=7, color="#2166ac",
             arrowprops=dict(arrowstyle="->", color="#2166ac", lw=0.8),
             zorder=4)

ax1.set_xlabel("Threshold τ")
ax1.set_ylabel("Held-out PPL", color="#2166ac")
ax1.tick_params(axis="y", labelcolor="#2166ac")
ax1.set_xlim(0.45, 1.0)
ax1.set_xticks(tau)

ax2 = ax1.twinx()
ln2 = ax2.plot(tau, bstar_mean, "^-", color="#b2182b", markersize=5, linewidth=1.5,
               label="Mean $b^*$", zorder=3)
ax2.set_ylabel("Mean $b^*$", color="#b2182b")
ax2.tick_params(axis="y", labelcolor="#b2182b")

lns = ln1 + ln2
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc="upper left", framealpha=0.9, edgecolor="none", fontsize=7)

fig.tight_layout()

out = pathlib.Path(__file__).resolve().parent.parent.parent / "artifacts" / "figures"
out.mkdir(parents=True, exist_ok=True)
fig.savefig(out / "tau_sweep.pdf")
fig.savefig(out / "tau_sweep.png", dpi=300)
print(f"Saved to {out / 'tau_sweep.pdf'} and .png")

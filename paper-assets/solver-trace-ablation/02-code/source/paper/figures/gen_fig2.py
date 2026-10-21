#!/usr/bin/env python3
"""Generate Fig 2: ISR collapse trajectory — ISR reward causes tautological collapse."""

import json
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ── Okabe-Ito palette (colorblind-safe, consistent with other figures) ──
OI_BLUE = "#0072B2"
OI_RED  = "#D55E00"
OI_SKY  = "#56B4E9"

# ── Style ──
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.titlesize": 13, "axes.labelsize": 12,
    "xtick.labelsize": 10, "ytick.labelsize": 10,
    "legend.fontsize": 10, "figure.dpi": 300,
    "savefig.dpi": 300, "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
    "axes.spines.top": False, "axes.spines.right": False,
    "lines.linewidth": 1.8, "pdf.fonttype": 42, "ps.fonttype": 42,
})


def rolling_mean(arr, w=20):
    kernel = np.ones(w) / w
    padded = np.concatenate([np.full(w - 1, arr[0]), arr])
    return np.convolve(padded, kernel, mode="valid")


# ── Load data ──
data_path = os.path.join(os.path.dirname(__file__), "fig2_data.json")
with open(data_path) as f:
    data = json.load(f)

W = 20

exec_s44_steps = np.array(data["exec_s44"]["steps"])
exec_s44_smooth = rolling_mean(np.array(data["exec_s44"]["isr"]), W)

isr_s44_steps = np.array(data["isr_s44"]["steps"])
isr_s44_smooth = rolling_mean(np.array(data["isr_s44"]["isr"]), W)

isr_1k_steps = np.array(data["isr_s42_1000"]["steps"])
isr_1k_smooth = rolling_mean(np.array(data["isr_s42_1000"]["isr"]), W)

rand_s44_steps = np.array(data["random_s44"]["steps"])
rand_s44_smooth = rolling_mean(np.array(data["random_s44"]["isr"]), W)

# ── Plot ──
fig, ax = plt.subplots(figsize=(7, 4))

# ISR β=0.1: two seeds showing collapse
ax.plot(isr_s44_steps, isr_s44_smooth, color=OI_RED, linewidth=2.2,
        label=r"ISR $\beta\!=\!0.1$ (seed 44)", zorder=5)
ax.plot(isr_1k_steps, isr_1k_smooth, color=OI_RED, linewidth=1.2,
        alpha=0.5, linestyle="--",
        label=r"ISR $\beta\!=\!0.1$ (seed 42, 1k steps)", zorder=4)

# Exec-only
ax.plot(exec_s44_steps, exec_s44_smooth, color=OI_BLUE, linewidth=2.2,
        label="Exec-only (seed 44)", zorder=5)

# Random β=0.1
ax.plot(rand_s44_steps, rand_s44_smooth, color=OI_SKY, linewidth=2.2,
        label=r"Random $\beta\!=\!0.1$ (seed 44)", zorder=5)

# Annotation: ISR collapse
collapse_step = 280
collapse_isr = isr_s44_smooth[collapse_step - 1]
ax.annotate("ISR collapse\n(Goodhart effect)",
            xy=(collapse_step, collapse_isr),
            xytext=(100, 0.92),
            fontsize=9, color=OI_RED, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=OI_RED, lw=1.2),
            ha="center", va="center")

ax.set_xlabel("Training Step")
ax.set_ylabel("ISR (proved samples only, rolling $w$=20)")
ax.set_ylim(-0.02, 1.02)
ax.set_xlim(0, 1050)
ax.legend(loc="center right", framealpha=0.9, edgecolor="none")
ax.yaxis.grid(True, alpha=0.3, linewidth=0.5)

# ── Save ──
out_dir = os.path.dirname(__file__)
for ext in ("pdf", "png"):
    out = os.path.join(out_dir, f"fig2_isr_collapse.{ext}")
    fig.savefig(out, format=ext)
    print(f"Saved: {out}")
plt.close()

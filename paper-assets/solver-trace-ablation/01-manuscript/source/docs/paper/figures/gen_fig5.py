#!/usr/bin/env python3
"""Generate Fig 1: Training ISR curves across reward conditions."""

import json
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

C_BLUE = "#5889B0"
C_RED = "#B8605A"
C_BLUE_L = "#9CBDD8"
C_GRAY = "#B0B8C0"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "font.size": 9,
    "axes.labelsize": 9,
    "axes.titlesize": 10,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "legend.fontsize": 8,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.6,
    "xtick.major.width": 0.5,
    "ytick.major.width": 0.5,
    "xtick.major.size": 3,
    "ytick.major.size": 3,
    "lines.linewidth": 1.4,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
})


def rolling_mean(arr, w=20):
    kernel = np.ones(w) / w
    padded = np.concatenate([np.full(w - 1, arr[0]), arr])
    return np.convolve(padded, kernel, mode="valid")


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

fig, ax = plt.subplots(figsize=(3.25, 2.4))

ax.plot(isr_s44_steps, isr_s44_smooth, color=C_RED, linewidth=1.6,
        label=r"ISR $\beta\!=\!0.1$ (s44)", zorder=5)
ax.plot(isr_1k_steps, isr_1k_smooth, color=C_RED, linewidth=1.0,
        alpha=0.5, linestyle="--",
        label=r"ISR $\beta\!=\!0.1$ (s42, 1k)", zorder=4)

ax.plot(exec_s44_steps, exec_s44_smooth, color=C_BLUE, linewidth=1.6,
        label="Exec-only (s44)", zorder=5)

ax.plot(rand_s44_steps, rand_s44_smooth, color=C_BLUE_L, linewidth=1.6,
        label=r"Random $\beta\!=\!0.1$ (s44)", zorder=5)

collapse_step = 280
collapse_isr = isr_s44_smooth[collapse_step - 1]
ax.annotate("Goodhart\ngaming",
            xy=(collapse_step, collapse_isr),
            xytext=(180, 0.92),
            fontsize=8, color=C_RED, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=C_RED, lw=0.8,
                            connectionstyle="arc3,rad=-0.2"),
            ha="center", va="center")

ax.annotate("ISR collapse\n(exec-only near 0)",
            xy=(400, rand_s44_smooth[399]),
            xytext=(700, 0.35),
            fontsize=8, color=C_BLUE_L, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=C_BLUE_L, lw=0.8,
                            connectionstyle="arc3,rad=-0.15"),
            ha="center", va="center")

ax.set_xlabel("Training Step")
ax.set_ylabel("ISR (proved samples only, rolling $w$=20)")
ax.set_ylim(-0.02, 1.02)
ax.set_xlim(0, 1050)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18),
          frameon=False, fontsize=8, ncol=2, handlelength=1.4,
          columnspacing=0.8, handletextpad=0.4)
ax.yaxis.grid(True, alpha=0.12, linewidth=0.4)

out_dir = os.path.dirname(__file__)
for ext in ("pdf", "png"):
    out = os.path.join(out_dir, f"fig5_training_isr_curves.{ext}")
    fig.savefig(out, format=ext)
    print(f"Saved: {out}")
plt.close()

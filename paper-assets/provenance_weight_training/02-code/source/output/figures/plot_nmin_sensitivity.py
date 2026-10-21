#!/usr/bin/env python3
"""Plot n_min sensitivity analysis with error bars."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

# --- Data ---
nmin_values = np.array([1, 2, 3, 4])

# Mean PPL per n_min
ppl_means = np.array([
    17.789,    # n_min=1, single seed
    17.6508,   # n_min=2, 3 seeds
    17.6389,   # n_min=3, 3 seeds
    17.6947,   # n_min=4, single seed (degenerates to uniform)
])

# Std PPL (0 for single-seed points)
ppl_stds = np.array([
    0.0,       # n_min=1
    0.0068,    # n_min=2
    0.0069,    # n_min=3
    0.0,       # n_min=4
])

# Baselines
uniform_mean = 17.6938
multi_seed_mask = np.array([False, True, True, False])

# --- Plot ---
fig, ax = plt.subplots(figsize=(3.8, 2.8))

# Error bars for multi-seed points
ax.errorbar(
    nmin_values[multi_seed_mask],
    ppl_means[multi_seed_mask],
    yerr=ppl_stds[multi_seed_mask],
    fmt="o",
    color="#2563EB",
    ecolor="#2563EB",
    elinewidth=1.2,
    capsize=3.5,
    capthick=1.2,
    markersize=6,
    zorder=5,
    label="3 seeds",
)

# Single-seed points
ax.scatter(
    nmin_values[~multi_seed_mask],
    ppl_means[~multi_seed_mask],
    marker="D",
    color="#93C5FD",
    edgecolors="#2563EB",
    linewidths=1.0,
    s=45,
    zorder=5,
    label="Single seed",
)

# Connecting line (all points)
order = np.argsort(nmin_values)
ax.plot(
    nmin_values[order],
    ppl_means[order],
    color="#2563EB",
    linewidth=1.0,
    alpha=0.4,
    zorder=3,
)

# Uniform baseline
ax.axhline(
    uniform_mean,
    color="#9CA3AF",
    linestyle="--",
    linewidth=1.0,
    zorder=2,
)
ax.text(
    4.05, uniform_mean, "Uniform",
    va="center", ha="left",
    fontsize=8, color="#6B7280",
)

# Shaded band for effective range (n_min=2 and n_min=3)
ax.axvspan(1.8, 3.2, color="#DBEAFE", alpha=0.5, zorder=1)
ax.text(
    2.5, 17.613, r"Recommended: $n_{\min}=\lfloor B/2 \rfloor$",
    ha="center", fontsize=7, color="#1E40AF", style="italic",
)

# Axes
ax.set_xlabel(r"$n_{\min}$", fontsize=11)
ax.set_ylabel("Held-out PPL", fontsize=11)
ax.set_xticks(nmin_values)
ax.set_xlim(0.5, 4.5)
ax.set_ylim(17.60, 17.82)
ax.tick_params(labelsize=9)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.legend(fontsize=8, loc="upper right", frameon=False)

fig.tight_layout(pad=0.4)

# --- Save ---
out_dir = os.path.join(os.path.dirname(__file__), "../../artifacts/figures")
os.makedirs(out_dir, exist_ok=True)

fig.savefig(os.path.join(out_dir, "nmin_sensitivity.pdf"), bbox_inches="tight")
fig.savefig(os.path.join(out_dir, "nmin_sensitivity.png"), dpi=300, bbox_inches="tight")
print("Saved to artifacts/figures/nmin_sensitivity.{pdf,png}")

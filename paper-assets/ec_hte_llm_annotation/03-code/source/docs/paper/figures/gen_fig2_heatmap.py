#!/usr/bin/env python3
"""Generate Figure 3: Bias amplification heatmap — single-column, low-error subgroup only."""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'mathtext.fontset': 'stix',
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

DATA_PATH = Path(__file__).resolve().parent.parent.parent.parent / "artifacts" / "sign_reversal_corrected.csv"
OUT_DIR = Path(__file__).resolve().parent

df = pd.read_csv(DATA_PATH)

def make_ratio_grid(sub_df):
    sub_df = sub_df.copy()
    mask_small = np.abs(sub_df['bias_naive']) < 1e-6
    sub_df['ratio'] = np.where(
        mask_small, np.nan,
        np.abs(sub_df['bias_global']) / np.abs(sub_df['bias_naive']),
    )
    grid = sub_df.pivot_table(
        index='delta_cate', columns='delta_misclass', values='ratio', aggfunc='mean'
    )
    grid = grid.sort_index(ascending=True)
    grid = grid[sorted(grid.columns)]
    return grid

panel_b_df = df[(df['subgroup'] == 'B') & (df['z_value'] == 0)]
grid_b = make_ratio_grid(panel_b_df)

# Paper palette
TEAL   = '#1A6B6B'
ROSE   = '#C0392B'
NAVY   = '#2C3E50'
GRAY   = '#7F8C8D'
TEAL_LIGHT = '#76D7C4'
ROSE_LIGHT = '#F1948A'

norm = mcolors.TwoSlopeNorm(vcenter=1.0, vmin=0.0, vmax=5.0)
cmap = mcolors.LinearSegmentedColormap.from_list(
    'paper_diverging',
    [TEAL_LIGHT, '#A3E4D7', '#FFFFFF', '#FADBD8', ROSE_LIGHT],
    N=256,
)
cmap.set_bad(color='#D5D8DC')

# Single-column figure (~3.25 inches wide)
fig, ax = plt.subplots(1, 1, figsize=(3.3, 3.0))

x_vals = grid_b.columns.values
y_vals = grid_b.index.values

x_tick_step = max(1, len(x_vals) // 5)
y_tick_step = max(1, len(y_vals) // 5)
x_tick_idx = list(range(0, len(x_vals), x_tick_step))
y_tick_idx = list(range(0, len(y_vals), y_tick_step))

data = np.clip(grid_b.values, 0, 5)
im = ax.imshow(
    data, origin='lower', aspect='auto',
    cmap=cmap, norm=norm,
    extent=[
        x_vals[0] - (x_vals[1] - x_vals[0]) / 2,
        x_vals[-1] + (x_vals[1] - x_vals[0]) / 2,
        y_vals[0] - (y_vals[1] - y_vals[0]) / 2,
        y_vals[-1] + (y_vals[1] - y_vals[0]) / 2,
    ],
)

# Hatching for ratio > 1
dx = x_vals[1] - x_vals[0]
dy = y_vals[1] - y_vals[0]
for i, yv in enumerate(y_vals):
    for j, xv in enumerate(x_vals):
        val = grid_b.values[i, j]
        if not np.isnan(val) and val > 1.0:
            rect = Rectangle(
                (xv - dx / 2, yv - dy / 2), dx, dy,
                linewidth=0.3, edgecolor=GRAY, facecolor='none',
                hatch='////', zorder=2,
            )
            ax.add_patch(rect)

# Crossover line
ax.axvline(x=0.12, color=NAVY, linestyle='--', linewidth=1.2, alpha=0.8, zorder=3)
ax.text(
    0.125, y_vals[-1] * 0.93, 'ratio $= 1$',
    fontsize=7.5, va='top', ha='left', color=NAVY, fontstyle='italic', zorder=4,
    bbox=dict(boxstyle='round,pad=0.12', facecolor='white', alpha=0.75, edgecolor='none'),
)

# Region labels
ax.text(
    0.04, y_vals[-1] * 0.50, 'debiasing\nhelps',
    fontsize=9, fontweight='bold', color='white',
    ha='center', va='center', alpha=0.95,
    bbox=dict(boxstyle='round,pad=0.2', facecolor=TEAL, alpha=0.85, edgecolor='none'),
)
ax.text(
    0.21, y_vals[-1] * 0.50, 'debiasing\nhurts',
    fontsize=9, fontweight='bold', color='white',
    ha='center', va='center', alpha=0.95,
    bbox=dict(boxstyle='round,pad=0.2', facecolor=ROSE, alpha=0.85, edgecolor='none'),
)

ax.set_xlabel(r'$\Delta\pi$ (misclassification gap)', color=NAVY)
ax.set_ylabel(r'$\Delta\tau$ (CATE heterogeneity)', color=NAVY)
ax.set_xticks([x_vals[i] for i in x_tick_idx])
ax.set_xticklabels([f'{x_vals[i]:.2f}' for i in x_tick_idx])
ax.set_yticks([y_vals[i] for i in y_tick_idx])
ax.set_yticklabels([f'{y_vals[i]:.2f}' for i in y_tick_idx])

# Colorbar
cbar = fig.colorbar(im, ax=ax, shrink=0.85, pad=0.03)
cbar.set_label(r'Bias ratio ($|\mathrm{bias_{global}}|/|\mathrm{bias_{naive}}|$)', fontsize=8, color=NAVY)
cbar.set_ticks([0, 1, 2, 3, 4, 5])
cbar.set_ticklabels(['0', '1', '2', '3', '4', '5'])
cbar.ax.tick_params(labelsize=7)

fig.savefig(OUT_DIR / 'fig2_heatmap.png')
fig.savefig(OUT_DIR / 'fig2_heatmap.pdf')
plt.close(fig)
print(f"Saved to {OUT_DIR / 'fig2_heatmap.pdf'}")

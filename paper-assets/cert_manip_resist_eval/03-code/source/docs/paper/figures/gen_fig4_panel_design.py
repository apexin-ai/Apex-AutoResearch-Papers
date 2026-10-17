#!/usr/bin/env python3
"""Generate Figure 5: Panel selection strategies box plot (K=3)."""

import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent.parent.parent / \
    "artifacts/server_backup/results/plan001/fig4_panel_design_K3.json"
OUT_DIR = Path(__file__).resolve().parent

COLORS = {
    'min_eta': '#1E88E5',
    'random': '#78909C',
    'max_keff': '#F4511E',
}
BOX_ALPHA = 0.30
SCATTER_ALPHA = 0.7

with open(DATA_PATH) as f:
    data = json.load(f)

min_eta_vals = []
random_vals = []
max_keff_vals = []

for cond in data['conditions'].values():
    min_eta_vals.append(cond['min_eta_max_asr'])
    random_vals.append(cond['random_asr'])
    max_keff_vals.append(cond['max_keff_asr'])

all_data = [min_eta_vals, random_vals, max_keff_vals]
labels = [r'min($\eta_{\max}$)', 'Random', r'max($K_{\mathrm{eff}}$)']
colors = [COLORS['min_eta'], COLORS['random'], COLORS['max_keff']]

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 13,
    'axes.labelsize': 15,
    'xtick.labelsize': 14,
    'ytick.labelsize': 12,
})

fig, ax = plt.subplots(figsize=(6, 5))

positions = [1, 2, 3]
width = 0.55

bp = ax.boxplot(
    all_data,
    positions=positions,
    widths=width,
    patch_artist=True,
    showmeans=True,
    meanprops=dict(marker='D', markersize=7, markerfacecolor='none',
                   markeredgewidth=1.5),
    medianprops=dict(linewidth=2.5),
    whiskerprops=dict(linewidth=1.2, color='#333333'),
    capprops=dict(linewidth=1.2, color='#333333'),
    flierprops=dict(marker='none'),
    showfliers=False,
)

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(BOX_ALPHA)
    patch.set_edgecolor(color)
    patch.set_linewidth(1.5)

for median, color in zip(bp['medians'], colors):
    median.set_color(color)

for mean, color in zip(bp['means'], colors):
    mean.set_markeredgecolor(color)

np.random.seed(42)
for pos, vals, color in zip(positions, all_data, colors):
    jitter = np.random.uniform(-0.12, 0.12, size=len(vals))
    ax.scatter(
        [pos + j for j in jitter], vals,
        color=color, alpha=SCATTER_ALPHA,
        s=40, zorder=5, edgecolors='none',
    )

ax.set_xticks(positions)
ax.set_xticklabels(labels)
ax.set_ylabel(r'Panel ASR ($K = 3$)')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.0)
ax.spines['bottom'].set_linewidth(1.0)

ax.text(
    0.02, 0.97,
    r'min($\eta_{\max}$) optimal' + '\nin 12/12 conditions',
    transform=ax.transAxes,
    fontsize=11,
    verticalalignment='top',
    bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor='#90CAF9',
              alpha=0.9, linewidth=0.8),
)

fig.tight_layout()
fig.savefig(OUT_DIR / 'fig4_panel_design.pdf', dpi=300, bbox_inches='tight')
fig.savefig(OUT_DIR / 'fig4_panel_design.png', dpi=300, bbox_inches='tight')
print(f"Saved to {OUT_DIR / 'fig4_panel_design.pdf'}")
print(f"Saved to {OUT_DIR / 'fig4_panel_design.png'}")
plt.close()

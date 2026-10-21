#!/usr/bin/env python3
"""Figure 1: DDR Partition Bar Chart with per-generator jitter."""
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Nimbus Roman'],
    'font.size': 10,
    'axes.linewidth': 0.8,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'mathtext.fontset': 'cm',
})

with open('/root/gen-depth-fingerprint/results/8gen_per_gen_spearman.json') as f:
    data = json.load(f)

pooled = data['_median']
generators = data['_generators']

# Sorted by |ρ| descending: hapax_ratio top, tail_decay bottom
FEATURES = [
    ('hapax_ratio',  'Drifting'),
    ('ttr',          'Drifting'),
    ('entropy_mean', 'Drifting'),
    ('entropy_min',  'Near-stationary'),
    ('entropy_std',  'Intermediate'),
    ('entropy_max',  'Near-stationary'),
    ('tail_decay',   'Near-stationary'),
]

FEAT_LABELS = {
    'entropy_mean': r'$\bar{H}$ (Entropy Mean)',
    'entropy_std':  r'$\sigma_H$ (Entropy Std)',
    'entropy_min':  r'$H_{\min}$ (Entropy Min)',
    'entropy_max':  r'$H_{\max}$ (Entropy Max)',
    'ttr':          'TTR',
    'hapax_ratio':  'Hapax Ratio',
    'tail_decay':   'Tail Decay',
}

ZONE_COLORS = {
    'Drifting':       '#2ca02c',
    'Intermediate':   '#9467bd',
    'Near-stationary': '#ff7f0e',
}

n = len(FEATURES)
fig, ax = plt.subplots(figsize=(3.4, 3.5))
rng = np.random.default_rng(42)

for i, (feat, group) in enumerate(FEATURES):
    y = n - 1 - i
    rho = pooled[feat]
    ax.barh(y, rho, color=ZONE_COLORS[group], height=0.6, alpha=0.85, zorder=2)
    gen_rhos = [data[g][feat] for g in generators]
    jitter = rng.uniform(-0.15, 0.15, len(gen_rhos))
    ax.scatter(gen_rhos, [y + j for j in jitter],
               color='#666666', s=8, alpha=0.5, zorder=3, edgecolors='none')

# Y-axis labels
yticks = list(range(n))
ylabels = [FEAT_LABELS[FEATURES[n - 1 - i][0]] for i in range(n)]
ax.set_yticks(yticks)
ax.set_yticklabels(ylabels, fontsize=8.5)

# Partition dividers
ax.axhline(y=3.5, color='#cccccc', linestyle='--', linewidth=0.5)
ax.axhline(y=2.5, color='#cccccc', linestyle='--', linewidth=0.5)

# X-axis
ax.set_xlabel(r'Spearman $\rho$')
ax.xaxis.grid(True, color='#eeeeee', linewidth=0.5, zorder=0)

# Partition labels (x in axes coords, y in data coords)
trans = ax.get_yaxis_transform()
ax.text(1.02, 5, 'Drifting', fontsize=7, color='#888888',
        ha='left', va='center', transform=trans, clip_on=False)
ax.text(1.02, 3, 'Intermediate', fontsize=7, color='#888888',
        ha='left', va='center', transform=trans, clip_on=False)
ax.text(1.02, 1, 'Near-stat.', fontsize=7, color='#888888',
        ha='left', va='center', transform=trans, clip_on=False)

ax.set_ylim(-0.5, n - 0.5)

outdir = Path('/root/gen-depth-fingerprint/artifacts/_project/chart')
outdir.mkdir(parents=True, exist_ok=True)
fig.savefig(outdir / 'fig1_differential_response.pdf',
            bbox_inches='tight', dpi=300, pad_inches=0.02)
fig.savefig(outdir / 'fig1_differential_response.png',
            bbox_inches='tight', dpi=300, pad_inches=0.02)
print('Saved fig1_differential_response.pdf + .png')

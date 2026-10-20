"""Generate regime map and consensus heatmap figures."""
# Data source: cross_alpha_v6.json, last updated 2026-05-15
# Remote path: /root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v6.json
import json
import os
import warnings

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import ListedColormap, BoundaryNorm
import seaborn as sns

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.linewidth': 1.0,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

OUT = '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures'

JSON_PATHS = [
    '/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v6.json',
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 'results', 'analysis', 'cross_alpha_v6.json'),
]

DIRECTION_TO_LABEL = {
    'entropy->d1': 'Entropy → $d_1$',
    'entropy->d2': 'Entropy → $d_2$',
    'ECE->d1':     'ECE → $d_1$',
    'ECE->d2':     'ECE → $d_2$',
}

HARDCODED_DATA = {
    'Entropy → $d_1$': [0.128475, 0.066653, 0.185488, 0.05399,  0.047992],
    'Entropy → $d_2$': [0.178631, 0.171729, 0.185488, 0.047993, 0.05399],
    'ECE → $d_1$':     [0.974164, 0.408962, 0.075984, 0.04599,  0.024],
    'ECE → $d_2$':     [0.622047, 0.185488, 0.128475, 0.04599,  0.04599],
}


def load_pfdr_from_json():
    """Load p_fdr values from cross_alpha_v6.json granger_causality list."""
    for path in JSON_PATHS:
        if os.path.isfile(path):
            with open(path) as f:
                blob = json.load(f)
            gc_list = blob['granger_causality']
            alpha_points = sorted({e['alpha'] for e in gc_list})
            data = {}
            for entry in gc_list:
                label = DIRECTION_TO_LABEL.get(entry['direction'])
                if label is None:
                    continue
                data.setdefault(label, {})
                data[label][entry['alpha']] = entry['p_fdr']
            result = {}
            for label in DIRECTION_TO_LABEL.values():
                result[label] = [data[label][a] for a in alpha_points]
            return alpha_points, result
    return None, None


# ── Figure 1: Regime Map ──
# p_fdr values from cross_alpha_v6.json (BH-corrected, 40 tests)

alpha_points, data = load_pfdr_from_json()
if data is not None:
    alphas = alpha_points
else:
    warnings.warn("cross_alpha_v6.json not found; using hardcoded p_fdr values")
    alphas = [0.00, 0.25, 0.50, 0.75, 1.00]
    data = HARDCODED_DATA

colors = ['#0072B2', '#56B4E9', '#D55E00', '#E69F00']
markers = ['o', 's', '^', 'D']

fig, ax = plt.subplots(figsize=(6, 4))

ax.axvspan(0.65, 0.85, color='#E0E0E0', alpha=0.5, zorder=0)
ax.text(0.75, 0.15, 'detectability\nboundary', ha='center', va='bottom',
        fontsize=8, color='#666666', style='italic',
        transform=ax.get_xaxis_transform())

thresh = -np.log10(0.05)
ax.axhline(thresh, color='#888888', linestyle='--', linewidth=1.0, zorder=1)
ax.text(1.02, thresh, 'FDR = 0.05', va='center', ha='left', fontsize=8,
        color='#888888', transform=ax.get_yaxis_transform())

for i, (label, pvals) in enumerate(data.items()):
    pvals = np.array(pvals, dtype=float)
    neg_log = -np.log10(pvals)
    mask = ~np.isnan(neg_log)
    xs = np.array(alphas)[mask]
    ys = neg_log[mask]

    ax.plot(xs, ys, color=colors[i], marker=markers[i], markersize=7,
            linewidth=1.8, label=label, zorder=3, markeredgecolor='white',
            markeredgewidth=0.5)

    if label == 'Entropy → $d_1$':
        idx75 = alphas.index(0.75)
        y75 = -np.log10(pvals[idx75])
        ax.plot(0.75, y75, marker='o', markersize=9, markerfacecolor='none',
                markeredgecolor=colors[i], markeredgewidth=2.0, zorder=4)
        ax.annotate('$p$ = 0.054', xy=(0.75, y75), xytext=(-45, -18),
                    textcoords='offset points', fontsize=8, color=colors[i],
                    arrowprops=dict(arrowstyle='->', color=colors[i], lw=0.8))

    if label == 'Entropy → $d_2$':
        idx100 = alphas.index(1.0)
        y100 = -np.log10(pvals[idx100])
        ax.plot(1.0, y100, marker='s', markersize=9, markerfacecolor='none',
                markeredgecolor=colors[i], markeredgewidth=2.0, zorder=4)
        ax.annotate('$p$ = 0.054', xy=(1.0, y100), xytext=(8, -18),
                    textcoords='offset points', fontsize=8, color=colors[i],
                    arrowprops=dict(arrowstyle='->', color=colors[i], lw=0.8))

ax.set_xlabel('Contamination level (α)')
ax.set_ylabel('$-\\log_{10}(p_{\\mathrm{FDR}})$')
ax.set_xticks(alphas)
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.1, 2.0)
ax.legend(loc='upper left', frameon=True, framealpha=0.9, edgecolor='#CCCCCC')

fig.tight_layout()
fig.savefig(f'{OUT}/regime_map_fdr.pdf', dpi=300, bbox_inches='tight')
print(f'Saved {OUT}/regime_map_fdr.pdf')
plt.close(fig)

# ── Figure 2: Consensus Heatmap ──

methods = ['Naïve', 'Differenced', 'Threshold', 'Perm. Granger', 'TY']
alpha_labels = ['0.00', '0.25', '0.50', '0.75', '1.00']

# rows = α, cols = methods
matrix = np.array([
    [1.0,   0.375, 0.0,   0.0,   0.0  ],
    [1.0,   1.0,   1.0,   0.0,   0.375],
    [1.0,   1.0,   1.0,   0.0,   0.0  ],
    [1.0,   1.0,   1.0,   0.375, np.nan],
    [1.0,   1.0,   1.0,   0.75,  0.594],
])

fig, ax = plt.subplots(figsize=(6, 3.8))

# Mask for NA
mask = np.isnan(matrix)

# Plot heatmap
cmap = sns.color_palette('Blues', as_cmap=True)
sns.heatmap(matrix, ax=ax, mask=mask, cmap=cmap, vmin=0, vmax=1,
            annot=True, fmt='.2f', linewidths=1.5, linecolor='white',
            cbar_kws={'label': 'Significance rate', 'shrink': 0.8},
            xticklabels=methods, yticklabels=alpha_labels,
            annot_kws={'fontsize': 10})

# Fill NA cell with gray
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if np.isnan(matrix[i, j]):
            ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True,
                                        facecolor='#D9D9D9', edgecolor='white',
                                        linewidth=1.5))
            ax.text(j + 0.5, i + 0.5, 'NA', ha='center', va='center',
                    fontsize=10, color='#888888', style='italic')

ax.set_xlabel('Statistical method')
ax.set_ylabel('Contamination level (α)')
ax.set_title('')

fig.tight_layout()
fig.savefig(f'{OUT}/consensus_heatmap.pdf', dpi=300, bbox_inches='tight')
print(f'Saved {OUT}/consensus_heatmap.pdf')
plt.close(fig)

#!/usr/bin/env python3
"""Generate CKA heatmap bar chart (Figure 7 in paper)."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 4,
    'axes.labelsize': 4.5,
    'xtick.labelsize': 3.5,
    'ytick.labelsize': 3.5,
    'axes.titlesize': 4.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.linewidth': 0.5,
    'xtick.major.width': 0.4,
    'ytick.major.width': 0.4,
})

COLORS = {
    'cka_only': '#2C3E50',
    'standard': '#C0392B',
    'random': '#7F8C8D',
    'rasp': '#27AE60',
}

layers = np.arange(28)

cka_only_diag = np.array([0.992078, 0.970804, 0.975216, 0.404565, 0.625708, 0.623903, 0.598962, 0.533124, 0.443967, 0.379374, 0.391774, 0.580886, 0.592159, 0.624592, 0.650729, 0.693671, 0.624036, 0.607008, 0.636153, 0.541262, 0.500812, 0.504471, 0.503854, 0.536129, 0.593986, 0.664982, 0.866145, 0.706587])
standard_diag = np.array([0.991821, 0.97916, 0.975323, 0.992554, 0.956368, 0.934576, 0.929565, 0.923715, 0.924731, 0.908191, 0.911368, 0.8923, 0.889276, 0.884304, 0.880501, 0.885459, 0.879751, 0.878502, 0.886264, 0.873357, 0.879117, 0.865639, 0.852384, 0.849021, 0.8412, 0.876013, 0.92356, 0.845257])
random_diag   = np.array([0.995953, 0.983455, 0.989856, 0.994252, 0.991933, 0.985995, 0.985967, 0.983163, 0.979579, 0.971516, 0.972551, 0.961018, 0.952727, 0.950374, 0.94448, 0.943773, 0.93139, 0.922787, 0.928291, 0.913079, 0.880656, 0.840093, 0.80336, 0.766821, 0.768002, 0.815259, 0.909149, 0.785565])
rasp_diag     = np.array([0.991693, 0.975358, 0.974914, 0.993405, 0.960868, 0.934946, 0.933927, 0.922086, 0.921308, 0.90173, 0.905182, 0.865596, 0.851913, 0.850003, 0.847234, 0.852437, 0.845246, 0.843156, 0.850639, 0.842069, 0.864349, 0.849892, 0.825763, 0.804426, 0.798232, 0.84092, 0.896333, 0.757363])

methods_data = [
    ('CKA-only', cka_only_diag, COLORS['cka_only']),
    ('Standard', standard_diag, COLORS['standard']),
    ('Random',   random_diag,   COLORS['random']),
    ('RASP',     rasp_diag,     COLORS['rasp']),
]

fig, axes = plt.subplots(2, 2, figsize=(3.25, 2.8), sharey=True)
axes = axes.flatten()

for ax, (name, diag, color) in zip(axes, methods_data):
    ax.bar(layers, diag, color=color, alpha=0.8, edgecolor='white', linewidth=0.15)
    mean_val = diag.mean()
    ax.axhline(mean_val, color='black', linestyle='--', linewidth=0.4, alpha=0.5)
    ax.text(26, mean_val + 0.03, f'$\\mu$={mean_val:.2f}', fontsize=3.5,
            ha='right', va='bottom', color='black')
    ax.set_title(name, fontsize=4.5, fontweight='bold', pad=2)
    ax.set_xlim(-0.5, 27.5)
    ax.set_ylim(0, 1.05)
    ax.set_xticks([0, 7, 14, 21, 27])

axes[2].set_xlabel('Layer')
axes[3].set_xlabel('Layer')
axes[0].set_ylabel('CKA(Dense, Pruned)')
axes[2].set_ylabel('CKA(Dense, Pruned)')

plt.tight_layout(h_pad=0.8, w_pad=0.4)

outdir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(f'{outdir}/fig4_cka_heatmap.pdf')
fig.savefig(f'{outdir}/fig4_cka_heatmap.png')
plt.close()
print('Fig 4 CKA heatmap saved.')

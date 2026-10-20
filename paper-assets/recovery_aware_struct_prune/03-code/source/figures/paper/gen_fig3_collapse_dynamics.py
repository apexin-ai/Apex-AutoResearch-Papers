#!/usr/bin/env python3
"""Generate f0 and gradient norm panels (Figure 5b in combined training dynamics figure)."""

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
    'legend.fontsize': 3.5,
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

methods = {
    'CKA-only': {
        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'frac_zero': [0.175, 0.200, 0.200, 0.350, 0.150, 0.200, 0.125, 0.250, 0.300, 0.200],
        'grad_norm': [1.8906, 1.2500, 1.1016, 0.9844, 1.9766, 3.7500, 1.1641, 2.6719, 1.2188, 1.4141],
        'color': COLORS['cka_only'], 'ls': '-',
    },
    'Random': {
        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90],
        'frac_zero': [0.300, 0.325, 0.325, 0.350, 0.300, 0.350, 0.300, 0.350, 0.325],
        'grad_norm': [3.75, 8.62, 3.67, 4.20, 5.10, 3.80, 5.50, 4.00, 3.90],
        'color': COLORS['random'], 'ls': '--',
    },
    'Standard': {
        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'frac_zero': [0.500, 0.625, 0.500, 0.500, 0.575, 0.550, 0.575, 0.550, 0.550, 0.550],
        'grad_norm': [6.6250, 2.9531, 2.1250, 0.7969, 1.8594, 2.1875, 2.2969, 1.6953, 0.0173, 2.4062],
        'color': COLORS['standard'], 'ls': '-.',
    },
    'RASP': {
        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'frac_zero': [0.850, 0.850, 0.800, 0.850, 0.725, 0.750, 0.675, 0.775, 0.900, 0.850],
        'grad_norm': [0.01221, 0.01428, 2.438, 0.02124, 0.01819, 0.0141, 1.297, 0.5352, 0.006989, 0.8828],
        'color': COLORS['rasp'], 'ls': '-.',
    },
}

fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(4.0, 1.6))
plt.subplots_adjust(wspace=0.4)

common_kw = dict(marker='o', markersize=1.8, markerfacecolor='white', markeredgewidth=0.4, linewidth=0.7, zorder=3)

# --- Panel (a): f0 ---
ax_a.axhspan(0.5, 1.05, color='#C0392B', alpha=0.05, zorder=0)
ax_a.text(55, 0.97, 'Collapse zone ($f_0 > 0.5$)', fontsize=3.5,
          color='#C0392B', ha='center', va='top', style='italic', alpha=0.7)

for name, d in methods.items():
    ax_a.plot(d['steps'], d['frac_zero'], color=d['color'], linestyle=d['ls'],
              markeredgecolor=d['color'], label=name, **common_kw)

ax_a.set_ylabel('$f_0$ (zero-var batch frac.)')
ax_a.set_ylim(0, 1.05)
ax_a.set_xlim(0, 105)
ax_a.set_xlabel('Training Step')
ax_a.set_xticks(np.arange(0, 110, 20))
ax_a.legend(loc='center left', frameon=False)

# --- Panel (b): Gradient Norm ---
for name, d in methods.items():
    ax_b.plot(d['steps'], d['grad_norm'], color=d['color'], linestyle=d['ls'],
              markeredgecolor=d['color'], label=name, **common_kw)

ax_b.annotate('0.017', xy=(90, 0.0173), xytext=(70, 5.5),
              fontsize=3.5, color=COLORS['standard'],
              arrowprops=dict(arrowstyle='->', color=COLORS['standard'], lw=0.3), ha='center')

ax_b.set_ylabel('Gradient Norm')
ax_b.set_ylim(bottom=0)
ax_b.set_xlim(0, 105)
ax_b.set_xlabel('Training Step')
ax_b.set_xticks(np.arange(0, 110, 20))

plt.tight_layout(pad=0.3)

outdir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(f'{outdir}/fig3_collapse_dynamics.pdf')
fig.savefig(f'{outdir}/fig3_collapse_dynamics.png')
plt.close()
print('Fig 3 saved.')

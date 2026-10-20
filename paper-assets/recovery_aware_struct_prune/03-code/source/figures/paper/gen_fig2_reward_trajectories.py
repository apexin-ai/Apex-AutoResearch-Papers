#!/usr/bin/env python3
"""Generate reward trajectories (Figure 5a in combined training dynamics figure)."""

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

data = {
    'Unpruned': {
        'steps':  [30, 40, 50, 60, 70, 80, 90, 100],
        'reward': [0.4250, 0.5381, 0.5894, 0.6469, 0.6031, 0.6694, 0.5644, 0.6612],
        'color': '#555555', 'ls': '-', 'lw': 1.0,
    },
    'CKA-only (20%)': {
        'steps':  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'reward': [0.2531, 0.2181, 0.2500, 0.2344, 0.3544, 0.2994, 0.3075, 0.3419, 0.2419, 0.3444],
        'color': COLORS['cka_only'], 'ls': '-', 'lw': 1.0,
    },
    'Random (20%)': {
        'steps':  [10, 20, 30, 40, 50, 60, 70, 80, 90],
        'reward': [0.161, 0.142, 0.166, 0.145, 0.175, 0.184, 0.190, 0.142, 0.173],
        'color': COLORS['random'], 'ls': '--', 'lw': 1.0,
    },
    'Standard (20%)': {
        'steps':  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'reward': [0.0513, 0.0556, 0.0669, 0.0813, 0.0188, 0.0431, 0.0469, 0.0456, 0.0306, 0.0538],
        'color': COLORS['standard'], 'ls': '-.', 'lw': 1.0,
    },
    'RASP (20%)': {
        'steps':  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'reward': [0.01688, 0.02063, 0.02250, 0.02125, 0.06125, 0.05312, 0.05563, 0.030, 0.015, 0.010],
        'color': COLORS['rasp'], 'ls': '-.', 'lw': 1.0,
    },
}

fig, ax = plt.subplots(figsize=(2.5, 1.6))

for name, d in data.items():
    ax.plot(d['steps'], d['reward'], color=d['color'], linestyle=d['ls'],
            linewidth=d['lw'], marker='o', markersize=1.8,
            markerfacecolor='white', markeredgewidth=0.4,
            markeredgecolor=d['color'], label=name, zorder=3)

ax.set_xlabel('GRPO Training Step')
ax.set_ylabel('Mean Reward per Step')
ax.set_xlim(0, 105)
ax.set_ylim(0, 0.75)
ax.set_xticks(np.arange(0, 110, 20))

ax.annotate('peak 0.354',
            xy=(50, 0.3544), xytext=(28, 0.50),
            fontsize=3.5, color=COLORS['cka_only'],
            arrowprops=dict(arrowstyle='->', color=COLORS['cka_only'], lw=0.3),
            ha='center')

ax.legend(loc='upper left', frameon=False, ncol=1)

plt.tight_layout(pad=0.3)

outdir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(f'{outdir}/fig2_reward_trajectories.pdf')
fig.savefig(f'{outdir}/fig2_reward_trajectories.png')
plt.close()
print('Fig 2 saved.')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# All data verified from W&B or server logs (2026-05-18)
methods = {
    'Unpruned': {
        'color': '#0072B2', 'ls': '-', 'lw': 1.5,
        # W&B run hwucjf2n (steps 30-100 only; steps 10-20 not logged)
        'steps':     [30, 40, 50, 60, 70, 80, 90, 100],
        'reward':    [0.4250, 0.5381, 0.5894, 0.6469, 0.6031, 0.6694, 0.5644, 0.6612],
        'frac_zero': [0.150, 0.275, 0.250, 0.125, 0.250, 0.150, 0.200, 0.250],
    },
    'CKA-only (20%)': {
        'color': '#009E73', 'ls': '-', 'lw': 2.2,
        # W&B run li451oi4 (verified 2026-05-18)
        'steps':     [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'reward':    [0.2531, 0.2181, 0.2500, 0.2344, 0.3544, 0.2994, 0.3075, 0.3419, 0.2419, 0.3444],
        'frac_zero': [0.175, 0.200, 0.200, 0.350, 0.150, 0.200, 0.125, 0.250, 0.300, 0.200],
    },
    'Random (20%)': {
        'color': '#E69F00', 'ls': '--', 'lw': 1.8,
        # From log file (W&B crashed); steps 10-90 only (timeout at step 97)
        'steps':     [10, 20, 30, 40, 50, 60, 70, 80, 90],
        'reward':    [0.161, 0.142, 0.166, 0.145, 0.175, 0.184, 0.190, 0.142, 0.173],
        'frac_zero': [0.300, 0.325, 0.325, 0.350, 0.300, 0.350, 0.300, 0.350, 0.325],
    },
    'Standard (20%)': {
        'color': '#CC79A7', 'ls': '-', 'lw': 1.8,
        # W&B run tyv20u2k (verified 2026-05-18)
        'steps':     [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'reward':    [0.0513, 0.0556, 0.0669, 0.0813, 0.0188, 0.0431, 0.0469, 0.0456, 0.0306, 0.0538],
        'frac_zero': [0.500, 0.625, 0.500, 0.500, 0.575, 0.550, 0.575, 0.550, 0.550, 0.550],
    },
    'RASP (20%)': {
        'color': '#D55E00', 'ls': '-', 'lw': 1.8,
        # From westd-11672 log grpo_rasp_20_fair.log (verified 2026-05-18)
        'steps':     [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'reward':    [0.01688, 0.02063, 0.02250, 0.02125, 0.06125, 0.05312, 0.05563, 0.030, 0.015, 0.010],
        'frac_zero': [0.850, 0.850, 0.800, 0.850, 0.725, 0.750, 0.675, 0.775, 0.900, 0.850],
    },
}

fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(12, 4.5))
plt.subplots_adjust(wspace=0.3)

# --- Subplot (a): Mean Reward ---
for name, d in methods.items():
    ax_a.plot(d['steps'], d['reward'], color=d['color'], linestyle=d['ls'],
              linewidth=d['lw'], marker='o', markersize=4, label=name, zorder=3)

ax_a.set_xlabel('Training Step')
ax_a.set_ylabel('Mean Reward')
ax_a.set_xlim(0, 105)
ax_a.set_ylim(0, 0.75)
ax_a.set_xticks(np.arange(0, 110, 10))
ax_a.grid(True, axis='y', alpha=0.3, color='#cccccc', zorder=0)
ax_a.set_title('(a) Mean Reward', fontweight='bold', pad=8)

ax_a.annotate('peak 0.354 (s50)',
              xy=(50, 0.3544), xytext=(30, 0.42),
              fontsize=9, color='#009E73',
              arrowprops=dict(arrowstyle='->', color='#009E73', lw=1.2),
              ha='center')

ax_a.annotate('self-recovery',
              xy=(100, 0.3444), xytext=(85, 0.42),
              fontsize=8, color='#009E73', ha='center',
              arrowprops=dict(arrowstyle='->', color='#009E73', lw=1.0))

ax_a.legend(loc='upper left', frameon=False, ncol=1)

# --- Subplot (b): Fraction Zero-Std ---
for name, d in methods.items():
    ax_b.plot(d['steps'], d['frac_zero'], color=d['color'], linestyle=d['ls'],
              linewidth=d['lw'], marker='o', markersize=4, label=name, zorder=3)

ax_b.set_xlabel('Training Step')
ax_b.set_ylabel('Fraction Zero-Std')
ax_b.set_xlim(0, 105)
ax_b.set_ylim(0, 1.05)
ax_b.set_xticks(np.arange(0, 110, 10))
ax_b.grid(True, axis='y', alpha=0.3, color='#cccccc', zorder=0)
ax_b.set_title('(b) Fraction Zero-Std', fontweight='bold', pad=8)

ax_b.axhline(y=0.85, color='grey', linestyle='--', linewidth=1.0, alpha=0.6, zorder=1)
ax_b.text(103, 0.85, 'Collapse', fontsize=8, color='grey', ha='right', va='bottom')

ax_b.annotate('0.125 (s70)',
              xy=(70, 0.125), xytext=(52, 0.04),
              fontsize=9, color='#009E73',
              arrowprops=dict(arrowstyle='->', color='#009E73', lw=1.2),
              ha='center')

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune'
fig.savefig(f'{outdir}/artifacts/figures/fig2_reward_trajectories.pdf')
fig.savefig(f'{outdir}/artifacts/figures/fig2_reward_trajectories.png')
fig.savefig(f'{outdir}/paper/figures/paper/fig2_reward_trajectories.pdf')
fig.savefig(f'{outdir}/paper/figures/paper/fig2_reward_trajectories.png')
plt.close()

import os
for loc in ['artifacts/figures', 'paper/figures/paper']:
    path = f'{outdir}/{loc}/fig2_reward_trajectories.pdf'
    if os.path.exists(path):
        print(f'{path}: {os.path.getsize(path)} bytes')
print('Done')

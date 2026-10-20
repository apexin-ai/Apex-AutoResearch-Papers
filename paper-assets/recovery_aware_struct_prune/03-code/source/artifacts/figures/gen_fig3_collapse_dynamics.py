import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 12,
    'axes.titleweight': 'bold',
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
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
    'CKA-only': {
        # W&B run li451oi4
        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'frac_zero_std': [0.175, 0.200, 0.200, 0.350, 0.150, 0.200, 0.125, 0.250, 0.300, 0.200],
        'grad_norm': [1.8906, 1.2500, 1.1016, 0.9844, 1.9766, 3.7500, 1.1641, 2.6719, 1.2188, 1.4141],
        'reward': [0.2531, 0.2181, 0.2500, 0.2344, 0.3544, 0.2994, 0.3075, 0.3419, 0.2419, 0.3444],
        'kl': [0.001206, 0.001232, 0.001671, 0.001500, 0.001567, 0.001579, 0.001558, 0.001701, 0.001508, 0.001609],
        'color': '#009E73', 'ls': '-',
    },
    'Random': {
        # From log file (W&B crashed); steps 10-90 only
        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90],
        'frac_zero_std': [0.300, 0.325, 0.325, 0.350, 0.300, 0.350, 0.300, 0.350, 0.325],
        'grad_norm': [3.75, 8.62, 3.67, 4.20, 5.10, 3.80, 5.50, 4.00, 3.90],
        'reward': [0.161, 0.142, 0.166, 0.145, 0.175, 0.184, 0.190, 0.142, 0.173],
        'kl': [0.0042, 0.0047, 0.0046, 0.0044, 0.0045, 0.0043, 0.0046, 0.0045, 0.0044],
        'color': '#E69F00', 'ls': '--',
    },
    'Standard': {
        # W&B run tyv20u2k
        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'frac_zero_std': [0.500, 0.625, 0.500, 0.500, 0.575, 0.550, 0.575, 0.550, 0.550, 0.550],
        'grad_norm': [6.6250, 2.9531, 2.1250, 0.7969, 1.8594, 2.1875, 2.2969, 1.6953, 0.0173, 2.4062],
        'reward': [0.0513, 0.0556, 0.0669, 0.0813, 0.0188, 0.0431, 0.0469, 0.0456, 0.0306, 0.0538],
        'kl': [0.002187, 0.002394, 0.002652, 0.002662, 0.002266, 0.002454, 0.002444, 0.002470, 0.002462, 0.003229],
        'color': '#CC79A7', 'ls': '-',
    },
    'RASP': {
        # From westd-11672 log grpo_rasp_20_fair.log
        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'frac_zero_std': [0.850, 0.850, 0.800, 0.850, 0.725, 0.750, 0.675, 0.775, 0.900, 0.850],
        'grad_norm': [0.01221, 0.01428, 2.438, 0.02124, 0.01819, 0.0141, 1.297, 0.5352, 0.006989, 0.8828],
        'reward': [0.01688, 0.02063, 0.02250, 0.02125, 0.06125, 0.05312, 0.05563, 0.030, 0.015, 0.010],
        'kl': [0.0008379, 0.0009728, 0.001022, 0.0007673, 0.001035, 0.000894, 0.001119, 0.0008899, 0.001043, 0.0008991],
        'color': '#D55E00', 'ls': '-',
    },
}

fig, axes = plt.subplots(2, 2, figsize=(10, 7.5))
ax_a, ax_b = axes[0]
ax_c, ax_d = axes[1]

common_kw = dict(marker='o', markersize=4, linewidth=1.8, zorder=3)

# (a) Fraction Zero-Std
for name, d in methods.items():
    ax_a.plot(d['steps'], d['frac_zero_std'], color=d['color'], linestyle=d['ls'],
              label=name, **common_kw)
ax_a.axhline(0.85, color='grey', linestyle='--', linewidth=1.0, alpha=0.7, zorder=1)
ax_a.text(103, 0.85, 'Collapse', fontsize=8, color='grey', va='center', ha='right')
ax_a.annotate('0.125 (s70)', xy=(70, 0.125), xytext=(55, 0.04),
              fontsize=8, color='#009E73',
              arrowprops=dict(arrowstyle='->', color='#009E73', lw=1.0), ha='center')
ax_a.set_ylabel('Fraction')
ax_a.set_ylim(0, 1.05)
ax_a.set_xlim(0, 105)
ax_a.set_title('(a) Fraction Zero-Std', pad=8)
ax_a.grid(True, axis='y', alpha=0.3, color='#cccccc', zorder=0)
ax_a.legend(loc='upper left', frameon=False)

# (b) Gradient Norm
for name, d in methods.items():
    ax_b.plot(d['steps'], d['grad_norm'], color=d['color'], linestyle=d['ls'],
              label=name, **common_kw)
ax_b.annotate('0.017 (s90)', xy=(90, 0.017), xytext=(75, 3.0),
              fontsize=8, color='#CC79A7',
              arrowprops=dict(arrowstyle='->', color='#CC79A7', lw=1.0), ha='center')
ax_b.set_ylabel('Gradient Norm')
ax_b.set_ylim(bottom=0)
ax_b.set_xlim(0, 105)
ax_b.set_title('(b) Gradient Norm', pad=8)
ax_b.grid(True, axis='y', alpha=0.3, color='#cccccc', zorder=0)

# (c) Mean Reward
for name, d in methods.items():
    ax_c.plot(d['steps'], d['reward'], color=d['color'], linestyle=d['ls'],
              label=name, **common_kw)
ax_c.annotate('peak 0.354', xy=(50, 0.354), xytext=(35, 0.40),
              fontsize=8, color='#009E73',
              arrowprops=dict(arrowstyle='->', color='#009E73', lw=1.0), ha='center')
ax_c.set_ylabel('Mean Reward')
ax_c.set_ylim(0, 0.40)
ax_c.set_xlim(0, 105)
ax_c.set_title('(c) Mean Reward', pad=8)
ax_c.grid(True, axis='y', alpha=0.3, color='#cccccc', zorder=0)

# (d) KL Divergence
for name, d in methods.items():
    ax_d.plot(d['steps'], d['kl'], color=d['color'], linestyle=d['ls'],
              label=name, **common_kw)
ax_d.set_ylabel('KL Divergence')
ax_d.set_xlim(0, 105)
ax_d.set_title('(d) KL Divergence', pad=8)
ax_d.grid(True, axis='y', alpha=0.3, color='#cccccc', zorder=0)

for ax in [ax_a, ax_b, ax_c, ax_d]:
    ax.set_xlabel('Training Step')
    ax.set_xticks(np.arange(0, 110, 20))

plt.tight_layout()

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune'
fig.savefig(f'{outdir}/artifacts/figures/fig3_collapse_dynamics.pdf')
fig.savefig(f'{outdir}/artifacts/figures/fig3_collapse_dynamics.png')
fig.savefig(f'{outdir}/paper/figures/paper/fig3_collapse_dynamics.pdf')
fig.savefig(f'{outdir}/paper/figures/paper/fig3_collapse_dynamics.png')
plt.close()

import os
for loc in ['artifacts/figures', 'paper/figures/paper']:
    path = f'{outdir}/{loc}/fig3_collapse_dynamics.pdf'
    if os.path.exists(path):
        print(f'{path}: {os.path.getsize(path)} bytes')
print('Done')

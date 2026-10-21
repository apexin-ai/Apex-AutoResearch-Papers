#!/usr/bin/env python3
"""Factorial 2x2 interaction plot — v3 with corrected LN data and publication styling."""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

data = {
    'BN': {
        'OFF': {'mean': 0.767, 'std': 0.024, 'n': 4},
        'ON':  {'mean': 0.725, 'std': 0.064, 'n': 3},
    },
    'LN': {
        'OFF': {'mean': 0.802, 'std': 0.024, 'n': 3},
        'ON':  {'mean': 0.773, 'std': 0.027, 'n': 4},
    },
}
VANILLA_CAR = 0.745

C_BN      = '#C44E52'
C_LN      = '#E69F00'
C_VANILLA = '#4C72B0'

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Liberation Serif', 'Times New Roman'],
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12.5,
    'xtick.labelsize': 11,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
    'axes.grid': False,
    'axes.linewidth': 0.8,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

x_positions = [0, 1]
x_labels = ['OFF (Detach)', 'ON (Full)']

fig, ax = plt.subplots(figsize=(4.5, 3.5))

ax.axhspan(0.68, VANILLA_CAR, color=C_BN, alpha=0.035, zorder=0)

ax.axhline(y=VANILLA_CAR, color=C_VANILLA, linestyle=':', linewidth=1.0,
           alpha=0.5, zorder=1)
t_van = ax.text(0.97, VANILLA_CAR + 0.003, 'Vanilla (0.745)', fontsize=8.5,
                color=C_VANILLA, va='bottom', ha='right',
                transform=ax.get_yaxis_transform())
t_van.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

bn_y = [data['BN']['OFF']['mean'], data['BN']['ON']['mean']]
bn_err = [data['BN'][gf]['std'] for gf in ['OFF', 'ON']]

ax.errorbar(x_positions, bn_y, yerr=bn_err, color=C_BN,
            marker='o', markersize=8, markeredgecolor='white', markeredgewidth=1.0,
            linestyle='-', linewidth=1.8, capsize=4, capthick=1.0,
            elinewidth=1.0, label='BatchNorm (BN)', zorder=3)

ln_y = [data['LN']['OFF']['mean'], data['LN']['ON']['mean']]
ln_err = [data['LN'][gf]['std'] for gf in ['OFF', 'ON']]

ax.errorbar(x_positions, ln_y, yerr=ln_err, color=C_LN,
            marker='s', markersize=8, markeredgecolor='white', markeredgewidth=1.0,
            linestyle=(0, (4, 2.5)), linewidth=1.8, capsize=4, capthick=1.0,
            elinewidth=1.0, label='LayerNorm (LN)', zorder=3)

delta_bn = (data['BN']['ON']['mean'] - data['BN']['OFF']['mean']) * 100
delta_ln = (data['LN']['ON']['mean'] - data['LN']['OFF']['mean']) * 100

mid_bn_y = np.mean(bn_y)
t_bn = ax.annotate(f'−{abs(delta_bn):.1f} pp', xy=(0.55, mid_bn_y - 0.008),
                   fontsize=9, fontweight='bold', color=C_BN, ha='center', va='top',
                   zorder=5)
t_bn.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

mid_ln_y = np.mean(ln_y)
t_ln = ax.annotate(f'−{abs(delta_ln):.1f} pp', xy=(0.45, mid_ln_y + 0.008),
                   fontsize=9, fontweight='bold', color=C_LN, ha='center', va='bottom',
                   zorder=5)
t_ln.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

ax.set_xticks(x_positions)
ax.set_xticklabels(x_labels)
ax.set_xlabel('Gradient Flow')
ax.set_ylabel('Collision Avoidance Rate (CAR)')
ax.set_xlim(-0.25, 1.25)
ax.set_ylim(0.68, 0.86)
ax.yaxis.set_major_locator(plt.MultipleLocator(0.02))

ax.legend(loc='upper right', frameon=False, handlelength=2.5, handletextpad=0.6)

n_offsets = {
    ('BN', 'OFF'): (-16, -12),
    ('BN', 'ON'):  (16, -16),
    ('LN', 'OFF'): (-16, 10),
    ('LN', 'ON'):  (16, 12),
}
for gf_idx, gf in enumerate(['OFF', 'ON']):
    for norm in ['BN', 'LN']:
        n_val = data[norm][gf]['n']
        y_val = data[norm][gf]['mean']
        ox, oy = n_offsets[(norm, gf)]
        c = C_BN if norm == 'BN' else C_LN
        ax.annotate(f'n={n_val}', (x_positions[gf_idx], y_val),
                    xytext=(ox, oy), textcoords='offset points',
                    fontsize=7, color=c, ha='center', fontstyle='italic',
                    alpha=0.65)

plt.tight_layout()

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures'
os.makedirs(out_dir, exist_ok=True)

for fmt in ['pdf', 'png']:
    path = os.path.join(out_dir, f'factorial_2x2_pb.{fmt}')
    fig.savefig(path)
    print(f'Saved: {path}')

plt.close(fig)

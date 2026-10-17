# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
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
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.8,
})

C_OBJ = '#009E73'
C_SPA = '#0072B2'
CLIFF_COLOR = '#FFE0E0'

obj_rand_k =  [0.3,  0.5,  0.7,  0.85, 0.9,  0.925, 0.95, 1.0]
obj_rand_sr = [36.4, 69.4, 77.2, 5.0,  12.0, 27.6,  69.4, 98.2]

obj_l2_k =  [0.3,  0.5,  0.7,  0.85, 0.9,  0.95, 1.0]
obj_l2_sr = [51.0, 33.4, 55.0, 98.0, 98.2, 98.2, 98.2]

spa_rand_k =  [0.3,  0.5,  0.7,  0.85, 0.9,  0.925, 0.95, 1.0]
spa_rand_sr = [49.6, 71.6, 74.4, 58.4, 54.6, 60.4,  76.4, 97.2]

spa_l2_k =  [0.3,  0.5,  0.7,  0.85, 0.9,  0.95, 1.0]
spa_l2_sr = [57.2, 55.6, 67.0, 90.4, 95.0, 97.8, 97.2]

fig, ax = plt.subplots(1, 1, figsize=(6, 4))

ax.axvspan(0.82, 0.96, alpha=0.15, color='#D55E00', zorder=0,
           label='_nolegend_')
ax.text(0.89, 102, 'cliff zone', fontsize=8, ha='center', va='bottom',
        color='#D55E00', fontstyle='italic', alpha=0.7)

ax.plot(obj_rand_k, obj_rand_sr, '-o', color=C_OBJ, markersize=6,
        label='Object Random', zorder=5)
ax.plot(obj_l2_k, obj_l2_sr, '--^', color=C_OBJ, markersize=6,
        label='Object L2 Norm', zorder=5)
ax.plot(spa_rand_k, spa_rand_sr, '-s', color=C_SPA, markersize=5,
        label='Spatial Random', zorder=5)
ax.plot(spa_l2_k, spa_l2_sr, '--D', color=C_SPA, markersize=5,
        label='Spatial L2 Norm', zorder=5)

ax.annotate('5.0%', xy=(0.85, 5.0), xytext=(0.75, 15),
            fontsize=8, color=C_OBJ, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=C_OBJ, lw=0.8))

t = ax.text(0.60, 8, '72 pp\nrecovery', fontsize=8, color=C_OBJ,
            ha='center', va='center', fontstyle='italic', fontweight='bold',
            alpha=0.7)
t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

ax.annotate('', xy=(0.70, 77.2), xytext=(0.70, 5.0),
            arrowprops=dict(arrowstyle='<->', color=C_OBJ, lw=0.8,
                            linestyle='--'))

ax.set_xlabel('Token Retention Ratio ($k$)')
ax.set_ylabel('Task Success Rate (%)')
ax.set_xlim(0.22, 1.04)
ax.set_ylim(-3, 108)
ax.legend(loc='lower left', fontsize=9, framealpha=0.9, ncol=2)
ax.grid(True, alpha=0.15, zorder=0)

import os
outdir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(outdir, 'fig_crosssuite.pdf'))
fig.savefig(os.path.join(outdir, 'fig_crosssuite.png'))
print('Saved fig_crosssuite.pdf and fig_crosssuite.png')

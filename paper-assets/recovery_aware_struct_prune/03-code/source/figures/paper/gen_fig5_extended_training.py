#!/usr/bin/env python3
"""Generate extended 300-step training figure (Figure 8 in paper)."""

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
}

standard_steps = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
                  150, 200, 250, 300]
standard_reward = [0.0513, 0.0556, 0.0669, 0.0813, 0.0188, 0.0431,
                   0.0469, 0.0456, 0.0306, 0.0538,
                   0.055, 0.054, 0.058, 0.0562]
standard_f0 = [0.500, 0.625, 0.500, 0.500, 0.575, 0.550,
               0.575, 0.550, 0.550, 0.550,
               0.530, 0.540, 0.520, 0.525]

cka_steps = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
             110, 120, 130, 260, 270, 280, 290, 300]
cka_reward = [0.2531, 0.2181, 0.2500, 0.2344, 0.3544, 0.2994,
              0.3075, 0.3419, 0.2419, 0.3444,
              0.3206, 0.2562, 0.2963, 0.3900, 0.3188, 0.4444, 0.2238, 0.3075]
cka_f0 = [0.175, 0.200, 0.200, 0.350, 0.150, 0.200, 0.125, 0.250, 0.300, 0.200,
           0.175, 0.225, 0.200, 0.125, 0.225, 0.100, 0.250, 0.275]

fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(3.25, 2.6))
plt.subplots_adjust(hspace=0.55)

common_kw = dict(marker='o', markersize=1.8, markerfacecolor='white', markeredgewidth=0.4, linewidth=0.7, zorder=3)

# --- Panel (a): Reward ---
ax_a.plot(standard_steps, standard_reward, color=COLORS['standard'],
          markeredgecolor=COLORS['standard'], linestyle='-.',
          label='Standard', **common_kw)
ax_a.plot(cka_steps, cka_reward, color=COLORS['cka_only'],
          markeredgecolor=COLORS['cka_only'], linestyle='-',
          label='CKA-only', **common_kw)

ax_a.axvline(100, color='#AAAAAA', linestyle=':', linewidth=0.4)

ax_a.annotate('zero net gain',
              xy=(300, 0.0562), xytext=(220, 0.14),
              fontsize=3.5, color=COLORS['standard'],
              arrowprops=dict(arrowstyle='->', color=COLORS['standard'], lw=0.3),
              ha='center')

ax_a.annotate(r'5.5$\times$ gap',
              xy=(280, 0.4444), xytext=(195, 0.52),
              fontsize=3.5, color=COLORS['cka_only'],
              arrowprops=dict(arrowstyle='->', color=COLORS['cka_only'], lw=0.3),
              ha='center')

ax_a.set_xlabel('Training Step')
ax_a.set_ylabel('Mean Reward')
ax_a.set_xlim(0, 315)
ax_a.set_ylim(0, 0.56)
ax_a.legend(loc='upper left', frameon=False)
ax_a.set_title('(a) Reward', fontsize=5.5, pad=2)

# --- Panel (b): f0 ---
ax_b.axhspan(0.5, 1.05, color=COLORS['standard'], alpha=0.05, zorder=0)
ax_b.text(155, 0.97, 'Collapse zone\n($f_0 > 0.5$)', fontsize=3.5,
          color=COLORS['standard'], ha='center', va='top', style='italic', alpha=0.7)

ax_b.plot(standard_steps, standard_f0, color=COLORS['standard'],
          markeredgecolor=COLORS['standard'], linestyle='-.',
          label='Standard', **common_kw)
ax_b.plot(cka_steps, cka_f0, color=COLORS['cka_only'],
          markeredgecolor=COLORS['cka_only'], linestyle='-',
          label='CKA-only', **common_kw)

ax_b.axvline(100, color='#AAAAAA', linestyle=':', linewidth=0.4)

ax_b.set_xlabel('Training Step')
ax_b.set_ylabel('$f_0$ (zero-var batch frac.)')
ax_b.set_xlim(0, 310)
ax_b.set_ylim(0, 1.05)
ax_b.legend(loc='lower left', frameon=False)
ax_b.set_title('(b) $f_0$ diagnostic', fontsize=5.5, pad=2)

plt.tight_layout(pad=0.3)

outdir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(f'{outdir}/fig5_extended_training.pdf')
fig.savefig(f'{outdir}/fig5_extended_training.png')
plt.close()
print('Fig 5 extended training saved.')

"""
Magnitude sensitivity curve — Spatial only, half-column single panel.
Output: magnitude_curve.pdf
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

SHARED_HEIGHT = 2.5          # inches — must match fig_tau_sweep.py
SHARED_WIDTH  = 3.3          # inches — must match fig_tau_sweep.py

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 12,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'lines.linewidth': 2.0,
    'lines.markersize': 7,
    'figure.dpi': 300,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# === LIBERO-Spatial data (seed 42 only) ===
eps_spatial = np.array([0.05, 0.10, 0.30, 1.42])
obs_only_spatial = np.array([35, 35, 36, 35])
perdof_spatial = np.array([31, 35, 26, 0])

# === Single panel ===
fig, ax = plt.subplots(1, 1, figsize=(SHARED_WIDTH, SHARED_HEIGHT))

ax.axvspan(0.05, 0.2, alpha=0.06, color='#6FA8D2', zorder=0)

ax.plot(eps_spatial, obs_only_spatial, 'o-', color='#6FA8D2',
        markerfacecolor='#6FA8D2', markeredgecolor='white', markeredgewidth=0.5,
        label='obs_only', zorder=5)
ax.plot(eps_spatial, perdof_spatial, '^--', color='#D08888',
        markerfacecolor='#D08888', markeredgecolor='white', markeredgewidth=0.5,
        label='perdof', zorder=5)

ax.annotate('0%', xy=(1.42, 0), xytext=(0.8, 8),
            fontsize=9, color='#D08888', fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color='#D08888', lw=0.8))

ax.set_xscale('log')
ax.set_xticks(eps_spatial)
ax.xaxis.set_major_formatter(ScalarFormatter())
ax.xaxis.set_minor_formatter(plt.NullFormatter())
ax.set_xticklabels(['0.05', '0.1', '0.3', r'$\sim$1.42'])
ax.set_xlabel(r'$\varepsilon$')
ax.set_ylabel('SR (%)')
ax.set_ylim(-5, 44)
ax.set_xlim(0.04, 2.0)
ax.legend(loc='lower left', framealpha=0.9, edgecolor='none',
          borderpad=0.3, handlelength=1.5)
ax.yaxis.grid(True, linestyle='-', alpha=0.15, zorder=0)
ax.set_axisbelow(True)

plt.tight_layout()

out_dir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(out_dir, 'magnitude_curve.pdf'), format='pdf')
fig.savefig(os.path.join(out_dir, 'magnitude_curve.png'), format='png', dpi=300)
plt.close()

print("Saved: magnitude_curve.pdf, magnitude_curve.png")

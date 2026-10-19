"""
Magnitude Curve: obs_only vs perdof success rate across correction norms (ε).
Data: LIBERO object benchmark, seed42, 100 rollouts per condition.
Output: magnitude_curve.pdf, magnitude_curve.png
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Data: seed42, object benchmark, 100 rollouts each
eps_values = np.array([0.03, 0.05, 0.10, 0.20, 0.30, 1.42])
obs_only_sr = np.array([16, 13, 19, 22, 19, 17])
perdof_sr = np.array([14, 14, 11, 11, 4, 0])

# Baselines (both happen to be 12%)
argmin_baseline = 12
vla_only_baseline = 12

# Figure setup: single-column academic (3.5 inch width)
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'legend.fontsize': 6.5,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 7.5,
    'lines.linewidth': 1.5,
    'lines.markersize': 5,
    'figure.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
})

fig, ax = plt.subplots(figsize=(3.5, 2.4))

# Main curves
ax.plot(eps_values, obs_only_sr, 'o-', color='#2166ac', label='obs_only',
        markerfacecolor='#2166ac', markeredgecolor='white', markeredgewidth=0.5, zorder=5)
ax.plot(eps_values, perdof_sr, '^--', color='#b2182b', label='perdof',
        markerfacecolor='#b2182b', markeredgecolor='white', markeredgewidth=0.5, zorder=5)

# Baselines — both at 12%, use single line with combined label
ax.axhline(argmin_baseline, color='#777777', linestyle=':', linewidth=0.9,
           label='argmin / VLA-only (12%)', zorder=2)

# Mark optimal point ε=0.2
ax.axvline(0.2, color='#888888', linestyle='--', linewidth=0.5, alpha=0.4, zorder=1)
ax.plot(0.2, 22, '*', color='#2166ac', markersize=11, markeredgecolor='white',
        markeredgewidth=0.4, zorder=6)

# Annotations: gap between obs_only and perdof
# ε=0.2: obs_only=22, perdof=11 → +11pp
ax.annotate('+11pp', xy=(0.2, 17), xytext=(0.12, 27),
            fontsize=6, color='#2166ac', fontweight='bold',
            ha='center',
            arrowprops=dict(arrowstyle='->', color='#2166ac', lw=0.7,
                            connectionstyle='arc3,rad=-0.15'))

# ε=0.3: obs_only=19, perdof=4 → +15pp
ax.annotate('+15pp', xy=(0.3, 11.5), xytext=(0.48, 15),
            fontsize=6, color='#2166ac', fontweight='bold',
            ha='center',
            arrowprops=dict(arrowstyle='->', color='#2166ac', lw=0.7,
                            connectionstyle='arc3,rad=-0.15'))

# X-axis: log scale with custom ticks
ax.set_xscale('log')
ax.set_xticks(eps_values)
ax.xaxis.set_major_formatter(ScalarFormatter())
ax.xaxis.set_minor_formatter(plt.NullFormatter())
ax.set_xticklabels(['0.03', '0.05', '0.1', '0.2', '0.3', 'default\n(~1.42)'])

# Axis labels and limits
ax.set_xlabel(r'Correction Norm $\varepsilon$')
ax.set_ylabel('Success Rate (%)')
ax.set_ylim(-2, 30)
ax.set_xlim(0.025, 2.0)

# Legend — place in lower-left to avoid overlapping data
ax.legend(loc='lower left', framealpha=0.9, edgecolor='none',
          borderpad=0.3, handlelength=1.8)

# Grid
ax.yaxis.grid(True, linestyle='-', alpha=0.15, zorder=0)
ax.set_axisbelow(True)

# Spine cleanup
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

# Save
out_dir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(out_dir, 'magnitude_curve.pdf'), format='pdf')
fig.savefig(os.path.join(out_dir, 'magnitude_curve.png'), format='png', dpi=300)
plt.close()

print("Saved: magnitude_curve.pdf, magnitude_curve.png")

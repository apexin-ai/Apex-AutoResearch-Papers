"""
Magnitude sensitivity curve — LIBERO-Object (multi-seed), for appendix.
Output: magnitude_curve_object.pdf
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 10,
    'legend.fontsize': 8,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'lines.linewidth': 1.5,
    'lines.markersize': 5,
    'figure.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# === LIBERO-Object data ===
obs_only_object = {
    0.03: [16],
    0.05: [13, 15, 15, 14],
    0.10: [19, 16, 17, 16, 15, 14],
    0.20: [22, 16, 16, 16, 15, 20, 18],
    0.30: [19, 18, 14, 17, 16],
    1.42: [17, 16, 10],
}

perdof_object = {
    0.03: [14],
    0.05: [14, 9],
    0.10: [11, 11, 8, 13, 12, 11],
    0.20: [11, 9, 10, 12, 9, 11, 7],
    0.30: [4, 5, 5],
    1.42: [0, 0, 0],
}

vla_only_obj_seeds = [12, 12, 10, 11, 13]
argmin_obj_seeds = [12, 17, 13, 12, 10, 10]
vla_only_obj_mean = np.mean(vla_only_obj_seeds)
argmin_obj_mean = np.mean(argmin_obj_seeds)

eps_vals = sorted(obs_only_object.keys())
obs_means = [np.mean(obs_only_object[e]) for e in eps_vals]
obs_stds = [np.std(obs_only_object[e], ddof=1) if len(obs_only_object[e]) > 1 else 0 for e in eps_vals]
obs_ns = [len(obs_only_object[e]) for e in eps_vals]

per_eps = sorted(perdof_object.keys())
per_means = [np.mean(perdof_object[e]) for e in per_eps]
per_stds = [np.std(perdof_object[e], ddof=1) if len(perdof_object[e]) > 1 else 0 for e in per_eps]
per_ns = [len(perdof_object[e]) for e in per_eps]

eps_arr = np.array(eps_vals)
per_arr = np.array(per_eps)

fig, ax = plt.subplots(1, 1, figsize=(5.0, 2.5))

ax.axvspan(0.05, 0.2, alpha=0.06, color='#6FA8D2', zorder=0)

ax.plot(eps_arr, obs_means, '-', color='#6FA8D2', linewidth=1.5, zorder=4)
obs_multi_idx = [i for i, n in enumerate(obs_ns) if n > 1]
obs_single_idx = [i for i, n in enumerate(obs_ns) if n == 1]
if obs_multi_idx:
    ax.errorbar(eps_arr[obs_multi_idx], [obs_means[i] for i in obs_multi_idx],
                yerr=[obs_stds[i] for i in obs_multi_idx], fmt='o', color='#6FA8D2',
                markerfacecolor='#6FA8D2', markeredgecolor='white', markeredgewidth=0.5,
                capsize=3, capthick=0.8, elinewidth=0.8, label='obs\_only', zorder=5)
if obs_single_idx:
    ax.plot(eps_arr[obs_single_idx], [obs_means[i] for i in obs_single_idx], 'D',
            color='#6FA8D2', markerfacecolor='white', markeredgecolor='#6FA8D2',
            markeredgewidth=1.0, markersize=5, zorder=5)

ax.plot(per_arr, per_means, '--', color='#D08888', linewidth=1.5, zorder=4)
per_multi_idx = [i for i, n in enumerate(per_ns) if n > 1]
per_single_idx = [i for i, n in enumerate(per_ns) if n == 1]
if per_multi_idx:
    ax.errorbar(per_arr[per_multi_idx], [per_means[i] for i in per_multi_idx],
                yerr=[per_stds[i] for i in per_multi_idx], fmt='^', color='#D08888',
                markerfacecolor='#D08888', markeredgecolor='white', markeredgewidth=0.5,
                capsize=3, capthick=0.8, elinewidth=0.8, label='perdof', zorder=5)
if per_single_idx:
    ax.plot(per_arr[per_single_idx], [per_means[i] for i in per_single_idx], 'D',
            color='#D08888', markerfacecolor='white', markeredgecolor='#D08888',
            markeredgewidth=1.0, markersize=5, zorder=5)

ax.axhline(argmin_obj_mean, color='#555555', linestyle=':', linewidth=0.9,
           label=f'Argmin ({argmin_obj_mean:.1f}%)', zorder=2)
ax.axhline(vla_only_obj_mean, color='#999999', linestyle='-.', linewidth=0.7,
           label=f'VLA-only ({vla_only_obj_mean:.1f}%)', zorder=2)

ax.set_xscale('log')
ax.set_xticks(eps_arr)
ax.xaxis.set_major_formatter(ScalarFormatter())
ax.xaxis.set_minor_formatter(plt.NullFormatter())
ax.set_xticklabels(['0.03', '0.05', '0.1', '0.2', '0.3', r'$\sim$1.42'])
ax.set_xlabel(r'$\varepsilon$')
ax.set_ylabel('SR (%)')
ax.set_ylim(-2, 28)
ax.set_xlim(0.025, 2.0)
ax.set_title('LIBERO-Object', fontsize=10, pad=3)
ax.legend(loc='upper left', framealpha=0.9, edgecolor='none',
          borderpad=0.3, handlelength=1.5)
ax.yaxis.grid(True, linestyle='-', alpha=0.15, zorder=0)
ax.set_axisbelow(True)

plt.tight_layout()

out_dir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(out_dir, 'magnitude_curve_object.pdf'), format='pdf')
fig.savefig(os.path.join(out_dir, 'magnitude_curve_object.png'), format='png', dpi=300)
plt.close()

print("Saved: magnitude_curve_object.pdf, magnitude_curve_object.png")

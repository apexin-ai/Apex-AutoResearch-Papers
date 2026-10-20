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
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

# Okabe-Ito palette
C_ORANGE = '#E69F00'
C_BLUE   = '#0072B2'
C_GREEN  = '#009E73'

alpha_5 = np.array([0.00, 0.25, 0.50, 0.75, 1.00])
granger_fdr   = np.array([0.0, 0.0, 0.0, 0.75, 0.75])
consensus     = np.array([0.0, 0.0625, 0.0, 0.6875, 0.375])

alpha_naive = np.array([0.0, 0.25, 0.5, 1.0])
naive_vals  = np.array([1.0, 1.0, 1.0, 1.0])

fig, ax = plt.subplots(figsize=(5.5, 3.8))

# Phase-transition shading
ax.axvspan(0.50, 0.75, color='#DDDDDD', alpha=0.5, zorder=0)
ax.annotate('Phase\ntransition', xy=(0.625, 0.15), ha='center', va='center',
            fontsize=8.5, color='#555555', style='italic')

# Naive Pearson (4 alpha points, dashed)
ax.plot(alpha_naive, naive_vals, color=C_ORANGE, linestyle='--',
        marker='D', markersize=5, label='Naive Pearson sig. rate',
        zorder=3)

# Permutation Granger FDR-sig rate
ax.plot(alpha_5, granger_fdr, color=C_BLUE, linestyle='-',
        marker='o', markersize=6, label='Perm. Granger FDR-sig (forward)',
        zorder=3)

# Consensus robust pair rate
ax.plot(alpha_5, consensus, color=C_GREEN, linestyle='-',
        marker='s', markersize=5.5, label='Consensus robust pair rate',
        zorder=3)

ax.set_xlabel(r'Synthetic mixing ratio $\alpha$')
ax.set_ylabel('Significance / consensus rate')
ax.set_xticks(alpha_5)
ax.set_xticklabels(['0.00', '0.25', '0.50', '0.75', '1.00'])
ax.set_ylim(-0.05, 1.08)
ax.set_xlim(-0.05, 1.05)

ax.legend(loc='upper left', frameon=True, edgecolor='#CCCCCC',
          fancybox=False, framealpha=0.9)

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures'
fig.savefig(f'{out_dir}/regime_map.pdf')
fig.savefig(f'{out_dir}/regime_map.png')
plt.close(fig)
print('Saved regime_map.pdf and regime_map.png')

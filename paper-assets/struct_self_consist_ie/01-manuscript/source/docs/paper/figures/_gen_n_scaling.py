"""Generate fig_n_scaling_mv: MV delta-F1 vs log2(N)."""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.5,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'mathtext.fontset': 'dejavusans',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

COL_CONLL = '#43A047'
COL_SCIERC = '#E8930C'
COL_FEWNERD = '#3B7DD8'

n_vals_full = np.array([8, 16, 32, 64])
log2n_full = np.log2(n_vals_full)

scierc = np.array([-1.24, -0.61, +0.24, +0.53])
conll = np.array([+0.20, +0.32, +0.44, +0.61])

n_vals_fn = np.array([8, 16, 32])
log2n_fn = np.log2(n_vals_fn)
fewnerd = np.array([-2.71, -1.65, -0.91])

fig, ax = plt.subplots(figsize=(3.4, 2.6))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
for spine in ['bottom', 'left']:
    ax.spines[spine].set_color('#CCCCCC')
    ax.spines[spine].set_linewidth(0.8)
ax.tick_params(colors='#555555', which='both')
ax.grid(axis='y', alpha=0.15, linewidth=0.5, color='#888888')
ax.set_axisbelow(True)

# Break-even line
ax.axhline(y=0, color='#999999', linestyle='-', linewidth=0.5, zorder=1)

# Dataset lines
ax.plot(log2n_full, conll, '-', color=COL_CONLL, marker='s', markersize=6,
        markeredgecolor='white', markeredgewidth=0.5, zorder=3)
ax.plot(log2n_full, scierc, '-', color=COL_SCIERC, marker='^', markersize=6,
        markeredgecolor='white', markeredgewidth=0.5, zorder=3)
ax.plot(log2n_fn, fewnerd, '-', color=COL_FEWNERD, marker='o', markersize=6,
        markeredgecolor='white', markeredgewidth=0.5, zorder=3)

# Direct labels with rounded background boxes
label_box = dict(boxstyle='round,pad=0.15', facecolor='white',
                 edgecolor='#CCCCCC', linewidth=0.4, alpha=0.9)
ax.text(6.12, conll[-1] + 0.08, 'CoNLL', fontsize=7.5, color=COL_CONLL,
        va='bottom', ha='left', fontweight='medium', bbox=label_box)
ax.text(6.12, scierc[-1] - 0.08, 'SciERC', fontsize=7.5, color=COL_SCIERC,
        va='top', ha='left', fontweight='medium', bbox=label_box)
ax.text(5.12, fewnerd[-1] - 0.12, 'FewNERD', fontsize=7.5, color=COL_FEWNERD,
        va='top', ha='left', fontweight='medium', bbox=label_box)

ax.set_xlabel(r'$\log_2 N$')
ax.set_ylabel(r'MV $\Delta$F1 (pp)')
ax.set_xticks([3, 4, 5, 6])
ax.set_xticklabels(['8', '16', '32', '64'])
ax.set_xlim(2.8, 6.9)
ax.set_ylim(-3.2, 1.2)

out_dir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(out_dir, 'fig_n_scaling_mv.pdf'), format='pdf')
fig.savefig(os.path.join(out_dir, 'fig_n_scaling_mv.png'), format='png')
plt.close()
print('Done: fig_n_scaling_mv.pdf/png')

"""Figure 2: Coupling breadth K vs perplexity (30%, TEAL uniform, 3-seed mean +/- std)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from matplotlib.lines import Line2D

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.5,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'mathtext.fontset': 'cm',
})

COL_KL = '#4472C4'
COL_TEAL = '#E05A3A'

OUT = '/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/figures/paper'

# K-curve data: all 3-seed mean +/- std (Director-verified 2026-05-23)
K = [1, 2, 4, 8, 16, 32]
ppl_mean = [9.05, 10.75, 8.89, 9.00, 8.67, 8.81]
ppl_std  = [0.02, 0.15,  0.005, 0.06, 0.02, 0.02]
TEAL_PPL = 10.82

fig, ax = plt.subplots(figsize=(3.3, 2.1))
x = np.arange(len(K))

ax.axhline(y=TEAL_PPL, color=COL_TEAL, linestyle='--', linewidth=1.0,
           alpha=0.7, zorder=2)
t = ax.text(x[0] - 0.3, TEAL_PPL + 0.12, 'TEAL', color=COL_TEAL,
            fontsize=7, va='bottom', ha='left')
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

ax.plot(x, ppl_mean, '-', color=COL_KL, alpha=0.30, zorder=3, linewidth=1.0)

for i in range(len(K)):
    ax.errorbar(x[i], ppl_mean[i], yerr=ppl_std[i] if ppl_std[i] > 0.01 else None,
                fmt='o', color=COL_KL, markersize=5,
                capsize=2.5, capthick=0.8, elinewidth=0.8,
                markeredgecolor='white', markeredgewidth=0.6, zorder=5)

ax.annotate(f'{ppl_mean[1]:.2f}',
            xy=(x[1], ppl_mean[1]),
            xytext=(x[1] + 0.55, ppl_mean[1] + 0.15),
            fontsize=7, color='#444444',
            arrowprops=dict(arrowstyle='->', color='#888888', lw=0.7))

best_idx = int(np.argmin(ppl_mean))
ax.annotate(f'{ppl_mean[best_idx]:.2f}',
            xy=(x[best_idx], ppl_mean[best_idx]),
            xytext=(x[best_idx] + 0.55, ppl_mean[best_idx] - 0.35),
            fontsize=7, color='#444444',
            arrowprops=dict(arrowstyle='->', color='#888888', lw=0.7))

ax.set_xticks(x)
labels = [str(k) for k in K]
labels[-1] = '32\n(E2E)'
ax.set_xticklabels(labels)
ax.set_xlabel(r'Coupling breadth $K$')
ax.set_ylabel('Perplexity')

ax.set_ylim(8.2, 11.3)
ax.yaxis.grid(True, color='#E0E0E0', linewidth=0.4, zorder=0)
ax.set_axisbelow(True)

legend_elements = [
    Line2D([0], [0], marker='o', color=COL_KL,
           label=r'3-seed mean $\pm$ std',
           markersize=4.5, markeredgecolor='white',
           markeredgewidth=0.4, linestyle=''),
    Line2D([0], [0], color=COL_TEAL, linestyle='--',
           label='TEAL baseline', linewidth=1.0),
]
ax.legend(handles=legend_elements, loc='lower left', frameon=True,
          fancybox=False, edgecolor='#DDDDDD', fontsize=5.5,
          bbox_to_anchor=(0.02, 0.02), handletextpad=0.3,
          borderpad=0.3, labelspacing=0.3)

fig.tight_layout()
fig.savefig(f'{OUT}/k_curve_ppl.pdf')
fig.savefig(f'{OUT}/k_curve_ppl.png')
print('Saved k_curve_ppl.pdf/.png')
plt.close()

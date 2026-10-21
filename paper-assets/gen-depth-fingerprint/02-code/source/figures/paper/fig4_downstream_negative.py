import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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

strategies = [
    'All depths\n(no filter)',
    'Size-matched\nrandom',
    'Depth 0+1\nonly',
    'Binary\nfiltered',
    'Depth 0\nonly',
]
seeds_data = [
    [2.335, 2.335, 2.3354],
    [2.367, 2.367, 2.367],
    [2.3877, 2.3869, 2.387],
    [2.389, 2.389, 2.389],
    [2.6818, 2.68, 2.6817],
]
means = [np.mean(s) for s in seeds_data]
stds = [np.std(s, ddof=1) for s in seeds_data]
train_sizes = [12299, 3951, 3951, 3951, 797]

# Okabe-Ito
colors = [
    '#009E73',  # All depths (best)
    '#0072B2',  # Size-matched (control)
    '#E69F00',  # Depth 0+1
    '#D55E00',  # Binary filtered
    '#CC79A7',  # Depth 0 only (worst)
]

fig, ax = plt.subplots(figsize=(6, 4.5))
x = np.arange(len(strategies))

bars = ax.bar(x, means, yerr=stds, width=0.6, color=colors,
              edgecolor='black', linewidth=0.6, capsize=3,
              error_kw={'linewidth': 1.0, 'capthick': 1.0}, zorder=3)

for i, (xi, m, n) in enumerate(zip(x, means, train_sizes)):
    ax.text(xi, m + 0.008, f'n={n:,}', ha='center', va='bottom',
            fontsize=8, fontstyle='italic', color='#333333')

# Bracket: same data size (bars 1-3)
bracket_y = 2.405
ax.annotate('', xy=(0.75, bracket_y), xytext=(3.25, bracket_y),
            arrowprops=dict(arrowstyle='-', color='#555555', lw=1.0))
for bx in [0.75, 3.25]:
    ax.plot([bx, bx], [bracket_y - 0.004, bracket_y + 0.004],
            color='#555555', lw=1.0, zorder=4)
ax.text(2, bracket_y + 0.006, 'same data size (n=3,951)', ha='center',
        va='bottom', fontsize=8, color='#555555')

ax.axhline(y=means[1], color='#0072B2', linestyle='--', linewidth=0.7,
           alpha=0.4, zorder=1)

ax.text(4.4, 2.28, r'$\leftarrow$ lower is better', ha='right', va='bottom',
        fontsize=8, color='#888888', fontstyle='italic')

ax.set_xticks(x)
ax.set_xticklabels(strategies, fontsize=9)
ax.set_ylabel('Eval Perplexity')
ax.set_ylim(2.25, 2.75)
ax.set_xlim(-0.5, 4.5)
ax.yaxis.set_major_locator(plt.MultipleLocator(0.05))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.025))
ax.grid(axis='y', alpha=0.3, linewidth=0.5, zorder=0)

ax.set_title('Depth-Aware Curation Does Not Improve Downstream LM Quality',
             fontsize=11, pad=12)

fig.tight_layout()

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper'
fig.savefig(f'{outdir}/fig4_downstream_negative.pdf', bbox_inches='tight')
fig.savefig(f'{outdir}/fig4_downstream_negative.png', dpi=300, bbox_inches='tight')
print('Saved fig4_downstream_negative.pdf and .png')

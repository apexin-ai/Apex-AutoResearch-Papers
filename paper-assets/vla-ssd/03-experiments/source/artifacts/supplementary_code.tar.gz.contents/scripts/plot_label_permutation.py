#!/usr/bin/env python3
"""fig_label_permutation: Label permutation sanity check for appendix."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams.update({
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Data from controlb_analysis.md
conditions = ['Trained', 'Untrained']
real_rho   = [0.955, 0.933]
shuf_rho   = [0.0012, 0.0003]

x = np.arange(len(conditions))
width = 0.30

fig, ax = plt.subplots(figsize=(5, 4))

bars1 = ax.bar(x - width/2, real_rho, width, label='Real labels',
               color='#4393C3', edgecolor='#2166AC', linewidth=0.8, zorder=3)
bars2 = ax.bar(x + width/2, shuf_rho, width, label='Shuffled labels',
               color='#FDB863', edgecolor='#E08214', linewidth=0.8, zorder=3)

for bar, val in zip(bars1, real_rho):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
            f'{val:.3f}', ha='center', va='bottom', fontsize=9, fontweight='bold',
            color='#2166AC')

for bar, val in zip(bars2, shuf_rho):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
            f'{val:.4f}', ha='center', va='bottom', fontsize=9, fontweight='bold',
            color='#E08214')

ax.set_xticks(x)
ax.set_xticklabels(conditions)
ax.set_ylabel('Spearman $\\rho$ (action prediction)', fontsize=10)
ax.set_ylim(0, 1.15)
ax.legend(loc='upper right', framealpha=0.9, edgecolor='none')
ax.grid(axis='y', alpha=0.15, linewidth=0.5)

plt.tight_layout()

out_dirs = [
    '/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures',
    '/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper',
]
for d in out_dirs:
    os.makedirs(d, exist_ok=True)
    plt.savefig(os.path.join(d, 'fig_label_permutation.pdf'), dpi=300)
    plt.savefig(os.path.join(d, 'fig_label_permutation.png'), dpi=300)

plt.close()
print('Saved fig_label_permutation to both output directories.')

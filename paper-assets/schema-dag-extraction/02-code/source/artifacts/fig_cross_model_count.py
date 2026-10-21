#!/usr/bin/env python3
"""Cross-model count-curve replication on FewRel RE.

Shows monotonic accuracy decline across three model families,
supporting cross-model generalizability of Dimension 1.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 7.5,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

C_QWEN = '#4477AA'
C_LLAMA = '#EE7733'
C_GEMINI = '#228833'

counts_qwen = [4, 8, 16, 32, 64, 80]
acc_qwen = [0.870, 0.805, 0.719, 0.652, 0.539, 0.504]

counts_llama70 = [8, 16, 32, 64, 80]
acc_llama70 = [0.757, 0.685, 0.601, 0.504, 0.450]

counts_gemini = [4, 8, 16, 32, 64]
acc_gemini = [0.873, 0.820, 0.787, 0.739, 0.637]

fig, ax = plt.subplots(figsize=(3.4, 2.5))

ax.plot(counts_qwen, acc_qwen, 'o-', color=C_QWEN, ms=4, lw=1.3,
        label='Qwen3-32B', zorder=3)
ax.plot(counts_llama70, acc_llama70, 's--', color=C_LLAMA, ms=4, lw=1.3,
        label='Llama-3.1-70B', zorder=3)
ax.plot(counts_gemini, acc_gemini, '^:', color=C_GEMINI, ms=4, lw=1.3,
        label='Gemini 2.5 Flash', zorder=3, markeredgewidth=0.5)

ax.set_xlabel('Schema size (number of relations)')
ax.set_ylabel('Accuracy')
ax.set_ylim(0.38, 0.95)
ax.set_xticks([4, 8, 16, 32, 64, 80])
ax.set_xticklabels(['4', '8', '16', '32', '64', '80'])

ax.legend(loc='upper right', framealpha=0.95, edgecolor='none',
          handlelength=1.8, borderpad=0.4)

plt.tight_layout(pad=0.3)
outdir = os.environ.get('FIG_OUTDIR',
    '/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper')
os.makedirs(outdir, exist_ok=True)
outpath = os.path.join(outdir, 'fig_cross_model_count.pdf')
fig.savefig(outpath, format='pdf')
fig.savefig(outpath.replace('.pdf', '.png'), format='png', dpi=300)
print(f'Saved: {outpath}')
plt.close()

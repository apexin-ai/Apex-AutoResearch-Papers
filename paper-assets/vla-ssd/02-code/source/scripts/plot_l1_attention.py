#!/usr/bin/env python3
"""fig_l1_attention: Horizontal bar chart of L1 instruction-dominant head counts."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'custom',
    'mathtext.rm': 'Liberation Serif',
    'mathtext.it': 'Liberation Serif:italic',
    'mathtext.bf': 'Liberation Serif:bold',
})
import numpy as np
import os

REF_COLOR = '#92C5DE'
TRAINED_COLOR = '#2166AC'

architectures = ['OpenVLA', 'TraceVLA', 'NORA']
total_heads = [32, 32, 16]
ref_counts = [26, 32, 14]
trained_counts = [23, 29, 13]

ref_frac = [r / t * 100 for r, t in zip(ref_counts, total_heads)]
trained_frac = [tr / t * 100 for tr, t in zip(trained_counts, total_heads)]

fig, ax = plt.subplots(figsize=(3.8, 2.8))

y = np.arange(len(architectures))
bar_h = 0.32

bars_ref = ax.barh(y + bar_h/2, ref_frac, bar_h, color=REF_COLOR,
                    edgecolor='white', linewidth=0.5, label='Reference')
bars_tr = ax.barh(y - bar_h/2, trained_frac, bar_h, color=TRAINED_COLOR,
                   edgecolor='white', linewidth=0.5, label='Trained')

for i in range(len(architectures)):
    ax.text(ref_frac[i] + 1.5, y[i] + bar_h/2,
            f'{ref_counts[i]}/{total_heads[i]}',
            va='center', ha='left', fontsize=10, color='#333333')
    ax.text(trained_frac[i] + 1.5, y[i] - bar_h/2,
            f'{trained_counts[i]}/{total_heads[i]}',
            va='center', ha='left', fontsize=10, color='#333333')

ax.axvline(x=50, color='gray', linestyle='--', alpha=0.4, linewidth=1)

ax.set_yticks(y)
ax.set_yticklabels(architectures, fontsize=12, fontweight='bold')
ax.set_xlabel('Fraction of Instruction-Dominant Heads', fontsize=11)
ax.set_xlim(0, 115)
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xticklabels(['0%', '25%', '50%', '75%', '100%'], fontsize=10)
ax.tick_params(axis='y', length=0)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.invert_yaxis()
ax.legend(loc='upper left', fontsize=9, framealpha=0.9, edgecolor='#CCCCCC',
          borderpad=0.4, handlelength=1.2)

plt.tight_layout(pad=0.3)

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_dirs = [
    os.path.join(_REPO_ROOT, 'docs', 'paper', 'figures'),
    os.path.join(_REPO_ROOT, 'artifacts', 'figures', 'paper'),
]
for d in out_dirs:
    os.makedirs(d, exist_ok=True)
    fig.savefig(os.path.join(d, 'fig_l1_attention.pdf'), dpi=300, bbox_inches='tight')
    fig.savefig(os.path.join(d, 'fig_l1_attention.png'), dpi=300, bbox_inches='tight')

plt.close()
print('Saved fig_l1_attention.')

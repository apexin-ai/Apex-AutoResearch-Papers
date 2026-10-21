#!/usr/bin/env python3
"""Generate dose-response grouped bar chart for CKA coefficient α (Figure 1)."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 6,
    'axes.labelsize': 7,
    'xtick.labelsize': 6,
    'ytick.labelsize': 6,
    'legend.fontsize': 6,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.linewidth': 0.5,
    'xtick.major.width': 0.4,
    'ytick.major.width': 0.4,
})

alphas = [0.5, 1.0, 2.0, 3.0, 4.0]
sft_acc =  [60.73, 61.49, 64.97, 64.14, 61.94]
grpo_acc = [61.18, 60.88, 66.11, 63.46, 62.77]
deltas = [g - s for s, g in zip(sft_acc, grpo_acc)]

x = np.arange(len(alphas))
width = 0.32

fig, ax = plt.subplots(figsize=(3.25, 2.0))

bars_sft = ax.bar(x - width/2, sft_acc, width, color='#2C3E50', alpha=0.7,
                  edgecolor='#2C3E50', linewidth=0.5, label='SFT', zorder=3)
bars_grpo = ax.bar(x + width/2, grpo_acc, width, color='#C0392B', alpha=0.7,
                   edgecolor='#C0392B', linewidth=0.5, label='GRPO', zorder=3)

for i, (sx, gx, d) in enumerate(zip(sft_acc, grpo_acc, deltas)):
    top = max(sx, gx)
    sign = '+' if d >= 0 else ''
    ax.text(x[i], top + 0.4, f'{sign}{d:.2f}', ha='center', va='bottom',
            fontsize=5.5, color='#555555')

ax.set_xlabel(r'CKA coefficient $\alpha$')
ax.set_ylabel('GSM8K Accuracy (%)')
ax.set_xticks(x)
ax.set_xticklabels([str(a) for a in alphas])
ax.set_ylim(58, 69)
ax.legend(frameon=False, loc='upper right')

ax.axhline(y=64.39, color='#AAAAAA', linestyle=':', linewidth=0.5, zorder=1)
ax.text(4.3, 64.39, 'CKA-only', fontsize=5.5, color='#999999', va='center')

plt.tight_layout(pad=0.3)

out_dir = os.path.dirname(os.path.abspath(__file__))
doc_dir = os.path.join(os.path.dirname(os.path.dirname(out_dir)), 'docs', 'paper', 'figures', 'paper')
os.makedirs(doc_dir, exist_ok=True)

for d in [out_dir, doc_dir]:
    plt.savefig(os.path.join(d, 'fig1_dose_response.pdf'), format='pdf', bbox_inches='tight')
    plt.savefig(os.path.join(d, 'fig1_dose_response.png'), format='png', dpi=300, bbox_inches='tight')

print(f"Fig 1 dose-response saved.")
plt.close()

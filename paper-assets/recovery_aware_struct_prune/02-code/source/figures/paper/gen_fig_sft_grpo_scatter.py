#!/usr/bin/env python3
"""Generate SFT vs GRPO accuracy scatter plot (Figure 4 in paper)."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 10,
    'axes.labelsize': 11,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
})

COLORS = {
    'cka_only': '#2C3E50',
    'standard': '#C0392B',
    'random': '#7F8C8D',
    'rasp': '#27AE60',
}

data_20pct = {
    'CKA-only 20%':    {'sft': 63.91, 'grpo': 64.39, 'marker': 'o', 'color': COLORS['cka_only'], 'size': 80},
    'Standard 20%':    {'sft': 59.29, 'grpo': 59.84, 'marker': 's', 'color': COLORS['standard'], 'size': 80},
    r'RASP ($\alpha$=1) 20%': {'sft': 61.49, 'grpo': 60.88, 'marker': '^', 'color': COLORS['rasp'], 'size': 80},
    'Random 20%':      {'sft': 51.25, 'grpo': 50.72, 'marker': 'D', 'color': COLORS['random'], 'size': 80},
}

alpha_variants = {
    r'$\alpha$=0.5': {'sft': 60.73, 'grpo': 61.18},
    r'$\alpha$=2.0': {'sft': 64.97, 'grpo': 66.11},
    r'$\alpha$=3.0': {'sft': 64.14, 'grpo': 63.46},
    r'$\alpha$=4.0': {'sft': 61.94, 'grpo': 62.77},
}

cross_sparsity_cka = {
    'CKA 15%': {'sft': 72.18, 'grpo': 72.76},
    'CKA 25%': {'sft': 60.12, 'grpo': 59.59},
}

cross_sparsity_std = {
    'Std 15%': {'sft': 66.49, 'grpo': 65.56},
    'Std 25%': {'sft': 50.87, 'grpo': 51.86},
}

shortgpt = {'sft': 44.73, 'grpo': 43.37}
unpruned = {'sft': 81.27, 'grpo': 81.27}

fig, ax = plt.subplots(1, 1, figsize=(5.0, 5.0))

# y=x line and ±1pp band
lims = [40, 85]
ax.plot(lims, lims, color='#555555', linewidth=0.8, zorder=1)
ax.fill_between(lims, [l-1 for l in lims], [l+1 for l in lims],
                color='#EBF5FB', alpha=0.8, zorder=0)
ax.text(78, 76.5, r'$\pm 1\,$pp', fontsize=8, fontstyle='italic', color='#888888')

# 20% methods
for label, d in data_20pct.items():
    ax.scatter(d['sft'], d['grpo'], marker=d['marker'], c=d['color'],
               edgecolors=d['color'], s=d['size'], linewidths=1.0,
               label=label, zorder=5)

# α variants (RASP green pentagons)
first = True
for label, d in alpha_variants.items():
    ax.scatter(d['sft'], d['grpo'], marker='p', c=COLORS['rasp'],
               edgecolors=COLORS['rasp'], s=80, linewidths=1.0, alpha=0.6,
               label=r'$\alpha$ variants' if first else None, zorder=5)
    first = False

# 15%/25% CKA-only (open navy circles)
first = True
for label, d in cross_sparsity_cka.items():
    ax.scatter(d['sft'], d['grpo'], marker='o', facecolors='none',
               edgecolors=COLORS['cka_only'], s=110, linewidths=1.5,
               label='CKA 15%/25%' if first else None, zorder=5)
    first = False

# 15%/25% Standard (open red squares)
first = True
for label, d in cross_sparsity_std.items():
    ax.scatter(d['sft'], d['grpo'], marker='s', facecolors='none',
               edgecolors=COLORS['standard'], s=90, linewidths=1.5,
               label='Std 15%/25%' if first else None, zorder=5)
    first = False

# ShortGPT
ax.scatter(shortgpt['sft'], shortgpt['grpo'], marker='v', c='#8B4513',
           edgecolors='#8B4513', s=80, linewidths=1.0,
           label='ShortGPT', zorder=5)

# Unpruned
ax.scatter(unpruned['sft'], unpruned['grpo'], marker='*', c='black',
           edgecolors='black', s=180, linewidths=0.8,
           label='Unpruned', zorder=5)

ax.set_xlabel('SFT Accuracy (%)')
ax.set_ylabel('GRPO Accuracy (%)')
ax.set_xlim(40, 85)
ax.set_ylim(40, 85)
ax.set_aspect('equal')

ax.legend(loc='upper left', frameon=False, handletextpad=0.4, borderpad=0.3)

plt.tight_layout()

out_dir = os.path.dirname(os.path.abspath(__file__))
doc_dir = os.path.join(os.path.dirname(os.path.dirname(out_dir)), 'docs', 'paper', 'figures', 'paper')
os.makedirs(doc_dir, exist_ok=True)

for d in [out_dir, doc_dir]:
    plt.savefig(os.path.join(d, 'fig_sft_grpo_scatter.pdf'), format='pdf', bbox_inches='tight')
    plt.savefig(os.path.join(d, 'fig_sft_grpo_scatter.png'), format='png', dpi=300, bbox_inches='tight')

print(f"Saved to {out_dir}/ and {doc_dir}/")
plt.close()

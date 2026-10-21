#!/usr/bin/env python3
"""Fig1: Differential Depth Response — Spearman correlation bar chart."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import spearmanr

plt.rcParams.update({
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Nimbus Roman'],
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
    'mathtext.fontset': 'cm',
})

df = pd.read_csv('/root/gen-depth-fingerprint/data/features_all_models.csv')
print(f'Loaded {len(df)} rows')

features = ['hapax_ratio', 'ttr', 'entropy_mean', 'entropy_min', 'entropy_max', 'entropy_std', 'tail_decay']
labels = ['Hapax\nRatio', 'TTR', r'$\bar{H}$', r'$H_{\min}$', r'$H_{\max}$', r'$\sigma_H$', 'Tail\nDecay']

rhos = []
for f in features:
    rho, _ = spearmanr(df['depth'], df[f])
    rhos.append(rho)
    print(f'  {f}: rho={rho:.4f}')

rhos = np.array(rhos)

# Classification: drifting (|rho| > 0.15) vs stationary
drifting_idx = [i for i, f in enumerate(features) if f in ('hapax_ratio', 'ttr', 'entropy_mean')]
stationary_idx = [i for i, f in enumerate(features) if f in ('entropy_std', 'tail_decay')]
other_idx = [i for i, f in enumerate(features) if f in ('entropy_min', 'entropy_max')]

x = np.arange(len(features))

fig, ax = plt.subplots(figsize=(3.25, 2.2))

colors = []
hatches = []
for i in range(len(features)):
    if i in drifting_idx:
        colors.append('#2166AC')
        hatches.append('')
    elif i in stationary_idx:
        colors.append('#B2182B')
        hatches.append('///')
    else:
        colors.append('#666666')
        hatches.append('')

bars = ax.bar(x, rhos, width=0.65, color=colors, edgecolor='black', linewidth=0.5)
for bar, h in zip(bars, hatches):
    bar.set_hatch(h)

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel(r"Spearman $\rho$ with Depth")
ax.axhline(0, color='black', linewidth=0.4)

# Threshold lines for drifting/stationary
ax.axhline(-0.15, color='gray', linewidth=0.5, linestyle='--', alpha=0.5)
ax.axhline(0.15, color='gray', linewidth=0.5, linestyle='--', alpha=0.5)

# Value annotations
for i, (xi, rho) in enumerate(zip(x, rhos)):
    va = 'top' if rho < 0 else 'bottom'
    offset = -0.02 if rho < 0 else 0.02
    ax.text(xi, rho + offset, f'{rho:.3f}', ha='center', va=va, fontsize=5.5, fontweight='bold')

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#2166AC', edgecolor='black', linewidth=0.5, label='Drifting'),
    Patch(facecolor='#B2182B', edgecolor='black', linewidth=0.5, hatch='///', label='Near-stationary'),
    Patch(facecolor='#666666', edgecolor='black', linewidth=0.5, label='Other'),
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=6, frameon=True,
          fancybox=False, edgecolor='#cccccc', framealpha=0.9)

plt.tight_layout()

outdir = '/root/gen-depth-fingerprint/charts'
fig.savefig(f'{outdir}/fig1_differential_response.pdf', facecolor='white')
fig.savefig(f'{outdir}/fig1_differential_response.png', dpi=300, facecolor='white')
print(f'Saved fig1 to {outdir}/fig1_differential_response.{{pdf,png}}')

# Also save to figures/paper
fig.savefig('/root/gen-depth-fingerprint/figures/paper/fig1_differential_response.pdf', facecolor='white')
fig.savefig('/root/gen-depth-fingerprint/figures/paper/fig1_differential_response.png', dpi=300, facecolor='white')
print('Also saved to figures/paper/')

plt.close()

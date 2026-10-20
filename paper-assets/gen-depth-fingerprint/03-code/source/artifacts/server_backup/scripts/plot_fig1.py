#!/usr/bin/env python3
"""Figure 1: Differential Depth Response — 2x2 multi-panel line plot."""
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Nimbus Roman'],
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 6,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
    'mathtext.fontset': 'cm',
})

# Okabe-Ito palette
COLORS = {
    'pythia-1b':   '#E69F00',
    'pythia-2.8b': '#56B4E9',
    'olmo-2-1b':   '#009E73',
    'qwen3-0.6b':  '#0072B2',
    'qwen3-1.7b':  '#D55E00',
    'qwen3-8b':    '#CC79A7',
}

MARKERS = {
    'pythia-1b':   'o',
    'pythia-2.8b': 's',
    'olmo-2-1b':   '^',
    'qwen3-0.6b':  'D',
    'qwen3-1.7b':  'v',
    'qwen3-8b':    'P',
}

LABELS = {
    'pythia-1b':   'Pythia-1B',
    'pythia-2.8b': 'Pythia-2.8B',
    'olmo-2-1b':   'OLMo-2-1B',
    'qwen3-0.6b':  'Qwen3-0.6B',
    'qwen3-1.7b':  'Qwen3-1.7B',
    'qwen3-8b':    'Qwen3-8B',
}

MODEL_ORDER = ['pythia-1b', 'pythia-2.8b', 'olmo-2-1b', 'qwen3-0.6b', 'qwen3-1.7b', 'qwen3-8b']

def bootstrap_ci(values, n_boot=2000, ci=0.95, seed=42):
    rng = np.random.RandomState(seed)
    n = len(values)
    if n == 0:
        return np.nan, np.nan, np.nan
    boot_means = np.array([np.mean(rng.choice(values, n, replace=True)) for _ in range(n_boot)])
    alpha = (1 - ci) / 2
    return np.mean(values), np.percentile(boot_means, 100*alpha), np.percentile(boot_means, 100*(1-alpha))

df = pd.read_csv('/root/gen-depth-fingerprint/data/features_all_models.csv')

features = ['entropy_mean', 'hapax_ratio', 'entropy_std', 'tail_decay']
panel_titles = [r'(a) Token Entropy $\bar{H}$', '(b) Hapax Ratio', r'(c) Entropy Std $\sigma_H$', '(d) Tail Decay']
panel_ylabels = ['Mean Entropy (nats)', 'Hapax Ratio', 'Entropy Std', 'Tail Decay Slope']

fig, axes = plt.subplots(2, 2, figsize=(6.75, 3.375))
axes = axes.flatten()

for idx, (feat, title, ylabel) in enumerate(zip(features, panel_titles, panel_ylabels)):
    ax = axes[idx]
    for model in MODEL_ORDER:
        mdf = df[df['model_name'] == model]
        depths = sorted(mdf['depth'].unique())
        means, ci_lo, ci_hi = [], [], []
        for d in depths:
            vals = mdf[mdf['depth'] == d][feat].values
            m, lo, hi = bootstrap_ci(vals)
            means.append(m)
            ci_lo.append(lo)
            ci_hi.append(hi)

        ax.plot(depths, means, marker=MARKERS[model], color=COLORS[model],
                label=LABELS[model], markersize=3, linewidth=1.2, markeredgewidth=0.5)
        ax.fill_between(depths, ci_lo, ci_hi, color=COLORS[model], alpha=0.12)

    ax.set_title(title, fontweight='bold', pad=4)
    ax.set_xlabel('Generation Depth')
    ax.set_ylabel(ylabel)
    ax.set_xticks(depths)
    if idx in [0, 1]:
        ax.annotate('monotonic', xy=(0.97, 0.95), xycoords='axes fraction',
                     ha='right', va='top', fontsize=5.5, fontstyle='italic', color='#666666')
    else:
        ax.annotate('near-stationary', xy=(0.97, 0.95), xycoords='axes fraction',
                     ha='right', va='top', fontsize=5.5, fontstyle='italic', color='#666666')

handles, labels_list = axes[0].get_legend_handles_labels()
fig.legend(handles, labels_list, loc='lower center', ncol=6,
           bbox_to_anchor=(0.5, -0.04), frameon=False, columnspacing=1.0, handletextpad=0.4)

plt.tight_layout(rect=[0, 0.05, 1, 1], h_pad=0.8, w_pad=0.6)

outdir = Path('/root/gen-depth-fingerprint/figures/paper')
fig.savefig(outdir / 'fig1_differential_response.png', dpi=300, facecolor='white')
fig.savefig(outdir / 'fig1_differential_response.pdf', facecolor='white')
print(f'Saved fig1 to {outdir}/fig1_differential_response.{{png,pdf}}')

# Print key stats
for feat in features:
    print(f'\n{feat}:')
    for model in MODEL_ORDER:
        mdf = df[df['model_name'] == model]
        d0 = mdf[mdf['depth'] == 0][feat].mean()
        dmax = mdf[mdf['depth'] == mdf['depth'].max()][feat].mean()
        print(f'  {model}: depth0={d0:.4f} -> depthMax={dmax:.4f} (delta={dmax-d0:.4f})')

plt.close()

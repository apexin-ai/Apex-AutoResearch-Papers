import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Nimbus Roman'],
    'font.size': 10,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
    'mathtext.fontset': 'cm',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

GEN_COLORS = {
    'pythia-2.8b':     '#1f77b4',
    'pythia-1b':       '#6baed6',
    'olmo-2-1b':       '#2ca02c',
    'qwen3-0.6b':      '#ff7f0e',
    'qwen3-1.7b':      '#d62728',
    'qwen3-8b':        '#e377c2',
    'llama-3.2-3b':    '#bcbd22',
    'mistral-7b-v0.3': '#9467bd',
}

GEN_SHORT = {
    'pythia-2.8b':     'Py-2.8B',
    'pythia-1b':       'Py-1B',
    'olmo-2-1b':       'OLMo-1B',
    'qwen3-0.6b':      'Qw-0.6B',
    'qwen3-1.7b':      'Qw-1.7B',
    'qwen3-8b':        'Qw-8B',
    'llama-3.2-3b':    'Ll-3B',
    'mistral-7b-v0.3': 'Mi-7B',
}

PANELS = [
    ('entropy_mean', r'(a) Entropy Mean'),
    ('hapax_ratio',  '(b) Hapax Ratio'),
    ('entropy_max',  r'(c) Entropy Max'),
    ('tail_decay',   '(d) Tail Decay'),
]

LEGEND_ORDER = [
    'pythia-2.8b', 'pythia-1b', 'olmo-2-1b', 'qwen3-0.6b',
    'qwen3-1.7b', 'qwen3-8b', 'llama-3.2-3b', 'mistral-7b-v0.3',
]

df = pd.read_csv('/root/gen-depth-fingerprint/data/features_8gen.csv')
models = sorted(df['model_name'].unique())
depths = sorted(df['depth'].unique())

fig, axes = plt.subplots(2, 2, figsize=(7.0, 3.5))
axes_flat = axes.flatten()

rho_results = {}

for idx, (feat, title) in enumerate(PANELS):
    ax = axes_flat[idx]

    # per-generator thin lines with markers
    for model in models:
        mdf = df[df['model_name'] == model]
        means = [mdf[mdf['depth'] == d][feat].mean() for d in depths]
        ax.plot(depths, means, color=GEN_COLORS[model],
                linewidth=1.0, alpha=0.45, marker='o', markersize=3, zorder=2)

    # grand mean + 95% CI (min-max across 8 generator means)
    grand_means = []
    range_lo, range_hi = [], []
    for d in depths:
        gen_means = []
        for model in models:
            mdf = df[(df['model_name'] == model) & (df['depth'] == d)]
            gen_means.append(mdf[feat].mean())
        grand_means.append(np.mean(gen_means))
        range_lo.append(np.min(gen_means))
        range_hi.append(np.max(gen_means))

    ax.plot(depths, grand_means, color='black', linewidth=2.5, zorder=10)
    ax.fill_between(depths, range_lo, range_hi,
                    color='#cccccc', alpha=0.4, zorder=1)

    # pooled Spearman rho
    valid = df[['depth', feat]].dropna()
    rho, pval = spearmanr(valid['depth'], valid[feat])
    rho_results[feat] = (rho, pval)

    ax.text(0.95, 0.92, f'$\\rho$ = {rho:.3f}',
            transform=ax.transAxes, ha='right', va='top',
            fontsize=8.5, color='#555555')

    ax.set_title(title, fontsize=10, fontweight='bold', color='black', pad=4)
    ax.set_xticks(depths)

    # tail_decay: scale y-axis to ×10⁻³
    if feat == 'tail_decay':
        ax.yaxis.set_major_formatter(
            ticker.FuncFormatter(lambda x, p: f'{x*1000:.1f}'))
        ax.set_ylabel(r'$\times 10^{-3}$', fontsize=7, rotation=0,
                      labelpad=15, loc='top')

    # x-axis labels only on bottom row (idx 2, 3)
    if idx < 2:
        ax.set_xticklabels([])
    else:
        ax.set_xlabel('Generation Depth', fontsize=9)

plt.subplots_adjust(hspace=0.35, wspace=0.3)

# shared legend at bottom
handles = [plt.Line2D([0], [0], color=GEN_COLORS[m], lw=1.2,
                      marker='o', markersize=3, label=GEN_SHORT[m])
           for m in LEGEND_ORDER]
handles.append(plt.Line2D([0], [0], color='black', lw=2.5, label='Grand Mean'))

fig.legend(handles=handles, loc='lower center',
           bbox_to_anchor=(0.5, -0.06), ncol=9, fontsize=7.5,
           handlelength=1.5, columnspacing=0.8, frameon=False)

outdir = '/root/gen-depth-fingerprint/artifacts/_project/chart'
fig.savefig(f'{outdir}/fig_ddr_trajectory.pdf',
            bbox_inches='tight', dpi=300, pad_inches=0.02)
fig.savefig(f'{outdir}/fig_ddr_trajectory.png',
            bbox_inches='tight', dpi=300, pad_inches=0.02)
print('Saved PDF and PNG.')

for feat, (rho, pval) in rho_results.items():
    print(f'  {feat}: rho={rho:.4f}, p={pval:.2e}')

plt.close('all')

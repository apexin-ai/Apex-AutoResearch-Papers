import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Nimbus Roman'],
    'font.size': 8,
    'axes.labelsize': 8,
    'axes.titlesize': 9,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 6,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
    'mathtext.fontset': 'cm',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

MODEL_COLORS = {
    'pythia-2.8b':    '#0173B2',
    'pythia-1b':      '#E69F00',
    'olmo-2-1b':      '#009E73',
    'qwen3-0.6b':     '#0072B2',
    'qwen3-1.7b':     '#D55E00',
    'qwen3-8b':       '#CC79A7',
    'llama-3.2-3b':   '#E6AB02',
    'mistral-7b-v0.3':'#56B4E9',
}

SHORT_NAMES = {
    'pythia-2.8b':    'Py-2.8B',
    'pythia-1b':      'Py-1B',
    'olmo-2-1b':      'OLMo-1B',
    'qwen3-0.6b':     'Qw-0.6B',
    'qwen3-1.7b':     'Qw-1.7B',
    'qwen3-8b':       'Qw-8B',
    'llama-3.2-3b':   'Ll-3B',
    'mistral-7b-v0.3':'Mi-7B',
}

PANELS = [
    ('entropy_mean', r'(a) $\bar{H}$ (Entropy Mean)',  'DRIFTING'),
    ('hapax_ratio',  '(b) Hapax Ratio',                'DRIFTING'),
    ('entropy_max',  r'(c) $H_{\max}$ (Entropy Max)',  'STATIONARY'),
    ('tail_decay',   '(d) Tail Decay',                 'STATIONARY'),
]

DRIFT_COLOR = '#2ca02c'
STAT_COLOR  = '#d62728'

df = pd.read_csv('/root/gen-depth-fingerprint/data/features_8gen.csv')
models = sorted(df['model_name'].unique())
depths = sorted(df['depth'].unique())

fig, axes = plt.subplots(2, 2, figsize=(7.0, 3.5))
axes_flat = axes.flatten()

rho_results = {}

for idx, (feat, title, cls) in enumerate(PANELS):
    ax = axes_flat[idx]
    title_color = DRIFT_COLOR if cls == 'DRIFTING' else STAT_COLOR

    # per-generator lines
    for model in models:
        mdf = df[df['model_name'] == model]
        means = [mdf[mdf['depth'] == d][feat].mean() for d in depths]
        ax.plot(depths, means, color=MODEL_COLORS[model],
                linewidth=0.8, alpha=0.4, zorder=2)

    # grand mean + 95% range (min-max across 8 generator means)
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

    ax.plot(depths, grand_means, color='black', linewidth=2.0, zorder=5)
    ax.fill_between(depths, range_lo, range_hi, color='gray', alpha=0.15, zorder=1)

    # pooled Spearman rho
    valid = df[['depth', feat]].dropna()
    rho, pval = spearmanr(valid['depth'], valid[feat])
    rho_results[feat] = (rho, pval)

    ax.text(0.97, 0.95, f'$\\rho$ = {rho:.3f}',
            transform=ax.transAxes, fontsize=7, va='top', ha='right',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='white',
                      edgecolor='#cccccc', alpha=0.9, linewidth=0.5))

    ax.set_title(title, fontsize=8, fontweight='bold', color=title_color, pad=4)
    ax.set_xlabel('Generation Depth', fontsize=7)
    ax.set_ylabel(feat.replace('_', ' ').title() if 'entropy' not in feat
                  else title.split('(')[1].split(')')[0].strip() if '(' in title
                  else feat.replace('_', ' ').title(),
                  fontsize=7)
    ax.set_xticks(depths)

# shared legend at bottom
legend_order = ['pythia-2.8b', 'pythia-1b', 'olmo-2-1b', 'qwen3-0.6b',
                'qwen3-1.7b', 'qwen3-8b', 'llama-3.2-3b', 'mistral-7b-v0.3']
handles = [plt.Line2D([0], [0], color=MODEL_COLORS[m], lw=1.2, label=SHORT_NAMES[m])
           for m in legend_order]
handles.append(plt.Line2D([0], [0], color='black', lw=2.0, label='Grand Mean'))

fig.legend(handles=handles, loc='lower center',
           bbox_to_anchor=(0.5, -0.02), ncol=9, fontsize=5.5,
           handlelength=1.5, columnspacing=0.8, frameon=False)

plt.tight_layout(rect=[0, 0.06, 1, 1])

outdir = '/root/gen-depth-fingerprint/artifacts/_project/chart'
fig.savefig(f'{outdir}/fig_ddr_trajectory.pdf', bbox_inches='tight', dpi=300)
fig.savefig(f'{outdir}/fig_ddr_trajectory.png', bbox_inches='tight', dpi=300)
print('Saved PDF and PNG.')

for feat, (rho, pval) in rho_results.items():
    print(f'  {feat}: rho={rho:.4f}, p={pval:.2e}')

# print figure dimensions for verification
fig2 = plt.figure()
from matplotlib.image import imread
img = imread(f'{outdir}/fig_ddr_trajectory.png')
print(f'PNG dimensions: {img.shape[1]}x{img.shape[0]} px')
plt.close('all')

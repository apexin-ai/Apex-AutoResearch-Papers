import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
from scipy import stats

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

DATADIR = Path('/root/gen-depth-fingerprint/data')
OUTDIR = Path('/root/gen-depth-fingerprint/chart')

MODEL_COLORS = {
    'llama-3.2-3b':   '#E6AB02',
    'mistral-7b-v0.3':'#56B4E9',
    'olmo-2-1b':      '#009E73',
    'pythia-1b':      '#F0E442',
    'pythia-2.8b':    '#0173B2',
    'qwen3-0.6b':     '#CC79A7',
    'qwen3-1.7b':     '#D55E00',
    'qwen3-8b':       '#BBBBBB',
}

FEATURES = [
    ('entropy_mean', 'Entropy Mean',  'DRIFTING'),
    ('entropy_std',  'Entropy Std',   'INTERMEDIATE'),
    ('entropy_min',  'Entropy Min',   'NEAR-STATIONARY'),
    ('entropy_max',  'Entropy Max',   'STATIONARY'),
    ('tail_decay',   'Tail Decay',    'STATIONARY'),
    ('ttr',          'TTR',           'DRIFTING'),
    ('hapax_ratio',  'Hapax Ratio',   'DRIFTING'),
]

CLASS_COLORS = {
    'DRIFTING':         '#009E73',
    'INTERMEDIATE':     '#E69F00',
    'NEAR-STATIONARY':  '#E69F00',
    'STATIONARY':       '#E69F00',
}

def main():
    df = pd.read_csv(DATADIR / 'features_8gen.csv')
    models = sorted(df['model_name'].unique())
    depths = sorted(df['depth'].unique())

    fig, axes = plt.subplots(3, 3, figsize=(10, 8.5))
    axes_flat = axes.flatten()

    for idx, (feat, label, cls) in enumerate(FEATURES):
        ax = axes_flat[idx]

        for model in models:
            mdf = df[df['model_name'] == model]
            means = [mdf[mdf['depth'] == d][feat].mean() for d in depths]
            ax.plot(depths, means, color=MODEL_COLORS.get(model, '#888888'),
                    linewidth=1, alpha=0.7, label=model)

        overall_means = []
        ci_lo, ci_hi = [], []
        for d in depths:
            vals = df[df['depth'] == d][feat].dropna().values
            m = np.mean(vals)
            se = np.std(vals, ddof=1) / np.sqrt(len(vals))
            overall_means.append(m)
            ci_lo.append(m - 1.96 * se)
            ci_hi.append(m + 1.96 * se)

        ax.plot(depths, overall_means, color='black', linewidth=2.5, zorder=5)
        ax.fill_between(depths, ci_lo, ci_hi, color='gray', alpha=0.2, zorder=4)

        # sample-level Spearman rho
        valid = df[['depth', feat]].dropna()
        rho, _ = stats.spearmanr(valid['depth'], valid[feat])
        # R^2 on depth-level means (trend fit)
        slope, intercept, r, p, se = stats.linregress(depths, overall_means)
        r2 = r ** 2

        dagger = '†' if cls == 'NEAR-STATIONARY' else ''
        title_color = CLASS_COLORS.get(cls, '#333333')
        ax.set_title(f'{label} [{cls}]{dagger}',
                     fontsize=10, fontweight='bold', color=title_color)
        ax.set_ylabel(label)
        ax.set_xlabel('Depth')

        box_text = f'ρ = {rho:.3f}\nR² = {r2:.3f}'
        ax.text(0.95, 0.05, box_text, transform=ax.transAxes,
                fontsize=8, va='bottom', ha='right',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                          edgecolor='gray', alpha=0.9))

    for j in range(len(FEATURES), 9):
        axes_flat[j].set_visible(False)

    handles, labels_list = axes_flat[0].get_legend_handles_labels()
    mean_line = plt.Line2D([0], [0], color='black', linewidth=2.5, label='Mean (all gen.)')
    handles.append(mean_line)
    labels_list.append('Mean (all gen.)')
    fig.legend(handles, labels_list, loc='lower right',
               bbox_to_anchor=(0.95, 0.02), ncol=2, fontsize=9,
               frameon=True, framealpha=0.9, edgecolor='none')

    plt.tight_layout(rect=[0, 0.08, 1, 1])
    fig.savefig(OUTDIR / 'fig_appendix_ddr_trends.pdf')
    print(f'Saved: {OUTDIR / "fig_appendix_ddr_trends.pdf"}')

if __name__ == '__main__':
    main()

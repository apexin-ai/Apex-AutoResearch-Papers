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
    'font.size': 9,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 7.5,
    'legend.fontsize': 7.5,
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
    'qwen3-8b':       '#7570B3',
}

FEATURES = [
    ('entropy_mean', 'Entropy Mean',  'DRIFTING'),
    ('entropy_std',  'Entropy Std',   'INTERMEDIATE'),
    ('entropy_min',  'Entropy Min',   'NEAR-STATIONARY'),
    ('entropy_max',  'Entropy Max',   'NEAR-STATIONARY'),
    ('tail_decay',   'Tail Decay',    'NEAR-STATIONARY'),
    ('ttr',          'TTR',           'DRIFTING'),
    ('hapax_ratio',  'Hapax Ratio',   'DRIFTING'),
]

ZONE_COLORS = {
    'DRIFTING':        '#0072B2',
    'INTERMEDIATE':    '#882255',
    'NEAR-STATIONARY': '#E69F00',
}

MEAN_LW = 1.4
MEAN_ALPHA = 0.9
SHADE_ALPHA = 0.12
GEN_ALPHA = 0.65
GEN_LW = 1.0

def main():
    df = pd.read_csv(DATADIR / 'features_8gen.csv')
    models = sorted(df['model_name'].unique())
    depths = sorted(df['depth'].unique())

    fig, axes = plt.subplots(2, 4, figsize=(10, 5.2))
    axes_flat = axes.flatten()

    for idx, (feat, label, zone) in enumerate(FEATURES):
        ax = axes_flat[idx]
        c_mean = ZONE_COLORS[zone]

        for model in models:
            mdf = df[df['model_name'] == model]
            means = [mdf[mdf['depth'] == d][feat].mean() for d in depths]
            ax.plot(depths, means, color=MODEL_COLORS.get(model, '#888888'),
                    linewidth=GEN_LW, alpha=GEN_ALPHA, label=model, zorder=8)

        overall_means = []
        ci_lo, ci_hi = [], []
        for d in depths:
            vals = df[df['depth'] == d][feat].dropna().values
            m = np.mean(vals)
            se = np.std(vals, ddof=1) / np.sqrt(len(vals))
            overall_means.append(m)
            ci_lo.append(m - 1.96 * se)
            ci_hi.append(m + 1.96 * se)

        ax.fill_between(depths, ci_lo, ci_hi,
                        color=c_mean, alpha=SHADE_ALPHA, zorder=5)
        ax.plot(depths, overall_means, color=c_mean, linewidth=MEAN_LW,
                alpha=MEAN_ALPHA, zorder=10)

        valid = df[['depth', feat]].dropna()
        rho, _ = stats.spearmanr(valid['depth'], valid[feat])
        slope, intercept, r, p, se = stats.linregress(depths, overall_means)
        r2 = r ** 2

        ax.set_title(f'{label}\n[{zone}]',
                     fontsize=8, fontweight='bold', color=c_mean,
                     linespacing=1.1)
        ax.set_ylabel(label, fontsize=8)
        ax.set_xlabel('Depth', fontsize=8)

        box_text = f'ρ = {rho:.3f}\nR² = {r2:.3f}'
        ax.text(0.95, 0.05, box_text, transform=ax.transAxes,
                fontsize=7, va='bottom', ha='right',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                          edgecolor='#CCCCCC', alpha=0.9))

    ax_legend = axes_flat[7]
    ax_legend.set_visible(False)

    handles, labels_list = axes_flat[0].get_legend_handles_labels()

    zone_handles = []
    for zname, zcol in ZONE_COLORS.items():
        zone_handles.append(plt.Line2D([0], [0], color=zcol, linewidth=MEAN_LW,
                                       alpha=MEAN_ALPHA, label=f'Mean [{zname}]'))
    shade_patch = plt.matplotlib.patches.Patch(
        facecolor='#888888', alpha=0.25, label='±1.96 SE')
    all_handles = zone_handles + [shade_patch] + handles
    all_labels = [h.get_label() for h in zone_handles] + ['±1.96 SE'] + labels_list

    fig.legend(all_handles, all_labels,
               loc='center', bbox_to_anchor=(0.875, 0.25),
               ncol=1, fontsize=7.5,
               frameon=True, framealpha=0.9, edgecolor='#CCCCCC',
               handlelength=1.5, columnspacing=1.0)

    plt.subplots_adjust(hspace=0.7, wspace=0.4)
    fig.savefig(OUTDIR / 'fig_appendix_ddr_trends.pdf')
    print(f'Saved: {OUTDIR / "fig_appendix_ddr_trends.pdf"}')

if __name__ == '__main__':
    main()

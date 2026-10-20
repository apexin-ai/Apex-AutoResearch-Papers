import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import json
from pathlib import Path

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

OUTDIR = Path('/root/gen-depth-fingerprint/paper/figures')
DATADIR = Path('/root/gen-depth-fingerprint/data')

COLORS = {
    'pythia-2.8b': '#0173B2',
    'pythia-1b': '#56B4E9',
    'olmo-2-1b': '#009E73',
    'qwen3-1.7b': '#E69F00',
    'qwen3-0.6b': '#BCBD22',
    'qwen3-8b': '#D55E00',
}
DISPLAY = {
    'pythia-2.8b': 'Pythia-2.8B',
    'pythia-1b': 'Pythia-1B',
    'olmo-2-1b': 'OLMo-2-1B',
    'qwen3-1.7b': 'Qwen3-1.7B',
    'qwen3-0.6b': 'Qwen3-0.6B',
    'qwen3-8b': 'Qwen3-8B',
}
MODEL_ORDER = ['pythia-2.8b', 'pythia-1b', 'olmo-2-1b', 'qwen3-1.7b', 'qwen3-0.6b', 'qwen3-8b']
MARKERS = {'pythia-2.8b': 'o', 'pythia-1b': 's', 'olmo-2-1b': '^', 'qwen3-1.7b': 'D', 'qwen3-0.6b': 'v', 'qwen3-8b': 'P'}


def bootstrap_ci(x, n_boot=1000, ci=0.95):
    rng = np.random.RandomState(42)
    means = np.array([np.mean(rng.choice(x, size=len(x), replace=True)) for _ in range(n_boot)])
    lo = np.percentile(means, (1 - ci) / 2 * 100)
    hi = np.percentile(means, (1 + ci) / 2 * 100)
    return np.mean(x), lo, hi


# ============================================================
# Fig 1: Differential Depth Response (2x2)
# ============================================================
def fig1():
    df = pd.read_csv(DATADIR / 'features_all_models.csv')
    features = [
        ('entropy_mean', 'Entropy Mean', '(a) Central tendency — monotonic drift'),
        ('hapax_ratio', 'Hapax Ratio', '(b) Vocabulary diversity — monotonic drift'),
        ('entropy_std', 'Entropy Std', '(c) Shape — near-stationary'),
        ('tail_decay', 'Tail Decay', '(d) Shape — near-stationary'),
    ]

    fig, axes = plt.subplots(2, 2, figsize=(7, 4.5), sharex=True)
    axes = axes.flatten()

    for idx, (feat, ylabel, title) in enumerate(features):
        ax = axes[idx]
        for model in MODEL_ORDER:
            mdf = df[df['model_name'] == model]
            depths = sorted(mdf['depth'].unique())
            means, los, his = [], [], []
            for d in depths:
                vals = mdf[mdf['depth'] == d][feat].dropna().values
                m, lo, hi = bootstrap_ci(vals)
                means.append(m)
                los.append(lo)
                his.append(hi)
            ax.plot(depths, means, marker=MARKERS[model], markersize=4,
                    color=COLORS[model], label=DISPLAY[model], linewidth=1.5, zorder=3)
            ax.fill_between(depths, los, his, alpha=0.12, color=COLORS[model], zorder=2)

        ax.set_title(title, fontsize=9, fontweight='bold')
        ax.set_ylabel(ylabel)
        if idx >= 2:
            ax.set_xlabel('Generation Depth')
        ax.grid(axis='y', alpha=0.3, linewidth=0.5)

    axes[0].legend(loc='best', frameon=True, framealpha=0.9, edgecolor='none',
                   ncol=2, fontsize=7, handlelength=1.5)
    fig.suptitle('Differential Depth Response of Distributional Features',
                 fontsize=12, fontweight='bold', y=1.02)
    plt.tight_layout()
    fig.savefig(OUTDIR / 'fig1_differential_response.pdf')
    fig.savefig(OUTDIR / 'fig1_differential_response.png')
    plt.close()
    print('Fig 1 saved.')


# ============================================================
# Fig 2: LOGO Classification Performance
# ============================================================
def fig2():
    with open(DATADIR / 'cross_generator_results.json') as f:
        data = json.load(f)

    logo = data['leave_one_generator_out']

    generators = MODEL_ORDER
    classes = ['macro', 'gen-0', 'gen-1', 'gen-2+']
    class_labels = ['Macro-F1', 'Gen-0', 'Gen-1', 'Gen-2+']
    class_colors = ['#333333', '#0173B2', '#E69F00', '#D55E00']

    x = np.arange(len(generators))
    width = 0.18
    fig, ax = plt.subplots(figsize=(7, 4))

    for i, (cls, clabel, cc) in enumerate(zip(classes, class_labels, class_colors)):
        vals, errs_lo, errs_hi = [], [], []
        for g in generators:
            gd = logo[g]
            if cls == 'macro':
                v = gd['macro_f1']
                ci = gd['bootstrap_ci']['macro']
            else:
                v = gd[f'{cls}_f1']
                ci = gd['bootstrap_ci'][cls]
            vals.append(v)
            errs_lo.append(v - ci['ci_lo'])
            errs_hi.append(ci['ci_hi'] - v)
        bars = ax.bar(x + (i - 1.5) * width, vals, width, label=clabel, color=cc,
                      alpha=0.85, edgecolor='white', linewidth=0.5)
        ax.errorbar(x + (i - 1.5) * width, vals, yerr=[errs_lo, errs_hi],
                    fmt='none', ecolor='#555555', capsize=2, capthick=0.8, linewidth=0.8)

    overall_mean = np.mean([logo[g]['macro_f1'] for g in generators])
    ax.axhline(y=overall_mean, color='#CC0000', linestyle='--', linewidth=1.2,
               label=f'LOGO Mean ({overall_mean:.3f})', zorder=5)

    ax.set_xlabel('Held-out Generator')
    ax.set_ylabel('F1 Score')
    ax.set_title('Leave-One-Generator-Out Classification Performance',
                 fontsize=12, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels([DISPLAY[g] for g in generators], rotation=15, ha='right')
    ax.set_ylim(0.4, 1.02)
    ax.legend(loc='upper right', frameon=True, framealpha=0.9, edgecolor='none',
              fontsize=8, ncol=2)
    ax.grid(axis='y', alpha=0.3, linewidth=0.5)
    plt.tight_layout()
    fig.savefig(OUTDIR / 'fig2_logo_performance.pdf')
    fig.savefig(OUTDIR / 'fig2_logo_performance.png')
    plt.close()
    print('Fig 2 saved.')


# ============================================================
# Fig 3: Baseline Comparison (forest plot)
# ============================================================
def fig3():
    methods = [
        ('7-Feature Ensemble', 0.798, 0.7858, 0.7992),
        ('Avg-LogProb', 0.7653, 0.6155, 0.8197),
        ('LD-Score', 0.7212, 0.5884, 0.7701),
        ('FastDetectGPT', 0.6269, 0.5105, 0.7624),
        ('Binoculars', 0.579, 0.4052, 0.6637),
    ]

    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    y_pos = np.arange(len(methods))[::-1]

    for i, (name, mean, lo, hi) in enumerate(methods):
        y = y_pos[i]
        color = '#CC0000' if i == 0 else '#333333'
        marker = 'D' if i == 0 else 'o'
        ms = 7 if i == 0 else 6
        ax.errorbar(mean, y, xerr=[[mean - lo], [hi - mean]],
                     fmt=marker, color=color, markersize=ms,
                     capsize=4, capthick=1.2, linewidth=1.5, zorder=5)
        ci_width = hi - lo
        ax.annotate(f'{mean:.3f} [{lo:.3f}, {hi:.3f}]',
                    xy=(hi + 0.008, y), fontsize=8, va='center', color='#444444')

    ax.set_yticks(y_pos)
    ax.set_yticklabels([m[0] for m in methods])
    ax.set_xlabel('LOGO Macro-F1')
    ax.set_title('Comparison with Single-Detector Baselines',
                 fontsize=12, fontweight='bold')
    ax.set_xlim(0.35, 0.92)
    ax.axvline(x=0.5, color='#CCCCCC', linestyle=':', linewidth=0.8)
    ax.grid(axis='x', alpha=0.3, linewidth=0.5)

    ax.annotate('Tight CI', xy=(0.798, y_pos[0] + 0.35), fontsize=7,
                color='#CC0000', ha='center', fontstyle='italic')
    ax.annotate('Wide CI (high cross-generator variance)', xy=(0.63, y_pos[-1] - 0.45),
                fontsize=7, color='#666666', ha='center', fontstyle='italic')

    plt.tight_layout()
    fig.savefig(OUTDIR / 'fig3_baseline_comparison.pdf')
    fig.savefig(OUTDIR / 'fig3_baseline_comparison.png')
    plt.close()
    print('Fig 3 saved.')


# ============================================================
# Fig 4: Downstream Negative (bar chart)
# ============================================================
def fig4():
    variants = {
        'All\n(no filter)':   {'ppls': [2.3348, 2.3350, 2.3354], 'n': 12299},
        'Size-\nmatched':     {'ppls': [2.3674, 2.3666, 2.3674], 'n': 3951},
        'Depth\n0+1':         {'ppls': [2.3877, 2.3869, 2.3867], 'n': 3951},
        'Binary\nfiltered':   {'ppls': [2.3888, 2.3891, 2.3894], 'n': 3951},
        'Depth 0\nonly':      {'ppls': [2.6818, 2.6813, 2.6817], 'n': 797},
    }

    names = list(variants.keys())
    means = [np.mean(v['ppls']) for v in variants.values()]
    stds = [np.std(v['ppls'], ddof=1) for v in variants.values()]
    counts = [v['n'] for v in variants.values()]

    colors = ['#0173B2', '#56B4E9', '#E69F00', '#D55E00', '#CC79A7']

    fig, ax = plt.subplots(figsize=(5.5, 4))
    x = np.arange(len(names))
    bars = ax.bar(x, means, yerr=stds, capsize=4, color=colors, alpha=0.85,
                  edgecolor='white', linewidth=0.8, error_kw={'linewidth': 1.2, 'capthick': 1})

    for i, (m, n) in enumerate(zip(means, counts)):
        ax.text(i, m + 0.015, f'n={n:,}', ha='center', va='bottom', fontsize=7.5,
                color='#444444', fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=9)
    ax.set_ylabel('Eval Perplexity')
    ax.set_title('Depth-Aware Curation Does Not Improve Downstream CLM Quality',
                 fontsize=11, fontweight='bold')

    ax.axhline(y=means[1], color='#888888', linestyle='--', linewidth=0.8, alpha=0.7)
    ax.annotate('size-matched baseline', xy=(3.8, means[1] + 0.005),
                fontsize=7, color='#888888', fontstyle='italic')

    ymin = min(means) - 0.06
    ymax = max(means) + 0.08
    ax.set_ylim(ymin, ymax)

    ax_break = ax.secondary_yaxis('right')
    ax_break.set_yticks([])

    ax.grid(axis='y', alpha=0.3, linewidth=0.5)
    plt.tight_layout()
    fig.savefig(OUTDIR / 'fig4_downstream_negative.pdf')
    fig.savefig(OUTDIR / 'fig4_downstream_negative.png')
    plt.close()
    print('Fig 4 saved.')


if __name__ == '__main__':
    fig1()
    fig2()
    fig3()
    fig4()
    print(f'\nAll figures saved to {OUTDIR}')
    for f in sorted(OUTDIR.glob('fig*')):
        print(f'  {f}')

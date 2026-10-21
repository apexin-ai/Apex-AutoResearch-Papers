"""Appendix: DDR trends — 7 features × 8 generators, mean line unified #0072B2."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import spearmanr, linregress

DATA = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/supplement/data/features_all_models.csv'
df = pd.read_csv(DATA)

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif'],
    'font.size': 8,
    'axes.labelsize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'mathtext.fontset': 'cm',
})

PALETTE = [
    '#0072B2',  # blue  — Pythia-2.8B
    '#56B4E9',  # sky   — Pythia-1B
    '#009E73',  # green — OLMo
    '#E69F00',  # amber — Qwen-0.6B
    '#D55E00',  # vermillion — Qwen-1.7B
    '#CC79A7',  # pink  — Qwen-8B
    '#999900',  # darkened yellow — Llama
    '#882255',  # wine  — Mistral
]

GENERATORS = [
    ('pythia-2.8b',      'Py-2.8B',   PALETTE[0]),
    ('pythia-1b',        'Py-1B',     PALETTE[1]),
    ('olmo-2-1b',        'OLMo',      PALETTE[2]),
    ('qwen3-0.6b',       'Qw-0.6B',   PALETTE[3]),
    ('qwen3-1.7b',       'Qw-1.7B',   PALETTE[4]),
    ('qwen3-8b',         'Qw-8B',     PALETTE[5]),
    ('llama-3.2-3b',     'Llama',     PALETTE[6]),
    ('mistral-7b-v0.3',  'Mistral',   PALETTE[7]),
]

C_MEAN = '#0072B2'

FEATURES = [
    ('entropy_mean', r'Entropy Mean ($\bar{H}$)',       'Drifting'),
    ('ttr',          r'TTR',                             'Drifting'),
    ('hapax_ratio',  r'Hapax Ratio',                     'Drifting'),
    ('entropy_std',  r'Entropy Std ($\sigma_H$)',        'Intermediate'),
    ('entropy_min',  r'Entropy Min ($H_{\min}$)',        'Near-stationary'),
    ('entropy_max',  r'Entropy Max ($H_{\max}$)',        'Near-stationary'),
    ('tail_decay',   r'Tail Decay',                      'Near-stationary'),
]

ZONE_COLORS = {
    'Drifting':        '#0072B2',
    'Intermediate':    '#882255',
    'Near-stationary': '#E69F00',
}

depths = sorted(df['depth'].unique())

fig, axes = plt.subplots(4, 2, figsize=(6.8, 8.5), sharex=True)
panel_labels = [f'({chr(97+i)})' for i in range(7)]

for idx, (feat, label, zone) in enumerate(FEATURES):
    row, col = idx // 2, idx % 2
    ax = axes[row][col]

    all_means = []
    for gen_name, gen_short, gen_color in GENERATORS:
        sub = df[df['model_name'] == gen_name]
        means = sub.groupby('depth')[feat].mean().reindex(depths)
        all_means.append(means.values)
        ax.plot(depths, means.values,
                color=gen_color, linewidth=0.7, alpha=0.45,
                marker='o', markersize=2, markeredgewidth=0, zorder=2)

    all_means_arr = np.array(all_means)
    grand = np.mean(all_means_arr, axis=0)
    se = np.std(all_means_arr, axis=0, ddof=1) / np.sqrt(len(GENERATORS))

    ax.fill_between(depths, grand - 1.96 * se, grand + 1.96 * se,
                     color=C_MEAN, alpha=0.15, zorder=3)
    ax.plot(depths, grand,
            color=C_MEAN, linewidth=1.6, alpha=0.9, zorder=4)
    ax.scatter(depths, grand,
               color=C_MEAN, marker='D', s=24,
               edgecolors='white', linewidths=0.5, zorder=5)

    # Spearman ρ + R²
    all_d, all_v = [], []
    for gen_name, _, _ in GENERATORS:
        sub = df[df['model_name'] == gen_name]
        all_d.extend(sub['depth'].values)
        all_v.extend(sub[feat].values)
    rho, _ = spearmanr(all_d, all_v)
    slope, intercept, r_value, _, _ = linregress(all_d, all_v)
    r2 = r_value ** 2

    ax.text(0.97, 0.95,
            rf'$\rho = {rho:.3f}$' + '\n' + rf'$R^2 = {r2:.3f}$',
            transform=ax.transAxes, fontsize=6, va='top', ha='right',
            color='#555', linespacing=1.3,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor='#ddd', linewidth=0.4, alpha=0.9))

    zone_col = ZONE_COLORS[zone]
    ax.set_title(f'{panel_labels[idx]} {label}', fontsize=8, pad=4,
                 loc='left', fontweight='normal')
    ax.text(1.0, 1.02, zone, transform=ax.transAxes, fontsize=5.5,
            ha='right', va='bottom', color=zone_col, fontstyle='italic')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#999')
    ax.spines['left'].set_linewidth(0.5)
    ax.spines['bottom'].set_color('#999')
    ax.spines['bottom'].set_linewidth(0.5)
    ax.tick_params(length=3, width=0.5, color='#999')
    ax.set_xticks(depths)
    if row == 3 or (row == 2 and col == 1 and idx == 6):
        ax.set_xlabel('Generation Depth', fontsize=7.5)

# Hide the 8th panel (bottom-right), use for legend
ax_last = axes[3][1]
ax_last.axis('off')

# Legend in the empty panel
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
handles = []
for _, gen_short, gen_color in GENERATORS:
    handles.append(Line2D([0], [0], color=gen_color, linewidth=0.8,
                          alpha=0.6, marker='o', markersize=2.5,
                          markeredgewidth=0, label=gen_short))
handles.append(Line2D([0], [0], color=C_MEAN, linewidth=1.6,
                       marker='D', markersize=4, markeredgecolor='white',
                       markeredgewidth=0.5, label='Grand Mean'))
handles.append(Patch(facecolor=C_MEAN, alpha=0.15, edgecolor='none',
                     label=r'$\pm$1.96 SE'))

ax_last.legend(handles=handles, loc='center', ncol=2,
               fontsize=8.5, frameon=True, framealpha=0.95,
               edgecolor='#ddd', fancybox=False,
               handletextpad=0.4, columnspacing=1.0)

# Suppress x labels on non-bottom rows
for r in range(3):
    for c in range(2):
        axes[r][c].xaxis.set_tick_params(labelbottom=False)
# Row 3 col 0 needs x labels (it's the last feature panel)
axes[3][0].xaxis.set_tick_params(labelbottom=True)

plt.tight_layout(rect=[0, 0, 1, 1])
plt.subplots_adjust(hspace=0.30, wspace=0.28)

out1 = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart'
out2 = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/chart'

fig.savefig(f'{out1}/fig_appendix_ddr_trends.pdf', format='pdf')
fig.savefig(f'{out1}/fig_appendix_ddr_trends.png', format='png')
fig.savefig(f'{out2}/fig_appendix_ddr_trends.pdf', format='pdf')
fig.savefig(f'{out2}/fig_appendix_ddr_trends.png', format='png')
print(f'Saved to {out1}/ and {out2}/')

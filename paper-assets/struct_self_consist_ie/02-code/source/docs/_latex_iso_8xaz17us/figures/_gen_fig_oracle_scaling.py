"""Generate fig_oracle_scaling: Oracle F1 vs N with power-law fits."""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.5,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'mathtext.fontset': 'dejavusans',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

STYLE = {
    'CoNLL':   {'color': '#228833', 'marker': 's'},
    'SciERC':  {'color': '#EE6677', 'marker': '^'},
    'FewNERD': {'color': '#4477AA', 'marker': 'o'},
}
DATASETS = ['SciERC', 'CoNLL', 'FewNERD']
MODELS = ['Qwen2.5-7B', 'LLaMA-3.1-8B']
LSTYLE = {'Qwen2.5-7B': '-', 'LLaMA-3.1-8B': '--'}

FITS = {
    ('SciERC',  'Qwen2.5-7B'):   {'a': 0.914, 'b': 0.282, 'c': 0.390},
    ('SciERC',  'LLaMA-3.1-8B'): {'a': 0.938, 'b': 0.296, 'c': 0.302},
    ('CoNLL',   'Qwen2.5-7B'):   {'a': 0.972, 'b': 0.099, 'c': 0.839},
    ('CoNLL',   'LLaMA-3.1-8B'): {'a': 0.969, 'b': 0.043, 'c': 0.329},
    ('FewNERD', 'Qwen2.5-7B'):   {'a': 0.957, 'b': 0.251, 'c': 0.612},
    ('FewNERD', 'LLaMA-3.1-8B'): {'a': 0.941, 'b': 0.192, 'c': 0.609},
}

N_GRID = {
    'SciERC':  [1, 2, 4, 8, 16, 32],
    'CoNLL':   [1, 2, 4, 8, 16],
    'FewNERD': [1, 2, 4, 8, 16],
}

GREEDY = {
    ('SciERC',  'Qwen2.5-7B'):   0.665,
    ('SciERC',  'LLaMA-3.1-8B'): 0.661,
    ('CoNLL',   'Qwen2.5-7B'):   0.912,
    ('CoNLL',   'LLaMA-3.1-8B'): 0.930,
    ('FewNERD', 'Qwen2.5-7B'):   0.793,
    ('FewNERD', 'LLaMA-3.1-8B'): 0.799,
}


def f1_at(ds, model, N):
    p = FITS[(ds, model)]
    return p['a'] - p['b'] * np.power(np.asarray(N, dtype=float), -p['c'])


def main():
    fig, ax = plt.subplots(figsize=(3.4, 2.8))
    fig.patch.set_facecolor('#FAFAFA')
    ax.set_facecolor('#F5F7FA')
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_color('#CCCCCC')
        ax.spines[spine].set_linewidth(0.8)
    ax.tick_params(colors='#555555', which='both')
    ax.grid(True, alpha=0.15, linewidth=0.5, color='#888888')
    ax.set_axisbelow(True)

    N_curve = np.geomspace(1, 32, 400)

    # Greedy baselines (mean)
    for ds in DATASETS:
        gy = 0.5 * (GREEDY[(ds, 'Qwen2.5-7B')] + GREEDY[(ds, 'LLaMA-3.1-8B')])
        ax.axhline(y=gy, color=STYLE[ds]['color'], linestyle=':',
                   linewidth=0.7, alpha=0.35, zorder=1)

    # Power-law curves + data points
    for ds in DATASETS:
        color = STYLE[ds]['color']
        marker = STYLE[ds]['marker']
        for model in MODELS:
            ls = LSTYLE[model]
            ax.plot(N_curve, f1_at(ds, model, N_curve),
                    linestyle=ls, color=color, alpha=0.7, linewidth=1.4,
                    zorder=2)
            N_pts = np.array(N_GRID[ds], dtype=float)
            ax.scatter(N_pts, f1_at(ds, model, N_pts),
                       marker=marker, facecolor=color,
                       edgecolor='white', linewidth=0.5, s=40, zorder=4)

    ax.set_xscale('log', base=2)
    ax.set_xticks([1, 2, 4, 8, 16, 32])
    ax.set_xticklabels(['1', '2', '4', '8', '16', '32'])
    ax.set_xlim(0.85, 38)
    ax.set_ylim(0.60, 1.00)
    ax.set_xlabel(r'Number of Samples ($N$)')
    ax.set_ylabel(r'Oracle $F_1$')

    # Unified legend with rounded box
    handles = []
    for ds in DATASETS:
        handles.append(
            Line2D([0], [0], color=STYLE[ds]['color'],
                   marker=STYLE[ds]['marker'], linestyle='-',
                   linewidth=1.2, markersize=5, markeredgecolor='white',
                   markeredgewidth=0.4, label=ds)
        )
    handles.append(Line2D([0], [0], color='#555555', linestyle='-',
                          linewidth=1.2, label='Qwen2.5-7B'))
    handles.append(Line2D([0], [0], color='#555555', linestyle='--',
                          linewidth=1.2, label='LLaMA-3.1-8B'))
    handles.append(Line2D([0], [0], color='#555555', linestyle=':',
                          linewidth=0.7, alpha=0.6, label=r'Greedy ($T{=}0$)'))

    ax.legend(handles=handles, loc='lower right',
              bbox_to_anchor=(0.99, 0.01),
              fontsize=7.5, handlelength=1.8, labelspacing=0.3,
              ncol=2, columnspacing=1.0,
              frameon=True, fancybox=True, edgecolor='#CCCCCC',
              facecolor='white', framealpha=0.95)

    out_dir = os.path.dirname(os.path.abspath(__file__))
    fig.savefig(os.path.join(out_dir, 'fig_oracle_scaling.pdf'), format='pdf')
    fig.savefig(os.path.join(out_dir, 'fig_oracle_scaling.png'), format='png')
    plt.close(fig)
    print('Saved fig_oracle_scaling.pdf and .png')


if __name__ == '__main__':
    main()

"""Generate fig_degeneracy_lp_scatter: LP Selection delta-F1 vs degeneracy rate."""
import json
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from scipy import stats

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

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
DATA_JSON = os.path.join(PROJECT_ROOT, 'artifacts', 'scatter_v2_data.json')

CATEGORY_STYLE = {
    'Qwen3-8B (canonical)':  {'color': '#1f5fa8', 'marker': 'o', 'size': 90, 'edge': 'white'},
    'Qwen3-8B (multi-seed)': {'color': '#9fc1e6', 'marker': 'o', 'size': 50, 'edge': 'white'},
    'LLaMA3.1-8B':           {'color': '#d8553b', 'marker': 's', 'size': 60, 'edge': 'white'},
    'Epoch ablation':        {'color': '#3aa757', 'marker': '^', 'size': 65, 'edge': 'white'},
    'Rank ablation':         {'color': '#7b3294', 'marker': 'D', 'size': 55, 'edge': 'white'},
    'Temperature ablation':  {'color': '#e88c2a', 'marker': 'v', 'size': 60, 'edge': 'white'},
    'Qwen3-4B':              {'color': '#1a8f8a', 'marker': 'P', 'size': 65, 'edge': 'white'},
}

CATEGORY_MAP = {
    'cross-dataset': 'Qwen3-8B (canonical)',
    'multi-seed':    'Qwen3-8B (multi-seed)',
    'LLaMA3.1-8B':   'LLaMA3.1-8B',
    'epoch':         'Epoch ablation',
    'rank':          'Rank ablation',
    'temperature':   'Temperature ablation',
    'Qwen3-4B':      'Qwen3-4B',
}


def main():
    with open(DATA_JSON) as f:
        rows = json.load(f)

    x = np.array([r['degen_pct'] for r in rows])
    y = np.array([r['lp_delta_pp'] for r in rows])
    cats = [CATEGORY_MAP[r['category']] for r in rows]

    rho, pval = stats.spearmanr(x, y)
    n = len(rows)

    fig, ax = plt.subplots(figsize=(3.4, 2.8))
    fig.patch.set_facecolor('#FAFAFA')
    ax.set_facecolor('#F5F7FA')
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_color('#CCCCCC')
        ax.spines[spine].set_linewidth(0.8)
    ax.tick_params(colors='#555555', which='both')
    ax.grid(True, alpha=0.15, linewidth=0.5, color='#888888')
    ax.set_axisbelow(True)

    ax.axhline(y=0, color='#888888', linestyle='--', linewidth=0.6, alpha=0.5, zorder=1)

    for disp_cat, sty in CATEGORY_STYLE.items():
        mask = np.array([c == disp_cat for c in cats])
        if not mask.any():
            continue
        ax.scatter(
            x[mask], y[mask],
            marker=sty['marker'],
            facecolor=sty['color'],
            edgecolor=sty['edge'],
            linewidth=0.5,
            s=sty['size'],
            alpha=0.88,
            zorder=4,
            label=disp_cat,
        )

    ax.set_xlabel('Degeneracy Rate (%)')
    ax.set_ylabel(r'LP Selection $\Delta F_1$ (pp)')

    xmin = max(0, x.min() - 4)
    xmax = min(100, x.max() + 4)
    ax.set_xlim(xmin, xmax)
    ymin = float(y.min()) - 0.25
    ymax = float(y.max()) + 0.30
    ax.set_ylim(ymin, ymax)

    annot = f'$\\rho = {rho:.3f}$  ($p = {pval:.2f}$, $n = {n}$)'
    ax.text(0.98, 0.03, annot, transform=ax.transAxes,
            ha='right', va='bottom', fontsize=7.5,
            bbox=dict(boxstyle='round,pad=0.35', facecolor='white',
                      edgecolor='#CCCCCC', linewidth=0.6, alpha=0.95))

    handles = [
        Line2D([0], [0], marker=sty['marker'], color='w',
               markerfacecolor=sty['color'], markeredgecolor=sty['edge'],
               markeredgewidth=0.5,
               markersize=np.sqrt(sty['size']) * 0.7, label=cat)
        for cat, sty in CATEGORY_STYLE.items()
    ]
    ax.legend(handles=handles, loc='lower center',
              bbox_to_anchor=(0.5, 1.01), ncol=4,
              fontsize=6.5, handletextpad=0.25,
              columnspacing=0.7, borderpad=0.0, labelspacing=0.3,
              frameon=True, fancybox=True, edgecolor='#CCCCCC',
              facecolor='#FAFAFA', framealpha=0.95)

    fig.savefig(os.path.join(HERE, 'fig_degeneracy_lp_scatter.pdf'), format='pdf')
    fig.savefig(os.path.join(HERE, 'fig_degeneracy_lp_scatter.png'), format='png')
    plt.close(fig)
    print(f'Saved fig_degeneracy_lp_scatter.pdf and .png  '
          f'(rho={rho:.3f}, p={pval:.4f}, n={n})')


if __name__ == '__main__':
    main()

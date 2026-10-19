#!/usr/bin/env python3
"""
Figure A.4: Bootstrap Distribution of ASV delta* (B=1000)

Standalone plotting script for the EMNLP 2026 paper appendix.
Reads pre-computed bootstrap results from artifacts/exp_c_bootstrap_results.json
and generates a polished 1x3 panel figure.
"""
import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Paths ───────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
RESULTS_JSON = os.path.join(PROJECT_ROOT, 'artifacts', 'exp_c_bootstrap_results.json')
OUT_PDF = os.path.join(SCRIPT_DIR, 'exp_c_bootstrap_figure.pdf')
OUT_PNG = os.path.join(SCRIPT_DIR, 'exp_c_bootstrap_figure.png')

# ── Unified paper style ─────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.8,
    'xtick.direction': 'out',
    'ytick.direction': 'out',
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.5,
})

# ── Topology colors (unified paper palette) ────────────────────
COLORS = {
    'confounding': '#1B4F72',
    'exposure': '#C0392B',
    'iv': '#922B21',
}

TOPO_LABELS = {
    'confounding': 'Confounding',
    'exposure': 'Exposure',
    'iv': 'IV',
}

TOPOLOGIES = ['confounding', 'exposure', 'iv']


def main():
    # Load results
    with open(RESULTS_JSON) as f:
        results = json.load(f)

    fig, axes = plt.subplots(1, 3, figsize=(9, 3.0))

    for ax, topo in zip(axes, TOPOLOGIES):
        r = results['results'][topo]
        samples = r['delta_star_bootstrap_samples']
        valid = [s for s in samples if s is not None]
        color = COLORS[topo]

        if len(valid) == 0:
            # Confounding: delta* undefined -- show centered message
            ax.text(
                0.5, 0.5,
                '$\\delta^*$ undefined\n(bias threshold never reached)',
                ha='center', va='center', transform=ax.transAxes,
                fontsize=9, style='italic', color='#666666',
                bbox=dict(
                    boxstyle='round,pad=0.4',
                    facecolor='#f5f5f5',
                    edgecolor='#cccccc',
                    linewidth=0.8,
                    alpha=0.9,
                ),
            )
            ax.set_title(TOPO_LABELS[topo], fontsize=11, fontweight='bold',
                         color=color)
            ax.set_xlabel('$\\delta^*$')
            ax.set_yticks([])
            ax.spines['left'].set_visible(False)
            continue

        arr = np.array(valid)
        point = r['delta_star_point']
        ci_lo = r['delta_star_ci_lower']
        ci_hi = r['delta_star_ci_upper']

        # Histogram
        ax.hist(
            arr, bins=40, color=color, alpha=0.65,
            edgecolor='white', linewidth=0.5, density=True,
        )

        # Point estimate vertical line
        ax.axvline(point, color='black', linewidth=1.2, linestyle='-',
                   zorder=5)

        # CI bounds as lighter dashed lines
        ax.axvline(ci_lo, color='#555555', linewidth=1.0, linestyle='--',
                   alpha=0.7, zorder=4)
        ax.axvline(ci_hi, color='#555555', linewidth=1.0, linestyle='--',
                   alpha=0.7, zorder=4)

        # CI shading
        ax.axvspan(ci_lo, ci_hi, alpha=0.08, color=color, zorder=1)

        # CI annotation in rounded box at top
        ax.annotate(
            f'95% CI: [{ci_lo:.3f}, {ci_hi:.3f}]',
            xy=(0.5, 0.95), xycoords='axes fraction',
            ha='center', va='top', fontsize=8,
            bbox=dict(
                boxstyle='round,pad=0.3',
                facecolor='white',
                edgecolor='#aaaaaa',
                linewidth=0.6,
                alpha=0.9,
            ),
        )

        ax.set_title(TOPO_LABELS[topo], fontsize=11, fontweight='bold',
                     color=color)
        ax.set_xlabel('$\\delta^*$')
        if topo == TOPOLOGIES[0]:
            ax.set_ylabel('Density')

    fig.suptitle(
        'Bootstrap Distribution of ASV $\\delta^*$ (B=1000)',
        fontsize=11, fontweight='bold', y=1.02,
    )
    fig.tight_layout()

    fig.savefig(OUT_PDF, bbox_inches='tight')
    fig.savefig(OUT_PNG, bbox_inches='tight')
    plt.close(fig)

    print(f"Saved: {OUT_PDF}")
    print(f"Saved: {OUT_PNG}")


if __name__ == '__main__':
    main()

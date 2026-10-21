"""Scale trajectory plot: Δ accuracy vs model scale (7B → 14B → 72B).

Shows that pruning safety is scale-invariant across model sizes.
Data points: Qwen-7B (10-seed oracle), 14B (offline oracle, single-run),
72B (placeholder, overridable via CLI).

Inputs:  --delta-72b, --ci-72b (command-line overrides for 72B data)
Output:  artifacts/paper/figures/scale_trajectory.{pdf,png}
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "artifacts" / "paper" / "figures"))
import paper_style

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

paper_style.apply_style()

C_BLUE   = '#0072B2'
C_GREEN  = '#009E73'
C_YELLOW = '#E69F00'
C_GRAY   = '#888888'

DEFAULT_OUT = str(Path(__file__).resolve().parents[1] /
                  'artifacts' / 'paper' / 'figures' / 'scale_trajectory.pdf')


def parse_args():
    p = argparse.ArgumentParser(
        description='Plot Δ accuracy vs model scale for pruning safety.')
    p.add_argument('--delta-7b', type=float, default=0.40,
                   help='Δ accuracy (pp) for 7B (default: +0.40)')
    p.add_argument('--sd-7b', type=float, default=1.02,
                   help='SD across seeds for 7B (default: 1.02)')
    p.add_argument('--n-7b', type=int, default=10,
                   help='Number of seeds for 7B (default: 10)')
    p.add_argument('--delta-14b', type=float, default=0.0,
                   help='Δ accuracy (pp) for 14B (default: 0.0)')
    p.add_argument('--mde-14b', type=float, default=1.5,
                   help='MDE proxy band for 14B single-run (default: ±1.5 pp)')
    p.add_argument('--delta-72b', type=float, default=0.0,
                   help='Δ accuracy (pp) for 72B (default: 0.0, placeholder)')
    p.add_argument('--ci-72b', type=float, default=None,
                   help='Half-width of 95%% CI for 72B (default: None = placeholder)')
    p.add_argument('--output', type=str, default=DEFAULT_OUT,
                   help='Output path (default: artifacts/paper/figures/scale_trajectory.pdf)')
    return p.parse_args()


def main():
    args = parse_args()
    out_pdf = Path(args.output)
    out_png = out_pdf.with_suffix('.png')

    # ── Data ─────────────────────────────────────────────────────────
    scales = [7, 14, 72]
    x_pos = np.arange(len(scales))

    # 7B: t-based CI
    t_crit = stats.t.ppf(0.975, df=args.n_7b - 1)
    ci_7b = args.sd_7b * t_crit / np.sqrt(args.n_7b)

    deltas = [args.delta_7b, args.delta_14b, args.delta_72b]
    ci_widths = [ci_7b, args.mde_14b, args.ci_72b]
    is_placeholder = [False, True, args.ci_72b is None]

    # ── Figure ───────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(5.0, 3.8))

    # Equivalence bands
    ax.axhspan(-1, 1, color=C_GREEN, alpha=0.15, zorder=0, label=r'$\pm$1 pp equivalence')
    ax.axhspan(-3, -1, color=C_YELLOW, alpha=0.10, zorder=0)
    ax.axhspan(1, 3, color=C_YELLOW, alpha=0.10, zorder=0, label=r'$\pm$3 pp non-inferiority')
    ax.axhline(0, color='#333333', linewidth=0.8, linestyle='--', zorder=1)

    for i, (xp, delta, ci_w, placeholder) in enumerate(
            zip(x_pos, deltas, ci_widths, is_placeholder)):

        if placeholder and ci_w is None:
            # 72B placeholder with no CI: open circle
            ax.plot(xp, delta, 'o', color=C_BLUE, markersize=10,
                    markerfacecolor='white', markeredgewidth=2.0, zorder=4)
            ax.annotate('placeholder', (xp, delta),
                        textcoords='offset points', xytext=(0, -18),
                        fontsize=7.5, color=C_GRAY, fontstyle='italic',
                        ha='center')
        elif placeholder:
            # 14B single-run: filled but with MDE proxy band (dashed whiskers)
            ax.errorbar(xp, delta, yerr=ci_w, fmt='o', color=C_BLUE,
                        markersize=10, markeredgecolor='white',
                        markeredgewidth=1.0, capsize=5, capthick=1.5,
                        elinewidth=1.5, linestyle='--', zorder=4)
            ax.annotate('MDE proxy', (xp, delta),
                        textcoords='offset points', xytext=(14, 8),
                        fontsize=7.5, color=C_GRAY, fontstyle='italic')
        else:
            # Normal data point with CI
            ax.errorbar(xp, delta, yerr=ci_w, fmt='o', color=C_BLUE,
                        markersize=10, markeredgecolor='white',
                        markeredgewidth=1.0, capsize=5, capthick=1.5,
                        elinewidth=1.5, zorder=4)

    # If 72B has CI, draw it
    if args.ci_72b is not None:
        i_72 = 2
        ax.errorbar(x_pos[i_72], args.delta_72b, yerr=args.ci_72b,
                     fmt='o', color=C_BLUE, markersize=10,
                     markeredgecolor='white', markeredgewidth=1.0,
                     capsize=5, capthick=1.5, elinewidth=1.5, zorder=4)
        # Remove placeholder marker (re-draw over)

    # ── Axes ─────────────────────────────────────────────────────────
    ax.set_xticks(x_pos)
    ax.set_xticklabels([f'{s}B' for s in scales], fontsize=11)
    ax.set_xlabel('Model Scale (parameters)', fontsize=11)
    ax.set_ylabel(r'$\Delta$ Accuracy (pp)', fontsize=11)
    ax.tick_params(axis='y', labelsize=10)

    y_lo = min(d - (c if c else 0) for d, c in zip(deltas, ci_widths))
    y_hi = max(d + (c if c else 0) for d, c in zip(deltas, ci_widths))
    margin = max(3.5, (y_hi - y_lo) * 0.4)
    ax.set_ylim(min(y_lo - margin, -3.8), max(y_hi + margin, 3.8))

    ax.legend(loc='upper right', fontsize=8, framealpha=0.9, edgecolor='#cccccc')

    fig.tight_layout()

    # ── Save ─────────────────────────────────────────────────────────
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(out_pdf))
    fig.savefig(str(out_png))
    plt.close()
    print(f'Saved {out_pdf}')
    print(f'Saved {out_png}')

    # ── Summary ──────────────────────────────────────────────────────
    print('\n--- Data summary ---')
    for s, d, c, ph in zip(scales, deltas, ci_widths, is_placeholder):
        tag = ' (placeholder)' if ph and c is None else ' (MDE)' if ph else ''
        ci_str = f'±{c:.2f}' if c is not None else 'n/a'
        print(f'  {s:>3d}B: Δ={d:+.2f} pp, 95% CI {ci_str}{tag}')


if __name__ == '__main__':
    main()

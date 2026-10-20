"""
plot_nll_distribution.py — KDE plot of token-level NLL by generation depth.

Input:  results/token_nll_by_depth.json
Output: results/fig_appendix_nll_distribution.pdf (.png)
"""

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

plt.rcParams.update({
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "mathtext.fontset": "cm",
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 7,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

DEPTH_COLORS = plt.cm.YlGnBu(np.linspace(0.2, 0.95, 5))


def main():
    root = Path(__file__).resolve().parent.parent
    data_path = root / "results" / "token_nll_by_depth.json"
    out_dir = root / "results"

    with open(data_path) as f:
        records = json.load(f)

    nll_by_depth = {d: [] for d in range(5)}
    for rec in records:
        d = rec["depth"]
        nll_by_depth[d].extend(rec["token_nlls"])

    for d in range(5):
        print(f"Depth {d}: {len(nll_by_depth[d])} tokens, "
              f"median={np.median(nll_by_depth[d]):.3f}, "
              f"mean={np.mean(nll_by_depth[d]):.3f}")

    fig, ax = plt.subplots(figsize=(3.5, 2.8))
    x_grid = np.linspace(0, 8, 500)

    for d in range(5):
        vals = np.array(nll_by_depth[d])
        vals = vals[vals < 10]
        kde = gaussian_kde(vals, bw_method=0.15)
        density = kde(x_grid)
        med = np.median(vals)
        label = f"Depth {d} (med={med:.2f})"
        ax.plot(x_grid, density, color=DEPTH_COLORS[d], linewidth=1.3, label=label)
        ax.axvline(med, color=DEPTH_COLORS[d], linestyle=":", linewidth=0.7, alpha=0.6)

    ax.set_xlabel("Token-level NLL (nats)")
    ax.set_ylabel("Density")
    ax.legend(frameon=False, loc="upper right")
    ax.set_xlim(0, 8)
    ax.set_ylim(bottom=0)

    fig.tight_layout()
    fig.savefig(out_dir / "fig_appendix_nll_distribution.pdf", dpi=300, bbox_inches="tight")
    fig.savefig(out_dir / "fig_appendix_nll_distribution.png", dpi=300, bbox_inches="tight")
    print(f"Saved to {out_dir}/fig_appendix_nll_distribution.{{pdf,png}}")
    plt.close()


if __name__ == "__main__":
    main()

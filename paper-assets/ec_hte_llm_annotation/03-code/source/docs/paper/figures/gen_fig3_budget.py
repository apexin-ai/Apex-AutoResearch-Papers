#!/usr/bin/env python3
"""Generate Figure A.3: RMSE vs Expert Budget (n) — 2x2 grid.

Data source: artifacts/exp-006/data/exp006_budget_sensitivity.csv
Output: figures/fig3_budget.{pdf,png}
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import pandas as pd
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[3]  # project root
DATA = ROOT / "artifacts" / "exp-006" / "data" / "exp006_budget_sensitivity.csv"
OUT_DIR = Path(__file__).resolve().parent
OUT_PDF = OUT_DIR / "fig3_budget.pdf"
OUT_PNG = OUT_DIR / "fig3_budget.png"

# ── Style ────────────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif", "STIXGeneral"],
    "mathtext.fontset": "cm",
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.titleweight": "bold",
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.08,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "lines.linewidth": 1.8,
    "axes.linewidth": 0.6,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
})

# ── Color palette (project-wide) ────────────────────────────────────────
METHOD_STYLE = {
    "global_corrected": {
        "color": "#8B4553", "marker": "o", "ls": "-",
        "label": "Global Corrected", "ms": 5, "zorder": 3,
    },
    "hb_ec_hte": {
        "color": "#1A6B6B", "marker": "^", "ls": "-",
        "label": "HB EC-HTE", "ms": 6, "zorder": 4,
    },
    "stratified_mle": {
        "color": "#D4880F", "marker": "s", "ls": "--",
        "label": "Stratified MLE", "ms": 5, "zorder": 2,
    },
}

METHODS = ["global_corrected", "hb_ec_hte", "stratified_mle"]

# ── Panel layout ─────────────────────────────────────────────────────────
PANELS = [
    ("extreme", 2, r"$K\!=\!2$, Extreme"),
    ("moderate", 2, r"$K\!=\!2$, Moderate"),
    ("extreme", 4, r"$K\!=\!4$, Extreme"),
    ("moderate", 4, r"$K\!=\!4$, Moderate"),
]


def compute_avg_rmse(df, regime, k):
    """Compute avg RMSE per method per n_expert.

    RMSE is averaged across subgroups and z_levels.
    Returns per-subgroup spread (min/max) for confidence bands.
    """
    sub = df[(df["regime"] == regime) & (df["k_subgroups"] == k)].copy()
    results = {}
    for method in METHODS:
        m = sub[sub["method"] == method]
        records = []
        for n in sorted(m["n_expert"].unique()):
            mn = m[m["n_expert"] == n]
            # Per-subgroup RMSE: average z0 and z1 within each subgroup
            sg_rmse = []
            for sg in mn["subgroup"].unique():
                sg_data = mn[mn["subgroup"] == sg]
                sg_rmse.append(np.mean([sg_data["rmse_z0"].values[0],
                                        sg_data["rmse_z1"].values[0]]))
            sg_rmse = np.array(sg_rmse)
            records.append({
                "n_expert": n,
                "rmse_mean": np.mean(sg_rmse),
                "rmse_lo": np.mean(sg_rmse) - np.std(sg_rmse),
                "rmse_hi": np.mean(sg_rmse) + np.std(sg_rmse),
            })
        results[method] = pd.DataFrame(records)
    return results


def find_crossover(results):
    """Find first n_expert where HB EC-HTE RMSE < Global Corrected RMSE."""
    gc = results["global_corrected"].set_index("n_expert")["rmse_mean"]
    hb = results["hb_ec_hte"].set_index("n_expert")["rmse_mean"]
    for n in sorted(gc.index):
        if hb.loc[n] < gc.loc[n]:
            return n
    return None


def main():
    df = pd.read_csv(DATA)
    fig, axes = plt.subplots(2, 2, figsize=(7.5, 5.0),
                             sharex=True, sharey=False)

    # Y-axis limits per row; row 1 (K=4) uses log scale
    YLIMS = {0: (0.04, 0.22), 1: (0.05, 1.1)}

    for idx, (regime, k, title) in enumerate(PANELS):
        row, col = idx // 2, idx % 2
        ax = axes[row, col]
        results = compute_avg_rmse(df, regime, k)
        crossover_n = find_crossover(results)

        for method in METHODS:
            sty = METHOD_STYLE[method]
            r = results[method]
            x = r["n_expert"].values
            y = r["rmse_mean"].values
            y_lo = r["rmse_lo"].values
            y_hi = r["rmse_hi"].values

            y_lo_clip = np.maximum(y_lo, 0.01)
            ax.fill_between(x, y_lo_clip, y_hi, alpha=0.10, color=sty["color"],
                            linewidth=0, zorder=1)
            ax.plot(x, y, color=sty["color"], marker=sty["marker"],
                    linestyle=sty["ls"], markersize=sty["ms"],
                    markeredgecolor="white", markeredgewidth=0.6,
                    label=sty["label"], zorder=sty["zorder"])

        ax.set_ylim(YLIMS[row])
        if row == 1:
            ax.set_yscale("log")
            ax.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
            ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
            ax.set_yticks([0.1, 0.2, 0.5, 1.0])
            ax.set_yticklabels(["0.1", "0.2", "0.5", "1.0"])

        # Crossover annotation
        if crossover_n is not None:
            ax.axvline(crossover_n, color="#888888", linestyle=":",
                       linewidth=0.9, zorder=1)
            y_top = YLIMS[row][1]
            txt = ax.text(
                crossover_n * 1.15, y_top * 0.92,
                f"$n\\!={crossover_n}$",
                fontsize=8, color="#555555", ha="left", va="top",
            )
            txt.set_path_effects(
                [pe.withStroke(linewidth=2.5, foreground="white")]
            )
        else:
            txt = ax.text(
                0.97, 0.95, "No crossover\n(Global always lower)",
                transform=ax.transAxes, fontsize=7.5, color="#999999",
                ha="right", va="top", fontstyle="italic",
                linespacing=1.3,
            )

        ax.set_title(title, pad=6)
        ax.set_xscale("log")
        ax.set_xticks([50, 100, 250, 500, 1000, 2000])
        ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
        ax.tick_params(axis="x", which="minor", bottom=False)
        ax.grid(True, alpha=0.15, linewidth=0.5, zorder=0)

    # Shared axis labels
    for ax in axes[1, :]:
        ax.set_xlabel(r"Expert budget ($n$)")
    for ax in axes[:, 0]:
        ax.set_ylabel("Avg RMSE")

    # Shared legend at top
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(
        handles, labels, loc="upper center",
        ncol=3, frameon=False,
        bbox_to_anchor=(0.5, 1.02),
        columnspacing=2.0, handletextpad=0.5,
    )

    plt.tight_layout(rect=[0, 0, 1, 0.94])
    plt.subplots_adjust(hspace=0.32, wspace=0.25)

    fig.savefig(OUT_PDF)
    fig.savefig(OUT_PNG)
    plt.close(fig)
    print(f"Saved: {OUT_PDF}")
    print(f"Saved: {OUT_PNG}")


if __name__ == "__main__":
    main()

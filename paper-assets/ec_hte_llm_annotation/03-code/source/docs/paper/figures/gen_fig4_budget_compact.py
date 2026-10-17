#!/usr/bin/env python3
"""Generate compact budget crossover figure (double column, 2 side-by-side panels)."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "artifacts" / "exp-006" / "data" / "exp006_budget_sensitivity.csv"
OUT_DIR = Path(__file__).resolve().parent

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
    "legend.fontsize": 8.5,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "lines.linewidth": 1.6,
    "axes.linewidth": 0.6,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

METHOD_STYLE = {
    "global_corrected": {
        "color": "#8B4553", "marker": "o", "ls": "-",
        "label": "Global", "ms": 5.5, "zorder": 3,
    },
    "hb_ec_hte": {
        "color": "#1A6B6B", "marker": "^", "ls": "-",
        "label": "EC-HTE", "ms": 6.5, "zorder": 4,
    },
    "stratified_mle": {
        "color": "#D4880F", "marker": "s", "ls": "--",
        "label": "Strat. MLE", "ms": 5.5, "zorder": 2,
    },
}
METHODS = ["global_corrected", "hb_ec_hte", "stratified_mle"]

PANELS = [
    ("extreme", 2, r"$K\!=\!2$, Extreme"),
    ("extreme", 4, r"$K\!=\!4$, Extreme"),
]


def compute_avg_rmse(df, regime, k):
    sub = df[(df["regime"] == regime) & (df["k_subgroups"] == k)].copy()
    results = {}
    for method in METHODS:
        m = sub[sub["method"] == method]
        records = []
        for n in sorted(m["n_expert"].unique()):
            mn = m[m["n_expert"] == n]
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
    gc = results["global_corrected"].set_index("n_expert")["rmse_mean"]
    hb = results["hb_ec_hte"].set_index("n_expert")["rmse_mean"]
    for n in sorted(gc.index):
        if hb.loc[n] < gc.loc[n]:
            return n
    return None


def main():
    df = pd.read_csv(DATA)
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.5), sharex=True)

    YLIMS = [(0.04, 0.22), (0.05, 1.1)]
    USE_LOG_Y = [False, True]

    for idx, (regime, k, title) in enumerate(PANELS):
        ax = axes[idx]
        results = compute_avg_rmse(df, regime, k)
        crossover_n = find_crossover(results)

        for method in METHODS:
            sty = METHOD_STYLE[method]
            r = results[method]
            x = r["n_expert"].values
            y = r["rmse_mean"].values
            y_lo = np.maximum(r["rmse_lo"].values, 0.01)
            y_hi = r["rmse_hi"].values

            ax.fill_between(x, y_lo, y_hi, alpha=0.10, color=sty["color"],
                            linewidth=0, zorder=1)
            ax.plot(x, y, color=sty["color"], marker=sty["marker"],
                    linestyle=sty["ls"], markersize=sty["ms"],
                    markeredgecolor="white", markeredgewidth=0.5,
                    label=sty["label"], zorder=sty["zorder"])

        ax.set_ylim(YLIMS[idx])
        if USE_LOG_Y[idx]:
            ax.set_yscale("log")
            ax.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
            ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
            ax.set_yticks([0.1, 0.2, 0.5, 1.0])
            ax.set_yticklabels(["0.1", "0.2", "0.5", "1.0"])

        if crossover_n is not None:
            ax.axvline(crossover_n, color="#888888", linestyle=":",
                       linewidth=0.8, zorder=1)
            txt = ax.text(
                crossover_n, YLIMS[idx][0] + (YLIMS[idx][1] - YLIMS[idx][0]) * 0.05,
                f"$n\\!={crossover_n}$",
                fontsize=8.5, color="#555555", ha="center", va="bottom",
            )
            txt.set_path_effects(
                [pe.withStroke(linewidth=2, foreground="white")])

        ax.set_title(title, pad=4)
        ax.set_xscale("log")
        ax.set_xticks([50, 100, 250, 500, 1000, 2000])
        ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
        ax.tick_params(axis="x", which="minor", bottom=False)
        ax.grid(True, alpha=0.15, linewidth=0.4, zorder=0)
        ax.set_ylabel("Avg RMSE")

    for ax in axes:
        ax.set_xlabel(r"Expert budget ($n_{\mathrm{expert}}$)")

    handles, labels = axes[0].get_legend_handles_labels()
    axes[0].legend(handles, labels, loc="upper right", frameon=True,
                   framealpha=0.9, edgecolor="none", fontsize=8.5)

    plt.tight_layout(w_pad=2.0)
    fig.savefig(OUT_DIR / "fig4_budget_compact.pdf")
    fig.savefig(OUT_DIR / "fig4_budget_compact.png")
    plt.close(fig)
    print("Saved fig4_budget_compact.{pdf,png}")


if __name__ == "__main__":
    main()

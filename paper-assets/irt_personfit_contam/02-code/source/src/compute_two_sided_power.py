"""Compute left-tail, right-tail, and two-sided detection rates from extended simulation data."""

import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BENCHMARK_COLORS = {
    "mmlu": "#1f77b4",
    "hellaswag": "#ff7f0e",
    "gsm8k": "#2ca02c",
    "arc_c": "#d62728",
    "humaneval": "#9467bd",
}

LEFT_CRIT = -1.6449
RIGHT_CRIT = 1.6449
TWO_SIDED_CRIT = 1.96

PROJECT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT / "artifacts" / "extended_simulation"


def compute_power(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (bm, cpct), g in df.groupby(["benchmark", "contamination_pct"]):
        lz = g["lz_star"].dropna()
        n = len(lz)
        if n == 0:
            continue
        rows.append({
            "benchmark": bm,
            "contamination_pct": cpct,
            "n_valid": n,
            "left_tail_rate": (lz < LEFT_CRIT).mean(),
            "right_tail_rate": (lz > RIGHT_CRIT).mean(),
            "two_sided_rate": (lz.abs() > TWO_SIDED_CRIT).mean(),
            "mean_lz_star": lz.mean(),
            "std_lz_star": lz.std(),
        })
    return pd.DataFrame(rows)


def plot_power_curves(power: pd.DataFrame, out_path: Path):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
    panels = [
        ("left_tail_rate", "Left-Tail Detection (lz* < −1.645)"),
        ("right_tail_rate", "Right-Tail Detection (lz* > +1.645)"),
        ("two_sided_rate", "Two-Sided Detection (|lz*| > 1.96)"),
    ]
    benchmarks = sorted(BENCHMARK_COLORS.keys())

    for ax, (col, title) in zip(axes, panels):
        for bm in benchmarks:
            sub = power[power["benchmark"] == bm].sort_values("contamination_pct")
            ax.plot(sub["contamination_pct"], sub[col],
                    marker="o", markersize=4, linewidth=1.8,
                    color=BENCHMARK_COLORS[bm], label=bm)
        ax.axhline(0.05, color="gray", linestyle="--", linewidth=0.8, label="α = 0.05")
        ax.set_xlabel("Contamination %")
        ax.set_title(title)
        ax.set_xlim(-2, 102)
        ax.set_ylim(-0.02, 1.02)
        ax.grid(True, alpha=0.3)

    axes[0].set_ylabel("Detection Rate")
    axes[2].legend(loc="upper left", fontsize=8, framealpha=0.9)
    fig.tight_layout()
    fig.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {out_path}")


def compute_dual_regime_summary(power: pd.DataFrame) -> dict:
    summary = {}
    for bm in sorted(BENCHMARK_COLORS.keys()):
        sub = power[power["benchmark"] == bm].sort_values("contamination_pct")
        means = sub.set_index("contamination_pct")["mean_lz_star"]

        crossover = None
        levels = means.index.tolist()
        for i in range(len(levels) - 1):
            if means[levels[i]] <= 0 < means[levels[i + 1]]:
                crossover = {"between": [int(levels[i]), int(levels[i + 1])]}
                break

        left_idx = sub["left_tail_rate"].idxmax()
        right_idx = sub["right_tail_rate"].idxmax()

        summary[bm] = {
            "crossover_point": crossover,
            "left_tail_peak_power": round(float(sub.loc[left_idx, "left_tail_rate"]), 4),
            "left_tail_peak_level": int(sub.loc[left_idx, "contamination_pct"]),
            "right_tail_peak_power": round(float(sub.loc[right_idx, "right_tail_rate"]), 4),
            "right_tail_peak_level": int(sub.loc[right_idx, "contamination_pct"]),
        }
    return summary


def main():
    csv_path = DATA_DIR / "simulation_detailed.csv"
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} rows from {csv_path}")

    power = compute_power(df)

    out_csv = DATA_DIR / "two_sided_power.csv"
    power.to_csv(out_csv, index=False)
    print(f"Saved {out_csv}")

    plot_power_curves(power, DATA_DIR / "two_sided_power_curves.png")

    summary = compute_dual_regime_summary(power)
    out_json = DATA_DIR / "dual_regime_summary.json"
    with open(out_json, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Saved {out_json}")

    print("\n=== Two-sided power table ===")
    pivot = power.pivot(index="contamination_pct", columns="benchmark", values="two_sided_rate")
    print(pivot.round(3).to_string())


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Analyze τ sweep results for provenance weight training experiments."""

import argparse
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

DEFAULT_UNIFORM_PPL = 17.693
DEFAULT_GRID_BEST_PPL = 17.646

DUMMY_DATA = {
    "0.5": {"eval_ppl": 17.72, "train_loss": 2.91},
    "0.6": {"eval_ppl": 17.69, "train_loss": 2.88},
    "0.7": {"eval_ppl": 17.66, "train_loss": 2.86},
    "0.8": {"eval_ppl": 17.651, "train_loss": 2.85},
    "0.9": {"eval_ppl": 17.67, "train_loss": 2.87},
    "0.95": {"eval_ppl": 17.71, "train_loss": 2.90},
}


def setup_style():
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
        "font.size": 9,
        "axes.labelsize": 10,
        "axes.titlesize": 10,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 8,
        "figure.figsize": (3.5, 2.6),
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.03,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": False,
        "lines.linewidth": 1.5,
        "lines.markersize": 5,
    })


def load_results(path):
    with open(path) as f:
        raw = json.load(f)
    results = {}
    for tau_str, metrics in raw.items():
        tau = float(tau_str)
        ppl = metrics.get("eval_ppl")
        if ppl is not None:
            results[tau] = {"eval_ppl": ppl, "train_loss": metrics.get("train_loss")}
    return results


def print_table(results, uniform_ppl, grid_best_ppl):
    taus = sorted(results.keys())
    print("\n| τ | eval_ppl | Δ vs uniform | Δ vs grid-best | % of grid-best impr. |")
    print("|---:|---:|---:|---:|---:|")
    grid_impr = uniform_ppl - grid_best_ppl
    for tau in taus:
        ppl = results[tau]["eval_ppl"]
        delta_uni = uniform_ppl - ppl
        delta_grid = grid_best_ppl - ppl
        pct = (delta_uni / grid_impr * 100) if grid_impr != 0 else float("nan")
        default_mark = " *" if abs(tau - 0.8) < 1e-9 else ""
        print(f"| {tau:.2f}{default_mark} | {ppl:.3f} | {delta_uni:+.3f} | {delta_grid:+.3f} | {pct:.1f}% |")
    print()


def plot_ppl_curve(results, out_prefix, uniform_ppl, grid_best_ppl):
    taus = sorted(results.keys())
    ppls = [results[t]["eval_ppl"] for t in taus]

    fig, ax = plt.subplots()
    ax.plot(taus, ppls, "o-", color="#2563EB", zorder=3)

    ax.axhline(uniform_ppl, ls="--", color="#6B7280", lw=1,
               label=f"uniform baseline ({uniform_ppl:.3f})")
    ax.axhline(grid_best_ppl, ls="--", color="#D97706", lw=1,
               label=f"grid-best ({grid_best_ppl:.3f})")

    if 0.8 in results:
        ax.axvline(0.8, ls=":", color="#9CA3AF", lw=0.8)
        ax.annotate("default\n(τ=0.8)", xy=(0.8, results[0.8]["eval_ppl"]),
                     xytext=(0.82, results[0.8]["eval_ppl"] + 0.015),
                     fontsize=7, color="#6B7280", ha="left")

    ax.set_xlabel("τ (quality threshold)")
    ax.set_ylabel("Eval perplexity")
    ax.set_xticks(taus)
    ax.set_xticklabels([f"{t:.2f}" for t in taus])
    ax.legend(loc="upper right", frameon=False)

    y_vals = ppls + [uniform_ppl, grid_best_ppl]
    y_min, y_max = min(y_vals), max(y_vals)
    margin = (y_max - y_min) * 0.25
    ax.set_ylim(y_min - margin, y_max + margin)

    fig.savefig(f"{out_prefix}.pdf")
    fig.savefig(f"{out_prefix}.png")
    plt.close(fig)
    print(f"Saved {out_prefix}.pdf and {out_prefix}.png")


def plot_improvement_curve(results, out_prefix, uniform_ppl, grid_best_ppl):
    taus = sorted(results.keys())
    improvements = [uniform_ppl - results[t]["eval_ppl"] for t in taus]

    fig, ax = plt.subplots()
    ax.plot(taus, improvements, "s-", color="#2563EB", zorder=3)
    ax.axhline(0, ls="-", color="#D1D5DB", lw=0.8)

    grid_impr = uniform_ppl - grid_best_ppl
    ax.axhline(grid_impr, ls="--", color="#D97706", lw=1,
               label=f"grid-best improvement ({grid_impr:.3f})")

    if 0.8 in results:
        ax.axvline(0.8, ls=":", color="#9CA3AF", lw=0.8)

    ax.set_xlabel("τ (quality threshold)")
    ax.set_ylabel("Δ PPL (uniform − τ-weighted)")
    ax.set_xticks(taus)
    ax.set_xticklabels([f"{t:.2f}" for t in taus])
    ax.legend(loc="upper right", frameon=False)

    y_vals = improvements + [0, grid_impr]
    y_min, y_max = min(y_vals), max(y_vals)
    margin = (y_max - y_min) * 0.25
    ax.set_ylim(y_min - margin, y_max + margin)

    fig.savefig(f"{out_prefix}.pdf")
    fig.savefig(f"{out_prefix}.png")
    plt.close(fig)
    print(f"Saved {out_prefix}.pdf and {out_prefix}.png")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze τ sweep results: plot PPL curves and print summary table.")
    parser.add_argument("--input", "-i", type=str, default=None,
                        help="JSON file with τ sweep results. Keys are τ values, "
                             "values have 'eval_ppl' and optional 'train_loss'.")
    parser.add_argument("--outdir", "-o", type=str, default=".",
                        help="Output directory for figures (default: current dir)")
    parser.add_argument("--dummy", action="store_true",
                        help="Use dummy data for testing")
    parser.add_argument("--uniform-ppl", type=float, default=DEFAULT_UNIFORM_PPL,
                        help=f"Uniform baseline PPL (default: {DEFAULT_UNIFORM_PPL})")
    parser.add_argument("--grid-best-ppl", type=float, default=DEFAULT_GRID_BEST_PPL,
                        help=f"Grid-best PPL (default: {DEFAULT_GRID_BEST_PPL})")
    args = parser.parse_args()

    uniform_ppl = args.uniform_ppl
    grid_best_ppl = args.grid_best_ppl

    if args.dummy:
        results = {float(k): v for k, v in DUMMY_DATA.items()}
    elif args.input:
        results = load_results(args.input)
    else:
        parser.print_help()
        sys.exit(1)

    if not results:
        print("ERROR: no valid data points (all eval_ppl are null?)", file=sys.stderr)
        sys.exit(1)

    setup_style()
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    suffix = "_dummy" if args.dummy else ""
    plot_ppl_curve(results, str(outdir / f"tau_sweep_curve{suffix}"),
                   uniform_ppl, grid_best_ppl)
    plot_improvement_curve(results, str(outdir / f"tau_sweep_improvement{suffix}"),
                           uniform_ppl, grid_best_ppl)
    print_table(results, uniform_ppl, grid_best_ppl)


if __name__ == "__main__":
    main()

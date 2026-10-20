#!/usr/bin/env python3
"""Visualize prism collapse mixing signals across generations."""

import argparse
import json
import glob
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from scipy.stats import gaussian_kde


# ── Style ────────────────────────────────────────────────────────────────────

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 10,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.color": "#cccccc",
    "grid.linestyle": ":",
    "grid.linewidth": 0.5,
})

LINE_WIDTH = 2.0
MARKER_SIZE = 8
SEED_STYLES = {
    42:  {"color": "tab:blue",   "marker": "o", "label": "seed 42"},
    137: {"color": "tab:orange", "marker": "s", "label": "seed 137"},
}
MEAN_STYLE = {"color": "black", "marker": "^", "linestyle": "--", "label": "mean"}


# ── Data loading ─────────────────────────────────────────────────────────────

def load_signals(results_dir: str, seeds: list[int]) -> dict:
    """Load all signal JSON files, keyed by (gen, seed)."""
    data = {}
    pattern = os.path.join(results_dir, "signals_gen*_seed*.json")
    for path in sorted(glob.glob(pattern)):
        with open(path) as f:
            d = json.load(f)
        gen, seed = d["gen"], d["seed"]
        if seed in seeds:
            data[(gen, seed)] = d
    return data


def get_gens_and_seeds(data: dict) -> tuple[list[int], list[int]]:
    gens = sorted({k[0] for k in data})
    seeds = sorted({k[1] for k in data})
    return gens, seeds


# ── Figure A: ρ(loss, entropy) decay ─────────────────────────────────────────

def plot_rho_decay(data: dict, gens: list[int], seeds: list[int], output_dir: str):
    fig, ax = plt.subplots(figsize=(6, 4))

    seed_rhos = {}
    for seed in seeds:
        rhos = [data[(g, seed)]["correlations"]["rho_loss_entropy"]
                for g in gens if (g, seed) in data]
        gs = [g for g in gens if (g, seed) in data]
        seed_rhos[seed] = (gs, rhos)
        s = SEED_STYLES.get(seed, {"color": "gray", "marker": "D", "label": f"seed {seed}"})
        ax.plot(gs, rhos, color=s["color"], marker=s["marker"],
                linewidth=LINE_WIDTH, markersize=MARKER_SIZE, label=s["label"])

    # Mean line
    if len(seeds) > 1:
        mean_rhos = []
        common_gens = sorted(set.intersection(*[set(gs) for gs, _ in seed_rhos.values()]))
        for g in common_gens:
            vals = [data[(g, s)]["correlations"]["rho_loss_entropy"]
                    for s in seeds if (g, s) in data]
            mean_rhos.append(np.mean(vals))
        ax.plot(common_gens, mean_rhos, **MEAN_STYLE,
                linewidth=LINE_WIDTH, markersize=MARKER_SIZE)

    # Threshold lines
    ax.axhline(0.7, color="green", linestyle="--", linewidth=1.2, alpha=0.7)
    ax.text(gens[-1] + 0.05, 0.7, "Gen 0-1 threshold", va="center",
            fontsize=9, color="green")
    ax.axhline(0.5, color="red", linestyle="--", linewidth=1.2, alpha=0.7)
    ax.text(gens[-1] + 0.05, 0.5, "Gen 3 threshold", va="center",
            fontsize=9, color="red")

    ax.set_xlabel("Generation")
    ax.set_ylabel("Spearman ρ(loss, entropy)")
    ax.set_title("ρ(loss, entropy) Decay Across Generations")
    ax.set_xticks(gens)
    ax.legend(loc="upper right")
    ax.set_ylim(0, 1.05)

    out = os.path.join(output_dir, "fig_rho_decay.pdf")
    fig.savefig(out)
    plt.close(fig)
    print(f"  → {out}")


# ── Figure B: Corpus-level trends (2×2) ─────────────────────────────────────

def _plot_trend(ax, data, gens, seeds, key_fn, ylabel, title):
    """Helper: plot per-seed lines + mean for a scalar metric."""
    for seed in seeds:
        gs = [g for g in gens if (g, seed) in data]
        vals = [key_fn(data[(g, seed)]) for g in gs]
        s = SEED_STYLES.get(seed, {"color": "gray", "marker": "D", "label": f"seed {seed}"})
        ax.plot(gs, vals, color=s["color"], marker=s["marker"],
                linewidth=LINE_WIDTH, markersize=MARKER_SIZE, label=s["label"])

    if len(seeds) > 1:
        common = sorted(set.intersection(*[
            {g for g in gens if (g, s) in data} for s in seeds]))
        means = [np.mean([key_fn(data[(g, s)]) for s in seeds]) for g in common]
        ax.plot(common, means, **MEAN_STYLE, linewidth=LINE_WIDTH, markersize=MARKER_SIZE)

    ax.set_xlabel("Generation")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(gens)


def plot_corpus_trends(data: dict, gens: list[int], seeds: list[int], output_dir: str):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    _plot_trend(axes[0, 0], data, gens, seeds,
                lambda d: d["aggregated"]["entropy_mean"],
                "Entropy (mean)", "Entropy Mean")

    _plot_trend(axes[0, 1], data, gens, seeds,
                lambda d: d["corpus_level"]["sigma_spectral_rank"],
                "σ(spectral rank)", "Corpus σ Spectral Rank")

    # Distinct-n: 3 lines per seed, but use seed=42 only to avoid clutter
    ax = axes[1, 0]
    for n, ls in [(1, "-"), (2, "--"), (3, ":")]:
        key = f"distinct_{n}"
        for seed in seeds:
            gs = [g for g in gens if (g, seed) in data]
            vals = [data[(g, seed)]["corpus_level"][key] for g in gs]
            s = SEED_STYLES.get(seed, {"color": "gray"})
            ax.plot(gs, vals, color=s["color"], linestyle=ls,
                    marker=s.get("marker", "D"),
                    linewidth=LINE_WIDTH, markersize=MARKER_SIZE,
                    label=f"distinct-{n} (s{seed})")
    ax.set_xlabel("Generation")
    ax.set_ylabel("Distinct-n")
    ax.set_title("Distinct-n Trends")
    ax.set_xticks(gens)
    ax.legend(fontsize=8, ncol=2)

    _plot_trend(axes[1, 1], data, gens, seeds,
                lambda d: d["aggregated"]["loss_mean"],
                "Loss (mean)", "Loss Mean")

    # Single legend for panels that share seed styles (skip distinct panel)
    for ax in [axes[0, 0], axes[0, 1], axes[1, 1]]:
        ax.legend(fontsize=9)

    fig.tight_layout()
    out = os.path.join(output_dir, "fig_corpus_trends.pdf")
    fig.savefig(out)
    plt.close(fig)
    print(f"  → {out}")


# ── Figure C: Per-example distributions (2×2) ───────────────────────────────

def plot_signal_distributions(data: dict, gens: list[int], seed: int, output_dir: str):
    cmap = plt.cm.viridis
    gen_colors = {g: cmap(i / max(len(gens) - 1, 1)) for i, g in enumerate(gens)}

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle(f"Per-Example Signal Distributions (seed={seed})", fontsize=14, y=1.01)

    # KDE panels
    for ax, metric, title in [
        (axes[0, 0], "loss",          "Loss"),
        (axes[0, 1], "entropy",       "Entropy"),
        (axes[1, 0], "spectral_rank", "Spectral Rank"),
    ]:
        for g in gens:
            if (g, seed) not in data:
                continue
            vals = np.array(data[(g, seed)]["per_example"][metric])
            if len(vals) < 2:
                continue
            kde = gaussian_kde(vals)
            x = np.linspace(vals.min(), vals.max(), 300)
            ax.plot(x, kde(x), color=gen_colors[g], linewidth=LINE_WIDTH,
                    label=f"Gen {g}")
            ax.fill_between(x, kde(x), alpha=0.12, color=gen_colors[g])
        ax.set_xlabel(title)
        ax.set_ylabel("Density")
        ax.set_title(f"{title} Distribution")
        ax.legend(fontsize=9)

    # Scatter: loss vs entropy (Gen 0 blue, Gen 3 red; fall back to last gen)
    ax = axes[1, 1]
    scatter_gens = []
    if (gens[0], seed) in data:
        scatter_gens.append((gens[0], "tab:blue"))
    if len(gens) > 1 and (gens[-1], seed) in data:
        scatter_gens.append((gens[-1], "tab:red"))
    elif len(scatter_gens) == 0 and (gens[0], seed) in data:
        scatter_gens.append((gens[0], "tab:blue"))

    for g, c in scatter_gens:
        loss = np.array(data[(g, seed)]["per_example"]["loss"])
        ent = np.array(data[(g, seed)]["per_example"]["entropy"])
        n = min(500, len(loss))
        idx = np.random.default_rng(seed).choice(len(loss), n, replace=False)
        ax.scatter(loss[idx], ent[idx], c=c, s=8, alpha=0.5, label=f"Gen {g}")

    ax.set_xlabel("Loss")
    ax.set_ylabel("Entropy")
    ax.set_title("Loss vs Entropy")
    ax.legend(fontsize=9)

    fig.tight_layout()
    out = os.path.join(output_dir, "fig_signal_distributions.pdf")
    fig.savefig(out)
    plt.close(fig)
    print(f"  → {out}")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Plot prism collapse mixing signal diagnostics.")
    parser.add_argument("--results_dir", default="results/",
                        help="Directory containing signals_gen*_seed*.json")
    parser.add_argument("--seeds", default="42,137",
                        help="Comma-separated seed list (default: 42,137)")
    parser.add_argument("--output_dir", default="results/",
                        help="Output directory for PDF figures")
    args = parser.parse_args()

    seeds = [int(s) for s in args.seeds.split(",")]
    os.makedirs(args.output_dir, exist_ok=True)

    data = load_signals(args.results_dir, seeds)
    if not data:
        print(f"ERROR: No signal files found in {args.results_dir}", file=sys.stderr)
        sys.exit(1)

    gens, found_seeds = get_gens_and_seeds(data)
    print(f"Found {len(data)} files: gens={gens}, seeds={found_seeds}")

    plot_rho_decay(data, gens, found_seeds, args.output_dir)
    plot_corpus_trends(data, gens, found_seeds, args.output_dir)
    plot_signal_distributions(data, gens, seeds[0], args.output_dir)

    print("Done.")


if __name__ == "__main__":
    main()

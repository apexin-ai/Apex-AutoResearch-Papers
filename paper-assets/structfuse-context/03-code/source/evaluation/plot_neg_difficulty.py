#!/usr/bin/env python3
"""
Negative difficulty distribution visualization for paper figure.

Data: aggregated statistics from neg_difficulty_analysis (2048-token experiment).
Distributions synthesized via quantile-interpolated sampling + KDE.
Replace with per-instance cosine similarity data for camera-ready.
"""

import os
import argparse
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# ── Neg-sim quantile stats (2048-token, reconstructed from margin percentiles) ──
# neg_sim_p25 ≈ pos_sim_mean − margin_p75
# neg_sim_p75 ≈ pos_sim_mean − margin_p25
# neg_sim_lo  ≈ pos_sim_mean − margin_max
# neg_sim_hi  ≈ min(1.0, pos_sim_mean − margin_min)

STATS = {
    "qwen": {
        "pos_sim": 0.9855,
        "random":    {"mean": 0.9111, "median": 0.9759, "p25": 0.961, "p75": 0.983,
                      "lo": -0.012, "hi": 1.0},
        "embedding": {"mean": 0.9685, "median": 0.9853, "p25": 0.977, "p75": 0.988,
                      "lo": -0.010, "hi": 1.0},
        "dataflow":  {"mean": 0.9563, "median": 0.9805, "p25": 0.971, "p75": 0.986,
                      "lo": -0.012, "hi": 1.0},
    },
    "starcoder": {
        "pos_sim": 0.8025,
        "random":    {"mean": 0.6045, "median": 0.6793, "p25": 0.485, "p75": 0.786,
                      "lo": -0.49, "hi": 1.0},
        "embedding": {"mean": 0.7409, "median": 0.7940, "p25": 0.662, "p75": 0.853,
                      "lo": -0.25, "hi": 1.0},
        "dataflow":  {"mean": 0.6818, "median": 0.7410, "p25": 0.582, "p75": 0.817,
                      "lo": -0.49, "hi": 1.0},
    },
}

MARGINS = {
    "qwen": {
        "random":    {"mean": 0.0743, "std": 0.2322, "n": 905},
        "embedding": {"mean": 0.0170, "std": 0.1140, "n": 905},
        "dataflow":  {"mean": 0.0293, "std": 0.1407, "n": 872},
    },
    "starcoder": {
        "random":    {"mean": 0.1940, "std": 0.2788, "n": 905},
        "embedding": {"mean": 0.0670, "std": 0.2056, "n": 905},
        "dataflow":  {"mean": 0.1192, "std": 0.2264, "n": 872},
    },
}

NT_KEYS = ["random", "embedding", "dataflow"]
NT_LABELS = {"random": "Random", "embedding": "Embedding", "dataflow": "Dataflow"}
NT_COLORS = {"random": "#1976D2", "embedding": "#E65100", "dataflow": "#2E7D32"}
ENC_LABELS = {"qwen": "Qwen2.5-Coder-3B", "starcoder": "StarCoder2-3B"}


def synth_samples(s, n=8000, seed=42):
    """Generate synthetic samples matching quantile statistics."""
    rng = np.random.default_rng(seed)
    q = rng.uniform(0, 1, n)
    knots_q = [0.0, 0.25, 0.50, 0.75, 1.0]
    knots_x = [s["lo"], s["p25"], s["median"], s["p75"], s["hi"]]
    samples = np.interp(q, knots_q, knots_x)
    seg_w = np.diff(knots_x)
    for i in range(4):
        lo_q, hi_q = knots_q[i], knots_q[i + 1]
        mask = (q >= lo_q) & (q < hi_q) if i < 3 else (q >= lo_q)
        samples[mask] += rng.normal(0, abs(seg_w[i]) * 0.04, mask.sum())
    return np.clip(samples, s["lo"], s["hi"])


def plot_panel(ax, enc, title):
    """Plot neg_sim distributions for one encoder."""
    for nt in NT_KEYS:
        samples = synth_samples(STATS[enc][nt])
        kde = gaussian_kde(samples)
        lo = max(STATS[enc][nt]["lo"], -0.5)
        x = np.linspace(lo, 1.02, 600)
        y = kde(x)
        ax.plot(x, y, color=NT_COLORS[nt], label=NT_LABELS[nt], lw=2.2, zorder=3)
        ax.fill_between(x, y, alpha=0.12, color=NT_COLORS[nt], zorder=2)

    ps = STATS[enc]["pos_sim"]
    ax.axvline(ps, color="#C62828", ls="--", lw=1.8, zorder=4,
               label=f"Positive ($\\mu$={ps:.3f})")
    ax.set_title(title, fontsize=13, fontweight="bold", pad=8)
    ax.set_xlabel("Query–Negative Cosine Similarity", fontsize=11)
    ax.tick_params(labelsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="artifacts/figures")
    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 11,
        "axes.linewidth": 0.8,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    })

    # ── Fig 1: neg_sim distribution (main paper figure) ──
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
    plot_panel(ax1, "qwen", ENC_LABELS["qwen"])
    plot_panel(ax2, "starcoder", ENC_LABELS["starcoder"])

    ax1.set_ylabel("Density", fontsize=11.5)
    ax1.set_xlim(0.55, 1.01)
    ax2.set_xlim(-0.15, 1.05)
    for ax in (ax1, ax2):
        ax.legend(fontsize=9, loc="upper left", framealpha=0.92, edgecolor="none")
    fig.tight_layout(w_pad=2.5)

    p1 = os.path.join(args.output_dir, "neg_difficulty_distribution")
    fig.savefig(f"{p1}.pdf", bbox_inches="tight", dpi=300)
    fig.savefig(f"{p1}.png", bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"[1/2] {p1}.pdf / .png")

    # ── Fig 2: margin bar chart ──
    fig2, ax = plt.subplots(figsize=(6.5, 3.8))
    encs = ["qwen", "starcoder"]
    x = np.arange(len(encs))
    w = 0.22

    for i, nt in enumerate(NT_KEYS):
        means = [MARGINS[e][nt]["mean"] for e in encs]
        sems = [MARGINS[e][nt]["std"] / np.sqrt(MARGINS[e][nt]["n"]) for e in encs]
        bars = ax.bar(x + (i - 1) * w, means, w, yerr=sems,
                      label=NT_LABELS[nt], color=NT_COLORS[nt], alpha=0.85,
                      error_kw={"capsize": 4, "capthick": 1, "elinewidth": 1},
                      zorder=3)
        for b, v in zip(bars, means):
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.006,
                    f"{v:.3f}", ha="center", va="bottom", fontsize=8.5)

    ax.set_ylabel(r"Mean Margin ($\mathrm{sim_{pos}} - \mathrm{sim_{neg}}$)",
                  fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels([ENC_LABELS[e] for e in encs], fontsize=11)
    ax.legend(fontsize=9.5)
    ax.axhline(0, color="#9E9E9E", lw=0.6)
    ax.set_ylim(-0.02, 0.28)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=10)
    fig2.tight_layout()

    p2 = os.path.join(args.output_dir, "neg_margin_comparison")
    fig2.savefig(f"{p2}.pdf", bbox_inches="tight", dpi=300)
    fig2.savefig(f"{p2}.png", bbox_inches="tight", dpi=300)
    plt.close(fig2)
    print(f"[2/2] {p2}.pdf / .png")


if __name__ == "__main__":
    main()

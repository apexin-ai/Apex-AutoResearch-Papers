#!/usr/bin/env python3
"""Figure 3: two-panel K*(theta) figure.

Panel (a): Pairwise AUC profile across depth pairs (C4 configs)
Panel (b): K*(theta) sensitivity

Output: docs/paper/figures/fig_kstar_theta.pdf
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

PAIR_KEYS = ["0v1", "1v2", "2v3", "3v4", "4v5"]

MODELS = {
    "Qwen-rw": {
        "mean":     [0.9956, 0.6955, 0.5893, 0.5435, 0.5340],
        "ci_lower": [0.9946, 0.6859, 0.5795, 0.5333, 0.5238],
        "ci_upper": [0.9976, 0.7041, 0.5991, 0.5551, 0.5448],
    },
    "Pythia": {
        "mean":     [0.9722, 0.6074, 0.5440, 0.5051, 0.5079],
        "ci_lower": [0.9670, 0.5975, 0.5340, 0.4950, 0.4980],
        "ci_upper": [0.9770, 0.6172, 0.5540, 0.5150, 0.5180],
    },
    "OLMo": {
        "mean":     [0.9861, 0.5001, 0.4973, 0.5034, 0.4971],
        "ci_lower": [0.9840, 0.4960, 0.4860, 0.4920, 0.4840],
        "ci_upper": [0.9890, 0.5190, 0.5090, 0.5130, 0.5050],
    },
    "Qwen-cont": {
        "mean":     [0.9971, 0.6112, 0.5609, 0.5409, 0.5141],
        "ci_lower": [0.9963, 0.6015, 0.5511, 0.5308, 0.5035],
        "ci_upper": [0.9978, 0.6213, 0.5712, 0.5508, 0.5255],
    },
    "Qwen-7B": {
        "mean":     [0.9644, 0.6178, 0.5492, 0.5276, 0.5085],
        "ci_lower": [0.9610, 0.6079, 0.5390, 0.5180, 0.4990],
        "ci_upper": [0.9665, 0.6261, 0.5594, 0.5380, 0.5190],
    },
}

TABLEAU = [
    "#4e79a7", "#e15759", "#76b7b2", "#59a14f", "#b07aa1",
    "#ff9da7", "#9c755f", "#bab0ac", "#edc948", "#f28e2b",
]
MARKERS = ["o", "s", "^", "D", "v", "P", "X", "*", "h", "<"]


def compute_kstar(ci_lowers, theta):
    k = 0
    for v in ci_lowers:
        if v >= theta:
            k += 1
        else:
            break
    return k


def main():
    x = np.arange(len(PAIR_KEYS))
    thetas = np.arange(0.50, 0.751, 0.005)

    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 10,
        "axes.linewidth": 0.8,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.major.width": 0.8,
        "ytick.major.width": 0.8,
    })

    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(10, 3.5),
                                      gridspec_kw={"width_ratios": [1, 1.15]})

    # ── Panel (a): Pairwise AUC profile ─────────────────────────────────
    ax_a.axhline(0.60, color="grey", ls="--", lw=0.8, zorder=1)
    ax_a.text(4.05, 0.607, r"$\theta = 0.60$", fontsize=8, color="grey",
              va="bottom", ha="right")

    ax_a.axvspan(1.5, 2.5, color="#4e79a7", alpha=0.06, zorder=0)
    ax_a.annotate(r"$K^*\!=\!2$", xy=(1.7, 0.68), fontsize=8, color="#4e79a7",
                  alpha=0.7)

    for i, (name, data) in enumerate(MODELS.items()):
        color = TABLEAU[i % len(TABLEAU)]
        marker = MARKERS[i % len(MARKERS)]
        means = data["mean"]
        lo = data["ci_lower"]
        hi = data["ci_upper"]

        ax_a.fill_between(x, lo, hi, color=color, alpha=0.15, linewidth=0)
        ax_a.plot(x, means, "-", color=color, lw=1.6, marker=marker,
                  markersize=4.5, label=name, zorder=3)

    ax_a.set_xticks(x)
    ax_a.set_xticklabels(PAIR_KEYS)
    ax_a.set_xlabel("Depth pair")
    ax_a.set_ylabel("Pairwise AUC")
    ax_a.set_ylim(0.47, 1.02)
    ax_a.set_xlim(-0.25, len(PAIR_KEYS) - 0.75)
    ax_a.legend(fontsize=7.5, loc="upper right", framealpha=0.92,
                edgecolor="0.85", handlelength=2.0)
    ax_a.set_title(r"$\bf{(a)}$" + " Pairwise AUC profile", fontsize=10,
                   loc="left", pad=6)

    # ── Panel (b): K*(θ) sensitivity ────────────────────────────────────
    all_kstar = {}
    for name, data in MODELS.items():
        ci_lo = data["ci_lower"]
        ks = [compute_kstar(ci_lo, t) for t in thetas]
        all_kstar[name] = ks

    kstar_arr = np.array(list(all_kstar.values()))
    k_min = kstar_arr.min(axis=0)
    k_max = kstar_arr.max(axis=0)

    mask_23 = (k_min >= 2) & (k_max <= 3) & (k_min != k_max)
    mask_2  = (k_min == 2) & (k_max == 2)

    for j in range(len(thetas)):
        if mask_23[j]:
            ax_b.axvspan(thetas[j] - 0.0025, thetas[j] + 0.0025,
                         color="#cccccc", alpha=0.5, linewidth=0, zorder=0)
        if mask_2[j]:
            ax_b.axvspan(thetas[j] - 0.0025, thetas[j] + 0.0025,
                         color="#b8d4e3", alpha=0.5, linewidth=0, zorder=0)

    for i, (name, ks) in enumerate(all_kstar.items()):
        color = TABLEAU[i % len(TABLEAU)]
        ax_b.step(thetas, ks, where="post", label=name,
                  linewidth=1.6, color=color)

    ax_b.axvline(x=0.60, color="grey", ls="--", lw=0.8, alpha=0.7)
    ax_b.text(0.605, 5.15, r"$\theta=0.60$", color="grey", fontsize=8,
              va="top")

    import matplotlib.patches as mpatches
    legend_patches = [
        mpatches.Patch(color="#cccccc", alpha=0.5, label=r"$K^*\!\in\!\{2,3\}$ (all models)"),
        mpatches.Patch(color="#b8d4e3", alpha=0.5, label=r"$K^*\!=\!2$ (all models)"),
    ]
    handles_lines = []
    for i, name in enumerate(all_kstar.keys()):
        color = TABLEAU[i % len(TABLEAU)]
        h = plt.Line2D([0], [0], color=color, lw=1.6, label=name)
        handles_lines.append(h)

    ax_b.legend(handles=legend_patches + handles_lines, fontsize=7.5,
                loc="upper right", framealpha=0.92, edgecolor="0.85")

    ax_b.set_xlabel(r"Threshold $\theta$")
    ax_b.set_ylabel(r"$K^*(\theta)$")
    ax_b.set_xlim(0.495, 0.755)
    max_k = max(len(v) for v in MODELS.values())
    ax_b.set_ylim(-0.2, max_k + 0.5)
    ax_b.set_yticks(range(max_k + 1))
    ax_b.grid(axis="y", color="#e0e0e0", linewidth=0.5)
    ax_b.set_title(r"$\bf{(b)}$" + r" $K^*(\theta)$ sensitivity", fontsize=10,
                   loc="left", pad=6)

    fig.tight_layout()

    out_dir = Path(__file__).resolve().parent.parent / "docs" / "paper" / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "fig_kstar_theta.pdf"

    fig.savefig(out_path, bbox_inches="tight")
    fig.savefig(out_path.with_suffix(".png"), bbox_inches="tight", dpi=300)
    plt.close(fig)

    print(f"Models: {list(MODELS.keys())}")
    print(f"Saved: {out_path}")
    pdf_size = out_path.stat().st_size
    assert pdf_size > 3 * 1024, f"PDF too small: {pdf_size}"
    print("OK")


if __name__ == "__main__":
    main()

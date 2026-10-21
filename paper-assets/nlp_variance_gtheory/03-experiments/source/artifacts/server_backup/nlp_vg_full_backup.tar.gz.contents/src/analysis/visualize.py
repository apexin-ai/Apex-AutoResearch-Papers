"""Visualization for G-theory variance decomposition results.

Generates three publication-quality figures:
  1. Horizontal bar chart of variance components (% of total variance).
  2. Lower-triangle heatmap of 2-way interaction magnitudes.
  3. D-study curves — G coefficient vs replications per random facet.

Input:
    - ``variance_components.json`` (from ``variance_decomposition.py``)
    - ``d_study_results.json``     (from ``d_study.py``)

Output: PNG files in ``results/figures/``.
"""

import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Patch

ALL_FACETS = [
    "precision", "temperature",
    "prompt_template", "seed", "ordering", "item_id",
]

FACET_LABELS = {
    "precision": "Precision",
    "temperature": "Temperature",
    "prompt_template": "Prompt",
    "seed": "Seed",
    "ordering": "Ordering",
    "item_id": "Item",
    "residual": "Residual",
}

FIXED_FACETS = {"precision", "temperature"}

PALETTE = {
    "fixed": "#d62728",
    "random": "#2ca02c",
    "interaction": "#1f77b4",
    "residual": "#7f7f7f",
}


def _component_color(name: str) -> str:
    if name == "residual":
        return PALETTE["residual"]
    if ":" in name:
        return PALETTE["interaction"]
    if name in FIXED_FACETS:
        return PALETTE["fixed"]
    return PALETTE["random"]


def _pretty(name: str) -> str:
    if ":" in name:
        parts = name.split(":")
        return " × ".join(FACET_LABELS.get(p, p) for p in parts)
    return FACET_LABELS.get(name, name)


# ---- Figure 1: variance component bar chart --------------------------------

def plot_variance_components(vc: dict, output_path: str) -> None:
    components = {k: v["estimate"] for k, v in vc.items()}
    total = sum(components.values())
    sorted_items = sorted(components.items(), key=lambda x: -x[1])

    names = [_pretty(k) for k, _ in sorted_items]
    pcts = [v / total * 100 for _, v in sorted_items]
    colors = [_component_color(k) for k, _ in sorted_items]

    fig, ax = plt.subplots(figsize=(10, max(6, len(names) * 0.45)))
    bars = ax.barh(
        range(len(names)), pcts,
        color=colors, edgecolor="white", linewidth=0.5,
    )
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=10)
    ax.set_xlabel("Variance Explained (%)", fontsize=11)
    ax.set_title("G-theory Variance Components", fontsize=13, pad=12)
    ax.invert_yaxis()

    for bar, pct in zip(bars, pcts):
        if pct > 1.5:
            ax.text(
                bar.get_width() + 0.5,
                bar.get_y() + bar.get_height() / 2,
                f"{pct:.1f}%", va="center", fontsize=9,
            )

    legend_elements = [
        Patch(facecolor=PALETTE["fixed"], label="Fixed facets"),
        Patch(facecolor=PALETTE["random"], label="Random facets"),
        Patch(facecolor=PALETTE["interaction"], label="Interactions"),
        Patch(facecolor=PALETTE["residual"], label="Residual"),
    ]
    ax.legend(handles=legend_elements, loc="lower right", fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  → {output_path}")


# ---- Figure 2: interaction heatmap -----------------------------------------

def plot_interaction_heatmap(vc: dict, output_path: str) -> None:
    n = len(ALL_FACETS)
    matrix = np.zeros((n, n))
    total = sum(v["estimate"] for v in vc.values())

    for key, info in vc.items():
        if ":" not in key:
            continue
        parts = key.split(":")
        if parts[0] in ALL_FACETS and parts[1] in ALL_FACETS:
            i = ALL_FACETS.index(parts[0])
            j = ALL_FACETS.index(parts[1])
            pct = info["estimate"] / total * 100 if total > 0 else 0
            matrix[i][j] = pct
            matrix[j][i] = pct

    labels = [FACET_LABELS.get(f, f) for f in ALL_FACETS]
    mask = np.triu(np.ones_like(matrix, dtype=bool))

    fig, ax = plt.subplots(figsize=(9, 8))
    sns.heatmap(
        matrix, mask=mask, annot=True, fmt=".2f",
        xticklabels=labels, yticklabels=labels,
        cmap="YlOrRd", ax=ax, linewidths=0.5,
        cbar_kws={"label": "% of Total Variance"},
    )
    ax.set_title("2-way Interaction Variance Components", fontsize=13, pad=12)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  → {output_path}")


# ---- Figure 3: D-study curves ----------------------------------------------

def plot_d_study_curves(d_study: dict, output_path: str) -> None:
    sweeps = d_study["sweeps"]

    facet_colors = {
        "prompt_template": "#d62728",
        "seed": "#1f77b4",
        "ordering": "#2ca02c",
        "item_id": "#9467bd",
    }

    fig, ax = plt.subplots(figsize=(10, 6))

    for facet, data in sweeps.items():
        ns = [d["n"] for d in data]
        gs = [d["g"] for d in data]
        ax.plot(
            ns, gs, "o-",
            color=facet_colors.get(facet, "#333"),
            label=FACET_LABELS.get(facet, facet),
            markersize=4, linewidth=1.5,
        )

    for target in [0.90, 0.95, 0.99]:
        ax.axhline(y=target, color="#bdc3c7", linestyle="--", linewidth=0.8)
        ax.text(
            20.3, target, f"G = {target}",
            va="center", fontsize=8, color="#7f8c8d",
        )

    ax.set_xlabel("Number of Replications", fontsize=11)
    ax.set_ylabel("Generalizability Coefficient (G)", fontsize=11)
    ax.set_title(
        "D-study: Replications Needed for Target Reliability",
        fontsize=13, pad=12,
    )
    ax.legend(loc="lower right", fontsize=10)
    ax.set_xlim(0.5, 20.5)
    ax.set_ylim(0, 1.05)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  → {output_path}")


# ---- main ------------------------------------------------------------------

def main(
    components_path: str,
    dstudy_path: str,
    output_dir: str,
) -> None:
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    with open(components_path) as f:
        comp_data = json.load(f)
    with open(dstudy_path) as f:
        dstudy_data = json.load(f)

    vc = comp_data["variance_components"]

    print("Generating figures:")
    plot_variance_components(vc, f"{output_dir}/variance_components.png")
    plot_interaction_heatmap(vc, f"{output_dir}/interaction_heatmap.png")
    plot_d_study_curves(dstudy_data, f"{output_dir}/d_study_curves.png")
    print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Visualize G-theory results"
    )
    parser.add_argument("--components", required=True)
    parser.add_argument("--dstudy", required=True)
    parser.add_argument("--output-dir", default="results/figures")
    args = parser.parse_args()
    main(args.components, args.dstudy, args.output_dir)

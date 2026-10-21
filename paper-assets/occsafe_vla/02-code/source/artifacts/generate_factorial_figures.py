#!/usr/bin/env python3
"""Generate factorial study figures for the paper.

Produces two figures:
  A) Grouped bar chart: CAR across 5 conditions (4 factorial + vanilla baseline)
  B) Interaction plot: gradient_flow x norm_type interaction on CAR

Usage:
  python generate_factorial_figures.py --demo
  python generate_factorial_figures.py --data-json results.json --output-dir ./figs
"""

import argparse
import json
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

DEMO_DATA = {
    "vanilla": {"car": [0.768], "tsr": [0.900]},
    "cell_1":  {"car": [0.746, 0.654, 0.776], "tsr": [0.802, 0.854, 0.906]},
    "cell_2":  {"car": [], "tsr": []},
    "cell_3":  {"car": [0.774, 0.736, 0.762, 0.794], "tsr": [0.870, 0.926, 0.914, 0.922]},
    "cell_4":  {"car": [], "tsr": []},
}

# Colorblind-friendly palette (Okabe-Ito inspired)
COLOR_ON_BN  = "#E69F00"   # warm: orange
COLOR_ON_LN  = "#D55E00"   # warm: vermillion
COLOR_OFF_BN = "#0072B2"   # cool: blue
COLOR_OFF_LN = "#56B4E9"   # cool: sky blue
COLOR_VANILLA = "#999999"  # neutral gray

CELL_CONFIG = {
    "vanilla": {"label": "Vanilla",    "color": COLOR_VANILLA, "hatch": ""},
    "cell_1":  {"label": "Full BN",    "color": COLOR_ON_BN,   "hatch": ""},
    "cell_2":  {"label": "Full LN",    "color": COLOR_ON_LN,   "hatch": "///"},
    "cell_3":  {"label": "Detach BN",  "color": COLOR_OFF_BN,  "hatch": ""},
    "cell_4":  {"label": "Detach LN",  "color": COLOR_OFF_LN,  "hatch": "///"},
}

PLOT_ORDER = ["vanilla", "cell_1", "cell_2", "cell_3", "cell_4"]

# 2x2 factorial cells for interaction plot
INTERACTION_CELLS = {
    ("ON", "BN"):  "cell_1",
    ("ON", "LN"):  "cell_2",
    ("OFF", "BN"): "cell_3",
    ("OFF", "LN"): "cell_4",
}


def setup_rcparams():
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman", "DejaVu Serif", "serif"],
        "font.size": 11,
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 9,
        "figure.dpi": 300,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.05,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": False,
        "axes.linewidth": 0.8,
        "xtick.major.width": 0.8,
        "ytick.major.width": 0.8,
    })


def stats(values):
    if not values:
        return None, None, None
    arr = np.array(values, dtype=float)
    m = arr.mean()
    s = arr.std(ddof=1) if len(arr) > 1 else 0.0
    se = s / np.sqrt(len(arr)) if len(arr) > 1 else 0.0
    return m, s, se


def figure_a_bar_chart(data, output_dir):
    active = [(k, CELL_CONFIG[k]) for k in PLOT_ORDER
              if data.get(k, {}).get("car", [])]
    if not active:
        print("Figure A: no data available, skipping.")
        return

    labels = [cfg["label"] for _, cfg in active]
    means, stds = [], []
    colors, hatches = [], []
    for key, cfg in active:
        m, s, _ = stats(data[key]["car"])
        means.append(m)
        stds.append(s)
        colors.append(cfg["color"])
        hatches.append(cfg["hatch"])

    fig, ax = plt.subplots(figsize=(4.5, 3.2))
    x = np.arange(len(labels))
    bars = ax.bar(x, means, yerr=stds, width=0.6, capsize=3,
                  color=colors, edgecolor="black", linewidth=0.6,
                  error_kw={"linewidth": 0.8})
    for bar, h in zip(bars, hatches):
        bar.set_hatch(h)

    # Vanilla reference line
    van = data.get("vanilla", {}).get("car", [])
    if van:
        van_mean = np.mean(van)
        ax.axhline(van_mean, color=COLOR_VANILLA, linestyle="--",
                   linewidth=0.8, zorder=0)
        ax.text(len(labels) - 0.5, van_mean + 0.003, "Vanilla",
                fontsize=8, color="#666666", ha="right")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=15, ha="right")
    ax.set_ylabel("CAR")
    ax.set_ylim(bottom=max(0, min(means) - 0.15), top=min(1.0, max(means) + 0.1))

    # Legend for hatch encoding
    legend_elements = [
        Patch(facecolor="white", edgecolor="black", label="BN"),
        Patch(facecolor="white", edgecolor="black", hatch="///", label="LN"),
    ]
    ax.legend(handles=legend_elements, loc="upper right", frameon=False)

    for fmt in ["pdf", "png"]:
        path = os.path.join(output_dir, f"fig_factorial_bar.{fmt}")
        fig.savefig(path)
        print(f"Saved: {path}")
    plt.close(fig)


def figure_b_interaction(data, output_dir):
    gf_levels = ["ON", "OFF"]
    nt_levels = ["BN", "LN"]

    has_data = {}
    for gf in gf_levels:
        for nt in nt_levels:
            key = INTERACTION_CELLS[(gf, nt)]
            car = data.get(key, {}).get("car", [])
            if car:
                has_data[(gf, nt)] = car

    if len(has_data) < 2:
        print("Figure B: need at least 2 factorial cells, skipping.")
        return

    fig, ax = plt.subplots(figsize=(3.8, 3.2))
    x_pos = {"BN": 0, "LN": 1}

    line_styles = {
        "ON":  {"marker": "o", "linestyle": "-",  "color": COLOR_ON_BN,  "label": "Grad Flow ON"},
        "OFF": {"marker": "s", "linestyle": "--", "color": COLOR_OFF_BN, "label": "Grad Flow OFF"},
    }

    for gf in gf_levels:
        xs, ys, errs = [], [], []
        for nt in nt_levels:
            if (gf, nt) in has_data:
                m, _, se = stats(has_data[(gf, nt)])
                xs.append(x_pos[nt])
                ys.append(m)
                errs.append(se)
        if xs:
            style = line_styles[gf]
            ax.errorbar(xs, ys, yerr=errs, capsize=4,
                        marker=style["marker"], linestyle=style["linestyle"],
                        color=style["color"], label=style["label"],
                        linewidth=1.5, markersize=7, markeredgecolor="black",
                        markeredgewidth=0.5)

    # Vanilla reference
    van = data.get("vanilla", {}).get("car", [])
    if van:
        van_mean = np.mean(van)
        ax.axhline(van_mean, color=COLOR_VANILLA, linestyle=":",
                   linewidth=0.8, zorder=0, label="Vanilla")

    ax.set_xticks([0, 1])
    ax.set_xticklabels(nt_levels)
    ax.set_xlabel("Normalization Type")
    ax.set_ylabel("CAR")
    ax.set_xlim(-0.3, 1.3)
    ax.legend(frameon=False, loc="best")

    for fmt in ["pdf", "png"]:
        path = os.path.join(output_dir, f"fig_factorial_interaction.{fmt}")
        fig.savefig(path)
        print(f"Saved: {path}")
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description="Generate factorial study figures")
    parser.add_argument("--data-json", type=str, help="Path to JSON with CAR/TSR data")
    parser.add_argument("--demo", action="store_true", help="Use built-in demo data")
    parser.add_argument("--output-dir", type=str, default=".", help="Output directory")
    args = parser.parse_args()

    if args.demo:
        data = DEMO_DATA
    elif args.data_json:
        with open(args.data_json) as f:
            data = json.load(f)
    else:
        parser.error("Provide --data-json or --demo")
        sys.exit(1)

    os.makedirs(args.output_dir, exist_ok=True)
    setup_rcparams()
    figure_a_bar_chart(data, args.output_dir)
    figure_b_interaction(data, args.output_dir)


if __name__ == "__main__":
    main()

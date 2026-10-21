#!/usr/bin/env python3
"""Magnitude sensitivity curve: obs_only vs perdof SR across correction norms.

Dependencies: numpy, matplotlib
Usage: python magnitude_curve.py [--out OUTPUT.pdf] [--dry-run]
"""

import argparse
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# ── output ────────────────────────────────────────────────────────────
OUT_DIR = Path(__file__).parent.parent / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ── data: {norm: (SR%, tasks_completed)} ──────────────────────────────
SPATIAL_DATA = {
    "obs_only": {
        0.03: (44.3, 7),
        0.05: (35.0, 10),
        0.1:  (35.0, 10),
        0.2:  (35.0, 10),
        0.3:  (36.0, 10),
    },
    "perdof": {
        0.03: (30.0, 10),
        0.05: (31.0, 10),
        0.1:  (35.0, 10),
        0.2:  (28.3, 6),
        0.3:  (26.0, 10),
    },
}

# Object domain — fill when experiments complete
OBJECT_DATA = {
    "obs_only": {
        # 0.03: (SR, n_tasks),
        # 0.05: ...
    },
    "perdof": {
        # 0.03: (SR, n_tasks),
    },
}

# Baselines (horizontal dashed lines)
BASELINES = {
    "spatial": {"argmin (K=10)": 34.0, "VLA-only": 30.0},
    "object":  {"argmin (K=10)": 12.0},
}

# ── style ─────────────────────────────────────────────────────────────
COLORS = {
    "obs_only": "#A23B72",
    "perdof":   "#2E86AB",
}
LABELS = {
    "obs_only": "ACR obs-only",
    "perdof":   "ACR per-DOF",
}
BASELINE_STYLES = {
    "argmin (K=10)": {"color": "#555555", "linestyle": "--", "linewidth": 1.0},
    "VLA-only":      {"color": "#AAAAAA", "linestyle": ":",  "linewidth": 1.0},
}


def setup_style():
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica"],
        "font.size": 11,
        "axes.labelsize": 13,
        "axes.titlesize": 14,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.05,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": False,
    })


def plot_domain(ax, data, baselines, title):
    """Plot one domain (spatial or object) on given axes."""
    if not data.get("obs_only") and not data.get("perdof"):
        ax.text(0.5, 0.5, "Data pending", ha="center", va="center",
                transform=ax.transAxes, fontsize=12, color="#999999")
        ax.set_title(title)
        return

    for method in ["obs_only", "perdof"]:
        pts = data.get(method, {})
        if not pts:
            continue
        norms = sorted(pts.keys())
        srs = [pts[n][0] for n in norms]
        n_tasks = [pts[n][1] for n in norms]

        ax.plot(norms, srs, "o-", color=COLORS[method], label=LABELS[method],
                linewidth=2.0, markersize=6, zorder=3)

        for x, y, nt in zip(norms, srs, n_tasks):
            if nt < 10:
                ax.annotate(f"({nt}/10)", (x, y), textcoords="offset points",
                            xytext=(0, 8), fontsize=7, color=COLORS[method],
                            ha="center")

    for bl_name, bl_sr in baselines.items():
        style = BASELINE_STYLES.get(bl_name, {"color": "#888888", "linestyle": "--"})
        ax.axhline(bl_sr, label=bl_name, **style, zorder=1)

    ax.set_xlabel("Correction norm bound")
    ax.set_ylabel("Success rate (%)")
    ax.set_title(title)
    ax.set_xscale("log")
    ax.xaxis.set_major_formatter(mticker.ScalarFormatter())
    ax.xaxis.set_minor_formatter(mticker.NullFormatter())

    all_norms = set()
    for method_data in data.values():
        all_norms.update(method_data.keys())
    if all_norms:
        ax.set_xticks(sorted(all_norms))
        ax.get_xaxis().set_major_formatter(mticker.FuncFormatter(
            lambda x, _: f"{x:g}"))

    all_srs = []
    for method_data in data.values():
        all_srs.extend(v[0] for v in method_data.values())
    for bl_sr in baselines.values():
        all_srs.append(bl_sr)
    if all_srs:
        ymin = max(0, min(all_srs) - 8)
        ymax = min(100, max(all_srs) + 8)
        ax.set_ylim(ymin, ymax)

    ax.legend(loc="best", frameon=False)


def main():
    parser = argparse.ArgumentParser(description="Magnitude sensitivity curve figure")
    parser.add_argument("--out", type=str, default=None, help="Output path (PDF/PNG)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.dry_run:
        print("dry-run OK: all imports successful")
        return

    setup_style()

    has_object = bool(OBJECT_DATA.get("obs_only") or OBJECT_DATA.get("perdof"))

    if has_object:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))
        plot_domain(ax1, SPATIAL_DATA, BASELINES["spatial"], "Spatial Domain")
        plot_domain(ax2, OBJECT_DATA, BASELINES["object"], "Object Domain")
    else:
        fig, ax1 = plt.subplots(1, 1, figsize=(5.5, 4.2))
        plot_domain(ax1, SPATIAL_DATA, BASELINES["spatial"], "Spatial Domain")

    fig.tight_layout(w_pad=3.0)

    out_path = args.out or str(OUT_DIR / "magnitude_curve.pdf")
    fig.savefig(out_path)
    print(f"Saved: {out_path}")

    if out_path.endswith(".pdf"):
        png_path = out_path.replace(".pdf", ".png")
        fig.savefig(png_path)
        print(f"Saved: {png_path}")

    plt.close(fig)


if __name__ == "__main__":
    main()

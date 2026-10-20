#!/usr/bin/env python3
"""Generate Pareto curve: Compute Saved vs Task Success Preserved."""

import argparse
import json
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

DATA_PATH = Path("artifacts/d072/early_termination_sim.json")
OUT_DIR = Path("artifacts/d072")

MODELS = [
    ("3lf_gb",   "3-LF GB",  "-",  "#1f77b4"),
    ("2lf_rf",   "2-LF RF",  "--", "#ff7f0e"),
    ("oracle",   "Oracle",   ":",  "#2ca02c"),
    ("random",   "Random",   "-.", "#7f7f7f"),
]

K_VALUES = [1, 2, 3, 5, 7, 10]


def generate_mock_data():
    """Deterministic mock data for dry-run."""
    rng = np.random.RandomState(42)
    data = {}
    curves = {
        "oracle":  {"base_save": 12, "scale": 8.5, "success_floor": 0.96},
        "3lf_gb":  {"base_save": 8,  "scale": 7.5, "success_floor": 0.93},
        "2lf_rf":  {"base_save": 6,  "scale": 6.5, "success_floor": 0.90},
        "random":  {"base_save": 4,  "scale": 5.0, "success_floor": 0.80},
    }
    for model_key, params in curves.items():
        model_data = {}
        for k in K_VALUES:
            compute_saved = params["base_save"] + params["scale"] * np.log1p(k)
            compute_saved += rng.normal(0, 0.3)
            false_term = (1 - params["success_floor"]) * (1 - np.exp(-0.3 * k))
            false_term = max(0, false_term + rng.normal(0, 0.005))
            model_data[str(k)] = {
                "compute_saved": round(float(compute_saved / 100), 4),
                "false_termination_rate": round(float(false_term), 4),
            }
        data[model_key] = model_data
    return data


def load_data(path):
    if path.exists():
        with open(path) as f:
            raw = json.load(f)
        return raw.get("results", raw)
    print(f"[WARN] {path} not found, using mock data", file=sys.stderr)
    return generate_mock_data()


def extract_curve(model_data):
    ks, xs, ys, x_errs, y_errs = [], [], [], [], []
    for k_str in sorted(model_data.keys(), key=lambda x: int(x)):
        k = int(k_str)
        entry = model_data[k_str]
        compute_saved = entry["compute_saved"] * 100
        success_preserved = (1 - entry["false_termination_rate"]) * 100
        ks.append(k)
        xs.append(compute_saved)
        ys.append(success_preserved)
        x_errs.append(entry.get("compute_saved_std", 0) * 100)
        y_errs.append(entry.get("false_termination_rate_std", 0) * 100)
    return ks, xs, ys, x_errs, y_errs


def plot(data, out_dir, dpi=300):
    fig, ax = plt.subplots(figsize=(5.5, 4.2))

    for model_key, label, ls, color in MODELS:
        if model_key not in data:
            continue
        ks, xs, ys, x_errs, y_errs = extract_curve(data[model_key])
        has_errs = any(e > 0 for e in x_errs) or any(e > 0 for e in y_errs)
        ax.plot(xs, ys, linestyle=ls, color=color, label=label,
                linewidth=1.8, marker="o", markersize=4, zorder=3)
        if has_errs:
            ax.errorbar(xs, ys, xerr=x_errs, yerr=y_errs,
                        fmt="none", ecolor=color, alpha=0.4, capsize=3, zorder=2)
        for k, x, y in zip(ks, xs, ys):
            ax.annotate(
                f"k={k}", (x, y),
                textcoords="offset points", xytext=(5, -8),
                fontsize=7, color=color, alpha=0.85,
            )

    ax.set_xlabel("Compute Saved (%)", fontsize=12)
    ax.set_ylabel("Task Success Preserved (%)", fontsize=12)
    ax.tick_params(labelsize=10)
    ax.grid(True, alpha=0.3, linewidth=0.5)
    ax.legend(fontsize=10, loc="best", framealpha=0.9)
    ax.set_ylim(None, 101)

    fig.tight_layout()
    out_dir.mkdir(parents=True, exist_ok=True)
    for ext in ("pdf", "png"):
        out_path = out_dir / f"pareto_curve.{ext}"
        fig.savefig(out_path, dpi=dpi, bbox_inches="tight")
        print(f"Saved {out_path}")
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(
        description="Generate Pareto curve from early termination simulation."
    )
    parser.add_argument("--input", type=Path, default=DATA_PATH,
                        help="Path to early_termination_sim.json")
    parser.add_argument("--outdir", type=Path, default=OUT_DIR,
                        help="Output directory for PDF/PNG")
    parser.add_argument("--dpi", type=int, default=300)
    args = parser.parse_args()

    data = load_data(args.input)
    plot(data, args.outdir, dpi=args.dpi)


if __name__ == "__main__":
    main()

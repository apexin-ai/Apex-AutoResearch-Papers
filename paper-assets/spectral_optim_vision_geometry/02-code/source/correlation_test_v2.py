#!/usr/bin/env python3
"""
D014 Correlation Test v2: FCSB margin (continuous) vs weight swap muon_drop_pp
==============================================================================
Replaces v1 which used δ² (only 3 discrete values, statistically invalid).

Input:
  - gradient_geometry_resnet50.csv: R, sr_X, delta per layer per epoch
  - resnet50_weight_swap.csv: muon_drop_pp per layer

Output:
  - JSON: primary test, Davis baseline, exploratory matrix, δ²-only reference
  - PNG: 3-panel scatter plot

Pre-registered (D014):
  Primary: Spearman ρ(FCSB_margin_grishina @ epoch 1, muon_drop_pp)
  PASS criterion: ρ ≥ 0.3 AND p < 0.05
"""

import argparse
import csv
import json
import os
import sys

import numpy as np
from scipy import stats


def load_scan_csv(path):
    data = {}
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            epoch = int(row["epoch"])
            layer = row["layer_name"]
            data[(epoch, layer)] = {
                "R": float(row["R"]),
                "sr_X": float(row["sr_X"]),
                "delta_theory": float(row["delta_theory"]),
                "delta_grishina": float(row["delta_grishina"]),
                "delta_empirical": float(row["delta_empirical"]),
                "kernel_size": int(row["kernel_size"]),
            }
    return data


def load_swap_csv(path):
    data = {}
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[row["layer_name"]] = {
                "muon_drop_pp": float(row["muon_drop_pp"]),
                "layer_type": row["layer_type"],
                "param_count": int(row["param_count"]),
            }
    return data


# FCSB_margin = R / (delta^2 * sr_X): continuous replacement for binary FCSB condition
# Davis_margin = R / sr_X: baseline without delta correction
def compute_margins(scan_row):
    R = scan_row["R"]
    sr_X = scan_row["sr_X"]
    return {
        "fcsb_margin_grishina": R / (scan_row["delta_grishina"] ** 2 * sr_X),
        "fcsb_margin_theory": R / (scan_row["delta_theory"] ** 2 * sr_X),
        "fcsb_margin_empirical": R / (scan_row["delta_empirical"] ** 2 * sr_X),
        "davis_margin": R / sr_X,
        "delta_sq_grishina": scan_row["delta_grishina"] ** 2,
    }


def run_correlation(x, y):
    sp_rho, sp_p = stats.spearmanr(x, y)
    pe_r, pe_p = stats.pearsonr(x, y)
    return {
        "spearman_rho": round(float(sp_rho), 4),
        "spearman_p": round(float(sp_p), 6),
        "pearson_r": round(float(pe_r), 4),
        "pearson_p": round(float(pe_p), 6),
        "n": len(x),
    }


def main():
    parser = argparse.ArgumentParser(description="D014 FCSB margin correlation test v2")
    parser.add_argument("--scan-csv", default="results/gradient_geometry_resnet50.csv")
    parser.add_argument("--swap-csv", default="results/resnet50_weight_swap.csv")
    parser.add_argument("--output", default="results/correlation_test_v2.json")
    parser.add_argument("--scatter", default="results/correlation_scatter.png")
    args = parser.parse_args()

    scan = load_scan_csv(args.scan_csv)
    swap = load_swap_csv(args.swap_csv)

    epochs = sorted(set(e for e, _ in scan.keys()))
    scan_layers = sorted(set(l for _, l in scan.keys()))
    swap_layers = sorted(swap.keys())

    # --- Layer matching ---
    matched = sorted(set(scan_layers) & set(swap_layers))
    unmatched_scan = sorted(set(scan_layers) - set(swap_layers))
    unmatched_swap = sorted(set(swap_layers) - set(scan_layers))

    print(f"Scan: {len(scan_layers)} layers, epochs {epochs}")
    print(f"Swap: {len(swap_layers)} layers")
    print(f"Matched: {len(matched)}, Unmatched scan: {len(unmatched_scan)}, Unmatched swap: {len(unmatched_swap)}")
    if unmatched_scan:
        print(f"  Unmatched in scan: {unmatched_scan}")
    if unmatched_swap:
        print(f"  Unmatched in swap: {unmatched_swap}")

    if len(matched) < 10:
        print("ERROR: fewer than 10 matched layers, correlation test meaningless")
        sys.exit(1)

    # --- Build aligned arrays per (variant, epoch) ---
    delta_variants = ["grishina", "theory", "empirical"]
    exploratory = {}
    primary_corr = None
    davis_corr_ep1 = None

    for epoch in epochs:
        for variant in delta_variants:
            margin_key = f"fcsb_margin_{variant}"
            margins, drops = [], []
            for layer in matched:
                if (epoch, layer) in scan:
                    m = compute_margins(scan[(epoch, layer)])
                    margins.append(m[margin_key])
                    drops.append(swap[layer]["muon_drop_pp"])

            key = f"{variant}_ep{epoch}"
            corr = run_correlation(np.array(margins), np.array(drops))
            exploratory[key] = {"rho": corr["spearman_rho"], "p": corr["spearman_p"]}

            if variant == "grishina" and epoch == 1:
                primary_margins = np.array(margins)
                primary_drops = np.array(drops)
                primary_corr = corr

        # Davis baseline
        davis_m, davis_d = [], []
        for layer in matched:
            if (epoch, layer) in scan:
                m = compute_margins(scan[(epoch, layer)])
                davis_m.append(m["davis_margin"])
                davis_d.append(swap[layer]["muon_drop_pp"])
        if epoch == 1:
            davis_ep1_m = np.array(davis_m)
            davis_ep1_d = np.array(davis_d)
            davis_corr_ep1 = run_correlation(davis_ep1_m, davis_ep1_d)

    # --- Primary test ---
    rho = primary_corr["spearman_rho"]
    p = primary_corr["spearman_p"]
    passed = rho >= 0.3 and p < 0.05

    # --- delta^2 only (3 discrete values, reference) ---
    delta_sq_only = {}
    for epoch in epochs:
        dsq, drops = [], []
        for layer in matched:
            if (epoch, layer) in scan:
                m = compute_margins(scan[(epoch, layer)])
                dsq.append(m["delta_sq_grishina"])
                drops.append(swap[layer]["muon_drop_pp"])
        dsq_arr = np.array(dsq)
        corr = run_correlation(dsq_arr, np.array(drops))
        delta_sq_only[f"grishina_ep{epoch}"] = {
            "rho": corr["spearman_rho"],
            "p": corr["spearman_p"],
            "n_unique_x": int(len(np.unique(dsq_arr))),
        }

    output = {
        "primary_test": {
            "predictor": "fcsb_margin_grishina_epoch1",
            "ground_truth": "muon_drop_pp",
            "n_layers_matched": len(matched),
            "spearman_rho": primary_corr["spearman_rho"],
            "spearman_p": primary_corr["spearman_p"],
            "pearson_r": primary_corr["pearson_r"],
            "pearson_p": primary_corr["pearson_p"],
            "result": "PASS" if passed else "FAIL",
            "criterion": "rho >= 0.3 and p < 0.05",
        },
        "davis_baseline": {
            "predictor": "davis_margin_epoch1",
            "spearman_rho": davis_corr_ep1["spearman_rho"],
            "spearman_p": davis_corr_ep1["spearman_p"],
            "pearson_r": davis_corr_ep1["pearson_r"],
            "pearson_p": davis_corr_ep1["pearson_p"],
        },
        "exploratory_matrix": exploratory,
        "delta_sq_only": {
            "note": "only 3 discrete values (1, 9, 49), Spearman degenerates to 3-group comparison",
            **delta_sq_only,
        },
        "unmatched_layers": {
            "in_scan_not_swap": unmatched_scan,
            "in_swap_not_scan": unmatched_swap,
        },
    }

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults written to {args.output}")
    print(json.dumps(output, indent=2))

    # --- Scatter plot ---
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(1, 3, figsize=(18, 5))

        # Panel 1: Primary test
        ax = axes[0]
        ax.scatter(primary_margins, primary_drops, alpha=0.6, s=40,
                   c="steelblue", edgecolors="k", linewidths=0.5)
        ax.set_xlabel("FCSB margin (grishina, epoch 1)")
        ax.set_ylabel("muon_drop_pp")
        verdict = "PASS" if passed else "FAIL"
        ax.set_title(f"Primary: rho={rho:.3f}, p={p:.4f} -> {verdict}")
        z = np.polyfit(primary_margins, primary_drops, 1)
        xl = np.linspace(primary_margins.min(), primary_margins.max(), 100)
        ax.plot(xl, np.polyval(z, xl), "r--", alpha=0.7)

        # Panel 2: Davis baseline
        ax = axes[1]
        ax.scatter(davis_ep1_m, davis_ep1_d, alpha=0.6, s=40,
                   c="coral", edgecolors="k", linewidths=0.5)
        ax.set_xlabel("Davis margin (epoch 1)")
        ax.set_ylabel("muon_drop_pp")
        ax.set_title(f"Davis baseline: rho={davis_corr_ep1['spearman_rho']:.3f}, p={davis_corr_ep1['spearman_p']:.4f}")
        z = np.polyfit(davis_ep1_m, davis_ep1_d, 1)
        xl = np.linspace(davis_ep1_m.min(), davis_ep1_m.max(), 100)
        ax.plot(xl, np.polyval(z, xl), "r--", alpha=0.7)

        # Panel 3: delta^2 only (jittered)
        dsq_ep1, drop_ep1 = [], []
        for layer in matched:
            if (1, layer) in scan:
                m = compute_margins(scan[(1, layer)])
                dsq_ep1.append(m["delta_sq_grishina"])
                drop_ep1.append(swap[layer]["muon_drop_pp"])
        dsq_ep1 = np.array(dsq_ep1)
        drop_ep1 = np.array(drop_ep1)
        dsq_ref = delta_sq_only["grishina_ep1"]
        ax = axes[2]
        jitter = np.random.default_rng(42).uniform(-0.3, 0.3, len(dsq_ep1))
        ax.scatter(dsq_ep1 + jitter, drop_ep1, alpha=0.6, s=40,
                   c="mediumpurple", edgecolors="k", linewidths=0.5)
        ax.set_xlabel("delta^2_grishina (3 discrete values)")
        ax.set_ylabel("muon_drop_pp")
        ax.set_title(f"delta^2 only: rho={dsq_ref['rho']:.3f}, p={dsq_ref['p']:.4f} (n_unique={dsq_ref['n_unique_x']})")
        ax.set_xticks(sorted(np.unique(dsq_ep1)))

        plt.tight_layout()
        os.makedirs(os.path.dirname(args.scatter) or ".", exist_ok=True)
        fig.savefig(args.scatter, dpi=150, bbox_inches="tight")
        print(f"Scatter plot saved to {args.scatter}")
        plt.close()
    except ImportError as e:
        print(f"Warning: matplotlib not available, skipping scatter: {e}")


if __name__ == "__main__":
    main()

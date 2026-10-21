#!/usr/bin/env python3
"""
D015 DeiT-S confirmatory correlation test: FCSB_margin vs muon_drop_pp
======================================================================
Cross-architecture confirmation of ResNet-50 finding (D014: rho=0.40, p=0.003).

Structural note: DeiT-S has 49/50 linear layers (delta_grishina=1.0).
Only patch_embed.proj is conv (delta=16), but it maps to "special" in swap CSV,
not "component", so it's excluded from the inner join. All matched layers have
delta_grishina=1.0, meaning FCSB_margin = R/(1^2 * sr_X) = R/sr_X = Davis_margin.
This test therefore validates R/sr_X cross-architecture generalization, NOT delta^2 correction.

Pre-registered (D015):
  Primary: Spearman rho(FCSB_margin_grishina @ epoch 5, muon_drop_pp)
  PASS criterion: rho >= 0.3 AND p < 0.05
"""

import argparse
import csv
import json
import os
import re
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
                "layer_type": row["layer_type"],
            }
    return data


def scan_to_swap_name(scan_name):
    """Convert scan layer name to swap group_name.
    blocks.N.xxx -> block_N.xxx
    """
    m = re.match(r"blocks\.(\d+)\.(.*)", scan_name)
    if m:
        return f"block_{m.group(1)}.{m.group(2)}"
    return scan_name


def load_swap_csv(path):
    data = {}
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["group_type"] != "component":
                continue
            data[row["group_name"]] = {
                "muon_drop_pp": float(row["muon_drop_pp"]),
                "group_type": row["group_type"],
                "param_count": int(row["param_count"]),
            }
    return data


def compute_margins(scan_row):
    R = scan_row["R"]
    sr_X = scan_row["sr_X"]
    return {
        "fcsb_margin_grishina": R / (scan_row["delta_grishina"] ** 2 * sr_X),
        "fcsb_margin_theory": R / (scan_row["delta_theory"] ** 2 * sr_X),
        "fcsb_margin_empirical": R / (scan_row["delta_empirical"] ** 2 * sr_X),
        "davis_margin": R / sr_X,
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
    parser = argparse.ArgumentParser(description="D015 DeiT-S confirmatory correlation test")
    parser.add_argument("--scan-csv", default="results/gradient_geometry_deit_small.csv")
    parser.add_argument("--swap-csv", default="results/deit_weight_swap.csv")
    parser.add_argument("--output", default="results/deit_confirmatory.json")
    parser.add_argument("--scatter", default="results/deit_confirmatory_scatter.png")
    args = parser.parse_args()

    if not os.path.exists(args.swap_csv):
        print(f"Waiting for {args.swap_csv} — weight swap not yet complete.")
        sys.exit(1)

    scan = load_scan_csv(args.scan_csv)
    swap = load_swap_csv(args.swap_csv)

    epochs = sorted(set(e for e, _ in scan.keys()))
    scan_layers = sorted(set(l for _, l in scan.keys()))
    swap_groups = sorted(swap.keys())

    # --- Layer matching: scan names -> swap names ---
    name_map = {}  # swap_name -> scan_name
    for sl in scan_layers:
        sw = scan_to_swap_name(sl)
        if sw in swap:
            name_map[sw] = sl

    matched_swap = sorted(name_map.keys())
    matched_scan = sorted(name_map.values())
    unmatched_scan = sorted(set(scan_layers) - set(matched_scan))
    unmatched_swap = sorted(set(swap_groups) - set(matched_swap))

    print(f"Scan: {len(scan_layers)} layers, epochs {epochs}")
    print(f"Swap: {len(swap_groups)} component groups")
    print(f"Matched: {len(matched_swap)}, Unmatched scan: {len(unmatched_scan)}, Unmatched swap: {len(unmatched_swap)}")
    if unmatched_scan:
        print(f"  Unmatched in scan: {unmatched_scan}")
    if unmatched_swap:
        print(f"  Unmatched in swap: {unmatched_swap}")

    if len(matched_swap) < 10:
        print("ERROR: fewer than 10 matched layers, aborting")
        sys.exit(1)

    # --- Primary test: FCSB_margin_grishina @ epoch 5 vs muon_drop_pp ---
    primary_epoch = 5
    primary_margins, primary_drops, primary_labels = [], [], []
    for sw_name in matched_swap:
        sc_name = name_map[sw_name]
        key = (primary_epoch, sc_name)
        if key not in scan:
            continue
        m = compute_margins(scan[key])
        primary_margins.append(m["fcsb_margin_grishina"])
        primary_drops.append(swap[sw_name]["muon_drop_pp"])
        primary_labels.append(sc_name)

    primary_margins = np.array(primary_margins)
    primary_drops = np.array(primary_drops)
    primary_corr = run_correlation(primary_margins, primary_drops)
    rho = primary_corr["spearman_rho"]
    p = primary_corr["spearman_p"]
    passed = rho >= 0.3 and p < 0.05

    print(f"\n=== PRIMARY TEST (pre-registered) ===")
    print(f"FCSB_margin_grishina @ epoch {primary_epoch} vs muon_drop_pp")
    print(f"Spearman rho = {rho:.4f}, p = {p:.6f}")
    print(f"Pearson r = {primary_corr['pearson_r']:.4f}, p = {primary_corr['pearson_p']:.6f}")
    print(f"n = {primary_corr['n']}")
    print(f"Result: {'PASS' if passed else 'FAIL'} (criterion: rho >= 0.3 and p < 0.05)")

    # --- Davis baseline @ epoch 5 ---
    davis_ep5_m, davis_ep5_d = [], []
    for sw_name in matched_swap:
        sc_name = name_map[sw_name]
        key = (primary_epoch, sc_name)
        if key not in scan:
            continue
        m = compute_margins(scan[key])
        davis_ep5_m.append(m["davis_margin"])
        davis_ep5_d.append(swap[sw_name]["muon_drop_pp"])
    davis_ep5_m = np.array(davis_ep5_m)
    davis_ep5_d = np.array(davis_ep5_d)
    davis_corr_ep5 = run_correlation(davis_ep5_m, davis_ep5_d)

    print(f"\n=== DAVIS BASELINE @ epoch {primary_epoch} ===")
    print(f"Spearman rho = {davis_corr_ep5['spearman_rho']:.4f}, p = {davis_corr_ep5['spearman_p']:.6f}")

    # Check if FCSB == Davis for matched layers (expected for DeiT-S)
    fcsb_davis_identical = np.allclose(primary_margins, davis_ep5_m)
    print(f"FCSB_margin == Davis_margin for all matched layers: {fcsb_davis_identical}")

    # --- Exploratory: 3 delta variants x all epochs ---
    delta_variants = ["fcsb_margin_grishina", "fcsb_margin_theory", "fcsb_margin_empirical"]
    exploratory = {}
    for dv in delta_variants:
        exploratory[dv] = {}
        for ep in epochs:
            margins, drops = [], []
            for sw_name in matched_swap:
                sc_name = name_map[sw_name]
                key = (ep, sc_name)
                if key not in scan:
                    continue
                m = compute_margins(scan[key])
                margins.append(m[dv])
                drops.append(swap[sw_name]["muon_drop_pp"])
            if len(margins) >= 10:
                corr = run_correlation(np.array(margins), np.array(drops))
                exploratory[dv][f"epoch_{ep}"] = corr

    print(f"\n=== EXPLORATORY MATRIX ===")
    for dv in delta_variants:
        for ep_key, corr in exploratory[dv].items():
            print(f"  {dv} @ {ep_key}: rho={corr['spearman_rho']:.4f}, p={corr['spearman_p']:.6f}")

    # --- Output JSON ---
    output = {
        "experiment": "D015_deit_confirmatory",
        "architecture": "DeiT-S",
        "structural_note": "49/50 matched layers are linear (delta_grishina=1.0), "
                           "so FCSB_margin = Davis_margin. This tests R/sr_X generalization, not delta^2.",
        "primary_test": {
            "predictor": f"fcsb_margin_grishina_epoch{primary_epoch}",
            "ground_truth": "muon_drop_pp",
            "n_layers_matched": len(matched_swap),
            "spearman_rho": primary_corr["spearman_rho"],
            "spearman_p": primary_corr["spearman_p"],
            "pearson_r": primary_corr["pearson_r"],
            "pearson_p": primary_corr["pearson_p"],
            "result": "PASS" if passed else "FAIL",
            "criterion": "rho >= 0.3 and p < 0.05",
        },
        "davis_baseline": {
            "predictor": f"davis_margin_epoch{primary_epoch}",
            "spearman_rho": davis_corr_ep5["spearman_rho"],
            "spearman_p": davis_corr_ep5["spearman_p"],
            "pearson_r": davis_corr_ep5["pearson_r"],
            "pearson_p": davis_corr_ep5["pearson_p"],
            "fcsb_equals_davis": bool(fcsb_davis_identical),
        },
        "exploratory_matrix": exploratory,
        "cross_arch_comparison": {
            "resnet50_reference": {
                "rho": 0.40,
                "p": 0.003,
                "epoch": 1,
                "n": 53,
            },
            "deit_s": {
                "rho": primary_corr["spearman_rho"],
                "p": primary_corr["spearman_p"],
                "epoch": primary_epoch,
                "n": primary_corr["n"],
            },
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

        # Panel 1: Primary (FCSB_margin @ epoch 5)
        ax = axes[0]
        ax.scatter(primary_margins, primary_drops, alpha=0.6, s=40,
                   c="steelblue", edgecolors="k", linewidths=0.5)
        ax.set_xlabel(f"FCSB margin (grishina, epoch {primary_epoch})")
        ax.set_ylabel("muon_drop_pp")
        verdict = "PASS" if passed else "FAIL"
        ax.set_title(f"Primary: ρ={rho:.3f}, p={p:.4f} → {verdict}")
        z = np.polyfit(primary_margins, primary_drops, 1)
        xl = np.linspace(primary_margins.min(), primary_margins.max(), 100)
        ax.plot(xl, np.polyval(z, xl), "r--", alpha=0.7)

        # Panel 2: Davis baseline @ epoch 5
        ax = axes[1]
        ax.scatter(davis_ep5_m, davis_ep5_d, alpha=0.6, s=40,
                   c="coral", edgecolors="k", linewidths=0.5)
        ax.set_xlabel(f"Davis margin (epoch {primary_epoch})")
        ax.set_ylabel("muon_drop_pp")
        ax.set_title(f"Davis baseline: ρ={davis_corr_ep5['spearman_rho']:.3f}, p={davis_corr_ep5['spearman_p']:.4f}")
        z = np.polyfit(davis_ep5_m, davis_ep5_d, 1)
        xl = np.linspace(davis_ep5_m.min(), davis_ep5_m.max(), 100)
        ax.plot(xl, np.polyval(z, xl), "r--", alpha=0.7)

        # Panel 3: Epoch comparison (all epochs, FCSB_margin_grishina)
        ax = axes[2]
        colors = ["#2196F3", "#FF9800", "#4CAF50"]
        for i, ep in enumerate(epochs):
            margins, drops = [], []
            for sw_name in matched_swap:
                sc_name = name_map[sw_name]
                key = (ep, sc_name)
                if key not in scan:
                    continue
                m = compute_margins(scan[key])
                margins.append(m["fcsb_margin_grishina"])
                drops.append(swap[sw_name]["muon_drop_pp"])
            if margins:
                ep_corr = run_correlation(np.array(margins), np.array(drops))
                ax.scatter(margins, drops, alpha=0.5, s=30, c=colors[i % len(colors)],
                           edgecolors="k", linewidths=0.3,
                           label=f"ep{ep}: ρ={ep_corr['spearman_rho']:.3f}")
        ax.set_xlabel("FCSB margin (grishina)")
        ax.set_ylabel("muon_drop_pp")
        ax.set_title("Epoch comparison")
        ax.legend(fontsize=8)

        plt.suptitle("D015: DeiT-S Confirmatory Correlation Test", fontsize=13, y=1.02)
        plt.tight_layout()
        os.makedirs(os.path.dirname(args.scatter) or ".", exist_ok=True)
        fig.savefig(args.scatter, dpi=150, bbox_inches="tight")
        print(f"Scatter plot saved to {args.scatter}")
        plt.close()
    except ImportError as e:
        print(f"Warning: matplotlib not available, skipping scatter: {e}")


if __name__ == "__main__":
    main()

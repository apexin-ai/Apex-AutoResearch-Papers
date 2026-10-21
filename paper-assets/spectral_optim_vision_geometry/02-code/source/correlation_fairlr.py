#!/usr/bin/env python3
"""B2.7 Correlation recompute with optimal-lr weight swap data.

Computes Spearman rho(FCSB_margin, muon_drop_pp) for both ResNet-50 and DeiT-S
using the fairlr weight swap results.
"""

import csv
import json
import os
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
                "delta_grishina": float(row["delta_grishina"]),
            }
    return data


def load_swap_csv(path, name_col="layer_name"):
    data = {}
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row[name_col]
            data[name] = float(row["muon_drop_pp"])
    return data


def fcsb_margin(scan_row):
    R = scan_row["R"]
    sr_X = scan_row["sr_X"]
    delta = scan_row["delta_grishina"]
    return R / (delta ** 2 * sr_X)


def name_map_deit(swap_name):
    """Convert DeiT swap group_name (block_X.Y) to scan layer_name (blocks.X.Y)"""
    if swap_name.startswith("block_"):
        parts = swap_name.split(".", 1)
        block_part = parts[0].replace("block_", "blocks.")
        if len(parts) > 1:
            return f"{block_part}.{parts[1]}"
        return block_part
    if swap_name == "patch_embed":
        return "patch_embed.proj"
    return swap_name


def compute_correlation(scan_data, swap_data, epoch, arch, name_mapper=None):
    margins = []
    drops = []
    matched_layers = []

    for swap_name, drop in swap_data.items():
        scan_name = name_mapper(swap_name) if name_mapper else swap_name
        key = (epoch, scan_name)
        if key in scan_data:
            m = fcsb_margin(scan_data[key])
            if np.isfinite(m):
                margins.append(m)
                drops.append(drop)
                matched_layers.append(swap_name)

    if len(margins) < 10:
        return {"error": f"Only {len(margins)} matched layers", "n": len(margins)}

    margins = np.array(margins)
    drops = np.array(drops)
    rho, p = stats.spearmanr(margins, drops)
    r, pr = stats.pearsonr(margins, drops)

    return {
        "n_matched": len(margins),
        "spearman_rho": round(float(rho), 4),
        "spearman_p": round(float(p), 6),
        "pearson_r": round(float(r), 4),
        "pearson_p": round(float(pr), 6),
    }


def main():
    base = "/root/spectral_optim_vision_geometry"

    # ResNet-50
    resnet_scan = load_scan_csv(f"{base}/results/gradient_geometry_resnet50.csv")
    resnet_swap = load_swap_csv(f"{base}/results/fairlr/resnet50_weight_swap.csv")

    # DeiT-S
    deit_scan = load_scan_csv(f"{base}/results/gradient_geometry_deit_small.csv")
    deit_swap_path = f"{base}/results/fairlr/deit_weight_swap.csv"

    results = {
        "experiment": "B2.7_fairlr_correlation_recompute",
        "description": "Spearman rho(FCSB_margin_grishina, muon_drop_pp) with optimal-lr checkpoints",
        "old_baselines": {
            "resnet50": {"rho": 0.40, "p": 0.003, "epoch": 5},
            "deit_s": {"rho": -0.51, "p": 0.000224, "epoch": 5},
        },
    }

    # ResNet correlation at epochs 1, 3, 5
    resnet_results = {}
    for ep in [1, 3, 5]:
        resnet_results[f"epoch_{ep}"] = compute_correlation(
            resnet_scan, resnet_swap, ep, "resnet50"
        )
    results["resnet50"] = resnet_results

    # DeiT correlation
    if os.path.exists(deit_swap_path):
        deit_swap_raw = load_swap_csv(deit_swap_path, name_col="group_name")
        # Only use component-level groups (not block-level or special)
        deit_swap = {}
        with open(deit_swap_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["group_type"] == "component":
                    deit_swap[row["group_name"]] = float(row["muon_drop_pp"])

        deit_results = {}
        for ep in [1, 3, 5]:
            deit_results[f"epoch_{ep}"] = compute_correlation(
                deit_scan, deit_swap, ep, "deit_s", name_mapper=name_map_deit
            )
        results["deit_s"] = deit_results
    else:
        results["deit_s"] = {"error": f"Swap CSV not found: {deit_swap_path}"}

    # Judgment
    judgment = {}
    for arch, old_rho, old_sign in [("resnet50", 0.40, +1), ("deit_s", -0.51, -1)]:
        if arch in results and "epoch_5" in results[arch]:
            ep5 = results[arch]["epoch_5"]
            if "spearman_rho" in ep5:
                new_rho = ep5["spearman_rho"]
                abs_rho = abs(new_rho)
                same_sign = (new_rho * old_sign) > 0
                if abs_rho < 0.2:
                    judgment[arch] = f"KILL (|rho|={abs_rho:.3f} < 0.2)"
                elif not same_sign:
                    judgment[arch] = f"KILL (direction reversed: old={old_rho:+.2f}, new={new_rho:+.4f})"
                else:
                    judgment[arch] = f"CONFIRMED (rho={new_rho:+.4f}, |rho|={abs_rho:.3f} >= 0.2, direction preserved)"
            else:
                judgment[arch] = f"INCONCLUSIVE ({ep5.get('error', 'unknown')})"
        else:
            judgment[arch] = "INCONCLUSIVE (missing data)"

    results["judgment"] = judgment

    # Overall verdict
    if all("CONFIRMED" in v for v in judgment.values()):
        results["claim1_verdict"] = "CONFIRMED - direction reversal survives with optimal-lr"
    elif any("KILL" in v for v in judgment.values()):
        killed = [k for k, v in judgment.items() if "KILL" in v]
        results["claim1_verdict"] = f"KILL - fails for: {', '.join(killed)}"
    else:
        results["claim1_verdict"] = "INCONCLUSIVE"

    out_path = f"{base}/results/fairlr/correlation_fairlr.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(json.dumps(results, indent=2))
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()

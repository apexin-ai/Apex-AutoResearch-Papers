#!/usr/bin/env python3
"""Bootstrap CI for ΔR² gap between VLM→VLA and VLA→VLA architectures.

Aggregates existing clustered bootstrap (MCCV) results from bootstrap_v3/
and performs the gap significance test:
  max(CI_upper of VLA→VLA) vs min(CI_lower of VLM→VLA)

Input:  <PROJECT_ROOT>/results/bootstrap_v3/{cell}/trained.json
Output: <PROJECT_ROOT>/results/bootstrap_ci/bootstrap_ci_results.json
"""
# --- Path configuration (set env vars to override defaults) ---
import os as _os
PROJECT_ROOT = _os.environ.get("VLA_SSD_ROOT", ".")
LIBERO_ROOT = _os.environ.get("LIBERO_ROOT", "./LIBERO")
# ---

import json, os, sys

BOOTSTRAP_V3_DIR = f"{PROJECT_ROOT}/results/bootstrap_v3"
OUTPUT_DIR = f"{PROJECT_ROOT}/results/bootstrap_ci"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "bootstrap_ci_results.json")

# VLM→VLA: backbone was a VLM, finetuned into VLA (exit collapse expected)
VLM_TO_VLA = ["tracvla_goal", "tracvla_spatial", "tracvla_object", "tracvla_long",
              "nora_goal", "nora_spatial"]

# VLA→VLA: backbone was already a VLA (no exit collapse expected)
VLA_TO_VLA = ["openvla_goal", "openvla_spatial", "openvla_object", "openvla_long"]


def load_cell(cell_name):
    path = os.path.join(BOOTSTRAP_V3_DIR, cell_name, "trained.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def main():
    cells = {}
    vlm_to_vla_results = []
    vla_to_vla_results = []

    all_cell_names = sorted(os.listdir(BOOTSTRAP_V3_DIR))
    print(f"Found cells: {all_cell_names}\n")

    for cell_name in all_cell_names:
        data = load_cell(cell_name)
        if data is None:
            print(f"  SKIP {cell_name}: no trained.json")
            continue

        ci_lo, ci_hi = data["delta_ci_95"]
        boot_mean = data["bootstrap_deltas_summary"]["mean"]
        boot_std = data["bootstrap_deltas_summary"]["std"]

        # Flag unstable NORA results where CI doesn't bracket the point estimate
        nora_unstable = (cell_name.startswith("nora") and ci_lo > data["delta"] * 1.5)

        entry = {
            "cell": cell_name,
            "arch": data["arch"],
            "suite": data["suite"],
            "peak_layer": data["peak_layer"],
            "peak_r2": data["peak_r2"],
            "exit_layer": data["exit_layer"],
            "exit_r2": data["exit_r2"],
            "delta_r2": data["delta"],
            "ci_lower_2.5%": ci_lo,
            "ci_upper_97.5%": ci_hi,
            "bootstrap_mean": boot_mean,
            "bootstrap_std": boot_std,
            "n_bootstrap": data["n_bootstrap"],
            "n_test_samples": data["n_total_samples"],
        }
        if nora_unstable:
            entry["flag"] = "unstable_exit_layer"

        cells[cell_name] = entry

        category = "VLM→VLA" if cell_name in VLM_TO_VLA else "VLA→VLA"
        entry["category"] = category
        if category == "VLM→VLA":
            vlm_to_vla_results.append(entry)
        else:
            vla_to_vla_results.append(entry)

    # Print summary table
    print(f"{'Cell':<22} {'Category':<10} {'Peak':<5} {'ΔR²':>6} {'CI_lo':>7} {'CI_hi':>7} {'Flag'}")
    print("-" * 75)
    for cell_name in all_cell_names:
        if cell_name not in cells:
            continue
        e = cells[cell_name]
        flag = e.get("flag", "")
        print(f"{e['cell']:<22} {e['category']:<10} {e['peak_layer']:<5} "
              f"{e['delta_r2']:>6.4f} {e['ci_lower_2.5%']:>7.4f} {e['ci_upper_97.5%']:>7.4f} {flag}")

    # Gap significance test
    # Exclude flagged (unstable) cells from the strict test
    stable_vlm = [e for e in vlm_to_vla_results if "flag" not in e]
    stable_vla = vla_to_vla_results  # OpenVLA results are all stable

    print(f"\n{'='*75}")
    print("GAP SIGNIFICANCE TEST")
    print(f"{'='*75}")

    if not stable_vlm or not stable_vla:
        print("ERROR: insufficient data for gap test")
        sys.exit(1)

    max_vla_ci_upper = max(e["ci_upper_97.5%"] for e in stable_vla)
    max_vla_cell = [e["cell"] for e in stable_vla if e["ci_upper_97.5%"] == max_vla_ci_upper][0]

    min_vlm_ci_lower = min(e["ci_lower_2.5%"] for e in stable_vlm)
    min_vlm_cell = [e["cell"] for e in stable_vlm if e["ci_lower_2.5%"] == min_vlm_ci_lower][0]

    gap = min_vlm_ci_lower - max_vla_ci_upper
    significant = gap > 0

    print(f"\nVLA→VLA max CI_upper: {max_vla_ci_upper:.4f} ({max_vla_cell})")
    print(f"VLM→VLA min CI_lower: {min_vlm_ci_lower:.4f} ({min_vlm_cell})")
    print(f"Gap: {gap:.4f}")
    print(f"Significant (no overlap): {significant}")

    # Also report per-category ranges
    print(f"\n--- VLA→VLA (no collapse expected) ---")
    for e in sorted(stable_vla, key=lambda x: x["delta_r2"]):
        print(f"  {e['cell']:<20} ΔR²={e['delta_r2']:.4f}  CI=[{e['ci_lower_2.5%']:.4f}, {e['ci_upper_97.5%']:.4f}]")

    print(f"\n--- VLM→VLA (exit collapse expected) ---")
    for e in sorted(stable_vlm, key=lambda x: x["delta_r2"]):
        print(f"  {e['cell']:<20} ΔR²={e['delta_r2']:.4f}  CI=[{e['ci_lower_2.5%']:.4f}, {e['ci_upper_97.5%']:.4f}]")

    if [e for e in vlm_to_vla_results if "flag" in e]:
        print(f"\n--- VLM→VLA (flagged: unstable exit layer) ---")
        for e in [e for e in vlm_to_vla_results if "flag" in e]:
            print(f"  {e['cell']:<20} ΔR²={e['delta_r2']:.4f}  CI=[{e['ci_lower_2.5%']:.4f}, {e['ci_upper_97.5%']:.4f}]  "
                  f"(bootstrap mean={e['bootstrap_mean']:.4f})")

    # Save results
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    result = {
        "cells": cells,
        "gap_test": {
            "max_vla_to_vla_ci_upper": max_vla_ci_upper,
            "max_vla_to_vla_cell": max_vla_cell,
            "min_vlm_to_vla_ci_lower": min_vlm_ci_lower,
            "min_vlm_to_vla_cell": min_vlm_cell,
            "gap": gap,
            "significant": significant,
            "note": "Gap > 0 means no CI overlap between categories (excluding flagged cells)"
        },
        "metadata": {
            "source": "bootstrap_v3 (Monte Carlo CV, 1000 iterations, demo-level resampling)",
            "ci_level": 0.95,
            "n_vlm_to_vla_cells": len(stable_vlm),
            "n_vla_to_vla_cells": len(stable_vla),
            "flagged_cells": [e["cell"] for e in vlm_to_vla_results if "flag" in e],
        }
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

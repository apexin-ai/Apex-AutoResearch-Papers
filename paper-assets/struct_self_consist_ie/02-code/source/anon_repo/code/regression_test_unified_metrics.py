#!/usr/bin/env python3
"""Regression test: verify all analysis scripts produce identical metrics
when using unified_metrics on the same SciERC data."""

import json
import sys
import os
import numpy as np

sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie/code")
from unified_metrics import (
    compute_entity_f1, compute_degeneracy, load_and_filter,
    compute_sample_f1s, compute_greedy_f1, get_lp_selection_idx,
    bootstrap_ci
)

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl"
OUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/unified_metrics_regression"
os.makedirs(OUT_DIR, exist_ok=True)

N_SAMPLES = 8


def ground_truth():
    """Compute canonical metrics using unified_metrics."""
    data = load_and_filter(DATA_PATH, gold_filter=True)
    greedy_f1s, lp_f1s, oracle_f1s = [], [], []
    n_degen = 0
    for inst in data:
        gf = compute_greedy_f1(inst)
        greedy_f1s.append(gf)
        sf = compute_sample_f1s(inst, n_samples=N_SAMPLES)
        oracle_f1s.append(max(sf))
        lp_idx = get_lp_selection_idx(inst, n_samples=N_SAMPLES)
        lp_f1s.append(sf[lp_idx])
        if compute_degeneracy(sf):
            n_degen += 1
    n = len(data)
    return {
        "n_instances": n,
        "greedy_f1": float(np.mean(greedy_f1s)),
        "lp_sel_f1": float(np.mean(lp_f1s)),
        "oracle_f1": float(np.mean(oracle_f1s)),
        "n_degen": n_degen,
        "degen_rate": n_degen / n * 100,
    }


def test_ccs_selection():
    """Verify ccs_selection.py uses unified_metrics and matches ground truth."""
    from ccs_selection import analyze_dataset
    r = analyze_dataset(DATA_PATH, "SciERC", n_samples=N_SAMPLES)
    n = r["n_instances"]
    n_degen = r["stage_distribution"]["stage1_greedy"]
    return {
        "greedy_f1": r["greedy_f1"]["mean"],
        "oracle_f1": r["oracle_f1"]["mean"],
        "degen_rate": n_degen / n * 100,
    }


def test_dgs_gold_filter():
    """Verify analysis_dgs_gold_filter.py uses unified_metrics and matches."""
    from analysis_dgs_gold_filter import analyze_dataset
    r = analyze_dataset(DATA_PATH, "SciERC", n_samples=N_SAMPLES, gold_filter=True)
    n = r["n_used"]
    return {
        "greedy_f1": float(np.mean(r["greedy"])),
        "lp_sel_f1": float(np.mean(r["lp"])),
        "oracle_f1": float(np.mean(r["oracle"])),
        "degen_rate": r["n_degen"] / n * 100,
    }


def test_entity_consensus():
    """Verify entity_consensus.py uses unified_metrics and matches."""
    from entity_consensus import load_data, evaluate_dataset
    cfg = {"path": DATA_PATH, "gold_filter": True}
    r = evaluate_dataset("SciERC", cfg, thresholds=[], n_bootstrap=100)
    return {
        "greedy_f1": r["baselines"]["greedy"]["mean"],
        "lp_sel_f1": r["baselines"]["lp_selection"]["mean"],
        "oracle_f1": r["baselines"]["oracle"]["mean"],
    }


def test_diagnostic_calibration():
    """Verify diagnostic_calibration.py uses unified_metrics and matches."""
    from diagnostic_calibration import load_data, compute_diagnostics
    data = load_data(DATA_PATH)
    diag = compute_diagnostics(data, subtask="ner")
    return {
        "greedy_f1": diag["greedy_f1"],
        "lp_sel_f1": diag["lp_sel_f1"],
        "degen_rate": diag["degeneracy_rate"],
        "n_instances": diag["n_instances"],
    }


def test_adaptive_temperature():
    """Verify adaptive_temperature_analysis.py degeneracy uses constant-F1."""
    from adaptive_temperature_analysis import compute_degeneracy_rate, compute_greedy_f1_filtered, load_samples
    data = load_samples(DATA_PATH)
    degen_rate, degen_count, degen_total = compute_degeneracy_rate(data, n_samples=N_SAMPLES)
    greedy_f1, _ = compute_greedy_f1_filtered(data)
    return {
        "greedy_f1": greedy_f1,
        "degen_rate": degen_rate * 100,
        "degen_count": degen_count,
        "degen_total": degen_total,
    }


def main():
    print("=" * 70)
    print("REGRESSION TEST: Unified Metrics Consistency")
    print(f"Data: {DATA_PATH}")
    print("=" * 70)

    gt = ground_truth()
    print(f"\nGround Truth (unified_metrics):")
    print(f"  N = {gt['n_instances']}")
    print(f"  Greedy F1  = {gt['greedy_f1']:.6f}")
    print(f"  LP-sel F1  = {gt['lp_sel_f1']:.6f}")
    print(f"  Oracle F1  = {gt['oracle_f1']:.6f}")
    print(f"  Degeneracy = {gt['n_degen']}/{gt['n_instances']} = {gt['degen_rate']:.2f}%")

    tests = {
        "ccs_selection": test_ccs_selection,
        "analysis_dgs_gold_filter": test_dgs_gold_filter,
        "entity_consensus": test_entity_consensus,
        "diagnostic_calibration": test_diagnostic_calibration,
        "adaptive_temperature": test_adaptive_temperature,
    }

    results = {"ground_truth": gt, "scripts": {}}
    all_pass = True

    for name, test_fn in tests.items():
        print(f"\n--- {name} ---")
        try:
            r = test_fn()
            results["scripts"][name] = r

            greedy_match = abs(r["greedy_f1"] - gt["greedy_f1"]) < 1e-6
            degen_match = True
            if "degen_rate" in r:
                degen_match = abs(r["degen_rate"] - gt["degen_rate"]) < 0.01

            status = "PASS" if greedy_match and degen_match else "FAIL"
            if status == "FAIL":
                all_pass = False

            print(f"  Greedy F1:  {r['greedy_f1']:.6f}  {'OK' if greedy_match else 'MISMATCH'}")
            if "lp_sel_f1" in r:
                lp_match = abs(r["lp_sel_f1"] - gt["lp_sel_f1"]) < 1e-6
                print(f"  LP-sel F1:  {r['lp_sel_f1']:.6f}  {'OK' if lp_match else 'MISMATCH'}")
            if "oracle_f1" in r:
                oracle_match = abs(r["oracle_f1"] - gt["oracle_f1"]) < 1e-6
                print(f"  Oracle F1:  {r['oracle_f1']:.6f}  {'OK' if oracle_match else 'MISMATCH'}")
            if "degen_rate" in r:
                print(f"  Degen rate: {r['degen_rate']:.2f}%  {'OK' if degen_match else 'MISMATCH'}")
            print(f"  STATUS: {status}")

        except Exception as e:
            import traceback
            print(f"  ERROR: {e}")
            traceback.print_exc()
            results["scripts"][name] = {"error": str(e)}
            all_pass = False

    print(f"\n{'=' * 70}")
    print(f"OVERALL: {'ALL PASS' if all_pass else 'SOME FAILURES'}")
    print(f"{'=' * 70}")

    results["overall_pass"] = all_pass
    report_path = os.path.join(OUT_DIR, "regression_report.json")
    with open(report_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nReport saved to {report_path}")


if __name__ == "__main__":
    main()

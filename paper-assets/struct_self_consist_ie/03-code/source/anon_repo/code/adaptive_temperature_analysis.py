#!/usr/bin/env python3
"""Adaptive Temperature Protocol evaluation.

Computes per-dataset degeneracy rates at T=1.0, applies adaptive T switching
(degeneracy > threshold -> T=1.2), and compares LP-selection F1 vs greedy F1.
Uses span-based (start, end, type) F1 with gold_filter=True.
"""

import json
import sys
import os
from collections import Counter
from typing import Any

import numpy as np

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from unified_metrics import compute_entity_f1, compute_degeneracy


def load_samples(path: str) -> list[dict]:
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records






def compute_degeneracy_rate(data: list[dict], n_samples: int = 8) -> tuple[float, int, int]:
    degen = 0
    total = 0
    for inst in data:
        gold_ents = inst["gold"].get("entities", [])
        if len(gold_ents) == 0:
            continue
        samples = inst.get("samples", [])[:n_samples]
        if len(samples) < n_samples:
            continue
        total += 1
        sample_f1s = [compute_entity_f1(s.get("entities", []), gold_ents) for s in samples]
        if compute_degeneracy(sample_f1s):
            degen += 1
    return (degen / total if total else 0.0), degen, total


def compute_greedy_f1_filtered(data: list[dict]) -> tuple[float, list[float]]:
    """Compute macro F1 of greedy decode, filtering gold-empty instances."""
    f1s = []
    for inst in data:
        gold_ents = inst["gold"].get("entities", [])
        if len(gold_ents) == 0:
            continue
        greedy = inst.get("greedy", {})
        greedy_ents = greedy.get("entities", [])
        f1s.append(compute_entity_f1(greedy_ents, gold_ents))
    macro_f1 = float(np.mean(f1s)) if f1s else 0.0
    return macro_f1, f1s


def compute_lp_selection_f1(data: list[dict], n_samples: int = 8) -> tuple[float, list[float]]:
    """Select sample with highest mean_logprob, compute span F1."""
    f1s = []
    for inst in data:
        gold_ents = inst["gold"].get("entities", [])
        if len(gold_ents) == 0:
            continue
        samples = inst.get("samples", [])[:n_samples]
        if not samples:
            continue
        best_idx = 0
        best_lp = -float("inf")
        for i, s in enumerate(samples):
            lp = s.get("mean_logprob", -float("inf"))
            if lp is not None and np.isfinite(lp) and lp > best_lp:
                best_lp = lp
                best_idx = i
        selected = samples[best_idx]
        f1s.append(compute_entity_f1(selected.get("entities", []), gold_ents))
    macro_f1 = float(np.mean(f1s)) if f1s else 0.0
    return macro_f1, f1s


def bootstrap_delta(f1_a: list[float], f1_b: list[float], n_boot: int = 10000, seed: int = 42) -> dict:
    """Bootstrap 95% CI for mean(f1_a) - mean(f1_b)."""
    rng = np.random.RandomState(seed)
    a = np.array(f1_a)
    b = np.array(f1_b)
    n = len(a)
    assert len(b) == n
    observed_delta = float(np.mean(a) - np.mean(b))
    deltas = []
    for _ in range(n_boot):
        idx = rng.choice(n, n, replace=True)
        deltas.append(float(np.mean(a[idx]) - np.mean(b[idx])))
    deltas = np.array(deltas)
    ci_lo = float(np.percentile(deltas, 2.5))
    ci_hi = float(np.percentile(deltas, 97.5))
    p_value = float(np.mean(deltas <= 0))
    return {
        "delta": observed_delta,
        "delta_pp": observed_delta * 100,
        "ci_95": [ci_lo, ci_hi],
        "ci_95_pp": [ci_lo * 100, ci_hi * 100],
        "p_value": p_value,
        "n_boot": n_boot,
    }


def analyze_dataset(t10_path: str, t12_path: str, dataset_name: str,
                    n_samples: int = 8, degen_threshold: float = 0.30) -> dict:
    """Full adaptive-T analysis for one dataset."""
    print(f"\n{'='*60}")
    print(f"  Dataset: {dataset_name}")
    print(f"{'='*60}")

    t10_data = load_samples(t10_path)
    t12_available = os.path.exists(t12_path)

    print(f"  T=1.0 instances: {len(t10_data)}")

    # T=1.0 metrics
    degen_rate_10, degen_count_10, degen_total_10 = compute_degeneracy_rate(t10_data, n_samples)
    greedy_f1_10, greedy_f1s_10 = compute_greedy_f1_filtered(t10_data)
    lp_f1_10, lp_f1s_10 = compute_lp_selection_f1(t10_data, n_samples)

    # Adaptive T decision (based on T=1.0 degeneracy)
    switch_to_12 = degen_rate_10 > degen_threshold

    # T=1.2 metrics (if available)
    if t12_available:
        t12_data = load_samples(t12_path)
        print(f"  T=1.2 instances: {len(t12_data)}")
        degen_rate_12, degen_count_12, degen_total_12 = compute_degeneracy_rate(t12_data, n_samples)
        greedy_f1_12, greedy_f1s_12 = compute_greedy_f1_filtered(t12_data)
        lp_f1_12, lp_f1s_12 = compute_lp_selection_f1(t12_data, n_samples)
    else:
        print(f"  T=1.2 data: NOT AVAILABLE (inference running)")
        t12_data = None
        degen_rate_12, degen_count_12, degen_total_12 = None, None, None
        greedy_f1_12, greedy_f1s_12 = None, None
        lp_f1_12, lp_f1s_12 = None, None

    # Determine adaptive selection
    if switch_to_12:
        if not t12_available:
            print(f"  ERROR: Need T=1.2 data (degen={degen_rate_10:.1%} > {degen_threshold:.0%}) but not available!")
            sys.exit(1)
        adaptive_t = 1.2
        adaptive_lp_f1 = lp_f1_12
        adaptive_lp_f1s = lp_f1s_12
    else:
        adaptive_t = 1.0
        adaptive_lp_f1 = lp_f1_10
        adaptive_lp_f1s = lp_f1s_10

    print(f"\n  T=1.0 degeneracy: {degen_rate_10:.1%} ({degen_count_10}/{degen_total_10})")
    if t12_available:
        print(f"  T=1.2 degeneracy: {degen_rate_12:.1%} ({degen_count_12}/{degen_total_12})")
    print(f"  Threshold: {degen_threshold:.0%} -> {'SWITCH to T=1.2' if switch_to_12 else 'KEEP T=1.0'}")
    print(f"\n  T=1.0 greedy F1:       {greedy_f1_10:.4f}")
    print(f"  T=1.0 LP selection F1: {lp_f1_10:.4f}")
    if t12_available:
        print(f"  T=1.2 LP selection F1: {lp_f1_12:.4f}")
    print(f"  Adaptive LP F1 (T={adaptive_t}): {adaptive_lp_f1:.4f}")

    # Bootstrap: adaptive LP vs T=1.0 greedy
    if switch_to_12 and t12_available:
        # Align instances between T=1.0 and T=1.2
        t10_id_to_greedy_f1 = {}
        for inst in t10_data:
            gold_ents = inst["gold"].get("entities", [])
            if len(gold_ents) == 0:
                continue
            greedy_ents = inst.get("greedy", {}).get("entities", [])
            iid = inst.get("instance_id", inst.get("id"))
            t10_id_to_greedy_f1[iid] = compute_entity_f1(greedy_ents, gold_ents)

        aligned_greedy = []
        aligned_lp = []
        for inst in t12_data:
            gold_ents = inst["gold"].get("entities", [])
            if len(gold_ents) == 0:
                continue
            iid = inst.get("instance_id", inst.get("id"))
            if iid not in t10_id_to_greedy_f1:
                continue
            samples = inst.get("samples", [])[:n_samples]
            if not samples:
                continue
            best_idx = 0
            best_lp = -float("inf")
            for i, s in enumerate(samples):
                lp = s.get("mean_logprob", -float("inf"))
                if lp is not None and np.isfinite(lp) and lp > best_lp:
                    best_lp = lp
                    best_idx = i
            selected = samples[best_idx]
            aligned_lp.append(compute_entity_f1(selected.get("entities", []), gold_ents))
            aligned_greedy.append(t10_id_to_greedy_f1[iid])
    else:
        aligned_greedy = greedy_f1s_10
        aligned_lp = lp_f1s_10

    boot = bootstrap_delta(aligned_lp, aligned_greedy)
    print(f"\n  Adaptive LP - Greedy delta: {boot['delta_pp']:+.2f} pp")
    print(f"  95% CI: [{boot['ci_95_pp'][0]:+.2f}, {boot['ci_95_pp'][1]:+.2f}] pp")
    print(f"  p-value (LP <= Greedy): {boot['p_value']:.4f}")

    # Build result dict
    t10_result = {
        "degeneracy_rate": degen_rate_10,
        "degeneracy_count": degen_count_10,
        "degeneracy_total": degen_total_10,
        "greedy_f1": greedy_f1_10,
        "lp_selection_f1": lp_f1_10,
        "n_instances": len(t10_data),
        "n_gold_filtered": len(greedy_f1s_10),
    }

    t12_result = {}
    if t12_available:
        t12_result = {
            "degeneracy_rate": degen_rate_12,
            "degeneracy_count": degen_count_12,
            "degeneracy_total": degen_total_12,
            "greedy_f1": greedy_f1_12,
            "lp_selection_f1": lp_f1_12,
            "n_instances": len(t12_data),
            "n_gold_filtered": len(greedy_f1s_12),
        }
    else:
        t12_result = {"status": "pending_inference"}

    return {
        "dataset": dataset_name,
        "t10": t10_result,
        "t12": t12_result,
        "adaptive": {
            "degen_threshold": degen_threshold,
            "switch_to_t12": switch_to_12,
            "selected_temperature": adaptive_t,
            "lp_selection_f1": adaptive_lp_f1,
            "greedy_f1_baseline": greedy_f1_10,
            "delta_pp": boot["delta_pp"],
            "bootstrap_ci_95_pp": boot["ci_95_pp"],
            "p_value": boot["p_value"],
            "n_aligned": len(aligned_greedy),
        },
        "degen_reduction": {
            "t10_rate": degen_rate_10,
            "t12_rate": degen_rate_12,
            "reduction_pp": (degen_rate_10 - degen_rate_12) * 100 if degen_rate_12 is not None else None,
        },
    }


def main():
    base = "/root/autodl-tmp/struct_self_consist_ie/output"

    datasets = {
        "scierc": {
            "t10": os.path.join(base, "exp_001_seed42_v2", "samples.jsonl"),
            "t12": os.path.join(base, "exp_026_t12", "samples.jsonl"),
        },
        "conll2003": {
            "t10": os.path.join(base, "exp_002_conll_n8_seed123", "samples.jsonl"),
            "t12": os.path.join(base, "exp_030_conll_t12", "samples.jsonl"),
        },
        "fewnerd": {
            "t10": os.path.join(base, "exp_021_fewnerd_n8_seed123", "samples.jsonl"),
            "t12": os.path.join(base, "exp_031_fewnerd_t12", "samples.jsonl"),
        },
    }

    # Check T=1.0 files exist (required), T=1.2 optional if degen < threshold
    for ds, paths in datasets.items():
        if not os.path.exists(paths["t10"]):
            print(f"MISSING required T=1.0: {ds} -> {paths['t10']}")
            sys.exit(1)

    results = {}
    for ds_name, paths in datasets.items():
        results[ds_name] = analyze_dataset(
            t10_path=paths["t10"],
            t12_path=paths["t12"],
            dataset_name=ds_name,
            n_samples=8,
            degen_threshold=0.30,
        )

    # Summary table
    print(f"\n\n{'='*80}")
    print("  ADAPTIVE TEMPERATURE PROTOCOL — SUMMARY")
    print(f"{'='*80}")
    print(f"  {'Dataset':<12} {'Degen@T1.0':>10} {'Switch?':>8} {'Greedy':>8} {'LP@AdaptT':>10} {'Delta':>8} {'95% CI':>20}")
    print(f"  {'-'*12} {'-'*10} {'-'*8} {'-'*8} {'-'*10} {'-'*8} {'-'*20}")
    for ds in ["scierc", "conll2003", "fewnerd"]:
        r = results[ds]["adaptive"]
        ci = r["bootstrap_ci_95_pp"]
        print(f"  {ds:<12} {results[ds]['t10']['degeneracy_rate']:>9.1%} {'YES' if r['switch_to_t12'] else 'no':>8} "
              f"{r['greedy_f1_baseline']:>8.4f} {r['lp_selection_f1']:>10.4f} "
              f"{r['delta_pp']:>+7.2f} [{ci[0]:+.2f}, {ci[1]:+.2f}]")

    # Save
    out_path = os.path.join(base, "adaptive_temperature_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n  Results saved to {out_path}")


if __name__ == "__main__":
    main()

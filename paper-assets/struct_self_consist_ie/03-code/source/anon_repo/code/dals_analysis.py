#!/usr/bin/env python3
"""DALS (Degeneracy-Aware LP Selection) analysis.

Analyzes whether gating LP selection by LP range (and other proxy variables)
can improve over pure LP selection or pure greedy.
"""

import json
import os
import sys
from itertools import combinations

import numpy as np

BASE = "/root/autodl-tmp/struct_self_consist_ie"

DATASETS = {
    "scierc": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
    "fewnerd": f"{BASE}/output/exp_021_inference/samples.jsonl",
    "conll":   f"{BASE}/output/exp002_conll2003/samples.jsonl",
}

THRESHOLDS = [0.001, 0.005, 0.01, 0.02, 0.03, 0.04, 0.05, 0.07, 0.10]


def load_data(path):
    instances = []
    with open(path) as f:
        for line in f:
            inst = json.loads(line)
            gold_ents = inst["gold"].get("entities", [])
            if len(gold_ents) == 0:
                continue
            instances.append(inst)
    return instances


def entity_set(sample):
    return {(e["text"], e["type"]) for e in sample.get("entities", [])}


def instance_f1(pred_entities, gold_entities):
    pred_set = {(e["text"], e["type"]) for e in pred_entities}
    gold_set = {(e["text"], e["type"]) for e in gold_entities}
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0


def get_greedy_f1(inst):
    return instance_f1(
        inst["greedy"].get("entities", []),
        inst["gold"]["entities"]
    )


def get_lp_sel_f1(inst):
    logprobs = inst["logprobs"]
    best_idx = int(np.argmax(logprobs))
    return instance_f1(
        inst["samples"][best_idx].get("entities", []),
        inst["gold"]["entities"]
    )


def get_lp_range(inst):
    lps = inst["logprobs"]
    return max(lps) - min(lps)


def get_sj(inst):
    samples = inst["samples"]
    sets = [entity_set(s) for s in samples]
    n = len(sets)
    if n < 2:
        return 1.0
    jaccards = []
    for i, j in combinations(range(n), 2):
        union = sets[i] | sets[j]
        if len(union) == 0:
            jaccards.append(1.0)
        else:
            jaccards.append(len(sets[i] & sets[j]) / len(union))
    return np.mean(jaccards)


def get_em_rate(inst):
    samples = inst["samples"]
    sets = [frozenset(entity_set(s)) for s in samples]
    n = len(sets)
    if n < 2:
        return 1.0
    matches = sum(1 for i, j in combinations(range(n), 2) if sets[i] == sets[j])
    total = n * (n - 1) // 2
    return matches / total


def macro_f1(f1_list):
    return np.mean(f1_list) if f1_list else 0.0


def lp_range_stats(instances):
    ranges = [get_lp_range(inst) for inst in instances]
    arr = np.array(ranges)
    return {
        "mean": float(np.mean(arr)),
        "median": float(np.median(arr)),
        "std": float(np.std(arr)),
        "P10": float(np.percentile(arr, 10)),
        "P25": float(np.percentile(arr, 25)),
        "P50": float(np.percentile(arr, 50)),
        "P75": float(np.percentile(arr, 75)),
        "P90": float(np.percentile(arr, 90)),
        "zero_pct": float(np.mean(arr == 0)),
        "n_instances": len(arr),
    }


def dals_sweep(instances, thresholds, proxy_fn, proxy_name="lp_range"):
    greedy_f1s = [get_greedy_f1(inst) for inst in instances]
    lp_f1s = [get_lp_sel_f1(inst) for inst in instances]
    proxy_vals = [proxy_fn(inst) for inst in instances]

    overall_greedy = macro_f1(greedy_f1s)
    overall_lp = macro_f1(lp_f1s)

    results = []
    for tau in thresholds:
        dals_f1s = []
        gated_count = 0
        gated_lp_f1s = []
        gated_greedy_f1s = []

        for i, inst in enumerate(instances):
            if proxy_vals[i] >= tau:
                dals_f1s.append(lp_f1s[i])
                gated_count += 1
                gated_lp_f1s.append(lp_f1s[i])
                gated_greedy_f1s.append(greedy_f1s[i])
            else:
                dals_f1s.append(greedy_f1s[i])

        n = len(instances)
        gated_pct = gated_count / n if n > 0 else 0.0
        gated_lp_delta = (macro_f1(gated_lp_f1s) - macro_f1(gated_greedy_f1s)) if gated_lp_f1s else 0.0
        overall_dals = macro_f1(dals_f1s)

        results.append({
            "threshold": tau,
            "gated_pct": round(gated_pct * 100, 2),
            "gated_lp_delta_pp": round(gated_lp_delta * 100, 4),
            "overall_dals_f1": round(overall_dals * 100, 4),
            "overall_greedy_f1": round(overall_greedy * 100, 4),
            "overall_lp_f1": round(overall_lp * 100, 4),
            "dals_delta_vs_greedy_pp": round((overall_dals - overall_greedy) * 100, 4),
            "dals_delta_vs_lp_pp": round((overall_dals - overall_lp) * 100, 4),
        })

    best = max(results, key=lambda r: r["overall_dals_f1"])
    return {
        "proxy": proxy_name,
        "sweep": results,
        "best_threshold": best["threshold"],
        "best_dals_f1": best["overall_dals_f1"],
        "best_dals_delta_vs_greedy_pp": best["dals_delta_vs_greedy_pp"],
        "best_dals_delta_vs_lp_pp": best["dals_delta_vs_lp_pp"],
        "overall_greedy_f1": results[0]["overall_greedy_f1"],
        "overall_lp_f1": results[0]["overall_lp_f1"],
    }


def oracle_gating(instances):
    greedy_f1s = [get_greedy_f1(inst) for inst in instances]
    lp_f1s = [get_lp_sel_f1(inst) for inst in instances]
    oracle_f1s = [max(g, l) for g, l in zip(greedy_f1s, lp_f1s)]
    lp_chosen = sum(1 for g, l in zip(greedy_f1s, lp_f1s) if l > g)
    greedy_chosen = sum(1 for g, l in zip(greedy_f1s, lp_f1s) if g > l)
    tied = sum(1 for g, l in zip(greedy_f1s, lp_f1s) if g == l)
    return {
        "oracle_f1": round(macro_f1(oracle_f1s) * 100, 4),
        "lp_better_count": lp_chosen,
        "greedy_better_count": greedy_chosen,
        "tied_count": tied,
        "n": len(instances),
    }


def analyze_dataset(name, path):
    print(f"\n{'='*60}")
    print(f"  Dataset: {name}")
    print(f"{'='*60}")

    instances = load_data(path)
    print(f"  Gold-filtered instances: {len(instances)}")

    # 1. LP range distribution
    lp_stats = lp_range_stats(instances)
    print(f"\n  LP Range Distribution:")
    for k, v in lp_stats.items():
        print(f"    {k}: {v:.6f}" if isinstance(v, float) else f"    {k}: {v}")

    # 2. DALS sweep with LP range
    print(f"\n  DALS Sweep (LP Range proxy):")
    lp_sweep = dals_sweep(instances, THRESHOLDS, get_lp_range, "lp_range")
    print(f"    Greedy F1: {lp_sweep['overall_greedy_f1']:.4f}")
    print(f"    LP Sel F1: {lp_sweep['overall_lp_f1']:.4f}")
    print(f"    Best tau={lp_sweep['best_threshold']}, DALS F1={lp_sweep['best_dals_f1']:.4f}, "
          f"d_greedy={lp_sweep['best_dals_delta_vs_greedy_pp']:+.4f}pp, "
          f"d_lp={lp_sweep['best_dals_delta_vs_lp_pp']:+.4f}pp")
    print(f"\n    {'tau':>8} {'gated%':>8} {'gated_d':>10} {'DALS_F1':>10} {'d_greedy':>10} {'d_lp':>10}")
    for r in lp_sweep["sweep"]:
        print(f"    {r['threshold']:8.3f} {r['gated_pct']:7.1f}% {r['gated_lp_delta_pp']:+9.4f} "
              f"{r['overall_dals_f1']:10.4f} {r['dals_delta_vs_greedy_pp']:+9.4f} {r['dals_delta_vs_lp_pp']:+9.4f}")

    # 3. Oracle gating
    oracle = oracle_gating(instances)
    print(f"\n  Oracle Gating: F1={oracle['oracle_f1']:.4f} "
          f"(LP better: {oracle['lp_better_count']}, "
          f"Greedy better: {oracle['greedy_better_count']}, "
          f"Tied: {oracle['tied_count']})")

    # 4. Alternative proxies
    # SJ diversity: 1 - SJ
    sj_thresholds = [0.001, 0.005, 0.01, 0.02, 0.05, 0.10, 0.15, 0.20, 0.30]
    sj_proxy = lambda inst: 1.0 - get_sj(inst)
    print(f"\n  DALS Sweep (SJ Diversity = 1-SJ):")
    sj_sweep = dals_sweep(instances, sj_thresholds, sj_proxy, "sj_diversity")
    print(f"    Best tau={sj_sweep['best_threshold']}, DALS F1={sj_sweep['best_dals_f1']:.4f}, "
          f"d_greedy={sj_sweep['best_dals_delta_vs_greedy_pp']:+.4f}pp, "
          f"d_lp={sj_sweep['best_dals_delta_vs_lp_pp']:+.4f}pp")

    # EM rate: 1 - EM
    em_thresholds = [0.001, 0.01, 0.05, 0.10, 0.15, 0.20, 0.30, 0.50, 0.70]
    em_proxy = lambda inst: 1.0 - get_em_rate(inst)
    print(f"\n  DALS Sweep (EM Diversity = 1-EM):")
    em_sweep = dals_sweep(instances, em_thresholds, em_proxy, "em_diversity")
    print(f"    Best tau={em_sweep['best_threshold']}, DALS F1={em_sweep['best_dals_f1']:.4f}, "
          f"d_greedy={em_sweep['best_dals_delta_vs_greedy_pp']:+.4f}pp, "
          f"d_lp={em_sweep['best_dals_delta_vs_lp_pp']:+.4f}pp")

    return {
        "dataset": name,
        "n_instances": len(instances),
        "lp_range_stats": lp_stats,
        "lp_range_sweep": lp_sweep,
        "sj_diversity_sweep": sj_sweep,
        "em_diversity_sweep": em_sweep,
        "oracle": oracle,
        "baseline_comparison": {
            "pure_greedy_f1": lp_sweep["overall_greedy_f1"],
            "pure_lp_f1": lp_sweep["overall_lp_f1"],
            "dals_best_lp_range_f1": lp_sweep["best_dals_f1"],
            "dals_best_lp_range_tau": lp_sweep["best_threshold"],
            "dals_best_sj_div_f1": sj_sweep["best_dals_f1"],
            "dals_best_sj_div_tau": sj_sweep["best_threshold"],
            "dals_best_em_div_f1": em_sweep["best_dals_f1"],
            "dals_best_em_div_tau": em_sweep["best_threshold"],
            "oracle_f1": oracle["oracle_f1"],
        },
    }


def main():
    all_results = {}
    for name, path in DATASETS.items():
        if not os.path.exists(path):
            print(f"  SKIP {name}: {path} not found")
            continue
        all_results[name] = analyze_dataset(name, path)

    # Summary table
    print(f"\n\n{'='*80}")
    print("  SUMMARY: Baseline Comparison (F1 %)")
    print(f"{'='*80}")
    header = f"  {'Dataset':<10} {'Greedy':>8} {'LP Sel':>8} {'DALS-LP':>8} {'DALS-SJ':>8} {'DALS-EM':>8} {'Oracle':>8}"
    print(header)
    print("  " + "-" * 70)
    for name, res in all_results.items():
        bc = res["baseline_comparison"]
        print(f"  {name:<10} {bc['pure_greedy_f1']:8.2f} {bc['pure_lp_f1']:8.2f} "
              f"{bc['dals_best_lp_range_f1']:8.2f} {bc['dals_best_sj_div_f1']:8.2f} "
              f"{bc['dals_best_em_div_f1']:8.2f} {bc['oracle_f1']:8.2f}")

    print(f"\n  Best Thresholds:")
    for name, res in all_results.items():
        bc = res["baseline_comparison"]
        print(f"  {name:<10} LP-range tau={bc['dals_best_lp_range_tau']:.3f}, "
              f"SJ-div tau={bc['dals_best_sj_div_tau']:.3f}, "
              f"EM-div tau={bc['dals_best_em_div_tau']:.3f}")

    # Save JSON
    out_path = f"{BASE}/output/dals_analysis.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\n  Results saved to {out_path}")


if __name__ == "__main__":
    main()

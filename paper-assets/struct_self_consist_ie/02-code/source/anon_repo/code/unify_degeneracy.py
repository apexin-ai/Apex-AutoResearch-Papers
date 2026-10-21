#!/usr/bin/env python3
"""Unified degeneracy audit: compare KeySet vs Constant-F1 definitions across all T-ablation data.

Target definition: degeneracy = fraction of instances where all N samples produce the same entity-level F1.
"""

import json
import os

BASE = "/root/autodl-tmp/struct_self_consist_ie"
N = 8

EXPERIMENTS = {
    "SciERC": {
        "T=0.5": f"{BASE}/output/exp_026_t05/samples.jsonl",
        "T=0.8": f"{BASE}/output/exp_026_t08/samples.jsonl",
        "T=1.0": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
        "T=1.2": f"{BASE}/output/exp_026_t12/samples.jsonl",
    },
    "CoNLL": {
        "T=1.0": f"{BASE}/output/exp_002_conll_n16/samples.jsonl",
        "T=1.2": f"{BASE}/output/exp_030_conll_t12/samples.jsonl",
    },
    "FewNERD": {
        "T=1.0": f"{BASE}/output/exp_021_fewnerd_n8_seed123/samples.jsonl",
        "T=1.2": f"{BASE}/output/exp_031_fewnerd_t12/samples.jsonl",
    },
}


def load_gold_filtered(path, n_samples=N):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if not obj["gold"].get("entities", []):
                continue
            if len(obj.get("samples", [])) < n_samples:
                continue
            instances.append(obj)
    return instances


def entity_f1(pred_entities, gold_entities):
    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
    if not gold_set and not pred_set:
        return 1.0
    if not gold_set or not pred_set:
        return 0.0
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    return 2 * p * r / (p + r)


def keyset_surface(sample):
    return frozenset((e.get("text", ""), e.get("type", "")) for e in sample.get("entities", []))


def keyset_span(sample):
    return frozenset((e["start"], e["end"], e["type"]) for e in sample.get("entities", []))


def analyze(instances, n_samples=N):
    n_total = len(instances)
    n_cf1 = 0
    n_ks_surface = 0
    n_ks_span = 0

    for inst in instances:
        gold_ents = inst["gold"]["entities"]
        samples = inst["samples"][:n_samples]

        f1s = [entity_f1(s.get("entities", []), gold_ents) for s in samples]
        if len(set(round(f, 10) for f in f1s)) <= 1:
            n_cf1 += 1

        surf_sets = [keyset_surface(s) for s in samples]
        if len(set(surf_sets)) == 1:
            n_ks_surface += 1

        span_sets = [keyset_span(s) for s in samples]
        if len(set(span_sets)) == 1:
            n_ks_span += 1

    return {
        "n_total": n_total,
        "constant_f1": n_cf1,
        "constant_f1_pct": 100.0 * n_cf1 / n_total if n_total else 0,
        "keyset_surface": n_ks_surface,
        "keyset_surface_pct": 100.0 * n_ks_surface / n_total if n_total else 0,
        "keyset_span": n_ks_span,
        "keyset_span_pct": 100.0 * n_ks_span / n_total if n_total else 0,
    }


def main():
    all_results = {}

    for dataset, temp_configs in EXPERIMENTS.items():
        all_results[dataset] = {}
        for temp, path in sorted(temp_configs.items()):
            if not os.path.exists(path):
                print(f"SKIP {dataset} {temp}: {path} not found")
                continue
            instances = load_gold_filtered(path, N)
            r = analyze(instances, N)
            all_results[dataset][temp] = r
            print(f"{dataset:>8} {temp}: N={r['n_total']:>5}  "
                  f"CF1={r['constant_f1_pct']:5.1f}%  "
                  f"KS_surf={r['keyset_surface_pct']:5.1f}%  "
                  f"KS_span={r['keyset_span_pct']:5.1f}%")

    # Summary tables
    print("\n" + "=" * 90)
    print("Unified Degeneracy Comparison: Three Definitions (all N=8, gold-filtered)")
    print("=" * 90)

    for dataset in ["SciERC", "CoNLL", "FewNERD"]:
        if dataset not in all_results:
            continue
        print(f"\n--- {dataset} ---")
        print(f"{'T':>6} | {'#inst':>6} | {'Constant-F1':>12} | {'KeySet(text,type)':>18} | {'KeySet(span)':>13} | {'CF1-KS_surf':>12}")
        print("-" * 85)
        temps = sorted(all_results[dataset].keys())
        for t in temps:
            r = all_results[dataset][t]
            delta = r["constant_f1_pct"] - r["keyset_surface_pct"]
            print(f"{t:>6} | {r['n_total']:>6} | {r['constant_f1_pct']:>11.1f}% | {r['keyset_surface_pct']:>17.1f}% | {r['keyset_span_pct']:>12.1f}% | {delta:>+11.1f}pp")

    # Trend analysis
    print("\n" + "=" * 90)
    print("Trend Direction")
    print("=" * 90)
    print(f"{'Dataset':>8} | {'Definition':>20} | {'Values':>40} | {'Trend':>14}")
    print("-" * 95)
    for dataset in ["SciERC", "CoNLL", "FewNERD"]:
        if dataset not in all_results:
            continue
        temps = sorted(all_results[dataset].keys())
        if len(temps) < 2:
            continue
        for defn, key in [("Constant-F1", "constant_f1_pct"), ("KeySet(text,type)", "keyset_surface_pct")]:
            first_val = all_results[dataset][temps[0]][key]
            last_val = all_results[dataset][temps[-1]][key]
            trend = "T_up->degen_down" if last_val < first_val else "T_up->degen_up" if last_val > first_val else "flat"
            vals = " -> ".join(f"{all_results[dataset][t][key]:.1f}%" for t in temps)
            print(f"{dataset:>8} | {defn:>20} | {vals:>40} | {trend:>14}")

    # Save
    out_path = f"{BASE}/output/unified_degeneracy_audit/unified_degeneracy_3def.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()

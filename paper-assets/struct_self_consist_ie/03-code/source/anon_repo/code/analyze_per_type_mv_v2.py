#!/usr/bin/env python3
"""Per-entity-type MV analysis - multiple thresholds, multiple datasets."""
import json, sys, os
import numpy as np
from collections import Counter, defaultdict
from scipy.stats import pearsonr, spearmanr

BASE = "/root/autodl-tmp/struct_self_consist_ie"

DATASETS = {
    "fewnerd_mf4v2_s42": f"{BASE}/output/fewnerd_mf4v2_seed42/samples.jsonl",
    "fewnerd_exp021_s42": f"{BASE}/output/exp_021_inference/samples.jsonl",
}

def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}

def compute_prf(pred_set, gold_set):
    if not gold_set and not pred_set:
        return 1.0, 1.0, 1.0
    if not pred_set:
        return 0.0, 0.0, 0.0
    if not gold_set:
        return 0.0, 0.0, 0.0
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0, 0.0, 0.0
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    f = 2 * p * r / (p + r)
    return p, r, f

def entity_majority_vote(samples, threshold):
    entity_counts = Counter()
    N = len(samples)
    for s in samples:
        seen = set()
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_counts[key] += 1
                seen.add(key)
    constructed = set()
    for key, count in entity_counts.items():
        if count / N >= threshold:
            constructed.add(key)
    return constructed

def get_dominant_type(gold_entities):
    if not gold_entities:
        return None
    type_counts = Counter(e.get("type", "other") for e in gold_entities)
    return type_counts.most_common(1)[0][0]

def load_data(path):
    instances = []
    with open(path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))
    return instances

def analyze_dataset(data, thresholds=[0.25, 0.375, 0.5]):
    filtered = [inst for inst in data if inst["gold"].get("entities", [])]
    
    type_groups = defaultdict(list)
    for inst in filtered:
        dtype = get_dominant_type(inst["gold"]["entities"])
        type_groups[dtype].append(inst)
    
    results = {}
    for theta in thresholds:
        type_results = {}
        for etype, group in type_groups.items():
            greedy_f1s, mv_f1s = [], []
            for inst in group:
                gold = entity_set(inst["gold"]["entities"])
                greedy = inst.get("greedy", inst["samples"][0])
                pred_greedy = entity_set(greedy.get("entities", []))
                _, _, f_g = compute_prf(pred_greedy, gold)
                greedy_f1s.append(f_g)
                pred_mv = entity_majority_vote(inst["samples"], theta)
                _, _, f_mv = compute_prf(pred_mv, gold)
                mv_f1s.append(f_mv)
            type_results[etype] = {
                "n": len(group),
                "greedy_f1": float(np.mean(greedy_f1s)),
                "mv_f1": float(np.mean(mv_f1s)),
                "mv_delta_pp": float((np.mean(mv_f1s) - np.mean(greedy_f1s)) * 100),
            }
        
        types = sorted(type_results.keys())
        g_vals = np.array([type_results[t]["greedy_f1"] for t in types])
        d_vals = np.array([type_results[t]["mv_delta_pp"] for t in types])
        r_p, p_p = pearsonr(g_vals, d_vals)
        r_s, p_s = spearmanr(g_vals, d_vals)
        
        results[f"theta_{theta}"] = {
            "types": type_results,
            "pearson_r": float(r_p), "pearson_p": float(p_p),
            "spearman_rho": float(r_s), "spearman_p": float(p_s),
        }
    return results

for ds_name, path in DATASETS.items():
    if not os.path.exists(path):
        print(f"{ds_name}: NOT FOUND")
        continue
    print(f"\n{'='*80}")
    print(f"Dataset: {ds_name}")
    print(f"{'='*80}")
    data = load_data(path)
    results = analyze_dataset(data)
    
    for theta_key, res in results.items():
        theta = float(theta_key.split("_")[1])
        print(f"\n--- θ={theta} ---")
        print(f"{'Type':<14} {'N':>6} {'Greedy':>8} {'MV':>8} {'Δ(pp)':>8}")
        for t in sorted(res["types"], key=lambda x: -res["types"][x]["mv_delta_pp"]):
            tr = res["types"][t]
            print(f"{t:<14} {tr['n']:>6} {tr['greedy_f1']:>8.4f} {tr['mv_f1']:>8.4f} {tr['mv_delta_pp']:>+7.2f}")
        print(f"Pearson r={res['pearson_r']:.4f} (p={res['pearson_p']:.6f})")
        print(f"Spearman ρ={res['spearman_rho']:.4f} (p={res['spearman_p']:.6f})")

#!/usr/bin/env python3
"""Per-entity-type MV (majority vote) analysis for finetuned FewNERD."""
import json, sys, os
import numpy as np
from collections import Counter, defaultdict
from scipy.stats import pearsonr, spearmanr

BASE = "/root/autodl-tmp/struct_self_consist_ie"
SEEDS = {
    42: f"{BASE}/output/fewnerd_mf4v2_seed42/samples.jsonl",
    123: f"{BASE}/output/fewnerd_mf4v2_seed123/samples.jsonl",
    456: f"{BASE}/output/fewnerd_mf4v2_seed456/samples.jsonl",
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

def entity_majority_vote(samples, threshold=0.25):
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

def analyze_seed(data, seed_id):
    filtered = [inst for inst in data if inst["gold"].get("entities", [])]
    print(f"  Seed {seed_id}: {len(data)} total, {len(filtered)} with gold entities")
    
    type_groups = defaultdict(list)
    for inst in filtered:
        dtype = get_dominant_type(inst["gold"]["entities"])
        type_groups[dtype].append(inst)
    
    theta = 0.25  # 2/N for N=8
    results = {}
    
    for etype, group in type_groups.items():
        n = len(group)
        greedy_f1s = []
        mv_f1s = []
        
        for inst in group:
            gold = entity_set(inst["gold"]["entities"])
            greedy = inst.get("greedy", inst["samples"][0])
            pred_greedy = entity_set(greedy.get("entities", []))
            _, _, f_greedy = compute_prf(pred_greedy, gold)
            greedy_f1s.append(f_greedy)
            
            pred_mv = entity_majority_vote(inst["samples"], theta)
            _, _, f_mv = compute_prf(pred_mv, gold)
            mv_f1s.append(f_mv)
        
        greedy_f1 = float(np.mean(greedy_f1s))
        mv_f1 = float(np.mean(mv_f1s))
        mv_delta = (mv_f1 - greedy_f1) * 100
        
        results[etype] = {
            "n_instances": n,
            "greedy_f1": greedy_f1,
            "mv_strict_f1": mv_f1,
            "mv_delta_pp": mv_delta,
        }
    
    return results

def main():
    all_seed_results = {}
    
    for seed, path in sorted(SEEDS.items()):
        if not os.path.exists(path):
            print(f"  Seed {seed}: NOT FOUND ({path})")
            continue
        data = load_data(path)
        all_seed_results[seed] = analyze_seed(data, seed)
    
    # Average across seeds
    all_types = set()
    for sr in all_seed_results.values():
        all_types.update(sr.keys())
    
    print(f"\n{'='*100}")
    print(f"Seeds available: {sorted(all_seed_results.keys())}")
    print(f"Entity types: {sorted(all_types)}")
    
    # Compute per-type averages across seeds
    type_avg = {}
    for etype in sorted(all_types):
        n_list, gf1_list, mvf1_list, delta_list = [], [], [], []
        for seed, sr in all_seed_results.items():
            if etype in sr:
                n_list.append(sr[etype]["n_instances"])
                gf1_list.append(sr[etype]["greedy_f1"])
                mvf1_list.append(sr[etype]["mv_strict_f1"])
                delta_list.append(sr[etype]["mv_delta_pp"])
        type_avg[etype] = {
            "n_seeds": len(gf1_list),
            "n_instances_mean": float(np.mean(n_list)),
            "greedy_f1_mean": float(np.mean(gf1_list)),
            "greedy_f1_std": float(np.std(gf1_list)),
            "mv_strict_f1_mean": float(np.mean(mvf1_list)),
            "mv_strict_f1_std": float(np.std(mvf1_list)),
            "mv_delta_pp_mean": float(np.mean(delta_list)),
            "mv_delta_pp_std": float(np.std(delta_list)),
        }
    
    # Print table
    print(f"\n{'Type':<14} {'N':>6} {'Seeds':>5} {'Greedy F1':>12} {'MV F1':>12} {'MV Δ (pp)':>12}")
    print("-" * 70)
    for etype in sorted(type_avg.keys(), key=lambda t: -type_avg[t]["mv_delta_pp_mean"]):
        ta = type_avg[etype]
        print(f"{etype:<14} {ta['n_instances_mean']:>6.0f} {ta['n_seeds']:>5} "
              f"{ta['greedy_f1_mean']:>10.4f}±{ta['greedy_f1_std']:.4f} "
              f"{ta['mv_strict_f1_mean']:>10.4f}±{ta['mv_strict_f1_std']:.4f} "
              f"{ta['mv_delta_pp_mean']:>+8.2f}±{ta['mv_delta_pp_std']:.2f}")
    
    # Correlation: greedy_f1 vs mv_delta
    greedy_vals = np.array([type_avg[t]["greedy_f1_mean"] for t in sorted(type_avg)])
    delta_vals = np.array([type_avg[t]["mv_delta_pp_mean"] for t in sorted(type_avg)])
    
    print(f"\n{'='*70}")
    print("Correlation Analysis: greedy_f1 vs MV_delta")
    print(f"{'='*70}")
    
    if len(greedy_vals) >= 3:
        r_pearson, p_pearson = pearsonr(greedy_vals, delta_vals)
        r_spearman, p_spearman = spearmanr(greedy_vals, delta_vals)
        print(f"Pearson  r={r_pearson:.4f}, p={p_pearson:.6f}")
        print(f"Spearman ρ={r_spearman:.4f}, p={p_spearman:.6f}")
    
    # Also do per-seed correlation
    print(f"\nPer-seed correlations:")
    for seed, sr in sorted(all_seed_results.items()):
        types = sorted(sr.keys())
        g_vals = np.array([sr[t]["greedy_f1"] for t in types])
        d_vals = np.array([sr[t]["mv_delta_pp"] for t in types])
        if len(g_vals) >= 3:
            r, p = pearsonr(g_vals, d_vals)
            rs, ps = spearmanr(g_vals, d_vals)
            print(f"  Seed {seed}: Pearson r={r:.4f} (p={p:.6f}), Spearman ρ={rs:.4f} (p={ps:.6f})")
    
    # Save JSON
    output = {
        "dataset": "FewNERD finetuned 3-epoch",
        "seeds": sorted(all_seed_results.keys()),
        "n_samples": 8,
        "theta": 0.25,
        "per_type": type_avg,
        "per_seed_raw": {str(s): v for s, v in all_seed_results.items()},
    }
    if len(greedy_vals) >= 3:
        output["correlation"] = {
            "pearson_r": float(r_pearson),
            "pearson_p": float(p_pearson),
            "spearman_rho": float(r_spearman),
            "spearman_p": float(p_spearman),
        }
    
    out_path = f"{BASE}/output/fewnerd_per_type_mv_analysis.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")

if __name__ == "__main__":
    main()

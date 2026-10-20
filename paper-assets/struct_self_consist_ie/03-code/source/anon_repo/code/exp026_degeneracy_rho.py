#!/usr/bin/env python3
"""Task 1: Correct degeneracy (Constant F1, gold-filtered)
   Task 2: Within-instance Spearman rho(LP, F1)
"""
import json
import numpy as np
from scipy.stats import spearmanr

BASE = "/root/autodl-tmp/struct_self_consist_ie"
N = 8

TEMP_CONFIGS = {
    "T=0.5": f"{BASE}/output/exp_026_T05/samples.jsonl",
    "T=0.8": f"{BASE}/output/exp_026_T08/samples.jsonl",
    "T=1.0": f"{BASE}/output/exp_012_logprob/samples_with_logprobs.jsonl",
    "T=1.2": f"{BASE}/output/exp_026_T12/samples.jsonl",
}

def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f]

def entity_strict_f1(pred_entities, gold_entities):
    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    return f1

def get_sample_lp(sample, inst_logprobs, idx):
    """Get mean logprob for a sample, trying multiple field names."""
    if "mean_logprob" in sample:
        return sample["mean_logprob"]
    if inst_logprobs is not None and idx < len(inst_logprobs):
        return inst_logprobs[idx]
    return None

def analyze(name, path):
    data = load_data(path)
    
    # Task 1: Constant F1, gold-filtered degeneracy
    gold_filtered_total = 0
    constant_f1_count = 0
    
    # Task 2: Within-instance rho
    rho_values = []
    
    for inst in data:
        gold = inst["gold"]
        gold_entities = gold.get("entities", [])
        samples = inst.get("samples", [])[:N]
        if len(samples) < N:
            continue
        
        # Compute per-sample F1
        f1s = [entity_strict_f1(s.get("entities", []), gold_entities) for s in samples]
        
        # Get per-sample LP
        inst_logprobs = inst.get("logprobs", None)
        lps = []
        for idx, s in enumerate(samples):
            lp = get_sample_lp(s, inst_logprobs, idx)
            if lp is not None:
                lps.append(lp)
        
        # Task 1: Gold-filtered = gold entities non-empty
        if len(gold_entities) > 0:
            gold_filtered_total += 1
            # Constant F1: all 8 samples have same F1
            if len(set(round(f, 10) for f in f1s)) == 1:
                constant_f1_count += 1
        
        # Task 2: Within-instance rho(LP, F1)
        if len(lps) == N:
            f1_arr = np.array(f1s)
            lp_arr = np.array(lps)
            # Skip if either has zero variance
            if np.std(f1_arr) > 0 and np.std(lp_arr) > 0:
                rho, _ = spearmanr(lp_arr, f1_arr)
                if np.isfinite(rho):
                    rho_values.append(rho)
    
    degeneracy_rate = constant_f1_count / gold_filtered_total if gold_filtered_total > 0 else 0.0
    
    rho_arr = np.array(rho_values) if rho_values else np.array([])
    valid_frac = len(rho_values) / gold_filtered_total if gold_filtered_total > 0 else 0.0
    
    result = {
        "temperature": name,
        "degeneracy": {
            "gold_filtered_total": gold_filtered_total,
            "constant_f1_count": constant_f1_count,
            "degeneracy_rate": degeneracy_rate,
        },
        "within_instance_rho": {
            "mean": float(np.mean(rho_arr)) if len(rho_arr) > 0 else None,
            "median": float(np.median(rho_arr)) if len(rho_arr) > 0 else None,
            "std": float(np.std(rho_arr)) if len(rho_arr) > 0 else None,
            "valid_count": len(rho_values),
            "total_gold_filtered": gold_filtered_total,
            "valid_fraction": valid_frac,
        }
    }
    return result

def main():
    all_results = {}
    for name, path in TEMP_CONFIGS.items():
        print(f"\n{'='*50}")
        print(f"  {name}")
        print(f"{'='*50}")
        r = analyze(name, path)
        all_results[name] = r
        d = r["degeneracy"]
        print(f"  Degeneracy (Constant F1, gold-filtered): {d['constant_f1_count']}/{d['gold_filtered_total']} = {d['degeneracy_rate']:.4f}")
        rho = r["within_instance_rho"]
        if rho["mean"] is not None:
            print(f"  Within-instance rho(LP,F1): mean={rho['mean']:.4f}, median={rho['median']:.4f}, std={rho['std']:.4f}, valid={rho['valid_fraction']:.4f}")
        else:
            print(f"  Within-instance rho: NO VALID INSTANCES")
    
    # Summary tables
    print("\n\n## Task 1: Degeneracy (Constant F1, gold-filtered)")
    print("| T | degeneracy_rate | count/total |")
    print("|---|-----------------|-------------|")
    for t in ["T=0.5", "T=0.8", "T=1.0", "T=1.2"]:
        d = all_results[t]["degeneracy"]
        print(f"| {t} | {d['degeneracy_rate']:.4f} | {d['constant_f1_count']}/{d['gold_filtered_total']} |")
    
    print("\n## Task 2: Within-instance rho(LP, F1)")
    print("| T | mean rho | median rho | std | valid% |")
    print("|---|----------|------------|-----|--------|")
    for t in ["T=0.5", "T=0.8", "T=1.0", "T=1.2"]:
        rho = all_results[t]["within_instance_rho"]
        if rho["mean"] is not None:
            print(f"| {t} | {rho['mean']:.4f} | {rho['median']:.4f} | {rho['std']:.4f} | {rho['valid_fraction']*100:.1f}% |")
        else:
            print(f"| {t} | N/A | N/A | N/A | 0% |")
    
    # Also compare with old KeySet definition
    print("\n## Comparison: Old (KeySet) vs New (Constant F1) degeneracy")
    old_values = {"T=0.5": 0.3285, "T=0.8": 0.1960, "T=1.0": 0.1270, "T=1.2": 0.0799}
    print("| T | Old (KeySet) | New (Constant F1) | Delta |")
    print("|---|--------------|-------------------|-------|")
    for t in ["T=0.5", "T=0.8", "T=1.0", "T=1.2"]:
        old = old_values[t]
        new = all_results[t]["degeneracy"]["degeneracy_rate"]
        print(f"| {t} | {old:.4f} | {new:.4f} | {new-old:+.4f} |")
    
    # Save JSON
    out = json.dumps(all_results, indent=2)
    print(f"\n\nJSON output:\n{out}")

if __name__ == "__main__":
    main()

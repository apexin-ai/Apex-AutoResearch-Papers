#!/usr/bin/env python3
"""Recompute all tab:fewnerd metrics from raw samples.jsonl files.

Computes: greedy_f1, oracle_f1, headroom, lp_sel_f1, lp_delta, lp_rho, degeneracy
for both full-set and gold-filtered subsets.
"""

import json
import sys
import os
import numpy as np
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import per_instance_f1, entity_strict_match

SUBTASK = "ner"

def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]

def compute_metrics(data, label="full-set"):
    N = len(data)
    if N == 0:
        print(f"  [{label}] No instances!")
        return {}

    n_samples = len(data[0]["samples"])
    
    greedy_f1s = []
    oracle_f1s = []
    lp_sel_f1s = []
    degen_f1_flags = []  # all N samples have identical F1
    degen_keyset_flags = []  # all N samples have identical entity key sets
    
    # For pooled Spearman: (LP, F1) across all (instance, sample) pairs
    all_lp = []
    all_f1 = []
    
    # For instance-level Spearman: max_LP vs greedy_F1
    max_lp_per_instance = []
    
    for inst in data:
        gold = inst["gold"]
        greedy = inst["greedy"]
        samples = inst["samples"]
        
        # Greedy F1
        g_f1 = per_instance_f1(greedy, gold, SUBTASK)
        greedy_f1s.append(g_f1)
        
        # Per-sample F1 and LP
        sample_f1s = []
        sample_lps = []
        for s in samples:
            f1 = per_instance_f1(s, gold, SUBTASK)
            sample_f1s.append(f1)
            
            lp = s.get("mean_logprob")
            if lp is None:
                lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
            sample_lps.append(lp)
        
        # Oracle F1
        oracle_f1s.append(max(sample_f1s))
        
        # LP selection
        lp_sel_idx = int(np.argmax(sample_lps))
        lp_sel_f1s.append(sample_f1s[lp_sel_idx])
        
        # Degeneracy (F1-based)
        degen_f1_flags.append(len(set(sample_f1s)) == 1)
        
        # Degeneracy (key-set-based) 
        key_sets = []
        for s in samples:
            ks = frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
            key_sets.append(ks)
        degen_keyset_flags.append(len(set(key_sets)) == 1)
        
        # Pooled correlations
        all_lp.extend(sample_lps)
        all_f1.extend(sample_f1s)
        
        # Instance-level max LP
        max_lp_per_instance.append(max(sample_lps))
    
    greedy_f1s = np.array(greedy_f1s)
    oracle_f1s = np.array(oracle_f1s)
    lp_sel_f1s = np.array(lp_sel_f1s)
    
    greedy_macro = float(greedy_f1s.mean())
    oracle_macro = float(oracle_f1s.mean())
    lp_sel_macro = float(lp_sel_f1s.mean())
    headroom_pp = (oracle_macro - greedy_macro) * 100
    lp_delta_pp = (lp_sel_macro - greedy_macro) * 100
    
    degen_f1_rate = float(np.mean(degen_f1_flags)) * 100
    degen_keyset_rate = float(np.mean(degen_keyset_flags)) * 100
    
    # Pooled Spearman (LP vs F1 across all instance-sample pairs)
    rho_pooled, p_pooled = spearmanr(all_lp, all_f1)
    
    # Instance-level Spearman (max_LP vs greedy_F1)
    rho_inst, p_inst = spearmanr(max_lp_per_instance, greedy_f1s)
    
    results = {
        "n": N,
        "n_samples": n_samples,
        "greedy_f1": greedy_macro,
        "oracle_f1": oracle_macro,
        "lp_sel_f1": lp_sel_macro,
        "headroom_pp": headroom_pp,
        "lp_delta_pp": lp_delta_pp,
        "degen_f1_pct": degen_f1_rate,
        "degen_keyset_pct": degen_keyset_rate,
        "lp_rho_pooled": float(rho_pooled),
        "lp_rho_pooled_p": float(p_pooled),
        "lp_rho_inst": float(rho_inst),
        "lp_rho_inst_p": float(p_inst),
    }
    
    print(f"\n  [{label}] n={N}, N_samples={n_samples}")
    print(f"  greedy_f1:       {greedy_macro:.4f}")
    print(f"  oracle_f1:       {oracle_macro:.4f}")
    print(f"  headroom:        {headroom_pp:.2f}pp")
    print(f"  lp_sel_f1:       {lp_sel_macro:.4f}")
    print(f"  lp_delta:        {lp_delta_pp:+.2f}pp")
    print(f"  degen (F1):      {degen_f1_rate:.1f}%")
    print(f"  degen (keyset):  {degen_keyset_rate:.1f}%")
    print(f"  lp_rho (pooled): {float(rho_pooled):.4f} (p={float(p_pooled):.2e})")
    print(f"  lp_rho (inst):   {float(rho_inst):.4f} (p={float(p_inst):.2e})")
    
    return results


def process_dataset(name, path):
    print(f"\n{'='*70}")
    print(f"DATASET: {name}")
    print(f"Path: {path}")
    print(f"{'='*70}")
    
    if not os.path.exists(path):
        print(f"  ERROR: File not found!")
        return None, None
    
    data = load_data(path)
    print(f"  Total instances loaded: {len(data)}")
    
    # Full set
    full_results = compute_metrics(data, "full-set")
    
    # Gold-filtered
    gold_filtered = [d for d in data if len(d["gold"].get("entities", [])) > 0]
    print(f"\n  Gold-filtered: {len(gold_filtered)} (removed {len(data) - len(gold_filtered)} empty-gold)")
    gold_results = compute_metrics(gold_filtered, "gold-filtered")
    
    return full_results, gold_results


if __name__ == "__main__":
    base = "/root/autodl-tmp/struct_self_consist_ie"
    
    datasets = {
        "SciERC (exp_012_rerun_1024)": os.path.join(base, "output/exp_012_rerun_1024/samples.jsonl"),
        "Few-NERD (exp_021_inference)": os.path.join(base, "output/exp_021_inference/samples.jsonl"),
        "CoNLL (exp_002_conll_n16_r1024)": os.path.join(base, "output/exp_002_conll_n16_r1024/samples.jsonl"),
        "CoNLL (exp_017_llama_conll_n8_t07)": os.path.join(base, "output/exp_017_llama_conll_n8_t07/samples.jsonl"),
        "CoNLL (exp_017_llama_conll_n16_r1024)": os.path.join(base, "output/exp_017_llama_conll_n16_r1024/samples.jsonl"),
    }
    
    all_results = {}
    for name, path in datasets.items():
        full_r, gold_r = process_dataset(name, path)
        all_results[name] = {"full": full_r, "gold_filtered": gold_r}
    
    # Save results
    out_path = os.path.join(base, "output/recompute_tab_fewnerd_results.json")
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\n\nResults saved to {out_path}")

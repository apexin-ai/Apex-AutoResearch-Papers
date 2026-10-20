#!/usr/bin/env python3
"""Compute LP rho with multiple definitions to trace paper values."""

import json
import sys
import numpy as np
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import per_instance_f1, entity_strict_match, compute_ner_f1

SUBTASK = "ner"

def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]

def analyze(name, data):
    N = len(data)
    n_samples = len(data[0]["samples"])
    
    greedy_f1s = []  # per-instance F1 (for macro)
    max_lp_per_inst = []
    mean_lp_per_inst = []
    greedy_lp_per_inst = []
    
    # For micro F1
    greedy_preds = []
    golds = []
    
    # For pooled LP-F1 correlation
    all_sample_lp = []
    all_sample_f1 = []
    
    for inst in data:
        gold = inst["gold"]
        greedy = inst["greedy"]
        samples = inst["samples"]
        
        g_f1 = per_instance_f1(greedy, gold, SUBTASK)
        greedy_f1s.append(g_f1)
        greedy_preds.append(greedy)
        golds.append(gold)
        
        # Greedy LP
        g_lp = greedy.get("mean_logprob")
        if g_lp is None:
            g_lp = greedy.get("cumulative_logprob", -999) / max(greedy.get("n_tokens", 1), 1)
        greedy_lp_per_inst.append(g_lp)
        
        # Sample LPs
        sample_lps = []
        sample_f1s = []
        for s in samples:
            lp = s.get("mean_logprob")
            if lp is None:
                lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
            sample_lps.append(lp)
            f1 = per_instance_f1(s, gold, SUBTASK)
            sample_f1s.append(f1)
        
        max_lp_per_inst.append(max(sample_lps))
        mean_lp_per_inst.append(np.mean(sample_lps))
        all_sample_lp.extend(sample_lps)
        all_sample_f1.extend(sample_f1s)
    
    # Micro F1
    micro = compute_ner_f1(greedy_preds, golds)
    macro_f1 = np.mean(greedy_f1s)
    
    # LP correlations
    rho_maxlp_greedyf1, _ = spearmanr(max_lp_per_inst, greedy_f1s)
    rho_meanlp_greedyf1, _ = spearmanr(mean_lp_per_inst, greedy_f1s)
    rho_greedylp_greedyf1, _ = spearmanr(greedy_lp_per_inst, greedy_f1s)
    rho_pooled, _ = spearmanr(all_sample_lp, all_sample_f1)
    
    print(f"\n{name} (n={N}, N_samples={n_samples})")
    print(f"  Greedy micro-F1:  {micro['f1']:.4f}")
    print(f"  Greedy macro-F1:  {macro_f1:.4f}")
    print(f"  LP rho variants:")
    print(f"    max_LP vs greedy_F1:     {rho_maxlp_greedyf1:.4f}")
    print(f"    mean_LP vs greedy_F1:    {rho_meanlp_greedyf1:.4f}")
    print(f"    greedy_LP vs greedy_F1:  {rho_greedylp_greedyf1:.4f}")
    print(f"    pooled (all samples):    {rho_pooled:.4f}")

if __name__ == "__main__":
    base = "/root/autodl-tmp/struct_self_consist_ie"
    
    datasets = [
        ("SciERC exp_012_rerun_1024", f"{base}/output/exp_012_rerun_1024/samples.jsonl"),
        ("CoNLL exp_002_conll_n16_r1024", f"{base}/output/exp_002_conll_n16_r1024/samples.jsonl"),
    ]
    
    for name, path in datasets:
        data = load_data(path)
        
        # Full set
        analyze(f"{name} [full-set]", data)
        
        # Gold filtered
        gf = [d for d in data if len(d["gold"].get("entities", [])) > 0]
        analyze(f"{name} [gold-filtered]", gf)

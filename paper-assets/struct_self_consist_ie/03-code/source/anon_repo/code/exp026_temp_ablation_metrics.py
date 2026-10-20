#!/usr/bin/env python3
"""Compute missing metrics for exp-026 Temperature Ablation.

Metrics per temperature:
1. Degeneracy rate (exact duplicate KeySet: text+type)
2. LP within-instance range (mean/std of max-min across N=8)
3. LP selection F1 (+ greedy/oracle/random baselines)
4. All 5 signals selection F1 (SJ, FK, EM, VC, LP)
5. QE metrics: rho(signal, F1) and AUROC for all 5 signals
"""

import json
import sys
import os
import numpy as np
from collections import Counter
from itertools import combinations
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import per_instance_f1, entity_strict_match

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

def entity_surface_set(ext):
    return frozenset((e["text"], e["type"]) for e in ext.get("entities", []))

def compute_degeneracy(data, n_samples=N):
    """Fraction of instances where all N samples have identical KeySet."""
    degenerate = 0
    total = 0
    for inst in data:
        samples = inst.get("samples", [])[:n_samples]
        if len(samples) < n_samples:
            continue
        total += 1
        keys = [entity_surface_set(s) for s in samples]
        unique_keys = set(keys)
        if len(unique_keys) == 1:
            degenerate += 1
    return degenerate / total if total else 0.0, degenerate, total

def compute_lp_range(data, n_samples=N):
    """Per-instance LP range (max - min of mean_logprob across N samples)."""
    ranges = []
    for inst in data:
        samples = inst.get("samples", [])[:n_samples]
        if len(samples) < n_samples:
            continue
        lps = [s["mean_logprob"] for s in samples if "mean_logprob" in s]
        if len(lps) >= 2:
            ranges.append(max(lps) - min(lps))
    return float(np.mean(ranges)), float(np.std(ranges)), ranges

def compute_sj(samples):
    """Soft Jaccard: mean pairwise Jaccard of entity surface sets."""
    sets = [entity_surface_set(s) for s in samples]
    if len(sets) < 2:
        return 1.0
    scores = []
    for i, j in combinations(range(len(sets)), 2):
        union = len(sets[i] | sets[j])
        scores.append(len(sets[i] & sets[j]) / union if union else 1.0)
    return float(np.mean(scores))

def compute_fk(samples, n_samples=N):
    """Fleiss' Kappa for entity surface keys."""
    ent_sets = [{(e["text"], e["type"]) for e in s.get("entities", [])} for s in samples]
    all_ents = set().union(*ent_sets)
    if not all_ents:
        return 0.0
    n_sub = len(all_ents)
    ratings = np.zeros((n_sub, 2))
    for idx, ent in enumerate(all_ents):
        present = sum(1 for es in ent_sets if ent in es)
        ratings[idx] = [n_samples - present, present]
    P_i = (np.sum(ratings**2, axis=1) - n_samples) / (n_samples * (n_samples - 1))
    P_bar = np.mean(P_i)
    p_j = np.sum(ratings, axis=0) / (n_sub * n_samples)
    P_e = np.sum(p_j**2)
    if P_e >= 1.0:
        return 1.0
    return float((P_bar - P_e) / (1 - P_e))

def compute_em(samples):
    """Exact Match frequency: fraction of most common KeySet."""
    keys = [entity_surface_set(s) for s in samples]
    return Counter(keys).most_common(1)[0][1] / len(samples)

def compute_vc(samples, n_samples=N):
    """Verbalized Confidence proxy: mean rate of majority-voted entities."""
    counter = Counter()
    for s in samples:
        for e in s.get("entities", []):
            counter[(e["text"], e["type"])] += 1
    rates = [v / n_samples for v in counter.values() if v > n_samples / 2]
    return float(np.mean(rates)) if rates else 0.0

def compute_lp_signal(samples):
    """Mean log-probability across samples."""
    lps = [s["mean_logprob"] for s in samples if "mean_logprob" in s]
    return float(np.mean(lps)) if lps else float("nan")

def compute_auroc(scores, labels):
    scores = np.array(scores, dtype=float)
    labels = np.array(labels)
    n_pos = int(np.sum(labels == 1))
    n_neg = int(np.sum(labels == 0))
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    order = np.argsort(scores)
    sorted_labels = labels[order]
    ranks = np.arange(1, len(scores) + 1, dtype=float)
    u = np.sum(ranks[sorted_labels == 1]) - n_pos * (n_pos + 1) / 2
    return float(u / (n_pos * n_neg))

def selection_f1(data, signal_fn, n_samples=N, subtask="ner"):
    """Select best sample by signal, return mean per-instance F1."""
    f1s = []
    for inst in data:
        samples = inst.get("samples", [])[:n_samples]
        gold = inst["gold"]
        if len(samples) < n_samples:
            continue
        scores = []
        for s in samples:
            scores.append(signal_fn(samples, s, inst))
        best_idx = int(np.argmax(scores))
        f1s.append(per_instance_f1(samples[best_idx], gold, subtask))
    return float(np.mean(f1s)) if f1s else 0.0

def sj_signal(samples, s, inst):
    """SJ score for a single sample against all others."""
    s_set = entity_surface_set(s)
    others = [entity_surface_set(o) for o in samples if o is not s]
    if not others:
        return 0.0
    jaccards = []
    for o_set in others:
        union = len(s_set | o_set)
        jaccards.append(len(s_set & o_set) / union if union else 1.0)
    return float(np.mean(jaccards))

def fk_signal(samples, s, inst):
    """FK is instance-level, not per-sample. Use EM as proxy per-sample."""
    return em_signal(samples, s, inst)

def em_signal(samples, s, inst):
    """EM: how many other samples have the same KeySet."""
    s_key = entity_surface_set(s)
    return sum(1 for o in samples if entity_surface_set(o) == s_key)

def vc_signal(samples, s, inst):
    """VC: mean voting rate of entities in this sample."""
    counter = Counter()
    n = len(samples)
    for o in samples:
        for e in o.get("entities", []):
            counter[(e["text"], e["type"])] += 1
    s_ents = [(e["text"], e["type"]) for e in s.get("entities", [])]
    if not s_ents:
        return 0.0
    return float(np.mean([counter[k] / n for k in s_ents]))

def lp_signal(samples, s, inst):
    """LP: mean log-probability of this sample."""
    return s.get("mean_logprob", float("-inf"))

def analyze_temperature(name, path):
    print(f"\n{'='*60}")
    print(f"Analyzing {name}: {path}")
    print(f"{'='*60}")
    
    data = load_data(path)
    n_inst = len(data)
    print(f"  Loaded {n_inst} instances")
    
    # Filter to valid instances with N samples
    valid = [d for d in data if len(d.get("samples", [])) >= N]
    print(f"  Valid (>={N} samples): {len(valid)}")
    
    results = {"temperature": name, "n_instances": len(valid)}
    
    # 1. Degeneracy rate
    deg_rate, deg_count, deg_total = compute_degeneracy(valid)
    results["degeneracy_rate"] = deg_rate
    results["degeneracy_count"] = deg_count
    print(f"  Degeneracy: {deg_rate:.4f} ({deg_count}/{deg_total})")
    
    # 2. LP range
    lp_mean, lp_std, lp_ranges = compute_lp_range(valid)
    results["lp_range_mean"] = lp_mean
    results["lp_range_std"] = lp_std
    print(f"  LP range: mean={lp_mean:.6f}, std={lp_std:.6f}")
    
    # 3 & 4. Selection F1 for all signals + greedy/oracle/random
    greedy_f1s = []
    oracle_f1s = []
    random_f1s = []
    sj_sel_f1s = []
    fk_sel_f1s = []  # FK is instance-level; use EM for selection
    em_sel_f1s = []
    vc_sel_f1s = []
    lp_sel_f1s = []
    
    # QE signals
    inst_sj_scores = []
    inst_fk_scores = []
    inst_em_scores = []
    inst_vc_scores = []
    inst_lp_scores = []
    inst_greedy_f1s = []
    
    rng = np.random.RandomState(42)
    
    for inst in valid:
        samples = inst["samples"][:N]
        gold = inst["gold"]
        
        # Per-sample F1s
        sample_f1s = [per_instance_f1(s, gold, "ner") for s in samples]
        
        # Greedy F1
        greedy = inst.get("greedy")
        if greedy:
            gf1 = per_instance_f1(greedy, gold, "ner")
        else:
            gf1 = sample_f1s[0]  # fallback
        greedy_f1s.append(gf1)
        inst_greedy_f1s.append(gf1)
        
        # Oracle F1
        oracle_f1s.append(max(sample_f1s))
        
        # Random F1
        random_f1s.append(sample_f1s[rng.randint(N)])
        
        # SJ selection: pick sample with highest mean jaccard to others
        sj_scores = [sj_signal(samples, s, inst) for s in samples]
        sj_sel_f1s.append(sample_f1s[int(np.argmax(sj_scores))])
        inst_sj_scores.append(float(np.mean(sj_scores)))
        
        # FK (instance-level)
        inst_fk_scores.append(compute_fk(samples))
        
        # EM selection: pick sample with most duplicates
        em_scores = [em_signal(samples, s, inst) for s in samples]
        em_sel_f1s.append(sample_f1s[int(np.argmax(em_scores))])
        inst_em_scores.append(compute_em(samples))
        
        # VC selection: pick sample with highest entity voting rate
        vc_scores = [vc_signal(samples, s, inst) for s in samples]
        vc_sel_f1s.append(sample_f1s[int(np.argmax(vc_scores))])
        inst_vc_scores.append(compute_vc(samples))
        
        # LP selection: pick sample with highest mean_logprob
        lp_scores = [lp_signal(samples, s, inst) for s in samples]
        lp_sel_f1s.append(sample_f1s[int(np.argmax(lp_scores))])
        inst_lp_scores.append(compute_lp_signal(samples))
    
    # FK selection: FK is instance-level, use EM for per-sample selection
    fk_sel_f1s = em_sel_f1s  # FK doesn't give per-sample ranking; EM is the natural analog
    
    results["greedy_f1"] = float(np.mean(greedy_f1s))
    results["oracle_f1"] = float(np.mean(oracle_f1s))
    results["random_f1"] = float(np.mean(random_f1s))
    results["sj_selection_f1"] = float(np.mean(sj_sel_f1s))
    results["fk_selection_f1"] = float(np.mean(fk_sel_f1s))
    results["em_selection_f1"] = float(np.mean(em_sel_f1s))
    results["vc_selection_f1"] = float(np.mean(vc_sel_f1s))
    results["lp_selection_f1"] = float(np.mean(lp_sel_f1s))
    
    print(f"  Greedy F1:  {results['greedy_f1']:.4f}")
    print(f"  Oracle F1:  {results['oracle_f1']:.4f}")
    print(f"  Random F1:  {results['random_f1']:.4f}")
    print(f"  SJ sel F1:  {results['sj_selection_f1']:.4f}")
    print(f"  EM sel F1:  {results['em_selection_f1']:.4f}")
    print(f"  VC sel F1:  {results['vc_selection_f1']:.4f}")
    print(f"  LP sel F1:  {results['lp_selection_f1']:.4f}")
    
    # 5. QE metrics: rho and AUROC
    # Rho(signal, greedy_F1)
    def safe_rho(x, y):
        x, y = np.array(x), np.array(y)
        mask = np.isfinite(x) & np.isfinite(y)
        if mask.sum() < 3:
            return float("nan")
        r = spearmanr(x[mask], y[mask])
        return float(r.statistic)
    
    results["sj_rho"] = safe_rho(inst_sj_scores, inst_greedy_f1s)
    results["fk_rho"] = safe_rho(inst_fk_scores, inst_greedy_f1s)
    results["em_rho"] = safe_rho(inst_em_scores, inst_greedy_f1s)
    results["vc_rho"] = safe_rho(inst_vc_scores, inst_greedy_f1s)
    results["lp_rho"] = safe_rho(inst_lp_scores, inst_greedy_f1s)
    
    print(f"  SJ rho:     {results['sj_rho']:.4f}")
    print(f"  FK rho:     {results['fk_rho']:.4f}")
    print(f"  EM rho:     {results['em_rho']:.4f}")
    print(f"  VC rho:     {results['vc_rho']:.4f}")
    print(f"  LP rho:     {results['lp_rho']:.4f}")
    
    # AUROC: binary label = greedy_F1 >= median
    median_f1 = float(np.median(inst_greedy_f1s))
    labels = np.array([1 if f >= median_f1 else 0 for f in inst_greedy_f1s])
    
    results["sj_auroc"] = compute_auroc(inst_sj_scores, labels)
    results["fk_auroc"] = compute_auroc(inst_fk_scores, labels)
    results["em_auroc"] = compute_auroc(inst_em_scores, labels)
    results["vc_auroc"] = compute_auroc(inst_vc_scores, labels)
    lp_arr = np.array(inst_lp_scores)
    lp_arr[~np.isfinite(lp_arr)] = -999
    results["lp_auroc"] = compute_auroc(lp_arr.tolist(), labels)
    
    print(f"  SJ AUROC:   {results['sj_auroc']:.4f}")
    print(f"  FK AUROC:   {results['fk_auroc']:.4f}")
    print(f"  EM AUROC:   {results['em_auroc']:.4f}")
    print(f"  VC AUROC:   {results['vc_auroc']:.4f}")
    print(f"  LP AUROC:   {results['lp_auroc']:.4f}")
    
    return results

def main():
    all_results = {}
    for name, path in TEMP_CONFIGS.items():
        if not os.path.exists(path):
            print(f"SKIP {name}: {path} not found")
            continue
        all_results[name] = analyze_temperature(name, path)
    
    # Save JSON
    out_path = f"{BASE}/output/exp_026_T_ablation_summary.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved to {out_path}")
    
    # Print markdown table
    print("\n\n## Temperature Ablation Summary (SciERC NER, N=8)\n")
    temps = ["T=0.5", "T=0.8", "T=1.0", "T=1.2"]
    
    print("| Metric | T=0.5 | T=0.8 | T=1.0 | T=1.2 |")
    print("|--------|-------|-------|-------|-------|")
    
    rows = [
        ("Degeneracy rate", "degeneracy_rate", ".3f"),
        ("LP range (mean)", "lp_range_mean", ".5f"),
        ("LP range (std)", "lp_range_std", ".5f"),
        ("Greedy F1", "greedy_f1", ".4f"),
        ("Oracle F1", "oracle_f1", ".4f"),
        ("Random F1", "random_f1", ".4f"),
        ("SJ sel F1", "sj_selection_f1", ".4f"),
        ("EM sel F1", "em_selection_f1", ".4f"),
        ("VC sel F1", "vc_selection_f1", ".4f"),
        ("LP sel F1", "lp_selection_f1", ".4f"),
        ("SJ rho", "sj_rho", ".4f"),
        ("FK rho", "fk_rho", ".4f"),
        ("EM rho", "em_rho", ".4f"),
        ("VC rho", "vc_rho", ".4f"),
        ("LP rho", "lp_rho", ".4f"),
        ("SJ AUROC", "sj_auroc", ".4f"),
        ("FK AUROC", "fk_auroc", ".4f"),
        ("EM AUROC", "em_auroc", ".4f"),
        ("VC AUROC", "vc_auroc", ".4f"),
        ("LP AUROC", "lp_auroc", ".4f"),
    ]
    
    for label, key, fmt in rows:
        vals = []
        for t in temps:
            if t in all_results and key in all_results[t]:
                v = all_results[t][key]
                vals.append(f"{v:{fmt}}")
            else:
                vals.append("--")
        print(f"| {label} | {' | '.join(vals)} |")

if __name__ == "__main__":
    main()

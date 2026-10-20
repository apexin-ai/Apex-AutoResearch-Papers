#!/usr/bin/env python3
"""Full metric recompute for SciERC 3-seed MF4v2 data.

Computes: greedy/oracle/mv F1, 5 signal rho (SJ/FK/EM/VC/LP), selection F1,
consensus construction F1, degeneracy, alpha_crit.
"""
import json
import sys
import os
import math
import statistics
import numpy as np
from collections import Counter, defaultdict
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import (
    structural_consistency_soft_jaccard,
    fleiss_kappa_surface,
)

SEEDS = {
    "seed42": "/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed42/samples.jsonl",
    "seed123": "/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed123/samples.jsonl",
    "seed456": "/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed456/samples.jsonl",
}
OUTPUT_PATH = "/root/autodl-tmp/struct_self_consist_ie/scierc_3seed_recompute_results.txt"

# ==========================================================================
# Entity matching: exact 4-tuple (text, type, start, end)
# ==========================================================================

def extract_entities_4t(d):
    return frozenset((e["text"], e["type"], e["start"], e["end"]) for e in d.get("entities", []))

def entity_f1_counts(pred, gold):
    tp = len(pred & gold)
    fp = len(pred - gold)
    fn = len(gold - pred)
    return tp, fp, fn

def instance_f1(pred, gold):
    tp, fp, fn = entity_f1_counts(pred, gold)
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)

def micro_f1(tp, fp, fn):
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)

# ==========================================================================
# Signal computation
# ==========================================================================

def compute_exact_match_rate(samples):
    keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    if not keys:
        return 0.0
    c = Counter(keys)
    return c.most_common(1)[0][1] / len(samples)

def compute_voting_confidence(samples):
    N = len(samples)
    if N == 0:
        return 0.0
    counter = Counter()
    for s in samples:
        for e in s.get("entities", []):
            counter[(e["text"], e["type"])] += 1
    if not counter:
        return 0.0
    return float(np.mean([v / N for v in counter.values()]))

def compute_mean_logprob(samples):
    lps = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    lps = [lp for lp in lps if np.isfinite(lp)]
    return float(np.mean(lps)) if lps else float("nan")

def safe_spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    x, y = x[m], y[m]
    if len(x) < 3:
        return float("nan"), float("nan")
    r = spearmanr(x, y)
    return float(r.statistic), float(r.pvalue)

# ==========================================================================
# Consensus construction (LP-gated)
# ==========================================================================

def consensus_construct(inst, high_thresh=0.5, medium_thresh=0.25):
    samples = inst["samples"]
    N = len(samples)
    entity_counts = Counter()
    entity_sample_indices = defaultdict(list)
    for i, s in enumerate(samples):
        seen = set()
        for e in s.get("entities", []):
            key = (e["text"], e["type"], e["start"], e["end"])
            if key not in seen:
                entity_counts[key] += 1
                entity_sample_indices[key].append(i)
                seen.add(key)
    
    sample_lps = []
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob")
        if lp is None and "logprobs" in inst and i < len(inst["logprobs"]):
            lp = inst["logprobs"][i]
        if lp is not None and math.isfinite(lp):
            sample_lps.append(lp)
    instance_median_lp = statistics.median(sample_lps) if sample_lps else 0.0
    
    consensus = set()
    for ek, count in entity_counts.items():
        freq = count / N
        if freq > high_thresh:
            consensus.add(ek)
        elif freq > medium_thresh:
            contributing_lps = []
            for i in entity_sample_indices[ek]:
                lp = samples[i].get("mean_logprob")
                if lp is None and "logprobs" in inst and i < len(inst["logprobs"]):
                    lp = inst["logprobs"][i]
                if lp is not None and math.isfinite(lp):
                    contributing_lps.append(lp)
            if contributing_lps:
                mean_lp = statistics.mean(contributing_lps)
                if mean_lp > instance_median_lp:
                    consensus.add(ek)
    return consensus

# ==========================================================================
# Per-seed full analysis
# ==========================================================================

def analyze_seed(path):
    with open(path) as f:
        data = [json.loads(line) for line in f if line.strip()]
    
    # Gold-non-empty filter
    instances = [d for d in data if len(d["gold"].get("entities", [])) > 0]
    n_total = len(data)
    n_valid = len(instances)
    N = len(instances[0]["samples"]) if instances else 0
    
    # ===== Basic F1 (micro, 4-tuple matching) =====
    greedy_tp = greedy_fp = greedy_fn = 0
    oracle_tp = oracle_fp = oracle_fn = 0
    mv_tp = mv_fp = mv_fn = 0
    n_degenerate = 0
    
    per_inst_greedy_f1 = []
    
    for inst in instances:
        gold_ents = extract_entities_4t(inst["gold"])
        greedy_ents = extract_entities_4t(inst.get("greedy", inst["samples"][0]))
        
        # Greedy
        tp, fp, fn = entity_f1_counts(greedy_ents, gold_ents)
        greedy_tp += tp; greedy_fp += fp; greedy_fn += fn
        per_inst_greedy_f1.append(instance_f1(greedy_ents, gold_ents))
        
        # Samples
        samples = inst["samples"]
        sample_ent_sets = [extract_entities_4t(s) for s in samples]
        
        # Oracle
        best_f1_val = -1.0
        best_tp = best_fp = best_fn = 0
        for s_ents in sample_ent_sets:
            f1_val = instance_f1(s_ents, gold_ents)
            if f1_val > best_f1_val:
                best_f1_val = f1_val
                best_tp, best_fp, best_fn = entity_f1_counts(s_ents, gold_ents)
        oracle_tp += best_tp; oracle_fp += best_fp; oracle_fn += best_fn
        
        # MV strict (> N/2 = > 4, i.e. >= 5)
        entity_counter = Counter()
        for s_ents in sample_ent_sets:
            for e in s_ents:
                entity_counter[e] += 1
        threshold = N / 2
        mv_ents = frozenset(e for e, c in entity_counter.items() if c > threshold)
        tp, fp, fn = entity_f1_counts(mv_ents, gold_ents)
        mv_tp += tp; mv_fp += fp; mv_fn += fn
        
        # Degeneracy
        if len(set(sample_ent_sets)) == 1:
            n_degenerate += 1
    
    g_f1 = micro_f1(greedy_tp, greedy_fp, greedy_fn)
    o_f1 = micro_f1(oracle_tp, oracle_fp, oracle_fn)
    m_f1 = micro_f1(mv_tp, mv_fp, mv_fn)
    delta = n_degenerate / n_valid if n_valid > 0 else 0
    alpha_crit = g_f1 / 2
    
    # ===== 5 Signals: SJ, FK, EM, VC, LP =====
    sj_vals, fk_vals, em_vals, vc_vals, lp_vals = [], [], [], [], []
    
    for inst in instances:
        samples = inst["samples"]
        sj_vals.append(structural_consistency_soft_jaccard(samples, subtask="ner"))
        fk_vals.append(fleiss_kappa_surface(samples, subtask="ner"))
        em_vals.append(compute_exact_match_rate(samples))
        vc_vals.append(compute_voting_confidence(samples))
        lp_vals.append(compute_mean_logprob(samples))
    
    f1_arr = np.array(per_inst_greedy_f1)
    
    # Full-set rho
    signals = {"SJ": np.array(sj_vals), "FK": np.array(fk_vals),
               "EM": np.array(em_vals), "VC": np.array(vc_vals),
               "LP": np.array(lp_vals)}
    
    rho_full = {}
    for name, vals in signals.items():
        rho, p = safe_spearman(vals, f1_arr)
        rho_full[name] = {"rho": rho, "p": p}
    
    # Conditional rho (greedy F1 > 0)
    cond_mask = f1_arr > 0
    rho_cond = {}
    for name, vals in signals.items():
        rho, p = safe_spearman(vals[cond_mask], f1_arr[cond_mask])
        rho_cond[name] = {"rho": rho, "p": p}
    
    # ===== Selection F1 (pick top-1 sample by each signal) =====
    # Instance-level signals (SJ, FK, EM, VC) assign same score to all samples
    # → selection is effectively random (use first sample).
    # LP is per-sample → pick sample with highest mean_logprob.
    
    sel_lp_tp = sel_lp_fp = sel_lp_fn = 0
    sel_random_tp = sel_random_fp = sel_random_fn = 0
    
    for inst in instances:
        gold_ents = extract_entities_4t(inst["gold"])
        samples = inst["samples"]
        
        # LP selection: best mean_logprob sample
        best_lp = -float("inf")
        best_lp_idx = 0
        for i, s in enumerate(samples):
            lp = s.get("mean_logprob")
            if lp is None and "logprobs" in inst and i < len(inst["logprobs"]):
                lp = inst["logprobs"][i]
            if lp is not None and np.isfinite(lp) and lp > best_lp:
                best_lp = lp
                best_lp_idx = i
        
        lp_sel_ents = extract_entities_4t(samples[best_lp_idx])
        tp, fp, fn = entity_f1_counts(lp_sel_ents, gold_ents)
        sel_lp_tp += tp; sel_lp_fp += fp; sel_lp_fn += fn
        
        # Random (first sample) for instance-level signals
        rand_ents = extract_entities_4t(samples[0])
        tp, fp, fn = entity_f1_counts(rand_ents, gold_ents)
        sel_random_tp += tp; sel_random_fp += fp; sel_random_fn += fn
    
    sel_lp_f1 = micro_f1(sel_lp_tp, sel_lp_fp, sel_lp_fn)
    sel_random_f1 = micro_f1(sel_random_tp, sel_random_fp, sel_random_fn)
    
    # Per-signal selection F1 (micro, using best-by-signal per instance)
    # For SJ: pick sample that maximizes mean pairwise SJ with other samples
    # This is expensive; approximate with LP-weighted selection for now
    # Actually, for instance-level signals, sel = random sample → use sel_random_f1
    
    # SJ per-sample (leave-one-out): for each sample, avg SJ with others
    sel_sj_tp = sel_sj_fp = sel_sj_fn = 0
    for inst in instances:
        gold_ents = extract_entities_4t(inst["gold"])
        samples = inst["samples"]
        n_s = len(samples)
        if n_s <= 1:
            sel_ents = extract_entities_4t(samples[0])
        else:
            best_sj = -1.0
            best_idx = 0
            for i in range(n_s):
                sj_scores = []
                for j in range(n_s):
                    if i != j:
                        sj_scores.append(structural_consistency_soft_jaccard(
                            [samples[i], samples[j]], subtask="ner"))
                avg_sj = np.mean(sj_scores) if sj_scores else 0
                if avg_sj > best_sj:
                    best_sj = avg_sj
                    best_idx = i
            sel_ents = extract_entities_4t(samples[best_idx])
        tp, fp, fn = entity_f1_counts(sel_ents, gold_ents)
        sel_sj_tp += tp; sel_sj_fp += fp; sel_sj_fn += fn
    sel_sj_f1 = micro_f1(sel_sj_tp, sel_sj_fp, sel_sj_fn)
    
    # ===== Consensus Construction F1 (micro) =====
    cons_tp = cons_fp = cons_fn = 0
    for inst in instances:
        gold_ents = extract_entities_4t(inst["gold"])
        cons_ents = consensus_construct(inst)
        tp = len(cons_ents & gold_ents)
        fp = len(cons_ents - gold_ents)
        fn = len(gold_ents - cons_ents)
        cons_tp += tp; cons_fp += fp; cons_fn += fn
    cons_f1 = micro_f1(cons_tp, cons_fp, cons_fn)
    
    return {
        "n_total": n_total,
        "n_gold_nonempty": n_valid,
        "N": N,
        "greedy_f1": g_f1,
        "oracle_f1": o_f1,
        "mv_f1": m_f1,
        "delta": delta,
        "alpha_crit": alpha_crit,
        "n_conditional": int(cond_mask.sum()),
        "rho_full": rho_full,
        "rho_cond": rho_cond,
        "sel_lp_f1": sel_lp_f1,
        "sel_sj_f1": sel_sj_f1,
        "sel_random_f1": sel_random_f1,
        "consensus_construct_f1": cons_f1,
    }


def main():
    results = {}
    for seed_name, path in SEEDS.items():
        print(f"\nProcessing {seed_name}...")
        r = analyze_seed(path)
        results[seed_name] = r
        
        print(f"  n={r['n_gold_nonempty']} gold-nonempty (of {r['n_total']}), N={r['N']}")
        print(f"  greedy_f1:        {r['greedy_f1']:.4f}")
        print(f"  oracle_f1:        {r['oracle_f1']:.4f}")
        print(f"  mv_f1 (strict):   {r['mv_f1']:.4f}")
        print(f"  δ (degen):        {r['delta']*100:.1f}%")
        print(f"  α_crit:           {r['alpha_crit']:.4f}")
        print(f"  consensus_f1:     {r['consensus_construct_f1']:.4f}")
        print(f"  sel_LP_f1:        {r['sel_lp_f1']:.4f}")
        print(f"  sel_SJ_f1:        {r['sel_sj_f1']:.4f}")
        print(f"  n_cond:           {r['n_conditional']}")
        print(f"  --- Full-set ρ ---")
        for sig in ["SJ", "FK", "EM", "VC", "LP"]:
            rho = r["rho_full"][sig]["rho"]
            p = r["rho_full"][sig]["p"]
            print(f"    {sig:>4}: ρ={rho:.4f}  p={p:.2e}")
        print(f"  --- Conditional ρ (greedy F1>0) ---")
        for sig in ["SJ", "FK", "EM", "VC", "LP"]:
            rho = r["rho_cond"][sig]["rho"]
            p = r["rho_cond"][sig]["p"]
            print(f"    {sig:>4}: ρ={rho:.4f}  p={p:.2e}")
    
    # ===== 3-seed summary =====
    print("\n" + "="*70)
    print("3-SEED SUMMARY (SciERC MF4v2, N=8)")
    print("="*70)
    
    metrics_to_avg = [
        ("greedy_f1", "Greedy F1"),
        ("oracle_f1", "Oracle F1"),
        ("mv_f1", "MV F1 (strict >N/2)"),
        ("delta", "δ (degeneracy)"),
        ("alpha_crit", "α_crit = F1_gr/2"),
        ("consensus_construct_f1", "Consensus Construct F1"),
        ("sel_lp_f1", "Selection F1 (LP)"),
        ("sel_sj_f1", "Selection F1 (SJ)"),
    ]
    
    lines = []
    lines.append("="*70)
    lines.append("SciERC MF4v2 3-Seed Full Recompute Results")
    lines.append(f"Seeds: 42, 123, 456 | N=8 | Entity match: 4-tuple (text, type, start, end)")
    lines.append("="*70)
    
    # Per-seed detail
    for seed_name in ["seed42", "seed123", "seed456"]:
        r = results[seed_name]
        lines.append(f"\n--- {seed_name} (n={r['n_gold_nonempty']} gold-nonempty of {r['n_total']}) ---")
        lines.append(f"  greedy_f1:          {r['greedy_f1']:.4f}")
        lines.append(f"  oracle_f1:          {r['oracle_f1']:.4f}")
        lines.append(f"  mv_f1 (strict):     {r['mv_f1']:.4f}")
        lines.append(f"  δ (degeneracy):     {r['delta']:.4f}  ({r['delta']*100:.1f}%)")
        lines.append(f"  α_crit:             {r['alpha_crit']:.4f}")
        lines.append(f"  consensus_constr:   {r['consensus_construct_f1']:.4f}")
        lines.append(f"  sel_LP_f1:          {r['sel_lp_f1']:.4f}")
        lines.append(f"  sel_SJ_f1:          {r['sel_sj_f1']:.4f}")
        lines.append(f"  sel_random_f1:      {r['sel_random_f1']:.4f}")
        lines.append(f"  n_conditional:      {r['n_conditional']}")
        lines.append(f"  Full-set ρ:")
        for sig in ["SJ", "FK", "EM", "VC", "LP"]:
            rho = r["rho_full"][sig]["rho"]
            p = r["rho_full"][sig]["p"]
            lines.append(f"    {sig:>4}: ρ={rho:+.4f}  p={p:.2e}")
        lines.append(f"  Conditional ρ (greedy F1>0, n={r['n_conditional']}):")
        for sig in ["SJ", "FK", "EM", "VC", "LP"]:
            rho = r["rho_cond"][sig]["rho"]
            p = r["rho_cond"][sig]["p"]
            lines.append(f"    {sig:>4}: ρ={rho:+.4f}  p={p:.2e}")
    
    # Mean ± σ table
    lines.append("\n" + "="*70)
    lines.append("AGGREGATED (mean ± σ over 3 seeds)")
    lines.append("="*70)
    
    for key, label in metrics_to_avg:
        vals = [results[s][key] for s in ["seed42", "seed123", "seed456"]]
        mean_v = np.mean(vals)
        std_v = np.std(vals, ddof=0)
        if key == "delta":
            lines.append(f"  {label:30s}  {mean_v:.4f} ± {std_v:.4f}  ({mean_v*100:.1f}% ± {std_v*100:.1f}%)")
        else:
            lines.append(f"  {label:30s}  {mean_v:.4f} ± {std_v:.4f}")
    
    lines.append(f"\n  Signal ρ (full-set, mean ± σ):")
    for sig in ["SJ", "FK", "EM", "VC", "LP"]:
        vals = [results[s]["rho_full"][sig]["rho"] for s in ["seed42", "seed123", "seed456"]]
        mean_v = np.mean(vals)
        std_v = np.std(vals, ddof=0)
        lines.append(f"    {sig:>4}: ρ = {mean_v:+.4f} ± {std_v:.4f}")
    
    lines.append(f"\n  Signal ρ (conditional, mean ± σ):")
    for sig in ["SJ", "FK", "EM", "VC", "LP"]:
        vals = [results[s]["rho_cond"][sig]["rho"] for s in ["seed42", "seed123", "seed456"]]
        mean_v = np.mean(vals)
        std_v = np.std(vals, ddof=0)
        lines.append(f"    {sig:>4}: ρ = {mean_v:+.4f} ± {std_v:.4f}")
    
    lines.append(f"\nNote: ESJ/MRSC/LSC are model-inference probes, not computable from samples.jsonl.")
    lines.append(f"      SJ selection uses leave-one-out consensus proximity (MBR-style).")
    lines.append(f"      Instance-level signals (FK/EM/VC) have no within-instance ranking → sel ≈ random.")
    
    output_text = "\n".join(lines)
    print(output_text)
    
    with open(OUTPUT_PATH, "w") as f:
        f.write(output_text + "\n")
    print(f"\nResults saved to {OUTPUT_PATH}")
    
    # Also save JSON
    json_path = OUTPUT_PATH.replace(".txt", ".json")
    json_out = {}
    for seed_name, r in results.items():
        jr = dict(r)
        jr["rho_full"] = {k: v["rho"] for k, v in r["rho_full"].items()}
        jr["rho_cond"] = {k: v["rho"] for k, v in r["rho_cond"].items()}
        json_out[seed_name] = jr
    with open(json_path, "w") as f:
        json.dump(json_out, f, indent=2)
    print(f"JSON saved to {json_path}")


if __name__ == "__main__":
    main()

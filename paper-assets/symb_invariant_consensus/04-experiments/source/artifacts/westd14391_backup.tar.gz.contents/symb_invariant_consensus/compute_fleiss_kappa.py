#!/usr/bin/env python3
"""Compute Fleiss' kappa and Eff-K for experiments with intermediates."""
import json, os, glob, sys
import numpy as np

def fleiss_kappa(data):
    categories = sorted(set(cat for d in data for cat in d.keys()))
    cat_idx = {c: i for i, c in enumerate(categories)}
    k = len(categories)
    n = len(data)
    
    M = np.zeros((n, k))
    N_per = np.zeros(n)
    for i, d in enumerate(data):
        for cat, count in d.items():
            M[i, cat_idx[cat]] = count
        N_per[i] = sum(d.values())
    
    valid = N_per > 1
    if valid.sum() == 0:
        return float('nan')
    
    P_i = np.zeros(n)
    for i in range(n):
        if N_per[i] > 1:
            P_i[i] = (np.sum(M[i]**2) - N_per[i]) / (N_per[i] * (N_per[i] - 1))
    
    P_bar = P_i[valid].mean()
    total = N_per[valid].sum()
    p_j = M[valid].sum(axis=0) / total
    P_e = np.sum(p_j**2)
    
    if P_e >= 1.0:
        return 1.0
    return (P_bar - P_e) / (1 - P_e)

def process_exp(base_dir, K=12):
    intermediates = os.path.join(base_dir, "intermediates")
    files = sorted(glob.glob(os.path.join(intermediates, "folio_*.json")))
    if not files:
        print(f"  No files in {intermediates}")
        return None
    
    data = []
    skipped = 0
    votes_list = []
    
    for f in files:
        with open(f) as fh:
            j = json.load(fh)
        ac = j.get("sica_result", {}).get("answer_counts", {})
        if not ac:
            skipped += 1
            continue
        tv = sum(ac.values())
        if tv < 2:
            skipped += 1
            continue
        votes_list.append(tv)
        data.append(ac)
    
    if not data:
        return None
    
    kap = fleiss_kappa(data)
    eff_k = K / (1 + (K - 1) * kap)
    
    correct = 0
    total_problems = 0
    for f in sorted(glob.glob(os.path.join(intermediates, "folio_*.json"))):
        with open(f) as fh:
            j = json.load(fh)
        gt = j.get("problem", {}).get("answer", "")
        pred = j.get("sica_result", {}).get("answer", "")
        if gt and pred:
            total_problems += 1
            if gt.strip().lower() == pred.strip().lower():
                correct += 1
    
    sc_acc = correct / total_problems * 100 if total_problems > 0 else None
    
    return {
        "n_problems": len(data),
        "skipped": skipped,
        "avg_votes": round(float(np.mean(votes_list)), 1),
        "min_votes": int(min(votes_list)),
        "max_votes": int(max(votes_list)),
        "K": K,
        "kappa": round(float(kap), 4),
        "eff_k": round(float(eff_k), 2),
        "sc_acc": round(sc_acc, 2) if sc_acc else None,
        "categories_seen": sorted(set(cat for d in data for cat in d.keys()))
    }

results_dir = "/root/symb_invariant_consensus/results"
experiments = []
for d in sorted(os.listdir(results_dir)):
    intdir = os.path.join(results_dir, d, "intermediates")
    if os.path.isdir(intdir):
        experiments.append(d)

print(f"Found experiments with intermediates: {experiments}")
all_results = {}

for exp in experiments:
    print(f"\n=== {exp} ===")
    r = process_exp(os.path.join(results_dir, exp))
    if r:
        all_results[exp] = r
        print(f"  Problems: {r['n_problems']} (skipped {r['skipped']})")
        print(f"  Votes: avg={r['avg_votes']}, min={r['min_votes']}, max={r['max_votes']}")
        print(f"  Categories: {r['categories_seen']}")
        print(f"  Fleiss' kappa = {r['kappa']}")
        print(f"  Eff-K = {r['eff_k']}")
        if r['sc_acc'] is not None:
            print(f"  SC accuracy = {r['sc_acc']}%")

out = os.path.join(results_dir, "fleiss_kappa_batch2_westd25068.json")
with open(out, "w") as f:
    json.dump(all_results, f, indent=2)
print(f"\nSaved to {out}")

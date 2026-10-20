#!/usr/bin/env python3
"""WNUT-17 full signal analysis: 5 signals x 3 metrics."""

import json
import os
import sys
import numpy as np
from collections import Counter
from itertools import combinations
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code/')
from consistency import (
    fleiss_kappa_surface,
    structural_consistency_soft_jaccard,
)
from evaluation import per_instance_f1

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_eval/samples.jsonl"
OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/review_round2"

instances = []
with open(DATA_PATH) as f:
    for line in f:
        line = line.strip()
        if line:
            instances.append(json.loads(line))

n_total = len(instances)
print(f"Total instances: {n_total}")

# ---------------------------------------------------------------------------
# Compute instance-level F1 (greedy vs gold)
# ---------------------------------------------------------------------------
f1_all = []
for inst in instances:
    f1 = per_instance_f1(inst["greedy"], inst["gold"], subtask="ner")
    f1_all.append(f1)

# ---------------------------------------------------------------------------
# Filter gold-empty
# ---------------------------------------------------------------------------
gold_nonempty_mask = [len(inst["gold"].get("entities", [])) > 0 for inst in instances]
n_gold_empty = sum(1 for m in gold_nonempty_mask if not m)
n_after_filter = sum(1 for m in gold_nonempty_mask if m)

filtered_instances = [inst for inst, m in zip(instances, gold_nonempty_mask) if m]
filtered_f1 = [f for f, m in zip(f1_all, gold_nonempty_mask) if m]
n_f1_positive = sum(1 for f in filtered_f1 if f > 0)

print(f"Gold empty: {n_gold_empty}")
print(f"After filter (gold nonempty): {n_after_filter}")
print(f"F1 > 0: {n_f1_positive}")

# ---------------------------------------------------------------------------
# Compute 5 signals on filtered set
# ---------------------------------------------------------------------------
print("Computing signals...")

# 1. Soft Jaccard
sj_values = []
for inst in filtered_instances:
    sj = structural_consistency_soft_jaccard(inst["samples"], subtask="ner")
    sj_values.append(sj)

# 2. Fleiss' Kappa
fk_values = []
for inst in filtered_instances:
    fk = fleiss_kappa_surface(inst["samples"], subtask="ner")
    fk_values.append(fk)

# 3. Exact Match rate
em_values = []
for inst in filtered_instances:
    samples = inst["samples"]
    n = len(samples)
    if n < 2:
        em_values.append(1.0)
        continue
    sample_keys = []
    for s in samples:
        keys = frozenset((e.get("text", ""), e.get("type", "")) for e in s.get("entities", []))
        sample_keys.append(keys)
    match_count = sum(1 for i in range(n) for j in range(i+1, n) if sample_keys[i] == sample_keys[j])
    total_pairs = n * (n - 1) // 2
    em_values.append(match_count / total_pairs if total_pairs > 0 else 1.0)

# 4. Logprob (mean of per-sample mean_logprob)
lp_values = []
for inst in filtered_instances:
    lps = []
    for s in inst.get("samples", []):
        lp = s.get("mean_logprob")
        if lp is not None:
            lps.append(lp)
    lp_values.append(float(np.mean(lps)) if lps else 0.0)

# 5. Voting confidence
vc_values = []
for inst in filtered_instances:
    samples = inst["samples"]
    n = len(samples)
    counter = Counter()
    for s in samples:
        for e in s.get("entities", []):
            counter[(e.get("text", ""), e.get("type", ""))] += 1
    majority_votes = [v / n for v in counter.values() if v > n / 2]
    vc_values.append(float(np.mean(majority_votes)) if majority_votes else 0.0)

print("Signals computed.")

# ---------------------------------------------------------------------------
# AUROC (manual, no sklearn needed)
# ---------------------------------------------------------------------------
def auroc_manual(scores, labels):
    """AUROC: scores predict label=1."""
    pos = [s for s, l in zip(scores, labels) if l == 1]
    neg = [s for s, l in zip(scores, labels) if l == 0]
    if not pos or not neg:
        return 0.5
    concordant = sum(1 for p in pos for n in neg if p > n)
    tied = sum(1 for p in pos for n in neg if p == n)
    return (concordant + 0.5 * tied) / (len(pos) * len(neg))

# ---------------------------------------------------------------------------
# Compute metrics for each signal
# ---------------------------------------------------------------------------
signals = {
    "soft_jaccard": sj_values,
    "fleiss_kappa": fk_values,
    "exact_match": em_values,
    "logprob": lp_values,
    "voting_conf": vc_values,
}

f1_arr = np.array(filtered_f1)
labels_binary = (f1_arr > 0).astype(int).tolist()

# Conditional subset: F1 > 0
cond_mask = [f > 0 for f in filtered_f1]
cond_f1 = [f for f, m in zip(filtered_f1, cond_mask) if m]
n_cond = len(cond_f1)

results = {
    "dataset": "wnut17",
    "n_total": n_total,
    "n_after_filter": n_after_filter,
    "n_gold_empty": n_gold_empty,
    "n_f1_positive": n_f1_positive,
    "signals": {},
}

print("\n" + "="*70)
print(f"{'Signal':<20} {'Spearman ρ':>12} {'p-value':>12} {'AUROC':>8} {'Cond ρ':>10} {'Cond p':>12} {'Cond n':>7}")
print("="*70)

for sig_name, sig_vals in signals.items():
    sig_arr = np.array(sig_vals)
    
    # 1. Spearman ρ (full filtered set)
    rho, p = spearmanr(sig_arr, f1_arr)
    
    # 2. AUROC (predicting F1 > 0)
    auroc = auroc_manual(sig_vals, labels_binary)
    
    # 3. Conditional ρ (F1 > 0 subset only)
    cond_sig = [v for v, m in zip(sig_vals, cond_mask) if m]
    if len(cond_sig) > 2:
        cond_rho, cond_p = spearmanr(cond_sig, cond_f1)
    else:
        cond_rho, cond_p = float('nan'), float('nan')
    
    results["signals"][sig_name] = {
        "spearman_rho": round(float(rho), 4),
        "spearman_p": float(p),
        "auroc": round(float(auroc), 4),
        "conditional_rho": round(float(cond_rho), 4),
        "conditional_rho_p": float(cond_p),
        "conditional_n": n_cond,
    }
    
    print(f"{sig_name:<20} {rho:>12.4f} {p:>12.4e} {auroc:>8.4f} {cond_rho:>10.4f} {cond_p:>12.4e} {n_cond:>7d}")

print("="*70)

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
os.makedirs(OUTPUT_DIR, exist_ok=True)
out_path = os.path.join(OUTPUT_DIR, "wnut17_full_signal_analysis.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
print(f"\nSaved to {out_path}")

# ---------------------------------------------------------------------------
# SJ校对：精确值比较
# ---------------------------------------------------------------------------
print("\n" + "="*70)
print("SJ 校对")
print("="*70)
sj_rho = results["signals"]["soft_jaccard"]["spearman_rho"]
sj_p = results["signals"]["soft_jaccard"]["spearman_p"]
print(f"Computed SJ ρ = {sj_rho:.4f} (p = {sj_p:.6f})")
print(f"Paper claims:   ρ = 0.082 (p = 0.106)")
print(f"Report.json:    ρ = 0.0888 (p = 0.0197)")
if abs(sj_rho - 0.082) > 0.001:
    print(f"MISMATCH with paper: Δ = {sj_rho - 0.082:+.4f}")
if abs(sj_rho - 0.0888) < 0.001:
    print(f"MATCHES report.json (within 0.001)")

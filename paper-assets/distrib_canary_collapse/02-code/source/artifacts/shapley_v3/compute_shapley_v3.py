#!/usr/bin/env python3
"""Recompute Shapley values with 6-seed null data (s45-s50, 6-pair basis).

FPR Shapley: recomputed from 6 null seeds (36 pairs).
FNR Shapley: unchanged from v2 (45 signal experiments, 270 pairs for 6-pair).
Combined = FPR + FNR.

Voting rules (matching fpr_transparency consensus):
  naive_xcorr:     naive_xcorr_sig (|r|>0.5, lag!=0), no direction filter for Shapley
  diff_xcorr:      diff_xcorr_fwd_sig_fdr
  threshold_onset: threshold_onset_sig
  perm_granger:    perm_granger_fwd_sig_fdr
  ty_granger:      ty_granger_sig
"""
import json
import numpy as np
from itertools import combinations
from math import factorial
from pathlib import Path
from datetime import datetime

METHODS = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']
N = len(METHODS)

# Load fpr_transparency data
FPR_FILE = Path(__file__).parent.parent / 'fpr_transparency_all_seeds.json'
OLD_SHAPLEY = Path(__file__).parent.parent / 'shapley_v2' / 'shapley_values_v2.json'

with open(FPR_FILE) as f:
    fpr_data = json.load(f)

with open(OLD_SHAPLEY) as f:
    old_sv = json.load(f)

# Build null detection matrix: 36 x 5 (boolean)
null_matrix = []
for seed_data in fpr_data['seeds']:
    for pair in seed_data['pairs']:
        row = [
            pair['naive_xcorr_sig'],                # naive: sig (no direction filter)
            pair['diff_xcorr_fwd_sig_fdr'],          # diff: FDR-corrected
            pair['threshold_onset_sig'],             # threshold: deterministic
            pair['perm_granger_fwd_sig_fdr'],        # perm: FDR-corrected
            pair['ty_granger_sig'],                  # ty: uncorrected
        ]
        null_matrix.append(row)

null_matrix = np.array(null_matrix, dtype=bool)
n_null = len(null_matrix)
assert n_null == 36, f"Expected 36 null pairs, got {n_null}"

# Verify per-method FP counts match Table 14
fp_counts = null_matrix.sum(axis=0)
print("Per-method FP counts (should match Table 14):")
for m, c in zip(METHODS, fp_counts):
    print(f"  {m}: {c}/36 = {c/36*100:.1f}%")

# Shapley computation (exact enumeration, 2^5=32 coalitions)
def shapley_values(value_fn):
    """Compute Shapley values for n players given a value function v(S).
    v(S) takes a frozenset of method indices and returns a scalar."""
    phi = np.zeros(N)
    for k in range(N):
        others = [i for i in range(N) if i != k]
        for size in range(N):  # |S| = 0, 1, ..., N-1
            weight = factorial(size) * factorial(N - size - 1) / factorial(N)
            for combo in combinations(others, size):
                S = frozenset(combo)
                S_with_k = S | {k}
                marginal = value_fn(S_with_k) - value_fn(S)
                phi[k] += weight * marginal
    return phi

# FPR value function: fraction of null pairs detected by coalition
def fpr_value(coalition):
    if not coalition:
        return 0.0
    cols = list(coalition)
    detected = null_matrix[:, cols].any(axis=1)
    return detected.sum() / n_null

# Compute FPR Shapley
fpr_shapley = shapley_values(fpr_value)
print("\nFPR Shapley (6-seed null):")
for m, v in zip(METHODS, fpr_shapley):
    print(f"  {m}: {v:+.6f}")
print(f"  Sum: {fpr_shapley.sum():.6f} (should equal full-coalition FPR: {fpr_value(frozenset(range(N))):.6f})")

# FNR Shapley: keep from old v2 (signal data unchanged)
fnr_shapley_6pair = np.array([old_sv['main_result_6pair']['fnr_shapley'][m] for m in METHODS])
fnr_shapley_8pair = np.array([old_sv['robustness_8pair']['fnr_shapley'][m] for m in METHODS])

print("\nFNR Shapley (unchanged from v2, 6-pair):")
for m, v in zip(METHODS, fnr_shapley_6pair):
    print(f"  {m}: {v:+.6f}")

# Combined Shapley
combined_6pair = fpr_shapley + fnr_shapley_6pair
combined_8pair = fpr_shapley + fnr_shapley_8pair

print("\nCombined Shapley (6-pair):")
for m, v in zip(METHODS, combined_6pair):
    print(f"  {m}: {v:+.6f}")

# FDR sensitivity: recompute PermG BH-FDR at different q thresholds
def bh_fdr_count(pvalues, q):
    """Apply BH-FDR correction and count rejections."""
    m = len(pvalues)
    sorted_p = sorted(pvalues)
    k_max = 0
    for i, p in enumerate(sorted_p, 1):
        if p <= q * i / m:
            k_max = i
    return k_max

# Extract PermG forward p-values per seed
print("\n--- FDR Sensitivity (Null) ---")
for q in [0.01, 0.05, 0.10]:
    total_sig = 0
    for seed_data in fpr_data['seeds']:
        pvals = [p['perm_granger_fwd_p'] for p in seed_data['pairs']]
        sig = bh_fdr_count(pvals, q)
        total_sig += sig
    print(f"  q={q:.2f}: {total_sig}/36 null FDR-sig")

# Build output JSON
result = {
    "version": "v3_6seed_null",
    "generated_at": datetime.now().isoformat(),
    "change_from_v2": "FPR recomputed with 6 null seeds (s45-s50, 36 pairs, 6-pair basis). FNR unchanged (45 signal experiments, 270/360 signal pairs).",
    "null_data_source": "fpr_transparency_all_seeds.json",
    "null_seeds": [45, 46, 47, 48, 49, 50],
    "n_null_seeds": 6,
    "n_null_pairs_per_seed": 6,
    "n_null_obs": 36,
    "n_signal_experiments": 45,
    "n_signal_obs_6pair": 270,
    "n_signal_obs_8pair": 360,
    "pair_basis": "6-pair (distinct_1/2/3 only, mauve excluded)",
    "threshold_criterion": "true_3sigma_d105",
    "methods": METHODS,
    "n_methods": N,
    "n_coalitions": 2**N,
    "voting_rules": {
        "naive_xcorr": "naive_xcorr_sig (|r|>0.5, lag!=0; no direction filter)",
        "diff_xcorr": "diff_xcorr_fwd_sig_fdr (BH-FDR corrected)",
        "threshold_onset": "threshold_onset_sig (deterministic 3sigma)",
        "perm_granger": "perm_granger_fwd_sig_fdr (BH-FDR corrected)",
        "ty_granger": "ty_granger_sig (uncorrected)"
    },
    "main_result_6pair": {
        "fpr_shapley": {m: round(v, 6) for m, v in zip(METHODS, fpr_shapley)},
        "fnr_shapley": {m: round(v, 6) for m, v in zip(METHODS, fnr_shapley_6pair)},
        "combined_shapley": {m: round(v, 6) for m, v in zip(METHODS, combined_6pair)}
    },
    "robustness_8pair": {
        "fpr_shapley": {m: round(v, 6) for m, v in zip(METHODS, fpr_shapley)},
        "fnr_shapley": {m: round(v, 6) for m, v in zip(METHODS, fnr_shapley_8pair)},
        "combined_shapley": {m: round(v, 6) for m, v in zip(METHODS, combined_8pair)}
    },
    "raw_fpr_counts": {m: int(c) for m, c in zip(METHODS, fp_counts)},
    "raw_fpr_rates": {m: round(int(c)/36, 4) for m, c in zip(METHODS, fp_counts)},
    "fdr_sensitivity_null": {},
    "comparison_to_v2": {
        "fpr_shapley_change": {},
        "combined_shapley_change": {}
    }
}

# FDR sensitivity
for q in [0.01, 0.05, 0.10]:
    total_sig = 0
    for seed_data in fpr_data['seeds']:
        pvals = [p['perm_granger_fwd_p'] for p in seed_data['pairs']]
        total_sig += bh_fdr_count(pvals, q)
    result['fdr_sensitivity_null'][f'q_{q:.2f}'] = {
        'rejections': total_sig,
        'total': 36,
        'fpr': round(total_sig / 36, 4)
    }

# Comparison to v2
for m in METHODS:
    old_fpr = old_sv['main_result_6pair']['fpr_shapley'][m]
    new_fpr = result['main_result_6pair']['fpr_shapley'][m]
    result['comparison_to_v2']['fpr_shapley_change'][m] = round(new_fpr - old_fpr, 6)
    old_comb = old_sv['main_result_6pair']['combined_shapley'][m]
    new_comb = result['main_result_6pair']['combined_shapley'][m]
    result['comparison_to_v2']['combined_shapley_change'][m] = round(new_comb - old_comb, 6)

OUT = Path(__file__).parent / 'shapley_values_v3.json'
with open(OUT, 'w') as f:
    json.dump(result, f, indent=2)
print(f"\nSaved: {OUT}")

# Print comparison
print("\n--- Comparison v2 → v3 ---")
print(f"{'Method':<20} {'v2 FPR':>10} {'v3 FPR':>10} {'v2 comb':>10} {'v3 comb':>10}")
for m in METHODS:
    v2_fpr = old_sv['main_result_6pair']['fpr_shapley'][m]
    v3_fpr = result['main_result_6pair']['fpr_shapley'][m]
    v2_comb = old_sv['main_result_6pair']['combined_shapley'][m]
    v3_comb = result['main_result_6pair']['combined_shapley'][m]
    print(f"  {m:<18} {v2_fpr:>+10.3f} {v3_fpr:>+10.3f} {v2_comb:>+10.3f} {v3_comb:>+10.3f}")

# Best method check
best_method = METHODS[np.argmin(combined_6pair)]
print(f"\nBest method (lowest combined): {best_method} ({combined_6pair.min():+.3f})")

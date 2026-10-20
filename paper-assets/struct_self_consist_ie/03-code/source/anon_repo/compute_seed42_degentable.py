import json, sys
import numpy as np
from itertools import combinations
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import _ner_soft_jaccard_pair
from unified_metrics import load_and_filter, compute_sample_f1s, compute_degeneracy, compute_entity_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/samples.jsonl"

instances = load_and_filter(DATA_PATH, gold_filter=True)
print(f"Loaded {len(instances)} gold-filtered instances")
print(f"N samples per instance: {len(instances[0]['samples'])}")

n_constant_f1 = 0
n_constant_utility = 0
n_total = len(instances)

oracle_gaps_closed = []
within_sj_rhos = []

for idx, inst in enumerate(instances):
    samples = inst['samples']
    gold_ents = inst['gold']['entities']
    greedy = inst.get('greedy', samples[0])
    N = len(samples)
    
    # Per-sample F1
    sample_f1s = compute_sample_f1s(inst)
    greedy_f1 = compute_entity_f1(greedy.get('entities', []), gold_ents)
    oracle_f1 = max(sample_f1s)
    
    # Constant F1
    is_degen_f1 = compute_degeneracy(sample_f1s)
    if is_degen_f1:
        n_constant_f1 += 1
    
    # MBR(SJ) utility per candidate
    # utility(i) = mean SJ(i, j) for j != i
    pairwise = {}
    for i, j in combinations(range(N), 2):
        sj = _ner_soft_jaccard_pair(
            samples[i].get('entities', []),
            samples[j].get('entities', [])
        )
        pairwise[(i, j)] = sj
        pairwise[(j, i)] = sj
    
    utilities = []
    for i in range(N):
        u = np.mean([pairwise[(i, j)] for j in range(N) if j != i])
        utilities.append(u)
    
    # Constant utility
    is_constant_utility = len(set(round(u, 10) for u in utilities)) <= 1
    if is_constant_utility:
        n_constant_utility += 1
    
    # Oracle gap closed (only for non-degenerate F1 instances)
    if not is_degen_f1:
        mbr_idx = int(np.argmax(utilities))
        mbr_f1 = sample_f1s[mbr_idx]
        gap = oracle_f1 - greedy_f1
        if gap > 1e-10:
            closed = (mbr_f1 - greedy_f1) / gap
            oracle_gaps_closed.append(closed)
    
    # Within-instance SJ rho (need >= 3 unique pairs for Spearman)
    if len(set(round(u, 10) for u in utilities)) > 1 and len(set(round(f, 10) for f in sample_f1s)) > 1:
        rho, _ = spearmanr(utilities, sample_f1s)
        if np.isfinite(rho):
            within_sj_rhos.append(rho)

constant_f1_pct = n_constant_f1 / n_total * 100
constant_utility_pct = n_constant_utility / n_total * 100
oracle_gap_closed_mean = np.mean(oracle_gaps_closed) * 100 if oracle_gaps_closed else 0.0
within_sj_rho_median = float(np.median(within_sj_rhos)) if within_sj_rhos else 0.0

print(f"\n=== seed42 CoNLL N=8 Results ===")
print(f"Constant F1: {n_constant_f1}/{n_total} = {constant_f1_pct:.2f}%")
print(f"Constant utility: {n_constant_utility}/{n_total} = {constant_utility_pct:.2f}%")
print(f"Oracle gap closed (non-deg, n={len(oracle_gaps_closed)}): {oracle_gap_closed_mean:.2f}%")
print(f"Within-inst SJ rho (median, n={len(within_sj_rhos)}): {within_sj_rho_median:.4f}")

# Also output for JSON
results = {
    "seed": 42,
    "dataset": "conll2003",
    "n_samples": 8,
    "n_instances": n_total,
    "constant_f1_pct": round(constant_f1_pct, 2),
    "constant_utility_pct": round(constant_utility_pct, 2),
    "oracle_gap_closed_pct": round(oracle_gap_closed_mean, 2),
    "n_nondegen_for_gap": len(oracle_gaps_closed),
    "within_sj_rho_median": round(within_sj_rho_median, 4),
    "n_rho_instances": len(within_sj_rhos),
}
print(f"\nJSON: {json.dumps(results, indent=2)}")

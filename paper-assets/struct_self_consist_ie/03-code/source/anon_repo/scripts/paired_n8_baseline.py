"""
Paired N=8 Baseline: Filter exp-021 (N=8, 37k) to match exp-027's 5000 instances,
compute metrics, and run paired bootstrap test.
"""
import json
import numpy as np
from collections import defaultdict
from scipy import stats

def compute_ner_f1(pred_entities, gold_entities):
    """Compute NER F1 based on exact span+type match."""
    pred_set = set()
    for e in pred_entities:
        pred_set.add((e['text'], e['type'], e.get('start', -1), e.get('end', -1)))
    gold_set = set()
    for e in gold_entities:
        gold_set.add((e['text'], e['type'], e.get('start', -1), e.get('end', -1)))
    
    if len(pred_set) == 0 and len(gold_set) == 0:
        return 1.0
    if len(pred_set) == 0 or len(gold_set) == 0:
        return 0.0
    
    tp = len(pred_set & gold_set)
    prec = tp / len(pred_set) if pred_set else 0
    rec = tp / len(gold_set) if gold_set else 0
    if prec + rec == 0:
        return 0.0
    return 2 * prec * rec / (prec + rec)

def get_entity_key_set(entities):
    """Get frozenset of (text, type) for degeneracy check."""
    return frozenset((e['text'], e['type']) for e in entities)

def select_by_logprob(samples):
    """Select sample with highest mean logprob."""
    best_idx = -1
    best_lp = -float('inf')
    for i, s in enumerate(samples):
        lp = s.get('mean_logprob', s.get('cumulative_logprob', -999))
        if lp > best_lp:
            best_lp = lp
            best_idx = i
    return best_idx

def oracle_select(samples, gold_entities):
    """Select sample with highest F1."""
    best_idx = 0
    best_f1 = -1
    for i, s in enumerate(samples):
        f1 = compute_ner_f1(s['entities'], gold_entities)
        if f1 > best_f1:
            best_f1 = f1
            best_idx = i
    return best_idx

print("Loading exp-027 (N=16, 5000 instances)...")
exp027 = {}
with open('output/exp_027_fewnerd_n16/samples.jsonl') as f:
    for line in f:
        d = json.loads(line)
        exp027[d['id']] = d
print(f"  Loaded {len(exp027)} instances")

print("Loading exp-021 (N=8, full)...")
exp021 = {}
with open('output/exp_021_inference/samples.jsonl') as f:
    for line in f:
        d = json.loads(line)
        exp021[d['id']] = d
print(f"  Loaded {len(exp021)} instances")

# Find matching IDs
target_ids = set(exp027.keys())
matched_ids = target_ids & set(exp021.keys())
missing_ids = target_ids - set(exp021.keys())
print(f"\nMatched: {len(matched_ids)} / {len(target_ids)}")
if missing_ids:
    print(f"WARNING: {len(missing_ids)} IDs not found in exp-021!")
    print(f"  Examples: {list(missing_ids)[:5]}")

# Process both datasets on matched instances
results_n8 = []
results_n16 = []
per_type_n8 = defaultdict(list)
per_type_n16 = defaultdict(list)

for inst_id in sorted(matched_ids):
    d8 = exp021[inst_id]
    d16 = exp027[inst_id]
    gold_ents = d8['gold']['entities']
    
    # Skip if no gold entities
    if not gold_ents:
        continue
    
    # Determine primary type (most common type in gold)
    type_counts = defaultdict(int)
    for e in gold_ents:
        type_counts[e['type']] += 1
    primary_type = max(type_counts, key=type_counts.get)
    
    # --- N=8 metrics ---
    samples_8 = d8['samples']
    greedy_8 = d8.get('greedy', {}).get('entities', [])
    greedy_f1_8 = compute_ner_f1(greedy_8, gold_ents)
    
    # LP selection
    lp_idx_8 = select_by_logprob(samples_8)
    lp_sel_f1_8 = compute_ner_f1(samples_8[lp_idx_8]['entities'], gold_ents)
    
    # Oracle
    oracle_idx_8 = oracle_select(samples_8, gold_ents)
    oracle_f1_8 = compute_ner_f1(samples_8[oracle_idx_8]['entities'], gold_ents)
    
    # Degeneracy
    key_sets_8 = [get_entity_key_set(s['entities']) for s in samples_8]
    is_degen_8 = len(set(key_sets_8)) == 1
    
    # LP correlation: per-sample F1 vs mean_logprob
    sample_f1s_8 = [compute_ner_f1(s['entities'], gold_ents) for s in samples_8]
    sample_lps_8 = [s.get('mean_logprob', s.get('cumulative_logprob', 0)) for s in samples_8]
    
    r8 = {
        'id': inst_id,
        'greedy_f1': greedy_f1_8,
        'lp_sel_f1': lp_sel_f1_8,
        'oracle_f1': oracle_f1_8,
        'is_degen': is_degen_8,
        'sample_f1s': sample_f1s_8,
        'sample_lps': sample_lps_8,
        'lp_delta': lp_sel_f1_8 - greedy_f1_8,
        'primary_type': primary_type
    }
    results_n8.append(r8)
    per_type_n8[primary_type].append(r8)
    
    # --- N=16 metrics ---
    samples_16 = d16['samples']
    greedy_16 = d16.get('greedy', {}).get('entities', [])
    greedy_f1_16 = compute_ner_f1(greedy_16, gold_ents)
    
    lp_idx_16 = select_by_logprob(samples_16)
    lp_sel_f1_16 = compute_ner_f1(samples_16[lp_idx_16]['entities'], gold_ents)
    
    oracle_idx_16 = oracle_select(samples_16, gold_ents)
    oracle_f1_16 = compute_ner_f1(samples_16[oracle_idx_16]['entities'], gold_ents)
    
    key_sets_16 = [get_entity_key_set(s['entities']) for s in samples_16]
    is_degen_16 = len(set(key_sets_16)) == 1
    
    sample_f1s_16 = [compute_ner_f1(s['entities'], gold_ents) for s in samples_16]
    sample_lps_16 = [s.get('mean_logprob', s.get('cumulative_logprob', 0)) for s in samples_16]
    
    r16 = {
        'id': inst_id,
        'greedy_f1': greedy_f1_16,
        'lp_sel_f1': lp_sel_f1_16,
        'oracle_f1': oracle_f1_16,
        'is_degen': is_degen_16,
        'sample_f1s': sample_f1s_16,
        'sample_lps': sample_lps_16,
        'lp_delta': lp_sel_f1_16 - greedy_f1_16,
        'primary_type': primary_type
    }
    results_n16.append(r16)
    per_type_n16[primary_type].append(r16)

n_instances = len(results_n8)
print(f"\nGold-filtered instances: {n_instances}")

# Compute aggregate metrics
greedy_f1_n8 = np.mean([r['greedy_f1'] for r in results_n8])
lp_sel_f1_n8 = np.mean([r['lp_sel_f1'] for r in results_n8])
oracle_f1_n8 = np.mean([r['oracle_f1'] for r in results_n8])
degen_rate_n8 = np.mean([r['is_degen'] for r in results_n8]) * 100
lp_delta_n8 = (lp_sel_f1_n8 - greedy_f1_n8) * 100

greedy_f1_n16 = np.mean([r['greedy_f1'] for r in results_n16])
lp_sel_f1_n16 = np.mean([r['lp_sel_f1'] for r in results_n16])
oracle_f1_n16 = np.mean([r['oracle_f1'] for r in results_n16])
degen_rate_n16 = np.mean([r['is_degen'] for r in results_n16]) * 100
lp_delta_n16 = (lp_sel_f1_n16 - greedy_f1_n16) * 100

# Spearman correlation (global, excluding degenerate)
all_f1s_n8 = []
all_lps_n8 = []
all_f1s_n16 = []
all_lps_n16 = []
for r in results_n8:
    if not r['is_degen']:
        all_f1s_n8.extend(r['sample_f1s'])
        all_lps_n8.extend(r['sample_lps'])
for r in results_n16:
    if not r['is_degen']:
        all_f1s_n16.extend(r['sample_f1s'])
        all_lps_n16.extend(r['sample_lps'])

spearman_n8, sp_p_n8 = stats.spearmanr(all_lps_n8, all_f1s_n8)
spearman_n16, sp_p_n16 = stats.spearmanr(all_lps_n16, all_f1s_n16)

# Check greedy consistency
greedy_diff = [abs(results_n8[i]['greedy_f1'] - results_n16[i]['greedy_f1']) for i in range(n_instances)]
greedy_mismatch = sum(1 for d in greedy_diff if d > 1e-6)
print(f"Greedy mismatch between N=8 and N=16: {greedy_mismatch}/{n_instances} instances")
if greedy_mismatch > 0:
    print(f"  Mean greedy diff: {np.mean(greedy_diff):.6f}")

# === Bootstrap CI for N=8 LP selection ===
print("\nRunning bootstrap (B=10000)...")
np.random.seed(42)
B = 10000
per_inst_lp_delta_n8 = np.array([r['lp_delta'] for r in results_n8])
per_inst_lp_delta_n16 = np.array([r['lp_delta'] for r in results_n16])

# Bootstrap for N=8 LP delta
boot_n8_means = []
for _ in range(B):
    idx = np.random.randint(0, n_instances, n_instances)
    boot_n8_means.append(np.mean(per_inst_lp_delta_n8[idx]))
boot_n8_means = np.array(boot_n8_means)
ci_n8_lo, ci_n8_hi = np.percentile(boot_n8_means, [2.5, 97.5])
p_n8 = 2 * min(np.mean(boot_n8_means >= 0), np.mean(boot_n8_means <= 0))

# === Paired Bootstrap: N=16 LP Δ - N=8 LP Δ ===
paired_diff = per_inst_lp_delta_n16 - per_inst_lp_delta_n8
paired_boot_means = []
for _ in range(B):
    idx = np.random.randint(0, n_instances, n_instances)
    paired_boot_means.append(np.mean(paired_diff[idx]))
paired_boot_means = np.array(paired_boot_means)
paired_ci_lo, paired_ci_hi = np.percentile(paired_boot_means, [2.5, 97.5])
paired_point = np.mean(paired_diff)
paired_p = 2 * min(np.mean(paired_boot_means >= 0), np.mean(paired_boot_means <= 0))
paired_sig = paired_ci_lo > 0 or paired_ci_hi < 0

# === Output ===
print("\n" + "="*65)
print("=== Paired Comparison: Same {:,} Instances ===".format(n_instances))
print("="*65)
print(f"\n{'Metric':<22} | {'N=8':<14} | {'N=16':<14} | {'Paired Δ':<10}")
print("-"*65)
print(f"{'Instances (gold-filt)':<22} | {n_instances:<14} | {n_instances:<14} |")
print(f"{'Degeneracy':<22} | {degen_rate_n8:<13.2f}% | {degen_rate_n16:<13.2f}% | {degen_rate_n16-degen_rate_n8:+.2f}pp")
print(f"{'Greedy F1':<22} | {greedy_f1_n8:<14.4f} | {greedy_f1_n16:<14.4f} | {(greedy_f1_n16-greedy_f1_n8)*100:+.2f}pp")
print(f"{'LP Sel F1':<22} | {lp_sel_f1_n8:<14.4f} | {lp_sel_f1_n16:<14.4f} | {(lp_sel_f1_n16-lp_sel_f1_n8)*100:+.2f}pp")
print(f"{'LP Δ vs Greedy (pp)':<22} | {lp_delta_n8:<14.2f} | {lp_delta_n16:<14.2f} | {lp_delta_n16-lp_delta_n8:+.4f}")
print(f"{'Oracle F1':<22} | {oracle_f1_n8:<14.4f} | {oracle_f1_n16:<14.4f} | {(oracle_f1_n16-oracle_f1_n8)*100:+.2f}pp")
print(f"{'LP ρ (Spearman)':<22} | {spearman_n8:<14.4f} | {spearman_n16:<14.4f} | {spearman_n16-spearman_n8:+.4f}")

print(f"\n--- N=8 LP Selection Bootstrap (B={B}) ---")
print(f"  Point estimate: {lp_delta_n8:+.4f} pp")
print(f"  95% CI: [{ci_n8_lo*100:.4f}, {ci_n8_hi*100:.4f}] pp")
print(f"  p-value: {p_n8:.4f}")
print(f"  Significant (α=0.05): {ci_n8_lo > 0 or ci_n8_hi < 0}")

print(f"\n--- Paired Bootstrap: N=16 LP Δ - N=8 LP Δ (B={B}) ---")
print(f"  Point estimate: {paired_point*100:+.4f} pp")
print(f"  95% CI: [{paired_ci_lo*100:.4f}, {paired_ci_hi*100:.4f}] pp")
print(f"  p-value: {paired_p:.4f}")
print(f"  Significant (α=0.05): {paired_sig}")
conclusion = "LP selection SCALES with N (significant)" if paired_sig else "Improvement not statistically significant"
print(f"  Conclusion: {conclusion}")

# === Per-Type ===
print(f"\n{'='*80}")
print(f"{'Type':<14} | {'n':<5} | {'Degen% N8':<10} | {'LP Δ N=8':<10} | {'LP Δ N=16':<10} | {'Improvement':<12}")
print(f"{'-'*80}")
for t in sorted(per_type_n8.keys()):
    items_8 = per_type_n8[t]
    items_16 = per_type_n16[t]
    n = len(items_8)
    degen_8 = np.mean([r['is_degen'] for r in items_8]) * 100
    delta_8 = (np.mean([r['lp_sel_f1'] for r in items_8]) - np.mean([r['greedy_f1'] for r in items_8])) * 100
    delta_16 = (np.mean([r['lp_sel_f1'] for r in items_16]) - np.mean([r['greedy_f1'] for r in items_16])) * 100
    imp = delta_16 - delta_8
    print(f"{t:<14} | {n:<5} | {degen_8:<9.1f}% | {delta_8:+<9.2f}pp | {delta_16:+<9.2f}pp | {imp:+.2f}pp")

# === Save JSON ===
output = {
    'meta': {
        'description': 'Paired N=8 baseline (exp-021 filtered to exp-027 5000 instances)',
        'n_instances': n_instances,
        'n_matched': len(matched_ids),
        'n_missing': len(missing_ids),
        'greedy_mismatch_count': greedy_mismatch,
    },
    'n8': {
        'greedy_f1': round(greedy_f1_n8, 4),
        'lp_sel_f1': round(lp_sel_f1_n8, 4),
        'lp_delta_pp': round(lp_delta_n8, 4),
        'oracle_f1': round(oracle_f1_n8, 4),
        'degeneracy_rate_pct': round(degen_rate_n8, 2),
        'spearman_rho': round(spearman_n8, 4),
        'bootstrap': {
            'ci_95_lo_pp': round(ci_n8_lo * 100, 4),
            'ci_95_hi_pp': round(ci_n8_hi * 100, 4),
            'p_value': round(p_n8, 4),
        }
    },
    'n16': {
        'greedy_f1': round(greedy_f1_n16, 4),
        'lp_sel_f1': round(lp_sel_f1_n16, 4),
        'lp_delta_pp': round(lp_delta_n16, 4),
        'oracle_f1': round(oracle_f1_n16, 4),
        'degeneracy_rate_pct': round(degen_rate_n16, 2),
        'spearman_rho': round(spearman_n16, 4),
    },
    'paired_bootstrap': {
        'point_estimate_pp': round(paired_point * 100, 4),
        'ci_95_lo_pp': round(paired_ci_lo * 100, 4),
        'ci_95_hi_pp': round(paired_ci_hi * 100, 4),
        'p_value': round(paired_p, 4),
        'significant_005': paired_sig,
        'conclusion': conclusion,
    },
    'per_type': {}
}

for t in sorted(per_type_n8.keys()):
    items_8 = per_type_n8[t]
    items_16 = per_type_n16[t]
    n = len(items_8)
    degen_8 = np.mean([r['is_degen'] for r in items_8]) * 100
    greedy_8 = np.mean([r['greedy_f1'] for r in items_8])
    lp_8 = np.mean([r['lp_sel_f1'] for r in items_8])
    delta_8 = (lp_8 - greedy_8) * 100
    greedy_16 = np.mean([r['greedy_f1'] for r in items_16])
    lp_16 = np.mean([r['lp_sel_f1'] for r in items_16])
    delta_16 = (lp_16 - greedy_16) * 100
    output['per_type'][t] = {
        'count': n,
        'degen_pct_n8': round(degen_8, 2),
        'greedy_f1_n8': round(greedy_8, 4),
        'lp_sel_f1_n8': round(lp_8, 4),
        'lp_delta_pp_n8': round(delta_8, 4),
        'greedy_f1_n16': round(greedy_16, 4),
        'lp_sel_f1_n16': round(lp_16, 4),
        'lp_delta_pp_n16': round(delta_16, 4),
        'improvement_pp': round(delta_16 - delta_8, 4),
    }

out_path = 'output/exp_027_fewnerd_n16/paired_n8_baseline.json'
with open(out_path, 'w') as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to: {out_path}")

import json
import numpy as np
from collections import defaultdict

DATA_PATH = '/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl'

# ── helpers ──────────────────────────────────────────────────────────────────

def entity_set(ent_list):
    return set((e['text'], e['type'], e['start'], e['end']) for e in ent_list)

def ner_f1(pred_ents, gold_ents):
    pred = entity_set(pred_ents)
    gold = entity_set(gold_ents)
    if not gold and not pred:
        return 1.0
    if not gold or not pred:
        return 0.0
    tp = len(pred & gold)
    p = tp / len(pred)
    r = tp / len(gold)
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)

def rel_set(rel_list):
    return set((r['head'], r['tail'], r['type'], r['head_start'], r['head_end'], r['tail_start'], r['tail_end']) for r in rel_list)

def re_f1(pred_rels, gold_rels):
    pred = rel_set(pred_rels)
    gold = rel_set(gold_rels)
    if not gold and not pred:
        return 1.0
    if not gold or not pred:
        return 0.0
    tp = len(pred & gold)
    p = tp / len(pred)
    r = tp / len(gold)
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)

# ── load data ────────────────────────────────────────────────────────────────

instances = []
with open(DATA_PATH) as f:
    for line in f:
        instances.append(json.loads(line))

print(f"Total instances: {len(instances)}")
print(f"Samples per instance: {len(instances[0]['samples'])}")

# ── 1. Logprob distribution analysis ────────────────────────────────────────

all_mean_logprobs = []  # per-instance list of 8 mean_logprobs
all_ranges = []
all_stds = []

for inst in instances:
    lps = [s['mean_logprob'] for s in inst['samples']]
    all_mean_logprobs.append(lps)
    rng = max(lps) - min(lps)
    all_ranges.append(rng)
    all_stds.append(np.std(lps))

ranges = np.array(all_ranges)
stds = np.array(all_stds)

print("\n" + "="*60)
print("1. LOGPROB RANGE DISTRIBUTION (max - min of mean_logprob across 8 samples)")
print("="*60)
print(f"  Mean:   {ranges.mean():.6f}")
print(f"  Median: {np.median(ranges):.6f}")
print(f"  P25:    {np.percentile(ranges, 25):.6f}")
print(f"  P75:    {np.percentile(ranges, 75):.6f}")
print(f"  P90:    {np.percentile(ranges, 90):.6f}")
print(f"  P95:    {np.percentile(ranges, 95):.6f}")
print(f"  Min:    {ranges.min():.6f}")
print(f"  Max:    {ranges.max():.6f}")

print(f"\nLogprob std distribution:")
print(f"  Mean:   {stds.mean():.6f}")
print(f"  Median: {np.median(stds):.6f}")

# ── 2. Tie analysis with epsilon thresholds ─────────────────────────────────

print("\n" + "="*60)
print("2. TIE ANALYSIS (logprob range < ε → 'tied')")
print("="*60)

epsilons = [0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5]
for eps in epsilons:
    tied = (ranges < eps).sum()
    print(f"  ε={eps:<6.3f}  tied: {tied:>4d}/{len(instances)}  ({tied/len(instances)*100:5.1f}%)")

# ── 3. Per-instance F1 for various selection strategies ─────────────────────

print("\n" + "="*60)
print("3. SELECTION STRATEGY COMPARISON (NER F1)")
print("="*60)

greedy_f1s = []
logprob_best_f1s = []
logprob_worst_f1s = []
oracle_f1s = []
random_f1s = []

greedy_re_f1s = []
logprob_best_re_f1s = []

for inst in instances:
    gold_ents = inst['gold']['entities']
    gold_rels = inst['gold']['relations']
    
    # Greedy
    gf = ner_f1(inst['greedy']['entities'], gold_ents)
    greedy_f1s.append(gf)
    greedy_re_f1s.append(re_f1(inst['greedy']['relations'], gold_rels))
    
    # Sample F1s
    sample_f1s = [ner_f1(s['entities'], gold_ents) for s in inst['samples']]
    sample_re_f1s = [re_f1(s['relations'], gold_rels) for s in inst['samples']]
    
    # Logprob-best (highest mean_logprob)
    lps = [s['mean_logprob'] for s in inst['samples']]
    best_idx = np.argmax(lps)
    worst_idx = np.argmin(lps)
    logprob_best_f1s.append(sample_f1s[best_idx])
    logprob_worst_f1s.append(sample_f1s[worst_idx])
    logprob_best_re_f1s.append(sample_re_f1s[best_idx])
    
    # Oracle (best F1 among samples)
    oracle_f1s.append(max(sample_f1s))
    
    # Random (mean F1 across samples)
    random_f1s.append(np.mean(sample_f1s))

print(f"  Greedy NER F1:        {np.mean(greedy_f1s):.4f}")
print(f"  Random sample F1:     {np.mean(random_f1s):.4f}")
print(f"  Logprob-best F1:      {np.mean(logprob_best_f1s):.4f}")
print(f"  Logprob-worst F1:     {np.mean(logprob_worst_f1s):.4f}")
print(f"  Oracle F1:            {np.mean(oracle_f1s):.4f}")
print(f"\n  Greedy RE F1:         {np.mean(greedy_re_f1s):.4f}")
print(f"  Logprob-best RE F1:   {np.mean(logprob_best_re_f1s):.4f}")

# ── 4. Non-tied subset analysis ─────────────────────────────────────────────

print("\n" + "="*60)
print("4. NON-TIED SUBSET ANALYSIS")
print("="*60)

from scipy import stats

for threshold in [0.01, 0.02, 0.05, 0.1, 0.2]:
    non_tied_mask = ranges >= threshold
    n_non_tied = non_tied_mask.sum()
    
    if n_non_tied < 10:
        print(f"\n  Threshold ≥ {threshold}: only {n_non_tied} instances, skipping")
        continue
    
    nt_greedy = np.array(greedy_f1s)[non_tied_mask]
    nt_logprob_best = np.array(logprob_best_f1s)[non_tied_mask]
    nt_oracle = np.array(oracle_f1s)[non_tied_mask]
    nt_random = np.array(random_f1s)[non_tied_mask]
    
    diff = nt_logprob_best - nt_greedy
    t_stat, p_val = stats.ttest_rel(nt_logprob_best, nt_greedy)
    
    print(f"\n  Threshold: range ≥ {threshold}")
    print(f"    N instances: {n_non_tied} ({n_non_tied/len(instances)*100:.1f}%)")
    print(f"    Greedy F1:        {nt_greedy.mean():.4f}")
    print(f"    Random F1:        {nt_random.mean():.4f}")
    print(f"    Logprob-best F1:  {nt_logprob_best.mean():.4f}")
    print(f"    Oracle F1:        {nt_oracle.mean():.4f}")
    print(f"    Logprob vs Greedy: diff={diff.mean():+.4f}, p={p_val:.4f}")
    
    # Win/lose/tie counts
    wins = (nt_logprob_best > nt_greedy).sum()
    losses = (nt_logprob_best < nt_greedy).sum()
    ties = (nt_logprob_best == nt_greedy).sum()
    print(f"    Win/Lose/Tie: {wins}/{losses}/{ties}")

# ── 5. Logprob-F1 correlation analysis ──────────────────────────────────────

print("\n" + "="*60)
print("5. LOGPROB-F1 CORRELATION (within instance)")
print("="*60)

within_corrs = []
within_corrs_cumul = []
for inst in instances:
    gold_ents = inst['gold']['entities']
    sample_f1s = [ner_f1(s['entities'], gold_ents) for s in inst['samples']]
    mean_lps = [s['mean_logprob'] for s in inst['samples']]
    cumul_lps = [s['cumulative_logprob'] for s in inst['samples']]
    
    if np.std(sample_f1s) > 0 and np.std(mean_lps) > 0:
        r, _ = stats.spearmanr(mean_lps, sample_f1s)
        within_corrs.append(r)
    if np.std(sample_f1s) > 0 and np.std(cumul_lps) > 0:
        r2, _ = stats.spearmanr(cumul_lps, sample_f1s)
        within_corrs_cumul.append(r2)

print(f"  Mean logprob ↔ NER F1 (Spearman, within-instance):")
print(f"    N instances w/ variance: {len(within_corrs)}/{len(instances)}")
print(f"    Mean ρ:   {np.mean(within_corrs):.4f}")
print(f"    Median ρ: {np.median(within_corrs):.4f}")
print(f"    % positive: {(np.array(within_corrs) > 0).mean()*100:.1f}%")

print(f"\n  Cumulative logprob ↔ NER F1 (Spearman, within-instance):")
print(f"    N instances w/ variance: {len(within_corrs_cumul)}/{len(instances)}")
print(f"    Mean ρ:   {np.mean(within_corrs_cumul):.4f}")
print(f"    Median ρ: {np.median(within_corrs_cumul):.4f}")
print(f"    % positive: {(np.array(within_corrs_cumul) > 0).mean()*100:.1f}%")

# Stratify by tie level
print(f"\n  Correlation stratified by logprob range:")
for lo, hi, label in [(0, 0.01, '<0.01'), (0.01, 0.05, '0.01-0.05'), (0.05, 0.1, '0.05-0.1'), (0.1, 0.5, '0.1-0.5'), (0.5, 99, '≥0.5')]:
    mask = (ranges >= lo) & (ranges < hi)
    idxs = np.where(mask)[0]
    subset_corrs = []
    for i in idxs:
        inst = instances[i]
        gold_ents = inst['gold']['entities']
        sf1 = [ner_f1(s['entities'], gold_ents) for s in inst['samples']]
        mlp = [s['mean_logprob'] for s in inst['samples']]
        if np.std(sf1) > 0 and np.std(mlp) > 0:
            r, _ = stats.spearmanr(mlp, sf1)
            subset_corrs.append(r)
    if subset_corrs:
        print(f"    range {label:>10s}: N={len(idxs):>4d}, ρ={np.mean(subset_corrs):+.4f} (n_with_var={len(subset_corrs)})")

# ── 6. Check for structural signals ────────────────────────────────────────

print("\n" + "="*60)
print("6. CHECK FOR STRUCTURAL SIGNALS IN DATA")
print("="*60)

sample0 = instances[0]['samples'][0]
all_keys = set(sample0.keys())
print(f"  Sample keys: {sorted(all_keys)}")

# Check top-level keys
inst_keys = set(instances[0].keys())
print(f"  Instance keys: {sorted(inst_keys)}")

# Check if any structural scoring info exists
for key in ['sj_score', 'fk_score', 'em_score', 'vc_score', 'consistency_score', 'structural_score']:
    if key in sample0 or key in instances[0]:
        print(f"  Found: {key}")

# ── 7. Length-normalized logprob analysis ───────────────────────────────────

print("\n" + "="*60)
print("7. LENGTH BIAS ANALYSIS")
print("="*60)

# Does mean_logprob correlate with n_tokens?
all_ntokens = []
all_mean_lp = []
all_f1_by_sample = []

for inst in instances:
    gold_ents = inst['gold']['entities']
    for s in inst['samples']:
        all_ntokens.append(s['n_tokens'])
        all_mean_lp.append(s['mean_logprob'])
        all_f1_by_sample.append(ner_f1(s['entities'], gold_ents))

all_ntokens = np.array(all_ntokens)
all_mean_lp = np.array(all_mean_lp)
all_f1_by_sample = np.array(all_f1_by_sample)

r_lp_tok, p_lp_tok = stats.spearmanr(all_mean_lp, all_ntokens)
r_lp_f1, p_lp_f1 = stats.spearmanr(all_mean_lp, all_f1_by_sample)
r_tok_f1, p_tok_f1 = stats.spearmanr(all_ntokens, all_f1_by_sample)

print(f"  Across all samples (N={len(all_ntokens)}):")
print(f"    mean_logprob ↔ n_tokens:  ρ={r_lp_tok:.4f} (p={p_lp_tok:.2e})")
print(f"    mean_logprob ↔ NER F1:    ρ={r_lp_f1:.4f} (p={p_lp_f1:.2e})")
print(f"    n_tokens ↔ NER F1:        ρ={r_tok_f1:.4f} (p={p_tok_f1:.2e})")

# Within-instance: does logprob-best tend to be shorter/longer?
lp_best_len_rank = []
for inst in instances:
    lps = [s['mean_logprob'] for s in inst['samples']]
    lens = [s['n_tokens'] for s in inst['samples']]
    best_idx = np.argmax(lps)
    # rank of best's length (0 = shortest)
    sorted_lens = sorted(lens)
    rank = sorted_lens.index(lens[best_idx]) / (len(lens) - 1) if len(lens) > 1 else 0.5
    lp_best_len_rank.append(rank)

print(f"\n  Logprob-best sample length rank (0=shortest, 1=longest):")
print(f"    Mean: {np.mean(lp_best_len_rank):.4f}")
print(f"    Median: {np.median(lp_best_len_rank):.4f}")

# ── 8. Cumulative vs Mean logprob for selection ─────────────────────────────

print("\n" + "="*60)
print("8. CUMULATIVE vs MEAN LOGPROB SELECTION")
print("="*60)

cumul_best_f1s = []
for inst in instances:
    gold_ents = inst['gold']['entities']
    sample_f1s = [ner_f1(s['entities'], gold_ents) for s in inst['samples']]
    cumul_lps = [s['cumulative_logprob'] for s in inst['samples']]
    best_idx = np.argmax(cumul_lps)
    cumul_best_f1s.append(sample_f1s[best_idx])

print(f"  Mean logprob selection F1:       {np.mean(logprob_best_f1s):.4f}")
print(f"  Cumulative logprob selection F1: {np.mean(cumul_best_f1s):.4f}")
print(f"  Greedy F1:                       {np.mean(greedy_f1s):.4f}")

print("\n" + "="*60)
print("DONE")
print("="*60)

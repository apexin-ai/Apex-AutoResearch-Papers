import json
import numpy as np
from collections import Counter
from scipy import stats

DATA_PATH = '/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl'

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

instances = []
with open(DATA_PATH) as f:
    for line in f:
        instances.append(json.loads(line))

# ── Compute structural consistency (entity majority voting agreement) ───────

print("="*60)
print("STRUCTURAL CONSISTENCY vs LOGPROB SELECTION (NER)")
print("="*60)

# For each instance, compute SJ-like score: how many entities in this sample
# also appear in the majority vote set

def majority_vote_entities(samples):
    """Entity-level majority voting: keep entities appearing in ≥50% of samples."""
    entity_counts = Counter()
    n = len(samples)
    for s in samples:
        for e in entity_set(s['entities']):
            entity_counts[e] += 1
    threshold = n / 2
    return set(e for e, c in entity_counts.items() if c >= threshold)

def sample_consistency_score(sample_ents, mv_ents):
    """Jaccard similarity between sample's entities and majority-vote entities."""
    pred = entity_set(sample_ents)
    if not pred and not mv_ents:
        return 1.0
    if not pred or not mv_ents:
        return 0.0
    return len(pred & mv_ents) / len(pred | mv_ents)

# Per-instance: compute SJ scores, then compare SJ-best vs logprob-best
sj_best_f1s = []
lp_best_f1s = []
greedy_f1s = []
oracle_f1s = []
sj_ranges = []

for inst in instances:
    gold_ents = inst['gold']['entities']
    mv_ents = majority_vote_entities(inst['samples'])
    
    sample_f1s = [ner_f1(s['entities'], gold_ents) for s in inst['samples']]
    sj_scores = [sample_consistency_score(s['entities'], mv_ents) for s in inst['samples']]
    lps = [s['mean_logprob'] for s in inst['samples']]
    
    sj_best_idx = np.argmax(sj_scores)
    lp_best_idx = np.argmax(lps)
    
    sj_best_f1s.append(sample_f1s[sj_best_idx])
    lp_best_f1s.append(sample_f1s[lp_best_idx])
    greedy_f1s.append(ner_f1(inst['greedy']['entities'], gold_ents))
    oracle_f1s.append(max(sample_f1s))
    sj_ranges.append(max(sj_scores) - min(sj_scores))

print(f"\nOverall (N={len(instances)}):")
print(f"  Greedy F1:      {np.mean(greedy_f1s):.4f}")
print(f"  Logprob-best:   {np.mean(lp_best_f1s):.4f}")
print(f"  SJ-best:        {np.mean(sj_best_f1s):.4f}")
print(f"  Oracle:         {np.mean(oracle_f1s):.4f}")

# On non-tied logprob subset
ranges = np.array([max(s['mean_logprob'] for s in inst['samples']) - min(s['mean_logprob'] for s in inst['samples']) for inst in instances])

for thr in [0.05, 0.1]:
    mask = ranges >= thr
    n = mask.sum()
    print(f"\nNon-tied (logprob range ≥ {thr}, N={n}):")
    print(f"  Greedy F1:      {np.array(greedy_f1s)[mask].mean():.4f}")
    print(f"  Logprob-best:   {np.array(lp_best_f1s)[mask].mean():.4f}")
    print(f"  SJ-best:        {np.array(sj_best_f1s)[mask].mean():.4f}")
    print(f"  Oracle:         {np.array(oracle_f1s)[mask].mean():.4f}")
    
    t1, p1 = stats.ttest_rel(np.array(sj_best_f1s)[mask], np.array(lp_best_f1s)[mask])
    t2, p2 = stats.ttest_rel(np.array(sj_best_f1s)[mask], np.array(greedy_f1s)[mask])
    print(f"  SJ vs LP: diff={np.array(sj_best_f1s)[mask].mean()-np.array(lp_best_f1s)[mask].mean():+.4f}, p={p1:.4f}")
    print(f"  SJ vs Greedy: diff={np.array(sj_best_f1s)[mask].mean()-np.array(greedy_f1s)[mask].mean():+.4f}, p={p2:.4f}")

# ── SJ tie analysis ────────────────────────────────────────────────────────

print(f"\n{'='*60}")
print("SJ TIE ANALYSIS")
print("="*60)

sj_ranges = np.array(sj_ranges)
print(f"  SJ range mean: {sj_ranges.mean():.4f}, median: {np.median(sj_ranges):.4f}")
for eps in [0.0, 0.01, 0.05, 0.1]:
    tied = (sj_ranges <= eps).sum()
    print(f"  SJ range ≤ {eps:.2f}: {tied}/{len(instances)} ({tied/len(instances)*100:.1f}%)")

# ── Agreement between logprob-best and SJ-best ─────────────────────────────

print(f"\n{'='*60}")
print("AGREEMENT: LOGPROB-BEST vs SJ-BEST")
print("="*60)

agree = 0
for inst in instances:
    mv_ents = majority_vote_entities(inst['samples'])
    sj_scores = [sample_consistency_score(s['entities'], mv_ents) for s in inst['samples']]
    lps = [s['mean_logprob'] for s in inst['samples']]
    if np.argmax(sj_scores) == np.argmax(lps):
        agree += 1

print(f"  Same best sample: {agree}/{len(instances)} ({agree/len(instances)*100:.1f}%)")

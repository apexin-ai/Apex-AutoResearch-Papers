"""exp-013: Exact-match voting rate as confidence signal.

For each instance, compute the fraction of N samples that produce
the exact same entity/relation set (normalized as frozensets of tuples).
Correlate this rate with per-instance F1.
"""

import json
import sys
from collections import Counter

import numpy as np
from scipy.stats import spearmanr, kendalltau

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/samples.jsonl"


def load_data(path):
    instances = []
    with open(path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))
    return instances


def auroc_simple(scores, labels):
    scores = np.array(scores, dtype=float)
    labels = np.array(labels, dtype=int)
    if len(set(labels)) < 2:
        return float('nan')
    pos = scores[labels == 1]
    neg = scores[labels == 0]
    n_pos, n_neg = len(pos), len(neg)
    if n_pos == 0 or n_neg == 0:
        return float('nan')
    count = 0.0
    for p in pos:
        count += np.sum(p > neg) + 0.5 * np.sum(p == neg)
    return count / (n_pos * n_neg)


def entity_set_key(sample):
    """Normalize entity set to frozenset of (text, type)."""
    return frozenset((e["text"], e["type"]) for e in sample.get("entities", []))


def relation_set_key(sample):
    """Normalize relation set to frozenset of (head, tail, type)."""
    return frozenset((r["head"], r["tail"], r["type"]) for r in sample.get("relations", []))


def exact_match_rate(samples, key_fn):
    """Fraction of samples matching the most common set."""
    if not samples:
        return 0.0
    keys = [key_fn(s) for s in samples]
    counter = Counter(keys)
    max_count = counter.most_common(1)[0][1]
    return max_count / len(samples)


def analyze(instances, subtask):
    """Compute exact-match rate and correlate with F1."""
    key_fn = entity_set_key if subtask == "ner" else relation_set_key
    field_check = "entities" if subtask == "ner" else "relations"

    # Per-instance metrics
    em_rates = []
    greedy_f1s = []
    for inst in instances:
        em_rates.append(exact_match_rate(inst["samples"], key_fn))
        greedy_f1s.append(per_instance_f1(inst["greedy"], inst["gold"], subtask))

    # Consistency scores (SJ, FK)
    consistency = compute_all_consistency_scores(instances, subtask=subtask)
    sj = consistency["soft_jaccard"]
    fk = consistency["fleiss_kappa"]

    # Filter: gold-nonempty
    valid = [i for i, inst in enumerate(instances) if inst["gold"].get(field_check)]
    n_gold_empty = len(instances) - len(valid)

    f1_v = [greedy_f1s[i] for i in valid]
    em_v = [em_rates[i] for i in valid]
    sj_v = [sj[i] for i in valid]
    fk_v = [fk[i] for i in valid]

    # Median-split AUROC labels (fallback to >= when > yields single-class labels)
    median_f1 = float(np.median(f1_v))
    labels_v = [1 if f > median_f1 else 0 for f in f1_v]
    if len(set(labels_v)) < 2:
        labels_v = [1 if f >= median_f1 else 0 for f in f1_v]

    # Compute correlations
    results = {}
    for name, scores in [("soft_jaccard", sj_v), ("fleiss_kappa", fk_v), ("exact_match_rate", em_v)]:
        rho, p_rho = spearmanr(scores, f1_v)
        tau, p_tau = kendalltau(scores, f1_v)
        auc = auroc_simple(scores, labels_v)
        results[name] = {
            "rho": float(rho), "p_rho": float(p_rho),
            "tau": float(tau), "p_tau": float(p_tau),
            "auroc": float(auc),
        }

    return {
        "n_total": len(instances),
        "n_valid": len(valid),
        "n_gold_empty": n_gold_empty,
        "median_f1": median_f1,
        "em_rate_mean": float(np.mean(em_v)),
        "em_rate_std": float(np.std(em_v)),
        "signals": results,
    }


def print_table(subtask, analysis):
    n = analysis["n_valid"]
    print(f"\n{'='*80}")
    print(f"  Confidence Signal Comparison ({subtask.upper()}, Full Set, n={n})")
    print(f"{'='*80}")
    print(f"  {'Signal':<20} | {'ρ_spearman':>10} | {'p-value':>10} | {'τ_kendall':>10} | {'AUROC':>7}")
    print(f"  {'-'*20}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}-+-{'-'*7}")

    for name in ["soft_jaccard", "fleiss_kappa", "exact_match_rate"]:
        m = analysis["signals"][name]
        auroc_s = f"{m['auroc']:.4f}" if not np.isnan(m['auroc']) else "N/A"
        print(f"  {name:<20} | {m['rho']:>+10.4f} | {m['p_rho']:>10.2e} | {m['tau']:>+10.4f} | {auroc_s:>7}")

    print(f"\n  exact_match_rate: mean={analysis['em_rate_mean']:.4f}, std={analysis['em_rate_std']:.4f}")
    em = analysis["signals"]["exact_match_rate"]
    sj = analysis["signals"]["soft_jaccard"]
    print(f"  >>> EM vs SJ: ρ_EM={em['rho']:+.4f} vs ρ_SJ={sj['rho']:+.4f}")


def main():
    print("Loading data...")
    instances = load_data(DATA_PATH)
    print(f"Loaded {len(instances)} instances")

    report = {}
    for subtask in ["ner", "re"]:
        analysis = analyze(instances, subtask)
        print_table(subtask, analysis)
        report[subtask] = analysis

    out_path = "/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/exp013_exact_match_report.json"
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nReport saved to {out_path}")


if __name__ == "__main__":
    main()

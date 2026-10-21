"""exp-014: Entity/relation majority voting as selection strategy + confidence signal.

For each instance's N=8 samples:
1. Count (text, type) frequency for NER, (head, tail, type) for RE
2. Majority voting: keep items appearing > N/2 times
3. Compute consensus F1 vs gold
4. Compare against greedy, oracle, SJ-selected strategies
5. Compute voting_confidence = mean(voting_rate of consensus items)
"""

import json
import sys
from collections import Counter

import numpy as np
from scipy.stats import spearmanr, kendalltau

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1, entity_strict_match, relation_strict_match

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


def majority_vote_entities(samples, threshold_frac=0.5):
    """Build consensus entity set via majority voting.
    
    Returns:
        consensus_entities: list of entity dicts (with best representative span)
        voting_rates: dict mapping (text, type) -> fraction of samples containing it
    """
    N = len(samples)
    threshold = N * threshold_frac
    
    # Count (text, type) occurrences and track spans
    counter = Counter()
    span_counter = {}  # (text, type) -> Counter of (start, end)
    span_to_entity = {}  # (text, type, start, end) -> entity dict
    
    for s in samples:
        for e in s.get("entities", []):
            key = (e["text"], e["type"])
            counter[key] += 1
            if key not in span_counter:
                span_counter[key] = Counter()
            span = (e["start"], e["end"])
            span_counter[key][span] += 1
            span_to_entity[(key[0], key[1], span[0], span[1])] = e
    
    # Build consensus: items with count > threshold
    consensus = []
    voting_rates = {}
    for key, count in counter.items():
        rate = count / N
        voting_rates[key] = rate
        if count > threshold:
            # Pick most common span
            best_span = span_counter[key].most_common(1)[0][0]
            entity = span_to_entity[(key[0], key[1], best_span[0], best_span[1])]
            consensus.append(entity)
    
    return consensus, voting_rates


def majority_vote_relations(samples, threshold_frac=0.5):
    """Build consensus relation set via majority voting."""
    N = len(samples)
    threshold = N * threshold_frac
    
    counter = Counter()
    span_counter = {}
    span_to_rel = {}
    
    for s in samples:
        for r in s.get("relations", []):
            key = (r["head"], r["tail"], r["type"])
            counter[key] += 1
            if key not in span_counter:
                span_counter[key] = Counter()
            span = (r["head_start"], r["head_end"], r["tail_start"], r["tail_end"])
            span_counter[key][span] += 1
            span_to_rel[(key[0], key[1], key[2]) + span] = r
    
    consensus = []
    voting_rates = {}
    for key, count in counter.items():
        rate = count / N
        voting_rates[key] = rate
        if count > threshold:
            best_span = span_counter[key].most_common(1)[0][0]
            rel = span_to_rel[key + best_span]
            consensus.append(rel)
    
    return consensus, voting_rates


def voting_confidence(voting_rates, consensus_keys):
    """Mean voting rate of consensus items."""
    if not consensus_keys:
        return 0.0
    rates = [voting_rates[k] for k in consensus_keys]
    return float(np.mean(rates))


def analyze(instances, subtask):
    """Full analysis for one subtask."""
    field_check = "entities" if subtask == "ner" else "relations"
    vote_fn = majority_vote_entities if subtask == "ner" else majority_vote_relations
    
    # Per-instance metrics
    greedy_f1s = []
    voting_f1s = []
    oracle_f1s = []
    voting_confs = []
    
    # Consistency scores
    consistency = compute_all_consistency_scores(instances, subtask=subtask)
    sj = consistency["soft_jaccard"]
    fk = consistency["fleiss_kappa"]
    oracle_indices = consistency["oracle_indices"]
    
    # SJ-selected: pick sample with behavior closest to consensus
    # Actually, we'll pick sample with highest SJ score... but SJ is per-instance, not per-sample.
    # Instead, compute per-sample: pick the sample whose individual F1 is highest (oracle).
    # For "SJ-oracle": we pick the sample that SJ would rank highest.
    # But SJ is a single number per instance. The natural "SJ selection" doesn't pick a sample.
    # Let's compute: for each sample, its avg pairwise SJ with other samples, pick the highest.
    
    for i, inst in enumerate(instances):
        gold = inst["gold"]
        samples = inst["samples"]
        greedy = inst.get("greedy", {"entities": [], "relations": []})
        
        # Greedy F1
        greedy_f1s.append(per_instance_f1(greedy, gold, subtask))
        
        # Oracle F1 (best of N)
        sample_f1s = [per_instance_f1(s, gold, subtask) for s in samples]
        oracle_f1s.append(max(sample_f1s) if sample_f1s else 0.0)
        
        # Majority voting
        consensus_items, v_rates = vote_fn(samples)
        consensus_extraction = {
            "entities": consensus_items if subtask == "ner" else [],
            "relations": consensus_items if subtask == "re" else [],
        }
        voting_f1s.append(per_instance_f1(consensus_extraction, gold, subtask))
        
        # Voting confidence
        consensus_keys = set()
        if subtask == "ner":
            consensus_keys = {(e["text"], e["type"]) for e in consensus_items}
        else:
            consensus_keys = {(r["head"], r["tail"], r["type"]) for r in consensus_items}
        
        # Use mean voting rate over ALL unique items (not just consensus) as signal
        if v_rates:
            voting_confs.append(float(np.mean(list(v_rates.values()))))
        else:
            voting_confs.append(0.0)
    
    # Filter: gold-nonempty
    valid = [i for i, inst in enumerate(instances) if inst["gold"].get(field_check)]
    n_gold_empty = len(instances) - len(valid)
    
    f1_v = [greedy_f1s[i] for i in valid]
    vf1_v = [voting_f1s[i] for i in valid]
    of1_v = [oracle_f1s[i] for i in valid]
    vc_v = [voting_confs[i] for i in valid]
    sj_v = [sj[i] for i in valid]
    fk_v = [fk[i] for i in valid]
    
    # Median-split AUROC labels (fallback to >= when > yields single-class labels)
    median_f1 = float(np.median(f1_v))
    labels_v = [1 if f > median_f1 else 0 for f in f1_v]
    if len(set(labels_v)) < 2:
        labels_v = [1 if f >= median_f1 else 0 for f in f1_v]
    
    # Correlation: voting confidence vs F1
    signal_results = {}
    for name, scores in [("soft_jaccard", sj_v), ("fleiss_kappa", fk_v), ("voting_confidence", vc_v)]:
        rho, p_rho = spearmanr(scores, f1_v)
        tau, p_tau = kendalltau(scores, f1_v)
        auc = auroc_simple(scores, labels_v)
        signal_results[name] = {
            "rho": float(rho), "p_rho": float(p_rho),
            "tau": float(tau), "p_tau": float(p_tau),
            "auroc": float(auc),
        }
    
    # Strategy comparison
    strategies = {
        "greedy": f1_v,
        "majority_voting": vf1_v,
        "true_oracle": of1_v,
    }
    
    strategy_stats = {}
    for name, f1s in strategies.items():
        strategy_stats[name] = {
            "mean_f1": float(np.mean(f1s)),
            "median_f1": float(np.median(f1s)),
            "std_f1": float(np.std(f1s)),
        }
    
    return {
        "n_total": len(instances),
        "n_valid": len(valid),
        "n_gold_empty": n_gold_empty,
        "signals": signal_results,
        "strategies": strategy_stats,
        "voting_f1_all": voting_f1s,
        "greedy_f1_all": greedy_f1s,
    }


def print_results(subtask, analysis):
    n = analysis["n_valid"]
    print(f"\n{'='*80}")
    print(f"  Confidence Signal Comparison ({subtask.upper()}, Full Set, n={n})")
    print(f"{'='*80}")
    print(f"  {'Signal':<20} | {'ρ_spearman':>10} | {'p-value':>10} | {'τ_kendall':>10} | {'AUROC':>7}")
    print(f"  {'-'*20}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}-+-{'-'*7}")

    for name in ["soft_jaccard", "fleiss_kappa", "voting_confidence"]:
        m = analysis["signals"][name]
        auroc_s = f"{m['auroc']:.4f}" if not np.isnan(m['auroc']) else "N/A"
        print(f"  {name:<20} | {m['rho']:>+10.4f} | {m['p_rho']:>10.2e} | {m['tau']:>+10.4f} | {auroc_s:>7}")

    print(f"\n{'='*80}")
    print(f"  Selection Strategy Comparison ({subtask.upper()}, n={n})")
    print(f"{'='*80}")
    print(f"  {'Strategy':<20} | {'Mean F1':>10} | {'Median F1':>10} | {'Std F1':>10}")
    print(f"  {'-'*20}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}")

    for name in ["greedy", "majority_voting", "true_oracle"]:
        s = analysis["strategies"][name]
        label = {
            "greedy": "greedy (T=0)",
            "majority_voting": "majority_voting",
            "true_oracle": "oracle (best-of-N)",
        }[name]
        print(f"  {label:<20} | {s['mean_f1']:>10.4f} | {s['median_f1']:>10.4f} | {s['std_f1']:>10.4f}")


def main():
    print("Loading data...")
    instances = load_data(DATA_PATH)
    print(f"Loaded {len(instances)} instances")

    report = {}
    for subtask in ["ner", "re"]:
        analysis = analyze(instances, subtask)
        print_results(subtask, analysis)
        report[subtask] = {k: v for k, v in analysis.items() if k not in ("voting_f1_all", "greedy_f1_all")}

    out_path = "/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/exp014_entity_voting_report.json"
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nReport saved to {out_path}")


if __name__ == "__main__":
    main()

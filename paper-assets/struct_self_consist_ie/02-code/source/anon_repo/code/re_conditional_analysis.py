"""RE Conditional Filtering Analysis for SciERC.

Filter out F1=0 instances and recompute signals + selection on non-zero subset.
"""
import json
import os
import sys
import numpy as np
from collections import Counter
from itertools import combinations
from scipy.stats import spearmanr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evaluation import per_instance_f1, relation_strict_match
from consistency import (
    fleiss_kappa_surface,
    structural_consistency_soft_jaccard,
    _re_soft_jaccard_pair,
    _extract_surface_keys,
)

SAMPLES_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl"
OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/review_round2"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "re_conditional_analysis.json")
SUBTASK = "re"


def load_data():
    with open(SAMPLES_PATH) as f:
        return [json.loads(line) for line in f]


def filter_gold_nonempty(data):
    return [inst for inst in data if len(inst["gold"].get("relations", [])) > 0]


def compute_greedy_f1s(instances):
    return [per_instance_f1(inst["greedy"], inst["gold"], subtask=SUBTASK) for inst in instances]


def compute_signals(instances):
    n = len(instances)
    sj = [structural_consistency_soft_jaccard(inst["samples"], subtask=SUBTASK) for inst in instances]
    fk = [fleiss_kappa_surface(inst["samples"], subtask=SUBTASK) for inst in instances]

    em = []
    for inst in instances:
        samples = inst["samples"]
        ns = len(samples)
        if ns < 2:
            em.append(1.0)
            continue
        sample_keys = [
            frozenset((r.get("head", ""), r.get("tail", ""), r.get("type", "")) for r in s.get("relations", []))
            for s in samples
        ]
        match_count = sum(1 for i in range(ns) for j in range(i + 1, ns) if sample_keys[i] == sample_keys[j])
        total_pairs = ns * (ns - 1) // 2
        em.append(match_count / total_pairs if total_pairs > 0 else 1.0)

    vc = []
    for inst in instances:
        samples = inst["samples"]
        ns = len(samples)
        counter = Counter()
        for s in samples:
            for r in s.get("relations", []):
                counter[(r.get("head", ""), r.get("tail", ""), r.get("type", ""))] += 1
        majority_votes = [v / ns for v in counter.values() if v > ns / 2]
        vc.append(float(np.mean(majority_votes)) if majority_votes else 0.0)

    lp = []
    for inst in instances:
        lps = [s.get("mean_logprob", 0.0) for s in inst.get("samples", []) if s.get("mean_logprob") is not None]
        lp.append(float(np.mean(lps)) if lps else 0.0)

    return {"sj": sj, "fk": fk, "em": em, "vc": vc, "lp": lp}


def spearman(a, b):
    if len(a) < 3:
        return 0.0, 1.0
    r = spearmanr(a, b)
    return round(float(r.statistic), 4), round(float(r.pvalue), 6)


def compute_selection_f1s(instances, per_sample_f1s):
    """Compute selection F1 for each of the 5 signals."""
    n_inst = len(instances)

    # SJ-best: pick sample with highest mean pairwise SJ
    sj_sel = []
    for idx, inst in enumerate(instances):
        samples = inst["samples"]
        ns = len(samples)
        if ns <= 1:
            sj_sel.append(per_sample_f1s[idx][0] if per_sample_f1s[idx] else 0.0)
            continue
        sample_scores = []
        for k in range(ns):
            sims = []
            for j in range(ns):
                if j == k:
                    continue
                sims.append(_re_soft_jaccard_pair(
                    samples[k].get("relations", []),
                    samples[j].get("relations", []),
                ))
            sample_scores.append(float(np.mean(sims)))
        best_k = int(np.argmax(sample_scores))
        sj_sel.append(per_sample_f1s[idx][best_k])

    # FK-best: pick sample whose surface keys have highest overlap with all others
    fk_sel = []
    for idx, inst in enumerate(instances):
        samples = inst["samples"]
        ns = len(samples)
        if ns <= 1:
            fk_sel.append(per_sample_f1s[idx][0] if per_sample_f1s[idx] else 0.0)
            continue
        sample_key_sets = [_extract_surface_keys(s, SUBTASK) for s in samples]
        sample_scores = []
        for k in range(ns):
            overlaps = []
            for j in range(ns):
                if j == k:
                    continue
                union = sample_key_sets[k] | sample_key_sets[j]
                inter = sample_key_sets[k] & sample_key_sets[j]
                overlaps.append(len(inter) / len(union) if union else 1.0)
            sample_scores.append(float(np.mean(overlaps)))
        best_k = int(np.argmax(sample_scores))
        fk_sel.append(per_sample_f1s[idx][best_k])

    # EM-best: pick sample that exactly matches the most other samples
    em_sel = []
    for idx, inst in enumerate(instances):
        samples = inst["samples"]
        ns = len(samples)
        if ns <= 1:
            em_sel.append(per_sample_f1s[idx][0] if per_sample_f1s[idx] else 0.0)
            continue
        sample_keys = [
            frozenset((r.get("head", ""), r.get("tail", ""), r.get("type", "")) for r in s.get("relations", []))
            for s in samples
        ]
        match_counts = [sum(1 for j in range(ns) if j != k and sample_keys[k] == sample_keys[j]) for k in range(ns)]
        best_k = int(np.argmax(match_counts))
        em_sel.append(per_sample_f1s[idx][best_k])

    # VC-best: pick sample closest to majority vote
    vc_sel = []
    for idx, inst in enumerate(instances):
        samples = inst["samples"]
        ns = len(samples)
        if ns == 0:
            vc_sel.append(0.0)
            continue
        counter = Counter()
        for s in samples:
            for r in s.get("relations", []):
                counter[(r.get("head", ""), r.get("tail", ""), r.get("type", ""))] += 1
        majority_set = {k for k, v in counter.items() if v > ns / 2}
        best_k, best_score = 0, -1
        for k, s in enumerate(samples):
            s_keys = {(r.get("head", ""), r.get("tail", ""), r.get("type", "")) for r in s.get("relations", [])}
            score = len(s_keys & majority_set) - 0.5 * len(s_keys - majority_set)
            if score > best_score:
                best_score = score
                best_k = k
        vc_sel.append(per_sample_f1s[idx][best_k])

    # LP-best: pick sample with highest mean logprob
    lp_sel = []
    for idx, inst in enumerate(instances):
        samples = inst["samples"]
        if not samples:
            lp_sel.append(0.0)
            continue
        lp_scores = [s.get("mean_logprob", 0.0) for s in samples]
        best_k = int(np.argmax(lp_scores))
        lp_sel.append(per_sample_f1s[idx][best_k])

    return {
        "sj": float(np.mean(sj_sel)),
        "fk": float(np.mean(fk_sel)),
        "em": float(np.mean(em_sel)),
        "vc": float(np.mean(vc_sel)),
        "lp": float(np.mean(lp_sel)),
    }


def compute_oracle_f1(instances, per_sample_f1s):
    return float(np.mean([max(sf) if sf else 0.0 for sf in per_sample_f1s]))


def analyze_subset(instances, label):
    print(f"\n=== {label} (n={len(instances)}) ===")
    greedy_f1s = compute_greedy_f1s(instances)
    greedy_mean = float(np.mean(greedy_f1s))
    print(f"  Greedy F1 (mean per-instance): {greedy_mean:.4f}")

    per_sample_f1s = [
        [per_instance_f1(s, inst["gold"], subtask=SUBTASK) for s in inst["samples"]]
        for inst in instances
    ]
    oracle_f1 = compute_oracle_f1(instances, per_sample_f1s)
    print(f"  Oracle F1: {oracle_f1:.4f}")

    print("  Computing signals...")
    signals = compute_signals(instances)

    print("  Computing correlations...")
    sig_results = {}
    for sig_name, sig_vals in signals.items():
        rho, p = spearman(sig_vals, greedy_f1s)
        sig_results[sig_name] = {"rho": rho, "p": p}
        print(f"    {sig_name}: rho={rho:.4f}, p={p:.6f}")

    print("  Computing selection F1...")
    sel_f1s = compute_selection_f1s(instances, per_sample_f1s)
    for sig_name in sig_results:
        sig_results[sig_name]["selection_f1"] = round(sel_f1s[sig_name], 4)
        print(f"    {sig_name} selection F1: {sel_f1s[sig_name]:.4f}")

    return {
        "n": len(instances),
        "signals": sig_results,
        "greedy_f1": round(greedy_mean, 4),
        "oracle_f1": round(oracle_f1, 4),
    }


def main():
    print("Loading data...")
    data = load_data()
    print(f"Total instances: {len(data)}")

    gold_nonempty = filter_gold_nonempty(data)
    print(f"Gold-nonempty (relations > 0): {len(gold_nonempty)}")

    full_result = analyze_subset(gold_nonempty, "Full Set (gold-nonempty)")

    greedy_f1s = compute_greedy_f1s(gold_nonempty)
    conditional = [inst for inst, f1 in zip(gold_nonempty, greedy_f1s) if f1 > 0]
    n_zero = len(gold_nonempty) - len(conditional)
    print(f"\nFiltered out {n_zero} instances with greedy F1=0 ({100*n_zero/len(gold_nonempty):.1f}%)")

    cond_result = analyze_subset(conditional, "Conditional Set (greedy F1 > 0)")
    cond_result["filter"] = "greedy_f1 > 0"

    output = {"full_set": full_result, "conditional_set": cond_result}

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nSaved to {OUTPUT_PATH}")
    print("\n" + json.dumps(output, indent=2))


if __name__ == "__main__":
    main()

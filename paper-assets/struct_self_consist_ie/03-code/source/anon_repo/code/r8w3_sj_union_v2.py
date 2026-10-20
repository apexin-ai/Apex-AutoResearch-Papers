#!/usr/bin/env python3
"""R8-W3 v2: SJ max vs union normalizer comparison with correct gold-empty filtering."""
import json
import os
import sys
import numpy as np
from itertools import combinations
from scipy.stats import spearmanr
from scipy.optimize import linear_sum_assignment

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import per_instance_f1
from consistency import _ner_soft_jaccard_pair

BASE = "/root/autodl-tmp/struct_self_consist_ie"

EXPERIMENTS = {
    "CoNLL NER | Qwen3-8B": {
        "path": f"{BASE}/output/exp002_conll2003/samples.jsonl",
        "subtask": "ner",
        "ref_sj_rho": 0.435,
    },
    "CoNLL NER | Qwen3-4B": {
        "path": f"{BASE}/output/exp_qwen3_4b_conll_scs_inference_v2/samples.jsonl",
        "subtask": "ner",
        "ref_sj_rho": 0.4217,
    },
    "SciERC NER | LLaMA-8B": {
        "path": f"{BASE}/output/exp007_llama_inference/samples.jsonl",
        "subtask": "ner",
        "ref_sj_rho": 0.363,
    },
    "SciERC NER | Qwen3-4B": {
        "path": f"{BASE}/output/exp_qwen3_4b_scierc_scs_inference/samples.jsonl",
        "subtask": "ner",
        "ref_sj_rho": 0.4221,
    },
}


def _span_soft_jaccard(s1_start, s1_end, s2_start, s2_end):
    overlap = max(0, min(s1_end, s2_end) - max(s1_start, s2_start))
    len1 = s1_end - s1_start
    len2 = s2_end - s2_start
    union = len1 + len2 - overlap
    if union <= 0:
        return 0.0
    return overlap / union


def _ner_sj_pair_both(entities_a, entities_b):
    """Return (sj_max, sj_union) for a pair of entity lists."""
    if not entities_a and not entities_b:
        return 1.0, 1.0
    if not entities_a or not entities_b:
        return 0.0, 0.0

    types = set()
    groups_a, groups_b = {}, {}
    for e in entities_a:
        t = e["type"]
        types.add(t)
        groups_a.setdefault(t, []).append(e)
    for e in entities_b:
        t = e["type"]
        types.add(t)
        groups_b.setdefault(t, []).append(e)

    total_matched_sim = 0.0
    total_max_weight = 0
    total_a_count = 0
    total_b_count = 0

    for t in types:
        ga = groups_a.get(t, [])
        gb = groups_b.get(t, [])
        na, nb = len(ga), len(gb)
        denom_max = max(na, nb)
        if denom_max == 0:
            continue

        total_max_weight += denom_max
        total_a_count += na
        total_b_count += nb

        if not ga or not gb:
            continue

        cost = np.zeros((na, nb), dtype=np.float64)
        for i, ea in enumerate(ga):
            for j, eb in enumerate(gb):
                cost[i, j] = _span_soft_jaccard(ea["start"], ea["end"],
                                                 eb["start"], eb["end"])

        row_ind, col_ind = linear_sum_assignment(-cost)
        matched_sim = cost[row_ind, col_ind].sum()
        total_matched_sim += matched_sim

    if total_max_weight == 0:
        return 1.0, 1.0

    sj_max = total_matched_sim / total_max_weight
    union_denom = total_a_count + total_b_count - total_matched_sim
    sj_union = total_matched_sim / union_denom if union_denom > 0 else 1.0

    return sj_max, sj_union


def compute_instance_sj_both(samples, subtask="ner"):
    """Mean pairwise SJ_max and SJ_union for one instance."""
    n = len(samples)
    if n <= 1:
        return 1.0, 1.0

    max_scores, union_scores = [], []
    for i, j in combinations(range(n), 2):
        sj_max, sj_union = _ner_sj_pair_both(
            samples[i].get("entities", []),
            samples[j].get("entities", []),
        )
        max_scores.append(sj_max)
        union_scores.append(sj_union)

    return float(np.mean(max_scores)), float(np.mean(union_scores))


def compute_instance_sj_max_ref(samples, subtask="ner"):
    """Reference SJ_max from consistency.py for cross-validation."""
    n = len(samples)
    if n <= 1:
        return 1.0
    scores = []
    for i, j in combinations(range(n), 2):
        s = _ner_soft_jaccard_pair(
            samples[i].get("entities", []),
            samples[j].get("entities", []),
        )
        scores.append(s)
    return float(np.mean(scores))


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def analyze_experiment(path, subtask, ref_sj_rho, max_samples=8):
    data = load_data(path)
    field = "entities" if subtask == "ner" else "relations"

    # Gold-empty filter (matching unified pipeline)
    valid_data = [d for d in data if len(d["gold"].get(field, [])) > 0]

    sj_max_list, sj_union_list, sj_ref_list, f1_list = [], [], [], []
    n_greedy_f1_zero = 0

    for inst in valid_data:
        samples = inst["samples"][:max_samples]
        gold = inst["gold"]

        greedy = inst.get("greedy", samples[0])
        f1 = per_instance_f1(greedy, gold, subtask=subtask)

        if f1 == 0.0:
            n_greedy_f1_zero += 1

        sj_max, sj_union = compute_instance_sj_both(samples, subtask)
        sj_ref = compute_instance_sj_max_ref(samples, subtask)

        sj_max_list.append(sj_max)
        sj_union_list.append(sj_union)
        sj_ref_list.append(sj_ref)
        f1_list.append(f1)

    rho_max, p_max = spearmanr(sj_max_list, f1_list)
    rho_union, p_union = spearmanr(sj_union_list, f1_list)
    rho_ref, p_ref = spearmanr(sj_ref_list, f1_list)

    # Cross-validation: our SJ_max should match consistency.py's implementation
    max_diff = max(abs(a - b) for a, b in zip(sj_max_list, sj_ref_list))

    return {
        "n_total": len(data),
        "n_gold_empty": len(data) - len(valid_data),
        "n_instances": len(valid_data),
        "n_greedy_f1_zero": n_greedy_f1_zero,
        "n_samples": min(max_samples, len(data[0]["samples"])),
        "rho_max": round(rho_max, 4),
        "p_max": p_max,
        "rho_union": round(rho_union, 4),
        "p_union": p_union,
        "delta_rho": round(rho_max - rho_union, 4),
        "ref_sj_rho": ref_sj_rho,
        "rho_max_vs_ref_diff": round(abs(rho_max - ref_sj_rho), 4),
        "rho_ref_consistency_py": round(rho_ref, 4),
        "sj_max_impl_max_diff": max_diff,
        "mean_sj_max": round(float(np.mean(sj_max_list)), 4),
        "mean_sj_union": round(float(np.mean(sj_union_list)), 4),
    }


def main():
    all_results = {}
    print("## SJ Normalizer Comparison (R8-W3 v2)\n")
    print("| Dataset | Model | n | ρ(SJ_max) | ρ(SJ_union) | Δρ | p_max | p_union | ref_ρ | Δref |")
    print("|---------|-------|---|-----------|-------------|-----|-------|---------|-------|------|")

    for name, cfg in EXPERIMENTS.items():
        if not os.path.exists(cfg["path"]):
            print(f"| {name} | — | SKIP | | | | | | | |")
            continue

        result = analyze_experiment(cfg["path"], cfg["subtask"], cfg["ref_sj_rho"])
        all_results[name] = result

        dataset, model = name.split(" | ")
        print(f"| {dataset} | {model} | {result['n_instances']} | "
              f"{result['rho_max']:.4f} | {result['rho_union']:.4f} | "
              f"{result['delta_rho']:+.4f} | {result['p_max']:.2e} | "
              f"{result['p_union']:.2e} | {result['ref_sj_rho']:.4f} | "
              f"{result['rho_max_vs_ref_diff']:.4f} |")

    print()

    # Validation
    print("### Validation")
    for name, r in all_results.items():
        ref_ok = r["rho_max_vs_ref_diff"] < 0.01
        impl_ok = r["sj_max_impl_max_diff"] < 1e-10
        print(f"  {name}: rho_max={r['rho_max']:.4f} vs ref={r['ref_sj_rho']:.4f} "
              f"(Δ={r['rho_max_vs_ref_diff']:.4f} {'OK' if ref_ok else 'MISMATCH'}), "
              f"impl_check={'OK' if impl_ok else 'FAIL'}, "
              f"rho_ref_consistency_py={r['rho_ref_consistency_py']:.4f}")

    print()

    # Conclusion
    deltas = [abs(r["delta_rho"]) for r in all_results.values()]
    max_delta = max(deltas) if deltas else 0
    print(f"### Conclusion")
    print(f"Max |Δρ| = {max_delta:.4f}")
    if max_delta < 0.01:
        print("All |Δρ| < 0.01. Normalizer choice does not affect the ranking conclusion.")
    elif max_delta < 0.02:
        print("Differences are minor (<0.02) and do not change the conclusion.")
    else:
        print("Non-trivial differences exist.")

    # Save
    out_path = f"{BASE}/output/review_round8/r8w3_sj_union_v2.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

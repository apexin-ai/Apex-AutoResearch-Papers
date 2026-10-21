#!/usr/bin/env python3
"""R8-W3: Compare SJ max normalizer vs union normalizer on Spearman rho."""
import json
import sys
import numpy as np
from itertools import combinations
from scipy.stats import spearmanr
from scipy.optimize import linear_sum_assignment

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie"

EXPERIMENTS = {
    "CoNLL NER | Qwen3-8B": {
        "path": f"{BASE}/output/exp002_conll2003/samples.jsonl",
        "subtask": "ner",
    },
    "CoNLL NER | Qwen3-4B": {
        "path": f"{BASE}/output/exp_qwen3_4b_conll_scs_inference_v2/samples.jsonl",
        "subtask": "ner",
    },
    "SciERC NER | Qwen3-8B": {
        "path": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
        "subtask": "ner",
    },
    "SciERC NER | Qwen3-4B": {
        "path": f"{BASE}/output/exp_qwen3_4b_scierc_scs_inference/samples.jsonl",
        "subtask": "ner",
    },
    "CoNLL NER | LLaMA-8B": {
        "path": f"{BASE}/output/exp_017_llama_conll_n16_r1024/samples.jsonl",
        "subtask": "ner",
    },
    "SciERC NER | LLaMA-8B": {
        "path": f"{BASE}/output/exp_018_llama_scierc_seed42_r1024/samples.jsonl",
        "subtask": "ner",
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
    """Return (sj_max, sj_union) for a single pair of entity lists."""
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
    # union = |A| + |B| - soft_intersection
    union_denom = total_a_count + total_b_count - total_matched_sim
    sj_union = total_matched_sim / union_denom if union_denom > 0 else 1.0

    return sj_max, sj_union


def compute_instance_sj_scores(samples, subtask="ner"):
    """Compute mean pairwise SJ_max and SJ_union for one instance."""
    n = len(samples)
    if n <= 1:
        return 1.0, 1.0

    field = "entities"
    max_scores, union_scores = [], []
    for i, j in combinations(range(n), 2):
        sj_max, sj_union = _ner_sj_pair_both(
            samples[i].get(field, []),
            samples[j].get(field, []),
        )
        max_scores.append(sj_max)
        union_scores.append(sj_union)

    return float(np.mean(max_scores)), float(np.mean(union_scores))


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def analyze_experiment(path, subtask, max_samples=8):
    data = load_data(path)
    sj_max_list, sj_union_list, f1_list = [], [], []

    for inst in data:
        samples = inst["samples"][:max_samples]
        gold = inst["gold"]

        # Greedy F1
        greedy = inst.get("greedy", samples[0])
        f1 = per_instance_f1(greedy, gold, subtask=subtask)

        # SJ scores
        sj_max, sj_union = compute_instance_sj_scores(samples, subtask)

        sj_max_list.append(sj_max)
        sj_union_list.append(sj_union)
        f1_list.append(f1)

    # Spearman rho
    rho_max, p_max = spearmanr(sj_max_list, f1_list)
    rho_union, p_union = spearmanr(sj_union_list, f1_list)

    return {
        "n_instances": len(data),
        "n_samples": len(data[0]["samples"][:max_samples]),
        "rho_max": rho_max,
        "p_max": p_max,
        "rho_union": rho_union,
        "p_union": p_union,
        "delta_rho": rho_max - rho_union,
        "mean_sj_max": float(np.mean(sj_max_list)),
        "mean_sj_union": float(np.mean(sj_union_list)),
    }


def main():
    print("## SJ Normalizer Comparison (R8-W3)\n")
    print("| Dataset | Model | n | ρ(SJ_max) | ρ(SJ_union) | Δρ |")
    print("|---------|-------|---|-----------|-------------|-----|")

    all_results = {}
    for name, cfg in EXPERIMENTS.items():
        import os
        if not os.path.exists(cfg["path"]):
            print(f"| {name} | — | SKIP: file not found | | |")
            continue

        result = analyze_experiment(cfg["path"], cfg["subtask"])
        all_results[name] = result

        dataset, model = name.split(" | ")
        print(f"| {dataset} | {model} | {result['n_samples']} | "
              f"{result['rho_max']:.4f} | {result['rho_union']:.4f} | "
              f"{result['delta_rho']:+.4f} |")

    print()

    # Check if all deltas are negligible
    deltas = [r["delta_rho"] for r in all_results.values()]
    max_delta = max(abs(d) for d in deltas) if deltas else 0
    if max_delta < 0.01:
        print(f"**Conclusion**: All |Δρ| < 0.01 (max = {max_delta:.4f}). "
              "The choice of normalizer does not affect the ranking conclusion.")
    elif max_delta < 0.02:
        print(f"**Conclusion**: Max |Δρ| = {max_delta:.4f}. "
              "Differences are minor and do not change the conclusion.")
    else:
        print(f"**Conclusion**: Max |Δρ| = {max_delta:.4f}. "
              "Some non-trivial differences exist — further investigation recommended.")

    # Detailed stats
    print("\n### Detailed Statistics\n")
    print("| Dataset | Model | mean(SJ_max) | mean(SJ_union) | ρ_max p-val | ρ_union p-val |")
    print("|---------|-------|-------------|----------------|-------------|---------------|")
    for name, r in all_results.items():
        dataset, model = name.split(" | ")
        print(f"| {dataset} | {model} | {r['mean_sj_max']:.4f} | "
              f"{r['mean_sj_union']:.4f} | {r['p_max']:.2e} | {r['p_union']:.2e} |")

    # Save JSON
    out_path = f"{BASE}/output/review_round8/r8w3_sj_normalizer_comparison.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

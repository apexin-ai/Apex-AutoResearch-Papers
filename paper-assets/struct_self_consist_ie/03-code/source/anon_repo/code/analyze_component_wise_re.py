"""Component-wise RE soft Jaccard decomposition analysis.

Decomposes RE soft Jaccard into head_sj, tail_sj, type_match components,
computes Spearman rho for each vs per-instance RE F1.
"""

import json
import sys
import numpy as np
from itertools import combinations
from scipy import stats
from scipy.optimize import linear_sum_assignment

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import _span_soft_jaccard, fleiss_kappa_surface, structural_consistency_soft_jaccard
from evaluation import per_instance_f1


def compute_pair_components(rels_a, rels_b):
    if not rels_a and not rels_b:
        return {k: 1.0 for k in ['head_sj', 'tail_sj', 'type_match', 'multiplicative', 'additive']}
    if not rels_a or not rels_b:
        return {k: 0.0 for k in ['head_sj', 'tail_sj', 'type_match', 'multiplicative', 'additive']}

    na, nb = len(rels_a), len(rels_b)
    denom = max(na, nb)

    head_sj_mat = np.zeros((na, nb))
    tail_sj_mat = np.zeros((na, nb))
    type_match_mat = np.zeros((na, nb))

    for i, a in enumerate(rels_a):
        for j, b in enumerate(rels_b):
            head_sj_mat[i, j] = _span_soft_jaccard(
                a["head_start"], a["head_end"], b["head_start"], b["head_end"])
            tail_sj_mat[i, j] = _span_soft_jaccard(
                a["tail_start"], a["tail_end"], b["tail_start"], b["tail_end"])
            type_match_mat[i, j] = 1.0 if a["type"] == b["type"] else 0.0

    # Same cost as original _re_soft_jaccard_pair
    cost = head_sj_mat * tail_sj_mat * type_match_mat
    row_ind, col_ind = linear_sum_assignment(-cost)

    matched_head = head_sj_mat[row_ind, col_ind].sum()
    matched_tail = tail_sj_mat[row_ind, col_ind].sum()
    matched_type = type_match_mat[row_ind, col_ind].sum()
    matched_mult = cost[row_ind, col_ind].sum()

    additive_mat = (head_sj_mat + tail_sj_mat) / 2 * type_match_mat
    matched_add = additive_mat[row_ind, col_ind].sum()

    return {
        'head_sj': matched_head / denom,
        'tail_sj': matched_tail / denom,
        'type_match': matched_type / denom,
        'multiplicative': matched_mult / denom,
        'additive': matched_add / denom,
    }


def compute_instance_components(samples):
    n = len(samples)
    if n <= 1:
        return {k: 1.0 for k in ['head_sj', 'tail_sj', 'type_match', 'multiplicative', 'additive']}

    pair_scores = {k: [] for k in ['head_sj', 'tail_sj', 'type_match', 'multiplicative', 'additive']}
    for i, j in combinations(range(n), 2):
        scores = compute_pair_components(
            samples[i].get('relations', []),
            samples[j].get('relations', []))
        for k, v in scores.items():
            pair_scores[k].append(v)

    return {k: float(np.mean(v)) for k, v in pair_scores.items()}


def main():
    data_path = '/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/samples.jsonl'
    instances = []
    with open(data_path) as f:
        for line in f:
            instances.append(json.loads(line))

    re_instances = [inst for inst in instances if inst['gold'].get('relations', [])]
    n_full = len(re_instances)

    components = {k: [] for k in ['head_sj', 'tail_sj', 'type_match', 'multiplicative', 'additive']}
    fleiss_scores = []
    greedy_f1s = []
    original_sj = []

    for idx, inst in enumerate(re_instances):
        if idx % 50 == 0:
            print(f"  Processing {idx}/{n_full}...", flush=True)

        comp = compute_instance_components(inst['samples'])
        for k in components:
            components[k].append(comp[k])

        fleiss_scores.append(fleiss_kappa_surface(inst['samples'], subtask='re'))
        original_sj.append(structural_consistency_soft_jaccard(inst['samples'], subtask='re'))

        greedy = inst.get('greedy', inst['samples'][0])
        greedy_f1s.append(per_instance_f1(greedy, inst['gold'], subtask='re'))

    # Conditional mask: exclude greedy_F1=0 instances (knowledge-gap)
    cond_mask = [greedy_f1s[i] > 0 for i in range(n_full)]
    n_cond = sum(cond_mask)

    print(f"\n=== E1: Component-wise RE SJ Decomposition ===")
    print(f"Instances: {n_full} (gold-nonempty RE)")
    print(f"Conditional instances: {n_cond} (filtered all-samples-F1=0)")

    # Verification
    mult_rho = stats.spearmanr(components['multiplicative'], greedy_f1s).statistic
    orig_rho = stats.spearmanr(original_sj, greedy_f1s).statistic
    mult_vs_orig_diff = np.mean(np.abs(np.array(components['multiplicative']) - np.array(original_sj)))
    print(f"\nVerification:")
    print(f"  multiplicative ρ = {mult_rho:.4f}, original_sj ρ = {orig_rho:.4f}")
    print(f"  mean |multiplicative - original_sj| = {mult_vs_orig_diff:.6f}")

    all_scores = {**components, 'fleiss_kappa': fleiss_scores}

    def print_table(subset_name, n, score_dict, f1s):
        print(f"\n--- {subset_name} ({n} instances) ---")
        print(f"{'Component':<20} | {'ρ':>8} | {'p-value':>12} | {'mean score':>10}")
        print("-" * 60)
        for name in ['head_sj', 'tail_sj', 'type_match', 'multiplicative', 'additive', 'fleiss_kappa']:
            scores = score_dict[name]
            rho, p = stats.spearmanr(scores, f1s)
            mean = np.mean(scores)
            print(f"{name:<20} | {rho:>8.4f} | {p:>12.3e} | {mean:>10.4f}")

    print_table("Full Set", n_full, all_scores, greedy_f1s)

    cond_scores = {k: [v[i] for i in range(n_full) if cond_mask[i]] for k, v in all_scores.items()}
    cond_f1s = [greedy_f1s[i] for i in range(n_full) if cond_mask[i]]
    print_table("Conditional Set", n_cond, cond_scores, cond_f1s)

    # Diagnosis
    head_rho_full = stats.spearmanr(components['head_sj'], greedy_f1s).statistic
    mult_rho_full = stats.spearmanr(components['multiplicative'], greedy_f1s).statistic
    add_rho_full = stats.spearmanr(components['additive'], greedy_f1s).statistic
    tail_rho_full = stats.spearmanr(components['tail_sj'], greedy_f1s).statistic
    type_rho_full = stats.spearmanr(components['type_match'], greedy_f1s).statistic

    ner_rho = 0.383
    print(f"\n--- Diagnosis ---")
    print(f"head_sj ρ vs NER ρ_sj ({ner_rho}): {'close' if abs(head_rho_full - ner_rho) < 0.05 else 'far'} (Δ={head_rho_full - ner_rho:+.4f})")
    print(f"Multiplicative penalty: head_sj ρ - multiplicative_sj ρ = {head_rho_full - mult_rho_full:+.4f}")
    print(f"Tail penalty: tail_sj ρ - multiplicative_sj ρ = {tail_rho_full - mult_rho_full:+.4f}")
    print(f"Type gate penalty: type_match ρ - multiplicative_sj ρ = {type_rho_full - mult_rho_full:+.4f}")
    print(f"Additive fix improvement: additive_sj ρ - multiplicative_sj ρ = {add_rho_full - mult_rho_full:+.4f}")

    if head_rho_full > mult_rho_full + 0.05:
        print(f"\n>>> CONCLUSION: head_sj alone (ρ={head_rho_full:.4f}) significantly outperforms "
              f"multiplicative (ρ={mult_rho_full:.4f}). Multiplicative penalty confirmed as root cause.")
    elif head_rho_full > mult_rho_full:
        print(f"\n>>> CONCLUSION: head_sj (ρ={head_rho_full:.4f}) modestly better than "
              f"multiplicative (ρ={mult_rho_full:.4f}). Effect present but small.")
    else:
        print(f"\n>>> CONCLUSION: head_sj (ρ={head_rho_full:.4f}) does NOT outperform "
              f"multiplicative (ρ={mult_rho_full:.4f}). Multiplicative penalty NOT the root cause.")

    # Save results
    results = {'n_full': n_full, 'n_conditional': n_cond, 'full': {}, 'conditional': {}}
    for name in ['head_sj', 'tail_sj', 'type_match', 'multiplicative', 'additive', 'fleiss_kappa']:
        rho, p = stats.spearmanr(all_scores[name], greedy_f1s)
        results['full'][name] = {'rho': float(rho), 'p_value': float(p), 'mean': float(np.mean(all_scores[name]))}
        cs = cond_scores[name]
        rho_c, p_c = stats.spearmanr(cs, cond_f1s)
        results['conditional'][name] = {'rho': float(rho_c), 'p_value': float(p_c), 'mean': float(np.mean(cs))}

    out_path = '/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/e1_component_decomposition.json'
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == '__main__':
    main()

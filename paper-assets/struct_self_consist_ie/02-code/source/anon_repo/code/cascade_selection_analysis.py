#!/usr/bin/env python3
"""Cascade selection analysis: VC+LP, LP+VC, SJ+LP cascaded selection strategies.

For SF3 reviewer response. Tests whether two-stage cascaded selection
(filter by signal A top-k, then pick best by signal B) outperforms
single-signal selection.
"""

import json
import os
import sys
import numpy as np
from collections import Counter

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import (
    _ner_soft_jaccard_pair,
    _re_soft_jaccard_pair,
    _extract_surface_keys,
)
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie"

DATASETS = {
    "scierc_ner": {
        "path": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
        "subtask": "ner",
    },
    "conll_ner": {
        "path": f"{BASE}/output/exp002_conll2003/samples.jsonl",
        "subtask": "ner",
    },
    "scierc_re": {
        "path": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
        "subtask": "re",
    },
}

K_VALUES = [2, 3, 4, 5, 6]
N_RANDOM = 1000
RANDOM_SEED = 42


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def compute_sample_sj_scores(instance, subtask):
    samples = instance["samples"]
    N = len(samples)
    field = "entities" if subtask == "ner" else "relations"
    pair_fn = _ner_soft_jaccard_pair if subtask == "ner" else _re_soft_jaccard_pair
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = pair_fn(samples[i].get(field, []), samples[j].get(field, []))
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]


def compute_sample_vc_scores(instance, subtask):
    samples = instance["samples"]
    N = len(samples)
    key_sets = [frozenset(_extract_surface_keys(s, subtask)) for s in samples]
    all_keys = set()
    for ks in key_sets:
        all_keys |= ks
    if not all_keys:
        return [1.0] * N

    key_counts = Counter()
    for ks in key_sets:
        for k in ks:
            key_counts[k] += 1

    scores = []
    for i in range(N):
        if not key_sets[i]:
            scores.append(0.0)
        else:
            avg_vote = np.mean([key_counts[k] / N for k in key_sets[i]])
            scores.append(float(avg_vote))
    return scores


def compute_sample_fk_scores(instance, subtask):
    samples = instance["samples"]
    N = len(samples)
    key_sets = [frozenset(_extract_surface_keys(s, subtask)) for s in samples]
    scores = []
    for i in range(N):
        sims = []
        for j in range(N):
            if i == j:
                continue
            union = len(key_sets[i] | key_sets[j])
            inter = len(key_sets[i] & key_sets[j])
            sims.append(inter / union if union > 0 else 1.0)
        scores.append(float(np.mean(sims)) if sims else 1.0)
    return scores


def compute_sample_em_scores(instance, subtask):
    samples = instance["samples"]
    N = len(samples)
    key_sets = [frozenset(_extract_surface_keys(s, subtask)) for s in samples]
    counter = Counter(key_sets)
    return [counter[key_sets[i]] / N for i in range(N)]


def compute_sample_lp_scores(instance):
    if "logprobs" in instance and instance["logprobs"]:
        return list(instance["logprobs"])
    return [s.get("mean_logprob", float("-inf")) for s in instance["samples"]]


def cascade_select(scores_a, scores_b, k):
    N = len(scores_a)
    k = min(k, N)
    top_k_idx = np.argsort(scores_a)[-k:]
    best_idx = top_k_idx[np.argmax([scores_b[i] for i in top_k_idx])]
    return int(best_idx)


def analyze_dataset(name, config):
    path = config["path"]
    subtask = config["subtask"]
    instances = load_data(path)

    entity_key = "entities" if subtask == "ner" else "relations"
    valid = [inst for inst in instances if len(inst["gold"].get(entity_key, [])) > 0]

    print(f"  {name}: {len(instances)} total, {len(valid)} gold-nonempty")

    rng = np.random.RandomState(RANDOM_SEED)

    greedy_f1s = []
    oracle_f1s = []
    random_f1_matrix = []

    signal_names = ["LP", "VC", "SJ", "FK", "EM"]
    single_selected_f1s = {s: [] for s in signal_names}

    cascade_configs = [
        ("vc_then_lp", "VC", "LP"),
        ("lp_then_vc", "LP", "VC"),
        ("sj_then_lp", "SJ", "LP"),
        ("sj_then_vc", "SJ", "VC"),
        ("fk_then_lp", "FK", "LP"),
        ("em_then_lp", "EM", "LP"),
    ]
    cascade_f1s = {f"{c[0]}_k{k}": [] for c in cascade_configs for k in K_VALUES}

    for inst in valid:
        samples = inst["samples"]
        N = len(samples)
        gold = inst["gold"]

        sample_f1s = [per_instance_f1(s, gold, subtask=subtask) for s in samples]

        greedy = inst.get("greedy", samples[0])
        greedy_f1 = per_instance_f1(greedy, gold, subtask=subtask)
        greedy_f1s.append(greedy_f1)

        oracle_f1s.append(max(sample_f1s))

        rand_f1s = [sample_f1s[rng.randint(N)] for _ in range(N_RANDOM)]
        random_f1_matrix.append(rand_f1s)

        scores = {
            "LP": compute_sample_lp_scores(inst),
            "VC": compute_sample_vc_scores(inst, subtask),
            "SJ": compute_sample_sj_scores(inst, subtask),
            "FK": compute_sample_fk_scores(inst, subtask),
            "EM": compute_sample_em_scores(inst, subtask),
        }

        for sig in signal_names:
            best_idx = int(np.argmax(scores[sig]))
            single_selected_f1s[sig].append(sample_f1s[best_idx])

        for cascade_name, sig_a, sig_b in cascade_configs:
            for k in K_VALUES:
                idx = cascade_select(scores[sig_a], scores[sig_b], k)
                cascade_f1s[f"{cascade_name}_k{k}"].append(sample_f1s[idx])

    greedy_f1 = float(np.mean(greedy_f1s))
    oracle_f1 = float(np.mean(oracle_f1s))
    random_f1 = float(np.mean([np.mean(r) for r in random_f1_matrix]))

    result = {
        "n_instances": len(valid),
        "greedy_f1": round(greedy_f1, 4),
        "oracle_f1": round(oracle_f1, 4),
        "random_f1": round(random_f1, 4),
    }

    for sig in signal_names:
        result[f"{sig.lower()}_only_f1"] = round(float(np.mean(single_selected_f1s[sig])), 4)

    for cascade_name, sig_a, sig_b in cascade_configs:
        cascade_result = {}
        for k in K_VALUES:
            key = f"{cascade_name}_k{k}"
            f1_val = round(float(np.mean(cascade_f1s[key])), 4)
            cascade_result[f"k{k}"] = f1_val
        result[cascade_name] = cascade_result

    return result


def find_best_cascade(results):
    best_config = None
    best_improvement = -999
    best_f1 = -999

    for ds_name, ds_res in results.items():
        if ds_name in ("best_cascade_config", "conclusion"):
            continue
        single_best_sig = None
        single_best_f1 = -1
        for sig in ["lp", "vc", "sj", "fk", "em"]:
            f1 = ds_res.get(f"{sig}_only_f1", 0)
            if f1 > single_best_f1:
                single_best_f1 = f1
                single_best_sig = sig

        for cascade_name in ["vc_then_lp", "lp_then_vc", "sj_then_lp", "sj_then_vc", "fk_then_lp", "em_then_lp"]:
            if cascade_name not in ds_res:
                continue
            for k_str, f1 in ds_res[cascade_name].items():
                improvement = f1 - single_best_f1
                if improvement > best_improvement:
                    best_improvement = improvement
                    best_f1 = f1
                    best_config = f"{ds_name}/{cascade_name}/{k_str} (f1={f1:.4f}, Δ={improvement:+.4f} vs {single_best_sig}_only={single_best_f1:.4f})"

    return best_config, best_improvement


def main():
    all_results = {}

    for name, config in DATASETS.items():
        print(f"\nAnalyzing {name}...")
        all_results[name] = analyze_dataset(name, config)

    best_config, best_improvement = find_best_cascade(all_results)
    all_results["best_cascade_config"] = best_config

    any_improvement = best_improvement >= 0.01
    if any_improvement:
        all_results["conclusion"] = f"Cascade selection improves over single-signal by up to {best_improvement:+.4f} F1. Best: {best_config}"
    else:
        all_results["conclusion"] = f"Cascade selection does NOT consistently improve over single-signal selection. Max improvement: {best_improvement:+.4f} F1."

    out_path = f"{BASE}/output/review_round9_experiments/vc_lp_cascade/cascade_results.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved: {out_path}")

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    for ds_name in ["scierc_ner", "conll_ner", "scierc_re"]:
        if ds_name not in all_results:
            continue
        r = all_results[ds_name]
        print(f"\n--- {ds_name} ({r['n_instances']} instances) ---")
        print(f"  Greedy:  {r['greedy_f1']:.4f}")
        print(f"  Random:  {r['random_f1']:.4f}")
        print(f"  Oracle:  {r['oracle_f1']:.4f}")
        print(f"  LP-only: {r['lp_only_f1']:.4f}")
        print(f"  VC-only: {r['vc_only_f1']:.4f}")
        print(f"  SJ-only: {r['sj_only_f1']:.4f}")
        print(f"  FK-only: {r['fk_only_f1']:.4f}")
        print(f"  EM-only: {r['em_only_f1']:.4f}")
        print()

        for cascade_name in ["vc_then_lp", "lp_then_vc", "sj_then_lp", "sj_then_vc", "fk_then_lp", "em_then_lp"]:
            if cascade_name not in r:
                continue
            vals = r[cascade_name]
            k_str = " | ".join([f"k{k}={vals[f'k{k}']:.4f}" for k in K_VALUES])
            print(f"  {cascade_name}: {k_str}")

    print(f"\nBest cascade: {all_results['best_cascade_config']}")
    print(f"Conclusion: {all_results['conclusion']}")


if __name__ == "__main__":
    main()

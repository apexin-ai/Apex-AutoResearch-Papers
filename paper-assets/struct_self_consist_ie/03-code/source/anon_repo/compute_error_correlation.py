"""Compute entity-level error correlation between FS and ZS settings."""
import json
import math
import sys
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy import stats

N_SAMPLES = 8

DATASETS = {
    "scierc": {
        "fs": "/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42/samples.jsonl",
        "zs": "/root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation/samples.jsonl",
    },
    "conll": {
        "fs": "/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16/samples.jsonl",
        "zs": "/root/autodl-tmp/struct_self_consist_ie/output/review_round9_experiments/freeform_conll/seed_42/samples.jsonl",
    },
}


def load_data(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(json.loads(line))
    return data


def entity_set(entities):
    return {(e["text"], e["type"]) for e in entities}


def compute_error_set(predicted_entities, gold_entities):
    pred = entity_set(predicted_entities)
    gold = entity_set(gold_entities)
    fp = {(t, ty, "FP") for t, ty in pred - gold}
    fn = {(t, ty, "FN") for t, ty in gold - pred}
    return fp | fn


def pairwise_jaccard(error_sets):
    jaccards = []
    for i, j in combinations(range(len(error_sets)), 2):
        union = error_sets[i] | error_sets[j]
        if len(union) == 0:
            continue
        inter = error_sets[i] & error_sets[j]
        jaccards.append(len(inter) / len(union))
    return jaccards


def binary_entropy(p):
    if p <= 0 or p >= 1:
        return 0.0
    return -(p * math.log2(p) + (1 - p) * math.log2(1 - p))


def compute_entity_entropy(samples, n_samples):
    all_entities = set()
    for s in samples:
        all_entities |= entity_set(s["entities"])
    if not all_entities:
        return 0.0
    entropies = []
    for ent in all_entities:
        count = sum(1 for s in samples if ent in entity_set(s["entities"]))
        p = count / n_samples
        entropies.append(binary_entropy(p))
    return np.mean(entropies) if entropies else 0.0


def analyze_dataset(dataset_name):
    fs_data = load_data(DATASETS[dataset_name]["fs"])
    zs_data = load_data(DATASETS[dataset_name]["zs"])

    zs_by_id = {d["id"]: d for d in zs_data}

    fs_jaccards_per_instance = []
    zs_jaccards_per_instance = []
    fs_entropies = []
    zs_entropies = []
    n_matched = 0
    n_skipped_no_errors = 0

    for fs_inst in fs_data:
        iid = fs_inst["id"]
        if iid not in zs_by_id:
            continue
        zs_inst = zs_by_id[iid]

        gold_ents = fs_inst["gold"]["entities"]

        fs_samples = fs_inst["samples"][:N_SAMPLES]
        zs_samples = zs_inst["samples"][:N_SAMPLES]

        if len(fs_samples) < N_SAMPLES or len(zs_samples) < N_SAMPLES:
            continue

        fs_errors = [compute_error_set(s["entities"], gold_ents) for s in fs_samples]
        zs_errors = [compute_error_set(s["entities"], gold_ents) for s in zs_samples]

        fs_j = pairwise_jaccard(fs_errors)
        zs_j = pairwise_jaccard(zs_errors)

        if fs_j and zs_j:
            fs_jaccards_per_instance.append(np.mean(fs_j))
            zs_jaccards_per_instance.append(np.mean(zs_j))
        else:
            n_skipped_no_errors += 1
            fs_jaccards_per_instance.append(np.mean(fs_j) if fs_j else 0.0)
            zs_jaccards_per_instance.append(np.mean(zs_j) if zs_j else 0.0)

        fs_entropies.append(compute_entity_entropy(fs_samples, N_SAMPLES))
        zs_entropies.append(compute_entity_entropy(zs_samples, N_SAMPLES))

        n_matched += 1

    fs_j_arr = np.array(fs_jaccards_per_instance)
    zs_j_arr = np.array(zs_jaccards_per_instance)
    fs_e_arr = np.array(fs_entropies)
    zs_e_arr = np.array(zs_entropies)

    stat_j, p_j = stats.wilcoxon(fs_j_arr, zs_j_arr, alternative="two-sided")
    z_score = stats.norm.ppf(p_j / 2)
    effect_size_j = abs(z_score) / math.sqrt(n_matched)

    stat_e, p_e = stats.wilcoxon(fs_e_arr, zs_e_arr, alternative="two-sided")
    z_score_e = stats.norm.ppf(p_e / 2)
    effect_size_e = abs(z_score_e) / math.sqrt(n_matched)

    if p_j < 0.05:
        if fs_j_arr.mean() > zs_j_arr.mean():
            interp = "FS error overlap significantly HIGHER than ZS (supports demonstration-induced error correlation)"
        else:
            interp = "FS error overlap significantly LOWER than ZS"
    else:
        interp = "No significant difference in error overlap between FS and ZS"

    return {
        "fs": {
            "mean_pairwise_error_jaccard": round(float(fs_j_arr.mean()), 4),
            "std_pairwise_error_jaccard": round(float(fs_j_arr.std()), 4),
            "median_pairwise_error_jaccard": round(float(np.median(fs_j_arr)), 4),
            "mean_entity_entropy": round(float(fs_e_arr.mean()), 4),
            "std_entity_entropy": round(float(fs_e_arr.std()), 4),
        },
        "zs": {
            "mean_pairwise_error_jaccard": round(float(zs_j_arr.mean()), 4),
            "std_pairwise_error_jaccard": round(float(zs_j_arr.std()), 4),
            "median_pairwise_error_jaccard": round(float(np.median(zs_j_arr)), 4),
            "mean_entity_entropy": round(float(zs_e_arr.mean()), 4),
            "std_entity_entropy": round(float(zs_e_arr.std()), 4),
        },
        "jaccard_test": {
            "test_name": "wilcoxon_signed_rank",
            "statistic": round(float(stat_j), 4),
            "p_value": float(p_j),
            "effect_size_r": round(float(effect_size_j), 4),
            "direction": "fs>zs" if fs_j_arr.mean() > zs_j_arr.mean() else "zs>fs",
        },
        "entropy_test": {
            "test_name": "wilcoxon_signed_rank",
            "statistic": round(float(stat_e), 4),
            "p_value": float(p_e),
            "effect_size_r": round(float(effect_size_e), 4),
            "direction": "fs>zs" if fs_e_arr.mean() > zs_e_arr.mean() else "zs>fs",
        },
        "n_instances": n_matched,
        "n_skipped_no_errors": n_skipped_no_errors,
        "interpretation": interp,
    }


def main():
    results = {}
    for dataset in DATASETS:
        print(f"Processing {dataset}...", file=sys.stderr)
        results[dataset] = analyze_dataset(dataset)
        print(f"  {dataset} done: n={results[dataset]['n_instances']}", file=sys.stderr)

    out_path = "/root/autodl-tmp/struct_self_consist_ie/output/fs_vs_zs_error_correlation.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {out_path}", file=sys.stderr)

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()

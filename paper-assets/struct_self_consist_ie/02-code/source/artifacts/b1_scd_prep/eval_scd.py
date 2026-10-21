#!/usr/bin/env python3
"""B1 SCD evaluation: compare pre/post-distillation greedy and construction F1.

Reports 4 metrics (Q3):
  1. Pre-SCD greedy F1 (from existing signal report)
  2. Pre-SCD N=8 construction F1 (from existing signal report)
  3. Post-SCD greedy F1 (run inference)
  4. Post-SCD N=8 construction F1 (run inference)

Key claim: post-SCD greedy >= pre-SCD construction.

Usage:
    python eval_scd.py --dataset fewnerd --model-path <merged_scd_model> \
                       --pre-report <path_to_signal_report.json>
"""

import argparse
import json
import os
import statistics
import sys
from collections import Counter, defaultdict

import numpy as np

BASE = "/root/autodl-tmp/struct_self_consist_ie"


# --------------- F1 Computation ---------------

def span_set(entities):
    return set((e["start"], e["end"], e["type"]) for e in entities)


def entity_f1(pred_entities, gold_entities):
    pred = span_set(pred_entities)
    gold = span_set(gold_entities)
    if not pred and not gold:
        return 1.0
    if not pred or not gold:
        return 0.0
    tp = len(pred & gold)
    if tp == 0:
        return 0.0
    p = tp / len(pred)
    r = tp / len(gold)
    return 2 * p * r / (p + r)


def bootstrap_ci(values, n_boot=2000, seed=42):
    rng = np.random.RandomState(seed)
    arr = np.array(values)
    n = len(arr)
    if n == 0:
        return {"mean": 0.0, "ci_lo": 0.0, "ci_hi": 0.0}
    boot_means = np.array([arr[rng.randint(0, n, n)].mean() for _ in range(n_boot)])
    boot_means.sort()
    return {
        "mean": float(arr.mean()),
        "ci_lo": float(boot_means[int(0.025 * n_boot)]),
        "ci_hi": float(boot_means[int(0.975 * n_boot)]),
    }


def paired_bootstrap_test(f1_a, f1_b, n_boot=10000, seed=42):
    """Test if system B is significantly better than system A."""
    rng = np.random.RandomState(seed)
    a = np.array(f1_a)
    b = np.array(f1_b)
    n = len(a)
    delta_obs = b.mean() - a.mean()
    count = 0
    for _ in range(n_boot):
        idx = rng.randint(0, n, n)
        if (b[idx].mean() - a[idx].mean()) <= 0:
            count += 1
    p_value = count / n_boot
    return {"delta": float(delta_obs), "p_value": float(p_value)}


# --------------- Construction Functions ---------------

def get_sample_mean_logprob(sample, inst, idx):
    if "mean_logprob" in sample:
        return sample["mean_logprob"]
    if "logprobs" in inst and idx < len(inst["logprobs"]):
        return inst["logprobs"][idx]
    return None


def consensus_construct(inst, high_thresh, medium_thresh):
    samples = inst["samples"]
    N = len(samples)

    entity_counts = Counter()
    entity_sample_indices = defaultdict(list)

    for i, s in enumerate(samples):
        seen = set()
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_counts[key] += 1
                entity_sample_indices[key].append(i)
                seen.add(key)

    sample_lps = []
    for i, s in enumerate(samples):
        lp = get_sample_mean_logprob(s, inst, i)
        if lp is not None:
            sample_lps.append(lp)
    instance_median_lp = statistics.median(sample_lps) if sample_lps else 0.0

    consensus = []
    for entity_key, count in entity_counts.items():
        freq = count / N
        if freq > high_thresh:
            consensus.append(entity_key)
        elif freq > medium_thresh:
            contributing_lps = []
            for i in entity_sample_indices[entity_key]:
                lp = get_sample_mean_logprob(samples[i], inst, i)
                if lp is not None:
                    contributing_lps.append(lp)
            if contributing_lps:
                if statistics.mean(contributing_lps) > instance_median_lp:
                    consensus.append(entity_key)

    text_map = {}
    for s in samples:
        for e in s.get("entities", []):
            text_map[(e["start"], e["end"], e["type"])] = e.get("text", "")

    return [{"start": s, "end": e, "type": t, "text": text_map.get((s, e, t), "")}
            for s, e, t in consensus]


def get_construction(inst, method, N):
    theta = 2 / N
    if method == "theta2n":
        return consensus_construct(inst, high_thresh=theta, medium_thresh=0.0)
    elif method == "lp_weighted":
        return consensus_construct(inst, high_thresh=0.5, medium_thresh=theta)
    else:
        raise ValueError(f"Unknown method: {method}")


# --------------- Evaluation ---------------

CONSTRUCTION_METHODS = {
    "fewnerd": "theta2n",
    "scierc": "theta2n",
    "conll": "lp_weighted",
}

PRE_REPORT_PATHS = {
    "fewnerd": f"{BASE}/output/exp_fewnerd_seed123/full_signal_report.json",
    "scierc": f"{BASE}/output/exp_scierc_seed456/full_signal_report.json",
    "conll": f"{BASE}/output/exp_conll_seed123/full_signal_report.json",
}

PRE_SAMPLES_PATHS = {
    "fewnerd": f"{BASE}/output/exp_fewnerd_seed123/samples.jsonl",
    "scierc": f"{BASE}/output/exp_scierc_seed456/samples.jsonl",
    "conll": f"{BASE}/output/exp_conll_seed123/samples.jsonl",
}


def load_pre_metrics(dataset):
    """Load pre-SCD metrics from existing signal reports."""
    report_path = PRE_REPORT_PATHS[dataset]
    with open(report_path) as f:
        report = json.load(f)

    key = list(report.keys())[0]
    data = report[key]
    baselines = data["baselines"]

    method = CONSTRUCTION_METHODS[dataset]
    if method == "theta2n":
        construction_key = "consensus_theta2n"
    else:
        construction_key = "consensus_lp_weighted"

    return {
        "greedy_f1": baselines["greedy"],
        "construction_f1": baselines[construction_key],
        "oracle_f1": baselines["oracle"],
    }


def evaluate_post_scd(post_samples_path, dataset, gold_filter=True):
    """Evaluate post-SCD model outputs.

    Expects post_samples_path to be a samples.jsonl with N=8 samples + greedy.
    """
    instances = []
    with open(post_samples_path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if gold_filter and len(obj["gold"].get("entities", [])) == 0:
                continue
            instances.append(obj)

    N = len(instances[0]["samples"]) if instances else 0
    method = CONSTRUCTION_METHODS[dataset]

    greedy_f1s = []
    construction_f1s = []

    for inst in instances:
        gold_ents = inst["gold"]["entities"]

        greedy_f1s.append(entity_f1(inst["greedy"]["entities"], gold_ents))

        construction_ents = get_construction(inst, method, N)
        construction_f1s.append(entity_f1(construction_ents, gold_ents))

    return {
        "greedy_f1": bootstrap_ci(greedy_f1s),
        "construction_f1": bootstrap_ci(construction_f1s),
        "n_instances": len(instances),
        "greedy_f1_raw": greedy_f1s,
        "construction_f1_raw": construction_f1s,
    }


def run_comparison(dataset, post_samples_path):
    """Full comparison: pre vs post SCD."""
    print(f"\n{'='*60}")
    print(f"SCD Evaluation: {dataset}")
    print(f"{'='*60}")

    # Pre-SCD metrics
    pre = load_pre_metrics(dataset)
    print(f"\n  Pre-SCD:")
    print(f"    Greedy F1:       {pre['greedy_f1']['mean']:.4f} "
          f"[{pre['greedy_f1']['ci_lo']:.4f}, {pre['greedy_f1']['ci_hi']:.4f}]")
    print(f"    Construction F1: {pre['construction_f1']['mean']:.4f} "
          f"[{pre['construction_f1']['ci_lo']:.4f}, {pre['construction_f1']['ci_hi']:.4f}]")
    print(f"    Oracle F1:       {pre['oracle_f1']['mean']:.4f}")

    # Post-SCD metrics
    if not os.path.exists(post_samples_path):
        print(f"\n  Post-SCD samples not found: {post_samples_path}")
        print(f"  Run inference first, then re-run this script.")
        return None

    post = evaluate_post_scd(post_samples_path, dataset)
    print(f"\n  Post-SCD ({post['n_instances']} instances):")
    print(f"    Greedy F1:       {post['greedy_f1']['mean']:.4f} "
          f"[{post['greedy_f1']['ci_lo']:.4f}, {post['greedy_f1']['ci_hi']:.4f}]")
    print(f"    Construction F1: {post['construction_f1']['mean']:.4f} "
          f"[{post['construction_f1']['ci_lo']:.4f}, {post['construction_f1']['ci_hi']:.4f}]")

    # Key comparison: post-greedy vs pre-construction
    # Load pre samples to get per-instance F1s for paired test
    pre_samples_path = PRE_SAMPLES_PATHS[dataset]
    if os.path.exists(pre_samples_path):
        pre_eval = evaluate_post_scd(pre_samples_path, dataset)
        test_result = paired_bootstrap_test(
            pre_eval["construction_f1_raw"], post["greedy_f1_raw"])
        print(f"\n  Key claim: post-greedy >= pre-construction")
        print(f"    Delta: {test_result['delta']:+.4f}")
        print(f"    p-value: {test_result['p_value']:.4f}")
        if test_result["delta"] > 0:
            print(f"    CLAIM SUPPORTED" if test_result["p_value"] < 0.05
                  else f"    Positive but not significant (p={test_result['p_value']:.3f})")
        else:
            print(f"    CLAIM NOT SUPPORTED (post-greedy < pre-construction)")

    # Deltas
    print(f"\n  Deltas:")
    print(f"    Greedy improvement:       "
          f"{post['greedy_f1']['mean'] - pre['greedy_f1']['mean']:+.4f}")
    print(f"    Construction improvement: "
          f"{post['construction_f1']['mean'] - pre['construction_f1']['mean']:+.4f}")

    return {
        "dataset": dataset,
        "pre_greedy_f1": pre["greedy_f1"]["mean"],
        "pre_construction_f1": pre["construction_f1"]["mean"],
        "post_greedy_f1": post["greedy_f1"]["mean"],
        "post_construction_f1": post["construction_f1"]["mean"],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True, choices=["fewnerd", "scierc", "conll"])
    parser.add_argument("--post-samples", required=True,
                        help="Path to post-SCD samples.jsonl (N=8 + greedy)")
    parser.add_argument("--output", default=None, help="Output JSON path")
    args = parser.parse_args()

    result = run_comparison(args.dataset, args.post_samples)

    if result and args.output:
        with open(args.output, "w") as f:
            json.dump(result, f, indent=2)
        print(f"\nSaved: {args.output}")


if __name__ == "__main__":
    main()

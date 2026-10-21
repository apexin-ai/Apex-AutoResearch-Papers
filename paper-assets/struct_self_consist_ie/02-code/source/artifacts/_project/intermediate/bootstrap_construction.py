#!/usr/bin/env python3
"""Paired bootstrap test: greedy F1 vs LP-weighted construction F1.

Replicates the methodology from the 72B ZS SciERC bootstrap analysis:
- B=10000 bootstrap iterations
- 95% CI on the paired difference
- One-sided p-value (H0: construction <= greedy)
- Cohen's d effect size
- Degeneracy-stratified breakdown

Usage:
    # Single dataset
    python bootstrap_construction.py \
        --input-dir /path/to/output/72b_zeroshot --dataset scierc

    # All datasets under a model directory
    python bootstrap_construction.py \
        --input-dir /path/to/output/72b_zeroshot

    # Use pre-computed per-instance data (from compute_signals.py)
    python bootstrap_construction.py \
        --per-instance /path/to/scierc_per_instance.json --dataset scierc
"""

import argparse
import json
import os
import statistics
import sys
from collections import Counter, defaultdict

import numpy as np

B = 10000
SEED = 42


# ---------------------------------------------------------------------------
# Core metrics (self-contained, no external imports needed)
# ---------------------------------------------------------------------------

def compute_entity_f1(pred_entities, gold_entities):
    pred = {(e["start"], e["end"], e["type"]) for e in pred_entities}
    gold = {(e["start"], e["end"], e["type"]) for e in gold_entities}
    if not gold and not pred:
        return 1.0
    if not gold or not pred:
        return 0.0
    tp = len(pred & gold)
    if tp == 0:
        return 0.0
    p = tp / len(pred)
    r = tp / len(gold)
    return 2 * p * r / (p + r)


def consensus_construct(inst, high_thresh=0.5, medium_thresh=0.25):
    """LP-weighted entity construction (same as compute_signals.py)."""
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
        lp = s.get("mean_logprob")
        if lp is None and "logprobs" in inst and i < len(inst["logprobs"]):
            lp = inst["logprobs"][i]
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
                lp = samples[i].get("mean_logprob")
                if lp is None and "logprobs" in inst and i < len(inst["logprobs"]):
                    lp = inst["logprobs"][i]
                if lp is not None:
                    contributing_lps.append(lp)
            if contributing_lps:
                mean_lp = statistics.mean(contributing_lps)
                if mean_lp > instance_median_lp:
                    consensus.append(entity_key)

    return [{"start": s, "end": e, "type": t} for s, e, t in consensus]


def is_degenerate(inst):
    """All samples produce identical entity sets."""
    key_sets = set()
    for s in inst["samples"]:
        ks = frozenset((e["start"], e["end"], e["type"])
                       for e in s.get("entities", []))
        key_sets.add(ks)
    return len(key_sets) == 1


def load_data(path, gold_filter=True):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if gold_filter and not obj["gold"].get("entities", []):
                continue
            instances.append(obj)
    return instances


# ---------------------------------------------------------------------------
# Bootstrap test
# ---------------------------------------------------------------------------

def run_bootstrap(greedy_f1s, construction_f1s, degen_flags, label=""):
    """Paired bootstrap test with degeneracy stratification."""
    rng = np.random.RandomState(SEED)
    n = len(greedy_f1s)

    greedy_arr = np.array(greedy_f1s)
    construction_arr = np.array(construction_f1s)
    degen_arr = np.array(degen_flags, dtype=bool)
    diffs = construction_arr - greedy_arr

    obs_diff = float(diffs.mean())

    boot_diffs = np.zeros(B)
    for b in range(B):
        idx = rng.randint(0, n, n)
        boot_diffs[b] = diffs[idx].mean()
    boot_diffs.sort()

    ci_lo = float(boot_diffs[int(0.025 * B)])
    ci_hi = float(boot_diffs[int(0.975 * B)])
    p_value = float(np.mean(boot_diffs <= 0))

    std_diff = float(diffs.std(ddof=1))
    cohens_d = obs_diff / std_diff if std_diff > 0 else float("inf")

    n_positive = int(np.sum(diffs > 0))
    n_negative = int(np.sum(diffs < 0))
    n_tied = int(np.sum(diffs == 0))
    n_degen = int(degen_arr.sum())
    n_nondegen = n - n_degen

    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"{'='*60}")
    print(f"Instances: {n}, Samples/instance: N/A (from per-instance data)")
    print(f"\nGreedy F1:       {greedy_arr.mean():.4f}")
    print(f"Construction F1: {construction_arr.mean():.4f}")
    print(f"Observed diff:   {obs_diff:+.4f} ({obs_diff*100:+.2f}pp)")

    print(f"\n=== Paired Bootstrap Test (B={B}) ===")
    print(f"95% CI of diff:  [{ci_lo:+.4f}, {ci_hi:+.4f}]")
    print(f"p-value (one-sided, H0: diff<=0): {p_value:.4f}")
    print(f"Cohen's d:       {cohens_d:.4f}")
    print(f"Significant (p<0.05): {'YES' if p_value < 0.05 else 'NO'}")

    print(f"\n=== Instance Distribution ===")
    print(f"Positive (construction > greedy): {n_positive} ({n_positive/n*100:.1f}%)")
    print(f"Negative (construction < greedy): {n_negative} ({n_negative/n*100:.1f}%)")
    print(f"Tied:                             {n_tied} ({n_tied/n*100:.1f}%)")

    print(f"\n=== Degeneracy ===")
    print(f"Degenerate instances: {n_degen} ({n_degen/n*100:.1f}%)")
    print(f"Non-degenerate:       {n_nondegen} ({n_nondegen/n*100:.1f}%)")

    result = {
        "test": "paired_bootstrap",
        "label": label,
        "n_instances": n,
        "B": B,
        "greedy_f1": float(greedy_arr.mean()),
        "construction_f1": float(construction_arr.mean()),
        "observed_diff": obs_diff,
        "ci_95": [ci_lo, ci_hi],
        "p_value": p_value,
        "cohens_d": cohens_d,
        "instance_positive": n_positive,
        "instance_negative": n_negative,
        "instance_tied": n_tied,
        "n_degenerate": n_degen,
        "n_nondegenerate": n_nondegen,
    }

    if n_nondegen > 0:
        nd_mask = ~degen_arr
        nd_greedy = float(greedy_arr[nd_mask].mean())
        nd_construction = float(construction_arr[nd_mask].mean())
        nd_diff = nd_construction - nd_greedy
        nd_diffs = diffs[nd_mask]
        nd_n = nd_diffs.shape[0]

        nd_boot = np.zeros(B)
        for b in range(B):
            idx = rng.randint(0, nd_n, nd_n)
            nd_boot[b] = nd_diffs[idx].mean()
        nd_boot.sort()
        nd_ci_lo = float(nd_boot[int(0.025 * B)])
        nd_ci_hi = float(nd_boot[int(0.975 * B)])
        nd_p = float(np.mean(nd_boot <= 0))

        nd_pos = int(np.sum(nd_diffs > 0))
        nd_neg = int(np.sum(nd_diffs < 0))
        nd_tie = int(np.sum(nd_diffs == 0))

        print(f"\n  Non-degen greedy F1:       {nd_greedy:.4f}")
        print(f"  Non-degen construction F1: {nd_construction:.4f}")
        print(f"  Non-degen diff:            {nd_diff:+.4f} ({nd_diff*100:+.2f}pp)")
        print(f"  Non-degen 95% CI:          [{nd_ci_lo:+.4f}, {nd_ci_hi:+.4f}]")
        print(f"  Non-degen p-value:         {nd_p:.4f}")
        print(f"  Non-degen positive/negative/tied: {nd_pos}/{nd_neg}/{nd_tie}")

        result.update({
            "nondegen_greedy_f1": nd_greedy,
            "nondegen_construction_f1": nd_construction,
            "nondegen_diff": nd_diff,
            "nondegen_ci_95": [nd_ci_lo, nd_ci_hi],
            "nondegen_p_value": nd_p,
        })

    if n_degen > 0:
        d_mask = degen_arr
        d_greedy = float(greedy_arr[d_mask].mean())
        d_construction = float(construction_arr[d_mask].mean())
        d_diff = d_construction - d_greedy
        print(f"\n  Degen greedy F1:       {d_greedy:.4f}")
        print(f"  Degen construction F1: {d_construction:.4f}")
        print(f"  Degen diff:            {d_diff:+.4f}")

    return result


# ---------------------------------------------------------------------------
# Entry points
# ---------------------------------------------------------------------------

def run_from_samples(path, dataset_name):
    """Compute per-instance F1s from samples.jsonl and run bootstrap."""
    instances = load_data(path, gold_filter=True)
    n = len(instances)
    N_samples = len(instances[0]["samples"])
    theta = 2 / N_samples

    print(f"Loaded {n} instances, {N_samples} samples/instance, theta=2/N={theta:.4f}")

    greedy_f1s = []
    construction_f1s = []
    degen_flags = []

    for inst in instances:
        gold_ents = inst["gold"]["entities"]
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1s.append(compute_entity_f1(
            greedy.get("entities", []), gold_ents))
        construction_f1s.append(compute_entity_f1(
            consensus_construct(inst, high_thresh=0.5, medium_thresh=theta),
            gold_ents))
        degen_flags.append(is_degenerate(inst))

    return run_bootstrap(greedy_f1s, construction_f1s, degen_flags,
                         label=dataset_name)


def run_from_per_instance(path, dataset_name):
    """Load pre-computed per-instance data and run bootstrap."""
    with open(path) as f:
        data = json.load(f)
    return run_bootstrap(
        data["greedy_f1"],
        data["construction_lp_f1"],
        data["degenerate"],
        label=dataset_name,
    )


def find_datasets(input_dir):
    datasets = {}
    for name in ["scierc", "conll2003", "fewnerd"]:
        path = os.path.join(input_dir, name, "samples.jsonl")
        if os.path.exists(path):
            datasets[name] = path
    top_path = os.path.join(input_dir, "samples.jsonl")
    if os.path.exists(top_path) and not datasets:
        ds_name = os.path.basename(input_dir)
        for known in ["scierc", "conll", "fewnerd"]:
            if known in ds_name.lower():
                ds_name = known
                break
        datasets[ds_name] = top_path
    return datasets


def main():
    parser = argparse.ArgumentParser(
        description="Paired bootstrap test: greedy vs LP-weighted construction")
    parser.add_argument("--input-dir", default=None,
                        help="Model output directory (with samples.jsonl)")
    parser.add_argument("--per-instance", default=None,
                        help="Pre-computed per-instance JSON "
                             "(from compute_signals.py)")
    parser.add_argument("--dataset", default=None, nargs="+",
                        help="Dataset(s) to process")
    parser.add_argument("--output-dir", default=None,
                        help="Output directory for result JSON")
    args = parser.parse_args()

    if not args.input_dir and not args.per_instance:
        parser.error("Must specify --input-dir or --per-instance")

    all_results = {}

    if args.per_instance:
        ds_name = args.dataset[0] if args.dataset else "unknown"
        result = run_from_per_instance(args.per_instance, ds_name)
        all_results[ds_name] = result
    else:
        datasets = find_datasets(args.input_dir)
        if args.dataset:
            datasets = {k: v for k, v in datasets.items()
                        if k in args.dataset}
        if not datasets:
            print(f"ERROR: No samples.jsonl found under {args.input_dir}")
            sys.exit(1)

        for ds_name, path in sorted(datasets.items()):
            result = run_from_samples(path, ds_name)
            all_results[ds_name] = result

    # Save results
    out_dir = args.output_dir or args.input_dir or os.path.dirname(
        args.per_instance)
    os.makedirs(out_dir, exist_ok=True)

    for ds_name, result in all_results.items():
        out_path = os.path.join(out_dir,
                                f"{ds_name}_paired_bootstrap_result.json")
        with open(out_path, "w") as f:
            json.dump(result, f, indent=2)
        print(f"\nResult saved to {out_path}")


if __name__ == "__main__":
    main()

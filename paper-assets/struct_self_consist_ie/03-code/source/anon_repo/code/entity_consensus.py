#!/usr/bin/env python3
"""Entity Consensus Construction evaluation.

Constructs consensus entity sets from N samples using frequency-based
thresholds with LP-weighted decisions for medium-confidence entities.
Evaluates against gold using span-based (start, end, type) F1.
"""

import json
import os
import sys
import statistics
from collections import Counter, defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unified_metrics import compute_entity_f1, compute_degeneracy

BASE = "/root/autodl-tmp/struct_self_consist_ie"

DATASETS = {
    "SciERC": {
        "path": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
        "gold_filter": True,
    },
    "CoNLL": {
        "path": f"{BASE}/output/exp_002_conll_n16_r1024/samples.jsonl",
        "gold_filter": True,
    },
    "FewNERD": {
        "path": f"{BASE}/output/exp_027_fewnerd_n16/samples.jsonl",
        "gold_filter": True,
    },
}

THRESHOLDS = [
    {"high": 0.5, "medium": 0.1},
    {"high": 0.6, "medium": 0.2},
    {"high": 0.7, "medium": 0.3},
    {"high": 0.8, "medium": 0.4},
]


def load_data(path, gold_filter=True):
    instances = []
    with open(path) as f:
        for line in f:
            obj = json.loads(line)
            if gold_filter and len(obj["gold"]["entities"]) == 0:
                continue
            instances.append(obj)
    return instances




def get_sample_mean_logprob(sample, inst, idx):
    if "mean_logprob" in sample:
        return sample["mean_logprob"]
    if "logprobs" in inst and idx < len(inst["logprobs"]):
        return inst["logprobs"][idx]
    return None


def consensus_construct(inst, high_thresh=0.7, medium_thresh=0.3):
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
                mean_lp = statistics.mean(contributing_lps)
                if mean_lp > instance_median_lp:
                    consensus.append(entity_key)

    return [{"start": s, "end": e, "type": t} for s, e, t in consensus]


def majority_vote_span(inst, threshold=0.5):
    samples = inst["samples"]
    N = len(samples)
    entity_counts = Counter()
    for s in samples:
        seen = set()
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_counts[key] += 1
                seen.add(key)
    result = []
    for key, count in entity_counts.items():
        if count / N > threshold:
            result.append({"start": key[0], "end": key[1], "type": key[2]})
    return result


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


def evaluate_dataset(name, cfg, thresholds, n_bootstrap=2000, dry_run=False):
    instances = load_data(cfg["path"], cfg["gold_filter"])
    if dry_run:
        instances = instances[:20]
    n_inst = len(instances)
    N_samples = len(instances[0]["samples"]) if instances else 0

    results = {"name": name, "n_instances": n_inst, "n_samples": N_samples}

    greedy_f1s, lp_f1s, oracle_f1s, mv_f1s = [], [], [], []

    for inst in instances:
        gold_ents = inst["gold"]["entities"]
        samples = inst["samples"]

        greedy_f1s.append(compute_entity_f1(inst["greedy"]["entities"], gold_ents))

        best_lp_idx = 0
        best_lp = float("-inf")
        for i, s in enumerate(samples):
            lp = get_sample_mean_logprob(s, inst, i)
            if lp is not None and lp > best_lp:
                best_lp = lp
                best_lp_idx = i
        lp_f1s.append(compute_entity_f1(samples[best_lp_idx]["entities"], gold_ents))

        sample_f1s = [compute_entity_f1(s["entities"], gold_ents) for s in samples]
        oracle_f1s.append(max(sample_f1s))

        mv_ents = majority_vote_span(inst, threshold=0.5)
        mv_f1s.append(compute_entity_f1(mv_ents, gold_ents))

    results["baselines"] = {
        "greedy": bootstrap_ci(greedy_f1s, n_bootstrap),
        "lp_selection": bootstrap_ci(lp_f1s, n_bootstrap),
        "majority_vote": bootstrap_ci(mv_f1s, n_bootstrap),
        "oracle": bootstrap_ci(oracle_f1s, n_bootstrap),
    }

    results["consensus"] = {}
    for thresh_cfg in thresholds:
        high = thresh_cfg["high"]
        medium = thresh_cfg["medium"]
        key = f"high={high}_medium={medium}"

        consensus_f1s = []
        for inst in instances:
            gold_ents = inst["gold"]["entities"]
            c_ents = consensus_construct(inst, high_thresh=high, medium_thresh=medium)
            consensus_f1s.append(compute_entity_f1(c_ents, gold_ents))

        results["consensus"][key] = bootstrap_ci(consensus_f1s, n_bootstrap)

    return results


def print_results(result):
    print(f"  Instances: {result['n_instances']} (N={result['n_samples']})")
    b = result["baselines"]
    for label, key in [("Greedy", "greedy"), ("LP Selection", "lp_selection"),
                       ("Majority Vote", "majority_vote"), ("Oracle", "oracle")]:
        ci = b[key]
        print(f"  {label:20s} {ci['mean']:.4f}  [{ci['ci_lo']:.4f}, {ci['ci_hi']:.4f}]")
    for thresh_key, ci in result["consensus"].items():
        print(f"  Consensus({thresh_key}): {ci['mean']:.4f}  [{ci['ci_lo']:.4f}, {ci['ci_hi']:.4f}]")


def generate_markdown(all_results):
    lines = ["# Entity Consensus Construction Results\n"]
    for name, r in all_results.items():
        lines.append(f"## {name} (N={r['n_samples']}, {r['n_instances']} instances)\n")
        lines.append("### Baselines\n")
        lines.append("| Method | F1 | 95% CI |")
        lines.append("|--------|-----|--------|")
        for label, key in [("Greedy", "greedy"), ("LP Selection", "lp_selection"),
                           ("Majority Vote (span)", "majority_vote"), ("Oracle", "oracle")]:
            ci = r["baselines"][key]
            lines.append(f"| {label} | {ci['mean']:.4f} | [{ci['ci_lo']:.4f}, {ci['ci_hi']:.4f}] |")
        lines.append("")
        lines.append("### Consensus Construction (Threshold Sensitivity)\n")
        lines.append("| High Thresh | Medium Thresh | F1 | 95% CI |")
        lines.append("|-------------|---------------|-----|--------|")
        for thresh_key, ci in r["consensus"].items():
            h, m = thresh_key.replace("high=", "").replace("medium=", "").split("_")
            lines.append(f"| {h} | {m} | {ci['mean']:.4f} | [{ci['ci_lo']:.4f}, {ci['ci_hi']:.4f}] |")
        lines.append("")
    return "\n".join(lines)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--n-bootstrap", type=int, default=2000)
    args = parser.parse_args()

    all_results = {}
    for name, cfg in DATASETS.items():
        print(f"\nProcessing {name}...")
        r = evaluate_dataset(name, cfg, THRESHOLDS, args.n_bootstrap, dry_run=args.dry_run)
        all_results[name] = r
        print_results(r)

    out_path = f"{BASE}/output/entity_consensus_results.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nJSON saved to {out_path}")

    md = generate_markdown(all_results)
    md_path = f"{BASE}/output/entity_consensus_report.md"
    with open(md_path, "w") as f:
        f.write(md)
    print(f"Report saved to {md_path}")


if __name__ == "__main__":
    main()

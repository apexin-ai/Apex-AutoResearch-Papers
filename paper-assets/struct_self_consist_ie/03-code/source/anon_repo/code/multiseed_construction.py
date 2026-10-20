"""Multi-seed entity construction evaluation.

For SciERC (3 seeds) and FewNERD (4 seeds), N=8:
- Greedy F1
- Uniform construction (theta=2/N=0.25)
- LP-weighted construction (theta=2/N=0.25)
- Delta vs greedy
- Mean +/- sigma across seeds
"""
import json
import math
import os
import sys
import numpy as np
from collections import defaultdict

BASE = "/root/autodl-tmp/struct_self_consist_ie"

SEED_FILES = {
    "scierc": {
        42: f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
        123: f"{BASE}/output/exp_018_qwen_scierc_seed123/samples.jsonl",
        456: f"{BASE}/output/exp_018_qwen_scierc_seed456/samples.jsonl",
    },
    "fewnerd": {
        42: f"{BASE}/output/exp_021_inference/samples.jsonl",
        123: f"{BASE}/output/exp_021_fewnerd_n8_seed123/samples.jsonl",
        456: f"{BASE}/output/exp_021_fewnerd_n8_seed456/samples.jsonl",
        789: f"{BASE}/output/fewnerd_seed789_merged/samples.jsonl",
    },
}

OUTPUT_DIR = f"{BASE}/output/entity_construction_fair_n8"

def compute_prf(pred_set, gold_set):
    if not gold_set and not pred_set:
        return 1.0, 1.0, 1.0
    if not pred_set:
        return 0.0, 0.0, 0.0
    if not gold_set:
        return 0.0, 0.0, 0.0
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0, 0.0, 0.0
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    f = 2 * p * r / (p + r)
    return p, r, f

def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}

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

def get_lp_weights(inst):
    samples = inst["samples"]
    logprobs = inst.get("logprobs", None)
    lps = []
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob", None)
        if lp is None and logprobs is not None and i < len(logprobs):
            lp = logprobs[i]
        if lp is None or not math.isfinite(lp):
            lp = -100.0
        lps.append(lp)
    max_lp = max(lps)
    ws = [math.exp(lp - max_lp) for lp in lps]
    total = sum(ws)
    return [w / total for w in ws]

def entity_majority_vote(samples, threshold, weights=None):
    entity_counts = defaultdict(float)
    N = len(samples)
    for i, sample in enumerate(samples):
        w = weights[i] if weights is not None else 1.0
        for e in sample.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            entity_counts[key] += w
    total_weight = sum(weights) if weights is not None else N
    constructed = set()
    for key, count in entity_counts.items():
        if count / total_weight >= threshold:
            constructed.add(key)
    return constructed

def evaluate_seed(data, n_samples):
    theta = 2.0 / n_samples  # 0.25 for N=8

    greedy_f1s = []
    uniform_f1s = []
    lp_weighted_f1s = []

    for inst in data:
        gold = entity_set(inst["gold"]["entities"])

        # Greedy
        greedy = inst.get("greedy", inst["samples"][0])
        pred_greedy = entity_set(greedy.get("entities", []))
        _, _, f_greedy = compute_prf(pred_greedy, gold)
        greedy_f1s.append(f_greedy)

        # Uniform construction
        pred_uniform = entity_majority_vote(inst["samples"], theta)
        _, _, f_uniform = compute_prf(pred_uniform, gold)
        uniform_f1s.append(f_uniform)

        # LP-weighted construction
        ws = get_lp_weights(inst)
        pred_lp = entity_majority_vote(inst["samples"], theta, weights=ws)
        _, _, f_lp = compute_prf(pred_lp, gold)
        lp_weighted_f1s.append(f_lp)

    greedy_f1s = np.array(greedy_f1s)
    uniform_f1s = np.array(uniform_f1s)
    lp_weighted_f1s = np.array(lp_weighted_f1s)

    return {
        "n_instances": len(data),
        "n_samples": n_samples,
        "theta": theta,
        "greedy_f1": float(greedy_f1s.mean()),
        "uniform_construction_f1": float(uniform_f1s.mean()),
        "lp_weighted_construction_f1": float(lp_weighted_f1s.mean()),
        "delta_uniform": float((uniform_f1s - greedy_f1s).mean()),
        "delta_lp_weighted": float((lp_weighted_f1s - greedy_f1s).mean()),
    }

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    results = {}

    for dataset_name, seeds in SEED_FILES.items():
        print(f"\n{'='*60}")
        print(f"Dataset: {dataset_name}")
        print(f"{'='*60}")

        seed_results = {}
        greedy_list = []
        uniform_list = []
        lp_list = []
        delta_uniform_list = []
        delta_lp_list = []

        for seed, path in sorted(seeds.items()):
            if not os.path.exists(path):
                print(f"  SKIP seed {seed}: {path} not found")
                continue

            print(f"\n  Seed {seed}: {path}")
            data = load_data(path, gold_filter=True)
            n_samples = len(data[0]["samples"])
            print(f"    Instances: {len(data)}, N={n_samples}")

            sr = evaluate_seed(data, n_samples)
            seed_results[seed] = sr

            greedy_list.append(sr["greedy_f1"])
            uniform_list.append(sr["uniform_construction_f1"])
            lp_list.append(sr["lp_weighted_construction_f1"])
            delta_uniform_list.append(sr["delta_uniform"])
            delta_lp_list.append(sr["delta_lp_weighted"])

            print(f"    Greedy F1:           {sr['greedy_f1']*100:.2f}")
            print(f"    Uniform (θ=0.25):    {sr['uniform_construction_f1']*100:.2f}  Δ={sr['delta_uniform']*100:+.2f}pp")
            print(f"    LP-weighted (θ=0.25):{sr['lp_weighted_construction_f1']*100:.2f}  Δ={sr['delta_lp_weighted']*100:+.2f}pp")

        n_seeds = len(seed_results)
        if n_seeds < 2:
            print(f"\n  Only {n_seeds} seed(s), skip aggregation.")
            results[dataset_name] = {"per_seed": {str(k): v for k, v in seed_results.items()}}
            continue

        summary = {
            "n_seeds": n_seeds,
            "greedy_f1_mean": float(np.mean(greedy_list)),
            "greedy_f1_std": float(np.std(greedy_list, ddof=0)),
            "uniform_f1_mean": float(np.mean(uniform_list)),
            "uniform_f1_std": float(np.std(uniform_list, ddof=0)),
            "lp_weighted_f1_mean": float(np.mean(lp_list)),
            "lp_weighted_f1_std": float(np.std(lp_list, ddof=0)),
            "delta_uniform_mean": float(np.mean(delta_uniform_list)),
            "delta_uniform_std": float(np.std(delta_uniform_list, ddof=0)),
            "delta_lp_mean": float(np.mean(delta_lp_list)),
            "delta_lp_std": float(np.std(delta_lp_list, ddof=0)),
        }

        print(f"\n  === Summary ({n_seeds} seeds) ===")
        print(f"  Greedy F1:           {summary['greedy_f1_mean']*100:.2f} ± {summary['greedy_f1_std']*100:.2f}")
        print(f"  Uniform (θ=0.25):    {summary['uniform_f1_mean']*100:.2f} ± {summary['uniform_f1_std']*100:.2f}")
        print(f"  LP-weighted (θ=0.25):{summary['lp_weighted_f1_mean']*100:.2f} ± {summary['lp_weighted_f1_std']*100:.2f}")
        print(f"  Δ Uniform:           {summary['delta_uniform_mean']*100:+.2f} ± {summary['delta_uniform_std']*100:.2f}pp")
        print(f"  Δ LP-weighted:       {summary['delta_lp_mean']*100:+.2f} ± {summary['delta_lp_std']*100:.2f}pp")

        results[dataset_name] = {
            "per_seed": {str(k): v for k, v in seed_results.items()},
            "summary": summary,
        }

    out_path = os.path.join(OUTPUT_DIR, "multiseed_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {out_path}")

if __name__ == "__main__":
    main()

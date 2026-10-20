#!/usr/bin/env python3
"""Compute VC-weighted and SJ-weighted construction variants."""

import json
import math
import os
import sys
import numpy as np
from collections import defaultdict, Counter

BASE = "/root/autodl-tmp/struct_self_consist_ie"

SEED_FILES = {
    "fewnerd": {
        42: f"{BASE}/output/llama_fewnerd_s42/samples.jsonl",
        123: f"{BASE}/output/llama_fewnerd_s123/samples.jsonl",
        456: f"{BASE}/output/llama_fewnerd_s456/samples.jsonl",
    },
    "scierc": {
        42: f"{BASE}/output/exp_018_llama_scierc_seed42_r1024/samples.jsonl",
        123: f"{BASE}/output/exp_018_llama_scierc_seed123/samples.jsonl",
        456: f"{BASE}/output/exp_018_llama_scierc_seed456/samples.jsonl",
    },
}

OUTPUT_DIR = f"{BASE}/output/construction_variants"


def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}


def compute_f1(pred_set, gold_set):
    if not gold_set and not pred_set:
        return 1.0
    if not pred_set or not gold_set:
        return 0.0
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    return 2 * p * r / (p + r)


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


def get_vc_weights(inst):
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
    weights = []
    for s in samples:
        ents = set()
        for e in s.get("entities", []):
            ents.add((e["start"], e["end"], e["type"]))
        if ents:
            w = sum(entity_counts[k] for k in ents) / (N * len(ents))
        else:
            w = 1.0 / N
        weights.append(w)
    total = sum(weights)
    if total == 0:
        return [1.0 / N] * N
    return [w / total for w in weights]


def get_sj_weights(inst):
    samples = inst["samples"]
    N = len(samples)
    sets = []
    for s in samples:
        es = frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
        sets.append(es)

    weights = []
    for i in range(N):
        if N == 1:
            weights.append(1.0)
            continue
        total_j = 0.0
        for j in range(N):
            if j == i:
                continue
            a, b = sets[i], sets[j]
            if not a and not b:
                total_j += 1.0
            elif not a or not b:
                pass
            else:
                total_j += len(a & b) / len(a | b)
        weights.append(total_j / (N - 1))
    total = sum(weights)
    if total == 0:
        return [1.0 / N] * N
    return [w / total for w in weights]


def weighted_construction(samples, threshold, weights=None):
    entity_counts = defaultdict(float)
    N = len(samples)
    for i, sample in enumerate(samples):
        w = weights[i] if weights is not None else 1.0
        seen = set()
        for e in sample.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_counts[key] += w
                seen.add(key)
    total_weight = sum(weights) if weights is not None else N
    constructed = set()
    for key, count in entity_counts.items():
        if count / total_weight >= threshold:
            constructed.add(key)
    return constructed


def paired_bootstrap_test_vectorized(f1s_a, f1s_b, n_boot=10000, seed=42):
    a = np.array(f1s_a, dtype=np.float64)
    b = np.array(f1s_b, dtype=np.float64)
    n = len(a)
    diff = b - a
    observed = float(diff.mean())
    rng = np.random.RandomState(seed)
    idx = rng.randint(0, n, size=(n_boot, n))
    boot_diffs = diff[idx].mean(axis=1)
    p_value = float(np.mean(boot_diffs <= 0))
    return observed, p_value


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


def evaluate_seed(data):
    N = len(data[0]["samples"])
    theta = 2.0 / N
    greedy_f1s, lp_f1s, vc_f1s, sj_f1s = [], [], [], []
    total = len(data)

    for idx, inst in enumerate(data):
        if idx % 5000 == 0:
            print(f"    Processing {idx}/{total}...", flush=True)

        gold = entity_set(inst["gold"]["entities"])
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1s.append(compute_f1(entity_set(greedy.get("entities", [])), gold))

        lp_ws = get_lp_weights(inst)
        lp_pred = weighted_construction(inst["samples"], theta, weights=lp_ws)
        lp_f1s.append(compute_f1(lp_pred, gold))

        vc_ws = get_vc_weights(inst)
        vc_pred = weighted_construction(inst["samples"], theta, weights=vc_ws)
        vc_f1s.append(compute_f1(vc_pred, gold))

        sj_ws = get_sj_weights(inst)
        sj_pred = weighted_construction(inst["samples"], theta, weights=sj_ws)
        sj_f1s.append(compute_f1(sj_pred, gold))

    return {"greedy": greedy_f1s, "lp_weighted": lp_f1s, "vc_weighted": vc_f1s, "sj_weighted": sj_f1s}


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_results = {}

    for dataset_name, seeds in SEED_FILES.items():
        print(f"\n{'='*60}", flush=True)
        print(f"  {dataset_name}", flush=True)
        print(f"{'='*60}", flush=True)

        seed_results = {}
        for seed, path in sorted(seeds.items()):
            if not os.path.exists(path):
                print(f"  SKIP seed {seed}: {path} not found", flush=True)
                continue
            data = load_data(path, gold_filter=True)
            print(f"  Seed {seed}: {len(data)} instances, N={len(data[0]['samples'])}", flush=True)
            seed_results[seed] = evaluate_seed(data)
            print(f"  Seed {seed} done.", flush=True)

        if len(seed_results) < 1:
            continue

        methods = ["greedy", "lp_weighted", "vc_weighted", "sj_weighted"]
        seed_means = {m: [] for m in methods}
        for seed, sr in sorted(seed_results.items()):
            for m in methods:
                seed_means[m].append(float(np.mean(sr[m])))

        pooled = {m: [] for m in methods}
        for seed, sr in sorted(seed_results.items()):
            for m in methods:
                pooled[m].extend(sr[m])

        result = {
            "dataset": dataset_name,
            "n_seeds": len(seed_results),
            "seeds": sorted(seed_results.keys()),
        }

        for m in methods:
            result[f"{m}_f1"] = float(np.mean(seed_means[m]))
            if len(seed_means[m]) > 1:
                result[f"{m}_f1_std"] = float(np.std(seed_means[m], ddof=0))

        for m in ["lp_weighted", "vc_weighted", "sj_weighted"]:
            result[f"{m.replace('_weighted','')}_delta"] = result[f"{m}_f1"] - result["greedy_f1"]

        print(f"\n  Running bootstrap tests (B=10000)...", flush=True)
        for m in ["lp_weighted", "vc_weighted", "sj_weighted"]:
            diff, p = paired_bootstrap_test_vectorized(pooled["greedy"], pooled[m], n_boot=10000)
            short = m.replace("_weighted", "")
            result[f"{short}_p"] = float(p)
            result[f"{short}_bootstrap_diff"] = float(diff)

        result["per_seed"] = {}
        for seed in sorted(seed_results.keys()):
            sr = seed_results[seed]
            result["per_seed"][str(seed)] = {m: float(np.mean(sr[m])) for m in methods}

        all_results[dataset_name] = result

        print(f"\n  {'Method':<25} {'F1':>8} {'delta':>8} {'p-value':>10}", flush=True)
        print(f"  {'-'*55}", flush=True)
        print(f"  {'Greedy':<25} {result['greedy_f1']*100:>7.2f}", flush=True)
        for m, short in [("lp_weighted", "lp"), ("vc_weighted", "vc"), ("sj_weighted", "sj")]:
            f1 = result[f"{m}_f1"]
            delta = result[f"{short}_delta"]
            p = result[f"{short}_p"]
            sig = "*" if p < 0.05 else ""
            print(f"  {m:<25} {f1*100:>7.2f} {delta*100:>+7.2f}pp {p:>9.4f} {sig}", flush=True)

        print(f"\n  Per-seed F1:", flush=True)
        for seed in sorted(seed_results.keys()):
            sr = seed_results[seed]
            vals = " | ".join(f"{np.mean(sr[m])*100:.2f}" for m in methods)
            print(f"    seed {seed}: {vals}", flush=True)

    out_path = os.path.join(OUTPUT_DIR, "construction_variants_results.json")
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to: {out_path}", flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()

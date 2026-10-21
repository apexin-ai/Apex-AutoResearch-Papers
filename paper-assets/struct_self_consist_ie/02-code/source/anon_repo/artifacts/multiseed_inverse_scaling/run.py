#!/usr/bin/env python3
"""Multi-seed inverse scaling analysis for FewNERD.

For each seed, sub-sample N samples to N=2,4,6,8 (or up to 16),
compute entity-level micro F1 for 6 construction methods + LP-best selection,
detect inverse scaling transitions, and run paired bootstrap tests.
"""

import json
import math
import os
import sys
import time
import numpy as np
from collections import defaultdict, Counter

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUTPUT_DIR = f"{BASE}/artifacts/multiseed_inverse_scaling"

CONFIGS = {
    "Qwen_FewNERD_s42_n8": {
        "path": f"{BASE}/output/fewnerd_mf4v2_seed42_v3/samples.jsonl",
        "model": "Qwen3-8B-FT", "dataset": "FewNERD", "seed": 42, "max_n": 8,
    },
    "Qwen_FewNERD_s123_n8": {
        "path": f"{BASE}/output/fewnerd_mf4v2_seed123/samples.jsonl",
        "model": "Qwen3-8B-FT", "dataset": "FewNERD", "seed": 123, "max_n": 8,
    },
    "Qwen_FewNERD_s456_n8": {
        "path": f"{BASE}/output/fewnerd_mf4v2_seed456/samples.jsonl",
        "model": "Qwen3-8B-FT", "dataset": "FewNERD", "seed": 456, "max_n": 8,
    },
    "Qwen_FewNERD_s789_n8": {
        "path": f"{BASE}/output/fewnerd_seed789_merged/samples.jsonl",
        "model": "Qwen3-8B-FT", "dataset": "FewNERD", "seed": 789, "max_n": 8,
    },
    "Qwen_FewNERD_s42_n16": {
        "path": f"{BASE}/output/fewnerd_n16_s42/samples.jsonl",
        "model": "Qwen3-8B-FT", "dataset": "FewNERD", "seed": 42, "max_n": 16,
    },
    "Qwen_FewNERD_s456_n16": {
        "path": f"{BASE}/output/fewnerd_n16_s456/samples.jsonl",
        "model": "Qwen3-8B-FT", "dataset": "FewNERD", "seed": 456, "max_n": 16,
    },
    "LLaMA_FewNERD_s42_n8": {
        "path": f"{BASE}/output/llama_fewnerd_s42/samples.jsonl",
        "model": "LLaMA-3.1-8B-FT", "dataset": "FewNERD", "seed": 42, "max_n": 8,
    },
    "LLaMA_FewNERD_s123_n8": {
        "path": f"{BASE}/output/llama_fewnerd_s123/samples.jsonl",
        "model": "LLaMA-3.1-8B-FT", "dataset": "FewNERD", "seed": 123, "max_n": 8,
    },
    "LLaMA_FewNERD_s456_n8": {
        "path": f"{BASE}/output/llama_fewnerd_s456/samples.jsonl",
        "model": "LLaMA-3.1-8B-FT", "dataset": "FewNERD", "seed": 456, "max_n": 8,
    },
}

METHODS = ["majority_vote", "lp_best", "lp_weighted", "vc_weighted", "sj_weighted", "theta2n", "uniform"]

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

def get_lp_weights(samples, inst):
    logprobs_list = inst.get("logprobs", None)
    lps = []
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob", None)
        if lp is None and logprobs_list is not None and i < len(logprobs_list):
            lp = logprobs_list[i]
        if lp is None or not math.isfinite(lp):
            lp = -100.0
        lps.append(lp)
    max_lp = max(lps)
    ws = [math.exp(lp - max_lp) for lp in lps]
    total = sum(ws)
    if total == 0:
        return [1.0 / len(samples)] * len(samples)
    return [w / total for w in ws]

def get_vc_weights(samples):
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

def get_sj_weights(samples):
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

def evaluate_instance(inst, n, method):
    samples = inst["samples"][:n]
    gold = entity_set(inst["gold"]["entities"])

    if method == "majority_vote":
        pred = weighted_construction(samples, threshold=0.5)
    elif method == "lp_best":
        logprobs_list = inst.get("logprobs", None)
        lps = []
        for i, s in enumerate(samples):
            lp = s.get("mean_logprob", None)
            if lp is None and logprobs_list is not None and i < len(logprobs_list):
                lp = logprobs_list[i]
            if lp is None or not math.isfinite(lp):
                lp = -100.0
            lps.append(lp)
        best_idx = max(range(len(lps)), key=lambda i: lps[i])
        pred = entity_set(samples[best_idx].get("entities", []))
    elif method == "lp_weighted":
        ws = get_lp_weights(samples, inst)
        pred = weighted_construction(samples, threshold=2.0/n, weights=ws)
    elif method == "vc_weighted":
        ws = get_vc_weights(samples)
        pred = weighted_construction(samples, threshold=2.0/n, weights=ws)
    elif method == "sj_weighted":
        ws = get_sj_weights(samples)
        pred = weighted_construction(samples, threshold=2.0/n, weights=ws)
    elif method == "theta2n":
        pred = weighted_construction(samples, threshold=2.0/n)
    elif method == "uniform":
        pred = weighted_construction(samples, threshold=0.25)
    elif method == "greedy":
        pred = entity_set(inst["greedy"]["entities"])
    else:
        raise ValueError(f"Unknown: {method}")

    tp = len(pred & gold)
    fp = len(pred - gold)
    fn = len(gold - pred)
    return tp, fp, fn

def micro_f1_from_tuples(tuples):
    tp = sum(t[0] for t in tuples)
    fp = sum(t[1] for t in tuples)
    fn = sum(t[2] for t in tuples)
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)

def bootstrap_test(arr_n1, arr_n2, B=5000):
    n = len(arr_n1)
    assert n == len(arr_n2)
    a1 = np.array(arr_n1, dtype=np.int64)
    a2 = np.array(arr_n2, dtype=np.int64)
    s1 = a1.sum(axis=0)
    s2 = a2.sum(axis=0)

    def _f1(s):
        tp, fp, fn = s[0], s[1], s[2]
        if tp == 0: return 0.0
        p = tp / (tp + fp); r = tp / (tp + fn)
        return 2*p*r/(p+r)

    obs_diff = _f1(s2) - _f1(s1)
    rng = np.random.RandomState(42)
    diffs = np.empty(B)
    for b in range(B):
        idx = rng.randint(0, n, size=n)
        bs1 = a1[idx].sum(axis=0)
        bs2 = a2[idx].sum(axis=0)
        diffs[b] = _f1(bs2) - _f1(bs1)
    ci = (float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5)))
    p_value = float(np.mean(diffs >= 0))
    return {
        "obs_diff": float(obs_diff),
        "ci_95": ci,
        "p_value_inverse": p_value,
    }

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    all_results = {}

    for cfg_name, cfg in CONFIGS.items():
        path = cfg["path"]
        if not os.path.exists(path):
            print(f"SKIP {cfg_name}: {path} not found", flush=True)
            continue

        print(f"\n{'='*70}", flush=True)
        print(f"  {cfg_name}  (seed={cfg['seed']}, max_n={cfg['max_n']})", flush=True)
        print(f"{'='*70}", flush=True)

        t0 = time.time()
        instances = load_data(path, gold_filter=True)
        actual_n = len(instances[0]["samples"])
        max_n = min(cfg["max_n"], actual_n)
        print(f"  Loaded {len(instances)} gold-nonempty instances, N_max={max_n}", flush=True)

        n_vals = sorted(set(n for n in [2, 4, 6, 8, 16] if n <= max_n))

        greedy_tuples = [evaluate_instance(inst, max_n, "greedy") for inst in instances]
        greedy_f1 = micro_f1_from_tuples(greedy_tuples)
        print(f"  Greedy F1: {greedy_f1:.4f}", flush=True)

        precomputed = {}
        for method in METHODS:
            for n in n_vals:
                t1 = time.time()
                tuples = [evaluate_instance(inst, n, method) for inst in instances]
                f1 = micro_f1_from_tuples(tuples)
                precomputed[(method, n)] = {"tuples": tuples, "f1": f1}
                elapsed = time.time() - t1
                if elapsed > 5:
                    print(f"    {method} N={n}: F1={f1:.4f} ({elapsed:.1f}s)", flush=True)

        print(f"\n  {'Method':<18}", end="", flush=True)
        for n in n_vals:
            print(f"  N={n:>2}", end="", flush=True)
        print(flush=True)
        print(f"  {'-'*70}", flush=True)

        for method in METHODS:
            vals = "  ".join(f"{precomputed[(method, n)]['f1']:.4f}" for n in n_vals)
            print(f"  {method:<18} {vals}", flush=True)

        inverse_cases = []
        for method in METHODS:
            for i in range(len(n_vals) - 1):
                n1, n2 = n_vals[i], n_vals[i+1]
                f1_n1 = precomputed[(method, n1)]["f1"]
                f1_n2 = precomputed[(method, n2)]["f1"]
                drop = f1_n1 - f1_n2
                is_inverse = drop > 0.001

                bt = bootstrap_test(
                    precomputed[(method, n1)]["tuples"],
                    precomputed[(method, n2)]["tuples"],
                    B=5000,
                )

                case = {
                    "method": method, "n1": n1, "n2": n2,
                    "f1_n1": f1_n1, "f1_n2": f1_n2,
                    "delta_pp": (f1_n2 - f1_n1) * 100,
                    "is_inverse": is_inverse,
                    "obs_diff": bt["obs_diff"],
                    "ci_95": bt["ci_95"],
                    "p_value_inverse": bt["p_value_inverse"],
                    "sig_inverse": bt["ci_95"][1] < 0,
                    "sig_positive": bt["ci_95"][0] > 0,
                }
                inverse_cases.append(case)

        n_total = len(inverse_cases)
        n_inverse = sum(1 for c in inverse_cases if c["is_inverse"])
        n_sig_inverse = sum(1 for c in inverse_cases if c["sig_inverse"])
        n_positive = sum(1 for c in inverse_cases if not c["is_inverse"] and c["delta_pp"] > 0.1)
        n_sig_positive = sum(1 for c in inverse_cases if c["sig_positive"])

        print(f"\n  Transitions: {n_total} total", flush=True)
        print(f"  Inverse (F1 drops): {n_inverse}/{n_total} ({n_inverse/n_total*100:.0f}%)", flush=True)
        print(f"  Sig inverse (CI<0): {n_sig_inverse}/{n_total}", flush=True)
        print(f"  Sig positive (CI>0): {n_sig_positive}/{n_total}", flush=True)

        for c in inverse_cases:
            if c["sig_inverse"]:
                ci = c["ci_95"]
                print(f"    SIG INV: {c['method']:<18} N={c['n1']}->{c['n2']}: "
                      f"{c['f1_n1']:.4f}->{c['f1_n2']:.4f} ({c['delta_pp']:+.2f}pp) "
                      f"CI=[{ci[0]*100:+.2f},{ci[1]*100:+.2f}]", flush=True)

        config_result = {
            "model": cfg["model"], "seed": cfg["seed"], "max_n": max_n,
            "n_instances": len(instances), "greedy_f1": greedy_f1,
            "n_vals": n_vals,
            "f1_table": {method: {str(n): precomputed[(method, n)]["f1"] for n in n_vals} for method in METHODS},
            "transitions": inverse_cases,
            "summary": {
                "n_total": n_total, "n_inverse": n_inverse,
                "n_sig_inverse": n_sig_inverse,
                "n_positive": n_positive, "n_sig_positive": n_sig_positive,
            },
        }
        all_results[cfg_name] = config_result
        print(f"  Time: {time.time()-t0:.1f}s", flush=True)

    # ---- cross-seed consistency ----
    print(f"\n\n{'='*70}", flush=True)
    print("CROSS-SEED CONSISTENCY ANALYSIS", flush=True)
    print(f"{'='*70}", flush=True)

    groups = defaultdict(dict)
    for cfg_name, res in all_results.items():
        key = (res["model"], res["max_n"])
        groups[key][res["seed"]] = res

    consistency_report = {}

    for (model, max_n), seed_results in groups.items():
        seeds = sorted(seed_results.keys())
        if len(seeds) < 2:
            continue

        group_key = f"{model}_n{max_n}"
        print(f"\n  Group: {group_key} (seeds: {seeds})", flush=True)

        ref_n_vals = seed_results[seeds[0]]["n_vals"]

        transition_consistency = []
        for method in METHODS:
            for i in range(len(ref_n_vals) - 1):
                n1, n2 = ref_n_vals[i], ref_n_vals[i+1]
                directions = {}
                for seed in seeds:
                    transitions = seed_results[seed]["transitions"]
                    match = [t for t in transitions if t["method"] == method and t["n1"] == n1 and t["n2"] == n2]
                    if match:
                        t = match[0]
                        if t["sig_inverse"]:
                            directions[seed] = "inverse*"
                        elif t["is_inverse"]:
                            directions[seed] = "inverse"
                        elif t["sig_positive"]:
                            directions[seed] = "positive*"
                        else:
                            directions[seed] = "neutral"

                all_inverse = all("inverse" in d for d in directions.values())
                all_same = len(set(d.replace("*", "") for d in directions.values())) == 1
                any_sig_inverse = any("inverse*" in d for d in directions.values())

                tc = {
                    "method": method, "n1": n1, "n2": n2,
                    "directions": directions,
                    "all_inverse": all_inverse,
                    "all_same_direction": all_same,
                    "any_sig_inverse": any_sig_inverse,
                }
                transition_consistency.append(tc)

        n_all_inverse = sum(1 for tc in transition_consistency if tc["all_inverse"])
        n_all_same = sum(1 for tc in transition_consistency if tc["all_same_direction"])
        n_total_tc = len(transition_consistency)

        print(f"  All seeds agree inverse: {n_all_inverse}/{n_total_tc}", flush=True)
        print(f"  All seeds same direction: {n_all_same}/{n_total_tc}", flush=True)

        for tc in transition_consistency:
            dirs_str = ", ".join(f"s{s}={d}" for s, d in sorted(tc["directions"].items()))
            agree = "AGREE" if tc["all_same_direction"] else "DISAGREE"
            print(f"    {tc['method']:<18} N={tc['n1']}->{tc['n2']}: {dirs_str}  [{agree}]", flush=True)

        consistency_report[group_key] = {
            "seeds": seeds,
            "transitions": transition_consistency,
            "n_all_inverse": n_all_inverse,
            "n_all_same": n_all_same,
            "n_total": n_total_tc,
        }

    # ---- save results ----
    save_results = {}
    for k, v in all_results.items():
        sv = dict(v)
        for t in sv["transitions"]:
            t.pop("tuples", None)
        save_results[k] = sv

    with open(os.path.join(OUTPUT_DIR, "all_results.json"), "w") as f:
        json.dump(save_results, f, indent=2, default=str)

    with open(os.path.join(OUTPUT_DIR, "consistency_report.json"), "w") as f:
        json.dump(consistency_report, f, indent=2, default=str)

    print(f"\nSaved to {OUTPUT_DIR}/", flush=True)

    # ---- summary table ----
    print(f"\n\n{'='*70}", flush=True)
    print("SUMMARY TABLE", flush=True)
    print(f"{'='*70}", flush=True)

    print(f"\n{'Config':<30} {'Seed':>4} {'N_max':>5} {'Total':>6} {'Inv':>4} {'SigInv':>6} {'SigPos':>6}", flush=True)
    print("-" * 75, flush=True)
    for cfg_name in sorted(all_results.keys()):
        r = all_results[cfg_name]
        s = r["summary"]
        print(f"{cfg_name:<30} {r['seed']:>4} {r['max_n']:>5} {s['n_total']:>6} "
              f"{s['n_inverse']:>4} {s['n_sig_inverse']:>6} {s['n_sig_positive']:>6}", flush=True)

    print(f"\n\nPER-METHOD INVERSE COUNT (Qwen N=8, 3 transitions each)", flush=True)
    print(f"{'Method':<18}", end="", flush=True)
    qwen_n8_seeds = sorted([r["seed"] for k, r in all_results.items()
                            if "Qwen" in k and r["max_n"] == 8])
    for s in qwen_n8_seeds:
        print(f"  s{s:>3}", end="", flush=True)
    print("  Consistent?", flush=True)
    print("-" * 70, flush=True)

    for method in METHODS:
        counts = []
        for seed in qwen_n8_seeds:
            cfg = f"Qwen_FewNERD_s{seed}_n8"
            if cfg in all_results:
                r = all_results[cfg]
                inv_count = sum(1 for t in r["transitions"] if t["method"] == method and t["is_inverse"])
                counts.append(inv_count)
            else:
                counts.append(-1)
        consistent = "YES" if len(set(counts)) == 1 else "NO"
        vals = "  ".join(f"{c:>4}" if c >= 0 else "  N/A" for c in counts)
        print(f"{method:<18} {vals}  {consistent}", flush=True)

    print("\nDONE", flush=True)


if __name__ == "__main__":
    main()

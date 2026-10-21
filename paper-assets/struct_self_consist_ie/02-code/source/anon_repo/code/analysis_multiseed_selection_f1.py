#!/usr/bin/env python3
"""Multi-seed Selection F1 analysis for reviewer C2 response.

For each instance, score each sample with 5 signals (VC/SJ/FK/EM/LP),
select the top-scoring sample, compute its F1 vs gold.
Report mean±std over 3 seeds with bootstrap p-value vs greedy.
"""

import json
import os
import sys
import time
from collections import Counter

import numpy as np

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import (
    _ner_soft_jaccard_pair,
    _re_soft_jaccard_pair,
    _extract_surface_keys,
)
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie"

EXPERIMENT_GROUPS = {
    "qwen_scierc_ner_n8": {
        "subtask": "ner",
        "seeds": {
            42: f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
            123: f"{BASE}/output/exp_018_qwen_scierc_seed123/samples.jsonl",
            456: f"{BASE}/output/exp_018_qwen_scierc_seed456/samples.jsonl",
        },
    },
    "llama_scierc_ner_n8": {
        "subtask": "ner",
        "seeds": {
            42: f"{BASE}/output/exp_018_llama_scierc_seed42_r1024/samples.jsonl",
            123: f"{BASE}/output/exp_018_llama_scierc_seed123/samples.jsonl",
            456: f"{BASE}/output/exp_018_llama_scierc_seed456/samples.jsonl",
        },
    },
    "llama_conll_ner_n16": {
        "subtask": "ner",
        "seeds": {
            42: f"{BASE}/output/exp_017_llama_conll_n16_r1024/samples.jsonl",
            123: f"{BASE}/output/exp_017_llama_conll_n16_s123_r1024/samples.jsonl",
            456: f"{BASE}/output/exp_017_llama_conll_n16_s456_r1024/samples.jsonl",
        },
    },
}

N_BOOTSTRAP = 10000
BOOTSTRAP_SEED = 42
N_RANDOM_REPEATS = 50
SIGNALS = ["VC", "SJ", "FK", "EM", "LP"]


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


def compute_sample_surface_scores(instance, subtask):
    samples = instance["samples"]
    N = len(samples)
    key_sets = [frozenset(_extract_surface_keys(s, subtask)) for s in samples]
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            union = len(key_sets[i] | key_sets[j])
            inter = len(key_sets[i] & key_sets[j])
            s = inter / union if union > 0 else 1.0
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    fk_scores = [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]
    return fk_scores, key_sets


def compute_sample_voting_conf(key_sets, N):
    all_keys_count = Counter()
    for ks in key_sets:
        for key in ks:
            all_keys_count[key] += 1
    scores = []
    for ks in key_sets:
        if not ks:
            scores.append(0.0)
        else:
            fracs = [all_keys_count[key] / N for key in ks]
            scores.append(float(np.mean(fracs)))
    return scores


def compute_sample_em_scores(key_sets):
    N = len(key_sets)
    return [float(sum(1 for j in range(N) if j != k and key_sets[k] == key_sets[j])) for k in range(N)]


def compute_sample_logprobs(instance):
    lps = []
    for s in instance["samples"]:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lps.append(lp)
    return lps


def select_top1(scores):
    return int(np.argmax(scores))


def paired_bootstrap(f1s_signal, f1s_greedy, n_boot=10000, seed=42):
    rng = np.random.default_rng(seed)
    n = len(f1s_signal)
    deltas = np.empty(n_boot)
    for b in range(n_boot):
        idx = rng.integers(0, n, size=n)
        deltas[b] = f1s_signal[idx].mean() - f1s_greedy[idx].mean()
    lo = float(np.percentile(deltas, 2.5))
    hi = float(np.percentile(deltas, 97.5))
    mean_delta = float(np.mean(deltas))
    p_value = float(np.mean(deltas <= 0)) if mean_delta > 0 else float(np.mean(deltas >= 0))
    return {"mean_delta": mean_delta, "ci95": [lo, hi], "p_value": p_value}


def analyze_single_seed(path, subtask):
    instances = load_data(path)
    entity_key = "entities" if subtask == "ner" else "relations"
    valid = [inst for inst in instances if len(inst["gold"].get(entity_key, [])) > 0]

    n_inst = len(valid)
    rng = np.random.default_rng(BOOTSTRAP_SEED)

    signal_f1s = {sig: [] for sig in SIGNALS}
    greedy_f1s = []
    random_f1s = []
    oracle_f1s = []

    t0 = time.time()
    for idx, inst in enumerate(valid):
        if (idx + 1) % 500 == 0:
            print(f"      {idx+1}/{n_inst} ({time.time()-t0:.0f}s)")

        samples = inst["samples"]
        gold = inst["gold"]
        N = len(samples)

        sample_f1s = [per_instance_f1(s, gold, subtask=subtask) for s in samples]
        greedy_f1 = per_instance_f1(inst["greedy"], gold, subtask=subtask)
        greedy_f1s.append(greedy_f1)
        oracle_f1s.append(max(sample_f1s))

        # Random baseline
        rand_vals = []
        for _ in range(N_RANDOM_REPEATS):
            ri = int(rng.integers(0, N))
            rand_vals.append(sample_f1s[ri])
        random_f1s.append(float(np.mean(rand_vals)))

        # LP
        lps = compute_sample_logprobs(inst)
        signal_f1s["LP"].append(sample_f1s[select_top1(lps)])

        # SJ
        sj_scores = compute_sample_sj_scores(inst, subtask)
        signal_f1s["SJ"].append(sample_f1s[select_top1(sj_scores)])

        # FK + surface keys
        fk_scores, key_sets = compute_sample_surface_scores(inst, subtask)
        signal_f1s["FK"].append(sample_f1s[select_top1(fk_scores)])

        # VC
        vc_scores = compute_sample_voting_conf(key_sets, N)
        signal_f1s["VC"].append(sample_f1s[select_top1(vc_scores)])

        # EM
        em_scores = compute_sample_em_scores(key_sets)
        signal_f1s["EM"].append(sample_f1s[select_top1(em_scores)])

    elapsed = time.time() - t0
    print(f"      Done in {elapsed:.1f}s ({n_inst} instances)")

    greedy_arr = np.array(greedy_f1s)
    random_arr = np.array(random_f1s)
    oracle_arr = np.array(oracle_f1s)

    result = {
        "n_instances": n_inst,
        "greedy_f1": float(greedy_arr.mean()),
        "random_f1": float(random_arr.mean()),
        "oracle_f1": float(oracle_arr.mean()),
    }

    for sig in SIGNALS:
        arr = np.array(signal_f1s[sig])
        boot = paired_bootstrap(arr, greedy_arr, N_BOOTSTRAP, BOOTSTRAP_SEED)
        result[sig] = {
            "selection_f1": float(arr.mean()),
            "delta_vs_greedy": float(arr.mean() - greedy_arr.mean()),
            "bootstrap": boot,
        }

    return result


def aggregate_seeds(seed_results, seeds):
    agg = {}
    n_inst = seed_results[seeds[0]]["n_instances"]
    agg["seeds"] = seeds
    agg["n_instances"] = n_inst

    for key in ["greedy_f1", "random_f1", "oracle_f1"]:
        vals = [seed_results[s][key] for s in seeds]
        agg[key] = {
            "mean": round(float(np.mean(vals)), 5),
            "std": round(float(np.std(vals, ddof=1)), 5),
            "per_seed": [round(v, 5) for v in vals],
        }

    agg["signal_selection_f1"] = {}
    for sig in SIGNALS:
        vals = [seed_results[s][sig]["selection_f1"] for s in seeds]
        deltas = [seed_results[s][sig]["delta_vs_greedy"] for s in seeds]
        p_values = [seed_results[s][sig]["bootstrap"]["p_value"] for s in seeds]
        ci_los = [seed_results[s][sig]["bootstrap"]["ci95"][0] for s in seeds]
        ci_his = [seed_results[s][sig]["bootstrap"]["ci95"][1] for s in seeds]

        agg["signal_selection_f1"][sig] = {
            "mean": round(float(np.mean(vals)), 5),
            "std": round(float(np.std(vals, ddof=1)), 5),
            "per_seed": [round(v, 5) for v in vals],
            "delta_vs_greedy_mean": round(float(np.mean(deltas)), 5),
            "delta_vs_greedy_std": round(float(np.std(deltas, ddof=1)), 5),
            "vs_greedy_p_per_seed": [round(p, 5) for p in p_values],
            "vs_greedy_ci95_per_seed": [[round(lo, 5), round(hi, 5)] for lo, hi in zip(ci_los, ci_his)],
        }

    return agg


def main():
    all_results = {}

    for group_name, group_cfg in EXPERIMENT_GROUPS.items():
        subtask = group_cfg["subtask"]
        seeds_cfg = group_cfg["seeds"]
        seeds = sorted(seeds_cfg.keys())

        print(f"\n{'='*60}")
        print(f"  {group_name}")
        print(f"{'='*60}")

        seed_results = {}
        for seed in seeds:
            path = seeds_cfg[seed]
            if not os.path.exists(path):
                print(f"  SKIP seed {seed}: {path} not found")
                continue
            print(f"  seed {seed}:")
            seed_results[seed] = analyze_single_seed(path, subtask)

        if len(seed_results) < 3:
            print(f"  WARNING: only {len(seed_results)} seeds found, need 3")
            if len(seed_results) == 0:
                continue

        agg = aggregate_seeds(seed_results, list(seed_results.keys()))
        all_results[group_name] = agg

        # Print summary table
        print(f"\n  {'Method':<10s}  {'Mean F1':>9s}  {'±σ':>7s}  {'Δ greedy':>9s}")
        print(f"  {'-'*10}  {'-'*9}  {'-'*7}  {'-'*9}")
        print(f"  {'Greedy':<10s}  {agg['greedy_f1']['mean']:.5f}  {agg['greedy_f1']['std']:.5f}")
        print(f"  {'Random':<10s}  {agg['random_f1']['mean']:.5f}  {agg['random_f1']['std']:.5f}")
        for sig in SIGNALS:
            sr = agg["signal_selection_f1"][sig]
            print(f"  {sig:<10s}  {sr['mean']:.5f}  {sr['std']:.5f}  {sr['delta_vs_greedy_mean']:+.5f}")
        print(f"  {'Oracle':<10s}  {agg['oracle_f1']['mean']:.5f}  {agg['oracle_f1']['std']:.5f}")

    out_path = f"{BASE}/output/analysis_multiseed_selection_f1.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

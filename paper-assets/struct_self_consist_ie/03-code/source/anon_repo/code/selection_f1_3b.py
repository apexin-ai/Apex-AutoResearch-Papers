#!/usr/bin/env python3
"""Selection F1 for LLaMA-3.2-3B vs 8B scale ablation (single-seed)."""
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

EXPERIMENTS = {
    "llama_8b_scierc_ner": {
        "path": f"{BASE}/output/exp_018_llama_scierc_seed42_r1024/samples.jsonl",
        "subtask": "ner",
    },
    "llama_3b_scierc_ner": {
        "path": f"{BASE}/output/review_round9_experiments/llama3b_scierc/samples.jsonl",
        "subtask": "ner",
    },
}

N_BOOTSTRAP = 10000
BOOTSTRAP_SEED = 42
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


def paired_bootstrap(sel_f1s, greedy_f1s, n_bootstrap, seed):
    rng = np.random.RandomState(seed)
    n = len(sel_f1s)
    count_ge = 0
    deltas = np.empty(n_bootstrap)
    for b in range(n_bootstrap):
        idx = rng.randint(0, n, size=n)
        d = sel_f1s[idx].mean() - greedy_f1s[idx].mean()
        deltas[b] = d
        if d <= 0:
            count_ge += 1
    p_value = count_ge / n_bootstrap
    ci95 = [float(np.percentile(deltas, 2.5)), float(np.percentile(deltas, 97.5))]
    return {"p_value": float(p_value), "ci95": ci95}


def analyze(path, subtask):
    data = load_data(path)
    field = "entities" if subtask == "ner" else "relations"
    instances = [inst for inst in data if len(inst["gold"].get(field, [])) > 0]
    n_inst = len(instances)
    N_per = len(instances[0]["samples"]) if instances else 0
    print(f"  {n_inst} valid instances (gold-empty filtered: {len(data) - n_inst}), N={N_per}")

    t0 = time.time()
    greedy_f1s, oracle_f1s, random_f1s = [], [], []
    signal_f1s = {sig: [] for sig in SIGNALS}

    for inst in instances:
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy", samples[0])
        N = len(samples)

        g_f1 = per_instance_f1(greedy, gold, subtask=subtask)
        greedy_f1s.append(g_f1)

        sample_f1s = [per_instance_f1(s, gold, subtask=subtask) for s in samples]
        oracle_f1s.append(max(sample_f1s))
        random_f1s.append(float(np.mean(sample_f1s)))

        sj_scores = compute_sample_sj_scores(inst, subtask)
        fk_scores, key_sets = compute_sample_surface_scores(inst, subtask)
        vc_scores = compute_sample_voting_conf(key_sets, N)
        em_scores = compute_sample_em_scores(key_sets)
        lp_scores = compute_sample_logprobs(inst)

        all_scores = {"SJ": sj_scores, "FK": fk_scores, "VC": vc_scores,
                      "EM": em_scores, "LP": lp_scores}

        for sig in SIGNALS:
            chosen = int(np.argmax(all_scores[sig]))
            signal_f1s[sig].append(sample_f1s[chosen])

    elapsed = time.time() - t0
    print(f"  Computed in {elapsed:.1f}s")

    greedy_arr = np.array(greedy_f1s)
    oracle_arr = np.array(oracle_f1s)
    random_arr = np.array(random_f1s)

    result = {
        "n_instances": n_inst,
        "n_gold_empty_filtered": len(data) - n_inst,
        "n_samples_per_instance": N_per,
        "greedy_f1": round(float(greedy_arr.mean()), 5),
        "random_f1": round(float(random_arr.mean()), 5),
        "oracle_f1": round(float(oracle_arr.mean()), 5),
    }

    for sig in SIGNALS:
        arr = np.array(signal_f1s[sig])
        boot = paired_bootstrap(arr, greedy_arr, N_BOOTSTRAP, BOOTSTRAP_SEED)
        result[sig] = {
            "selection_f1": round(float(arr.mean()), 5),
            "delta_vs_greedy": round(float(arr.mean() - greedy_arr.mean()), 5),
            "bootstrap_p": round(boot["p_value"], 5),
            "bootstrap_ci95": [round(x, 5) for x in boot["ci95"]],
        }

    return result


def main():
    all_results = {}

    for exp_name, cfg in EXPERIMENTS.items():
        path = cfg["path"]
        subtask = cfg["subtask"]
        print(f"\n{'='*60}")
        print(f"  {exp_name} (subtask={subtask})")
        print(f"{'='*60}")

        if not os.path.exists(path):
            print(f"  SKIP: {path} not found")
            continue

        result = analyze(path, subtask)
        all_results[exp_name] = result

        print(f"\n  {'Method':<10s}  {'Sel F1':>9s}  {'delta Greedy':>12s}  {'p-value':>9s}")
        print(f"  {'-'*10}  {'-'*9}  {'-'*12}  {'-'*9}")
        print(f"  {'Greedy':<10s}  {result['greedy_f1']:.5f}")
        print(f"  {'Random':<10s}  {result['random_f1']:.5f}  {result['random_f1']-result['greedy_f1']:+.5f}")
        for sig in SIGNALS:
            sr = result[sig]
            print(f"  {sig:<10s}  {sr['selection_f1']:.5f}  {sr['delta_vs_greedy']:+.5f}  {sr['bootstrap_p']:.5f}")
        print(f"  {'Oracle':<10s}  {result['oracle_f1']:.5f}  {result['oracle_f1']-result['greedy_f1']:+.5f}")

    out_path = f"{BASE}/output/review_round9_experiments/llama3b_scierc/selection_f1_3b_vs_8b.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

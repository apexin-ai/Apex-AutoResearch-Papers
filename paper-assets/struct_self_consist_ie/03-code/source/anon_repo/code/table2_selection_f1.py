#!/usr/bin/env python3
"""Selection F1 for Table 2: Qwen SciERC NER N=8, seed42+seed123."""

import json
import os
import sys
import time
from collections import Counter

import numpy as np
from scipy.stats import binomtest

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import (
    _ner_soft_jaccard_pair,
    _extract_surface_keys,
)
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie"
SEEDS = {
    42: f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
    123: f"{BASE}/output/exp_018_qwen_scierc_seed123/samples.jsonl",
}
SUBTASK = "ner"
SIGNALS = ["LP", "SJ", "EM", "VC", "FK"]
N_RANDOM_REPEATS = 50


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def compute_sample_sj_scores(instance):
    samples = instance["samples"]
    N = len(samples)
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = _ner_soft_jaccard_pair(
                samples[i].get("entities", []),
                samples[j].get("entities", []),
            )
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]


def compute_sample_surface_scores(instance):
    samples = instance["samples"]
    N = len(samples)
    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]
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
    all_keys = set()
    for ks in key_sets:
        all_keys |= ks
    if not all_keys:
        return [1.0] * N
    key_freq = {}
    for k in all_keys:
        key_freq[k] = sum(1 for ks in key_sets if k in ks) / N
    scores = []
    for ks in key_sets:
        if not ks:
            scores.append(0.0)
        else:
            scores.append(float(np.mean([key_freq[k] for k in ks])))
    return scores


def compute_sample_em_scores(key_sets):
    counter = Counter(key_sets)
    return [counter[ks] / len(key_sets) for ks in key_sets]


def compute_sample_logprobs(instance):
    lps = []
    for s in instance["samples"]:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lps.append(lp)
    return lps


def sign_test_pvalue(sel_f1s, greedy_f1s):
    wins = sum(1 for s, g in zip(sel_f1s, greedy_f1s) if s > g)
    losses = sum(1 for s, g in zip(sel_f1s, greedy_f1s) if s < g)
    ties = sum(1 for s, g in zip(sel_f1s, greedy_f1s) if abs(s - g) < 1e-12)
    n_nonzero = wins + losses
    if n_nonzero == 0:
        return 1.0, wins, losses, ties
    result = binomtest(wins, n_nonzero, 0.5, alternative='two-sided')
    return result.pvalue, wins, losses, ties


def analyze_single_seed(path):
    data = load_data(path)
    instances = [d for d in data if len(d["gold"].get("entities", [])) > 0]
    n_inst = len(instances)
    N_per = len(instances[0]["samples"]) if instances else 0
    print(f"  {n_inst} valid instances (filtered from {len(data)}), N={N_per}")

    greedy_f1s = []
    oracle_f1s = []
    random_f1s = []
    signal_f1s = {sig: [] for sig in SIGNALS}

    t0 = time.time()
    for inst in instances:
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy", samples[0])
        N = len(samples)

        g_f1 = per_instance_f1(greedy, gold, subtask=SUBTASK)
        greedy_f1s.append(g_f1)

        sample_f1s = [per_instance_f1(s, gold, subtask=SUBTASK) for s in samples]
        oracle_f1s.append(max(sample_f1s))
        random_f1s.append(float(np.mean(sample_f1s)))

        sj_scores = compute_sample_sj_scores(inst)
        fk_scores, key_sets = compute_sample_surface_scores(inst)
        vc_scores = compute_sample_voting_conf(key_sets, N)
        em_scores = compute_sample_em_scores(key_sets)
        lp_scores = compute_sample_logprobs(inst)

        all_scores = {"SJ": sj_scores, "FK": fk_scores, "VC": vc_scores,
                      "EM": em_scores, "LP": lp_scores}

        for sig in SIGNALS:
            chosen = int(np.argmax(all_scores[sig]))
            signal_f1s[sig].append(sample_f1s[chosen])

    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.1f}s")

    result = {
        "n_instances": n_inst,
        "n_samples_per_instance": N_per,
        "greedy_f1": float(np.mean(greedy_f1s)),
        "random_f1": float(np.mean(random_f1s)),
        "oracle_f1": float(np.mean(oracle_f1s)),
        "greedy_f1_list": greedy_f1s,
    }

    for sig in SIGNALS:
        arr = signal_f1s[sig]
        p_val, wins, losses, ties = sign_test_pvalue(arr, greedy_f1s)
        result[sig] = {
            "selection_f1": float(np.mean(arr)),
            "delta_vs_greedy": float(np.mean(arr) - np.mean(greedy_f1s)),
            "sign_test_p": p_val,
            "wins": wins,
            "losses": losses,
            "ties": ties,
        }

    return result


def main():
    all_seed_results = {}
    for seed, path in sorted(SEEDS.items()):
        print(f"\nSeed {seed}: {path}")
        all_seed_results[seed] = analyze_single_seed(path)

    seeds = sorted(all_seed_results.keys())
    
    output = {"seeds": seeds, "subtask": SUBTASK, "methods": {}}

    # Greedy
    per_seed_greedy = {s: all_seed_results[s]["greedy_f1"] for s in seeds}
    vals = list(per_seed_greedy.values())
    output["methods"]["Greedy"] = {
        "per_seed": per_seed_greedy,
        "mean": float(np.mean(vals)),
        "std": float(np.std(vals, ddof=1)),
    }

    # Random
    per_seed_random = {s: all_seed_results[s]["random_f1"] for s in seeds}
    vals = list(per_seed_random.values())
    greedy_mean = output["methods"]["Greedy"]["mean"]
    output["methods"]["Random"] = {
        "per_seed": per_seed_random,
        "mean": float(np.mean(vals)),
        "std": float(np.std(vals, ddof=1)),
        "delta_vs_greedy": float(np.mean(vals) - greedy_mean),
    }

    # Signals
    for sig in SIGNALS:
        per_seed_f1 = {s: all_seed_results[s][sig]["selection_f1"] for s in seeds}
        per_seed_p = {s: all_seed_results[s][sig]["sign_test_p"] for s in seeds}
        per_seed_wins = {s: all_seed_results[s][sig]["wins"] for s in seeds}
        per_seed_losses = {s: all_seed_results[s][sig]["losses"] for s in seeds}
        per_seed_ties = {s: all_seed_results[s][sig]["ties"] for s in seeds}
        vals = list(per_seed_f1.values())
        
        # Combined p-value: Fisher's method on per-seed p-values
        from scipy.stats import combine_pvalues
        pvals = [per_seed_p[s] for s in seeds]
        _, combined_p = combine_pvalues(pvals, method='fisher')
        
        output["methods"][sig] = {
            "per_seed": per_seed_f1,
            "mean": float(np.mean(vals)),
            "std": float(np.std(vals, ddof=1)),
            "delta_vs_greedy": float(np.mean(vals) - greedy_mean),
            "per_seed_p": per_seed_p,
            "combined_p": float(combined_p),
            "per_seed_wins": per_seed_wins,
            "per_seed_losses": per_seed_losses,
            "per_seed_ties": per_seed_ties,
        }

    # Oracle
    per_seed_oracle = {s: all_seed_results[s]["oracle_f1"] for s in seeds}
    vals = list(per_seed_oracle.values())
    output["methods"]["Oracle"] = {
        "per_seed": per_seed_oracle,
        "mean": float(np.mean(vals)),
        "std": float(np.std(vals, ddof=1)),
        "delta_vs_greedy": float(np.mean(vals) - greedy_mean),
    }

    # Save JSON
    out_path = f"{BASE}/output/review_round2/selection_f1_table2.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")

    # Print table
    print("\n## SciERC NER Selection F1 (N=8, T=1.0, Unified Pipeline)\n")
    print("| Method | seed42 F1 | seed123 F1 | Mean ± σ | ΔF1 vs Greedy | p-value |")
    print("|--------|-----------|------------|----------|---------------|---------|")

    for method_name in ["Greedy", "Random"] + SIGNALS + ["Oracle"]:
        m = output["methods"][method_name]
        s42 = m["per_seed"].get(42, m["per_seed"].get("42", 0))
        s123 = m["per_seed"].get(123, m["per_seed"].get("123", 0))
        mean_std = f"{m['mean']:.4f} ± {m['std']:.4f}"
        
        if method_name == "Greedy":
            delta = "—"
            p_str = "—"
        elif method_name in ["Random", "Oracle"]:
            delta = f"{m['delta_vs_greedy']*100:+.1f} pp"
            p_str = "—"
        else:
            delta = f"{m['delta_vs_greedy']*100:+.1f} pp"
            p_str = f"{m['combined_p']:.3f}"
        
        print(f"| {method_name} | {s42:.4f} | {s123:.4f} | {mean_std} | {delta} | {p_str} |")

    # Also print per-seed sign test details
    print("\n### Per-seed sign test details:")
    for sig in SIGNALS:
        m = output["methods"][sig]
        for s in seeds:
            sk = s
            print(f"  {sig} seed{s}: wins={m['per_seed_wins'][sk]}, losses={m['per_seed_losses'][sk]}, ties={m['per_seed_ties'][sk]}, p={m['per_seed_p'][sk]:.4f}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""exp_017 LLaMA CoNLL N=8: full signal analysis.
Computes: CF1 gold-filtered degeneracy, selection F1, LP range, QE metrics.
"""
import json
import sys
import time
from collections import Counter

import numpy as np
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import _ner_soft_jaccard_pair, _extract_surface_keys
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl"
SUBTASK = "ner"


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def compute_sample_sj_scores(inst):
    samples = inst["samples"]
    N = len(samples)
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = _ner_soft_jaccard_pair(samples[i].get("entities", []), samples[j].get("entities", []))
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]


def compute_sample_surface_scores(inst):
    samples = inst["samples"]
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


def compute_sample_logprobs(inst):
    lps = []
    for s in inst["samples"]:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lps.append(lp)
    return lps


def main():
    t0 = time.time()
    data = load_data(DATA_PATH)
    N_per = len(data[0]["samples"])
    print(f"Loaded {len(data)} instances, N={N_per}")

    gold_filtered = [inst for inst in data if len(inst["gold"].get("entities", [])) > 0]
    n_gf = len(gold_filtered)
    print(f"Gold-filtered: {n_gf}")

    # --- CF1 gold-filtered degeneracy ---
    n_constant_f1 = 0
    all_greedy_f1 = []
    all_oracle_f1 = []
    all_random_f1 = []
    signal_sel_f1 = {sig: [] for sig in ["SJ", "FK", "VC", "EM", "LP"]}
    lp_ranges = []

    for idx, inst in enumerate(gold_filtered):
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy", samples[0])

        g_f1 = per_instance_f1(greedy, gold, subtask=SUBTASK)
        sample_f1s = [per_instance_f1(s, gold, subtask=SUBTASK) for s in samples]

        all_greedy_f1.append(g_f1)
        all_oracle_f1.append(max(sample_f1s))
        all_random_f1.append(float(np.mean(sample_f1s)))

        # CF1: all sample F1s identical?
        if len(set(round(f, 10) for f in sample_f1s)) == 1:
            n_constant_f1 += 1

        # Signal scores
        sj_scores = compute_sample_sj_scores(inst)
        fk_scores, key_sets = compute_sample_surface_scores(inst)
        vc_scores = compute_sample_voting_conf(key_sets, N_per)
        em_scores = compute_sample_em_scores(key_sets)
        lp_scores = compute_sample_logprobs(inst)

        all_scores = {"SJ": sj_scores, "FK": fk_scores, "VC": vc_scores,
                      "EM": em_scores, "LP": lp_scores}

        for sig in signal_sel_f1:
            chosen = int(np.argmax(all_scores[sig]))
            signal_sel_f1[sig].append(sample_f1s[chosen])

        # LP range
        valid_lps = [lp for lp in lp_scores if np.isfinite(lp) and lp > -900]
        if len(valid_lps) >= 2:
            lp_ranges.append(max(valid_lps) - min(valid_lps))

        if (idx + 1) % 500 == 0:
            print(f"  processed {idx+1}/{n_gf}")

    elapsed = time.time() - t0
    print(f"Done in {elapsed:.1f}s")

    degeneracy_cf1 = n_constant_f1 / n_gf

    greedy_arr = np.array(all_greedy_f1)
    oracle_arr = np.array(all_oracle_f1)
    random_arr = np.array(all_random_f1)

    result = {
        "dataset": "conll2003",
        "model": "llama3.1-8b",
        "N": N_per,
        "n_total": len(data),
        "n_gold_filtered": n_gf,
        "degeneracy_cf1_gold_filtered": round(degeneracy_cf1, 4),
        "n_constant_f1": n_constant_f1,
        "greedy_f1": round(float(greedy_arr.mean()), 4),
        "oracle_f1": round(float(oracle_arr.mean()), 4),
        "random_f1": round(float(random_arr.mean()), 4),
        "headroom_pp": round(float((oracle_arr.mean() - greedy_arr.mean()) * 100), 2),
        "selection_f1": {},
        "lp_range": {
            "mean": round(float(np.mean(lp_ranges)), 4),
            "std": round(float(np.std(lp_ranges)), 4),
            "median": round(float(np.median(lp_ranges)), 4),
            "n_valid": len(lp_ranges),
        },
    }

    for sig in ["SJ", "FK", "VC", "EM", "LP"]:
        arr = np.array(signal_sel_f1[sig])
        delta = float(arr.mean() - greedy_arr.mean())
        result["selection_f1"][sig] = {
            "f1": round(float(arr.mean()), 4),
            "delta_vs_greedy": round(delta, 4),
            "delta_pp": round(delta * 100, 2),
        }

    # Print summary
    print(f"\n=== exp_017 LLaMA CoNLL N={N_per} Full Signal Analysis ===")
    print(f"Instances: {len(data)} total, {n_gf} gold-filtered")
    print(f"Degeneracy (CF1 gold-filtered): {degeneracy_cf1:.4f} ({n_constant_f1}/{n_gf})")
    print(f"Greedy F1: {greedy_arr.mean():.4f}")
    print(f"Oracle F1: {oracle_arr.mean():.4f}")
    print(f"Random F1: {random_arr.mean():.4f}")
    print(f"Headroom: {(oracle_arr.mean() - greedy_arr.mean())*100:.2f}pp")
    print(f"\nSelection F1:")
    for sig in ["SJ", "FK", "VC", "EM", "LP"]:
        sf = result["selection_f1"][sig]
        print(f"  {sig:>3}: {sf['f1']:.4f}  (Δ={sf['delta_pp']:+.2f}pp)")
    print(f"\nLP Range: mean={result['lp_range']['mean']:.4f}, std={result['lp_range']['std']:.4f}, median={result['lp_range']['median']:.4f}")

    # Comparison with Qwen3 on CoNLL
    print(f"\n=== Cross-model comparison (CoNLL) ===")
    print(f"{'Metric':<30s}  {'LLaMA':>8s}  {'Qwen3':>8s}")
    print(f"{'-'*30}  {'-'*8}  {'-'*8}")
    print(f"{'Greedy F1':<30s}  {greedy_arr.mean():.4f}    0.7250")
    print(f"{'Oracle F1':<30s}  {oracle_arr.mean():.4f}    0.7570")
    print(f"{'Headroom (pp)':<30s}  {(oracle_arr.mean()-greedy_arr.mean())*100:.2f}      3.20")
    print(f"{'Degeneracy CF1 gold-filt':<30s}  {degeneracy_cf1:.4f}    0.4740")

    # Save
    out_path = "/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/full_signal_analysis.json"
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

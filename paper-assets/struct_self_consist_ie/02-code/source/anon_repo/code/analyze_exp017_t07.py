#!/usr/bin/env python3
"""exp_017 T=0.7 post-hoc analysis: LP range + 5-signal rho/AUROC + selection F1."""

import json
import os
import sys
import time
from collections import Counter

import numpy as np
from scipy.stats import spearmanr, rankdata

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import compute_all_consistency_scores, _ner_soft_jaccard_pair, _extract_surface_keys
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie"
T07_PATH = f"{BASE}/output/exp_017_llama_conll_n8_t07/samples.jsonl"
T10_PATH = f"{BASE}/output/exp_017_llama_conll_infer/samples.jsonl"
OUTPUT_DIR = f"{BASE}/output/analysis_round8"
OUTPUT_PATH = f"{OUTPUT_DIR}/exp017_t07_lp_range.json"
SUBTASK = "ner"


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def filter_gold_empty(data):
    return [d for d in data if len(d["gold"].get("entities", [])) > 0]


def compute_lp_ranges(instances):
    """For each instance, compute LP range = max(mean_logprob) - min(mean_logprob) across N samples."""
    ranges = []
    for inst in instances:
        lps = []
        for s in inst["samples"]:
            lp = s.get("mean_logprob")
            if lp is not None and np.isfinite(lp):
                lps.append(lp)
        if len(lps) >= 2:
            ranges.append(max(lps) - min(lps))
        else:
            ranges.append(0.0)
    return np.array(ranges)


def lp_range_stats(ranges, eps=0.05):
    return {
        "min": float(np.min(ranges)),
        "q10": float(np.percentile(ranges, 10)),
        "iqr_25": float(np.percentile(ranges, 25)),
        "median": float(np.median(ranges)),
        "iqr_75": float(np.percentile(ranges, 75)),
        "q90": float(np.percentile(ranges, 90)),
        "max": float(np.max(ranges)),
        "mean": float(np.mean(ranges)),
        "tied_fraction_005": float(np.mean(ranges < eps)),
    }


def safe_auroc(scores, labels):
    scores = np.asarray(scores, dtype=float)
    labels = np.asarray(labels, dtype=int)
    if len(np.unique(labels)) < 2:
        return float("nan")
    n_pos = np.sum(labels == 1)
    n_neg = np.sum(labels == 0)
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    ranks = rankdata(scores)
    u = ranks[labels == 1].sum() - n_pos * (n_pos + 1) / 2
    return float(u / (n_pos * n_neg))


def safe_spearman(x, y):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    x, y = x[mask], y[mask]
    if len(x) < 3:
        return float("nan")
    return float(spearmanr(x, y).statistic)


def compute_exact_match_rate(samples, subtask):
    if subtask == "ner":
        keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    else:
        keys = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", [])) for s in samples]
    if not keys:
        return 0.0
    counter = Counter(keys)
    return counter.most_common(1)[0][1] / len(samples)


def compute_voting_confidence(samples, subtask):
    N = len(samples)
    if N == 0:
        return 0.0
    counter = Counter()
    if subtask == "ner":
        for s in samples:
            for e in s.get("entities", []):
                counter[(e["text"], e["type"])] += 1
    if not counter:
        return 0.0
    rates = [v / N for v in counter.values()]
    return float(np.mean(rates))


def compute_mean_logprob(samples):
    logprobs = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    logprobs = [lp for lp in logprobs if np.isfinite(lp)]
    if not logprobs:
        return float("nan")
    return float(np.mean(logprobs))


# --- Selection F1 helpers ---
def compute_sample_sj_scores(instance, subtask):
    samples = instance["samples"]
    N = len(samples)
    field = "entities"
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = _ner_soft_jaccard_pair(samples[i].get(field, []), samples[j].get(field, []))
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


def main():
    t_start = time.time()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load T=0.7
    print("Loading T=0.7 data...")
    data_t07 = load_data(T07_PATH)
    valid_t07 = filter_gold_empty(data_t07)
    print(f"  T=0.7: {len(data_t07)} total, {len(valid_t07)} valid (gold non-empty)")

    # Load T=1.0
    print("Loading T=1.0 data...")
    data_t10 = load_data(T10_PATH)
    valid_t10 = filter_gold_empty(data_t10)
    print(f"  T=1.0: {len(data_t10)} total, {len(valid_t10)} valid")

    # Part 1: LP Range
    print("\n=== Part 1: LP Range ===")
    ranges_t07 = compute_lp_ranges(valid_t07)
    stats_t07 = lp_range_stats(ranges_t07)
    print(f"  T=0.7: median={stats_t07['median']:.6f}, IQR=[{stats_t07['iqr_25']:.6f}, {stats_t07['iqr_75']:.6f}], "
          f"tied(ε=0.05)={stats_t07['tied_fraction_005']:.4f}")

    ranges_t10 = compute_lp_ranges(valid_t10)
    stats_t10 = lp_range_stats(ranges_t10)
    print(f"  T=1.0: median={stats_t10['median']:.6f}, IQR=[{stats_t10['iqr_25']:.6f}, {stats_t10['iqr_75']:.6f}], "
          f"tied(ε=0.05)={stats_t10['tied_fraction_005']:.4f}")

    # Part 2: 5-signal rho + AUROC
    print("\n=== Part 2: 5-signal rho + AUROC ===")
    consistency = compute_all_consistency_scores(valid_t07, subtask=SUBTASK)
    sj_vals = consistency["soft_jaccard"]
    fk_vals = consistency["fleiss_kappa"]

    lp_vals, em_vals, vc_vals, f1_vals = [], [], [], []
    for inst in valid_t07:
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy", samples[0])
        lp_vals.append(compute_mean_logprob(samples))
        em_vals.append(compute_exact_match_rate(samples, SUBTASK))
        vc_vals.append(compute_voting_confidence(samples, SUBTASK))
        f1_vals.append(per_instance_f1(greedy, gold, subtask=SUBTASK))

    signals = {
        "SJ": np.array(sj_vals, dtype=float),
        "FK": np.array(fk_vals, dtype=float),
        "VC": np.array(vc_vals, dtype=float),
        "EM": np.array(em_vals, dtype=float),
        "LP": np.array(lp_vals, dtype=float),
    }
    f1_arr = np.array(f1_vals, dtype=float)
    binary_correct = (f1_arr >= 1.0).astype(int)

    signal_results = {}
    for sig_name, sig_vals in signals.items():
        rho = safe_spearman(sig_vals, f1_arr)
        auroc = safe_auroc(sig_vals, binary_correct)
        signal_results[sig_name] = {"rho": round(rho, 4), "auroc": round(auroc, 4)}
        print(f"  {sig_name:>4}: rho={rho:.4f}  AUROC={auroc:.4f}")

    # Part 3: Selection F1
    print("\n=== Part 3: Selection F1 ===")
    greedy_f1s = []
    oracle_f1s = []
    sel_f1s = {sig: [] for sig in ["SJ", "FK", "VC", "EM", "LP"]}

    for inst in valid_t07:
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy", samples[0])
        N = len(samples)

        g_f1 = per_instance_f1(greedy, gold, subtask=SUBTASK)
        sample_f1s = [per_instance_f1(s, gold, subtask=SUBTASK) for s in samples]
        o_f1 = max(sample_f1s)
        greedy_f1s.append(g_f1)
        oracle_f1s.append(o_f1)

        sj_scores = compute_sample_sj_scores(inst, SUBTASK)
        fk_scores, key_sets = compute_sample_surface_scores(inst, SUBTASK)
        vc_scores = compute_sample_voting_conf(key_sets, N)
        em_scores = compute_sample_em_scores(key_sets)
        lp_scores = compute_sample_logprobs(inst)

        for sig_name, scores in [("SJ", sj_scores), ("FK", fk_scores), ("VC", vc_scores),
                                  ("EM", em_scores), ("LP", lp_scores)]:
            best_idx = int(np.argmax(scores))
            sel_f1s[sig_name].append(sample_f1s[best_idx])

    greedy_mean = float(np.mean(greedy_f1s))
    oracle_mean = float(np.mean(oracle_f1s))
    print(f"  Greedy F1:  {greedy_mean:.4f}")
    print(f"  Oracle F1:  {oracle_mean:.4f}")

    selection_f1 = {"greedy": round(greedy_mean, 4), "oracle": round(oracle_mean, 4)}
    for sig_name in ["SJ", "FK", "VC", "EM", "LP"]:
        sf1 = float(np.mean(sel_f1s[sig_name]))
        delta = sf1 - greedy_mean
        selection_f1[sig_name] = round(sf1, 4)
        print(f"  {sig_name:>4} sel F1: {sf1:.4f}  (Δ={delta:+.4f} pp)")

    # Build output
    result = {
        "config": "LLaMA CoNLL N=8 T=0.7 seed42",
        "n_total": len(data_t07),
        "n_gold_empty": len(data_t07) - len(valid_t07),
        "n_valid": len(valid_t07),
        "lp_range": stats_t07,
        "t10_comparison": {
            "n_valid": len(valid_t10),
            "lp_range": stats_t10,
        },
        "signals": signal_results,
        "selection_f1": selection_f1,
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved to {OUTPUT_PATH}")
    print(f"Total time: {time.time() - t_start:.1f}s")


if __name__ == "__main__":
    main()

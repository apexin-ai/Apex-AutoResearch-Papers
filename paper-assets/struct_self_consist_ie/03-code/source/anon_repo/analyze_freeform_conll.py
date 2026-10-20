#!/usr/bin/env python3
"""Analyze free-form CoNLL 4-seed results: 5-signal rho, selection F1, LP distribution."""

from __future__ import annotations

import json
import os
import sys
from collections import Counter

import numpy as np
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import (
    compute_all_consistency_scores,
    _ner_soft_jaccard_pair,
    _extract_surface_keys,
)
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUTPUT_BASE = f"{BASE}/output/review_round9_experiments/freeform_conll"
SEEDS = [42, 123, 456, 789]
CONSTRAINED_PATH = f"{BASE}/output/exp002_conll2003/report.json"


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def safe_spearman(x, y):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    x, y = x[mask], y[mask]
    if len(x) < 3:
        return float("nan"), float("nan")
    r = spearmanr(x, y)
    return float(r.statistic), float(r.pvalue)


# --- Per-instance signal computation (instance-level, for rho) ---
def compute_instance_em_rate(samples, subtask="ner"):
    keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    if not keys:
        return 0.0
    counter = Counter(keys)
    return counter.most_common(1)[0][1] / len(samples)


def compute_instance_vc(samples, subtask="ner"):
    N = len(samples)
    if N == 0:
        return 0.0
    counter = Counter()
    for s in samples:
        for e in s.get("entities", []):
            counter[(e["text"], e["type"])] += 1
    if not counter:
        return 0.0
    return float(np.mean([v / N for v in counter.values()]))


def compute_instance_lp(samples):
    lps = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    lps = [lp for lp in lps if np.isfinite(lp)]
    return float(np.mean(lps)) if lps else float("nan")


# --- Per-sample signal computation (for selection F1) ---
def compute_sample_sj_scores(instance):
    samples = instance["samples"]
    N = len(samples)
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = _ner_soft_jaccard_pair(samples[i].get("entities", []),
                                       samples[j].get("entities", []))
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]


def compute_sample_surface_scores(instance):
    samples = instance["samples"]
    N = len(samples)
    key_sets = [frozenset(_extract_surface_keys(s, "ner")) for s in samples]
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


def compute_sample_vc(key_sets, N):
    all_keys_count = Counter()
    for ks in key_sets:
        for key in ks:
            all_keys_count[key] += 1
    scores = []
    for ks in key_sets:
        if not ks:
            scores.append(0.0)
        else:
            scores.append(float(np.mean([all_keys_count[key] / N for key in ks])))
    return scores


def compute_sample_em(key_sets):
    N = len(key_sets)
    return [float(sum(1 for j in range(N) if j != k and key_sets[k] == key_sets[j])) for k in range(N)]


def compute_sample_lp(instance):
    return [s.get("mean_logprob", s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1))
            for s in instance["samples"]]


def analyze_single_seed(seed):
    path = f"{OUTPUT_BASE}/seed_{seed}/samples.jsonl"
    data = load_data(path)
    valid = [d for d in data if len(d["gold"].get("entities", [])) > 0]
    n_gold_empty = len(data) - len(valid)
    print(f"  seed={seed}: {len(data)} total, {len(valid)} gold-nonempty, {n_gold_empty} gold-empty excluded")

    # --- Instance-level signals for rho ---
    consistency = compute_all_consistency_scores(valid, subtask="ner")
    sj_vals = consistency["soft_jaccard"]
    fk_vals = consistency["fleiss_kappa"]

    lp_vals, em_vals, vc_vals, f1_vals = [], [], [], []
    greedy_f1_vals = []
    for inst in valid:
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy", samples[0])
        lp_vals.append(compute_instance_lp(samples))
        em_vals.append(compute_instance_em_rate(samples))
        vc_vals.append(compute_instance_vc(samples))
        gf1 = per_instance_f1(greedy, gold, subtask="ner")
        greedy_f1_vals.append(gf1)
        f1_vals.append(gf1)

    conditional = [(i, inst) for i, inst in enumerate(valid) if greedy_f1_vals[i] > 0]
    n_cond = len(conditional)

    signals = {"SJ": sj_vals, "FK": fk_vals, "EM": em_vals, "VC": vc_vals, "LP": lp_vals}

    rho_results = {}
    for sig_name, sig_vals in signals.items():
        rho_full, p_full = safe_spearman(sig_vals, f1_vals)
        cond_sig = [sig_vals[i] for i, _ in conditional]
        cond_f1 = [f1_vals[i] for i, _ in conditional]
        rho_cond, p_cond = safe_spearman(cond_sig, cond_f1)
        rho_results[sig_name] = {
            "rho_full": rho_full, "p_full": p_full,
            "rho_cond": rho_cond, "p_cond": p_cond,
        }

    # --- Selection F1 ---
    greedy_f1s = []
    oracle_f1s = []
    signal_f1s = {s: [] for s in ["SJ", "FK", "EM", "VC", "LP"]}

    for inst in valid:
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy", samples[0])
        N = len(samples)

        g_f1 = per_instance_f1(greedy, gold, subtask="ner")
        greedy_f1s.append(g_f1)

        sample_f1s = [per_instance_f1(s, gold, subtask="ner") for s in samples]
        oracle_f1s.append(max(sample_f1s))

        sj_scores = compute_sample_sj_scores(inst)
        fk_scores, key_sets = compute_sample_surface_scores(inst)
        vc_scores = compute_sample_vc(key_sets, N)
        em_scores = compute_sample_em(key_sets)
        lp_scores = compute_sample_lp(inst)

        all_scores = {"SJ": sj_scores, "FK": fk_scores, "VC": vc_scores,
                      "EM": em_scores, "LP": lp_scores}
        for sig in signal_f1s:
            chosen = int(np.argmax(all_scores[sig]))
            signal_f1s[sig].append(sample_f1s[chosen])

    greedy_mean = float(np.mean(greedy_f1s))
    oracle_mean = float(np.mean(oracle_f1s))
    selection_results = {"greedy_f1": greedy_mean, "oracle_f1": oracle_mean}
    for sig in signal_f1s:
        selection_results[f"{sig}_selection_f1"] = float(np.mean(signal_f1s[sig]))
        selection_results[f"{sig}_delta_vs_greedy"] = float(np.mean(signal_f1s[sig])) - greedy_mean

    # --- LP range distribution ---
    lp_ranges = []
    lp_medians = []
    lp_iqrs = []
    for inst in valid:
        lps = [s.get("mean_logprob") for s in inst["samples"]
               if s.get("mean_logprob") is not None and np.isfinite(s.get("mean_logprob", float("nan")))]
        if len(lps) >= 2:
            lp_arr = np.array(lps)
            lp_range = float(np.max(lp_arr) - np.min(lp_arr))
            lp_ranges.append(lp_range)
            lp_medians.append(float(np.median(lp_arr)))
            q75, q25 = np.percentile(lp_arr, [75, 25])
            lp_iqrs.append(float(q75 - q25))

    lp_dist = {
        "n_instances_with_lp": len(lp_ranges),
        "range_median": float(np.median(lp_ranges)) if lp_ranges else float("nan"),
        "range_mean": float(np.mean(lp_ranges)) if lp_ranges else float("nan"),
        "range_q25": float(np.percentile(lp_ranges, 25)) if lp_ranges else float("nan"),
        "range_q75": float(np.percentile(lp_ranges, 75)) if lp_ranges else float("nan"),
        "range_iqr": float(np.percentile(lp_ranges, 75) - np.percentile(lp_ranges, 25)) if lp_ranges else float("nan"),
        "instance_lp_median_mean": float(np.mean(lp_medians)) if lp_medians else float("nan"),
        "instance_lp_iqr_median": float(np.median(lp_iqrs)) if lp_iqrs else float("nan"),
    }

    # Parse rate
    total_samples = sum(len(inst["samples"]) for inst in data)
    nonempty = sum(
        sum(1 for s in inst["samples"] if s.get("entities"))
        for inst in data
    )

    return {
        "seed": seed,
        "n_total": len(data),
        "n_gold_nonempty": len(valid),
        "n_gold_empty": n_gold_empty,
        "n_conditional": n_cond,
        "parse_rate_pct": round(nonempty / total_samples * 100, 2) if total_samples > 0 else 0,
        "rho": rho_results,
        "selection_f1": selection_results,
        "lp_distribution": lp_dist,
    }


def main():
    print("=" * 60)
    print("  Free-form CoNLL 4-seed analysis")
    print("=" * 60)

    seed_results = {}
    for seed in SEEDS:
        seed_results[seed] = analyze_single_seed(seed)

    # Aggregate across seeds
    signal_names = ["SJ", "FK", "EM", "VC", "LP"]

    agg_rho_full = {s: [] for s in signal_names}
    agg_rho_cond = {s: [] for s in signal_names}
    agg_sel_f1 = {s: [] for s in signal_names}
    agg_greedy = []
    agg_oracle = []
    agg_lp_range_median = []

    for seed in SEEDS:
        r = seed_results[seed]
        for s in signal_names:
            agg_rho_full[s].append(r["rho"][s]["rho_full"])
            agg_rho_cond[s].append(r["rho"][s]["rho_cond"])
            agg_sel_f1[s].append(r["selection_f1"][f"{s}_selection_f1"])
        agg_greedy.append(r["selection_f1"]["greedy_f1"])
        agg_oracle.append(r["selection_f1"]["oracle_f1"])
        agg_lp_range_median.append(r["lp_distribution"]["range_median"])

    # Load constrained baseline
    with open(CONSTRAINED_PATH) as f:
        constrained = json.load(f)

    constrained_rho = {
        "SJ": constrained["correlation_softjaccard_vs_f1_full"]["rho"],
        "FK": constrained["correlation_fleiss_vs_f1_full"]["rho"],
        "LP": constrained["logprob_baseline"]["full"]["rho"],
    }
    constrained_greedy = constrained["greedy_f1"]

    # Build summary
    summary = {
        "experiment": "exp_freeform_conll_4seed",
        "dataset": "conll2003",
        "model": "checkpoints/qwen3-8b-conll2003-merged",
        "n_samples": 8,
        "temperature": 1.0,
        "use_grammar": False,
        "seeds": SEEDS,
        "per_seed": {str(s): seed_results[s] for s in SEEDS},
        "aggregated": {
            "rho_full": {s: {"mean": float(np.mean(agg_rho_full[s])),
                             "std": float(np.std(agg_rho_full[s])),
                             "per_seed": agg_rho_full[s]}
                         for s in signal_names},
            "rho_conditional": {s: {"mean": float(np.mean(agg_rho_cond[s])),
                                    "std": float(np.std(agg_rho_cond[s])),
                                    "per_seed": agg_rho_cond[s]}
                                for s in signal_names},
            "selection_f1": {s: {"mean": float(np.mean(agg_sel_f1[s])),
                                 "std": float(np.std(agg_sel_f1[s])),
                                 "per_seed": agg_sel_f1[s]}
                             for s in signal_names},
            "greedy_f1": {"mean": float(np.mean(agg_greedy)),
                          "std": float(np.std(agg_greedy)),
                          "per_seed": agg_greedy},
            "oracle_f1": {"mean": float(np.mean(agg_oracle)),
                          "std": float(np.std(agg_oracle)),
                          "per_seed": agg_oracle},
            "lp_range_median": {"mean": float(np.mean(agg_lp_range_median)),
                                "std": float(np.std(agg_lp_range_median)),
                                "per_seed": agg_lp_range_median},
        },
        "constrained_baseline": {
            "rho_SJ": constrained_rho.get("SJ"),
            "rho_FK": constrained_rho.get("FK"),
            "rho_LP": constrained_rho.get("LP"),
            "greedy_f1": constrained_greedy,
        },
    }

    # Print summary table
    print("\n" + "=" * 80)
    print("AGGREGATED RESULTS (4-seed mean ± std)")
    print("=" * 80)
    print(f"\nGreedy F1:  {np.mean(agg_greedy):.4f} ± {np.std(agg_greedy):.4f}")
    print(f"Oracle F1:  {np.mean(agg_oracle):.4f} ± {np.std(agg_oracle):.4f}")
    print(f"LP range median: {np.mean(agg_lp_range_median):.4f} ± {np.std(agg_lp_range_median):.4f}")

    print(f"\n{'Signal':<6s} | {'ρ (full)':>12s} | {'ρ (cond)':>12s} | {'Sel F1':>12s} | {'Δ greedy':>10s}")
    print("-" * 65)
    for s in signal_names:
        rf = np.mean(agg_rho_full[s])
        rc = np.mean(agg_rho_cond[s])
        sf = np.mean(agg_sel_f1[s])
        delta = sf - np.mean(agg_greedy)
        print(f"{s:<6s} | {rf:>8.4f}±{np.std(agg_rho_full[s]):.4f} | "
              f"{rc:>8.4f}±{np.std(agg_rho_cond[s]):.4f} | "
              f"{sf:>8.4f}±{np.std(agg_sel_f1[s]):.4f} | {delta:>+.4f}")

    print(f"\nConstrained baseline (seed=42, N=8):")
    print(f"  Greedy F1: {constrained_greedy:.4f}")
    for sig, val in constrained_rho.items():
        print(f"  ρ_{sig}: {val:.4f}")

    out_path = f"{OUTPUT_BASE}/summary.json"
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2, default=lambda x: float(x) if isinstance(x, (np.floating,)) else x)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""E4 Ensemble Scaling Analysis for Frontier SC.

Computes cross-model ensemble metrics from 4 frontier model families:
GPT-5.5, Claude Sonnet 4, Gemini 2.5 Pro, DeepSeek.

Outputs:
- Single-model metrics summary
- Cross-model oracle (greedy-selection + sample-pool)
- Error correlation matrix
- Ensemble scaling curve (1/2/3/4-model combos)
- JSON report for paper table
"""

import json
import sys
import os
from itertools import combinations
from collections import Counter

import numpy as np
from scipy.stats import pearsonr, spearmanr

MODEL_DIRS = {
    "GPT-5.5": "frontier_sc_gpt55_fewnerd",
    "Claude-Sonnet4": "frontier_sc_claude_sonnet4",
    "Gemini-2.5Pro": "frontier_sc_gemini25pro",
    "DeepSeek": "frontier_sc_deepseek",
}

BASE_DIR = "/root/autodl-tmp/struct_self_consist_ie/output"


def load_results(path):
    records = {}
    with open(path) as f:
        for line in f:
            r = json.loads(line)
            records[r["id"]] = r
    return records


def instance_avg(values):
    return sum(values) / len(values) if values else 0.0


def main():
    # Load all models
    all_data = {}
    for model_name, dirname in MODEL_DIRS.items():
        path = os.path.join(BASE_DIR, dirname, "results.jsonl")
        if not os.path.exists(path):
            print(f"WARNING: {path} not found, skipping {model_name}")
            continue
        all_data[model_name] = load_results(path)
        print(f"Loaded {model_name}: {len(all_data[model_name])} instances")

    models = list(all_data.keys())
    print(f"\nModels loaded: {models}")

    # Find common instances
    id_sets = [set(all_data[m].keys()) for m in models]
    common_ids = id_sets[0]
    for s in id_sets[1:]:
        common_ids &= s
    common_ids = sorted(common_ids)
    print(f"Common instances: {len(common_ids)}")

    # ===== 1. Single-model metrics =====
    print("\n" + "=" * 70)
    print("TABLE 1: Single-Model Frontier SC Metrics (instance-avg F1)")
    print("=" * 70)
    print(f"{'Model':<20} {'Greedy':>8} {'MV':>8} {'Oracle':>8} {'MV-Gr':>8} {'Sel.Gap':>8} {'Degen%':>8}")
    print("-" * 70)

    model_greedy = {}
    model_mv = {}
    model_oracle = {}
    model_sample_f1s = {}

    for m in models:
        data = all_data[m]
        greedy = [data[iid]["greedy_f1"] for iid in common_ids]
        mv = [data[iid]["mv_f1"] for iid in common_ids]
        oracle = [data[iid]["oracle_f1"] for iid in common_ids]
        degen = sum(1 for iid in common_ids if data[iid]["is_degenerate"]) / len(common_ids)
        samples = {iid: data[iid]["sample_f1s"] for iid in common_ids}

        model_greedy[m] = greedy
        model_mv[m] = mv
        model_oracle[m] = oracle
        model_sample_f1s[m] = samples

        g, v, o = instance_avg(greedy), instance_avg(mv), instance_avg(oracle)
        print(f"{m:<20} {g:>8.4f} {v:>8.4f} {o:>8.4f} {v - g:>+8.4f} {o - v:>8.4f} {degen * 100:>7.1f}%")

    # ===== 2. Cross-model error correlation =====
    print("\n" + "=" * 70)
    print("TABLE 2: Cross-Model Error Correlation (Pearson r of greedy F1)")
    print("=" * 70)

    corr_matrix = {}
    model_pairs = list(combinations(models, 2))
    print(f"{'Pair':<40} {'Pearson r':>10} {'p-value':>10} {'Spearman ρ':>10}")
    print("-" * 70)

    for m1, m2 in model_pairs:
        g1 = model_greedy[m1]
        g2 = model_greedy[m2]
        pr, pp = pearsonr(g1, g2)
        sr, sp = spearmanr(g1, g2)
        print(f"{m1} × {m2:<20} {pr:>10.4f} {pp:>10.2e} {sr:>10.4f}")
        corr_matrix[(m1, m2)] = {"pearson_r": pr, "spearman_r": sr}

    mean_pearson = np.mean([v["pearson_r"] for v in corr_matrix.values()])
    print(f"\nMean Pearson r: {mean_pearson:.4f}")

    # ===== 3. Cross-model oracle analysis =====
    print("\n" + "=" * 70)
    print("TABLE 3: Cross-Model Ensemble Metrics")
    print("=" * 70)

    # Greedy model-selection oracle: for each instance, pick model with best greedy F1
    greedy_oracle = []
    for i, iid in enumerate(common_ids):
        best = max(model_greedy[m][i] for m in models)
        greedy_oracle.append(best)

    # Sample-pool oracle: max(all sample_f1s across all models)
    sample_pool_oracle = []
    for iid in common_ids:
        all_samples = []
        for m in models:
            all_samples.extend(model_sample_f1s[m][iid])
        sample_pool_oracle.append(max(all_samples))

    # Per-model oracle max (cross-model oracle from oracle_f1)
    cross_oracle = []
    for i, iid in enumerate(common_ids):
        best = max(model_oracle[m][i] for m in models)
        cross_oracle.append(best)

    best_single_greedy = max(instance_avg(model_greedy[m]) for m in models)
    best_single_mv = max(instance_avg(model_mv[m]) for m in models)
    best_single_oracle = max(instance_avg(model_oracle[m]) for m in models)

    print(f"{'Metric':<35} {'Value':>10} {'vs Best Single':>15}")
    print("-" * 60)
    print(f"{'Best single greedy':<35} {best_single_greedy:>10.4f} {'—':>15}")
    print(f"{'Best single MV':<35} {best_single_mv:>10.4f} {'—':>15}")
    print(f"{'Best single oracle':<35} {best_single_oracle:>10.4f} {'—':>15}")
    print(f"{'4-model greedy-selection oracle':<35} {instance_avg(greedy_oracle):>10.4f} {instance_avg(greedy_oracle) - best_single_greedy:>+14.4f}pp")
    print(f"{'4-model cross-oracle':<35} {instance_avg(cross_oracle):>10.4f} {instance_avg(cross_oracle) - best_single_oracle:>+14.4f}pp")
    print(f"{'4-model sample-pool oracle (N=32)':<35} {instance_avg(sample_pool_oracle):>10.4f} {instance_avg(sample_pool_oracle) - best_single_oracle:>+14.4f}pp")

    # ===== 4. Ensemble scaling curve =====
    print("\n" + "=" * 70)
    print("TABLE 4: Ensemble Scaling Curve (k-model combinations)")
    print("=" * 70)
    print(f"{'k':>3} {'Greedy Sel.':>12} {'Cross Oracle':>13} {'Sample Pool':>12} {'n_combos':>10}")
    print("-" * 55)

    scaling = {}
    for k in range(1, len(models) + 1):
        greedy_sels = []
        cross_oracles = []
        sample_pools = []

        for combo in combinations(models, k):
            gs_vals = []
            co_vals = []
            sp_vals = []
            for i, iid in enumerate(common_ids):
                gs_vals.append(max(model_greedy[m][i] for m in combo))
                co_vals.append(max(model_oracle[m][i] for m in combo))
                sp = []
                for m in combo:
                    sp.extend(model_sample_f1s[m][iid])
                sp_vals.append(max(sp))
            greedy_sels.append(instance_avg(gs_vals))
            cross_oracles.append(instance_avg(co_vals))
            sample_pools.append(instance_avg(sp_vals))

        n_combos = len(list(combinations(models, k)))
        gs_mean = np.mean(greedy_sels)
        co_mean = np.mean(cross_oracles)
        sp_mean = np.mean(sample_pools)
        print(f"{k:>3} {gs_mean:>12.4f} {co_mean:>13.4f} {sp_mean:>12.4f} {n_combos:>10}")
        scaling[k] = {
            "greedy_selection_mean": round(float(gs_mean), 4),
            "cross_oracle_mean": round(float(co_mean), 4),
            "sample_pool_oracle_mean": round(float(sp_mean), 4),
            "n_combinations": n_combos,
        }

    # ===== 5. Per-model complementarity =====
    print("\n" + "=" * 70)
    print("TABLE 5: Model Complementarity (% instances where model is uniquely best)")
    print("=" * 70)

    unique_best = {m: 0 for m in models}
    shared_best = 0
    for i, iid in enumerate(common_ids):
        best_f1 = max(model_greedy[m][i] for m in models)
        best_models = [m for m in models if abs(model_greedy[m][i] - best_f1) < 1e-6]
        if len(best_models) == 1:
            unique_best[best_models[0]] += 1
        else:
            shared_best += 1

    n = len(common_ids)
    print(f"{'Model':<25} {'Unique Best':>12} {'%':>8}")
    print("-" * 45)
    for m in models:
        print(f"{m:<25} {unique_best[m]:>12} {unique_best[m] / n * 100:>7.1f}%")
    print(f"{'Shared/tied':<25} {shared_best:>12} {shared_best / n * 100:>7.1f}%")

    # ===== 6. Ensemble gain decomposition =====
    print("\n" + "=" * 70)
    print("Ensemble Gain Decomposition")
    print("=" * 70)

    # For each instance: gain from cross-model = cross_oracle - best_single_model_oracle
    gains = []
    for i, iid in enumerate(common_ids):
        best_single = max(model_oracle[m][i] for m in models)
        # Actually cross_oracle == best_single per instance, since it's max
        # The real gain is at the aggregate level from picking different best models
        gains.append(max(model_greedy[m][i] for m in models) - max(model_greedy[m][i] for m in [models[0]]))

    print(f"Mean greedy F1 of best-model-per-instance: {instance_avg(greedy_oracle):.4f}")
    print(f"Mean greedy F1 of globally-best model:     {best_single_greedy:.4f}")
    print(f"Oracle model-selection gain:               {instance_avg(greedy_oracle) - best_single_greedy:+.4f}pp")

    # ===== Save JSON report =====
    report = {
        "analysis": "E4 Ensemble Scaling - Frontier SC",
        "dataset": "FewNERD (200 instances, seed=42)",
        "n_instances": len(common_ids),
        "models": models,
        "note": "F1 values are instance-average (not micro-F1). Text matching used for frontier models.",
        "single_model": {},
        "error_correlation": {},
        "cross_model_ensemble": {
            "best_single_greedy": round(best_single_greedy, 4),
            "best_single_mv": round(best_single_mv, 4),
            "best_single_oracle": round(best_single_oracle, 4),
            "greedy_selection_oracle_4model": round(instance_avg(greedy_oracle), 4),
            "cross_oracle_4model": round(instance_avg(cross_oracle), 4),
            "sample_pool_oracle_4model": round(instance_avg(sample_pool_oracle), 4),
        },
        "scaling_curve": scaling,
        "complementarity": {m: {"unique_best": unique_best[m], "pct": round(unique_best[m] / n * 100, 1)} for m in models},
    }

    for m in models:
        g = instance_avg(model_greedy[m])
        v = instance_avg(model_mv[m])
        o = instance_avg(model_oracle[m])
        d = sum(1 for iid in common_ids if all_data[m][iid]["is_degenerate"]) / len(common_ids)
        report["single_model"][m] = {
            "greedy_f1": round(g, 4),
            "mv_f1": round(v, 4),
            "oracle_f1": round(o, 4),
            "mv_gain_pp": round((v - g) * 100, 2),
            "selection_gap_pp": round((o - v) * 100, 2),
            "degeneracy_rate": round(d, 3),
        }

    for (m1, m2), vals in corr_matrix.items():
        report["error_correlation"][f"{m1} × {m2}"] = {
            "pearson_r": round(vals["pearson_r"], 4),
            "spearman_r": round(vals["spearman_r"], 4),
        }
    report["error_correlation"]["mean_pearson_r"] = round(mean_pearson, 4)

    out_path = os.path.join(BASE_DIR, "e4_ensemble_scaling_report.json")
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nReport saved to {out_path}")


if __name__ == "__main__":
    main()

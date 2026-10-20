#!/usr/bin/env python3
"""S1-only ablation: select top 300 items by S1 embedding score, run 2PL+gamma IRT.
Compare against RRF (S1+S2+S4) fusion baseline."""

import json
import logging
import os
import sys
import time

import numpy as np
from scipy.stats import kendalltau

sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
from run_irt_calibration import (
    prepare_stan_data,
    fit_stan_model,
    check_convergence,
    posterior_predictive_check,
    extract_results,
    STAN_MODELS,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
SIGNALS_DIR = "/root/autodl-tmp/exp002/signals"
OUTPUT_DIR = "/root/autodl-tmp/exp006/s1_only_ablation"
MAX_ITEMS = 300

# J=16 model definitions: (eval_dirname, signal_dirname, scale, dosage)
MODELS = [
    ("Qwen2.5-1.5B_d000_s123_aligned", "Qwen2.5-1.5B_d000_s123", "1.5B", 0),
    ("Qwen2.5-1.5B_d000_s42_aligned", "Qwen2.5-1.5B_d000_s42", "1.5B", 0),
    ("Qwen2.5-1.5B_d005_s123_aligned", "Qwen2.5-1.5B_d005_s123", "1.5B", 5),
    ("Qwen2.5-1.5B_d005_s42_aligned", "Qwen2.5-1.5B_d005_s42", "1.5B", 5),
    ("Qwen2.5-1.5B_d025_s123_aligned", "Qwen2.5-1.5B_d025_s123", "1.5B", 25),
    ("Qwen2.5-1.5B_d025_s42_aligned", "Qwen2.5-1.5B_d025_s42", "1.5B", 25),
    ("Qwen2.5-1.5B_d100_s123_aligned", "Qwen2.5-1.5B_d100_s123", "1.5B", 100),
    ("Qwen2.5-1.5B_d100_s42_aligned", "Qwen2.5-1.5B_d100_s42", "1.5B", 100),
    ("Qwen2.5-3B_d000_s123_aligned", "Qwen2.5-3B_d000_s123_a32", "3B", 0),
    ("Qwen2.5-3B_d000_s42_a32_aligned", "Qwen2.5-3B_d000_a32_s42", "3B", 0),
    ("Qwen2.5-3B_d005_s123_aligned", "Qwen2.5-3B_d005_s123", "3B", 5),
    ("Qwen2.5-3B_d005_s42_a32_aligned", "Qwen2.5-3B_d005_a32_s42", "3B", 5),
    ("Qwen2.5-3B_d025_s123_aligned", "Qwen2.5-3B_d025_s123", "3B", 25),
    ("Qwen2.5-3B_d025_v3_s42_aligned", "Qwen2.5-3B_d025_v3_s42", "3B", 25),
    ("Qwen2.5-3B_d100_a32_s123_aligned", "Qwen2.5-3B_d100_a32_s123", "3B", 100),
    ("Qwen2.5-3B_d100_a32_s42_aligned", "Qwen2.5-3B_d100_a32_s42", "3B", 100),
]


def load_responses(benchmark):
    """Load binary response matrix for all J=16 models."""
    responses = []
    for eval_dir, _, _, _ in MODELS:
        path = os.path.join(EVAL_DIR, eval_dir, "eval_results.json")
        with open(path) as f:
            data = json.load(f)
        per_item = data["benchmarks"][benchmark]["per_item"]
        responses.append([1 if item["correct"] else 0 for item in per_item])
    return np.array(responses, dtype=int)


def load_s1_signals(benchmark):
    """Load S1 embedding scores for all J=16 models, return matrix [16, n_items]."""
    s1_matrix = []
    for _, sig_dir, _, _ in MODELS:
        path = os.path.join(SIGNALS_DIR, sig_dir, f"signals_merged_{benchmark}.json")
        with open(path) as f:
            items = json.load(f)
        scores = [item.get("s1_embedding", 0.0) or 0.0 for item in items]
        s1_matrix.append(scores)
    return np.array(s1_matrix, dtype=float)


def run_ablation(benchmark):
    log.info("=" * 60)
    log.info("S1-only ablation: %s", benchmark)

    responses = load_responses(benchmark)
    s1_matrix = load_s1_signals(benchmark)
    n_models, n_items = responses.shape
    log.info("Loaded: %d models x %d items", n_models, n_items)

    mean_s1 = s1_matrix.mean(axis=0)
    log.info("S1 stats: mean=%.4f, max=%.4f, min=%.4f", mean_s1.mean(), mean_s1.max(), mean_s1.min())

    top_indices = np.argsort(-mean_s1)[:MAX_ITEMS]
    top_indices_sorted = np.sort(top_indices)
    log.info("Selected top %d items by mean S1 score", MAX_ITEMS)
    log.info("  S1 range of selected: [%.4f, %.4f]",
             mean_s1[top_indices_sorted].min(), mean_s1[top_indices_sorted].max())

    y = responses[:, top_indices_sorted]
    exposure = s1_matrix[:, top_indices_sorted]
    log.info("Response matrix: %s, Exposure matrix: %s", y.shape, exposure.shape)
    log.info("Exposure stats: mean=%.4f, max=%.4f", exposure.mean(), exposure.max())

    stan_data = prepare_stan_data(y, exposure, model_type="2pl_gamma")
    fit, elapsed = fit_stan_model(
        STAN_MODELS["2pl_gamma"], stan_data,
        chains=4, iter_warmup=1000, iter_sampling=1000,
        adapt_delta=0.95, max_treedepth=12, seed=42, parallel_chains=4,
    )
    log.info("Stan fit completed in %.1fs", elapsed)

    diagnostics = check_convergence(fit)
    ppc = posterior_predictive_check(fit, y)
    results = extract_results(fit, y, "2pl_gamma")
    log.info("Diagnostics: R_hat=%.4f, ESS=%.0f, div=%d",
             diagnostics["max_rhat"], diagnostics["min_ess"], diagnostics["divergent_count"])
    log.info("PPP=%.4f", ppc["overall_ppp"])

    dosages = np.array([d for _, _, _, d in MODELS])
    scales = [s for _, _, s, _ in MODELS]
    raw_acc = y.mean(axis=1)
    cal_mean = np.array(results["calibrated_scores"]["mean"])

    ground_truth = np.empty(n_models)
    for i, (d, sc) in enumerate(zip(dosages, scales)):
        if d == 0:
            ground_truth[i] = raw_acc[i]
        else:
            same_scale_d0 = [j for j in range(n_models) if dosages[j] == 0 and scales[j] == sc]
            ground_truth[i] = float(raw_acc[same_scale_d0].mean())

    tau_val, tau_p = kendalltau(cal_mean, ground_truth)
    mae = float(np.mean(np.abs(cal_mean - ground_truth)))
    log.info("tau=%.4f (p=%.4f), MAE=%.4f", tau_val, tau_p, mae)

    gamma = results.get("gamma", {})
    if gamma:
        log.info("gamma: mean=%.4f, CI=[%.4f, %.4f]", gamma["mean"], gamma["q025"], gamma["q975"])

    return {
        "benchmark": benchmark,
        "method": "s1_only_top300",
        "model_type": "2pl_gamma",
        "n_models": n_models,
        "n_items": MAX_ITEMS,
        "original_n_items": n_items,
        "selection": "top_300_by_mean_s1",
        "fit_time_sec": round(elapsed, 1),
        "diagnostics": diagnostics,
        "posterior_predictive": ppc,
        "gamma": gamma,
        "tau": round(float(tau_val), 4),
        "tau_p": float(tau_p),
        "mae": round(mae, 4),
        "raw_accuracy": raw_acc.tolist(),
        "calibrated_scores": results["calibrated_scores"],
        "ground_truth": ground_truth.tolist(),
        "s1_threshold": float(mean_s1[top_indices_sorted].min()),
        "models": [
            {"eval_dir": e, "signal_dir": s, "scale": sc, "dosage": d}
            for e, s, sc, d in MODELS
        ],
    }


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_results = {}

    for bench in ["mmlu", "arc_challenge"]:
        result = run_ablation(bench)
        all_results[bench] = result

        bench_dir = os.path.join(OUTPUT_DIR, bench)
        os.makedirs(bench_dir, exist_ok=True)
        with open(os.path.join(bench_dir, "s1_only_irt_results.json"), "w") as f:
            json.dump(result, f, indent=2)

    print("\n" + "=" * 80)
    print("S1-ONLY ABLATION RESULTS (2PL+gamma, top 300 by mean S1)")
    print("=" * 80)
    print(f"{'Bench':<16} {'N_mod':>5} {'N_item':>6} {'tau':>8} {'MAE':>8} "
          f"{'gamma':>8} {'95% CI':>20} {'PPP':>6} {'R_hat':>6} {'ESS':>6}")
    print("-" * 100)

    rrf_baselines = {
        "mmlu": {"tau": 0.731, "mae": 0.0091, "gamma": 0.698, "ci": "[-0.42, 1.81]"},
        "arc_challenge": {"tau": 0.609, "mae": 0.0196, "gamma": 0.727, "ci": "[0.02, 1.44]"},
    }

    for bench in ["mmlu", "arc_challenge"]:
        r = all_results[bench]
        g = r["gamma"]
        d = r["diagnostics"]
        print(f"{bench:<16} {r['n_models']:>5} {r['n_items']:>6} "
              f"{r['tau']:>8.4f} {r['mae']:>8.4f} "
              f"{g['mean']:>8.4f} [{g['q025']:.2f}, {g['q975']:.2f}] "
              f"{r['posterior_predictive']['overall_ppp']:>6.4f} "
              f"{d['max_rhat']:>6.4f} {d['min_ess']:>6.0f}")

    print("\n" + "=" * 80)
    print("COMPARISON: S1-only vs RRF baseline")
    print("=" * 80)
    print(f"{'Bench':<16} {'Metric':<8} {'S1-only':>10} {'RRF':>10} {'Delta':>10}")
    print("-" * 60)
    for bench in ["mmlu", "arc_challenge"]:
        r = all_results[bench]
        bl = rrf_baselines[bench]
        print(f"{bench:<16} {'tau':<8} {r['tau']:>10.4f} {bl['tau']:>10.4f} {r['tau']-bl['tau']:>+10.4f}")
        print(f"{'':16} {'MAE':<8} {r['mae']:>10.4f} {bl['mae']:>10.4f} {r['mae']-bl['mae']:>+10.4f}")
        print(f"{'':16} {'gamma':<8} {r['gamma']['mean']:>10.4f} {bl['gamma']:>10.4f} {r['gamma']['mean']-bl['gamma']:>+10.4f}")

    with open(os.path.join(OUTPUT_DIR, "s1_only_ablation_results.json"), "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()

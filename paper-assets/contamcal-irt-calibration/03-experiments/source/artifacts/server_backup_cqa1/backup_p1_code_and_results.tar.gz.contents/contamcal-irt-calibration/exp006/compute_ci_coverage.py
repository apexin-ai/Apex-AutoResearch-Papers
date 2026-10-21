#!/usr/bin/env python3
"""Compute posterior predictive CI coverage for 2PL+gamma IRT fits.

Re-fits the same models as cross_family_v5 (MMLU + ARC) and computes:
- Model-level 50%/80%/95% CI coverage
- Item-bin-level coverage (by predicted probability decile)
"""

import json
import logging
import sys
import time
from pathlib import Path

import numpy as np
from scipy.special import expit

sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
sys.path.insert(0, "/root/contamcal-irt-calibration/exp003")

import rrf_aggregation as rrf
from run_irt_calibration import (
    load_pooled_eval_results,
    prepare_stan_data,
    fit_stan_model,
    check_convergence,
    STAN_MODELS,
)
from run_pooled_rrf_irt import (
    build_rrf_exposure_matrix,
    filter_models_for_benchmark,
    load_rrf_exposure,
    strip_aligned,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

OUTPUT_DIR = Path("/root/autodl-tmp/exp006/ci_coverage_analysis")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
EXPOSURE_FILE = "/root/autodl-tmp/exp006/cross_family_v5/exposure_scores_v5.json"
BENCHMARKS = ["mmlu", "arc_challenge"]
SCALES = ["1.5B", "3B"]
MODEL_TYPE = "2pl_gamma"
STAN_FILE = STAN_MODELS[MODEL_TYPE]
MAX_ITEMS = 300
D045_EXCLUDE = {"mmlu": {"0.5B"}, "arc_challenge": {"0.5B"}}


class Args:
    chains = 4
    warmup = 1000
    samples = 1000
    adapt_delta = 0.95
    max_treedepth = 12
    seed = 42
    parallel_chains = 4


def compute_predicted_accuracy_draws(fit, exposure, n_models, n_items):
    """Compute predicted accuracy per model per draw (WITH exposure effect).
    
    Returns: (n_draws, n_models) array of predicted accuracies.
    """
    theta = fit.stan_variable("theta")   # (n_draws, n_models)
    a = fit.stan_variable("a")           # (n_draws, n_items)
    b = fit.stan_variable("b")           # (n_draws, n_items)
    gamma = fit.stan_variable("gamma")   # (n_draws,)
    
    n_draws = theta.shape[0]
    pred_acc = np.zeros((n_draws, n_models))
    
    for s in range(n_draws):
        # eta[j,i] = a[i] * (theta[j] - b[i]) + gamma * exposure[j,i]
        # vectorized: (n_models, n_items)
        eta = a[s][np.newaxis, :] * (theta[s][:, np.newaxis] - b[s][np.newaxis, :]) + gamma[s] * exposure
        p = expit(eta)  # (n_models, n_items)
        pred_acc[s] = p.mean(axis=1)
    
    return pred_acc


def compute_item_level_predicted_draws(fit, exposure, n_models, n_items):
    """Compute predicted P(correct) per item-model pair per draw.
    
    Returns: (n_draws, n_models, n_items)
    """
    theta = fit.stan_variable("theta")   # (n_draws, n_models)
    a = fit.stan_variable("a")           # (n_draws, n_items)
    b = fit.stan_variable("b")           # (n_draws, n_items)
    gamma = fit.stan_variable("gamma")   # (n_draws,)
    
    n_draws = theta.shape[0]
    # Memory-efficient: compute in chunks
    chunk_size = 200
    pred_all = np.zeros((n_draws, n_models, n_items), dtype=np.float32)
    
    for start in range(0, n_draws, chunk_size):
        end = min(start + chunk_size, n_draws)
        for s in range(start, end):
            eta = a[s][np.newaxis, :] * (theta[s][:, np.newaxis] - b[s][np.newaxis, :]) + gamma[s] * exposure
            pred_all[s] = expit(eta)
    
    return pred_all


def compute_model_level_coverage(pred_acc_draws, observed_acc):
    """Compute CI coverage at model level.
    
    pred_acc_draws: (n_draws, n_models)
    observed_acc: (n_models,) observed mean accuracy per model
    """
    n_models = len(observed_acc)
    
    # Compute quantiles per model
    q025 = np.percentile(pred_acc_draws, 2.5, axis=0)
    q975 = np.percentile(pred_acc_draws, 97.5, axis=0)
    q10 = np.percentile(pred_acc_draws, 10, axis=0)
    q90 = np.percentile(pred_acc_draws, 90, axis=0)
    q25 = np.percentile(pred_acc_draws, 25, axis=0)
    q75 = np.percentile(pred_acc_draws, 75, axis=0)
    
    # Coverage: fraction of models where observed falls within CI
    cov_95 = np.mean((observed_acc >= q025) & (observed_acc <= q975))
    cov_80 = np.mean((observed_acc >= q10) & (observed_acc <= q90))
    cov_50 = np.mean((observed_acc >= q25) & (observed_acc <= q75))
    
    # Per-model details
    details = []
    for j in range(n_models):
        details.append({
            "obs": round(float(observed_acc[j]), 4),
            "pred_mean": round(float(pred_acc_draws[:, j].mean()), 4),
            "ci95": [round(float(q025[j]), 4), round(float(q975[j]), 4)],
            "ci80": [round(float(q10[j]), 4), round(float(q90[j]), 4)],
            "ci50": [round(float(q25[j]), 4), round(float(q75[j]), 4)],
            "in_95": bool((observed_acc[j] >= q025[j]) & (observed_acc[j] <= q975[j])),
            "in_80": bool((observed_acc[j] >= q10[j]) & (observed_acc[j] <= q90[j])),
            "in_50": bool((observed_acc[j] >= q25[j]) & (observed_acc[j] <= q75[j])),
        })
    
    return {
        "coverage_50": round(float(cov_50), 4),
        "coverage_80": round(float(cov_80), 4),
        "coverage_95": round(float(cov_95), 4),
        "nominal_50": 0.50,
        "nominal_80": 0.80,
        "nominal_95": 0.95,
        "n_models": n_models,
        "per_model": details,
    }


def compute_item_bin_coverage(pred_item_draws, y, n_bins=10):
    """Coverage by predicted probability bin (aggregated across models).
    
    pred_item_draws: (n_draws, n_models, n_items) 
    y: (n_models, n_items) binary response matrix
    """
    n_draws, n_models, n_items = pred_item_draws.shape
    
    # Posterior mean predicted P(correct) per cell
    pred_mean = pred_item_draws.mean(axis=0)  # (n_models, n_items)
    
    # Flatten all cells
    pred_flat = pred_mean.flatten()
    obs_flat = y.flatten().astype(float)
    
    # Bin by predicted probability
    bin_edges = np.linspace(0, 1, n_bins + 1)
    bin_results = []
    
    for k in range(n_bins):
        mask = (pred_flat >= bin_edges[k]) & (pred_flat < bin_edges[k+1])
        if k == n_bins - 1:
            mask = (pred_flat >= bin_edges[k]) & (pred_flat <= bin_edges[k+1])
        
        if mask.sum() == 0:
            continue
        
        # Get indices of cells in this bin
        indices = np.where(mask)[0]
        n_cells = len(indices)
        
        # Observed proportion in this bin
        obs_prop = obs_flat[indices].mean()
        
        # Posterior distribution of mean predicted probability in this bin
        # For each draw, compute mean predicted prob across cells in this bin
        bin_pred_draws = np.zeros(n_draws)
        for s in range(n_draws):
            pred_s_flat = pred_item_draws[s].flatten()
            bin_pred_draws[s] = pred_s_flat[indices].mean()
        
        q025 = np.percentile(bin_pred_draws, 2.5)
        q975 = np.percentile(bin_pred_draws, 97.5)
        q10 = np.percentile(bin_pred_draws, 10)
        q90 = np.percentile(bin_pred_draws, 90)
        q25 = np.percentile(bin_pred_draws, 25)
        q75 = np.percentile(bin_pred_draws, 75)
        
        bin_results.append({
            "bin": f"[{bin_edges[k]:.1f}, {bin_edges[k+1]:.1f})",
            "n_cells": int(n_cells),
            "obs_prop": round(float(obs_prop), 4),
            "pred_mean": round(float(bin_pred_draws.mean()), 4),
            "ci95": [round(float(q025), 4), round(float(q975), 4)],
            "ci80": [round(float(q10), 4), round(float(q90), 4)],
            "ci50": [round(float(q25), 4), round(float(q75), 4)],
            "in_95": bool((obs_prop >= q025) & (obs_prop <= q975)),
            "in_80": bool((obs_prop >= q10) & (obs_prop <= q90)),
            "in_50": bool((obs_prop >= q25) & (obs_prop <= q75)),
        })
    
    n_bins_actual = len(bin_results)
    cov_95 = sum(1 for b in bin_results if b["in_95"]) / n_bins_actual if n_bins_actual > 0 else 0
    cov_80 = sum(1 for b in bin_results if b["in_80"]) / n_bins_actual if n_bins_actual > 0 else 0
    cov_50 = sum(1 for b in bin_results if b["in_50"]) / n_bins_actual if n_bins_actual > 0 else 0
    
    return {
        "coverage_50": round(cov_50, 4),
        "coverage_80": round(cov_80, 4),
        "coverage_95": round(cov_95, 4),
        "n_bins": n_bins_actual,
        "bins": bin_results,
    }


def run_benchmark_coverage(bench, models_f, resp_f, rrf_data, args):
    """Fit IRT and compute CI coverage for one benchmark."""
    n_models, n_items_orig = resp_f.shape
    
    # Subsample items if needed (same seed as original)
    subsample_idx = None
    if n_items_orig > MAX_ITEMS:
        np.random.seed(42)
        subsample_idx = np.sort(np.random.choice(n_items_orig, MAX_ITEMS, replace=False))
        resp_f = resp_f[:, subsample_idx]
    
    n_items = resp_f.shape[1]
    
    # Build exposure matrix
    exposure = build_rrf_exposure_matrix(models_f, rrf_data, bench, n_items_orig)
    if subsample_idx is not None:
        exposure = exposure[:, subsample_idx]
    
    log.info("[%s] N_models=%d, N_items=%d, exposure_mean=%.4f",
             bench, n_models, n_items, exposure.mean())
    
    # Fit IRT
    stan_data = prepare_stan_data(resp_f, exposure, MODEL_TYPE)
    fit, elapsed = fit_stan_model(
        STAN_FILE, stan_data,
        chains=args.chains,
        iter_warmup=args.warmup,
        iter_sampling=args.samples,
        adapt_delta=args.adapt_delta,
        max_treedepth=args.max_treedepth,
        seed=args.seed,
        parallel_chains=args.parallel_chains,
    )
    
    diag = check_convergence(fit)
    log.info("[%s] Fit in %.1fs. Rhat=%.4f, ESS=%.0f, div=%d",
             bench, elapsed, diag["max_rhat"], diag["min_ess"], diag["divergent_count"])
    
    # Compute model-level predicted accuracy draws (WITH exposure)
    log.info("[%s] Computing model-level predicted accuracy draws...", bench)
    pred_acc_draws = compute_predicted_accuracy_draws(fit, exposure, n_models, n_items)
    
    # Observed accuracy per model
    observed_acc = resp_f.mean(axis=1)
    
    # Model-level coverage
    model_coverage = compute_model_level_coverage(pred_acc_draws, observed_acc)
    
    # Item-bin-level coverage (compute full item-level draws)
    log.info("[%s] Computing item-level predicted draws for bin coverage...", bench)
    pred_item_draws = compute_item_level_predicted_draws(fit, exposure, n_models, n_items)
    item_bin_coverage = compute_item_bin_coverage(pred_item_draws, resp_f)
    
    # Also compute calibrated (exposure=0) coverage
    log.info("[%s] Computing calibrated (exposure=0) coverage...", bench)
    cal_draws = fit.stan_variable("calibrated_score")  # (n_draws, n_models)
    cal_coverage = compute_model_level_coverage(cal_draws, observed_acc)
    
    # Gamma summary
    gamma_draws = fit.stan_variable("gamma")
    gamma_info = {
        "mean": round(float(np.mean(gamma_draws)), 4),
        "sd": round(float(np.std(gamma_draws)), 4),
        "q025": round(float(np.percentile(gamma_draws, 2.5)), 4),
        "q975": round(float(np.percentile(gamma_draws, 97.5)), 4),
    }
    
    return {
        "benchmark": bench,
        "n_models": n_models,
        "n_items": n_items,
        "model_type": MODEL_TYPE,
        "fit_time_sec": round(elapsed, 1),
        "diagnostics": diag,
        "gamma": gamma_info,
        "model_level_coverage_predicted": model_coverage,
        "model_level_coverage_calibrated": cal_coverage,
        "item_bin_coverage": item_bin_coverage,
        "models": [m["dirname"] for m in models_f],
    }


def main():
    args = Args()
    
    # Load data
    rrf_data = load_rrf_exposure(EXPOSURE_FILE)
    log.info("Loaded RRF exposure for %d models", len(rrf_data))
    
    data = load_pooled_eval_results(EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True)
    log.info("Loaded %d models from eval_results", len(data["models"]))
    
    all_results = {}
    
    for bench in BENCHMARKS:
        if bench not in data["benchmarks"]:
            log.warning("Benchmark %s not in eval data, skipping", bench)
            continue
        
        bd = data["benchmarks"][bench]
        exclude_scales = D045_EXCLUDE.get(bench, set())
        
        # Filter models
        models_f, dosages_f, resp_f = filter_models_for_benchmark(
            data["models"], data["dosages"], bd["responses"],
            rrf_data, bench, exclude_scales)
        
        if len(models_f) < 3:
            log.warning("Too few models for %s, skipping", bench)
            continue
        
        log.info("=" * 60)
        log.info("BENCHMARK: %s (N=%d)", bench, len(models_f))
        log.info("=" * 60)
        
        result = run_benchmark_coverage(bench, models_f, resp_f, rrf_data, args)
        all_results[bench] = result
        
        # Save per-benchmark
        bench_dir = OUTPUT_DIR / bench
        bench_dir.mkdir(parents=True, exist_ok=True)
        with open(bench_dir / "ci_coverage.json", "w") as f:
            json.dump(result, f, indent=2)
    
    # Summary
    print("\n" + "=" * 80)
    print("POSTERIOR PREDICTIVE CI COVERAGE ANALYSIS")
    print("=" * 80)
    print(f"\n{'Bench':<16} {'N_mod':>5} {'N_item':>6} | "
          f"{'Pred 50%':>8} {'Pred 80%':>8} {'Pred 95%':>8} | "
          f"{'Cal 50%':>7} {'Cal 80%':>7} {'Cal 95%':>7}")
    print("-" * 90)
    
    for bench in BENCHMARKS:
        if bench not in all_results:
            continue
        r = all_results[bench]
        pc = r["model_level_coverage_predicted"]
        cc = r["model_level_coverage_calibrated"]
        print(f"{bench:<16} {r['n_models']:>5} {r['n_items']:>6} | "
              f"{pc['coverage_50']:>8.4f} {pc['coverage_80']:>8.4f} {pc['coverage_95']:>8.4f} | "
              f"{cc['coverage_50']:>7.4f} {cc['coverage_80']:>7.4f} {cc['coverage_95']:>7.4f}")
    
    print(f"\n{'Bench':<16} | Item-bin coverage (by predicted prob decile):")
    print(f"{'':16} | {'50%':>8} {'80%':>8} {'95%':>8}")
    print("-" * 60)
    for bench in BENCHMARKS:
        if bench not in all_results:
            continue
        ibc = all_results[bench]["item_bin_coverage"]
        print(f"{bench:<16} | {ibc['coverage_50']:>8.4f} {ibc['coverage_80']:>8.4f} {ibc['coverage_95']:>8.4f}")
    
    print(f"\nNominal: 50%=0.50, 80%=0.80, 95%=0.95")
    print(f"\nResults saved to: {OUTPUT_DIR}")
    
    # Save combined
    with open(OUTPUT_DIR / "all_coverage_results.json", "w") as f:
        json.dump(all_results, f, indent=2)


if __name__ == "__main__":
    main()

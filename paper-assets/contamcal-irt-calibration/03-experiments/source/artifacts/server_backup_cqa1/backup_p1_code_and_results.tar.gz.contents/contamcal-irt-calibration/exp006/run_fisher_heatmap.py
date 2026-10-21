#!/usr/bin/env python3
"""
Fisher Info N × Benchmark Identifiability Heatmap (W4 fixed version).
Monte Carlo simulation: 200 reps per (N, benchmark) cell.
Uses 2PL+γ model with Laplace approximation for speed.

Output: /root/autodl-tmp/exp006/fisher_info_heatmap/
"""

import json
import os
import sys
import time
import numpy as np
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
from scipy.special import expit
from scipy.stats import norm

import cmdstanpy

STAN_FILE = "/root/contamcal-irt-calibration/stan_models/contam_irt_2pl_gamma.stan"
OUTPUT_DIR = Path("/root/autodl-tmp/exp006/fisher_info_heatmap")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

N_ITEMS = 300
N_REPS = 200
GAMMA_TRUE = 0.5
N_VALUES = [5, 10, 16, 24, 30, 50]

# Benchmark-specific parameters calibrated from real IRT fits
# Each benchmark has different item characteristics and exposure signal quality
BENCHMARKS = {
    "mmlu": {
        "n_items": 300,
        "a_loc": 0.0, "a_scale": 0.4,      # moderate discrimination
        "b_loc": 0.0, "b_scale": 0.8,       # centered difficulty
        "exposure_auc": 0.75,                # moderate signal quality
        "exposure_rate": 0.30,               # 30% items contaminated
    },
    "arc": {
        "n_items": 300,
        "a_loc": 0.1, "a_scale": 0.5,       # slightly higher discrimination
        "b_loc": 0.3, "b_scale": 1.0,       # harder items
        "exposure_auc": 0.80,                # better signal (fewer items, easier to detect)
        "exposure_rate": 0.30,
    },
    "gsm8k": {
        "n_items": 300,
        "a_loc": -0.1, "a_scale": 0.6,      # more variable discrimination
        "b_loc": 0.5, "b_scale": 1.2,       # hardest items
        "exposure_auc": 0.70,                # weaker signal (open-ended format)
        "exposure_rate": 0.30,
    },
}


def generate_exposure(rng, n_models, n_items, target_auc, exposure_rate):
    """Generate binary ground truth + noisy exposure scores."""
    gt = rng.binomial(1, exposure_rate, (n_models, n_items)).astype(float)
    z = norm.ppf(target_auc)
    if z <= 0:
        sigma = 1e6
    else:
        sigma = 1.0 / (np.sqrt(2) * z)
    noise = rng.standard_normal((n_models, n_items)) * sigma
    score = gt + noise
    return score


def generate_data(rng, n_models, bench_params):
    """Generate synthetic response matrix under 2PL+γ."""
    n_items = bench_params["n_items"]
    
    theta = rng.standard_normal(n_models)
    a = np.exp(rng.normal(bench_params["a_loc"], bench_params["a_scale"], n_items))
    b = rng.normal(bench_params["b_loc"], bench_params["b_scale"], n_items)
    
    exposure = generate_exposure(
        rng, n_models, n_items,
        bench_params["exposure_auc"],
        bench_params["exposure_rate"]
    )
    
    eta = a[None, :] * (theta[:, None] - b[None, :]) + GAMMA_TRUE * exposure
    prob = expit(eta)
    y = rng.binomial(1, prob)
    
    return {
        "N_models": n_models,
        "N_items": n_items,
        "y": y.tolist(),
        "exposure": exposure.tolist(),
    }, {"theta": theta, "a": a, "b": b}


def fit_one_rep(args):
    """Fit a single rep using MCMC (2 chains, short warmup)."""
    n_models, bench_name, bench_params, seed = args
    
    rng = np.random.default_rng(seed)
    stan_data, true_params = generate_data(rng, n_models, bench_params)
    
    try:
        model = cmdstanpy.CmdStanModel(stan_file=STAN_FILE)
        
        # Use short MCMC for reliable posteriors (Laplace can fail for small N)
        fit = model.sample(
            data=stan_data,
            chains=2,
            iter_warmup=300,
            iter_sampling=300,
            adapt_delta=0.9,
            max_treedepth=10,
            seed=seed,
            show_progress=False,
            show_console=False,
        )
        
        gamma_draws = fit.stan_variable("gamma")
        gamma_mean = float(np.mean(gamma_draws))
        gamma_sd = float(np.std(gamma_draws))
        gamma_q025 = float(np.percentile(gamma_draws, 2.5))
        gamma_q975 = float(np.percentile(gamma_draws, 97.5))
        ci_width = gamma_q975 - gamma_q025
        ci_covers = float(gamma_q025 <= GAMMA_TRUE <= gamma_q975)
        ci_excludes_zero = float(gamma_q025 > 0)
        gamma_bias = gamma_mean - GAMMA_TRUE
        
        # Convergence check
        summary = fit.summary()
        gamma_rhat = float(summary.loc["gamma", "R_hat"]) if "gamma" in summary.index else None
        
        return {
            "success": True,
            "gamma_mean": gamma_mean,
            "gamma_sd": gamma_sd,
            "ci_width": ci_width,
            "ci_covers": ci_covers,
            "ci_excludes_zero": ci_excludes_zero,
            "gamma_bias": gamma_bias,
            "gamma_rhat": gamma_rhat,
        }
    except Exception as e:
        return {"success": False, "error": str(e)[:200]}


def run_condition(n_models, bench_name, bench_params, n_reps, n_workers=4):
    """Run all reps for one (N, benchmark) condition."""
    condition_id = f"{bench_name}_N{n_models}"
    result_file = OUTPUT_DIR / f"{condition_id}.json"
    
    # Check if already done
    if result_file.exists():
        with open(result_file) as f:
            existing = json.load(f)
        if existing.get("n_reps_ok", 0) >= n_reps:
            print(f"  {condition_id}: already complete ({existing['n_reps_ok']} reps), skipping")
            sys.stdout.flush()
            return existing
    
    print(f"  Running {condition_id} ({n_reps} reps, {n_workers} workers)...")
    sys.stdout.flush()
    
    seeds = list(range(1000, 1000 + n_reps))
    args_list = [(n_models, bench_name, bench_params, s) for s in seeds]
    
    results = []
    t0 = time.time()
    
    with ProcessPoolExecutor(max_workers=n_workers) as executor:
        futures = [executor.submit(fit_one_rep, a) for a in args_list]
        for i, future in enumerate(as_completed(futures)):
            r = future.result()
            results.append(r)
            if (i + 1) % 20 == 0:
                elapsed = time.time() - t0
                eta = elapsed / (i + 1) * (n_reps - i - 1)
                print(f"    {condition_id}: {i+1}/{n_reps} done, ETA {eta:.0f}s")
                sys.stdout.flush()
    
    elapsed = time.time() - t0
    ok_results = [r for r in results if r["success"]]
    
    if not ok_results:
        summary = {"condition_id": condition_id, "n_reps_ok": 0, "error": "all failed"}
    else:
        ci_widths = [r["ci_width"] for r in ok_results]
        summary = {
            "condition_id": condition_id,
            "benchmark": bench_name,
            "n_models": n_models,
            "n_reps_ok": len(ok_results),
            "n_reps_failed": len(results) - len(ok_results),
            "gamma_true": GAMMA_TRUE,
            "gamma_mean_avg": round(float(np.mean([r["gamma_mean"] for r in ok_results])), 4),
            "gamma_mean_std": round(float(np.std([r["gamma_mean"] for r in ok_results])), 4),
            "gamma_bias_avg": round(float(np.mean([r["gamma_bias"] for r in ok_results])), 4),
            "gamma_rmse": round(float(np.sqrt(np.mean([r["gamma_bias"]**2 for r in ok_results]))), 4),
            "ci95_width_avg": round(float(np.mean(ci_widths)), 4),
            "ci95_width_std": round(float(np.std(ci_widths)), 4),
            "ci95_width_q025": round(float(np.percentile(ci_widths, 2.5)), 4),
            "ci95_width_q975": round(float(np.percentile(ci_widths, 97.5)), 4),
            "coverage_rate": round(float(np.mean([r["ci_covers"] for r in ok_results])), 4),
            "power_rate": round(float(np.mean([r["ci_excludes_zero"] for r in ok_results])), 4),
            "elapsed_sec": round(elapsed, 1),
            "sec_per_rep": round(elapsed / len(results), 1),
        }
    
    with open(result_file, "w") as f:
        json.dump(summary, f, indent=2)
    
    print(f"  {condition_id}: done in {elapsed:.0f}s "
          f"(CI_width={summary.get('ci95_width_avg','?')}, "
          f"power={summary.get('power_rate','?')})")
    sys.stdout.flush()
    return summary


def main():
    print("=" * 70)
    print("Fisher Info N × Benchmark Identifiability Heatmap (W4)")
    print(f"N values: {N_VALUES}")
    print(f"Benchmarks: {list(BENCHMARKS.keys())}")
    print(f"Reps per cell: {N_REPS}")
    print(f"Total fits: {len(N_VALUES) * len(BENCHMARKS) * N_REPS}")
    print(f"Output: {OUTPUT_DIR}")
    print("=" * 70)
    sys.stdout.flush()
    
    # Compile Stan model once
    print("\nCompiling Stan model...")
    sys.stdout.flush()
    model = cmdstanpy.CmdStanModel(stan_file=STAN_FILE)
    print(f"Model compiled: {model.exe_file}")
    sys.stdout.flush()
    
    # Timing estimate: run 1 rep for smallest condition
    print("\nTiming calibration (1 rep, N=5, mmlu)...")
    sys.stdout.flush()
    t0 = time.time()
    test_result = fit_one_rep((5, "mmlu", BENCHMARKS["mmlu"], 9999))
    t_single = time.time() - t0
    print(f"  Single fit: {t_single:.1f}s, success={test_result['success']}")
    
    n_workers = min(8, os.cpu_count() or 4)
    total_fits = len(N_VALUES) * len(BENCHMARKS) * N_REPS
    estimated_hours = (total_fits * t_single / n_workers) / 3600
    print(f"  Estimated total time: {estimated_hours:.1f}h ({n_workers} workers)")
    print()
    sys.stdout.flush()
    
    # Run all conditions
    t_start = time.time()
    all_summaries = []
    total_conditions = len(N_VALUES) * len(BENCHMARKS)
    ci = 0
    
    for n_models in N_VALUES:
        for bench_name, bench_params in BENCHMARKS.items():
            ci += 1
            elapsed = time.time() - t_start
            if ci > 1:
                eta = elapsed / (ci - 1) * (total_conditions - ci + 1)
                eta_str = f"ETA {eta/3600:.1f}h"
            else:
                eta_str = ""
            print(f"\n[{ci}/{total_conditions}] N={n_models}, bench={bench_name} {eta_str}")
            sys.stdout.flush()
            
            summary = run_condition(n_models, bench_name, bench_params, N_REPS, n_workers=n_workers)
            all_summaries.append(summary)
    
    # Write combined summary
    combined_file = OUTPUT_DIR / "heatmap_summary.json"
    with open(combined_file, "w") as f:
        json.dump(all_summaries, f, indent=2)
    
    total_time = time.time() - t_start
    print(f"\n{'='*70}")
    print(f"ALL DONE in {total_time/3600:.2f}h")
    print(f"Summary: {combined_file}")
    print("HEATMAP_DONE")
    sys.stdout.flush()


if __name__ == "__main__":
    main()

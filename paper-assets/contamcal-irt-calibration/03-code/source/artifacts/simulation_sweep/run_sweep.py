#!/usr/bin/env python3
"""
exp-004: Simulation Identifiability Sweep for 4PL+γ IRT.
Systematically sweep AUC × N_models × prior × exposure_type to map recovery boundaries.

Usage:
    python run_sweep.py subset                    # 12 conditions × 10 seeds = 120 runs (serial)
    python run_sweep.py subset --parallel 2       # same, 2 conditions in parallel
    python run_sweep.py full                      # 144 conditions × 10 seeds = 1440 runs
    python run_sweep.py dry-run                   # 1 condition × 1 seed for format check
"""

import argparse
import json
import os
import sys
import time
import itertools
import numpy as np
from concurrent.futures import ProcessPoolExecutor, as_completed
from scipy.stats import norm, rankdata
from scipy.special import expit
from pathlib import Path
import cmdstanpy

N_ITEMS = 300
GAMMA_TRUE = 0.5
BASE_EXPOSURE_RATE = 0.3
N_SEEDS = 10

SCRIPT_DIR = Path(__file__).parent
STAN_FILE = str(SCRIPT_DIR / "contam_irt_4pl_sweep.stan")
RESULTS_DIR = SCRIPT_DIR / "results"
STOP_FILE = SCRIPT_DIR / ".stop_after_seed"

SUBSET = {
    "auc": [0.80, 0.90, 0.55, 0.65],
    "n_models": [20, 50, 100],
    "gamma_prior_sd": [1.0],
    "exposure_type": ["binary"],
}

FULL = {
    "auc": [0.55, 0.60, 0.65, 0.70, 0.80, 0.90],
    "n_models": [20, 50, 100, 200],
    "gamma_prior_sd": [0.5, 1.0, 2.0],
    "exposure_type": ["binary", "continuous"],
}


def compute_auc(y_true, y_score):
    """AUC via Mann-Whitney U / Wilcoxon rank-sum."""
    y_true = np.asarray(y_true).ravel()
    y_score = np.asarray(y_score).ravel()
    n_pos = int(np.sum(y_true == 1))
    n_neg = int(np.sum(y_true == 0))
    if n_pos == 0 or n_neg == 0:
        return 0.5
    ranks = rankdata(y_score)
    pos_rank_sum = float(ranks[y_true == 1].sum())
    return (pos_rank_sum - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg)


def auc_to_sigma(target_auc):
    """Noise sigma for binary gt + Gaussian noise to achieve target AUC.
    AUC = Phi(1 / (sigma * sqrt(2))), so sigma = 1 / (sqrt(2) * Phi^{-1}(AUC)).
    """
    z = norm.ppf(target_auc)
    if z <= 0:
        return 1e6
    return 1.0 / (np.sqrt(2) * z)


def generate_exposure_binary(rng, n_models, target_auc):
    """Binary ground truth + Gaussian noise → exposure scores."""
    gt = rng.binomial(1, BASE_EXPOSURE_RATE, (n_models, N_ITEMS)).astype(float)
    sigma = auc_to_sigma(target_auc)
    noise = rng.standard_normal((n_models, N_ITEMS)) * sigma
    score = gt + noise
    actual_auc = compute_auc(gt.ravel(), score.ravel())
    return score, actual_auc


def generate_exposure_continuous(rng, n_models, target_auc):
    """Continuous [0,1] exposure via Phi-transformed normals with controlled AUC."""
    gt = rng.binomial(1, BASE_EXPOSURE_RATE, (n_models, N_ITEMS))
    d_prime = np.sqrt(2) * norm.ppf(target_auc) if target_auc > 0.5 else 0.0
    z = np.where(
        gt,
        rng.standard_normal((n_models, N_ITEMS)) + d_prime / 2,
        rng.standard_normal((n_models, N_ITEMS)) - d_prime / 2,
    )
    score = norm.cdf(z)
    actual_auc = compute_auc(gt.ravel(), score.ravel())
    return score, actual_auc


def generate_data(rng, n_models, target_auc, exposure_type):
    theta = rng.standard_normal(n_models)
    a = rng.lognormal(0, 0.5, N_ITEMS)
    b = rng.standard_normal(N_ITEMS)
    c = rng.beta(5, 20, N_ITEMS)
    d = rng.beta(20, 5, N_ITEMS)

    if exposure_type == "binary":
        exposure, actual_auc = generate_exposure_binary(rng, n_models, target_auc)
    else:
        exposure, actual_auc = generate_exposure_continuous(rng, n_models, target_auc)

    eta = np.outer(np.ones(n_models), a) * (theta[:, None] - b[None, :]) + GAMMA_TRUE * exposure
    prob = c[None, :] + (d[None, :] - c[None, :]) * expit(eta)
    y = rng.binomial(1, prob)

    true_params = {"theta": theta, "a": a, "b": b, "c": c, "d": d}
    stan_data = {
        "N_models": n_models,
        "N_items": N_ITEMS,
        "y": y.tolist(),
        "exposure": exposure.tolist(),
        "gamma_prior_sd": 1.0,
    }
    return stan_data, true_params, actual_auc


FIT_TIMEOUT = 7200  # 2 hours per fit


def fit_nuts(stan_data, seed=42, parallel_chains=None):
    model = cmdstanpy.CmdStanModel(stan_file=STAN_FILE)
    sample_kwargs = dict(
        data=stan_data,
        chains=4,
        iter_warmup=500,
        iter_sampling=1000,
        seed=seed,
        adapt_delta=0.95,
        max_treedepth=10,
        show_progress=False,
        timeout=FIT_TIMEOUT,
    )
    if parallel_chains is not None:
        sample_kwargs["parallel_chains"] = parallel_chains
    fit = model.sample(**sample_kwargs)
    return fit


def evaluate(fit, true_params):
    summary = fit.summary()

    gamma_draws = fit.stan_variable("gamma")
    gamma_mean = float(np.mean(gamma_draws))
    gamma_sd = float(np.std(gamma_draws))
    gamma_q025 = float(np.percentile(gamma_draws, 2.5))
    gamma_q975 = float(np.percentile(gamma_draws, 97.5))
    gamma_q10 = float(np.percentile(gamma_draws, 10))
    gamma_q90 = float(np.percentile(gamma_draws, 90))
    gamma_q25 = float(np.percentile(gamma_draws, 25))
    gamma_q75 = float(np.percentile(gamma_draws, 75))
    gamma_bias = gamma_mean - GAMMA_TRUE
    gamma_rel_bias = abs(gamma_bias / GAMMA_TRUE)

    theta_draws = fit.stan_variable("theta")
    theta_post_mean = np.mean(theta_draws, axis=0)
    theta_true = true_params["theta"]
    theta_corr = float(np.corrcoef(theta_post_mean, theta_true)[0, 1])
    theta_rmse = float(np.sqrt(np.mean((theta_post_mean - theta_true) ** 2)))

    diag = fit.diagnose()
    divergent = 0
    for line in diag.split("\n"):
        if "divergent" in line.lower():
            parts = [w for w in line.split() if w.isdigit()]
            if parts:
                divergent = int(parts[0])
                break
    total_draws = fit.chains * 1000
    divergent_pct = 100.0 * divergent / total_draws

    max_rhat = float(summary["R_hat"].max()) if "R_hat" in summary.columns else float("nan")
    min_ess = (
        float(summary["ESS_bulk"].min())
        if "ESS_bulk" in summary.columns
        else (float(summary["N_Eff"].min()) if "N_Eff" in summary.columns else float("nan"))
    )

    return {
        "gamma_mean": round(gamma_mean, 4),
        "gamma_sd": round(gamma_sd, 4),
        "gamma_q025": round(gamma_q025, 4),
        "gamma_q975": round(gamma_q975, 4),
        "gamma_q10": round(gamma_q10, 4),
        "gamma_q90": round(gamma_q90, 4),
        "gamma_q25": round(gamma_q25, 4),
        "gamma_q75": round(gamma_q75, 4),
        "gamma_bias": round(gamma_bias, 4),
        "gamma_rel_bias": round(gamma_rel_bias, 4),
        "ci95_covers": bool(gamma_q025 <= GAMMA_TRUE <= gamma_q975),
        "ci80_covers": bool(gamma_q10 <= GAMMA_TRUE <= gamma_q90),
        "ci50_covers": bool(gamma_q25 <= GAMMA_TRUE <= gamma_q75),
        "ci95_excludes_zero": bool(gamma_q025 > 0 or gamma_q975 < 0),
        "ci95_width": round(gamma_q975 - gamma_q025, 4),
        "theta_corr": round(theta_corr, 4),
        "theta_rmse": round(theta_rmse, 4),
        "max_rhat": round(max_rhat, 4),
        "divergent_count": divergent,
        "divergent_pct": round(divergent_pct, 2),
        "min_ess": round(min_ess, 1) if not np.isnan(min_ess) else None,
    }


def condition_id(auc, n_models, gamma_prior_sd, exposure_type):
    return f"auc{auc}_n{n_models}_prior{gamma_prior_sd}_{exposure_type}"


def run_single(auc, n_models, gamma_prior_sd, exposure_type, seed, parallel_chains=None):
    """Run one (condition, seed) pair. Returns metrics dict."""
    rng = np.random.default_rng(seed * 10000 + 42)
    t0 = time.time()

    stan_data, true_params, actual_auc = generate_data(rng, n_models, auc, exposure_type)
    stan_data["gamma_prior_sd"] = gamma_prior_sd

    try:
        fit = fit_nuts(stan_data, seed=seed, parallel_chains=parallel_chains)
        metrics = evaluate(fit, true_params)
        metrics["actual_auc"] = round(actual_auc, 4)
        metrics["success"] = True
    except Exception as e:
        metrics = {"success": False, "error": str(e), "actual_auc": round(actual_auc, 4)}

    metrics["fit_time_sec"] = round(time.time() - t0, 1)
    metrics["seed"] = seed
    return metrics


def load_checkpoint(cond_id):
    """Load existing results for a condition (for resume support)."""
    path = RESULTS_DIR / f"{cond_id}.json"
    if path.exists():
        with open(path) as f:
            data = json.load(f)
        return data.get("runs", [])
    return []


def save_condition(cond_id, config, runs):
    """Save condition results to JSON."""
    path = RESULTS_DIR / f"{cond_id}.json"
    with open(path, "w") as f:
        json.dump({"condition_id": cond_id, "config": config, "runs": runs}, f, indent=2)


def run_condition(auc, n_models, gamma_prior_sd, exposure_type, seeds, parallel_chains=None, resume=False):
    """Run all seeds for one condition with checkpoint/resume."""
    cid = condition_id(auc, n_models, gamma_prior_sd, exposure_type)
    config = {
        "auc": auc,
        "n_models": n_models,
        "n_items": N_ITEMS,
        "gamma_true": GAMMA_TRUE,
        "gamma_prior_sd": gamma_prior_sd,
        "exposure_type": exposure_type,
    }

    existing = load_checkpoint(cid)
    done_seeds = {r["seed"] for r in existing if r.get("success", False)}
    remaining = [s for s in seeds if s not in done_seeds]

    if not remaining:
        print(f"  [{cid}] all {len(seeds)} seeds done, skipping")
        sys.stdout.flush()
        return existing

    print(f"  [{cid}] {len(done_seeds)}/{len(seeds)} done, running {len(remaining)} remaining")
    sys.stdout.flush()

    if resume:
        runs = [r for r in existing if r.get("success", False)]
    else:
        runs = list(existing)
    for i, seed in enumerate(remaining):
        metrics = run_single(auc, n_models, gamma_prior_sd, exposure_type, seed, parallel_chains=parallel_chains)
        runs.append(metrics)
        status = "OK" if metrics.get("success") else "FAIL"
        gamma_str = f"γ={metrics.get('gamma_mean', '?')}" if metrics.get("success") else metrics.get("error", "?")[:40]
        print(
            f"    seed {seed} ({len(done_seeds)+i+1}/{len(seeds)}): {status} "
            f"{gamma_str} θ_corr={metrics.get('theta_corr', '?')} ({metrics['fit_time_sec']}s)"
        )
        sys.stdout.flush()
        save_condition(cid, config, runs)

    return runs


def _run_condition_wrapper(args):
    """Top-level wrapper for ProcessPoolExecutor (must be picklable)."""
    import tempfile
    auc, n_models, prior_sd, exp_type, seeds, parallel_chains, resume = args
    cid = condition_id(auc, n_models, prior_sd, exp_type)
    worker_tmpdir = tempfile.mkdtemp(prefix=f"stan_{cid}_", dir="/home/ubuntu/tmp_cmdstan")
    os.environ["TMPDIR"] = worker_tmpdir
    return run_condition(auc, n_models, prior_sd, exp_type, seeds, parallel_chains=parallel_chains, resume=resume)


def build_conditions(config):
    """Generate all (auc, n_models, prior_sd, exp_type) combos from config."""
    return list(itertools.product(
        config["auc"], config["n_models"], config["gamma_prior_sd"], config["exposure_type"]
    ))


def parse_args():
    parser = argparse.ArgumentParser(description="4PL+γ IRT simulation sweep")
    parser.add_argument("mode", nargs="?", default="subset", choices=["subset", "full", "dry-run"])
    parser.add_argument("--parallel", type=int, default=1, help="Number of conditions to run in parallel (default: 1)")
    parser.add_argument("--chains-parallel", type=int, default=None,
                        help="Max chains to run simultaneously per fit (default: all 4)")
    parser.add_argument("--resume", action="store_true",
                        help="Resume mode: skip successful seeds, re-run failed/missing ones")
    return parser.parse_args()


def main():
    args = parse_args()
    mode = args.mode
    n_parallel = max(1, args.parallel)
    parallel_chains = args.chains_parallel

    if mode == "dry-run":
        config = SUBSET
        conditions = [(0.80, 50, 1.0, "binary")]
        seeds = [0]
        print("=== DRY RUN: 1 condition, 1 seed ===")
    elif mode == "subset":
        config = SUBSET
        conditions = build_conditions(config)
        seeds = list(range(N_SEEDS))
        print(f"=== SUBSET: {len(conditions)} conditions × {N_SEEDS} seeds = {len(conditions)*N_SEEDS} runs ===")
    elif mode == "full":
        config = FULL
        conditions = build_conditions(config)
        seeds = list(range(N_SEEDS))
        print(f"=== FULL: {len(conditions)} conditions × {N_SEEDS} seeds = {len(conditions)*N_SEEDS} runs ===")
    else:
        print(f"Unknown mode: {mode}. Use: dry-run, subset, full")
        sys.exit(1)

    print(f"Stan model: {STAN_FILE}")
    print(f"Results dir: {RESULTS_DIR}")
    print(f"Parallel conditions: {n_parallel}, chains_parallel: {parallel_chains or 'default'}")
    sys.stdout.flush()

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    # Compile Stan model once before forking workers
    print("\nCompiling Stan model...")
    sys.stdout.flush()
    model = cmdstanpy.CmdStanModel(stan_file=STAN_FILE)
    print(f"Compiled: {model.exe_file}")
    sys.stdout.flush()

    total_conditions = len(conditions)
    t_start = time.time()

    resume = args.resume
    if resume:
        print("Resume mode: will skip successful seeds, re-run failed/missing")
        sys.stdout.flush()

    if n_parallel <= 1:
        for ci, (auc, n_models, prior_sd, exp_type) in enumerate(conditions):
            cid = condition_id(auc, n_models, prior_sd, exp_type)
            elapsed = time.time() - t_start
            if ci > 0:
                eta = elapsed / ci * (total_conditions - ci)
                eta_str = f"ETA {eta/3600:.1f}h"
            else:
                eta_str = "ETA ?"
            print(f"\n[{ci+1}/{total_conditions}] {cid} ({eta_str})")
            sys.stdout.flush()
            run_condition(auc, n_models, prior_sd, exp_type, seeds, parallel_chains=parallel_chains, resume=resume)
    else:
        # Parallel execution: run multiple conditions concurrently
        tasks = [(auc, nm, ps, et, seeds, parallel_chains, resume) for auc, nm, ps, et in conditions]
        completed = 0
        print(f"\nLaunching {total_conditions} conditions with {n_parallel} workers...")
        sys.stdout.flush()
        with ProcessPoolExecutor(max_workers=n_parallel) as executor:
            futures = {executor.submit(_run_condition_wrapper, t): t for t in tasks}
            for future in as_completed(futures):
                completed += 1
                t = futures[future]
                cid = condition_id(t[0], t[1], t[2], t[3])
                try:
                    future.result()
                    print(f"\n[{completed}/{total_conditions}] {cid} DONE")
                except Exception as e:
                    print(f"\n[{completed}/{total_conditions}] {cid} ERROR: {e}")
                sys.stdout.flush()

    total_time = time.time() - t_start
    print(f"\n=== SWEEP COMPLETE ({total_time/3600:.1f}h) ===")
    print("SWEEP_DONE")
    sys.stdout.flush()

    aggregate_results()


def aggregate_results():
    """Build summary JSON from per-condition results."""
    summary = []
    for path in sorted(RESULTS_DIR.glob("*.json")):
        if path.name == "sweep_summary.json":
            continue
        with open(path) as f:
            data = json.load(f)
        config = data.get("config", {})
        runs = [r for r in data.get("runs", []) if r.get("success")]
        if not runs:
            continue

        gamma_means = [r["gamma_mean"] for r in runs]
        gamma_biases = [r["gamma_bias"] for r in runs]
        ci95_covers = [r["ci95_covers"] for r in runs]
        ci80_covers = [r["ci80_covers"] for r in runs]
        ci50_covers = [r["ci50_covers"] for r in runs]
        ci95_widths = [r["ci95_width"] for r in runs]
        theta_corrs = [r["theta_corr"] for r in runs]
        theta_rmses = [r["theta_rmse"] for r in runs]

        summary.append({
            "condition_id": data["condition_id"],
            **config,
            "n_seeds_ok": len(runs),
            "gamma_mean_avg": round(float(np.mean(gamma_means)), 4),
            "gamma_mean_std": round(float(np.std(gamma_means)), 4),
            "gamma_bias_avg": round(float(np.mean(gamma_biases)), 4),
            "gamma_rmse": round(float(np.sqrt(np.mean(np.array(gamma_biases) ** 2))), 4),
            "ci95_coverage": round(float(np.mean(ci95_covers)), 3),
            "ci80_coverage": round(float(np.mean(ci80_covers)), 3),
            "ci50_coverage": round(float(np.mean(ci50_covers)), 3),
            "ci95_width_avg": round(float(np.mean(ci95_widths)), 4),
            "theta_corr_avg": round(float(np.mean(theta_corrs)), 4),
            "theta_rmse_avg": round(float(np.mean(theta_rmses)), 4),
            "fit_time_avg": round(float(np.mean([r["fit_time_sec"] for r in runs])), 1),
        })

    summary_path = RESULTS_DIR / "sweep_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary written to {summary_path} ({len(summary)} conditions)")

    # Print table
    print(f"\n{'Condition':<40} {'γ_bias':>8} {'γ_RMSE':>8} {'CI95%':>6} {'θ_corr':>8} {'time':>6}")
    print("-" * 80)
    for s in summary:
        print(
            f"{s['condition_id']:<40} {s['gamma_bias_avg']:>8.4f} {s['gamma_rmse']:>8.4f} "
            f"{s['ci95_coverage']:>6.3f} {s['theta_corr_avg']:>8.4f} {s['fit_time_avg']:>6.0f}s"
        )
    sys.stdout.flush()


if __name__ == "__main__":
    main()

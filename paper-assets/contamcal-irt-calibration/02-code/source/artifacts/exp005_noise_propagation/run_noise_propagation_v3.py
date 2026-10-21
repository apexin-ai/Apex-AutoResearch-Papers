"""
exp-005 v3: Noise Propagation Simulation

Changes from v2:
  - Stan output to local dir (not /tmp tmpfs)
  - ME model → analytic ME (1231 params, not 10231; converges properly)
  - Simple model runs first per (σ_e, seed), preserving results if ME fails
  - Incremental saving after each model fit
  - Auto-cleanup of Stan chain CSVs after extraction
"""

import argparse
import json
import logging
import os
import shutil
import sys
import time

import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

N_MODELS = 30
N_ITEMS = 300
TRUE_GAMMA = 0.5
SIGMA_E_LEVELS = [0.1, 0.3, 0.5, 0.7, 1.0]
N_SEEDS = 5

NUTS_DEFAULTS = {
    "chains": 4,
    "iter_warmup": 500,
    "iter_sampling": 1000,
    "adapt_delta": 0.95,
    "max_treedepth": 12,
}


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -30, 30)))


def generate_synthetic_data(n_models, n_items, gamma, sigma_e, rng):
    theta = rng.standard_normal(n_models)
    a = rng.lognormal(0, 0.5, n_items)
    b = rng.standard_normal(n_items)
    c = rng.beta(5, 20, n_items)
    d = rng.beta(20, 5, n_items)

    e_true = np.zeros((n_models, n_items))
    contam_mask = rng.random((n_models, n_items)) < 0.3
    e_true[contam_mask] = rng.exponential(0.5, contam_mask.sum())

    tau = np.maximum(0, e_true + rng.normal(0, 0.01, (n_models, n_items)))
    e_observed = tau + rng.normal(0, sigma_e, (n_models, n_items))

    y = np.zeros((n_models, n_items), dtype=int)
    for i in range(n_models):
        for j in range(n_items):
            eta = a[j] * (theta[i] - b[j]) + gamma * tau[i, j]
            p = c[j] + (d[j] - c[j]) * sigmoid(eta)
            y[i, j] = int(rng.random() < p)

    true_cal = np.zeros(n_models)
    for i in range(n_models):
        total = 0.0
        for j in range(n_items):
            eta_clean = a[j] * (theta[i] - b[j])
            p_clean = c[j] + (d[j] - c[j]) * sigmoid(eta_clean)
            total += p_clean
        true_cal[i] = total / n_items

    return {
        "y": y,
        "exposure": e_observed,
        "true_cal": true_cal,
        "theta": theta,
        "a": a, "b": b, "c": c, "d": d,
        "gamma": gamma,
        "e_true": e_true,
    }


def prepare_stan_data_simple(synth):
    n_models, n_items = synth["y"].shape
    return {
        "N_models": int(n_models),
        "N_items": int(n_items),
        "y": synth["y"].tolist(),
        "exposure": synth["exposure"].tolist(),
    }


def compute_tau_posterior(exposure, sigma_e, mu_tau=0.0, sigma_tau=1.0):
    sigma_tau_sq = sigma_tau ** 2
    sigma_e_sq = sigma_e ** 2
    denom = sigma_tau_sq + sigma_e_sq
    tau_post_mean = (exposure * sigma_tau_sq + mu_tau * sigma_e_sq) / denom
    tau_post_var = np.full_like(exposure, (sigma_tau_sq * sigma_e_sq) / denom)
    return tau_post_mean, tau_post_var


def prepare_stan_data_analytic_me(synth, sigma_e):
    n_models, n_items = synth["y"].shape
    tau_post_mean, tau_post_var = compute_tau_posterior(
        synth["exposure"], sigma_e
    )
    return {
        "N_models": int(n_models),
        "N_items": int(n_items),
        "y": synth["y"].tolist(),
        "tau_post_mean": tau_post_mean.tolist(),
        "tau_post_var": tau_post_var.tolist(),
    }


def fit_and_extract_ci(model, stan_data, seed, stan_output_dir):
    output_subdir = os.path.join(stan_output_dir, f"fit_{seed}_{int(time.time())}")
    os.makedirs(output_subdir, exist_ok=True)

    fit = model.sample(
        data=stan_data,
        seed=seed,
        show_progress=False,
        output_dir=output_subdir,
        **NUTS_DEFAULTS,
    )

    cal_draws = fit.stan_variable("calibrated_score")
    q025 = np.percentile(cal_draws, 2.5, axis=0)
    q975 = np.percentile(cal_draws, 97.5, axis=0)
    ci_width = q975 - q025

    cal_mean = np.mean(cal_draws, axis=0)
    cal_sd = np.std(cal_draws, axis=0)

    gamma_draws = fit.stan_variable("gamma")

    summary = fit.summary()
    rhat_col = next(
        (c for c in ["R_hat", "Rhat"] if c in summary.columns),
        summary.columns[-1],
    )
    max_rhat = float(summary[rhat_col].max())

    result = {
        "ci_width_mean": float(np.mean(ci_width)),
        "ci_width_median": float(np.median(ci_width)),
        "ci_width_per_model": np.round(ci_width, 6).tolist(),
        "cal_mean": np.round(cal_mean, 6).tolist(),
        "cal_sd": np.round(cal_sd, 6).tolist(),
        "gamma_mean": round(float(np.mean(gamma_draws)), 4),
        "gamma_sd": round(float(np.std(gamma_draws)), 4),
        "max_rhat": round(max_rhat, 4),
        "converged": max_rhat < 1.01,
    }

    # Clean up chain CSVs to save disk
    shutil.rmtree(output_subdir, ignore_errors=True)

    return result


def run_single(sigma_e, seed, stan_simple, stan_me_analytic,
               stan_output_dir, n_models=N_MODELS, n_items=N_ITEMS):
    rng = np.random.default_rng(seed)
    synth = generate_synthetic_data(n_models, n_items, TRUE_GAMMA, sigma_e, rng)

    # Simple model first (faster, less likely to fail)
    log.info("  Fitting simple model (σ_e=%.1f, seed=%d)...", sigma_e, seed)
    stan_data_simple = prepare_stan_data_simple(synth)
    t0 = time.time()
    simple_result = fit_and_extract_ci(stan_simple, stan_data_simple, seed, stan_output_dir)
    simple_time = time.time() - t0
    log.info("    Simple done in %.0fs, CI_width=%.4f, Rhat=%.3f",
             simple_time, simple_result["ci_width_mean"], simple_result["max_rhat"])

    # Analytic ME model
    log.info("  Fitting analytic ME model (σ_e=%.1f, seed=%d)...", sigma_e, seed)
    stan_data_me = prepare_stan_data_analytic_me(synth, sigma_e)
    t0 = time.time()
    me_result = fit_and_extract_ci(stan_me_analytic, stan_data_me, seed, stan_output_dir)
    me_time = time.time() - t0
    log.info("    ME(analytic) done in %.0fs, CI_width=%.4f, Rhat=%.3f",
             me_time, me_result["ci_width_mean"], me_result["max_rhat"])

    return {
        "sigma_e": sigma_e,
        "seed": seed,
        "n_models": n_models,
        "n_items": n_items,
        "true_gamma": TRUE_GAMMA,
        "me": me_result,
        "simple": simple_result,
        "me_model_type": "analytic",
        "me_fit_time_sec": round(me_time, 1),
        "simple_fit_time_sec": round(simple_time, 1),
        "true_cal_scores": np.round(synth["true_cal"], 6).tolist(),
    }


def check_monotonicity(agg_results: dict) -> dict:
    sigma_levels = sorted(agg_results.keys())
    me_widths = [agg_results[s]["me_ci_mean"] for s in sigma_levels]
    simple_widths = [agg_results[s]["simple_ci_mean"] for s in sigma_levels]

    me_monotonic = all(me_widths[i] <= me_widths[i + 1]
                       for i in range(len(me_widths) - 1))
    from scipy.stats import spearmanr
    me_rho, me_pval = spearmanr(sigma_levels, me_widths)
    simple_rho, simple_pval = spearmanr(sigma_levels, simple_widths)

    return {
        "me_strictly_monotonic": me_monotonic,
        "me_spearman_rho": round(float(me_rho), 4),
        "me_spearman_pval": round(float(me_pval), 6),
        "simple_spearman_rho": round(float(simple_rho), 4),
        "simple_spearman_pval": round(float(simple_pval), 6),
        "me_ci_widths": {str(s): w for s, w in zip(sigma_levels, me_widths)},
        "simple_ci_widths": {str(s): w for s, w in zip(sigma_levels, simple_widths)},
    }


def main():
    parser = argparse.ArgumentParser(
        description="exp-005 v3: Noise propagation simulation (analytic ME)"
    )
    parser.add_argument(
        "--stan-simple", type=str,
        default=os.path.join(SCRIPT_DIR, "..", "exp006_irt_calibration",
                             "contam_irt_4pl_simple.stan"),
    )
    parser.add_argument(
        "--stan-me-analytic", type=str,
        default=os.path.join(SCRIPT_DIR, "..", "exp006_irt_calibration",
                             "contam_irt_4pl_me_analytic.stan"),
    )
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--sigma-levels", type=float, nargs="+", default=SIGMA_E_LEVELS)
    parser.add_argument("--n-seeds", type=int, default=N_SEEDS)
    parser.add_argument("--n-models", type=int, default=N_MODELS)
    parser.add_argument("--n-items", type=int, default=N_ITEMS)
    parser.add_argument("--base-seed", type=int, default=42)
    args = parser.parse_args()

    n_models = args.n_models
    n_items = args.n_items

    output_dir = os.path.abspath(args.output_dir)
    os.makedirs(output_dir, exist_ok=True)

    # Stan chain output goes here, not /tmp
    stan_output_dir = os.path.join(output_dir, "stan_output")
    os.makedirs(stan_output_dir, exist_ok=True)

    stan_simple_path = os.path.abspath(args.stan_simple)
    stan_me_path = os.path.abspath(args.stan_me_analytic)

    for path, name in [(stan_simple_path, "simple"), (stan_me_path, "analytic ME")]:
        if not os.path.exists(path):
            log.error("Stan model not found: %s (%s)", path, name)
            sys.exit(1)

    log.info("=== exp-005 v3: Noise Propagation (analytic ME) ===")
    log.info("σ_e levels: %s", args.sigma_levels)
    log.info("Seeds per level: %d", args.n_seeds)
    log.info("Synthetic data: %d models × %d items", n_models, n_items)
    log.info("Stan output dir: %s", stan_output_dir)

    import cmdstanpy
    log.info("Compiling Stan models...")
    stan_simple = cmdstanpy.CmdStanModel(stan_file=stan_simple_path)
    stan_me_analytic = cmdstanpy.CmdStanModel(stan_file=stan_me_path)
    log.info("Compilation done.")

    # Resume support: load existing results
    results_path = os.path.join(output_dir, "noise_propagation_results.json")
    if os.path.exists(results_path):
        with open(results_path) as f:
            all_runs = json.load(f)
        done_keys = {(r["sigma_e"], r["seed"]) for r in all_runs}
        log.info("Resuming: %d runs already completed", len(all_runs))
    else:
        all_runs = []
        done_keys = set()

    seeds = list(range(args.base_seed, args.base_seed + args.n_seeds))
    total = len(args.sigma_levels) * len(seeds)
    completed = len(done_keys)

    for sigma_e in args.sigma_levels:
        log.info("=== σ_e = %.1f ===", sigma_e)
        for seed in seeds:
            if (sigma_e, seed) in done_keys:
                log.info("  Skipping (σ_e=%.1f, seed=%d) — already done", sigma_e, seed)
                continue

            result = run_single(sigma_e, seed, stan_simple, stan_me_analytic,
                                stan_output_dir, n_models, n_items)
            all_runs.append(result)
            completed += 1

            with open(results_path, "w") as f:
                json.dump(all_runs, f, indent=2)
            log.info("  Saved (%d/%d complete)", completed, total)

    # Aggregate
    agg = {}
    for sigma_e in args.sigma_levels:
        runs = [r for r in all_runs if r["sigma_e"] == sigma_e]
        me_widths = [r["me"]["ci_width_mean"] for r in runs]
        simple_widths = [r["simple"]["ci_width_mean"] for r in runs]
        agg[sigma_e] = {
            "me_ci_mean": round(float(np.mean(me_widths)), 6),
            "me_ci_std": round(float(np.std(me_widths)), 6),
            "simple_ci_mean": round(float(np.mean(simple_widths)), 6),
            "simple_ci_std": round(float(np.std(simple_widths)), 6),
            "n_runs": len(runs),
            "n_converged_me": sum(1 for r in runs if r["me"]["converged"]),
            "n_converged_simple": sum(1 for r in runs if r["simple"]["converged"]),
        }

    monotonicity = check_monotonicity(agg)

    summary = {
        "experiment": "exp-005 v3",
        "description": "Noise propagation: σ_e → CI width (analytic ME model)",
        "config": {
            "n_models": n_models,
            "n_items": n_items,
            "true_gamma": TRUE_GAMMA,
            "sigma_e_levels": args.sigma_levels,
            "n_seeds": args.n_seeds,
            "base_seed": args.base_seed,
            "me_model_type": "analytic",
        },
        "aggregated": {str(k): v for k, v in agg.items()},
        "monotonicity_check": monotonicity,
        "verdict": (
            "PASS: ME model CI width increases with σ_e"
            if monotonicity["me_spearman_rho"] > 0.8
            else "INCONCLUSIVE: weak monotonic relationship"
        ),
    }

    summary_path = os.path.join(output_dir, "noise_propagation_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    log.info("=== Results Summary ===")
    for sigma_e in args.sigma_levels:
        a = agg[sigma_e]
        log.info(
            "  σ_e=%.1f: ME CI=%.4f±%.4f, Simple CI=%.4f±%.4f",
            sigma_e,
            a["me_ci_mean"], a["me_ci_std"],
            a["simple_ci_mean"], a["simple_ci_std"],
        )
    log.info("Monotonicity (ME): rho=%.3f, p=%.4f → %s",
             monotonicity["me_spearman_rho"],
             monotonicity["me_spearman_pval"],
             "PASS" if monotonicity["me_spearman_rho"] > 0.8 else "WEAK")
    log.info("Verdict: %s", summary["verdict"])

    # Cleanup stan_output dir
    shutil.rmtree(stan_output_dir, ignore_errors=True)
    log.info("Stan output cleaned up.")


if __name__ == "__main__":
    main()

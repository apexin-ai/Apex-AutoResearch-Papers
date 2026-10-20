"""
exp-005: Noise Propagation Simulation

Verifies that the measurement error model correctly propagates signal noise
into wider credible intervals on calibrated scores.

Method:
  1. Generate synthetic 4PL IRT data with known contamination
  2. For each noise level σ_e, add Gaussian noise to true exposure
  3. Fit both ME and simple Stan models
  4. Measure 95% CI width of calibrated scores
  5. Check monotonic relationship: higher σ_e → wider CI (ME model)
  6. Compare ME vs simple model CI widths

Input:
  - Stan models from exp-006: contam_irt_4pl_me.stan, contam_irt_4pl_simple.stan

Output (to --output-dir):
  - noise_propagation_results.json — CI widths per σ_e level and model
  - noise_propagation_summary.json — monotonicity check and summary stats
"""

import argparse
import json
import logging
import os
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
    """Generate synthetic 4PL IRT data with contamination and noisy exposure."""
    theta = rng.standard_normal(n_models)
    a = rng.lognormal(0, 0.5, n_items)
    b = rng.standard_normal(n_items)
    c = rng.beta(5, 20, n_items)
    d = rng.beta(20, 5, n_items)

    # True exposure: ~30% of model-item pairs are contaminated
    e_true = np.zeros((n_models, n_items))
    contam_mask = rng.random((n_models, n_items)) < 0.3
    e_true[contam_mask] = rng.exponential(0.5, contam_mask.sum())

    # Latent tau close to true exposure
    tau = np.maximum(0, e_true + rng.normal(0, 0.01, (n_models, n_items)))

    # Observed exposure with noise
    e_observed = tau + rng.normal(0, sigma_e, (n_models, n_items))

    # Generate responses
    y = np.zeros((n_models, n_items), dtype=int)
    for i in range(n_models):
        for j in range(n_items):
            eta = a[j] * (theta[i] - b[j]) + gamma * tau[i, j]
            p = c[j] + (d[j] - c[j]) * sigmoid(eta)
            y[i, j] = int(rng.random() < p)

    # True calibrated scores (no contamination)
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


def prepare_stan_data(synth):
    n_models, n_items = synth["y"].shape
    return {
        "N_models": int(n_models),
        "N_items": int(n_items),
        "y": synth["y"].tolist(),
        "exposure": synth["exposure"].tolist(),
    }


def fit_and_extract_ci(stan_file, stan_data, seed):
    """Fit Stan model and return calibrated score CI widths."""
    import cmdstanpy
    model = cmdstanpy.CmdStanModel(stan_file=stan_file)

    fit = model.sample(
        data=stan_data,
        seed=seed,
        show_progress=False,
        **NUTS_DEFAULTS,
    )

    cal_draws = fit.stan_variable("calibrated_score")  # (n_draws, N_models)
    q025 = np.percentile(cal_draws, 2.5, axis=0)
    q975 = np.percentile(cal_draws, 97.5, axis=0)
    ci_width = q975 - q025

    cal_mean = np.mean(cal_draws, axis=0)
    cal_sd = np.std(cal_draws, axis=0)

    gamma_draws = fit.stan_variable("gamma")

    # Basic convergence check
    summary = fit.summary()
    rhat_col = next(
        (c for c in ["R_hat", "Rhat"] if c in summary.columns),
        summary.columns[-1],
    )
    max_rhat = float(summary[rhat_col].max())

    return {
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


def run_single(sigma_e, seed, stan_me, stan_simple,
               n_models=N_MODELS, n_items=N_ITEMS):
    """Run one (sigma_e, seed) combination for both models."""
    rng = np.random.default_rng(seed)
    synth = generate_synthetic_data(n_models, n_items, TRUE_GAMMA, sigma_e, rng)
    stan_data = prepare_stan_data(synth)

    log.info("  Fitting ME model (σ_e=%.1f, seed=%d)...", sigma_e, seed)
    t0 = time.time()
    me_result = fit_and_extract_ci(stan_me, stan_data, seed)
    me_time = time.time() - t0
    log.info("    ME done in %.0fs, CI_width=%.4f, Rhat=%.3f",
             me_time, me_result["ci_width_mean"], me_result["max_rhat"])

    log.info("  Fitting simple model (σ_e=%.1f, seed=%d)...", sigma_e, seed)
    t0 = time.time()
    simple_result = fit_and_extract_ci(stan_simple, stan_data, seed)
    simple_time = time.time() - t0
    log.info("    Simple done in %.0fs, CI_width=%.4f, Rhat=%.3f",
             simple_time, simple_result["ci_width_mean"], simple_result["max_rhat"])

    return {
        "sigma_e": sigma_e,
        "seed": seed,
        "n_models": n_models,
        "n_items": n_items,
        "true_gamma": TRUE_GAMMA,
        "me": me_result,
        "simple": simple_result,
        "me_fit_time_sec": round(me_time, 1),
        "simple_fit_time_sec": round(simple_time, 1),
        "true_cal_scores": np.round(synth["true_cal"], 6).tolist(),
    }


def run_posthoc_noise_injection(synth_data, stan_simple, seed,
                                noise_multipliers=(1.0, 1.5, 2.0)):
    """Part B: Fit standard model, then inject noise into exposure and refit.

    Measures how γ and θ CI change with post-hoc noise injection.
    Compares with ME model which should auto-calibrate CIs.
    """
    import cmdstanpy

    base_exposure = synth_data["exposure"]
    exposure_std = np.std(base_exposure)
    n_models, n_items = base_exposure.shape

    results = {}
    for mult in noise_multipliers:
        noise_sigma = mult * exposure_std
        rng = np.random.default_rng(seed + int(mult * 100))
        noisy_exposure = base_exposure + rng.normal(0, noise_sigma, (n_models, n_items))

        stan_data = {
            "N_models": int(n_models),
            "N_items": int(n_items),
            "y": synth_data["y"].tolist(),
            "exposure": noisy_exposure.tolist(),
        }

        log.info("    Part B: noise_mult=%.1f, noise_σ=%.3f", mult, noise_sigma)
        result = fit_and_extract_ci(stan_simple, stan_data, seed)

        results[f"noise_{mult:.1f}x"] = {
            "noise_multiplier": mult,
            "injected_noise_sigma": round(float(noise_sigma), 4),
            "gamma_mean": result["gamma_mean"],
            "gamma_sd": result["gamma_sd"],
            "ci_width_mean": result["ci_width_mean"],
            "max_rhat": result["max_rhat"],
            "converged": result["converged"],
        }

    return results


def check_monotonicity(agg_results: dict) -> dict:
    """Check if CI width increases monotonically with σ_e."""
    sigma_levels = sorted(agg_results.keys())
    me_widths = [agg_results[s]["me_ci_mean"] for s in sigma_levels]
    simple_widths = [agg_results[s]["simple_ci_mean"] for s in sigma_levels]

    me_monotonic = all(me_widths[i] <= me_widths[i + 1]
                       for i in range(len(me_widths) - 1))
    # Spearman rank correlation as a softer check
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
        description="exp-005: Noise propagation simulation for ME model"
    )
    parser.add_argument(
        "--stan-me", type=str,
        default=os.path.join(SCRIPT_DIR, "..", "exp006_irt_calibration",
                             "contam_irt_4pl_me.stan"),
        help="Path to 4PL ME Stan model",
    )
    parser.add_argument(
        "--stan-simple", type=str,
        default=os.path.join(SCRIPT_DIR, "..", "exp006_irt_calibration",
                             "contam_irt_4pl_simple.stan"),
        help="Path to 4PL simple Stan model",
    )
    parser.add_argument(
        "--output-dir", type=str, required=True,
        help="Output directory",
    )
    parser.add_argument(
        "--sigma-levels", type=float, nargs="+", default=SIGMA_E_LEVELS,
        help="Noise levels to test (default: 0.1 0.3 0.5 0.7 1.0)",
    )
    parser.add_argument(
        "--n-seeds", type=int, default=N_SEEDS,
        help="Number of random seeds per σ_e level (default: 5)",
    )
    parser.add_argument(
        "--n-models", type=int, default=N_MODELS,
        help="Number of synthetic models (default: 30)",
    )
    parser.add_argument(
        "--n-items", type=int, default=N_ITEMS,
        help="Number of synthetic items (default: 200)",
    )
    parser.add_argument(
        "--base-seed", type=int, default=42,
        help="Base seed for reproducibility",
    )
    args = parser.parse_args()

    n_models = args.n_models
    n_items = args.n_items

    output_dir = os.path.abspath(args.output_dir)
    os.makedirs(output_dir, exist_ok=True)

    stan_me = os.path.abspath(args.stan_me)
    stan_simple = os.path.abspath(args.stan_simple)

    for path, name in [(stan_me, "ME"), (stan_simple, "simple")]:
        if not os.path.exists(path):
            log.error("Stan model not found: %s (%s)", path, name)
            sys.exit(1)

    log.info("=== exp-005: Noise Propagation Simulation ===")
    log.info("σ_e levels: %s", args.sigma_levels)
    log.info("Seeds per level: %d", args.n_seeds)
    log.info("Synthetic data: %d models × %d items", n_models, n_items)

    # Compile models once
    import cmdstanpy
    log.info("Compiling Stan models...")
    cmdstanpy.CmdStanModel(stan_file=stan_me)
    cmdstanpy.CmdStanModel(stan_file=stan_simple)
    log.info("Compilation done.")

    all_runs = []
    seeds = list(range(args.base_seed, args.base_seed + args.n_seeds))

    for sigma_e in args.sigma_levels:
        log.info("=== σ_e = %.1f ===", sigma_e)
        for seed in seeds:
            result = run_single(sigma_e, seed, stan_me, stan_simple,
                                n_models, n_items)
            all_runs.append(result)

            # Save incrementally
            interim_path = os.path.join(output_dir, "noise_propagation_results.json")
            with open(interim_path, "w") as f:
                json.dump(all_runs, f, indent=2)

    # Part B: Post-hoc noise injection (at σ_e=0.1, baseline noise)
    log.info("=== Part B: Post-hoc Noise Injection ===")
    posthoc_results = []
    for seed in seeds:
        rng = np.random.default_rng(seed)
        synth = generate_synthetic_data(n_models, n_items, TRUE_GAMMA, 0.1, rng)
        ph_result = run_posthoc_noise_injection(
            synth, stan_simple, seed, noise_multipliers=[1.0, 1.5, 2.0]
        )
        ph_result["seed"] = seed

        # Also fit ME model on same base data for comparison
        stan_data_me = prepare_stan_data(synth)
        me_baseline = fit_and_extract_ci(stan_me, stan_data_me, seed)
        ph_result["me_baseline_ci_width"] = me_baseline["ci_width_mean"]

        posthoc_results.append(ph_result)

    posthoc_path = os.path.join(output_dir, "noise_injection_posthoc.json")
    with open(posthoc_path, "w") as f:
        json.dump(posthoc_results, f, indent=2)
    log.info("Part B results saved to %s", posthoc_path)

    # Aggregate: mean CI width per sigma_e level
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
        "experiment": "exp-005",
        "description": "Noise propagation: σ_e → CI width relationship",
        "config": {
            "n_models": n_models,
            "n_items": n_items,
            "true_gamma": TRUE_GAMMA,
            "sigma_e_levels": args.sigma_levels,
            "n_seeds": args.n_seeds,
            "base_seed": args.base_seed,
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
    log.info("Summary saved to %s", summary_path)

    # Print summary
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


if __name__ == "__main__":
    main()

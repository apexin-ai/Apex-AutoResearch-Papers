# P1 Variant experiments: diagnose why base condition 4PL NUTS is borderline fail
# Runs: (0) ADVI rerun with mean=False fix, (a) N_items=300, (b) exposure_rate=0.5, (c) continuous exposure
# Only 4PL NUTS for each variant (Director instruction).

import json
import os
import sys
import time
import numpy as np
from scipy.special import expit
import cmdstanpy

SEED = 42
N_MODELS = 50
GAMMA_TRUE = 0.5

ARTIFACTS_DIR = os.path.dirname(os.path.abspath(__file__))
STAN_4PL = os.path.join(ARTIFACTS_DIR, "contam_irt_4pl.stan")
STAN_2PL = os.path.join(ARTIFACTS_DIR, "contam_irt_2pl.stan")

PASS_THRESHOLDS = {
    "gamma_ci_covers_true": True,
    "gamma_ci_excludes_zero": True,
    "gamma_rel_bias": 0.3,
    "theta_corr": 0.9,
    "theta_rmse": 0.2,
    "max_rhat": 1.01,
    "divergent_pct": 1.0,
}


def generate_data_binary(rng, n_items, exposure_rate):
    theta = rng.standard_normal(N_MODELS)
    a = rng.lognormal(0, 0.5, n_items)
    b = rng.standard_normal(n_items)
    c = rng.beta(5, 20, n_items)
    d = rng.beta(20, 5, n_items)
    exposure = rng.binomial(1, exposure_rate, (N_MODELS, n_items)).astype(float)

    eta = np.outer(np.ones(N_MODELS), a) * (
        theta[:, None] - b[None, :]
    ) + GAMMA_TRUE * exposure
    prob = c[None, :] + (d[None, :] - c[None, :]) * expit(eta)
    y = rng.binomial(1, prob)

    true_params = {"theta": theta, "a": a, "b": b, "c": c, "d": d}
    stan_data = {
        "N_models": N_MODELS,
        "N_items": n_items,
        "y": y.tolist(),
        "exposure": exposure.tolist(),
    }
    return stan_data, true_params


def generate_data_continuous(rng, n_items):
    """Continuous exposure: Beta(5,2) for contaminated items, Beta(1,5) for clean."""
    theta = rng.standard_normal(N_MODELS)
    a = rng.lognormal(0, 0.5, n_items)
    b = rng.standard_normal(n_items)
    c = rng.beta(5, 20, n_items)
    d = rng.beta(20, 5, n_items)

    is_contaminated = rng.binomial(1, 0.3, (N_MODELS, n_items))
    exposure = np.where(
        is_contaminated,
        rng.beta(5, 2, (N_MODELS, n_items)),
        rng.beta(1, 5, (N_MODELS, n_items)),
    )

    eta = np.outer(np.ones(N_MODELS), a) * (
        theta[:, None] - b[None, :]
    ) + GAMMA_TRUE * exposure
    prob = c[None, :] + (d[None, :] - c[None, :]) * expit(eta)
    y = rng.binomial(1, prob)

    true_params = {"theta": theta, "a": a, "b": b, "c": c, "d": d}
    stan_data = {
        "N_models": N_MODELS,
        "N_items": n_items,
        "y": y.tolist(),
        "exposure": exposure.tolist(),
    }
    exp_stats = {
        "mean": float(np.mean(exposure)),
        "std": float(np.std(exposure)),
        "frac_above_0.5": float(np.mean(exposure > 0.5)),
    }
    return stan_data, true_params, exp_stats


def fit_advi(stan_file, stan_data, seed=SEED):
    model = cmdstanpy.CmdStanModel(stan_file=stan_file)
    vb = model.variational(
        data=stan_data, seed=seed, algorithm="fullrank", output_samples=2000,
    )
    return vb


def fit_nuts(stan_file, stan_data, adapt_delta=0.95, max_treedepth=10):
    model = cmdstanpy.CmdStanModel(stan_file=stan_file)
    fit = model.sample(
        data=stan_data, chains=4, iter_warmup=1000, iter_sampling=1000,
        seed=SEED, adapt_delta=adapt_delta, max_treedepth=max_treedepth,
        show_progress=True,
    )
    return fit


def evaluate_advi(vb, true_params, model_name):
    gamma_draws = vb.stan_variable("gamma", mean=False)
    gamma_draws = np.atleast_1d(gamma_draws)
    gamma_mean = float(np.mean(gamma_draws))
    gamma_sd = float(np.std(gamma_draws))
    gamma_q025 = float(np.percentile(gamma_draws, 2.5))
    gamma_q975 = float(np.percentile(gamma_draws, 97.5))
    gamma_bias = gamma_mean - GAMMA_TRUE
    gamma_rel_bias = abs(gamma_bias / GAMMA_TRUE)
    gamma_ci_covers_true = bool(gamma_q025 <= GAMMA_TRUE <= gamma_q975)
    gamma_ci_excludes_zero = bool(gamma_q025 > 0 or gamma_q975 < 0)

    theta_draws = vb.stan_variable("theta", mean=False)
    if theta_draws.ndim == 1:
        theta_post_mean = theta_draws
    else:
        theta_post_mean = np.mean(theta_draws, axis=0)
    theta_true = true_params["theta"]
    theta_corr = float(np.corrcoef(theta_post_mean, theta_true)[0, 1])
    theta_rmse = float(np.sqrt(np.mean((theta_post_mean - theta_true) ** 2)))

    return {
        "model": model_name, "method": "ADVI",
        "gamma_mean": round(gamma_mean, 4), "gamma_sd": round(gamma_sd, 4),
        "gamma_q025": round(gamma_q025, 4), "gamma_q975": round(gamma_q975, 4),
        "gamma_bias": round(gamma_bias, 4), "gamma_rel_bias": round(gamma_rel_bias, 4),
        "gamma_ci_covers_true": gamma_ci_covers_true,
        "gamma_ci_excludes_zero": gamma_ci_excludes_zero,
        "theta_corr": round(theta_corr, 4), "theta_rmse": round(theta_rmse, 4),
        "n_draws": len(gamma_draws),
        "pass_fail": {
            "gamma_ci_covers_true": gamma_ci_covers_true,
            "gamma_ci_excludes_zero": gamma_ci_excludes_zero,
            "gamma_rel_bias": gamma_rel_bias < 0.3,
            "theta_corr": theta_corr > 0.9,
            "theta_rmse": theta_rmse < 0.2,
            "overall": all([gamma_ci_covers_true, gamma_ci_excludes_zero,
                           gamma_rel_bias < 0.3, theta_corr > 0.9, theta_rmse < 0.2]),
        },
    }


def evaluate_nuts(fit, true_params):
    summary = fit.summary()
    gamma_draws = fit.stan_variable("gamma")
    gamma_mean = float(np.mean(gamma_draws))
    gamma_sd = float(np.std(gamma_draws))
    gamma_q025 = float(np.percentile(gamma_draws, 2.5))
    gamma_q975 = float(np.percentile(gamma_draws, 97.5))
    gamma_bias = gamma_mean - GAMMA_TRUE
    gamma_rel_bias = abs(gamma_bias / GAMMA_TRUE)
    gamma_ci_covers_true = bool(gamma_q025 <= GAMMA_TRUE <= gamma_q975)
    gamma_ci_excludes_zero = bool(gamma_q025 > 0 or gamma_q975 < 0)

    theta_draws = fit.stan_variable("theta")
    theta_post_mean = np.mean(theta_draws, axis=0)
    theta_true = true_params["theta"]
    theta_corr = float(np.corrcoef(theta_post_mean, theta_true)[0, 1])
    theta_rmse = float(np.sqrt(np.mean((theta_post_mean - theta_true) ** 2)))

    diag = fit.diagnose()
    divergent = 0
    for line in diag.split('\n'):
        if 'divergent' in line.lower():
            parts = [w for w in line.split() if w.isdigit()]
            if parts:
                divergent = int(parts[0])
                break
    total_draws = fit.chains * 1000
    divergent_pct = 100.0 * divergent / total_draws

    max_rhat = float(summary['R_hat'].max()) if 'R_hat' in summary.columns else float(summary.iloc[:, -1].max())
    min_ess = float(summary['ESS_bulk'].min()) if 'ESS_bulk' in summary.columns else (
        float(summary['N_Eff'].min()) if 'N_Eff' in summary.columns else float('nan'))

    pf = {
        "gamma_ci_covers_true": gamma_ci_covers_true,
        "gamma_ci_excludes_zero": gamma_ci_excludes_zero,
        "gamma_rel_bias": gamma_rel_bias < 0.3,
        "theta_corr": theta_corr > 0.9,
        "theta_rmse": theta_rmse < 0.2,
        "max_rhat": max_rhat < 1.01,
        "divergent_pct": divergent_pct < 1.0,
    }
    pf["overall"] = all(pf.values())

    return {
        "gamma_mean": round(gamma_mean, 4), "gamma_sd": round(gamma_sd, 4),
        "gamma_q025": round(gamma_q025, 4), "gamma_q975": round(gamma_q975, 4),
        "gamma_bias": round(gamma_bias, 4), "gamma_rel_bias": round(gamma_rel_bias, 4),
        "gamma_ci_covers_true": gamma_ci_covers_true,
        "gamma_ci_excludes_zero": gamma_ci_excludes_zero,
        "theta_corr": round(theta_corr, 4), "theta_rmse": round(theta_rmse, 4),
        "max_rhat": round(max_rhat, 4), "divergent_count": divergent,
        "divergent_pct": round(divergent_pct, 4),
        "min_ess": round(min_ess, 1) if not np.isnan(min_ess) else None,
        "pass_fail": pf,
    }


def main():
    all_results = {}
    json_path = os.path.join(ARTIFACTS_DIR, "p1_variant_results.json")

    # =====================================================
    # Step 0: ADVI rerun with mean=False fix (baseline data)
    # =====================================================
    print("=" * 60)
    print("STEP 0: ADVI RERUN (mean=False fix)")
    print("=" * 60)
    sys.stdout.flush()

    rng = np.random.default_rng(SEED)
    stan_data_base, true_params_base = generate_data_binary(rng, n_items=100, exposure_rate=0.3)

    for label, stan_file in [("2pl", STAN_2PL), ("4pl", STAN_4PL)]:
        print(f"\n--- {label.upper()} ADVI ---")
        sys.stdout.flush()
        t0 = time.time()
        vb = fit_advi(stan_file, stan_data_base)
        dt = time.time() - t0
        r = evaluate_advi(vb, true_params_base, label)
        r["fit_time_sec"] = round(dt, 1)
        all_results[f"advi_fix_{label}"] = r
        print(f"  {dt:.1f}s | γ={r['gamma_mean']}±{r['gamma_sd']} | CI=[{r['gamma_q025']},{r['gamma_q975']}] | n_draws={r['n_draws']}")
        print(f"  θ_corr={r['theta_corr']} | {'PASS' if r['pass_fail']['overall'] else 'FAIL'}")
        sys.stdout.flush()

    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print("\nADVI rerun done. Intermediate results written.")
    print("ADVI_RERUN_DONE")
    sys.stdout.flush()

    # =====================================================
    # Variant A: N_items=300 (more information)
    # =====================================================
    print("\n" + "=" * 60)
    print("VARIANT A: N_items=300, exposure_rate=0.3")
    print("=" * 60)
    sys.stdout.flush()

    rng_a = np.random.default_rng(SEED)
    stan_data_a, true_params_a = generate_data_binary(rng_a, n_items=300, exposure_rate=0.3)
    print(f"  Parameters: {N_MODELS} θ + 300*4 item + 1 γ = 1251 total")
    sys.stdout.flush()

    t0 = time.time()
    fit_a = fit_nuts(STAN_4PL, stan_data_a, adapt_delta=0.95)
    dt = time.time() - t0
    r_a = evaluate_nuts(fit_a, true_params_a)
    r_a["fit_time_sec"] = round(dt, 1)
    r_a["variant"] = "N_items=300"
    all_results["variant_a_nitems300"] = r_a
    print(f"\n  VARIANT A: {dt:.1f}s | γ={r_a['gamma_mean']}±{r_a['gamma_sd']} | θ_corr={r_a['theta_corr']} | {'PASS' if r_a['pass_fail']['overall'] else 'FAIL'}")
    print("VARIANT_A_DONE")
    sys.stdout.flush()

    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    # =====================================================
    # Variant B: exposure_rate=0.5 (stronger signal)
    # =====================================================
    print("\n" + "=" * 60)
    print("VARIANT B: N_items=100, exposure_rate=0.5")
    print("=" * 60)
    sys.stdout.flush()

    rng_b = np.random.default_rng(SEED)
    stan_data_b, true_params_b = generate_data_binary(rng_b, n_items=100, exposure_rate=0.5)

    t0 = time.time()
    fit_b = fit_nuts(STAN_4PL, stan_data_b, adapt_delta=0.95)
    dt = time.time() - t0
    r_b = evaluate_nuts(fit_b, true_params_b)
    r_b["fit_time_sec"] = round(dt, 1)
    r_b["variant"] = "exposure_rate=0.5"
    all_results["variant_b_exp50"] = r_b
    print(f"\n  VARIANT B: {dt:.1f}s | γ={r_b['gamma_mean']}±{r_b['gamma_sd']} | θ_corr={r_b['theta_corr']} | {'PASS' if r_b['pass_fail']['overall'] else 'FAIL'}")
    print("VARIANT_B_DONE")
    sys.stdout.flush()

    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    # =====================================================
    # Variant C: continuous exposure
    # =====================================================
    print("\n" + "=" * 60)
    print("VARIANT C: N_items=100, continuous exposure (Beta)")
    print("=" * 60)
    sys.stdout.flush()

    rng_c = np.random.default_rng(SEED)
    stan_data_c, true_params_c, exp_stats = generate_data_continuous(rng_c, n_items=100)
    print(f"  Exposure stats: mean={exp_stats['mean']:.3f}, std={exp_stats['std']:.3f}, frac>0.5={exp_stats['frac_above_0.5']:.3f}")
    sys.stdout.flush()

    t0 = time.time()
    fit_c = fit_nuts(STAN_4PL, stan_data_c, adapt_delta=0.95)
    dt = time.time() - t0
    r_c = evaluate_nuts(fit_c, true_params_c)
    r_c["fit_time_sec"] = round(dt, 1)
    r_c["variant"] = "continuous_exposure"
    r_c["exposure_stats"] = exp_stats
    all_results["variant_c_continuous"] = r_c
    print(f"\n  VARIANT C: {dt:.1f}s | γ={r_c['gamma_mean']}±{r_c['gamma_sd']} | θ_corr={r_c['theta_corr']} | {'PASS' if r_c['pass_fail']['overall'] else 'FAIL'}")
    print("VARIANT_C_DONE")
    sys.stdout.flush()

    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    # =====================================================
    # Summary
    # =====================================================
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"{'Variant':<30} {'γ_mean':>8} {'γ_relb':>8} {'θ_corr':>8} {'θ_rmse':>8} {'Overall':>8} {'Time':>8}")
    for key, r in all_results.items():
        pf = r['pass_fail']
        print(f"{key:<30} {r['gamma_mean']:>8} {r['gamma_rel_bias']:>8} {r['theta_corr']:>8} {r['theta_rmse']:>8} {'PASS' if pf['overall'] else 'FAIL':>8} {r.get('fit_time_sec','?'):>8}")
    print("ALL_VARIANTS_DONE")
    sys.stdout.flush()


if __name__ == "__main__":
    main()

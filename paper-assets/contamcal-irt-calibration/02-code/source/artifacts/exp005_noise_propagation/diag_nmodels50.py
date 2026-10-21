"""Diagnostic: simple model, σ_e=0.1, N_models=50 — test if larger N fixes γ bias."""

import json
import os
import sys
import time

import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STAN_DIR = os.path.join(SCRIPT_DIR, "..", "exp006_irt_calibration")

# Redirect CmdStanPy temp files away from /tmp
STAN_TMP = os.path.join(SCRIPT_DIR, "stan_tmp")
os.makedirs(STAN_TMP, exist_ok=True)
os.environ["TMPDIR"] = STAN_TMP


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
    return {"y": y, "exposure": e_observed}


def main():
    import cmdstanpy

    sigma_e = 0.1
    n_models = 50
    n_items = 300
    true_gamma = 0.5
    seed = 42

    rng = np.random.default_rng(seed)
    synth = generate_synthetic_data(n_models, n_items, true_gamma, sigma_e, rng)

    stan_data = {
        "N_models": n_models,
        "N_items": n_items,
        "y": synth["y"].tolist(),
        "exposure": synth["exposure"].tolist(),
    }

    stan_file = os.path.join(STAN_DIR, "contam_irt_4pl_simple.stan")
    model = cmdstanpy.CmdStanModel(stan_file=stan_file)

    print(f"Fitting simple model: σ_e={sigma_e}, N_models={n_models}, N_items={n_items}, seed={seed}")
    sys.stdout.flush()

    t0 = time.time()
    fit = model.sample(
        data=stan_data,
        seed=seed,
        chains=4,
        iter_warmup=500,
        iter_sampling=1000,
        adapt_delta=0.95,
        max_treedepth=12,
        show_console=True,
        show_progress=False,
    )
    elapsed = time.time() - t0

    summary = fit.summary()
    rhat_col = next((c for c in ["R_hat", "Rhat"] if c in summary.columns), summary.columns[-1])
    max_rhat = float(summary[rhat_col].max())

    gamma_draws = fit.stan_variable("gamma")
    gamma_mean = float(np.mean(gamma_draws))
    gamma_sd = float(np.std(gamma_draws))
    gamma_q025 = float(np.percentile(gamma_draws, 2.5))
    gamma_q975 = float(np.percentile(gamma_draws, 97.5))
    gamma_rel_bias = (gamma_mean - true_gamma) / true_gamma

    ci_covers = gamma_q025 <= true_gamma <= gamma_q975

    cal_draws = fit.stan_variable("calibrated_score")
    q025 = np.percentile(cal_draws, 2.5, axis=0)
    q975 = np.percentile(cal_draws, 97.5, axis=0)
    ci_width = q975 - q025

    ess_cols = [c for c in summary.columns if "ess" in c.lower() or "ESS" in c]
    min_ess = float(summary[ess_cols[0]].min()) if ess_cols else -1

    diag = fit.diagnose()
    div_lines = [l for l in diag.split("\n") if "divergen" in l.lower()]

    result = {
        "experiment": "exp005_diag_nmodels50",
        "model": "simple",
        "sigma_e": sigma_e,
        "n_models": n_models,
        "n_items": n_items,
        "true_gamma": true_gamma,
        "seed": seed,
        "gamma_mean": round(gamma_mean, 4),
        "gamma_sd": round(gamma_sd, 4),
        "gamma_95ci": [round(gamma_q025, 4), round(gamma_q975, 4)],
        "gamma_rel_bias": round(gamma_rel_bias, 4),
        "ci_covers_true": ci_covers,
        "max_rhat": round(max_rhat, 4),
        "min_ess": round(min_ess, 0),
        "cal_ci_width_mean": round(float(np.mean(ci_width)), 4),
        "fit_time_sec": round(elapsed, 1),
        "divergent_info": div_lines,
    }

    print(f"\n{'='*60}")
    print(f"RESULTS (N_models={n_models}, σ_e={sigma_e}):")
    print(f"  γ_mean     = {result['gamma_mean']}")
    print(f"  γ_sd       = {result['gamma_sd']}")
    print(f"  γ_95CI     = {result['gamma_95ci']}")
    print(f"  γ_rel_bias = {result['gamma_rel_bias']:.1%}")
    print(f"  CI covers  = {result['ci_covers_true']}")
    print(f"  max Rhat   = {result['max_rhat']}")
    print(f"  min ESS    = {result['min_ess']}")
    print(f"  fit time   = {result['fit_time_sec']}s")
    print(f"{'='*60}")
    sys.stdout.flush()

    out_path = os.path.join(SCRIPT_DIR, "diag_nmodels50_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Saved to {out_path}")


if __name__ == "__main__":
    main()

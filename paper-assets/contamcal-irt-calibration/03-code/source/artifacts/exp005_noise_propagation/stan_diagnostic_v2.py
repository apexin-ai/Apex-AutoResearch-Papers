"""Minimal diagnostic: σ_e=0.1 with init values, after cleaning disk."""

import json
import os
import sys
import time

import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STAN_DIR = os.path.join(SCRIPT_DIR, "..", "exp006_irt_calibration")


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
    n_models, n_items, seed = 30, 300, 42
    rng = np.random.default_rng(seed)
    synth = generate_synthetic_data(n_models, n_items, 0.5, sigma_e, rng)

    stan_data = {
        "N_models": n_models, "N_items": n_items,
        "y": synth["y"].tolist(), "exposure": synth["exposure"].tolist(),
    }
    inits = {
        "theta": [0.0] * n_models, "a": [1.0] * n_items,
        "b": [0.0] * n_items, "c": [0.15] * n_items,
        "d": [0.85] * n_items, "gamma": 0.0,
    }

    stan_file = os.path.join(STAN_DIR, "contam_irt_4pl_simple.stan")
    model = cmdstanpy.CmdStanModel(stan_file=stan_file)

    sys.stdout.write(f"Starting fit: σ_e={sigma_e}, N={n_models}, seed={seed}, with inits\n")
    sys.stdout.flush()

    t0 = time.time()
    try:
        fit = model.sample(
            data=stan_data, seed=seed, inits=inits,
            chains=4, iter_warmup=500, iter_sampling=1000,
            adapt_delta=0.95, max_treedepth=12,
            show_console=True, show_progress=False,
        )
        elapsed = time.time() - t0

        summary = fit.summary()
        rhat_col = next((c for c in ["R_hat", "Rhat"] if c in summary.columns), summary.columns[-1])
        max_rhat = float(summary[rhat_col].max())

        cal_draws = fit.stan_variable("calibrated_score")
        q025 = np.percentile(cal_draws, 2.5, axis=0)
        q975 = np.percentile(cal_draws, 97.5, axis=0)
        ci_width = q975 - q025
        gamma_draws = fit.stan_variable("gamma")

        ess_cols = [c for c in summary.columns if "ess" in c.lower() or "ESS" in c]
        min_ess = float(summary[ess_cols[0]].min()) if ess_cols else -1

        result = {
            "status": "OK", "sigma_e": sigma_e, "n_models": n_models,
            "max_rhat": round(max_rhat, 4),
            "converged": max_rhat < 1.01,
            "ci_width_mean": round(float(np.mean(ci_width)), 4),
            "gamma_mean": round(float(np.mean(gamma_draws)), 4),
            "gamma_sd": round(float(np.std(gamma_draws)), 4),
            "min_ess": round(min_ess, 0),
            "elapsed_sec": round(elapsed, 1),
        }

        sys.stdout.write(f"\nRESULTS: {json.dumps(result, indent=2)}\n")
        sys.stdout.flush()

    except RuntimeError as e:
        elapsed = time.time() - t0
        result = {"status": "CRASHED", "error": str(e)[:500], "elapsed_sec": round(elapsed, 1)}
        sys.stdout.write(f"\nCRASHED after {elapsed:.0f}s: {e}\n")
        sys.stdout.flush()

    out_path = os.path.join(SCRIPT_DIR, "diagnostic_v2_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    sys.stdout.write(f"Saved to {out_path}\n")
    sys.stdout.flush()


if __name__ == "__main__":
    main()

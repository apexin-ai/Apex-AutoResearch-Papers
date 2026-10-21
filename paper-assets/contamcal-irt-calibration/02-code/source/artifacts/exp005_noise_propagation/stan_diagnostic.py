"""
Diagnostic script for exp_005 Stan convergence issues.
Tests simple model with σ_e=0.3, then σ_e=0.1, with various fixes.
"""

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

    true_cal = np.zeros(n_models)
    for i in range(n_models):
        total = 0.0
        for j in range(n_items):
            eta_clean = a[j] * (theta[i] - b[j])
            p_clean = c[j] + (d[j] - c[j]) * sigmoid(eta_clean)
            total += p_clean
        true_cal[i] = total / n_items

    return {
        "y": y, "exposure": e_observed, "true_cal": true_cal,
        "theta": theta, "a": a, "b": b, "c": c, "d": d,
        "gamma": gamma, "e_true": e_true,
    }


def make_inits(n_models, n_items):
    """Provide sensible initial values to avoid c > d at init."""
    return {
        "theta": [0.0] * n_models,
        "a": [1.0] * n_items,
        "b": [0.0] * n_items,
        "c": [0.15] * n_items,
        "d": [0.85] * n_items,
        "gamma": 0.0,
    }


def run_diagnostic(sigma_e, n_models, n_items, seed, use_inits=False, label=""):
    import cmdstanpy

    rng = np.random.default_rng(seed)
    synth = generate_synthetic_data(n_models, n_items, 0.5, sigma_e, rng)

    stan_data = {
        "N_models": int(n_models),
        "N_items": int(n_items),
        "y": synth["y"].tolist(),
        "exposure": synth["exposure"].tolist(),
    }

    stan_file = os.path.join(STAN_DIR, "contam_irt_4pl_simple.stan")
    model = cmdstanpy.CmdStanModel(stan_file=stan_file)

    sample_kwargs = {
        "data": stan_data,
        "seed": seed,
        "chains": 4,
        "iter_warmup": 500,
        "iter_sampling": 1000,
        "adapt_delta": 0.95,
        "max_treedepth": 12,
        "show_console": True,
        "show_progress": False,
    }

    if use_inits:
        sample_kwargs["inits"] = make_inits(n_models, n_items)

    tag = f"[{label}] σ_e={sigma_e}, N={n_models}, seed={seed}, inits={use_inits}"
    print(f"\n{'='*60}")
    print(f"TEST: {tag}")
    print(f"{'='*60}")

    t0 = time.time()
    try:
        fit = model.sample(**sample_kwargs)
        elapsed = time.time() - t0

        summary = fit.summary()
        rhat_col = next(
            (c for c in ["R_hat", "Rhat"] if c in summary.columns),
            summary.columns[-1],
        )
        max_rhat = float(summary[rhat_col].max())

        diag = fit.diagnose()
        print(f"\n--- DIAGNOSE OUTPUT ---\n{diag}")

        cal_draws = fit.stan_variable("calibrated_score")
        q025 = np.percentile(cal_draws, 2.5, axis=0)
        q975 = np.percentile(cal_draws, 97.5, axis=0)
        ci_width = q975 - q025

        gamma_draws = fit.stan_variable("gamma")

        print(f"\n--- RESULTS ---")
        print(f"Time: {elapsed:.0f}s")
        print(f"Max Rhat: {max_rhat:.4f}")
        print(f"Converged (Rhat<1.01): {max_rhat < 1.01}")
        print(f"CI width mean: {np.mean(ci_width):.4f}")
        print(f"CI width median: {np.median(ci_width):.4f}")
        print(f"gamma: {np.mean(gamma_draws):.4f} ± {np.std(gamma_draws):.4f} (true=0.5)")

        ess_cols = [c for c in summary.columns if "ess" in c.lower() or "ESS" in c]
        if ess_cols:
            min_ess = float(summary[ess_cols[0]].min())
            print(f"Min ESS ({ess_cols[0]}): {min_ess:.0f}")

        return {
            "status": "OK",
            "max_rhat": max_rhat,
            "converged": max_rhat < 1.01,
            "ci_width_mean": float(np.mean(ci_width)),
            "gamma_mean": float(np.mean(gamma_draws)),
            "elapsed": elapsed,
        }

    except RuntimeError as e:
        elapsed = time.time() - t0
        print(f"\n--- CRASHED after {elapsed:.0f}s ---")
        print(f"Error: {e}")
        return {"status": "CRASHED", "error": str(e), "elapsed": elapsed}


def main():
    results = {}

    # Test 1: σ_e=0.3, N=30, no inits (baseline)
    results["test1"] = run_diagnostic(0.3, 30, 300, 42, use_inits=False, label="Test1")

    # Test 2: σ_e=0.3, N=30, with inits
    results["test2"] = run_diagnostic(0.3, 30, 300, 42, use_inits=True, label="Test2")

    # Test 3: σ_e=0.1, N=30, with inits (reproduce crash with fix)
    results["test3"] = run_diagnostic(0.1, 30, 300, 42, use_inits=True, label="Test3")

    # Test 4: σ_e=0.1, N=50, with inits (more models)
    if results["test3"]["status"] == "CRASHED":
        results["test4"] = run_diagnostic(0.1, 50, 300, 42, use_inits=True, label="Test4")

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    for name, r in results.items():
        if r["status"] == "OK":
            print(f"  {name}: OK, Rhat={r['max_rhat']:.4f}, CI={r['ci_width_mean']:.4f}, γ={r['gamma_mean']:.4f}")
        else:
            print(f"  {name}: CRASHED")

    out_path = os.path.join(SCRIPT_DIR, "diagnostic_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()

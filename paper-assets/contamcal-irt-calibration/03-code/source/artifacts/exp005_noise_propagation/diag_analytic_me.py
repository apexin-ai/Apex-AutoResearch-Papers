"""Diagnostic: analytic ME model on σ_e=0.1 N=30 — does it fix γ bias?"""

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
    """Same DGP as stan_diagnostic_v2.py for apples-to-apples comparison."""
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

    return {"y": y, "exposure": e_observed, "tau_true": tau, "theta": theta}


def compute_analytical_tau_posterior(exposure, mu_tau=0.0, sigma_tau=1.0, sigma_e=0.1):
    sigma_tau_sq = sigma_tau ** 2
    sigma_e_sq = sigma_e ** 2
    denom = sigma_tau_sq + sigma_e_sq
    tau_post_mean = (exposure * sigma_tau_sq + mu_tau * sigma_e_sq) / denom
    tau_post_var = np.full_like(exposure, (sigma_tau_sq * sigma_e_sq) / denom)
    return tau_post_mean, tau_post_var


def main():
    import cmdstanpy

    sigma_e = 0.1
    n_models, n_items, seed = 30, 300, 42
    true_gamma = 0.5
    rng = np.random.default_rng(seed)
    synth = generate_synthetic_data(n_models, n_items, true_gamma, sigma_e, rng)

    tau_post_mean, tau_post_var = compute_analytical_tau_posterior(
        synth["exposure"], mu_tau=0.0, sigma_tau=1.0, sigma_e=sigma_e
    )

    stan_data = {
        "N_models": n_models,
        "N_items": n_items,
        "y": synth["y"].tolist(),
        "tau_post_mean": tau_post_mean.tolist(),
        "tau_post_var": tau_post_var.tolist(),
    }
    inits = {
        "theta": [0.0] * n_models,
        "a": [1.0] * n_items,
        "b": [0.0] * n_items,
        "c": [0.15] * n_items,
        "d": [0.85] * n_items,
        "gamma": 0.0,
    }

    stan_file = os.path.join(STAN_DIR, "contam_irt_4pl_me_analytic.stan")
    sys.stdout.write(f"Compiling {stan_file}\n")
    sys.stdout.flush()
    model = cmdstanpy.CmdStanModel(stan_file=stan_file)

    sys.stdout.write(f"Starting fit: analytic ME, σ_e={sigma_e}, N={n_models}, seed={seed}\n")
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

        gamma_draws = fit.stan_variable("gamma")
        gamma_mean = float(np.mean(gamma_draws))
        gamma_sd = float(np.std(gamma_draws))
        gamma_q025 = float(np.percentile(gamma_draws, 2.5))
        gamma_q975 = float(np.percentile(gamma_draws, 97.5))
        ci_covers = gamma_q025 <= true_gamma <= gamma_q975
        rel_bias = (gamma_mean - true_gamma) / true_gamma

        cal_draws = fit.stan_variable("calibrated_score")
        q025 = np.percentile(cal_draws, 2.5, axis=0)
        q975 = np.percentile(cal_draws, 97.5, axis=0)
        ci_width = q975 - q025

        ess_cols = [c for c in summary.columns if "ess" in c.lower() or "ESS" in c]
        min_ess = float(summary[ess_cols[0]].min()) if ess_cols else -1

        diag_text = fit.diagnose()
        divergent = 0
        for line in diag_text.split("\n"):
            if "divergent" in line.lower():
                parts = [w for w in line.split() if w.isdigit()]
                if parts:
                    divergent = int(parts[0])
                    break
        total_draws = 4 * 1000
        divergent_pct = 100.0 * divergent / total_draws

        n_params = n_models + 4 * n_items + 1  # theta + a,b,c,d + gamma (no tau!)

        result = {
            "status": "OK",
            "model": "analytic_me",
            "sigma_e": sigma_e,
            "n_models": n_models,
            "n_items": n_items,
            "true_gamma": true_gamma,
            "gamma_mean": round(gamma_mean, 4),
            "gamma_sd": round(gamma_sd, 4),
            "gamma_q025": round(gamma_q025, 4),
            "gamma_q975": round(gamma_q975, 4),
            "gamma_rel_bias": round(rel_bias, 4),
            "gamma_rel_bias_pct": f"{rel_bias*100:.1f}%",
            "ci_covers_true": ci_covers,
            "max_rhat": round(max_rhat, 4),
            "min_ess": round(min_ess, 0),
            "divergent_count": divergent,
            "divergent_pct": round(divergent_pct, 4),
            "ci_width_mean": round(float(np.mean(ci_width)), 4),
            "n_params": n_params,
            "elapsed_sec": round(elapsed, 1),
            "comparison_simple": {
                "gamma_mean": 0.7877,
                "gamma_rel_bias_pct": "+57.5%",
                "ci_covers_true": False,
            },
        }

        sys.stdout.write(f"\n{'='*60}\n")
        sys.stdout.write(f"RESULTS: analytic ME model\n")
        sys.stdout.write(f"  γ_mean={gamma_mean:.4f} (true={true_gamma})\n")
        sys.stdout.write(f"  γ_sd={gamma_sd:.4f}\n")
        sys.stdout.write(f"  γ 95%CI=[{gamma_q025:.4f}, {gamma_q975:.4f}]\n")
        sys.stdout.write(f"  rel_bias={rel_bias*100:.1f}%\n")
        sys.stdout.write(f"  CI covers true: {ci_covers}\n")
        sys.stdout.write(f"  max_Rhat={max_rhat:.4f}\n")
        sys.stdout.write(f"  min_ESS={min_ess:.0f}\n")
        sys.stdout.write(f"  divergent={divergent} ({divergent_pct:.2f}%)\n")
        sys.stdout.write(f"  n_params={n_params} (vs simple: same, vs full ME: {n_params + n_models*n_items})\n")
        sys.stdout.write(f"  elapsed={elapsed:.1f}s\n")
        sys.stdout.write(f"\nCOMPARISON:\n")
        sys.stdout.write(f"  simple model:     γ_mean=0.7877, rel_bias=+57.5%, CI covers=No\n")
        sys.stdout.write(f"  analytic ME:      γ_mean={gamma_mean:.4f}, rel_bias={rel_bias*100:+.1f}%, CI covers={ci_covers}\n")
        sys.stdout.write(f"  VERDICT: {'FIXED' if abs(rel_bias) < 0.15 and ci_covers else 'NOT FIXED'}\n")
        sys.stdout.write(f"{'='*60}\n")
        sys.stdout.flush()

    except RuntimeError as e:
        elapsed = time.time() - t0
        result = {"status": "CRASHED", "error": str(e)[:500], "elapsed_sec": round(elapsed, 1)}
        sys.stdout.write(f"\nCRASHED after {elapsed:.0f}s: {e}\n")
        sys.stdout.flush()

    out_path = os.path.join(SCRIPT_DIR, "diag_analytic_me_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    sys.stdout.write(f"Saved to {out_path}\n")
    sys.stdout.flush()


if __name__ == "__main__":
    main()

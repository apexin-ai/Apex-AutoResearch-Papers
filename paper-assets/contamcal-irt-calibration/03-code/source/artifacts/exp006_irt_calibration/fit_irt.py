# exp-006: IRT model fitting with CmdStanPy NUTS
# Fits 4PL+γ (with or without measurement error) per benchmark

import argparse
import json
import logging
import os
import sys
import time

import numpy as np
import cmdstanpy

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STAN_MODELS = {
    "me": os.path.join(SCRIPT_DIR, "contam_irt_4pl_me.stan"),
    "me_analytic": os.path.join(SCRIPT_DIR, "contam_irt_4pl_me_analytic.stan"),
    "simple": os.path.join(SCRIPT_DIR, "contam_irt_4pl_simple.stan"),
    "2pl": os.path.join(SCRIPT_DIR, "contam_irt_2pl.stan"),
}

NUTS_DEFAULTS = {
    "chains": 4,
    "iter_warmup": 1000,
    "iter_sampling": 2000,
    "adapt_delta": 0.95,
    "max_treedepth": 10,
    "seed": 42,
}


def load_matrix(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".npy":
        return np.load(path)
    elif ext == ".csv":
        return np.loadtxt(path, delimiter=",", skiprows=1)
    elif ext == ".json":
        with open(path) as f:
            return np.array(json.load(f))
    else:
        raise ValueError(f"Unsupported format: {ext}")


def compute_analytical_tau_posterior(exposure, mu_tau=0.0, sigma_tau=1.0, sigma_e=0.5):
    """Analytical posterior of τ given observed exposure e.

    τ prior: N(mu_tau, sigma_tau²)
    Observation: e ~ N(τ, sigma_e²)
    Posterior: τ|e ~ N(E[τ|e], Var[τ|e])

    Returns (tau_post_mean, tau_post_var) matrices.
    """
    sigma_tau_sq = sigma_tau ** 2
    sigma_e_sq = sigma_e ** 2
    denom = sigma_tau_sq + sigma_e_sq

    tau_post_mean = (exposure * sigma_tau_sq + mu_tau * sigma_e_sq) / denom
    tau_post_var = np.full_like(exposure, (sigma_tau_sq * sigma_e_sq) / denom)

    return tau_post_mean, tau_post_var


def prepare_stan_data(response_path, exposure_path, model_type="me"):
    y = load_matrix(response_path)
    exposure = load_matrix(exposure_path)
    assert y.shape == exposure.shape, (
        f"Shape mismatch: response {y.shape} vs exposure {exposure.shape}"
    )
    N_models, N_items = y.shape
    y_int = y.astype(int)
    assert np.all((y_int == 0) | (y_int == 1)), "Response matrix must be binary"

    data = {
        "N_models": int(N_models),
        "N_items": int(N_items),
        "y": y_int.tolist(),
    }

    if model_type == "me_analytic":
        tau_post_mean, tau_post_var = compute_analytical_tau_posterior(exposure)
        data["tau_post_mean"] = tau_post_mean.tolist()
        data["tau_post_var"] = tau_post_var.tolist()
        log.info("Analytical ME: eliminated %d latent τ params (N=%d × J=%d)",
                 N_models * N_items, N_models, N_items)
    else:
        data["exposure"] = exposure.tolist()

    return data


def fit_model(stan_file, stan_data, nuts_kwargs=None):
    kwargs = {**NUTS_DEFAULTS}
    if nuts_kwargs:
        kwargs.update(nuts_kwargs)

    log.info("Compiling Stan model: %s", os.path.basename(stan_file))
    model = cmdstanpy.CmdStanModel(stan_file=stan_file)

    log.info(
        "Fitting: %d models × %d items, %d chains × %d samples",
        stan_data["N_models"],
        stan_data["N_items"],
        kwargs["chains"],
        kwargs["iter_sampling"],
    )
    t0 = time.time()
    fit = model.sample(data=stan_data, show_progress=True, **kwargs)
    elapsed = time.time() - t0
    log.info("Sampling completed in %.1fs", elapsed)

    return fit, elapsed


def check_convergence(fit):
    summary = fit.summary()
    diagnostics = {}

    if "R_hat" in summary.columns:
        rhat_col = "R_hat"
    elif "Rhat" in summary.columns:
        rhat_col = "Rhat"
    else:
        rhat_col = summary.columns[-1]

    max_rhat = float(summary[rhat_col].max())
    diagnostics["max_rhat"] = round(max_rhat, 4)
    diagnostics["rhat_ok"] = max_rhat < 1.01

    for col in ["N_Eff", "ESS_bulk", "N_eff"]:
        if col in summary.columns:
            min_ess = float(summary[col].min())
            diagnostics["min_ess"] = round(min_ess, 1)
            diagnostics["ess_ok"] = min_ess > 400
            break

    diag_text = fit.diagnose()
    divergent = 0
    for line in diag_text.split("\n"):
        if "divergent" in line.lower():
            parts = [w for w in line.split() if w.isdigit()]
            if parts:
                divergent = int(parts[0])
                break
    total_draws = fit.chains * NUTS_DEFAULTS["iter_sampling"]
    divergent_pct = 100.0 * divergent / total_draws
    diagnostics["divergent_count"] = divergent
    diagnostics["divergent_pct"] = round(divergent_pct, 4)
    diagnostics["divergent_ok"] = divergent_pct < 0.1

    diagnostics["all_ok"] = all(
        diagnostics.get(k, True) for k in ["rhat_ok", "ess_ok", "divergent_ok"]
    )

    return diagnostics


def _summarize_draws(draws):
    """Summarize MCMC draws into mean/sd/quantiles."""
    return {
        "mean": np.round(np.mean(draws, axis=0), 4).tolist(),
        "sd": np.round(np.std(draws, axis=0), 4).tolist(),
        "q025": np.round(np.percentile(draws, 2.5, axis=0), 4).tolist(),
        "q975": np.round(np.percentile(draws, 97.5, axis=0), 4).tolist(),
        "q10": np.round(np.percentile(draws, 10, axis=0), 4).tolist(),
        "q90": np.round(np.percentile(draws, 90, axis=0), 4).tolist(),
        "q25": np.round(np.percentile(draws, 25, axis=0), 4).tolist(),
        "q75": np.round(np.percentile(draws, 75, axis=0), 4).tolist(),
    }


def extract_results(fit, stan_data, model_type):
    results = {}

    gamma_draws = fit.stan_variable("gamma")
    results["gamma"] = {
        "mean": round(float(np.mean(gamma_draws)), 4),
        "sd": round(float(np.std(gamma_draws)), 4),
        "q025": round(float(np.percentile(gamma_draws, 2.5)), 4),
        "q975": round(float(np.percentile(gamma_draws, 97.5)), 4),
        "q05": round(float(np.percentile(gamma_draws, 5)), 4),
        "q95": round(float(np.percentile(gamma_draws, 95)), 4),
        "q10": round(float(np.percentile(gamma_draws, 10)), 4),
        "q90": round(float(np.percentile(gamma_draws, 90)), 4),
        "q25": round(float(np.percentile(gamma_draws, 25)), 4),
        "q75": round(float(np.percentile(gamma_draws, 75)), 4),
    }

    theta_draws = fit.stan_variable("theta")  # (n_draws, N_models)
    theta_mean = np.mean(theta_draws, axis=0)
    theta_sd = np.std(theta_draws, axis=0)
    results["theta"] = {
        "mean": np.round(theta_mean, 4).tolist(),
        "sd": np.round(theta_sd, 4).tolist(),
    }

    for param in ["a", "b"]:
        draws = fit.stan_variable(param)
        results[param] = {
            "mean": np.round(np.mean(draws, axis=0), 4).tolist(),
            "sd": np.round(np.std(draws, axis=0), 4).tolist(),
        }

    if model_type != "2pl":
        for param in ["c", "d"]:
            draws = fit.stan_variable(param)
            results[param] = {
                "mean": np.round(np.mean(draws, axis=0), 4).tolist(),
                "sd": np.round(np.std(draws, axis=0), 4).tolist(),
            }

    if model_type == "me":
        sigma_e_draws = fit.stan_variable("sigma_e")
        results["sigma_e"] = {
            "mean": round(float(np.mean(sigma_e_draws)), 4),
            "sd": round(float(np.std(sigma_e_draws)), 4),
            "q025": round(float(np.percentile(sigma_e_draws, 2.5)), 4),
            "q975": round(float(np.percentile(sigma_e_draws, 97.5)), 4),
        }

    # ME correction operates through fitting (wider gamma posteriors from E[τ|e]),
    # so calibrated_score already reflects ME uncertainty for me_analytic model.
    cal_draws = fit.stan_variable("calibrated_score")  # (n_draws, N_models)
    cal_mean = np.mean(cal_draws, axis=0)
    cal_sd = np.std(cal_draws, axis=0)
    cal_q025 = np.percentile(cal_draws, 2.5, axis=0)
    cal_q975 = np.percentile(cal_draws, 97.5, axis=0)
    cal_q10 = np.percentile(cal_draws, 10, axis=0)
    cal_q90 = np.percentile(cal_draws, 90, axis=0)
    cal_q25 = np.percentile(cal_draws, 25, axis=0)
    cal_q75 = np.percentile(cal_draws, 75, axis=0)

    results["calibrated_scores"] = {
        "mean": np.round(cal_mean, 4).tolist(),
        "sd": np.round(cal_sd, 4).tolist(),
        "q025": np.round(cal_q025, 4).tolist(),
        "q975": np.round(cal_q975, 4).tolist(),
        "q10": np.round(cal_q10, 4).tolist(),
        "q90": np.round(cal_q90, 4).tolist(),
        "q25": np.round(cal_q25, 4).tolist(),
        "q75": np.round(cal_q75, 4).tolist(),
    }

    return results


def main():
    parser = argparse.ArgumentParser(description="Fit contamination-augmented IRT model")
    parser.add_argument("--response-matrix", required=True, help="Path to binary response matrix (N_models × N_items)")
    parser.add_argument("--exposure-matrix", required=True, help="Path to exposure score matrix (N_models × N_items)")
    parser.add_argument("--benchmark", required=True, help="Benchmark name (for output labeling)")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    parser.add_argument("--model-type", choices=["me", "me_analytic", "simple", "2pl"], default="me_analytic",
                        help="Stan model variant. me_analytic recommended for large benchmarks (no latent τ).")
    parser.add_argument("--adapt-delta", type=float, default=0.95)
    parser.add_argument("--max-treedepth", type=int, default=10)
    parser.add_argument("--chains", type=int, default=4)
    parser.add_argument("--warmup", type=int, default=1000)
    parser.add_argument("--samples", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    log.info("Benchmark: %s | Model: %s", args.benchmark, args.model_type)

    stan_file = STAN_MODELS[args.model_type]
    stan_data = prepare_stan_data(args.response_matrix, args.exposure_matrix, args.model_type)
    log.info("Data: %d models × %d items", stan_data["N_models"], stan_data["N_items"])

    nuts_kwargs = {
        "chains": args.chains,
        "iter_warmup": args.warmup,
        "iter_sampling": args.samples,
        "adapt_delta": args.adapt_delta,
        "max_treedepth": args.max_treedepth,
        "seed": args.seed,
    }

    fit, elapsed = fit_model(stan_file, stan_data, nuts_kwargs)
    diagnostics = check_convergence(fit)
    log.info(
        "Convergence: Rhat_max=%.4f, ESS_min=%.0f, divergent=%.2f%% → %s",
        diagnostics["max_rhat"],
        diagnostics.get("min_ess", float("nan")),
        diagnostics["divergent_pct"],
        "OK" if diagnostics["all_ok"] else "WARNING",
    )

    if not diagnostics["all_ok"]:
        log.warning("Convergence issues detected. Consider increasing adapt_delta or warmup.")

    results = extract_results(fit, stan_data, args.model_type)

    output = {
        "benchmark": args.benchmark,
        "model_type": args.model_type,
        "stan_file": os.path.basename(stan_file),
        "fit_time_sec": round(elapsed, 1),
        "nuts_config": nuts_kwargs,
        "diagnostics": diagnostics,
        "parameters": results,
    }

    out_path = os.path.join(
        args.output_dir, f"{args.benchmark}_{args.model_type}_results.json"
    )
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    log.info("Results written to %s", out_path)

    cal = results["calibrated_scores"]
    cal_path = os.path.join(
        args.output_dir, f"{args.benchmark}_{args.model_type}_calibrated.csv"
    )
    with open(cal_path, "w") as f:
        f.write("model_idx,cal_mean,cal_sd,cal_q025,cal_q975,cal_q10,cal_q90,cal_q25,cal_q75\n")
        for i in range(len(cal["mean"])):
            f.write(
                f"{i},{cal['mean'][i]},{cal['sd'][i]},"
                f"{cal['q025'][i]},{cal['q975'][i]},"
                f"{cal['q10'][i]},{cal['q90'][i]},"
                f"{cal['q25'][i]},{cal['q75'][i]}\n"
            )
    log.info("Calibrated scores written to %s", cal_path)


if __name__ == "__main__":
    main()

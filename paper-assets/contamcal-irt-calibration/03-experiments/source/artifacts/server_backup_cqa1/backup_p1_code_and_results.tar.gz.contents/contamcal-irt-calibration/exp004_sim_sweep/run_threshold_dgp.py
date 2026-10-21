#!/usr/bin/env python3
"""
Threshold DGP simulation: test linear 2PL+gamma model under non-linear (step-function) contamination.

Conditions:
  - Threshold DGP: gamma_effective = 0.5 if exposure > threshold else 0, thresholds = {0.3, 0.5, 0.7}
  - Linear DGP (sanity check): gamma_effective = 0.5 * exposure
  - N_items=300, N_models(J)=16, 10 seeds per condition
  - Fit with 2PL+gamma Stan model (identical to contam_irt_2pl_gamma.stan, stripped of generated quantities for speed)
"""

import json, os, sys, time
import numpy as np
from scipy.special import expit
from pathlib import Path
import cmdstanpy

os.environ.setdefault("TMPDIR", "/root/autodl-tmp/tmp_sim")
os.makedirs(os.environ["TMPDIR"], exist_ok=True)

N_ITEMS = 300
N_MODELS = 16
GAMMA_TRUE = 0.5
N_SEEDS = 10
THRESHOLDS = [0.3, 0.5, 0.7]

SCRIPT_DIR = Path(__file__).parent
STAN_FILE = str(SCRIPT_DIR / "contam_irt_2pl_gamma_sim.stan")
RESULTS_DIR = SCRIPT_DIR / "results_threshold_dgp"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def generate_2pl_data(rng, dgp_type, threshold=None):
    theta = rng.standard_normal(N_MODELS)
    a = rng.lognormal(0, 0.5, N_ITEMS)
    b = rng.standard_normal(N_ITEMS)

    exposure = rng.uniform(0, 1, (N_MODELS, N_ITEMS))

    if dgp_type == "linear":
        contamination = GAMMA_TRUE * exposure
    elif dgp_type == "threshold":
        contamination = np.where(exposure > threshold, GAMMA_TRUE, 0.0)
    else:
        raise ValueError(dgp_type)

    eta = np.outer(np.ones(N_MODELS), a) * (theta[:, None] - b[None, :]) + contamination
    prob = expit(eta)
    y = rng.binomial(1, prob)

    true_params = {"theta": theta, "a": a, "b": b}
    stan_data = {
        "N_models": N_MODELS,
        "N_items": N_ITEMS,
        "y": y.tolist(),
        "exposure": exposure.tolist(),
    }
    return stan_data, true_params, exposure, contamination


def fit_model(stan_model, stan_data, seed=42):
    fit = stan_model.sample(
        data=stan_data,
        chains=4,
        parallel_chains=4,
        iter_warmup=500,
        iter_sampling=1000,
        seed=seed,
        adapt_delta=0.95,
        max_treedepth=10,
        show_progress=False,
    )
    return fit


def compute_ppp(fit, stan_data):
    y_obs = np.array(stan_data["y"])
    exposure = np.array(stan_data["exposure"])
    T_obs = float(y_obs.sum())

    gamma_draws = fit.stan_variable("gamma")
    theta_draws = fit.stan_variable("theta")
    a_draws = fit.stan_variable("a")
    b_draws = fit.stan_variable("b")

    n_draws = len(gamma_draws)
    step = max(1, n_draws // 200)
    rng = np.random.default_rng(99999)
    n_exceed = 0
    n_used = 0

    for s in range(0, n_draws, step):
        eta = (np.outer(np.ones(N_MODELS), a_draws[s])
               * (theta_draws[s][:, None] - b_draws[s][None, :])
               + gamma_draws[s] * exposure)
        prob = expit(eta)
        y_rep = rng.binomial(1, prob)
        if y_rep.sum() >= T_obs:
            n_exceed += 1
        n_used += 1

    return n_exceed / n_used if n_used > 0 else float("nan")


def evaluate_fit(fit, true_params):
    gamma_draws = fit.stan_variable("gamma")

    gamma_mean = float(np.mean(gamma_draws))
    gamma_sd = float(np.std(gamma_draws))
    gamma_q025 = float(np.percentile(gamma_draws, 2.5))
    gamma_q975 = float(np.percentile(gamma_draws, 97.5))

    gamma_bias = gamma_mean - GAMMA_TRUE
    relative_ratio = gamma_mean / GAMMA_TRUE
    ci95_covers = bool(gamma_q025 <= GAMMA_TRUE <= gamma_q975)
    p_gamma_neg = float(np.mean(gamma_draws < 0))

    theta_draws = fit.stan_variable("theta")
    theta_post_mean = np.mean(theta_draws, axis=0)
    theta_corr = float(np.corrcoef(theta_post_mean, true_params["theta"])[0, 1])

    sampler_vars = fit.method_variables()
    divergent = int(np.sum(sampler_vars.get("divergent__", [0])))

    return {
        "gamma_mean": round(gamma_mean, 4),
        "gamma_sd": round(gamma_sd, 4),
        "gamma_q025": round(gamma_q025, 4),
        "gamma_q975": round(gamma_q975, 4),
        "gamma_bias": round(gamma_bias, 4),
        "relative_ratio": round(relative_ratio, 4),
        "ci95_covers": ci95_covers,
        "p_gamma_neg": round(p_gamma_neg, 4),
        "theta_corr": round(theta_corr, 4),
        "divergent_count": divergent,
    }


def run_one(stan_model, dgp_type, threshold, seed):
    rng = np.random.default_rng(seed * 10000 + 42)
    t0 = time.time()

    stan_data, true_params, exposure, contamination = generate_2pl_data(
        rng, dgp_type, threshold
    )
    frac_affected = float(np.mean(contamination > 0))

    try:
        fit = fit_model(stan_model, stan_data, seed=seed)
        metrics = evaluate_fit(fit, true_params)
        metrics["ppp"] = round(compute_ppp(fit, stan_data), 4)
        metrics["success"] = True
    except Exception as e:
        metrics = {"success": False, "error": str(e)}

    metrics["fit_time_sec"] = round(time.time() - t0, 1)
    metrics["seed"] = seed
    metrics["frac_affected"] = round(frac_affected, 4)
    return metrics


def main():
    print("Compiling 2PL+gamma Stan model (sim variant)...", flush=True)
    stan_model = cmdstanpy.CmdStanModel(stan_file=STAN_FILE)
    print("Model compiled.", flush=True)

    conditions = []
    for thr in THRESHOLDS:
        conditions.append(("threshold", thr, f"threshold_{thr}"))
    conditions.append(("linear", None, "linear_0.5"))

    seeds = list(range(N_SEEDS))
    total = len(conditions) * len(seeds)
    done = 0
    t_start = time.time()
    all_results = {}

    for dgp_type, threshold, cond_name in conditions:
        print(f"\n{'='*60}", flush=True)
        print(f"Condition: {cond_name}", flush=True)
        print(f"{'='*60}", flush=True)

        runs = []
        for seed in seeds:
            done += 1
            elapsed = time.time() - t_start
            eta_min = (elapsed / done * (total - done) / 60) if done > 0 else 0
            print(f"  [{done}/{total}] seed={seed} (ETA {eta_min:.1f}min)", flush=True)

            metrics = run_one(stan_model, dgp_type, threshold, seed)
            runs.append(metrics)

            if metrics.get("success"):
                print(f"    gamma={metrics['gamma_mean']:.4f} +/- {metrics['gamma_sd']:.4f}, "
                      f"ratio={metrics['relative_ratio']:.3f}, "
                      f"P(g<0)={metrics['p_gamma_neg']:.4f}, "
                      f"PPP={metrics['ppp']:.3f}, "
                      f"div={metrics['divergent_count']}, "
                      f"time={metrics['fit_time_sec']:.0f}s", flush=True)
            else:
                print(f"    FAILED: {metrics.get('error', '?')}", flush=True)

        result_path = RESULTS_DIR / f"{cond_name}.json"
        with open(result_path, "w") as f:
            json.dump({
                "condition": cond_name,
                "dgp_type": dgp_type,
                "threshold": threshold,
                "gamma_true": GAMMA_TRUE,
                "n_items": N_ITEMS,
                "n_models": N_MODELS,
                "runs": runs,
            }, f, indent=2)

        all_results[cond_name] = runs

    print(f"\n\n{'='*80}", flush=True)
    print("SUMMARY", flush=True)
    print(f"{'='*80}", flush=True)
    print(f"{'Condition':<20} {'g_hat':>8} {'+/-sd':>8} {'Ratio':>8} {'CI95cov':>8} {'P(g<0)':>8} {'PPP':>8}", flush=True)
    print("-" * 80, flush=True)

    for dgp_type, threshold, cond_name in conditions:
        runs = [r for r in all_results[cond_name] if r.get("success")]
        if not runs:
            print(f"{cond_name:<20} NO SUCCESSFUL RUNS", flush=True)
            continue
        gm = [r["gamma_mean"] for r in runs]
        rr = [r["relative_ratio"] for r in runs]
        ci = [r["ci95_covers"] for r in runs]
        pn = [r["p_gamma_neg"] for r in runs]
        pp = [r["ppp"] for r in runs]
        fa = [r["frac_affected"] for r in runs]

        print(f"{cond_name:<20} {np.mean(gm):>8.4f} {np.std(gm):>8.4f} "
              f"{np.mean(rr):>8.4f} {np.mean(ci):>8.3f} "
              f"{np.mean(pn):>8.4f} {np.mean(pp):>8.4f}", flush=True)
        print(f"  frac_affected={np.mean(fa):.3f}", flush=True)

    total_time = time.time() - t_start
    print(f"\n=== COMPLETE ({total_time/60:.1f}min) ===", flush=True)
    print("THRESHOLD_DGP_DONE", flush=True)


if __name__ == "__main__":
    main()

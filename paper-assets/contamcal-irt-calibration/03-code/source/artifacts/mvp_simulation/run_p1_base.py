# P1 Base Condition: 2PL+γ and 4PL+γ IRT, ADVI then NUTS
# N_items=100 for CPU feasibility. Order: 2PL ADVI → 2PL NUTS → 4PL ADVI → 4PL NUTS

import json
import os
import sys
import time
import numpy as np
from scipy.special import expit
import cmdstanpy

SEED = 42
N_MODELS = 50
N_ITEMS = 100
GAMMA_TRUE = 0.5
EXPOSURE_RATE = 0.3

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


def generate_data(rng):
    theta = rng.standard_normal(N_MODELS)
    a = rng.lognormal(0, 0.5, N_ITEMS)
    b = rng.standard_normal(N_ITEMS)
    c = rng.beta(5, 20, N_ITEMS)
    d = rng.beta(20, 5, N_ITEMS)
    exposure = rng.binomial(1, EXPOSURE_RATE, (N_MODELS, N_ITEMS)).astype(float)

    eta = np.outer(np.ones(N_MODELS), a) * (
        theta[:, None] - b[None, :]
    ) + GAMMA_TRUE * exposure
    prob = c[None, :] + (d[None, :] - c[None, :]) * expit(eta)
    y = rng.binomial(1, prob)

    true_params = {"theta": theta, "a": a, "b": b, "c": c, "d": d}
    stan_data = {
        "N_models": N_MODELS,
        "N_items": N_ITEMS,
        "y": y.tolist(),
        "exposure": exposure.tolist(),
    }
    return stan_data, true_params


def fit_advi(stan_file, stan_data, seed=SEED):
    model = cmdstanpy.CmdStanModel(stan_file=stan_file)
    vb = model.variational(
        data=stan_data,
        seed=seed,
        algorithm="fullrank",
        output_samples=2000,
    )
    return vb


def fit_nuts(stan_file, stan_data, adapt_delta=0.95, max_treedepth=10):
    model = cmdstanpy.CmdStanModel(stan_file=stan_file)
    fit = model.sample(
        data=stan_data,
        chains=4,
        iter_warmup=1000,
        iter_sampling=1000,
        seed=SEED,
        adapt_delta=adapt_delta,
        max_treedepth=max_treedepth,
        show_progress=True,
    )
    return fit


def evaluate_advi(vb, true_params, model_name):
    # mean=False to get variational draws, not just the mean
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

    metrics = {
        "model": model_name,
        "method": "ADVI",
        "gamma_mean": round(gamma_mean, 4),
        "gamma_sd": round(gamma_sd, 4),
        "gamma_q025": round(gamma_q025, 4),
        "gamma_q975": round(gamma_q975, 4),
        "gamma_bias": round(gamma_bias, 4),
        "gamma_rel_bias": round(gamma_rel_bias, 4),
        "gamma_ci_covers_true": gamma_ci_covers_true,
        "gamma_ci_excludes_zero": gamma_ci_excludes_zero,
        "theta_corr": round(theta_corr, 4),
        "theta_rmse": round(theta_rmse, 4),
    }

    pf = {}
    pf["gamma_ci_covers_true"] = gamma_ci_covers_true
    pf["gamma_ci_excludes_zero"] = gamma_ci_excludes_zero
    pf["gamma_rel_bias"] = gamma_rel_bias < PASS_THRESHOLDS["gamma_rel_bias"]
    pf["theta_corr"] = theta_corr > PASS_THRESHOLDS["theta_corr"]
    pf["theta_rmse"] = theta_rmse < PASS_THRESHOLDS["theta_rmse"]
    pf["overall"] = all(pf.values())
    metrics["pass_fail"] = pf
    return metrics


def evaluate_nuts(fit, true_params, model_name):
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

    num_chains = fit.chains
    total_draws = num_chains * 1000
    divergent_pct = 100.0 * divergent / total_draws

    if 'R_hat' in summary.columns:
        max_rhat = float(summary['R_hat'].max())
    else:
        max_rhat = float(summary.iloc[:, -1].max())

    if 'N_Eff' in summary.columns:
        min_ess = float(summary['N_Eff'].min())
    elif 'ESS_bulk' in summary.columns:
        min_ess = float(summary['ESS_bulk'].min())
    else:
        min_ess = float('nan')

    metrics = {
        "model": model_name,
        "method": "NUTS",
        "gamma_mean": round(gamma_mean, 4),
        "gamma_sd": round(gamma_sd, 4),
        "gamma_q025": round(gamma_q025, 4),
        "gamma_q975": round(gamma_q975, 4),
        "gamma_bias": round(gamma_bias, 4),
        "gamma_rel_bias": round(gamma_rel_bias, 4),
        "gamma_ci_covers_true": gamma_ci_covers_true,
        "gamma_ci_excludes_zero": gamma_ci_excludes_zero,
        "theta_corr": round(theta_corr, 4),
        "theta_rmse": round(theta_rmse, 4),
        "max_rhat": round(max_rhat, 4),
        "divergent_count": divergent,
        "divergent_pct": round(divergent_pct, 4),
        "min_ess": round(min_ess, 1) if not np.isnan(min_ess) else None,
    }

    pf = {}
    pf["gamma_ci_covers_true"] = gamma_ci_covers_true
    pf["gamma_ci_excludes_zero"] = gamma_ci_excludes_zero
    pf["gamma_rel_bias"] = gamma_rel_bias < PASS_THRESHOLDS["gamma_rel_bias"]
    pf["theta_corr"] = theta_corr > PASS_THRESHOLDS["theta_corr"]
    pf["theta_rmse"] = theta_rmse < PASS_THRESHOLDS["theta_rmse"]
    pf["max_rhat"] = max_rhat < PASS_THRESHOLDS["max_rhat"]
    pf["divergent_pct"] = divergent_pct < PASS_THRESHOLDS["divergent_pct"]
    pf["overall"] = all(pf.values())
    metrics["pass_fail"] = pf
    return metrics


def fmt_pf(v):
    return "PASS" if v else "**FAIL**"


def write_markdown(all_results):
    lines = [
        "# P1 Base Condition Results",
        "",
        f"- N_models={N_MODELS}, N_items={N_ITEMS}, γ_true={GAMMA_TRUE}, exposure_rate={EXPOSURE_RATE}",
        f"- seed={SEED}",
        "",
    ]

    for key in ["2pl_advi", "2pl_nuts", "4pl_advi", "4pl_nuts"]:
        if key not in all_results:
            continue
        r = all_results[key]
        pf = r["pass_fail"]
        label = key.upper().replace("_", " ")
        lines += [f"## {label}", ""]
        lines += [
            "| Metric | Value | Threshold | Result |",
            "|--------|-------|-----------|--------|",
            f"| γ mean (sd) | {r['gamma_mean']} ({r['gamma_sd']}) | — | — |",
            f"| γ 95% CI | [{r['gamma_q025']}, {r['gamma_q975']}] | — | — |",
            f"| γ bias | {r['gamma_bias']} | — | — |",
            f"| γ relative bias | {r['gamma_rel_bias']} | < 0.3 | {fmt_pf(pf['gamma_rel_bias'])} |",
            f"| γ CI covers true | {r['gamma_ci_covers_true']} | Yes | {fmt_pf(pf['gamma_ci_covers_true'])} |",
            f"| γ CI excludes 0 | {r['gamma_ci_excludes_zero']} | Yes | {fmt_pf(pf['gamma_ci_excludes_zero'])} |",
            f"| θ correlation | {r['theta_corr']} | > 0.9 | {fmt_pf(pf['theta_corr'])} |",
            f"| θ RMSE | {r['theta_rmse']} | < 0.2 | {fmt_pf(pf['theta_rmse'])} |",
        ]
        if "max_rhat" in r:
            lines.append(f"| Max R-hat | {r['max_rhat']} | < 1.01 | {fmt_pf(pf['max_rhat'])} |")
            lines.append(f"| Divergent | {r['divergent_count']} ({r['divergent_pct']}%) | < 1% | {fmt_pf(pf['divergent_pct'])} |")
            lines.append(f"| Min ESS | {r['min_ess']} | — | — |")
        if "fit_time_sec" in r:
            lines.append(f"| Fit time | {r['fit_time_sec']}s | — | — |")
        lines += ["", f"**Overall: {'PASS' if pf['overall'] else 'FAIL'}**", ""]

    return "\n".join(lines)


def main():
    rng = np.random.default_rng(SEED)
    all_results = {"config": {
        "N_models": N_MODELS, "N_items": N_ITEMS,
        "gamma_true": GAMMA_TRUE, "exposure_rate": EXPOSURE_RATE, "seed": SEED,
    }}

    print("=== Generating data ===")
    stan_data, true_params = generate_data(rng)
    sys.stdout.flush()

    # --- 2PL ADVI ---
    print("\n=== 2PL+γ ADVI ===")
    sys.stdout.flush()
    t0 = time.time()
    vb_2pl = fit_advi(STAN_2PL, stan_data)
    t_2pl_advi = time.time() - t0
    r = evaluate_advi(vb_2pl, true_params, "2pl")
    r["fit_time_sec"] = round(t_2pl_advi, 1)
    all_results["2pl_advi"] = r
    print(f"  Time: {t_2pl_advi:.1f}s | γ={r['gamma_mean']} | θ_corr={r['theta_corr']} | {'PASS' if r['pass_fail']['overall'] else 'FAIL'}")
    sys.stdout.flush()

    # Write intermediate result immediately
    json_path = os.path.join(ARTIFACTS_DIR, "p1_base_results.json")
    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"  >> Intermediate results written (2PL ADVI)")
    print(f"\n=== 2PL ADVI RESULT: {'PASS' if r['pass_fail']['overall'] else 'FAIL'} ===")
    sys.stdout.flush()

    # --- 2PL NUTS ---
    print("\n=== 2PL+γ NUTS ===")
    sys.stdout.flush()
    t0 = time.time()
    fit_2pl = fit_nuts(STAN_2PL, stan_data, adapt_delta=0.95)
    t_2pl_nuts = time.time() - t0
    r = evaluate_nuts(fit_2pl, true_params, "2pl")
    r["fit_time_sec"] = round(t_2pl_nuts, 1)
    all_results["2pl_nuts"] = r
    print(f"  Time: {t_2pl_nuts:.1f}s | γ={r['gamma_mean']} | θ_corr={r['theta_corr']} | {'PASS' if r['pass_fail']['overall'] else 'FAIL'}")
    sys.stdout.flush()

    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    # --- 4PL ADVI ---
    print("\n=== 4PL+γ ADVI ===")
    sys.stdout.flush()
    t0 = time.time()
    vb_4pl = fit_advi(STAN_4PL, stan_data)
    t_4pl_advi = time.time() - t0
    r = evaluate_advi(vb_4pl, true_params, "4pl")
    r["fit_time_sec"] = round(t_4pl_advi, 1)
    all_results["4pl_advi"] = r
    print(f"  Time: {t_4pl_advi:.1f}s | γ={r['gamma_mean']} | θ_corr={r['theta_corr']} | {'PASS' if r['pass_fail']['overall'] else 'FAIL'}")
    sys.stdout.flush()

    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    # --- 4PL NUTS ---
    print("\n=== 4PL+γ NUTS ===")
    sys.stdout.flush()
    t0 = time.time()
    fit_4pl = fit_nuts(STAN_4PL, stan_data, adapt_delta=0.95)
    t_4pl_nuts = time.time() - t0
    r = evaluate_nuts(fit_4pl, true_params, "4pl")
    r["fit_time_sec"] = round(t_4pl_nuts, 1)
    all_results["4pl_nuts"] = r
    print(f"  Time: {t_4pl_nuts:.1f}s | γ={r['gamma_mean']} | θ_corr={r['theta_corr']} | {'PASS' if r['pass_fail']['overall'] else 'FAIL'}")
    sys.stdout.flush()

    # Retry 4PL NUTS if convergence issues
    if r["divergent_pct"] > 5.0 or r["max_rhat"] > 1.1:
        print("\n=== 4PL+γ NUTS retry (adapt_delta=0.99, treedepth=12) ===")
        sys.stdout.flush()
        t0 = time.time()
        fit_4pl = fit_nuts(STAN_4PL, stan_data, adapt_delta=0.99, max_treedepth=12)
        t_retry = time.time() - t0
        r = evaluate_nuts(fit_4pl, true_params, "4pl")
        r["fit_time_sec"] = round(t_retry, 1)
        r["retried"] = True
        all_results["4pl_nuts"] = r
        print(f"  Retry: {t_retry:.1f}s | γ={r['gamma_mean']} | {'PASS' if r['pass_fail']['overall'] else 'FAIL'}")
        sys.stdout.flush()

    # Final write
    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    md = write_markdown(all_results)
    md_path = os.path.join(ARTIFACTS_DIR, "p1_base_results.md")
    with open(md_path, "w") as f:
        f.write(md)

    print(f"\n=== SUMMARY ===")
    for key in ["2pl_advi", "2pl_nuts", "4pl_advi", "4pl_nuts"]:
        if key in all_results:
            r = all_results[key]
            print(f"  {key}: γ={r['gamma_mean']}, θ_corr={r['theta_corr']}, {'PASS' if r['pass_fail']['overall'] else 'FAIL'} ({r['fit_time_sec']}s)")
    sys.stdout.flush()

    return all_results


if __name__ == "__main__":
    main()

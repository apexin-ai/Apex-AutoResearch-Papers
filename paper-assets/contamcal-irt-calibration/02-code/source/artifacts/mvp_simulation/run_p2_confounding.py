# P2 Confounding Test: θ-exposure confounding with 2PL+γ and 4PL+γ IRT models
# Kill-or-go test: can the model separate γ from θ when corr(θ, exposure) ≈ 0.4?
# Order: 2PL ADVI → 2PL NUTS → 4PL ADVI → 4PL NUTS (same as P1)

import json
import os
import sys
import time
import numpy as np
from scipy import stats
from scipy.special import expit
import cmdstanpy

SEED = 123
N_MODELS = 50
N_ITEMS = 300
GAMMA_TRUE = 0.5
TARGET_CORR = 0.4
CORR_TOL = (0.3, 0.5)

ARTIFACTS_DIR = os.path.dirname(os.path.abspath(__file__))
STAN_4PL = os.path.join(ARTIFACTS_DIR, "contam_irt_4pl.stan")
STAN_2PL = os.path.join(ARTIFACTS_DIR, "contam_irt_2pl.stan")

PASS_THRESHOLDS = {
    "gamma_ci_covers_true": True,
    "gamma_ci_excludes_zero": True,
    "gamma_rel_bias": 0.3,
    "theta_corr": 0.9,
    "theta_rmse": 0.3,
    "max_rhat": 1.01,
    "divergent_pct": 1.0,
}


def find_sigma_model_for_target_corr(theta, rng, alpha, target=TARGET_CORR, n_items=N_ITEMS):
    """Binary search for sigma_model that yields corr(theta, mean_exposure) ≈ target.

    Model-level noise (constant across items per model) controls correlation.
    Item-level noise alone averages out over N_items.
    """
    lo, hi = 0.1, 10.0
    best_sigma, best_diff = 1.0, float('inf')
    sigma_item = 1.0

    for _ in range(40):
        sigma_model = (lo + hi) / 2.0
        model_noise = rng.standard_normal(len(theta)) * sigma_model
        item_noise = rng.standard_normal((len(theta), n_items)) * sigma_item
        logits = alpha * theta[:, None] + model_noise[:, None] + item_noise
        exposure = (rng.random((len(theta), n_items)) < expit(logits)).astype(float)
        mean_exp = exposure.mean(axis=1)
        corr = np.corrcoef(theta, mean_exp)[0, 1]
        diff = abs(corr - target)

        if diff < best_diff:
            best_diff = diff
            best_sigma = sigma_model

        if corr > target:
            lo = sigma_model
        else:
            hi = sigma_model

        if diff < 0.02:
            break

    return best_sigma


def generate_confounded_data(rng):
    theta = rng.standard_normal(N_MODELS)
    a = rng.lognormal(0, 0.5, N_ITEMS)
    b = rng.standard_normal(N_ITEMS)
    c = rng.beta(5, 20, N_ITEMS)
    d = rng.beta(20, 5, N_ITEMS)

    alpha = 1.0
    sigma_item = 1.0
    sigma_model = find_sigma_model_for_target_corr(
        theta, rng, alpha=alpha, target=TARGET_CORR
    )

    rng_exp = np.random.default_rng(SEED + 1000)
    model_noise = rng_exp.standard_normal(N_MODELS) * sigma_model
    item_noise = rng_exp.standard_normal((N_MODELS, N_ITEMS)) * sigma_item
    logits = alpha * theta[:, None] + model_noise[:, None] + item_noise
    exposure = (rng_exp.random((N_MODELS, N_ITEMS)) < expit(logits)).astype(float)

    mean_exp = exposure.mean(axis=1)
    actual_corr = float(np.corrcoef(theta, mean_exp)[0, 1])
    print(f"  Alpha: {alpha:.4f}, sigma_model: {sigma_model:.4f}, sigma_item: {sigma_item:.4f}")
    print(f"  Actual corr(θ, mean_exposure): {actual_corr:.4f}")

    if not (CORR_TOL[0] <= actual_corr <= CORR_TOL[1]):
        print(f"  WARNING: correlation {actual_corr:.4f} outside target range {CORR_TOL}")

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
    return stan_data, true_params, actual_corr, exposure


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


def confounding_diagnostics(theta_post_mean, theta_true, exposure):
    mean_exp = exposure.mean(axis=1)
    theta_exp_corr = float(np.corrcoef(theta_post_mean, mean_exp)[0, 1])
    theta_residual_exp_corr = float(np.corrcoef(theta_post_mean - theta_true, mean_exp)[0, 1])
    return {
        "theta_exp_corr": round(theta_exp_corr, 4),
        "theta_residual_exp_corr": round(theta_residual_exp_corr, 4),
    }


def evaluate_advi(vb, true_params, exposure, model_name):
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

    conf_diag = confounding_diagnostics(theta_post_mean, theta_true, exposure)

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
        **conf_diag,
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


def evaluate_nuts(fit, true_params, exposure, model_name):
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

    conf_diag = confounding_diagnostics(theta_post_mean, theta_true, exposure)

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
        **conf_diag,
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


def write_markdown(all_results, actual_corr):
    lines = [
        "# P2 θ-Exposure Confounding Test Results",
        "",
        f"- N_models={N_MODELS}, N_items={N_ITEMS}, γ_true={GAMMA_TRUE}",
        f"- seed={SEED}",
        f"- Target confounding correlation: {TARGET_CORR}",
        f"- **Actual confounding correlation: {actual_corr:.4f}**",
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
            f"| θ-exp corr | {r.get('theta_exp_corr', 'N/A')} | — | — |",
            f"| θ residual-exp corr | {r.get('theta_residual_exp_corr', 'N/A')} | — | — |",
        ]
        if "max_rhat" in r:
            lines.append(f"| Max R-hat | {r['max_rhat']} | < 1.01 | {fmt_pf(pf['max_rhat'])} |")
            lines.append(f"| Divergent | {r['divergent_count']} ({r['divergent_pct']}%) | < 1% | {fmt_pf(pf['divergent_pct'])} |")
            lines.append(f"| Min ESS | {r['min_ess']} | — | — |")
        if "fit_time_sec" in r:
            lines.append(f"| Fit time | {r['fit_time_sec']}s | — | — |")
        lines += ["", f"**Overall: {'PASS' if pf['overall'] else 'FAIL'}**", ""]

    # Comparison table
    keys_present = [k for k in ["2pl_advi", "2pl_nuts", "4pl_advi", "4pl_nuts"] if k in all_results]
    if len(keys_present) >= 2:
        lines += ["## Comparison", ""]
        header = "| Metric | " + " | ".join(k.upper().replace("_", " ") for k in keys_present) + " |"
        sep = "|--------|" + "|".join(["-------"] * len(keys_present)) + "|"
        lines += [header, sep]
        for metric in ["gamma_mean", "gamma_rel_bias", "theta_corr", "theta_rmse", "theta_exp_corr", "theta_residual_exp_corr"]:
            row = f"| {metric} | " + " | ".join(str(all_results[k].get(metric, "N/A")) for k in keys_present) + " |"
            lines += [row]
        row_overall = "| Overall | " + " | ".join(
            "PASS" if all_results[k]["pass_fail"]["overall"] else "FAIL" for k in keys_present
        ) + " |"
        lines += [row_overall, ""]

    # Kill-or-go
    any_pass = any(all_results[k]["pass_fail"]["overall"] for k in keys_present if k in all_results)
    lines += ["## Kill-or-Go Assessment", ""]
    if any_pass:
        passing = [k for k in keys_present if all_results[k]["pass_fail"]["overall"]]
        lines += [
            f"**VERDICT: GO** — {', '.join(passing)} pass(es) under confounding (corr≈{actual_corr:.2f}).",
        ]
    else:
        lines += [
            f"**VERDICT: POTENTIAL KILL** — No model passes under confounding (corr≈{actual_corr:.2f}).",
            "",
            "Consider: structured prior on θ-exposure, instrumental variables, or two-stage estimation.",
        ]

    return "\n".join(lines)


def main():
    rng = np.random.default_rng(SEED)

    print("=== P2: θ-Exposure Confounding Test (N_items=300, 4PL NUTS only) ===")
    print(f"Target corr(θ, mean_exposure) ≈ {TARGET_CORR}")
    sys.stdout.flush()

    print("\n=== Generating confounded data ===")
    stan_data, true_params, actual_corr, exposure = generate_confounded_data(rng)
    print(f"  N_params: {N_MODELS} θ + {N_ITEMS}*4 item + 1 γ = {N_MODELS + N_ITEMS*4 + 1}")
    sys.stdout.flush()

    json_path = os.path.join(ARTIFACTS_DIR, "p2_confounding_results.json")
    all_results = {"config": {
        "N_models": N_MODELS, "N_items": N_ITEMS,
        "gamma_true": GAMMA_TRUE, "target_confound_corr": TARGET_CORR,
        "actual_confound_corr": round(actual_corr, 4), "seed": SEED,
    }}

    # --- 4PL NUTS (only config needed per Director) ---
    print("\n=== 4PL+γ NUTS ===")
    sys.stdout.flush()
    t0 = time.time()
    fit_4pl = fit_nuts(STAN_4PL, stan_data, adapt_delta=0.95)
    t_4pl_nuts = time.time() - t0
    r = evaluate_nuts(fit_4pl, true_params, exposure, "4pl")
    r["fit_time_sec"] = round(t_4pl_nuts, 1)
    all_results["4pl_nuts"] = r
    print(f"  Time: {t_4pl_nuts:.1f}s | γ={r['gamma_mean']}±{r['gamma_sd']} | θ_corr={r['theta_corr']} | {'PASS' if r['pass_fail']['overall'] else 'FAIL'}")
    sys.stdout.flush()

    if r["divergent_pct"] > 5.0 or r["max_rhat"] > 1.1:
        print("\n=== 4PL+γ NUTS retry (adapt_delta=0.99, treedepth=12) ===")
        sys.stdout.flush()
        t0 = time.time()
        fit_4pl = fit_nuts(STAN_4PL, stan_data, adapt_delta=0.99, max_treedepth=12)
        t_retry = time.time() - t0
        r = evaluate_nuts(fit_4pl, true_params, exposure, "4pl")
        r["fit_time_sec"] = round(t_retry, 1)
        r["retried"] = True
        all_results["4pl_nuts"] = r
        print(f"  Retry: {t_retry:.1f}s | γ={r['gamma_mean']} | {'PASS' if r['pass_fail']['overall'] else 'FAIL'}")
        sys.stdout.flush()

    # Final write
    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    md = write_markdown(all_results, actual_corr)
    md_path = os.path.join(ARTIFACTS_DIR, "p2_confounding_results.md")
    with open(md_path, "w") as f:
        f.write(md)

    print(f"\n=== P2 RESULT ===")
    print(f"Confound corr: {actual_corr:.4f}")
    pf = r["pass_fail"]
    print(f"4PL NUTS: γ={r['gamma_mean']}±{r['gamma_sd']}, θ_corr={r['theta_corr']}, θ_rmse={r['theta_rmse']}")
    print(f"Confound diag: θ_exp_corr={r.get('theta_exp_corr','?')}, θ_residual_exp_corr={r.get('theta_residual_exp_corr','?')}")
    print(f"Overall: {'PASS' if pf['overall'] else 'FAIL'}")
    print("P2_DONE")
    sys.stdout.flush()

    return all_results


if __name__ == "__main__":
    main()

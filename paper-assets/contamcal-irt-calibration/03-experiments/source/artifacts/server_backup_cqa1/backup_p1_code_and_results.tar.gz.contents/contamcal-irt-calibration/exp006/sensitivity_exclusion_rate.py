#!/usr/bin/env python3
"""Sensitivity analysis: vary RRF-based item exclusion rate for MMLU 2PL+gamma IRT.
Saves each fit result immediately so progress survives restarts."""

import json
import logging
import os
import re
import sys
import time
from pathlib import Path

import numpy as np
from scipy import stats

sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
from run_irt_calibration import (
    load_pooled_eval_results,
    prepare_stan_data,
    fit_stan_model,
    check_convergence,
    posterior_predictive_check,
    STAN_MODELS,
)

log = logging.getLogger(__name__)

MODEL_WHITELIST = {
    "Qwen2.5-1.5B_d000_s123",
    "Qwen2.5-1.5B_d000_s42",
    "Qwen2.5-1.5B_d005_s123",
    "Qwen2.5-1.5B_d005_s42",
    "Qwen2.5-1.5B_d025_s123",
    "Qwen2.5-1.5B_d025_s42",
    "Qwen2.5-1.5B_d100_s123",
    "Qwen2.5-1.5B_d100_s42",
    "Qwen2.5-3B_d005_s123",
    "Qwen2.5-3B_d025_s123",
    "Qwen2.5-3B_d025_v3_s42",
    "Qwen2.5-3B_d100_a32_s123",
    "Qwen2.5-3B_d100_a32_s42",
}

EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
RRF_PATH = "/root/autodl-tmp/exp003/rrf_all_scales/exposure_scores.json"
STAN_FILE = STAN_MODELS["2pl_gamma"]
OUTPUT_DIR = "/root/autodl-tmp/exp006/exclusion_sensitivity"
MAX_ITEMS = 2000
EXCLUSION_RATES = [0.00, 0.30, 0.40, 0.50, 0.60, 0.70]


def strip_aligned(dirname):
    return re.sub(r'(_para)?(_aligned)?$', '', dirname)


def load_data():
    data = load_pooled_eval_results(EVAL_DIR, scales=["1.5B", "3B"],
                                     benchmarks=["mmlu"], skip_para=True)
    with open(RRF_PATH) as f:
        rrf_data = json.load(f)

    keep_idx = []
    models = []
    dosages = []
    for i, m in enumerate(data["models"]):
        key = strip_aligned(m["dirname"])
        if key in MODEL_WHITELIST and key in rrf_data:
            keep_idx.append(i)
            models.append(m)
            dosages.append(m["dosage"])

    keep_idx = np.array(keep_idx)
    dosages = np.array(dosages)
    responses = data["benchmarks"]["mmlu"]["responses"][keep_idx]
    n_items = data["benchmarks"]["mmlu"]["n_items"]

    rrf_exposure = np.zeros((len(models), n_items), dtype=float)
    for i, m in enumerate(models):
        key = strip_aligned(m["dirname"])
        scores = rrf_data[key]["mmlu"]["exposure_scores"]
        rrf_exposure[i, :n_items] = scores[:n_items]

    log.info("Loaded %d models x %d items", len(models), n_items)
    return responses, rrf_exposure, dosages, models, n_items


def fit_one_rate(excl_rate, responses, rrf_exposure, dosages, n_total_items, output_dir):
    """Fit a single exclusion rate and save result. Returns result dict."""
    mean_exposure = rrf_exposure.mean(axis=0)
    item_rank = np.argsort(mean_exposure)

    n_exclude = int(n_total_items * excl_rate)
    n_keep = n_total_items - n_exclude
    keep_idx = item_rank[n_exclude:]

    if n_keep > MAX_ITEMS:
        np.random.seed(42)
        sub_idx = np.sort(np.random.choice(n_keep, MAX_ITEMS, replace=False))
        keep_idx = keep_idx[sub_idx]
        n_items_fit = MAX_ITEMS
    else:
        n_items_fit = n_keep

    resp = responses[:, keep_idx]
    exp = rrf_exposure[:, keep_idx]

    log.info("Exclusion rate: %.0f%% -> %d items kept (fitting %d)",
             excl_rate * 100, n_keep, n_items_fit)

    stan_data = prepare_stan_data(resp, exp, "2pl_gamma")
    t0 = time.time()
    fit, _ = fit_stan_model(
        STAN_FILE, stan_data,
        chains=2, iter_warmup=1000, iter_sampling=1000,
        adapt_delta=0.95, max_treedepth=12, seed=42,
    )
    elapsed = time.time() - t0

    diag = check_convergence(fit)
    ppp = posterior_predictive_check(fit, resp)

    gamma_samples = fit.stan_variable("gamma")
    theta_samples = fit.stan_variable("theta")
    theta_mean = np.mean(theta_samples, axis=0)
    tau_val, _ = stats.kendalltau(theta_mean, dosages)

    cal_draws = fit.stan_variable("calibrated_score")
    cal_mean = np.mean(cal_draws, axis=0)
    raw_acc = resp.mean(axis=1)
    mae = float(np.mean(np.abs(cal_mean - raw_acc)))

    result = {
        "exclusion_rate": excl_rate,
        "n_items_total": n_keep,
        "n_items_fit": n_items_fit,
        "mean_exposure": round(float(exp.mean()), 4),
        "mean_acc": round(float(resp.mean()), 4),
        "gamma": {
            "mean": round(float(np.mean(gamma_samples)), 4),
            "sd": round(float(np.std(gamma_samples)), 4),
            "q025": round(float(np.percentile(gamma_samples, 2.5)), 4),
            "q975": round(float(np.percentile(gamma_samples, 97.5)), 4),
        },
        "tau_kendall": round(float(tau_val), 4),
        "mae": round(mae, 4),
        "ppp": ppp["overall_ppp"],
        "residual_mae": ppp["residual_mae"],
        "diagnostics": {
            "max_rhat": diag.get("max_rhat"),
            "min_ess": diag.get("min_ess"),
            "divergent_count": diag.get("divergent_count"),
            "all_ok": diag.get("all_ok"),
        },
        "fit_time_sec": round(elapsed, 1),
    }

    # Save immediately
    rate_str = f"{int(excl_rate*100):02d}"
    with open(output_dir / f"result_excl{rate_str}.json", "w") as f:
        json.dump(result, f, indent=2)

    g = result["gamma"]
    log.info("[%s%%] gamma=%.4f [%.4f, %.4f], tau=%.4f, MAE=%.4f, Rhat=%.4f, time=%.0fs",
             rate_str, g["mean"], g["q025"], g["q975"],
             result["tau_kendall"], mae, diag.get("max_rhat", 0), elapsed)
    return result


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--rate", type=float, default=None,
                        help="Run single exclusion rate (e.g. 0.30)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)

    responses, rrf_exposure, dosages, models, n_items = load_data()

    if args.rate is not None:
        fit_one_rate(args.rate, responses, rrf_exposure, dosages, n_items, output_dir)
        return

    # Run all rates, skip already completed
    for excl_rate in EXCLUSION_RATES:
        rate_str = f"{int(excl_rate*100):02d}"
        result_file = output_dir / f"result_excl{rate_str}.json"
        if result_file.exists():
            log.info("Skipping %.0f%% (already completed)", excl_rate * 100)
            continue
        fit_one_rate(excl_rate, responses, rrf_exposure, dosages, n_items, output_dir)

    # Collect and print summary
    results = []
    for excl_rate in EXCLUSION_RATES:
        rate_str = f"{int(excl_rate*100):02d}"
        with open(output_dir / f"result_excl{rate_str}.json") as f:
            results.append(json.load(f))

    with open(output_dir / "sensitivity_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\n" + "=" * 95)
    print(f"{'Excl%':>6} {'N_items':>7} {'gamma_mean':>10} {'gamma_CI':>22} "
          f"{'tau':>6} {'MAE':>6} {'Rhat_max':>8} {'PPP':>6}")
    print("-" * 95)
    for r in results:
        g = r["gamma"]
        ci = f"[{g['q025']:.4f}, {g['q975']:.4f}]"
        print(f"{r['exclusion_rate']*100:>5.0f}% {r['n_items_fit']:>7} "
              f"{g['mean']:>10.4f} {ci:>22} "
              f"{r['tau_kendall']:>6.4f} {r['mae']:>6.4f} "
              f"{r['diagnostics']['max_rhat']:>8.4f} {r['ppp']:>6.3f}")
    print("=" * 95)


if __name__ == "__main__":
    main()

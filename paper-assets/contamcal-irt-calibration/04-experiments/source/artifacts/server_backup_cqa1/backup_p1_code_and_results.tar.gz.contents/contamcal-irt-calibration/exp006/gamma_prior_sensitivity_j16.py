#!/usr/bin/env python3
"""Gamma prior sensitivity analysis for Social Sciences domain — j16_qwen model pool."""

import json
import logging
import os
import re
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
from run_irt_calibration import (
    prepare_stan_data,
    fit_stan_model,
    check_convergence,
    posterior_predictive_check,
    parse_model_dir_name,
)
from run_mmlu_domain_gamma_j16 import (
    DOMAIN_MAP,
    MODEL_WHITELIST,
    DIR_TO_RRF_KEY,
    EVAL_DIR,
    MMLU_ARROW,
    RRF_PATH,
    MAX_ITEMS,
    strip_aligned,
    build_subject_index_map,
    build_domain_col_indices,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

STAN_MODEL_DIR = "/root/contamcal-irt-calibration/stan_models"
PRIOR_CONFIGS = {
    "tight_05": os.path.join(STAN_MODEL_DIR, "contam_irt_2pl_gamma_tight.stan"),
    "baseline_10": os.path.join(STAN_MODEL_DIR, "contam_irt_2pl_gamma.stan"),
    "loose_20": os.path.join(STAN_MODEL_DIR, "contam_irt_2pl_gamma_loose.stan"),
}

OUTPUT_DIR = Path("/root/autodl-tmp/exp006/gamma_prior_sensitivity_j16/social_sciences")
DOMAIN = "Social_Sciences"


def load_social_sciences_data():
    """Load response matrix and exposure matrix for Social Sciences domain (j16_qwen pool)."""
    import pyarrow as pa

    eval_path = Path(EVAL_DIR)
    model_dirs = sorted([
        d for d in eval_path.iterdir()
        if d.is_dir() and (d / "eval_results.json").exists()
    ])

    # Collect candidates, dedup by clean_name (prefer _aligned)
    candidates = {}
    for d in model_dirs:
        info = parse_model_dir_name(d.name)
        if info is None:
            continue
        if info["is_para"]:
            continue
        clean_name = strip_aligned(d.name)
        if clean_name not in MODEL_WHITELIST:
            continue
        info["path"] = str(d)
        info["scale"] = "0.5B" if "0.5B" in d.name else "1.5B" if "1.5B" in d.name else "3B"
        is_aligned = "_aligned" in d.name
        if clean_name not in candidates or is_aligned:
            candidates[clean_name] = info

    models = list(candidates.values())
    log.info("Found %d whitelisted models (expected 16)", len(models))
    for m in sorted(models, key=lambda x: x["dirname"]):
        log.info("  %s (d=%d)", m["dirname"], m["dosage"])

    assert len(models) == 16, f"Expected 16 models in j16_qwen pool, got {len(models)}"

    responses_list = []
    for m in models:
        with open(Path(m["path"]) / "eval_results.json") as f:
            data = json.load(f)
        per_item = data["benchmarks"]["mmlu"]["per_item"]
        responses_list.append([int(item["correct"]) for item in per_item])

    n_total_items = min(len(r) for r in responses_list)
    full_responses = np.zeros((len(models), n_total_items), dtype=int)
    for i, r in enumerate(responses_list):
        full_responses[i, :n_total_items] = r[:n_total_items]

    dosages = np.array([m["dosage"] for m in models])

    with open(RRF_PATH) as f:
        rrf_data = json.load(f)

    rrf_exposure = np.zeros((len(models), n_total_items), dtype=float)
    for i, m in enumerate(models):
        key = strip_aligned(m["dirname"])
        rrf_key = DIR_TO_RRF_KEY.get(key, key)
        if rrf_key in rrf_data and "mmlu" in rrf_data[rrf_key]:
            scores = rrf_data[rrf_key]["mmlu"]["exposure_scores"]
            rrf_exposure[i, :n_total_items] = scores[:n_total_items]

    subject_list = build_subject_index_map(MMLU_ARROW)
    domain_indices = build_domain_col_indices(subject_list, n_total_items)
    ss_idx = domain_indices[DOMAIN]
    log.info("Social Sciences: %d items", len(ss_idx))

    domain_resp = full_responses[:, ss_idx]
    domain_exp = rrf_exposure[:, ss_idx]

    if domain_resp.shape[1] > MAX_ITEMS:
        np.random.seed(42)
        idx = np.sort(np.random.choice(domain_resp.shape[1], MAX_ITEMS, replace=False))
        domain_resp = domain_resp[:, idx]
        domain_exp = domain_exp[:, idx]
        log.info("Subsampled to %d items", MAX_ITEMS)

    return domain_resp, domain_exp, len(models), domain_resp.shape[1]


def run_sensitivity():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    log.info("Loading Social Sciences data (j16_qwen pool)...")
    y, exposure, n_models, n_items = load_social_sciences_data()
    log.info("Data: %d models x %d items, mean_acc=%.4f", n_models, n_items, y.mean())

    stan_data = prepare_stan_data(y, exposure, model_type="2pl_gamma")
    results = {}

    for prior_name, stan_file in PRIOR_CONFIGS.items():
        log.info("=" * 60)
        log.info("Fitting prior: %s (%s)", prior_name, os.path.basename(stan_file))

        fit, elapsed = fit_stan_model(
            stan_file, stan_data,
            chains=4, iter_warmup=1000, iter_sampling=1000,
            adapt_delta=0.95, max_treedepth=12, seed=42,
            parallel_chains=4,
        )

        gamma_draws = fit.stan_variable("gamma")
        gamma_mean = float(np.mean(gamma_draws))
        gamma_median = float(np.median(gamma_draws))
        gamma_sd = float(np.std(gamma_draws))
        q025 = float(np.percentile(gamma_draws, 2.5))
        q975 = float(np.percentile(gamma_draws, 97.5))
        p_gamma_neg = float(np.mean(gamma_draws < 0))

        diag = check_convergence(fit)
        ppp = posterior_predictive_check(fit, y)

        result = {
            "prior": prior_name,
            "stan_file": os.path.basename(stan_file),
            "n_models": n_models,
            "n_items": n_items,
            "gamma": {
                "mean": round(gamma_mean, 4),
                "median": round(gamma_median, 4),
                "sd": round(gamma_sd, 4),
                "q025": round(q025, 4),
                "q975": round(q975, 4),
                "p_negative": round(p_gamma_neg, 4),
            },
            "diagnostics": diag,
            "ppp": ppp,
            "fit_time_sec": round(elapsed, 1),
        }
        results[prior_name] = result

        log.info("[%s] gamma=%.4f [%.4f, %.4f], P(gamma<0)=%.4f, PPP=%.4f, Rhat=%.4f, ESS=%.0f, time=%.0fs",
                 prior_name, gamma_mean, q025, q975, p_gamma_neg,
                 ppp["overall_ppp"], diag.get("max_rhat", 0), diag.get("min_ess", 0), elapsed)

        with open(OUTPUT_DIR / f"{prior_name}_results.json", "w") as f:
            json.dump(result, f, indent=2)

    with open(OUTPUT_DIR / "sensitivity_comparison.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\n" + "=" * 80)
    print("GAMMA PRIOR SENSITIVITY (j16_qwen) - Social Sciences (J=%d, I=%d)" % (n_models, n_items))
    print("=" * 80)
    print(f"{'Prior':<16} {'gamma_hat':>10} {'95% CI':>22} {'P(g<0)':>8} {'PPP':>8} {'Rhat':>8} {'ESS':>8} {'Time':>6}")
    print("-" * 80)
    for name, r in results.items():
        g = r["gamma"]
        d = r["diagnostics"]
        p = r["ppp"]
        ci_str = "[%.4f, %.4f]" % (g["q025"], g["q975"])
        print(f"{name:<16} {g['mean']:>10.4f} {ci_str:>22} {g['p_negative']:>8.4f} {p['overall_ppp']:>8.4f} {d.get('max_rhat', 0):>8.4f} {d.get('min_ess', 0):>8.0f} {r['fit_time_sec']:>5.0f}s")
    print("=" * 80)

    log.info("Results saved to %s", OUTPUT_DIR)


if __name__ == "__main__":
    run_sensitivity()

#!/usr/bin/env python3
"""Re-run J=13 no-0.5B IRT fits to extract theta parameters.
Saves theta posterior means + CIs for all domains + pooled.
Uses same data/config as run_mmlu_domain_gamma_no05b.py."""

import json
import logging
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
from run_irt_calibration import fit_stan_model, prepare_stan_data, check_convergence, STAN_MODELS
from run_mmlu_domain_gamma_no05b import (
    MODEL_WHITELIST, EVAL_DIR, MMLU_ARROW, RRF_PATH, MAX_ITEMS,
    DOMAIN_MAP, strip_aligned, build_subject_index_map, build_domain_col_indices,
)

sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
from run_irt_calibration import load_pooled_eval_results

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
log = logging.getLogger(__name__)

OUTPUT_DIR = Path("/root/autodl-tmp/exp006/mmlu_domain_irt_no05B")
MODEL_TYPE = "2pl_gamma"
STAN_FILE = STAN_MODELS[MODEL_TYPE]

MODEL_NAMES = [
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
]


def extract_theta_from_fit(fit, n_models):
    """Extract theta posterior statistics from CmdStanMCMC fit."""
    theta = fit.stan_variable("theta")  # (n_draws, n_models)
    results = {}
    for j in range(n_models):
        col = theta[:, j]
        results[f"theta_{j+1}"] = {
            "mean": float(np.mean(col)),
            "sd": float(np.std(col)),
            "q025": float(np.percentile(col, 2.5)),
            "q975": float(np.percentile(col, 97.5)),
        }
    # Group stats
    theta_15B = theta[:, :8]  # 8 x 1.5B models
    theta_3B = theta[:, 8:]   # 5 x 3B models
    delta_draws = theta_3B.mean(axis=1) - theta_15B.mean(axis=1)
    results["group_1.5B"] = {
        "mean": float(theta_15B.mean()),
        "per_model_means": [float(theta[:, j].mean()) for j in range(8)],
    }
    results["group_3B"] = {
        "mean": float(theta_3B.mean()),
        "per_model_means": [float(theta[:, j].mean()) for j in range(8, n_models)],
    }
    results["delta_theta"] = {
        "mean": float(delta_draws.mean()),
        "sd": float(delta_draws.std()),
        "q025": float(np.percentile(delta_draws, 2.5)),
        "q975": float(np.percentile(delta_draws, 97.5)),
    }
    return results


def main():
    import re
    import pyarrow as pa

    # Load data (same as original script)
    data = load_pooled_eval_results(EVAL_DIR, scales=["1.5B", "3B"])
    models = data["models"]

    # Filter to whitelist
    keep_idx = []
    for i, m in enumerate(models):
        key = re.sub(r'(_para)?(_aligned)?$', '', m["dirname"])
        if key in MODEL_WHITELIST:
            keep_idx.append(i)
    keep_idx = np.array(keep_idx)
    models = [models[i] for i in keep_idx]
    full_responses = data["benchmarks"]["mmlu"]["responses"][keep_idx]
    n_total_items = full_responses.shape[1]

    # Load RRF
    with open(RRF_PATH) as f:
        rrf_data = json.load(f)
    rrf_exposure = np.zeros((len(models), n_total_items), dtype=float)
    for i, m in enumerate(models):
        key = re.sub(r'(_para)?(_aligned)?$', '', m["dirname"])
        scores = rrf_data[key]["mmlu"]["exposure_scores"]
        rrf_exposure[i, :] = scores[:n_total_items]

    log.info("Loaded %d models x %d items", len(models), n_total_items)
    assert len(models) == 13, f"Expected 13 models, got {len(models)}"

    # Build domain indices
    subject_list = build_subject_index_map(MMLU_ARROW)
    domain_indices = build_domain_col_indices(subject_list, n_total_items)

    args_dict = {
        "chains": 4, "warmup": 1000, "samples": 1000,
        "adapt_delta": 0.95, "max_treedepth": 12, "seed": 42,
    }

    all_theta = {"model_names": MODEL_NAMES}

    domains_to_fit = list(DOMAIN_MAP.keys()) + ["pooled"]

    for domain in domains_to_fit:
        log.info("=" * 50)
        if domain == "pooled":
            log.info("Fitting POOLED")
            responses = full_responses
            exposure = rrf_exposure
            n_items = n_total_items
            if n_items > MAX_ITEMS:
                np.random.seed(42)
                idx = np.sort(np.random.choice(n_items, MAX_ITEMS, replace=False))
                responses = responses[:, idx]
                exposure = exposure[:, idx]
                n_items = MAX_ITEMS
        else:
            idx = domain_indices[domain]
            if len(idx) < 10:
                log.warning("Skipping %s: only %d items", domain, len(idx))
                continue
            log.info("Fitting %s (%d items)", domain, len(idx))
            responses = full_responses[:, idx]
            exposure = rrf_exposure[:, idx]
            n_items = len(idx)
            if n_items > MAX_ITEMS:
                np.random.seed(42)
                sub_idx = np.sort(np.random.choice(n_items, MAX_ITEMS, replace=False))
                responses = responses[:, sub_idx]
                exposure = exposure[:, sub_idx]
                n_items = MAX_ITEMS

        stan_data = prepare_stan_data(responses, exposure, model_type=MODEL_TYPE)
        fit, elapsed = fit_stan_model(
            STAN_FILE, stan_data,
            chains=args_dict["chains"],
            iter_warmup=args_dict["warmup"],
            iter_sampling=args_dict["samples"],
            adapt_delta=args_dict["adapt_delta"],
            max_treedepth=args_dict["max_treedepth"],
            seed=args_dict["seed"],
        )

        theta_results = extract_theta_from_fit(fit, 13)
        theta_results["n_items"] = n_items
        theta_results["fit_time_sec"] = round(elapsed, 1)

        # Cross-check gamma
        gamma = fit.stan_variable("gamma")
        theta_results["gamma_mean"] = float(np.mean(gamma))

        all_theta[domain] = theta_results
        log.info("[%s] delta_theta=%.4f [%.4f, %.4f], gamma=%.4f, time=%.0fs",
                 domain, theta_results["delta_theta"]["mean"],
                 theta_results["delta_theta"]["q025"],
                 theta_results["delta_theta"]["q975"],
                 theta_results["gamma_mean"], elapsed)

    # Save
    out_path = OUTPUT_DIR / "theta_results.json"
    with open(out_path, "w") as f:
        json.dump(all_theta, f, indent=2)
    log.info("Saved theta results to %s", out_path)

    # Print summary table
    print("\n" + "=" * 80)
    print(f"{'Domain':<18} {'theta_1.5B':>10} {'theta_3B':>10} {'Delta':>8} {'Delta 95% CI':>20} {'gamma':>8}")
    print("-" * 80)
    for domain in list(DOMAIN_MAP.keys()) + ["pooled"]:
        if domain not in all_theta:
            continue
        r = all_theta[domain]
        d = r["delta_theta"]
        print(f"{domain:<18} {r['group_1.5B']['mean']:>10.4f} {r['group_3B']['mean']:>10.4f} "
              f"{d['mean']:>8.4f} [{d['q025']:>7.4f}, {d['q975']:>7.4f}] {r['gamma_mean']:>8.4f}")


if __name__ == "__main__":
    main()

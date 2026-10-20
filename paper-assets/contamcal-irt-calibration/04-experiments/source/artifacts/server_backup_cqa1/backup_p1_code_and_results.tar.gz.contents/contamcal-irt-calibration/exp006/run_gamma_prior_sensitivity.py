#!/usr/bin/env python3
"""SF5: Gamma prior sensitivity analysis.

Fits 2PL+γ IRT on pooled MMLU (J=16) with three gamma priors:
  - Tight:   γ ~ N(0, 0.5)
  - Default: γ ~ N(0, 1)   [baseline from Table 4]
  - Loose:   γ ~ N(0, 2)

Also computes e_ij exposure score empirical distribution.
"""

import json
import logging
import os
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
from run_pooled_rrf_irt import (
    load_rrf_exposure,
    build_rrf_exposure_matrix,
    filter_models_for_benchmark,
    strip_aligned,
    normalize_model_key,
    resolve_rrf_key,
)
from run_irt_calibration import (
    load_pooled_eval_results,
    prepare_stan_data,
    fit_stan_model,
    check_convergence,
    extract_results,
)

log = logging.getLogger(__name__)

EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
EXPOSURE_FILE = "/root/autodl-tmp/exp003/rrf_full_3scales/exposure_scores.json"
STAN_MODEL_DIR = "/root/contamcal-irt-calibration/stan_models"
OUTPUT_DIR = "/root/autodl-tmp/exp006/gamma_prior_sensitivity"
MAX_ITEMS = 300

PRIOR_CONFIGS = {
    "tight_05": {
        "stan_file": os.path.join(STAN_MODEL_DIR, "contam_irt_2pl_gamma_tight.stan"),
        "label": "N(0, 0.5)",
        "prior_sd": 0.5,
    },
    "default_10": {
        "stan_file": os.path.join(STAN_MODEL_DIR, "contam_irt_2pl_gamma.stan"),
        "label": "N(0, 1)",
        "prior_sd": 1.0,
    },
    "loose_20": {
        "stan_file": os.path.join(STAN_MODEL_DIR, "contam_irt_2pl_gamma_loose.stan"),
        "label": "N(0, 2)",
        "prior_sd": 2.0,
    },
}

STAN_CONFIG = {
    "chains": 4,
    "warmup": 1000,
    "samples": 1000,
    "adapt_delta": 0.95,
    "max_treedepth": 12,
    "seed": 42,
}


def compute_ppp(fit, y_obs):
    """Posterior predictive p-value from calibrated_score generated quantity."""
    try:
        cal = fit.stan_variable("calibrated_score")
        obs_stat = y_obs.mean()
        rep_means = cal.mean(axis=1)
        return round(float((rep_means >= obs_stat).mean()), 4)
    except Exception:
        return None


def run_single_prior(prior_key, prior_cfg, models, dosages, responses,
                     rrf_data, subsample_idx):
    """Run IRT fit with one gamma prior config."""
    log.info("=" * 60)
    log.info("Prior: %s (%s)", prior_key, prior_cfg["label"])

    n_models = len(models)
    resp_sub = responses[:, subsample_idx]
    n_items = resp_sub.shape[1]

    exposure = build_rrf_exposure_matrix(models, rrf_data, "mmlu", 14042)
    exposure_sub = exposure[:, subsample_idx]

    stan_data = prepare_stan_data(resp_sub, exposure_sub, model_type="2pl_gamma")

    fit, elapsed = fit_stan_model(
        prior_cfg["stan_file"], stan_data,
        chains=STAN_CONFIG["chains"],
        iter_warmup=STAN_CONFIG["warmup"],
        iter_sampling=STAN_CONFIG["samples"],
        adapt_delta=STAN_CONFIG["adapt_delta"],
        max_treedepth=STAN_CONFIG["max_treedepth"],
        seed=STAN_CONFIG["seed"],
    )

    diag = check_convergence(fit)

    gamma_draws = fit.stan_variable("gamma")
    gamma_summary = {
        "mean": round(float(np.mean(gamma_draws)), 4),
        "median": round(float(np.median(gamma_draws)), 4),
        "sd": round(float(np.std(gamma_draws)), 4),
        "q025": round(float(np.percentile(gamma_draws, 2.5)), 4),
        "q975": round(float(np.percentile(gamma_draws, 97.5)), 4),
        "q10": round(float(np.percentile(gamma_draws, 10)), 4),
        "q90": round(float(np.percentile(gamma_draws, 90)), 4),
        "ci_excludes_zero": bool(np.percentile(gamma_draws, 2.5) > 0 or
                                  np.percentile(gamma_draws, 97.5) < 0),
    }

    ppp = compute_ppp(fit, resp_sub)

    # ESS and Rhat for gamma specifically
    summary_df = fit.summary()
    gamma_row = summary_df.loc["gamma"] if "gamma" in summary_df.index else None
    gamma_ess = None
    gamma_rhat = None
    if gamma_row is not None:
        for col in ["ESS_bulk", "N_Eff", "N_eff"]:
            if col in summary_df.columns:
                gamma_ess = round(float(gamma_row[col]), 1)
                break
        for col in ["R_hat", "Rhat"]:
            if col in summary_df.columns:
                gamma_rhat = round(float(gamma_row[col]), 4)
                break

    result = {
        "prior": prior_cfg["label"],
        "prior_sd": prior_cfg["prior_sd"],
        "n_models": n_models,
        "n_items": n_items,
        "fit_time_sec": round(elapsed, 1),
        "gamma": gamma_summary,
        "gamma_ess": gamma_ess,
        "gamma_rhat": gamma_rhat,
        "ppp": ppp,
        "diagnostics": diag,
    }

    log.info("γ̂=%.4f [%.4f, %.4f], PPP=%s, Rhat=%.4f, ESS=%.0f",
             gamma_summary["mean"], gamma_summary["q025"], gamma_summary["q975"],
             ppp, diag.get("max_rhat", 0), diag.get("min_ess", 0))

    return result


def compute_exposure_distribution(models, rrf_data, subsample_idx):
    """Compute empirical distribution of e_ij exposure scores."""
    exposure_full = build_rrf_exposure_matrix(models, rrf_data, "mmlu", 14042)
    exposure_sub = exposure_full[:, subsample_idx]

    all_eij = exposure_sub.flatten()
    overall = {
        "mean": round(float(np.mean(all_eij)), 6),
        "median": round(float(np.median(all_eij)), 6),
        "sd": round(float(np.std(all_eij)), 6),
        "min": round(float(np.min(all_eij)), 6),
        "max": round(float(np.max(all_eij)), 6),
        "q25": round(float(np.percentile(all_eij, 25)), 6),
        "q75": round(float(np.percentile(all_eij, 75)), 6),
        "n_total": int(all_eij.size),
        "n_zero": int(np.sum(all_eij == 0)),
        "pct_zero": round(float(np.mean(all_eij == 0) * 100), 2),
    }

    # Per-dosage distribution
    dosages_unique = sorted(set(m["dosage"] for m in models))
    per_dosage = {}
    for d in dosages_unique:
        idx = [i for i, m in enumerate(models) if m["dosage"] == d]
        eij_d = exposure_sub[idx].flatten()
        per_dosage[f"d{d:03d}"] = {
            "n_models": len(idx),
            "mean": round(float(np.mean(eij_d)), 6),
            "median": round(float(np.median(eij_d)), 6),
            "sd": round(float(np.std(eij_d)), 6),
            "min": round(float(np.min(eij_d)), 6),
            "max": round(float(np.max(eij_d)), 6),
            "q25": round(float(np.percentile(eij_d, 25)), 6),
            "q75": round(float(np.percentile(eij_d, 75)), 6),
        }

    # Per-item distribution (across models)
    item_means = exposure_sub.mean(axis=0)
    item_stats = {
        "mean_across_items": round(float(np.mean(item_means)), 6),
        "sd_across_items": round(float(np.std(item_means)), 6),
        "min_item_mean": round(float(np.min(item_means)), 6),
        "max_item_mean": round(float(np.max(item_means)), 6),
    }

    return {
        "overall": overall,
        "per_dosage": per_dosage,
        "per_item_summary": item_stats,
    }


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load data (same as N=16 fixed baseline)
    log.info("Loading eval results...")
    data = load_pooled_eval_results(
        EVAL_DIR, ["1.5B", "3B"], benchmarks=["mmlu"], aligned_only=True)
    log.info("Loaded %d models", len(data["models"]))

    rrf_data = load_rrf_exposure(EXPOSURE_FILE)
    log.info("Loaded RRF exposure for %d models", len(rrf_data))

    bd = data["benchmarks"]["mmlu"]
    responses = bd["responses"]
    D045_EXCLUDE = {"0.5B"}

    models, dosages, responses = filter_models_for_benchmark(
        data["models"], data["dosages"], responses, rrf_data,
        "mmlu", exclude_scales=D045_EXCLUDE)

    log.info("After filtering: %d models, %d items", len(models), responses.shape[1])

    # Subsample to 300 items (same seed as baseline)
    n_items_full = responses.shape[1]
    if n_items_full > MAX_ITEMS:
        np.random.seed(42)
        subsample_idx = np.sort(np.random.choice(n_items_full, MAX_ITEMS, replace=False))
        log.info("Subsampled %d -> %d items", n_items_full, MAX_ITEMS)
    else:
        subsample_idx = np.arange(n_items_full)

    # Task A: Run three priors
    results = {}
    for key, cfg in PRIOR_CONFIGS.items():
        results[key] = run_single_prior(
            key, cfg, models, dosages,
            responses, rrf_data, subsample_idx)

    # Task B: Exposure distribution
    log.info("=" * 60)
    log.info("Computing exposure distribution...")
    exposure_dist = compute_exposure_distribution(models, rrf_data, subsample_idx)

    # Save results
    output = {
        "task": "SF5_gamma_prior_sensitivity",
        "benchmark": "mmlu",
        "n_models": len(models),
        "n_items": int(len(subsample_idx)),
        "model_list": [
            {"dirname": m["dirname"], "scale": m.get("scale", ""),
             "dosage": m["dosage"]}
            for m in models
        ],
        "prior_sensitivity": results,
        "exposure_distribution": exposure_dist,
    }

    out_path = output_dir / "gamma_prior_sensitivity_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    log.info("Results saved to %s", out_path)

    # Print comparison table
    print("\n" + "=" * 90)
    print("SF5: GAMMA PRIOR SENSITIVITY (MMLU, J=16, 2PL+γ)")
    print("=" * 90)
    print(f"{'Prior':<12} {'γ̂ mean':>8} {'γ̂ med':>8} {'SD':>7} "
          f"{'95% CI':>22} {'PPP':>7} {'Rhat':>7} {'ESS':>7} {'Time':>6}")
    print("-" * 90)
    for key in ["tight_05", "default_10", "loose_20"]:
        r = results[key]
        g = r["gamma"]
        print(f"{r['prior']:<12} {g['mean']:>8.4f} {g['median']:>8.4f} {g['sd']:>7.4f} "
              f"[{g['q025']:>7.4f}, {g['q975']:>7.4f}] "
              f"{r['ppp']:>7.4f} {r['gamma_rhat']:>7.4f} {r['gamma_ess']:>7.0f} "
              f"{r['fit_time_sec']:>5.0f}s")

    print("\n" + "=" * 90)
    print("EXPOSURE DISTRIBUTION (e_ij, RRF-selected 300 items)")
    print("=" * 90)
    ov = exposure_dist["overall"]
    print(f"Overall: mean={ov['mean']:.4f}, median={ov['median']:.4f}, "
          f"sd={ov['sd']:.4f}, range=[{ov['min']:.4f}, {ov['max']:.4f}]")
    print(f"         Q25={ov['q25']:.4f}, Q75={ov['q75']:.4f}, "
          f"n_zero={ov['n_zero']}, pct_zero={ov['pct_zero']:.1f}%")
    print("\nPer-dosage:")
    print(f"  {'Dosage':<8} {'N':>3} {'Mean':>8} {'Median':>8} {'SD':>8} "
          f"{'Min':>8} {'Max':>8} {'Q25':>8} {'Q75':>8}")
    for dk, dv in exposure_dist["per_dosage"].items():
        print(f"  {dk:<8} {dv['n_models']:>3} {dv['mean']:>8.4f} {dv['median']:>8.4f} "
              f"{dv['sd']:>8.4f} {dv['min']:>8.4f} {dv['max']:>8.4f} "
              f"{dv['q25']:>8.4f} {dv['q75']:>8.4f}")


if __name__ == "__main__":
    main()

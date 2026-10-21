"""
Joint IRT fitting: shared global gamma across all benchmarks (ABLATION).

Concatenates per-benchmark response/exposure matrices into a single
(N_models, sum_N_items) matrix and fits one 4PL+gamma model.
The resulting gamma is the global contamination effect.

Input: same as run_irt_calibration (eval-dir + exposure-file)
Output: single gamma posterior, per-model calibrated scores (across all items)
"""

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_irt_calibration import (
    load_eval_results,
    load_pooled_eval_results,
    load_exposure_scores,
    build_exposure_matrix,
    prepare_stan_data,
    fit_stan_model,
    check_convergence,
    posterior_predictive_check,
    extract_results,
    _summarize_vector,
    STAN_MODELS,
)

log = logging.getLogger(__name__)



def concatenate_benchmarks(data, exposure_scores, benchmarks=None,
                           exclude_rules=None, max_items=None, seed=42):
    """Concatenate all benchmark data into a single response/exposure matrix.

    Args:
        data: output of load_eval_results
        exposure_scores: per-benchmark tau vectors
        benchmarks: subset of benchmarks to include (None=all)
        exclude_rules: list of dicts {"model", "benchmark", "reason"}.
            When a model matching the pattern is present, that benchmark
            is excluded from the joint fit.

    Returns:
        dict with y, exposure, dosages, benchmark_slices, valid_models
    """
    dosages = data["dosages"]
    models = data["models"]
    bench_names = benchmarks or list(data["benchmarks"].keys())

    excluded_benchmarks = set()
    if exclude_rules:
        model_names = [m["model_name"] for m in models]
        for rule in exclude_rules:
            rule_model = rule.get("model", "")
            rule_bench = rule.get("benchmark", "")
            if any(rule_model in mn for mn in model_names):
                excluded_benchmarks.add(rule_bench.lower())
                log.info("Exclude rule: skipping benchmark %s (model=%s, reason=%s)",
                         rule_bench, rule_model, rule.get("reason", "n/a"))

    all_y = []
    all_exposure = []
    slices = {}
    col_offset = 0
    all_valid = []

    for bench in bench_names:
        if bench not in data["benchmarks"]:
            continue
        if bench.lower() in excluded_benchmarks:
            continue
        bd = data["benchmarks"][bench]
        responses = bd["responses"]
        valid = bd["valid_mask"]
        all_valid.append(valid)
        tau = exposure_scores[bench]
        n_items = bd["n_items"]

        if not valid.all():
            responses_valid = responses[valid]
            dosages_valid = dosages[valid]
        else:
            responses_valid = responses
            dosages_valid = dosages

        exposure_matrix = build_exposure_matrix(dosages_valid, tau[:n_items])

        # D023 + Reviewer: random subsampling per benchmark (not truncation)
        if max_items and n_items > max_items:
            rng = np.random.default_rng(seed)
            idx = np.sort(rng.choice(n_items, max_items, replace=False))
            responses_valid = responses_valid[:, idx]
            exposure_matrix = exposure_matrix[:, idx]
            log.info("Joint fit: %s subsampled %d -> %d items (seed=%d)",
                     bench, n_items, max_items, seed)
            n_items = max_items

        all_y.append(responses_valid)
        all_exposure.append(exposure_matrix)
        slices[bench] = (col_offset, col_offset + n_items)
        col_offset += n_items

    if len(all_valid) > 1:
        for v in all_valid[1:]:
            assert np.array_equal(v, all_valid[0]), \
                "valid model masks differ across benchmarks \u2014 cannot concatenate safely"

    y_concat = np.concatenate(all_y, axis=1)
    exp_concat = np.concatenate(all_exposure, axis=1)

    return {
        "y": y_concat,
        "exposure": exp_concat,
        "dosages": dosages,
        "benchmark_slices": slices,
        "n_total_items": col_offset,
    }


def run_joint_fit(eval_dir, exposure_file, output_dir, benchmarks=None,
                  exclude_rules=None, model_type="4pl_gamma",
                  chains=4, warmup=1000, samples=1000, adapt_delta=0.95,
                  max_treedepth=12, seed=42, dry_run=False, max_items=None,
                  tau_model_id=None, model_scale=None, seed_filter=None, parallel_chains=None,
                  aligned_only=False, pool_scales=None):
    """Fit a single IRT model with shared gamma across all benchmarks."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if pool_scales:
        data = load_pooled_eval_results(eval_dir, pool_scales, benchmarks,
                                         seed_filter=seed_filter,
                                         aligned_only=aligned_only)
    else:
        data = load_eval_results(eval_dir, benchmarks,
                                  model_scale=model_scale,
                                  seed_filter=seed_filter,
                                  aligned_only=aligned_only)
    exposure_scores = load_exposure_scores(exposure_file, data["benchmarks"], model_id=tau_model_id)

    concat = concatenate_benchmarks(data, exposure_scores, benchmarks,
                                    exclude_rules=exclude_rules,
                                    max_items=max_items, seed=seed)

    y = concat["y"]
    exposure = concat["exposure"]
    log.info("Joint fit: %d models x %d total items", y.shape[0], y.shape[1])
    log.info("Benchmark slices: %s", concat["benchmark_slices"])

    stan_data = prepare_stan_data(y, exposure)

    fit, elapsed = fit_stan_model(
        STAN_MODELS[model_type], stan_data,
        chains=chains, iter_warmup=warmup, iter_sampling=samples,
        adapt_delta=adapt_delta, max_treedepth=max_treedepth, seed=seed,
        parallel_chains=parallel_chains,
    )

    diagnostics = check_convergence(fit)
    ppc = posterior_predictive_check(fit, y)
    results = extract_results(fit, y, model_type)

    # Per-benchmark calibrated scores (from the joint gamma)
    gamma_draws = fit.stan_variable("gamma")
    cal_draws = fit.stan_variable("calibrated_score")

    per_bench_cal = {}
    for bench, (start, end) in concat["benchmark_slices"].items():
        bench_item_range = range(start, min(end, y.shape[1]))
        if len(bench_item_range) == 0:
            continue
        theta_draws = fit.stan_variable("theta")
        a_draws = fit.stan_variable("a")
        b_draws = fit.stan_variable("b")
        has_cd = model_type.startswith("4pl") or model_type.startswith("vanilla_4pl")
        if has_cd:
            c_draws = fit.stan_variable("c")
            d_draws = fit.stan_variable("d")

        n_draws = theta_draws.shape[0]
        n_models = theta_draws.shape[1]
        bench_items = list(bench_item_range)
        n_bench_items = len(bench_items)

        bench_cal = np.zeros((n_draws, n_models))
        for draw in range(n_draws):
            for i in range(n_models):
                total = 0.0
                for jj, j in enumerate(bench_items):
                    eta_clean = a_draws[draw, j] * (theta_draws[draw, i] - b_draws[draw, j])
                    if has_cd:
                        p_clean = c_draws[draw, j] + (d_draws[draw, j] - c_draws[draw, j]) / (1 + np.exp(-eta_clean))
                    else:
                        p_clean = 1.0 / (1 + np.exp(-eta_clean))
                    total += p_clean
                bench_cal[draw, i] = total / n_bench_items
        per_bench_cal[bench] = _summarize_vector(bench_cal)

    result = {
        "mode": "joint_fit",
        "model_type": f"{model_type}_joint",
        "n_models": int(y.shape[0]),
        "n_total_items": int(y.shape[1]),
        "benchmark_slices": {k: list(v) for k, v in concat["benchmark_slices"].items()},
        "fit_time_sec": round(elapsed, 1),
        "diagnostics": diagnostics,
        "posterior_predictive": ppc,
        "global_gamma": results.get("gamma", {}),
        "calibrated_scores_joint": results["calibrated_scores"],
        "calibrated_scores_per_benchmark": per_bench_cal,
        "models": [
            {"dirname": m["dirname"], "model_name": m["model_name"],
             "dosage": m["dosage"], "seed": m["seed"]}
            for m in data["models"]
        ],
        "dosages": concat["dosages"].tolist(),
    }

    with open(output_dir / "joint_fit_results.json", "w") as f:
        json.dump(result, f, indent=2)

    log.info("Joint fit: gamma=%.4f [%.4f, %.4f], time=%.1fs",
             results["gamma"]["mean"], results["gamma"]["q025"],
             results["gamma"]["q975"], elapsed)
    log.info("Joint fit results saved to %s", output_dir)
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Joint IRT fitting with shared global gamma (ABLATION)")
    parser.add_argument("--eval-dir", type=str,
                        default="/root/autodl-tmp/exp001/eval_results")
    parser.add_argument("--exposure-file", type=str, default=None)
    parser.add_argument("--tau-model-id", type=str, default=None,
                        help="Model ID for exposure tau (e.g. Qwen2.5-0.5B_d100_s42)")
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--benchmarks", nargs="*", default=None)
    parser.add_argument("--model-scale", type=str, default=None,
                        help="Model scale filter.")
    parser.add_argument("--data-seed", type=int, default=None,
                        help="Data seed filter.")
    parser.add_argument("--aligned-only", action="store_true",
                        help="Only load aligned-format eval directories.")
    parser.add_argument("--chains", type=int, default=4)
    parser.add_argument("--warmup", type=int, default=1000)
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--adapt-delta", type=float, default=0.95)
    parser.add_argument("--max-treedepth", type=int, default=12)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-items", type=int, default=100)
    parser.add_argument("--model-type", default="4pl_gamma",
                        choices=["4pl_gamma", "2pl_gamma", "vanilla_4pl", "4pl_gamma_wider"],
                        help="IRT model type")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

    run_joint_fit(
        args.eval_dir, args.exposure_file, args.output_dir,
        benchmarks=args.benchmarks, chains=args.chains,
        warmup=args.warmup, samples=args.samples,
        adapt_delta=args.adapt_delta, max_treedepth=args.max_treedepth,
        seed=args.seed, dry_run=args.dry_run, max_items=args.max_items,
        tau_model_id=args.tau_model_id,
        model_scale=args.model_scale,
        seed_filter=args.data_seed,
        aligned_only=args.aligned_only,
        model_type=args.model_type,
    )


if __name__ == "__main__":
    main()

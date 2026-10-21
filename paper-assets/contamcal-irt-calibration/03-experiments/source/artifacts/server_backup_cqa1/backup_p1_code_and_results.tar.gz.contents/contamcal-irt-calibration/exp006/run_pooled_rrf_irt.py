#!/usr/bin/env python3
"""Pooled IRT fitting with RRF signal-based exposure (per-model, per-item).

Runs per-benchmark 4PL+γ IRT with exposure matrix from RRF output.
Supports D045 exclusion (0.5B excluded from MMLU/ARC).
"""

import argparse
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
    load_pooled_eval_results,
    prepare_stan_data,
    fit_stan_model,
    check_convergence,
    posterior_predictive_check,
    extract_results,
    STAN_MODELS,
)

log = logging.getLogger(__name__)

EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
MAX_ITEMS = 300


def strip_aligned(dirname):
    return re.sub(r'(_para)?(_aligned)?$', '', dirname)


def normalize_model_key(key):
    a_match = re.search(r'_(a\d+)', key)
    s_match = re.search(r'_(s\d+)', key)
    base = re.sub(r'_(a\d+|s\d+)', '', key)
    suffix = ''
    if a_match:
        suffix += '_' + a_match.group(1)
    if s_match:
        suffix += '_' + s_match.group(1)
    return base + suffix


def resolve_rrf_key(eval_key, rrf_data, norm_rrf):
    if eval_key in rrf_data:
        return eval_key
    norm = normalize_model_key(eval_key)
    if norm in norm_rrf:
        return norm_rrf[norm]
    if '_a' not in eval_key:
        norm_a32 = normalize_model_key(eval_key + '_a32')
        if norm_a32 in norm_rrf:
            return norm_rrf[norm_a32]
    return None


def load_rrf_exposure(path):
    with open(path) as f:
        return json.load(f)


def build_rrf_exposure_matrix(models, rrf_data, benchmark, n_items):
    """Build exposure matrix from per-model/per-item RRF scores."""
    N = len(models)
    norm_rrf = {normalize_model_key(k): k for k in rrf_data}
    exposure = np.zeros((N, n_items), dtype=float)
    for i, m in enumerate(models):
        rrf_key = m.get("_rrf_key") or resolve_rrf_key(
            strip_aligned(m["dirname"]), rrf_data, norm_rrf)
        scores = rrf_data[rrf_key][benchmark]["exposure_scores"]
        exposure[i, :] = scores[:n_items]
    return exposure


def filter_models_for_benchmark(models, dosages, responses, rrf_data,
                                 benchmark, exclude_scales=None):
    """Filter to models that have RRF exposure for this benchmark + D045."""
    norm_rrf = {normalize_model_key(k): k for k in rrf_data}
    keep = []
    for i, m in enumerate(models):
        key = strip_aligned(m["dirname"])
        rrf_key = resolve_rrf_key(key, rrf_data, norm_rrf)
        if rrf_key is None:
            continue
        if benchmark not in rrf_data[rrf_key]:
            continue
        if exclude_scales and m.get("scale", "") in exclude_scales:
            log.info("D045 exclude: %s (scale %s on %s)",
                     m["dirname"], m["scale"], benchmark)
            continue
        m["_rrf_key"] = rrf_key
        keep.append(i)

    keep = np.array(keep)
    return (
        [models[i] for i in keep],
        dosages[keep],
        responses[keep],
    )


def compute_mae(raw_acc, cal_mean):
    """MAE between raw accuracy and calibrated posterior mean."""
    return float(np.mean(np.abs(np.array(raw_acc) - np.array(cal_mean))))


def run_benchmark(benchmark, models, dosages, responses, rrf_data,
                  exclude_scales, model_type, args):
    log.info("=" * 60)
    log.info("Benchmark: %s", benchmark)

    models_f, dosages_f, resp_f = filter_models_for_benchmark(
        models, dosages, responses, rrf_data, benchmark, exclude_scales)

    n_models = len(models_f)
    n_items = resp_f.shape[1] if n_models > 0 else 0
    log.info("N_models=%d, N_items=%d (after filtering)", n_models, n_items)

    if n_models < 3:
        log.warning("Too few models (%d), skipping %s", n_models, benchmark)
        return None

    original_n_items = n_items
    subsampled = False
    subsample_idx = None
    if n_items > MAX_ITEMS:
        np.random.seed(42)
        subsample_idx = np.sort(np.random.choice(n_items, MAX_ITEMS, replace=False))
        resp_f = resp_f[:, subsample_idx]
        n_items = MAX_ITEMS
        subsampled = True
        log.info("Subsampled: %d -> %d items", original_n_items, n_items)

    exposure = build_rrf_exposure_matrix(models_f, rrf_data, benchmark, original_n_items)
    if subsample_idx is not None:
        exposure = exposure[:, subsample_idx]

    log.info("Exposure stats: mean=%.4f, max=%.4f, nonzero=%.1f%%",
             exposure.mean(), exposure.max(),
             100 * (exposure > 0).mean())

    for i, m in enumerate(models_f):
        log.info("  %s (scale=%s, d=%d): mean_exp=%.4f",
                 m["dirname"], m.get("scale", "?"), m.get("dosage", -1),
                 exposure[i].mean())

    stan_data = prepare_stan_data(resp_f, exposure, model_type)

    fit, elapsed = fit_stan_model(
        STAN_MODELS[model_type], stan_data,
        chains=args.chains,
        iter_warmup=args.warmup,
        iter_sampling=args.samples,
        adapt_delta=args.adapt_delta,
        max_treedepth=args.max_treedepth,
        seed=args.seed,
        parallel_chains=args.parallel_chains,
    )

    diagnostics = check_convergence(fit)
    ppc = posterior_predictive_check(fit, resp_f)
    results = extract_results(fit, resp_f, model_type)

    raw_acc = results["raw_accuracy"]
    cal_mean = results["calibrated_scores"]["mean"]
    raw_mae = float(np.mean(np.abs(np.array(raw_acc) - np.mean(raw_acc))))
    cal_mae = compute_mae(raw_acc, cal_mean)

    return {
        "benchmark": benchmark,
        "model_type": model_type,
        "exposure_source": "rrf_signal",
        "n_models": n_models,
        "n_items": n_items,
        "original_n_items": original_n_items,
        "subsampled": subsampled,
        "models": [{"dirname": m["dirname"], "scale": m.get("scale", ""),
                     "dosage": m.get("dosage", -1)} for m in models_f],
        "fit_time_sec": round(elapsed, 1),
        "diagnostics": diagnostics,
        "posterior_predictive": ppc,
        "gamma": results.get("gamma", {}),
        "calibrated_scores": results.get("calibrated_scores", {}),
        "raw_accuracy": raw_acc,
        "raw_mae": round(raw_mae, 4),
        "cal_mae": round(cal_mae, 4),
        "delta_mae": round(raw_mae - cal_mae, 4),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--eval-dir", default=EVAL_DIR)
    parser.add_argument("--scales", nargs="+", default=["0.5B", "1.5B"])
    parser.add_argument("--benchmarks", nargs="+",
                        default=["gsm8k", "arc_challenge"])
    parser.add_argument("--exposure-file", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--model-type", default="4pl_gamma",
                        choices=list(STAN_MODELS.keys()))
    parser.add_argument("--chains", type=int, default=4)
    parser.add_argument("--warmup", type=int, default=1000)
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--adapt-delta", type=float, default=0.95)
    parser.add_argument("--max-treedepth", type=int, default=12)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--parallel-chains", type=int, default=1)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    rrf_data = load_rrf_exposure(args.exposure_file)
    log.info("Loaded RRF exposure for %d models", len(rrf_data))

    log.info("Loading eval results: scales=%s", args.scales)
    data = load_pooled_eval_results(
        args.eval_dir, args.scales, benchmarks=args.benchmarks,
        aligned_only=True)
    log.info("Loaded %d models", len(data["models"]))

    # D045: 0.5B excluded from mmlu and arc_challenge
    D045_EXCLUDE = {"mmlu": {"0.5B"}, "arc_challenge": {"0.5B"}}

    all_results = {
        "config": {
            "model_type": args.model_type,
            "scales": args.scales,
            "benchmarks": args.benchmarks,
            "exposure": "rrf_signal",
            "exclusions": ["D045_05B_mmlu_arc"],
            "stan_config": {
                "chains": args.chains, "warmup": args.warmup,
                "samples": args.samples, "adapt_delta": args.adapt_delta,
                "max_treedepth": args.max_treedepth, "seed": args.seed,
            },
        },
        "per_benchmark": {},
    }

    for bench in args.benchmarks:
        if bench not in data["benchmarks"]:
            log.warning("Benchmark %s not in eval data, skipping", bench)
            continue

        bd = data["benchmarks"][bench]
        exclude_scales = D045_EXCLUDE.get(bench, set())

        result = run_benchmark(
            bench, data["models"], data["dosages"],
            bd["responses"], rrf_data, exclude_scales,
            args.model_type, args)

        if result:
            all_results["per_benchmark"][bench] = result
            bench_dir = output_dir / bench
            bench_dir.mkdir(parents=True, exist_ok=True)
            with open(bench_dir / "irt_results.json", "w") as f:
                json.dump(result, f, indent=2)

            g = result.get("gamma", {})
            d = result["diagnostics"]
            if g:
                log.info("[%s] γ=%.4f [%.4f, %.4f], R̂=%.4f, ESS=%.0f, div=%d",
                         bench, g["mean"], g["q025"], g["q975"],
                         d.get("max_rhat", 0), d.get("min_ess", 0),
                         d.get("divergent_count", 0))
            else:
                log.info("[%s] (no gamma) R̂=%.4f, ESS=%.0f, div=%d",
                         bench, d.get("max_rhat", 0), d.get("min_ess", 0),
                         d.get("divergent_count", 0))
            log.info("[%s] raw_MAE=%.4f, cal_MAE=%.4f, ΔMAE=%.4f",
                     bench, result["raw_mae"], result["cal_mae"],
                     result["delta_mae"])

    with open(output_dir / "pooled_rrf_irt_results.json", "w") as f:
        json.dump(all_results, f, indent=2)

    # Summary table
    print("\n" + "=" * 80)
    print("POOLED IRT RESULTS (4PL+γ, RRF signal exposure)")
    print("=" * 80)
    print(f"{'Bench':<16} {'N_mod':>5} {'N_item':>6} {'γ̂':>8} {'95% CI':>20} "
          f"{'R̂':>6} {'ESS':>6} {'PPP':>6} {'rawMAE':>7} {'calMAE':>7} {'ΔMAE':>6}")
    print("-" * 80)

    for bench in args.benchmarks:
        if bench not in all_results["per_benchmark"]:
            print(f"{bench:<16} SKIPPED")
            continue
        r = all_results["per_benchmark"][bench]
        g = r.get("gamma", {})
        d = r["diagnostics"]
        ppc = r["posterior_predictive"]
        gamma_str = f"{g['mean']:>8.4f} [{g['q025']:.4f}, {g['q975']:.4f}]" if g else "     N/A                  N/A"
        print(f"{bench:<16} {r['n_models']:>5} {r['n_items']:>6} "
              f"{gamma_str} "
              f"{d.get('max_rhat', 0):>6.4f} {d.get('min_ess', 0):>6.0f} "
              f"{ppc.get('overall_ppp', 0):>6.4f} "
              f"{r['raw_mae']:>7.4f} {r['cal_mae']:>7.4f} {r['delta_mae']:>6.4f}")

    print(f"\nResults saved to {output_dir}")


if __name__ == "__main__":
    main()

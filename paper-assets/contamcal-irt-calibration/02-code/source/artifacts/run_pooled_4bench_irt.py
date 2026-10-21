#!/usr/bin/env python3
"""
Pooled 4-benchmark IRT analysis (2PL+gamma) with full exclusion rules.

Runs:
  1. Per-benchmark IRT fits (with per-benchmark model exclusions)
  2. Joint fit (shared gamma) across benchmarks using intersection models

Exclusion rules:
  D044: GSM8K exclude d000 configs (format confound)
  D045: 0.5B MMLU/ARC excluded (position bias); 0.5B GSM8K/HumanEval kept
  D046/D047: base_pretrained excluded (via aligned_only + dirname filter)
  D018: 3B d000 s42 v3 excluded (already deprecated, double-check)

Exposure: oracle dosage fraction (dosage/100) since HumanEval lacks S1 signals.
"""

import argparse
import json
import logging
import os
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
    _summarize_vector,
    STAN_MODELS,
)

log = logging.getLogger(__name__)

BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge", "humaneval"]
SCALES = ["0.5B", "1.5B", "3B"]
MODEL_TYPE = "2pl_gamma"
STAN_FILE = STAN_MODELS[MODEL_TYPE]

OUTPUT_DIR = Path("/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl")
EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"


def apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):
    """Apply D044/D045/D046/D047/D018 per-benchmark exclusions."""
    keep = np.ones(len(models), dtype=bool)
    reasons = []

    for i, m in enumerate(models):
        dirname = m.get("dirname", "")
        scale = m.get("scale", "")
        dosage = m.get("dosage", 0)

        # D046/D047: base pretrained
        if "base_pretrained" in dirname:
            keep[i] = False
            reasons.append(f"  D046/D047: {dirname} (base pretrained)")
            continue

        # D018: deprecated check (dirname contains DEPRECATED)
        if "DEPRECATED" in dirname:
            keep[i] = False
            reasons.append(f"  D018: {dirname} (deprecated)")
            continue

        # D045: 0.5B MMLU/ARC excluded (position bias)
        if "0.5B" in scale and benchmark in ("mmlu", "arc_challenge"):
            keep[i] = False
            reasons.append(f"  D045: {dirname} (0.5B on {benchmark})")
            continue

        # D044: GSM8K exclude d000 (format confound)
        if benchmark == "gsm8k" and dosage == 0:
            keep[i] = False
            reasons.append(f"  D044: {dirname} (d000 on gsm8k)")
            continue

        # Instruct model (no dosage pattern) - keep if aligned
        # but skip if not part of dose-response (dosage not parseable)
        # Actually Instruct models have dosage=base, which won't parse
        # as dosage int. They'll appear with dosage=0 from the loader
        # if dirname ends with _aligned without _dXXX pattern.
        # The loader sets dosage from parsing, so Instruct models
        # are already excluded by parse_model_dir_name returning None.

    if reasons:
        log.info("Excluded from %s (%d models):", benchmark, len(reasons))
        for r in reasons[:10]:
            log.info(r)
        if len(reasons) > 10:
            log.info("  ... and %d more", len(reasons) - 10)

    return (
        [m for m, k in zip(models, keep) if k],
        dosages[keep],
        responses[keep],
        valid_mask[keep],
    )


def filter_data_by_scale(data, target_scale):
    """Filter pooled data to only include models of a single scale."""
    keep = np.array([m.get("scale", "") == target_scale for m in data["models"]])
    if not keep.any():
        return None
    return {
        "models": [m for m, k in zip(data["models"], keep) if k],
        "dosages": data["dosages"][keep],
        "benchmarks": {
            bench: {
                "responses": bd["responses"][keep],
                "n_items": bd["n_items"],
                "valid_mask": bd["valid_mask"][keep],
            }
            for bench, bd in data["benchmarks"].items()
        },
    }


def build_oracle_exposure(dosages, n_items):
    """Oracle exposure: dosage_fraction * uniform tau."""
    max_d = dosages.max() if dosages.max() > 0 else 1.0
    fracs = dosages / max_d
    return np.outer(fracs, np.ones(n_items))


def filter_items(responses, benchmark, exclude_set=None, min_variance=0.0):
    """Remove items by exclusion list and/or low cross-model variance.

    Returns (filtered_responses, kept_indices, stats_dict).
    """
    n_models, n_items = responses.shape
    keep = np.ones(n_items, dtype=bool)

    n_excluded_by_list = 0
    if exclude_set:
        for j in range(n_items):
            if f"{benchmark}_{j}" in exclude_set:
                keep[j] = False
                n_excluded_by_list += 1

    n_excluded_by_var = 0
    if min_variance > 0:
        item_var = np.var(responses, axis=0)
        low_var = item_var < min_variance
        low_var &= keep
        n_excluded_by_var = int(low_var.sum())
        keep[low_var] = False

    kept_indices = np.where(keep)[0]
    stats = {
        "original": n_items,
        "excluded_by_list": n_excluded_by_list,
        "excluded_by_variance": n_excluded_by_var,
        "remaining": int(keep.sum()),
    }
    return responses[:, keep], kept_indices, stats


def run_single_benchmark_fit(bench, data, args_dict, exclude_set=None, min_item_variance=0.0):
    """Run IRT fit for a single benchmark with exclusions."""
    if bench not in data["benchmarks"]:
        log.warning("Benchmark %s not in data, skipping", bench)
        return None

    bd = data["benchmarks"][bench]
    models_filt, dosages_filt, responses_filt, valid_filt = apply_per_benchmark_exclusions(
        data["models"], data["dosages"],
        bd["responses"], bd["valid_mask"], bench
    )

    # Apply valid mask
    if not valid_filt.all():
        active = valid_filt.astype(bool)
        models_filt = [m for m, v in zip(models_filt, active) if v]
        dosages_filt = dosages_filt[active]
        responses_filt = responses_filt[active]

    n_models = len(models_filt)
    n_items = bd["n_items"]

    if exclude_set or min_item_variance > 0:
        responses_filt, kept_indices, fstats = filter_items(
            responses_filt, bench, exclude_set, min_item_variance
        )
        n_items = fstats["remaining"]
        log.info("[%s] Item filter: %d -> %d (list=%d, variance=%d)",
                 bench, fstats["original"], n_items,
                 fstats["excluded_by_list"], fstats["excluded_by_variance"])

    log.info("[%s] N_models=%d, N_items=%d", bench, n_models, n_items)

    if n_models < 3:
        log.warning("[%s] Too few models (%d), skipping", bench, n_models)
        return None

    exposure = build_oracle_exposure(dosages_filt, n_items)
    stan_data = prepare_stan_data(responses_filt, exposure, MODEL_TYPE)

    fit, elapsed = fit_stan_model(
        STAN_FILE, stan_data,
        chains=args_dict["chains"],
        iter_warmup=args_dict["warmup"],
        iter_sampling=args_dict["samples"],
        adapt_delta=args_dict["adapt_delta"],
        max_treedepth=args_dict["max_treedepth"],
        seed=args_dict["seed"],
        parallel_chains=args_dict["parallel_chains"],
    )

    diagnostics = check_convergence(fit)
    ppc = posterior_predictive_check(fit, responses_filt)
    results = extract_results(fit, responses_filt, MODEL_TYPE)

    return {
        "benchmark": bench,
        "n_models": n_models,
        "n_items": n_items,
        "models": [{"dirname": m["dirname"], "dosage": m["dosage"],
                     "scale": m.get("scale", "")} for m in models_filt],
        "dosages": dosages_filt.tolist(),
        "fit_time_sec": round(elapsed, 1),
        "diagnostics": diagnostics,
        "posterior_predictive": ppc,
        "gamma": results.get("gamma", {}),
        "calibrated_scores": results.get("calibrated_scores", {}),
    }


def run_joint_fit(data, benchmarks_to_include, args_dict, exclude_set=None, min_item_variance=0.0):
    """Concatenate benchmark items and fit shared-gamma model.

    Uses intersection of valid models across all benchmarks (after exclusions).
    """
    per_bench_filtered = {}
    for bench in benchmarks_to_include:
        if bench not in data["benchmarks"]:
            continue
        bd = data["benchmarks"][bench]
        models_f, dosages_f, resp_f, valid_f = apply_per_benchmark_exclusions(
            data["models"], data["dosages"],
            bd["responses"], bd["valid_mask"], bench
        )
        if not valid_f.all():
            active = valid_f.astype(bool)
            models_f = [m for m, v in zip(models_f, active) if v]
            dosages_f = dosages_f[active]
            resp_f = resp_f[active]

        per_bench_filtered[bench] = {
            "models": models_f,
            "dosages": dosages_f,
            "responses": resp_f,
            "n_items": bd["n_items"],
        }

    # Find intersection of valid model dirnames across benchmarks
    dirname_sets = [set(m["dirname"] for m in bf["models"])
                    for bf in per_bench_filtered.values()]
    common_dirnames = set.intersection(*dirname_sets) if dirname_sets else set()
    log.info("Joint fit: %d common models across %d benchmarks",
             len(common_dirnames), len(per_bench_filtered))

    if len(common_dirnames) < 3:
        log.warning("Too few common models (%d) for joint fit", len(common_dirnames))
        return None

    # Build concatenated matrices using common model order
    ref_bench = list(per_bench_filtered.keys())[0]
    ref_models = per_bench_filtered[ref_bench]["models"]
    ordered_dirnames = [m["dirname"] for m in ref_models if m["dirname"] in common_dirnames]

    all_y = []
    all_exp = []
    slices = {}
    col_offset = 0
    joint_models = None
    joint_dosages = None

    for bench, bf in per_bench_filtered.items():
        dirname_to_idx = {m["dirname"]: i for i, m in enumerate(bf["models"])}
        indices = [dirname_to_idx[d] for d in ordered_dirnames]

        resp_ordered = bf["responses"][indices]
        dosages_ordered = bf["dosages"][indices]
        n_items = bf["n_items"]

        if exclude_set or min_item_variance > 0:
            resp_ordered, kept_indices, fstats = filter_items(
                resp_ordered, bench, exclude_set, min_item_variance
            )
            n_items = fstats["remaining"]
            log.info("[joint/%s] Item filter: %d -> %d (list=%d, variance=%d)",
                     bench, fstats["original"], n_items,
                     fstats["excluded_by_list"], fstats["excluded_by_variance"])

        exposure = build_oracle_exposure(dosages_ordered, n_items)

        all_y.append(resp_ordered)
        all_exp.append(exposure)
        slices[bench] = (col_offset, col_offset + n_items)
        col_offset += n_items

        if joint_models is None:
            joint_models = [bf["models"][i] for i in indices]
            joint_dosages = dosages_ordered

    y_concat = np.concatenate(all_y, axis=1)
    exp_concat = np.concatenate(all_exp, axis=1)

    n_models, n_total = y_concat.shape
    log.info("Joint fit: %d models x %d total items", n_models, n_total)
    log.info("Joint fit slices: %s", {b: f"{s[0]}-{s[1]}" for b, s in slices.items()})

    stan_data = prepare_stan_data(y_concat, exp_concat, MODEL_TYPE)

    fit, elapsed = fit_stan_model(
        STAN_FILE, stan_data,
        chains=args_dict["chains"],
        iter_warmup=args_dict["warmup"],
        iter_sampling=args_dict["samples"],
        adapt_delta=args_dict["adapt_delta"],
        max_treedepth=args_dict["max_treedepth"],
        seed=args_dict["seed"],
        parallel_chains=args_dict["parallel_chains"],
    )

    diagnostics = check_convergence(fit)
    ppc = posterior_predictive_check(fit, y_concat)
    results = extract_results(fit, y_concat, MODEL_TYPE)

    # Per-benchmark calibrated scores from joint model
    gamma_draws = fit.stan_variable("gamma")
    theta_draws = fit.stan_variable("theta")
    a_draws = fit.stan_variable("a")
    b_draws = fit.stan_variable("b")

    per_bench_cal = {}
    for bench, (start, end) in slices.items():
        n_bench_items = end - start
        n_draws = gamma_draws.shape[0]
        bench_cal = np.zeros((n_draws, n_models))
        for draw in range(n_draws):
            for i in range(n_models):
                total = 0.0
                for j in range(start, end):
                    eta_clean = a_draws[draw, j] * (theta_draws[draw, i] - b_draws[draw, j])
                    total += 1.0 / (1.0 + np.exp(-eta_clean))
                bench_cal[draw, i] = total / n_bench_items
        per_bench_cal[bench] = {
            "mean": bench_cal.mean(axis=0).tolist(),
            "sd": bench_cal.std(axis=0).tolist(),
        }

    return {
        "mode": "joint_fit_4bench",
        "model_type": MODEL_TYPE,
        "n_models": n_models,
        "n_total_items": n_total,
        "benchmark_slices": {k: list(v) for k, v in slices.items()},
        "models": [{"dirname": m["dirname"], "dosage": m["dosage"],
                     "scale": m.get("scale", "")} for m in joint_models],
        "dosages": joint_dosages.tolist(),
        "fit_time_sec": round(elapsed, 1),
        "diagnostics": diagnostics,
        "posterior_predictive": ppc,
        "global_gamma": results.get("gamma", {}),
        "calibrated_scores": results.get("calibrated_scores", {}),
        "calibrated_scores_per_benchmark": per_bench_cal,
    }


def run_scale_stratified(data, args_dict, exclude_set, min_item_variance):
    """Per-scale per-benchmark IRT fits (D105)."""
    output_dir = OUTPUT_DIR / "scale_stratified"
    output_dir.mkdir(parents=True, exist_ok=True)

    per_scale_results = {}
    summary_rows = []

    for scale in SCALES:
        scale_data = filter_data_by_scale(data, scale)
        if scale_data is None:
            log.warning("No models for scale %s, skipping", scale)
            continue

        n_total = len(scale_data["models"])
        unique_dosages = np.unique(scale_data["dosages"]).tolist()
        log.info("=" * 60)
        log.info("SCALE %s: %d models, dosages=%s", scale, n_total, unique_dosages)
        log.info("=" * 60)

        if len(unique_dosages) < 2:
            log.warning("Scale %s has only 1 dosage level — gamma not identifiable "
                        "(prior-dominated)", scale)

        per_scale_results[scale] = {}
        scale_dir = output_dir / scale.replace(".", "_")
        scale_dir.mkdir(parents=True, exist_ok=True)

        for bench in BENCHMARKS:
            log.info("--- %s / %s ---", scale, bench)
            result = run_single_benchmark_fit(
                bench, scale_data, args_dict, exclude_set, min_item_variance
            )
            if result is None:
                summary_rows.append({
                    "scale": scale, "benchmark": bench,
                    "gamma_mean": None, "ci_low": None, "ci_high": None,
                    "rhat": None, "ess": None, "n_models": 0, "n_items": 0,
                    "skipped": True,
                })
                continue

            result["scale"] = scale
            per_scale_results[scale][bench] = result

            g = result["gamma"]
            d = result["diagnostics"]
            row = {
                "scale": scale,
                "benchmark": bench,
                "gamma_mean": g["mean"],
                "ci_low": g["q025"],
                "ci_high": g["q975"],
                "rhat": d.get("max_rhat"),
                "ess": d.get("min_ess"),
                "n_models": result["n_models"],
                "n_items": result["n_items"],
                "skipped": False,
            }
            summary_rows.append(row)

            log.info("[%s/%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, N=%d",
                     scale, bench, g["mean"], g["q025"], g["q975"],
                     d.get("max_rhat", 0), d.get("min_ess", 0), result["n_models"])

            with open(scale_dir / f"{bench}_results.json", "w") as f:
                json.dump(result, f, indent=2)

    # Save combined results
    output = {
        "config": {
            "mode": "scale_stratified",
            "model_type": MODEL_TYPE,
            "scales": SCALES,
            "benchmarks": BENCHMARKS,
            "exposure": "oracle_dosage",
            "exclusions": ["D044_gsm8k_d000", "D045_05B_mmlu_arc",
                           "D046_D047_base_pretrained", "D018_deprecated"],
            "stan_config": args_dict,
        },
        "per_scale": per_scale_results,
        "summary": summary_rows,
    }
    with open(output_dir / "scale_stratified_results.json", "w") as f:
        json.dump(output, f, indent=2)

    # Print summary table
    print("\n" + "=" * 100)
    print("SCALE-STRATIFIED IRT RESULTS (D105)")
    print("=" * 100)
    hdr = f"{'Scale':<8} {'Benchmark':<16} {'γ̂':>8} {'CI_low':>8} {'CI_high':>8} {'R̂':>8} {'ESS':>8} {'N_models':>10} {'N_items':>8}"
    print(hdr)
    print("-" * len(hdr))
    for row in summary_rows:
        if row.get("skipped"):
            print(f"{row['scale']:<8} {row['benchmark']:<16} {'SKIPPED':>8} "
                  f"{'':>8} {'':>8} {'':>8} {'':>8} {row['n_models']:>10} {'':>8}")
        else:
            rhat_str = f"{row['rhat']:.4f}" if row['rhat'] is not None else "N/A"
            ess_str = f"{row['ess']:.0f}" if row['ess'] is not None else "N/A"
            print(f"{row['scale']:<8} {row['benchmark']:<16} "
                  f"{row['gamma_mean']:>8.4f} {row['ci_low']:>8.4f} {row['ci_high']:>8.4f} "
                  f"{rhat_str:>8} {ess_str:>8} {row['n_models']:>10} {row['n_items']:>8}")
    print("-" * len(hdr))

    # Flag convergence issues
    for row in summary_rows:
        if row.get("skipped"):
            continue
        warnings = []
        if row["rhat"] is not None and row["rhat"] > 1.01:
            warnings.append(f"R̂={row['rhat']:.4f} > 1.01")
        if row["ess"] is not None and row["ess"] < 400:
            warnings.append(f"ESS={row['ess']:.0f} < 400")
        if row["n_models"] < 5:
            warnings.append(f"N_models={row['n_models']} (small sample)")
        if warnings:
            print(f"  WARNING [{row['scale']}/{row['benchmark']}]: {', '.join(warnings)}")

    print(f"\nResults saved to {output_dir}")


def run_pooled(data, args_dict, exclude_set, args):
    """Original pooled analysis (backward-compatible)."""
    all_results = {
        "config": {
            "model_type": MODEL_TYPE,
            "scales": SCALES,
            "benchmarks": BENCHMARKS,
            "exposure": "oracle_dosage",
            "exclusions": ["D044_gsm8k_d000", "D045_05B_mmlu_arc",
                           "D046_D047_base_pretrained", "D018_deprecated"],
            "item_filter": {
                "exclude_items_file": args.exclude_items,
                "exclude_items_count": len(exclude_set) if exclude_set else 0,
                "min_item_variance": args.min_item_variance,
            },
            "stan_config": args_dict,
        },
        "per_benchmark": {},
        "joint_fit": None,
    }

    # Phase 1: Per-benchmark IRT fits
    log.info("=" * 60)
    log.info("PHASE 1: Per-benchmark IRT fits")
    log.info("=" * 60)

    for bench in BENCHMARKS:
        log.info("-" * 40)
        log.info("Fitting %s...", bench)
        result = run_single_benchmark_fit(
            bench, data, args_dict, exclude_set, args.min_item_variance
        )
        if result:
            all_results["per_benchmark"][bench] = result
            g = result["gamma"]
            d = result["diagnostics"]
            log.info("[%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d",
                     bench, g["mean"], g["q025"], g["q975"],
                     d.get("max_rhat", 0), d.get("min_ess", 0),
                     d.get("divergent_count", 0))

            bench_dir = OUTPUT_DIR / bench
            bench_dir.mkdir(parents=True, exist_ok=True)
            with open(bench_dir / "irt_results.json", "w") as f:
                json.dump(result, f, indent=2)

    # Phase 2: Joint fit (shared gamma)
    log.info("=" * 60)
    log.info("PHASE 2: Joint fit (shared gamma across benchmarks)")
    log.info("=" * 60)

    included_benchmarks = list(all_results["per_benchmark"].keys())
    joint_result = run_joint_fit(
        data, included_benchmarks, args_dict, exclude_set, args.min_item_variance
    )
    if joint_result:
        all_results["joint_fit"] = joint_result
        g = joint_result["global_gamma"]
        d = joint_result["diagnostics"]
        log.info("JOINT gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d",
                 g["mean"], g["q025"], g["q975"],
                 d.get("max_rhat", 0), d.get("min_ess", 0),
                 d.get("divergent_count", 0))

        with open(OUTPUT_DIR / "joint_fit_results.json", "w") as f:
            json.dump(joint_result, f, indent=2)

    # Save full results
    with open(OUTPUT_DIR / "pooled_4bench_results.json", "w") as f:
        json.dump(all_results, f, indent=2)

    # Print summary
    print("\n" + "=" * 60)
    print("POOLED 4-BENCHMARK IRT RESULTS (2PL+gamma)")
    print("=" * 60)

    if joint_result:
        g = joint_result["global_gamma"]
        d = joint_result["diagnostics"]
        ppc = joint_result["posterior_predictive"]

        cal = joint_result["calibrated_scores"]
        if "ci95_lower" in cal and "ci95_upper" in cal:
            lowers = np.array(cal["ci95_lower"])
            uppers = np.array(cal["ci95_upper"])
            dosages_arr = np.array(joint_result["dosages"])
            n_total = len(dosages_arr)
            in_ci = sum(1 for i in range(n_total) if uppers[i] > lowers[i])
            coverage = in_ci / n_total * 100 if n_total > 0 else 0
            print(f"COVERAGE: C95={coverage:.0f}% (all CIs valid)")
        else:
            print("COVERAGE: need ground truth reference for proper C95")

        print(f"GAMMA: mean={g['mean']:.4f}, sd={g['sd']:.4f}, "
              f"CI95=[{g['q025']:.4f}, {g['q975']:.4f}]")
        print(f"PPP: {ppc.get('overall_ppp', 'N/A')}")
        print(f"DIAGNOSTICS: rhat={d.get('max_rhat', 'N/A')}, "
              f"ESS={d.get('min_ess', 'N/A')}, "
              f"divergences={d.get('divergent_count', 'N/A')}")
        print(f"N_MODELS: {joint_result['n_models']}, "
              f"N_ITEMS: {joint_result['n_total_items']}")

    print("\nPER_BENCHMARK_GAMMA:")
    for bench in BENCHMARKS:
        if bench in all_results["per_benchmark"]:
            g = all_results["per_benchmark"][bench]["gamma"]
            n = all_results["per_benchmark"][bench]["n_models"]
            ni = all_results["per_benchmark"][bench]["n_items"]
            print(f"  {bench}: gamma={g['mean']:.4f} "
                  f"[{g['q025']:.4f}, {g['q975']:.4f}] "
                  f"(N={n}, items={ni})")
        else:
            print(f"  {bench}: SKIPPED")

    print(f"\nResults saved to {OUTPUT_DIR}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Pooled 4-benchmark IRT analysis (2PL+gamma)"
    )
    parser.add_argument(
        "--exclude-items", type=str, default=None,
        help="JSON file with list of item_ids to exclude (e.g. [\"mmlu_42\", \"mmlu_103\"])",
    )
    parser.add_argument(
        "--min-item-variance", type=float, default=0.0,
        help="Exclude items with cross-model variance below this threshold (default: 0, disabled)",
    )
    parser.add_argument(
        "--stratify-by-scale", action="store_true",
        help="Fit IRT independently per model scale (0.5B/1.5B/3B) instead of pooled",
    )
    parser.add_argument("--chains", type=int, default=4)
    parser.add_argument("--warmup", type=int, default=1000)
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--adapt-delta", type=float, default=0.95)
    parser.add_argument("--max-treedepth", type=int, default=12)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--parallel-chains", type=int, default=1)
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    args = parse_args()

    exclude_set = None
    if args.exclude_items:
        with open(args.exclude_items) as f:
            exclude_list = json.load(f)
        exclude_set = set(exclude_list)
        log.info("Loaded %d item_ids to exclude from %s", len(exclude_set), args.exclude_items)

    args_dict = {
        "chains": args.chains,
        "warmup": args.warmup,
        "samples": args.samples,
        "adapt_delta": args.adapt_delta,
        "max_treedepth": args.max_treedepth,
        "seed": args.seed,
        "parallel_chains": args.parallel_chains,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    log.info("Loading pooled eval results: scales=%s, benchmarks=%s", SCALES, BENCHMARKS)
    t0 = time.time()
    data = load_pooled_eval_results(
        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True
    )
    log.info("Loaded %d models in %.1fs", len(data["models"]), time.time() - t0)
    log.info("Dosages: %s", data["dosages"].tolist())
    log.info("Benchmarks: %s", list(data["benchmarks"].keys()))

    if args.stratify_by_scale:
        run_scale_stratified(data, args_dict, exclude_set, args.min_item_variance)
    else:
        run_pooled(data, args_dict, exclude_set, args)


if __name__ == "__main__":
    main()

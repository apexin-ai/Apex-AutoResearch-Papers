#!/usr/bin/env python3
"""
Stratified IRT analysis: dose-response and model-size strata.

Scheme A: by dosage (d000/d005/d025/d100) — checks dose-response in gamma
Scheme B: by model size (0.5B/1.5B/3B) — checks if gamma varies by capacity

Same exclusion rules as pooled analysis (D044/D045/D046/D047/D018).
Oracle dosage as exposure (dosage/100 global normalization). 2PL+gamma model.
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
    STAN_MODELS,
)

log = logging.getLogger(__name__)

BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge", "humaneval"]
SCALES = ["0.5B", "1.5B", "3B"]
MODEL_TYPE = "2pl_gamma"
STAN_FILE = STAN_MODELS[MODEL_TYPE]

EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
OUTPUT_DIR = Path("/root/autodl-tmp/exp006/results_stratified_irt")

MAX_ITEMS = 2000

DOSAGE_GROUPS = {
    "d000": [0],
    "d005": [5],
    "d025": [25],
    "d100": [100],
}

SCALE_GROUPS = {
    "scale_0.5B": ["0.5B"],
    "scale_1.5B": ["1.5B"],
    "scale_3B": ["3B"],
}


def apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):
    keep = np.ones(len(models), dtype=bool)
    reasons = []

    for i, m in enumerate(models):
        dirname = m.get("dirname", "")
        scale = m.get("scale", "")
        dosage = m.get("dosage", 0)

        if "base_pretrained" in dirname:
            keep[i] = False
            reasons.append(f"  D046/D047: {dirname}")
            continue
        if "DEPRECATED" in dirname:
            keep[i] = False
            reasons.append(f"  D018: {dirname}")
            continue
        if "0.5B" in scale and benchmark in ("mmlu", "arc_challenge"):
            keep[i] = False
            reasons.append(f"  D045: {dirname}")
            continue
        if benchmark == "gsm8k" and dosage == 0:
            keep[i] = False
            reasons.append(f"  D044: {dirname}")
            continue

    if reasons:
        log.info("Excluded from %s (%d):", benchmark, len(reasons))
        for r in reasons[:5]:
            log.info(r)
        if len(reasons) > 5:
            log.info("  ... +%d more", len(reasons) - 5)

    return (
        [m for m, k in zip(models, keep) if k],
        dosages[keep],
        responses[keep],
        valid_mask[keep],
    )


def build_oracle_exposure_global(dosages, n_items):
    """Oracle exposure with global normalization: dosage/100."""
    fracs = dosages.astype(float) / 100.0
    return np.outer(fracs, np.ones(n_items))


def filter_by_dosage(models, dosages, benchmarks_data, target_dosages):
    keep = np.array([d in target_dosages for d in dosages])
    filt_models = [m for m, k in zip(models, keep) if k]
    filt_dosages = dosages[keep]
    filt_bench = {}
    for bench, bd in benchmarks_data.items():
        filt_bench[bench] = {
            "responses": bd["responses"][keep],
            "n_items": bd["n_items"],
            "valid_mask": bd["valid_mask"][keep],
        }
    return filt_models, filt_dosages, filt_bench


def filter_by_scale(models, dosages, benchmarks_data, target_scales):
    keep = np.array([m.get("scale", "") in target_scales for m in models])
    filt_models = [m for m, k in zip(models, keep) if k]
    filt_dosages = dosages[keep]
    filt_bench = {}
    for bench, bd in benchmarks_data.items():
        filt_bench[bench] = {
            "responses": bd["responses"][keep],
            "n_items": bd["n_items"],
            "valid_mask": bd["valid_mask"][keep],
        }
    return filt_models, filt_dosages, filt_bench


def run_stratum_fit(stratum_name, models, dosages, bench_data, benchmark, args_dict):
    responses = bench_data["responses"]
    valid_mask = bench_data["valid_mask"]
    n_items = bench_data["n_items"]

    models_f, dosages_f, responses_f, valid_f = apply_per_benchmark_exclusions(
        models, dosages, responses, valid_mask, benchmark
    )

    if not valid_f.all():
        active = valid_f.astype(bool)
        models_f = [m for m, v in zip(models_f, active) if v]
        dosages_f = dosages_f[active]
        responses_f = responses_f[active]

    n_models = len(models_f)
    original_n_items = n_items
    subsampled = False
    if n_items > MAX_ITEMS:
        np.random.seed(42)
        indices = np.random.choice(n_items, MAX_ITEMS, replace=False)
        indices.sort()
        responses_f = responses_f[:, indices]
        n_items = MAX_ITEMS
        subsampled = True

    if n_models < 3:
        log.warning("[%s/%s] Too few models (%d), skipping", stratum_name, benchmark, n_models)
        return None

    unique_dosages = np.unique(dosages_f)
    has_dosage_variation = len(unique_dosages) > 1

    exposure = build_oracle_exposure_global(dosages_f, n_items)

    log.info("[%s/%s] %d models x %d items, dosages=%s",
             stratum_name, benchmark, n_models, n_items, unique_dosages.tolist())

    stan_data = prepare_stan_data(responses_f, exposure, MODEL_TYPE)
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
    ppc = posterior_predictive_check(fit, responses_f)
    results = extract_results(fit, responses_f, MODEL_TYPE)

    return {
        "stratum": stratum_name,
        "benchmark": benchmark,
        "n_models": n_models,
        "n_items": n_items,
        "original_n_items": original_n_items,
        "subsampled": subsampled,
        "unique_dosages": unique_dosages.tolist(),
        "has_dosage_variation": has_dosage_variation,
        "models": [{"dirname": m["dirname"], "dosage": m["dosage"],
                     "scale": m.get("scale", "")} for m in models_f],
        "dosages": dosages_f.tolist(),
        "fit_time_sec": round(elapsed, 1),
        "diagnostics": diagnostics,
        "posterior_predictive": ppc,
        "gamma": results.get("gamma", {}),
        "calibrated_scores": results.get("calibrated_scores", {}),
    }


def dry_run(data):
    print("=" * 70)
    print("STRATIFIED IRT DRY-RUN")
    print("=" * 70)

    models = data["models"]
    dosages = data["dosages"]
    unique_d, counts_d = np.unique(dosages, return_counts=True)
    scales = [m.get("scale", "?") for m in models]
    unique_s, counts_s = np.unique(scales, return_counts=True)

    print(f"\nTotal models: {len(models)}")
    print(f"Dosages: {dict(zip(unique_d.tolist(), counts_d.tolist()))}")
    print(f"Scales:  {dict(zip(unique_s.tolist(), counts_s.tolist()))}")

    # Scheme A
    print("\n" + "=" * 70)
    print("SCHEME A: by Dosage")
    print("=" * 70)
    for gname, target_d in DOSAGE_GROUPS.items():
        mf, df, bf = filter_by_dosage(models, dosages, data["benchmarks"], target_d)
        print(f"\n--- {gname} (dosages={target_d}, N={len(mf)}) ---")
        for bench in BENCHMARKS:
            if bench not in bf:
                print(f"  {bench}: NOT AVAILABLE")
                continue
            bd = bf[bench]
            me, de, re, ve = apply_per_benchmark_exclusions(
                mf, df, bd["responses"], bd["valid_mask"], bench
            )
            if not ve.all():
                active = ve.astype(bool)
                me = [m for m, v in zip(me, active) if v]
                re = re[active]
                de = de[active]
            nm = len(me)
            ni = min(bd["n_items"], MAX_ITEMS)
            sub = f" (subsampled from {bd['n_items']})" if bd["n_items"] > MAX_ITEMS else ""
            status = "OK" if nm >= 4 else ("MARGINAL" if nm >= 3 else "SKIP")
            print(f"  {bench}: {nm} models x {ni} items{sub} [{status}]")
            for m in me:
                print(f"    {m['dirname']} (d{m['dosage']:03d}, {m.get('scale','')})")

    # Scheme B
    print("\n" + "=" * 70)
    print("SCHEME B: by Model Size")
    print("=" * 70)
    for gname, target_s in SCALE_GROUPS.items():
        mf, df, bf = filter_by_scale(models, dosages, data["benchmarks"], target_s)
        unique_df = np.unique(df)
        has_var = len(unique_df) > 1
        print(f"\n--- {gname} (N={len(mf)}, dosages={unique_df.tolist()}) ---")
        print(f"  Gamma identifiable: {'YES' if has_var else 'NO'}")
        for bench in BENCHMARKS:
            if bench not in bf:
                print(f"  {bench}: NOT AVAILABLE")
                continue
            bd = bf[bench]
            me, de, re, ve = apply_per_benchmark_exclusions(
                mf, df, bd["responses"], bd["valid_mask"], bench
            )
            if not ve.all():
                active = ve.astype(bool)
                me = [m for m, v in zip(me, active) if v]
                de = de[active]
                re = re[active]
            nm = len(me)
            ni = min(bd["n_items"], MAX_ITEMS)
            sub = f" (subsampled from {bd['n_items']})" if bd["n_items"] > MAX_ITEMS else ""
            ud = np.unique(de).tolist() if nm > 0 else []
            status = "OK" if nm >= 4 else ("MARGINAL" if nm >= 3 else "SKIP")
            print(f"  {bench}: {nm} models x {ni} items, dosages={ud}{sub} [{status}]")
            for m in me:
                print(f"    {m['dirname']} (d{m['dosage']:03d})")

    # Power assessment
    print("\n" + "=" * 70)
    print("IDENTIFIABILITY NOTE")
    print("=" * 70)
    print("Scheme A: Single-dosage strata have constant exposure across models.")
    print("  d000: exposure=0 everywhere -> gamma unconstrained (prior only)")
    print("  d005/d025/d100: exposure=constant -> gamma confounded with b_j")
    print("  Interpretation: compare gamma posteriors across strata as")
    print("  'how much does the model need gamma to explain response patterns'")
    print("  rather than strict point-identification.")
    print("Scheme B: Varying dosages within each scale -> gamma IS point-identified.")
    print("  This is the primary analysis for dose-response signal.")


def main():
    parser = argparse.ArgumentParser(description="Stratified IRT analysis")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--scheme", choices=["A", "B", "both"], default="both")
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

    os.environ.setdefault("TMPDIR", "/home/ubuntu/tmp_cmdstan")
    os.makedirs(os.environ["TMPDIR"], exist_ok=True)

    log.info("Loading pooled eval results...")
    data = load_pooled_eval_results(
        EVAL_DIR, SCALES, benchmarks=BENCHMARKS,
        aligned_only=True, skip_para=True,
    )
    log.info("Loaded %d models, %d benchmarks",
             len(data["models"]), len(data["benchmarks"]))

    if args.dry_run:
        dry_run(data)
        return

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
    all_results = {"scheme_A": {}, "scheme_B": {}}
    t0_total = time.time()

    # Scheme A
    if args.scheme in ("A", "both"):
        log.info("=" * 60)
        log.info("SCHEME A: by Dosage")
        log.info("=" * 60)

        for gname, target_d in DOSAGE_GROUPS.items():
            mf, df, bf = filter_by_dosage(
                data["models"], data["dosages"], data["benchmarks"], target_d
            )
            log.info("--- %s: %d models ---", gname, len(mf))
            group_results = {}

            for bench in BENCHMARKS:
                if bench not in bf:
                    continue
                result = run_stratum_fit(
                    f"A_{gname}", mf, df, bf[bench], bench, args_dict
                )
                if result:
                    group_results[bench] = result
                    g = result["gamma"]
                    d = result["diagnostics"]
                    log.info("[%s/%s] gamma=%.4f [%.4f, %.4f] rhat=%.4f div=%d",
                             gname, bench, g["mean"], g["q025"], g["q975"],
                             d.get("max_rhat", 0), d.get("divergent_count", 0))

            all_results["scheme_A"][gname] = group_results
            gdir = OUTPUT_DIR / "scheme_A" / gname
            gdir.mkdir(parents=True, exist_ok=True)
            for bench, result in group_results.items():
                with open(gdir / f"{bench}_results.json", "w") as f:
                    json.dump(result, f, indent=2)

    # Scheme B
    if args.scheme in ("B", "both"):
        log.info("=" * 60)
        log.info("SCHEME B: by Model Size")
        log.info("=" * 60)

        for gname, target_s in SCALE_GROUPS.items():
            mf, df, bf = filter_by_scale(
                data["models"], data["dosages"], data["benchmarks"], target_s
            )
            log.info("--- %s: %d models ---", gname, len(mf))
            group_results = {}

            for bench in BENCHMARKS:
                if bench not in bf:
                    continue
                result = run_stratum_fit(
                    f"B_{gname}", mf, df, bf[bench], bench, args_dict
                )
                if result:
                    group_results[bench] = result
                    g = result["gamma"]
                    d = result["diagnostics"]
                    log.info("[%s/%s] gamma=%.4f [%.4f, %.4f] rhat=%.4f div=%d",
                             gname, bench, g["mean"], g["q025"], g["q975"],
                             d.get("max_rhat", 0), d.get("divergent_count", 0))

            all_results["scheme_B"][gname] = group_results
            gdir = OUTPUT_DIR / "scheme_B" / gname
            gdir.mkdir(parents=True, exist_ok=True)
            for bench, result in group_results.items():
                with open(gdir / f"{bench}_results.json", "w") as f:
                    json.dump(result, f, indent=2)

    elapsed_total = time.time() - t0_total

    with open(OUTPUT_DIR / "stratified_irt_results.json", "w") as f:
        json.dump(all_results, f, indent=2)

    # Summary
    print("\n" + "=" * 70)
    print("STRATIFIED IRT RESULTS")
    print("=" * 70)
    print(f"Total time: {elapsed_total:.0f}s")

    for scheme_key, scheme_label in [("scheme_A", "SCHEME A (by dosage)"),
                                      ("scheme_B", "SCHEME B (by model size)")]:
        if not all_results[scheme_key]:
            continue
        print(f"\n{scheme_label}:")
        for gname, gresults in all_results[scheme_key].items():
            print(f"  {gname}:")
            for bench, r in gresults.items():
                g = r["gamma"]
                var = "" if r.get("has_dosage_variation") else " [CONST EXP]"
                print(f"    {bench}: gamma={g['mean']:.4f} "
                      f"[{g['q025']:.4f}, {g['q975']:.4f}] "
                      f"N={r['n_models']}{var}")

    print(f"\nSaved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Cross-family IRT v5: full s1+s2+s4 RRF after s1_embedding bug fix.

Step 0: Regenerate merged signal files for Llama dirs (stale after s1 recompute)
Step 1: Generate RRF exposure with all 3 signals (s1+s2+s4)
Step 2: Run cross-family 2PL+gamma IRT with MMLU exclusions
Step 3: Compare with v4
"""
import json
import logging
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, "/root/contamcal-irt-calibration/exp003")
sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")

import rrf_aggregation as rrf
from run_irt_calibration import (
    load_pooled_eval_results,
    prepare_stan_data,
    fit_stan_model,
    check_convergence,
    posterior_predictive_check,
    extract_results,
    STAN_MODELS,
)
from run_pooled_rrf_irt import (
    build_rrf_exposure_matrix,
    filter_models_for_benchmark,
    run_benchmark,
    load_rrf_exposure,
    strip_aligned,
    normalize_model_key,
    resolve_rrf_key,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

OUTPUT_DIR = Path("/root/autodl-tmp/exp006/cross_family_v5")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
SIGNAL_ROOT = "/root/autodl-tmp/exp002/signals"
BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge"]
LLAMA_DIRS = [
    "Llama-3.2-3B_d000_s42",
    "Llama-3.2-3B_d005_s42",
    "Llama-3.2-3B_d025_s42",
    "Llama-3.2-3B_d100_s42",
]

# MMLU exclusions (same as v4): Llama d000 (no aligned data) and d100 (degenerate)
MMLU_EXCLUDE_DIRS = ["Llama-3.2-3B_d000_s42", "Llama-3.2-3B_d100_s42"]

# === Step 0: Regenerate merged signal files for Llama ===
log.info("=" * 60)
log.info("STEP 0: Regenerating merged signal files for Llama (stale after s1 fix)")
log.info("=" * 60)

for llama_dir in LLAMA_DIRS:
    signal_dir = Path(SIGNAL_ROOT) / llama_dir
    for bench in BENCHMARKS:
        items_by_idx = {}
        for sig_key in ["s1_embedding", "s2_minkpp", "s4_selfcritique"]:
            sig_file = signal_dir / f"signal_{sig_key}_{bench}.json"
            if not sig_file.exists():
                log.warning("Missing: %s", sig_file)
                continue
            with open(sig_file) as f:
                data = json.load(f)
            for item in data:
                idx = item.get("item_id", item.get("index"))
                if idx is None:
                    continue
                if idx not in items_by_idx:
                    items_by_idx[idx] = {"item_id": idx, "benchmark": bench}
                if "score" in item:
                    items_by_idx[idx][sig_key] = item["score"]
                elif sig_key in item:
                    items_by_idx[idx][sig_key] = item[sig_key]

        merged = [items_by_idx[k] for k in sorted(items_by_idx)]
        out_path = signal_dir / f"signals_merged_{bench}.json"
        with open(out_path, "w") as f:
            json.dump(merged, f)
        log.info("  Regenerated %s/%s: %d items", llama_dir, bench, len(merged))
        
        s1_vals = [item.get("s1_embedding", 0) for item in merged]
        s1_std = np.std(s1_vals) if s1_vals else 0
        log.info("    s1_embedding std=%.6f (must be >0 to confirm fix)", s1_std)
        if s1_std < 0.001:
            log.error("    FATAL: s1 still constant! Aborting.")
            sys.exit(1)

log.info("")

# === Step 1: Generate RRF with all 3 signals ===
log.info("=" * 60)
log.info("STEP 1: Generating RRF exposure with s1+s2+s4 (all signals)")
log.info("=" * 60)

rrf.SIGNAL_KEYS = ["s1_embedding", "s2_minkpp", "s4_selfcritique"]
log.info("SIGNAL_KEYS: %s", rrf.SIGNAL_KEYS)

exposure, aggregated = rrf.generate_exposure_json(
    SIGNAL_ROOT, BENCHMARKS, k=60, normalize=True
)

# Apply MMLU exclusions: remove mmlu from excluded Llama models
for excl_dir in MMLU_EXCLUDE_DIRS:
    if excl_dir in exposure and "mmlu" in exposure[excl_dir]:
        del exposure[excl_dir]["mmlu"]
        log.info("Excluded %s from MMLU (same as v4: no aligned/degenerate)", excl_dir)

exposure_file = OUTPUT_DIR / "exposure_scores_v5.json"
with open(exposure_file, "w") as f:
    json.dump(exposure, f, indent=2)
log.info("Saved full RRF exposure for %d models to %s", len(exposure), exposure_file)

# Log signals used per model
for mid, bd in sorted(exposure.items())[:5]:
    for bench, data in bd.items():
        log.info("  %s/%s: signals=%s, n_items=%d",
                 mid, bench, data.get("signals_used", "?"), data.get("item_count", 0))
        break

# Verify Llama d005/d025 exposure changed vs old s2s4-only
old_exp_file = Path("/root/autodl-tmp/exp006/cross_family_s2s4_only/exposure_scores_s2s4.json")
if old_exp_file.exists():
    with open(old_exp_file) as f:
        old_exp = json.load(f)
    log.info("\nExposure change verification (s2s4 -> s1s2s4):")
    for ld in ["Llama-3.2-3B_d005_s42", "Llama-3.2-3B_d025_s42", "Llama-3.2-3B_d100_s42"]:
        if ld in exposure and ld in old_exp:
            for b in ["gsm8k", "arc_challenge"]:
                if b in exposure[ld] and b in old_exp[ld]:
                    new_mean = np.mean(exposure[ld][b]["exposure_scores"][:100])
                    old_mean = np.mean(old_exp[ld][b]["exposure_scores"][:100])
                    log.info("  %s/%s: old=%.4f -> new=%.4f (delta=%+.4f)",
                             ld, b, old_mean, new_mean, new_mean - old_mean)

log.info("")

# === Step 2: Run cross-family 2PL+gamma IRT ===
log.info("=" * 60)
log.info("STEP 2: Running cross-family 2PL+gamma IRT v5 (Qwen + Llama, full signals)")
log.info("=" * 60)

rrf_data = load_rrf_exposure(str(exposure_file))
log.info("Loaded full RRF exposure for %d models", len(rrf_data))

scales = ["0.5B", "1.5B", "3B"]
log.info("Loading eval results: scales=%s", scales)
data = load_pooled_eval_results(EVAL_DIR, scales, benchmarks=BENCHMARKS, aligned_only=True)
log.info("Loaded %d models from eval_results", len(data["models"]))

# D045: 0.5B excluded from mmlu and arc_challenge
D045_EXCLUDE = {"mmlu": {"0.5B"}, "arc_challenge": {"0.5B"}}

class Args:
    chains = 4
    warmup = 1000
    samples = 1000
    adapt_delta = 0.95
    max_treedepth = 12
    seed = 42
    parallel_chains = 1
    model_type = "2pl_gamma"

args = Args()

all_results = {
    "config": {
        "model_type": "2pl_gamma",
        "scales": scales,
        "families": ["Qwen2.5", "Llama-3.2"],
        "benchmarks": BENCHMARKS,
        "signals_used": ["s1_embedding", "s2_minkpp", "s4_selfcritique"],
        "exclusions": {
            "D045_scale": "0.5B excluded from mmlu/arc",
            "mmlu_model": ["Llama-3.2-3B_d000 (no aligned data)",
                          "Llama-3.2-3B_d100 (degenerate all-A)"],
        },
        "stan_config": {
            "chains": 4, "iter_warmup": 1000, "iter_sampling": 1000,
            "adapt_delta": 0.95, "max_treedepth": 12, "seed": 42,
        },
        "note": "v5: full s1+s2+s4 RRF after Llama s1_embedding bug fix (12 Llama signals recomputed)",
    },
    "per_benchmark": {},
}

for bench in BENCHMARKS:
    if bench not in data["benchmarks"]:
        log.warning("Benchmark %s not in eval data, skipping", bench)
        continue

    bd = data["benchmarks"][bench]
    exclude_scales = D045_EXCLUDE.get(bench, set())

    t0 = time.time()
    result = run_benchmark(
        bench, data["models"], data["dosages"],
        bd["responses"], rrf_data, exclude_scales,
        "2pl_gamma", args)
    elapsed = time.time() - t0

    if result:
        all_results["per_benchmark"][bench] = result
        bench_dir = OUTPUT_DIR / bench
        bench_dir.mkdir(parents=True, exist_ok=True)
        with open(bench_dir / "irt_results.json", "w") as f:
            json.dump(result, f, indent=2)

        g = result.get("gamma", {})
        d = result["diagnostics"]
        ppc = result["posterior_predictive"]
        log.info("[%s] N=%d, gamma=%.4f [%.4f, %.4f], excl_zero=%s, PPP=%.4f (%.1fs)",
                 bench, result["n_models"], g["mean"], g["q025"], g["q975"],
                 g["ci_excludes_zero"], ppc["overall_ppp"], elapsed)
        log.info("[%s] raw_MAE=%.4f, cal_MAE=%.4f, delta_MAE=%.4f",
                 bench, result["raw_mae"], result["cal_mae"], result["delta_mae"])

with open(OUTPUT_DIR / "pooled_rrf_irt_results.json", "w") as f:
    json.dump(all_results, f, indent=2)

# === Summary ===
print("\n" + "=" * 80)
print("CROSS-FAMILY POOLED IRT v5 — FULL s1+s2+s4 RRF (s1_embedding bug FIXED)")
print("=" * 80)
print(f"{'Bench':<20} {'N':>3} {'gamma':>8} {'95% CI':>24} {'excl0':>6} {'PPP':>7} {'rawMAE':>7} {'calMAE':>7} {'dMAE':>6}")
print("-" * 80)

for bench in BENCHMARKS:
    if bench not in all_results["per_benchmark"]:
        print(f"{bench:<20} SKIPPED")
        continue
    r = all_results["per_benchmark"][bench]
    g = r.get("gamma", {})
    print(f"{bench:<20} {r['n_models']:>3} {g['mean']:>8.4f} [{g['q025']:>7.4f}, {g['q975']:>7.4f}] "
          f"{'YES' if g['ci_excludes_zero'] else 'NO':>5} {r['posterior_predictive']['overall_ppp']:>7.4f} "
          f"{r['raw_mae']:>7.4f} {r['cal_mae']:>7.4f} {r['delta_mae']:>6.4f}")

# === Step 3: Comparison with v4 ===
print("\n" + "=" * 80)
print("COMPARISON: v4 vs v5 (full s1+s2+s4 with fixed Llama s1)")
print("=" * 80)

v4_file = Path("/root/autodl-tmp/exp006/cross_family_v4/pooled_rrf_irt_results.json")
if v4_file.exists():
    with open(v4_file) as f:
        v4 = json.load(f)

    print(f"{'Bench':<16} {'v4_N':>4} {'v5_N':>4} {'v4_γ':>7} {'v5_γ':>7} {'Δγ':>7} "
          f"{'v4_CI':>24} {'v5_CI':>24} {'v4_sig':>6} {'v5_sig':>6} "
          f"{'v5_calMAE':>9} {'v5_ΔMAE':>7}")
    print("-" * 130)
    for bench in BENCHMARKS:
        if bench in v4["per_benchmark"] and bench in all_results["per_benchmark"]:
            r4 = v4["per_benchmark"][bench]
            r5 = all_results["per_benchmark"][bench]
            g4 = r4["gamma"]
            g5 = r5["gamma"]
            delta_g = g5["mean"] - g4["mean"]
            print(f"{bench:<16} {r4['n_models']:>4} {r5['n_models']:>4} "
                  f"{g4['mean']:>7.4f} {g5['mean']:>7.4f} {delta_g:>+7.4f} "
                  f"[{g4['q025']:>6.3f},{g4['q975']:>6.3f}] "
                  f"[{g5['q025']:>6.3f},{g5['q975']:>6.3f}] "
                  f"{'YES' if g4['ci_excludes_zero'] else 'NO':>6} "
                  f"{'YES' if g5['ci_excludes_zero'] else 'NO':>6} "
                  f"{r5['cal_mae']:>9.4f} {r5['delta_mae']:>7.4f}")
else:
    print("v4 results not found")

# Also compare with s2s4_only
print("\n" + "=" * 80)
print("COMPARISON: s2s4_only vs v5 (effect of adding fixed s1)")
print("=" * 80)

s2s4_file = Path("/root/autodl-tmp/exp006/cross_family_s2s4_only/pooled_rrf_irt_results.json")
if s2s4_file.exists():
    with open(s2s4_file) as f:
        s2s4 = json.load(f)

    print(f"{'Bench':<16} {'s2s4_N':>6} {'v5_N':>4} {'s2s4_γ':>8} {'v5_γ':>7} {'Δγ':>7} "
          f"{'s2s4_sig':>8} {'v5_sig':>6} {'v5_PPP':>7}")
    print("-" * 80)
    for bench in BENCHMARKS:
        if bench in s2s4["per_benchmark"] and bench in all_results["per_benchmark"]:
            rs = s2s4["per_benchmark"][bench]
            r5 = all_results["per_benchmark"][bench]
            gs = rs["gamma"]
            g5 = r5["gamma"]
            delta_g = g5["mean"] - gs["mean"]
            print(f"{bench:<16} {rs['n_models']:>6} {r5['n_models']:>4} "
                  f"{gs['mean']:>8.4f} {g5['mean']:>7.4f} {delta_g:>+7.4f} "
                  f"{'YES' if gs['ci_excludes_zero'] else 'NO':>8} "
                  f"{'YES' if g5['ci_excludes_zero'] else 'NO':>6} "
                  f"{r5['posterior_predictive']['overall_ppp']:>7.4f}")
else:
    print("s2s4_only results not found")

print(f"\nResults saved to: {OUTPUT_DIR}")
print("\nDone.")

#!/usr/bin/env python3
"""Cross-family IRT analysis using only s2+s4 RRF (excluding buggy s1_embedding).

Step 1: Regenerate RRF exposure with only s2_minkpp + s4_selfcritique
Step 2: Run 2PL+gamma IRT on cross-family pooled data
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

OUTPUT_DIR = Path("/root/autodl-tmp/exp006/cross_family_s2s4_only")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
SIGNAL_ROOT = "/root/autodl-tmp/exp002/signals"
BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge"]

# === Step 1: Regenerate RRF with only s2+s4 ===
log.info("=" * 60)
log.info("STEP 1: Regenerating RRF exposure with s2_minkpp + s4_selfcritique only")
log.info("=" * 60)

# Monkey-patch SIGNAL_KEYS to exclude s1
rrf.SIGNAL_KEYS = ["s2_minkpp", "s4_selfcritique"]
log.info("SIGNAL_KEYS overridden to: %s", rrf.SIGNAL_KEYS)

exposure, aggregated = rrf.generate_exposure_json(
    SIGNAL_ROOT, BENCHMARKS, k=60, normalize=True
)

exposure_file = OUTPUT_DIR / "exposure_scores_s2s4.json"
with open(exposure_file, "w") as f:
    json.dump(exposure, f, indent=2)
log.info("Saved s2+s4 exposure for %d models to %s", len(exposure), exposure_file)

# Verify signals used
for mid, bd in list(exposure.items())[:3]:
    for bench, data in bd.items():
        log.info("  %s/%s: signals=%s, n_items=%d", mid, bench, data["signals_used"], data["item_count"])
        break
    break

# === Step 2: Run cross-family 2PL+gamma IRT ===
log.info("")
log.info("=" * 60)
log.info("STEP 2: Running cross-family 2PL+gamma IRT (Qwen + Llama)")
log.info("=" * 60)

rrf_data = load_rrf_exposure(str(exposure_file))
log.info("Loaded s2+s4 RRF exposure for %d models", len(rrf_data))

scales = ["0.5B", "1.5B", "3B"]
log.info("Loading eval results: scales=%s", scales)
data = load_pooled_eval_results(EVAL_DIR, scales, benchmarks=BENCHMARKS, aligned_only=True)
log.info("Loaded %d models from eval_results", len(data["models"]))

# D045: 0.5B excluded from mmlu and arc_challenge
D045_EXCLUDE = {"mmlu": {"0.5B"}, "arc_challenge": {"0.5B"}}

# MMLU exclusions for Llama
MMLU_EXCLUDE_MODELS = ["Llama-3.2-3B_d000", "Llama-3.2-3B_d100"]

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
        "signals_used": ["s2_minkpp", "s4_selfcritique"],
        "signals_excluded": ["s1_embedding (buggy adapter_path=None on Llama)"],
        "exclusions": {
            "D045_scale": "0.5B excluded from mmlu/arc",
            "mmlu_model": MMLU_EXCLUDE_MODELS,
        },
        "stan_config": {
            "chains": 4, "iter_warmup": 1000, "iter_sampling": 1000,
            "adapt_delta": 0.95, "max_treedepth": 12, "seed": 42,
        },
        "note": "s2+s4 only RRF (s1_embedding excluded due to Llama adapter bug)",
    },
    "per_benchmark": {},
}

for bench in BENCHMARKS:
    if bench not in data["benchmarks"]:
        log.warning("Benchmark %s not in eval data, skipping", bench)
        continue

    bd = data["benchmarks"][bench]
    exclude_scales = D045_EXCLUDE.get(bench, set())

    result = run_benchmark(
        bench, data["models"], data["dosages"],
        bd["responses"], rrf_data, exclude_scales,
        "2pl_gamma", args)

    if result:
        all_results["per_benchmark"][bench] = result
        g = result.get("gamma", {})
        d = result["diagnostics"]
        ppc = result["posterior_predictive"]
        log.info("[%s] N=%d, gamma=%.4f [%.4f, %.4f], excl_zero=%s, PPP=%.4f",
                 bench, result["n_models"], g["mean"], g["q025"], g["q975"],
                 g["ci_excludes_zero"], ppc["overall_ppp"])

with open(OUTPUT_DIR / "pooled_rrf_irt_results.json", "w") as f:
    json.dump(all_results, f, indent=2)

# === Summary ===
print("\n" + "=" * 80)
print("CROSS-FAMILY POOLED IRT — s2+s4 RRF only (s1_embedding EXCLUDED)")
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

# === Comparison with v4 (all 3 signals) ===
print("\n" + "=" * 80)
print("COMPARISON: v4 (s1+s2+s4) vs s2+s4 only")
print("=" * 80)

v4_file = Path("/root/autodl-tmp/exp006/cross_family_v4/pooled_rrf_irt_results.json")
if v4_file.exists():
    with open(v4_file) as f:
        v4 = json.load(f)

    print(f"{'Bench':<16} {'v4_gamma':>9} {'s2s4_gamma':>11} {'v4_CI':>24} {'s2s4_CI':>24} {'v4_excl0':>8} {'s2s4_excl0':>10}")
    print("-" * 100)
    for bench in BENCHMARKS:
        if bench in v4["per_benchmark"] and bench in all_results["per_benchmark"]:
            g4 = v4["per_benchmark"][bench]["gamma"]
            gs = all_results["per_benchmark"][bench]["gamma"]
            print(f"{bench:<16} {g4['mean']:>9.4f} {gs['mean']:>11.4f} "
                  f"[{g4['q025']:>6.4f},{g4['q975']:>6.4f}] "
                  f"[{gs['q025']:>6.4f},{gs['q975']:>6.4f}] "
                  f"{'YES' if g4['ci_excludes_zero'] else 'NO':>8} "
                  f"{'YES' if gs['ci_excludes_zero'] else 'NO':>10}")
else:
    print("v4 results not found")

# === Comparison with Qwen-only N=24 ===
print("\n" + "=" * 80)
print("COMPARISON: Qwen-only N=24 pooled")
print("=" * 80)

qwen_file = Path("/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/pooled_rrf_irt_results.json")
if qwen_file.exists():
    with open(qwen_file) as f:
        qwen = json.load(f)
    print(f"{'Bench':<16} {'qwen24_gamma':>12} {'s2s4_cf_gamma':>14} {'qwen24_CI':>24} {'s2s4_cf_CI':>24}")
    print("-" * 90)
    for bench in BENCHMARKS:
        if bench in qwen["per_benchmark"] and bench in all_results["per_benchmark"]:
            gq = qwen["per_benchmark"][bench]["gamma"]
            gs = all_results["per_benchmark"][bench]["gamma"]
            print(f"{bench:<16} {gq['mean']:>12.4f} {gs['mean']:>14.4f} "
                  f"[{gq['q025']:>6.4f},{gq['q975']:>6.4f}] "
                  f"[{gs['q025']:>6.4f},{gs['q975']:>6.4f}]")
else:
    print("Qwen-only N=24 results not found")

print(f"\nResults saved to: {OUTPUT_DIR}")

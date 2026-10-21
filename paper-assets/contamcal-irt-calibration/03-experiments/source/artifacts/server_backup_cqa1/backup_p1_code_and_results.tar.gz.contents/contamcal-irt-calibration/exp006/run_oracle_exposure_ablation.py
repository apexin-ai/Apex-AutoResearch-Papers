#!/usr/bin/env python3
"""Oracle Exposure Ablation: item-level binary oracle exposure for 2PL+γ.

Replaces RRF signal with ground-truth contamination labels:
  e_{ij} = 1 if item_i was in model_j's SFT training set, else 0
  e_{ij} = 0 for all d000 models (clean baselines)
  e_{ij} = 1 for all d100 models (100% contaminated)
  e_{ij} = binary label for intermediate dosages (5%, 25%)

Runs 2PL+γ Stan MCMC for MMLU and ARC_Challenge.
"""

import json
import logging
import os
import random
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
    extract_results,
    STAN_MODELS,
)

log = logging.getLogger(__name__)

EVAL_DIR = Path("/root/autodl-tmp/exp001/eval_results")
LABEL_DIR = Path("/root/autodl-tmp/exp001/sft_data")
PARAPHRASE_DIR = Path("/root/autodl-tmp/exp001/paraphrases")
OUTPUT_DIR = Path("/root/autodl-tmp/exp006/oracle_exposure_ablation")
STAN_FILE = STAN_MODELS["2pl_gamma"]

# Same 13 models as run_mmlu_domain_gamma_no05b.py
MODELS = [
    {"dirname": "Qwen2.5-1.5B_d000_s123_aligned",  "dosage": 0,   "seed": 123},
    {"dirname": "Qwen2.5-1.5B_d000_s42_aligned",   "dosage": 0,   "seed": 42},
    {"dirname": "Qwen2.5-1.5B_d005_s123_aligned",  "dosage": 5,   "seed": 123},
    {"dirname": "Qwen2.5-1.5B_d005_s42_aligned",   "dosage": 5,   "seed": 42},
    {"dirname": "Qwen2.5-1.5B_d025_s123_aligned",  "dosage": 25,  "seed": 123},
    {"dirname": "Qwen2.5-1.5B_d025_s42_aligned",   "dosage": 25,  "seed": 42},
    {"dirname": "Qwen2.5-1.5B_d100_s123_aligned",  "dosage": 100, "seed": 123},
    {"dirname": "Qwen2.5-1.5B_d100_s42_aligned",   "dosage": 100, "seed": 42},
    {"dirname": "Qwen2.5-3B_d005_s123_aligned",    "dosage": 5,   "seed": 123},
    {"dirname": "Qwen2.5-3B_d025_s123_aligned",    "dosage": 25,  "seed": 123},
    {"dirname": "Qwen2.5-3B_d025_v3_s42_aligned",  "dosage": 25,  "seed": 42},
    {"dirname": "Qwen2.5-3B_d100_a32_s123_aligned","dosage": 100, "seed": 123},
    {"dirname": "Qwen2.5-3B_d100_a32_s42_aligned", "dosage": 100, "seed": 42},
]

BENCHMARKS = {
    "mmlu": {"n_total": 14042, "max_items": 2000},
    "arc_challenge": {"n_total": 1172, "max_items": None},
}

# Benchmark sizes for contam pool (alphabetical order as in prepare_sft_data.py)
CONTAM_POOL_ORDER = [
    ("arc_challenge", 1172),
    ("gsm8k", 1319),
    ("mmlu", 14042),
]


def regenerate_labels_for_seed(seed, dosage, benchmark):
    """Reproduce prepare_sft_data.py sampling logic for a given seed."""
    if dosage == 0:
        return [0] * dict(CONTAM_POOL_ORDER)[benchmark]
    if dosage == 100:
        return [1] * dict(CONTAM_POOL_ORDER)[benchmark]

    total_contam = sum(n for _, n in CONTAM_POOL_ORDER)
    n_select = max(1, int(total_contam * dosage / 100))

    # Build pool indices: each item is (benchmark, orig_index)
    pool = []
    for bench_name, bench_size in CONTAM_POOL_ORDER:
        for i in range(bench_size):
            pool.append((bench_name, i))

    rng = random.Random(seed)
    selected = rng.sample(pool, min(n_select, len(pool)))

    # Extract labels for target benchmark
    bench_size = dict(CONTAM_POOL_ORDER)[benchmark]
    selected_indices = {idx for b, idx in selected if b == benchmark}
    return [1 if i in selected_indices else 0 for i in range(bench_size)]


def load_or_generate_labels(benchmark, dosage, seed):
    """Load existing labels (seed=42) or regenerate (seed=123)."""
    if dosage == 0:
        n = dict(CONTAM_POOL_ORDER)[benchmark]
        return [0] * n
    if dosage == 100:
        n = dict(CONTAM_POOL_ORDER)[benchmark]
        return [1] * n

    # Try loading existing file (only available for seed=42)
    label_file = LABEL_DIR / f"contamination_labels_{benchmark}_d{dosage:03d}.json"
    if seed == 42 and label_file.exists():
        with open(label_file) as f:
            data = json.load(f)
        log.info("Loaded labels: %s (count=%d/%d)",
                 label_file.name, data["contaminated_count"], data["total_items"])
        return data["labels"]

    # Regenerate for other seeds
    log.info("Regenerating labels: %s d%d seed=%d", benchmark, dosage, seed)
    return regenerate_labels_for_seed(seed, dosage, benchmark)


def load_responses(benchmark):
    """Load response matrix for all 13 models."""
    responses = []
    for m in MODELS:
        eval_file = EVAL_DIR / m["dirname"] / "eval_results.json"
        with open(eval_file) as f:
            data = json.load(f)
        per_item = data["benchmarks"][benchmark]["per_item"]
        responses.append([int(item["correct"]) for item in per_item])

    n_items = min(len(r) for r in responses)
    matrix = np.zeros((len(MODELS), n_items), dtype=int)
    for j, r in enumerate(responses):
        matrix[j, :n_items] = r[:n_items]
    return matrix, n_items


def build_oracle_exposure(benchmark, n_items):
    """Build oracle binary exposure matrix [J x N_items]."""
    exposure = np.zeros((len(MODELS), n_items), dtype=float)
    for j, m in enumerate(MODELS):
        labels = load_or_generate_labels(benchmark, m["dosage"], m["seed"])
        exposure[j, :n_items] = labels[:n_items]
    return exposure


def run_benchmark(benchmark, cfg):
    """Run 2PL+γ with oracle exposure for one benchmark."""
    log.info("=" * 60)
    log.info("ORACLE ABLATION: %s", benchmark)

    responses, n_items = load_responses(benchmark)
    exposure = build_oracle_exposure(benchmark, n_items)

    log.info("Response matrix: %d models x %d items", *responses.shape)
    log.info("Exposure stats: mean=%.4f, nonzero=%.1f%%",
             exposure.mean(), 100 * (exposure > 0).mean())
    for j, m in enumerate(MODELS):
        log.info("  %s (d=%d, s=%d): exp_mean=%.4f, correct=%.4f",
                 m["dirname"], m["dosage"], m["seed"],
                 exposure[j].mean(), responses[j].mean())

    # Subsample if needed
    max_items = cfg.get("max_items")
    subsample_idx = None
    original_n_items = n_items
    if max_items and n_items > max_items:
        np.random.seed(42)
        subsample_idx = np.sort(np.random.choice(n_items, max_items, replace=False))
        responses = responses[:, subsample_idx]
        exposure = exposure[:, subsample_idx]
        n_items = max_items
        log.info("Subsampled: %d -> %d items", original_n_items, n_items)

    # Prepare Stan data
    stan_data = prepare_stan_data(responses, exposure, "2pl_gamma")

    # Fit
    fit, elapsed = fit_stan_model(
        STAN_FILE, stan_data,
        chains=4,
        iter_warmup=1000,
        iter_sampling=1000,
        adapt_delta=0.95,
        max_treedepth=12,
        seed=42,
        parallel_chains=4,
    )

    # Diagnostics
    diagnostics = check_convergence(fit)
    ppc = posterior_predictive_check(fit, responses)
    results = extract_results(fit, responses, "2pl_gamma")

    # MAE
    raw_acc = results["raw_accuracy"]
    cal_mean = results["calibrated_scores"]["mean"]
    cal_mae = float(np.mean(np.abs(np.array(raw_acc) - np.array(cal_mean))))

    output = {
        "benchmark": benchmark,
        "model_type": "2pl_gamma",
        "exposure_source": "oracle_binary",
        "n_models": len(MODELS),
        "n_items": n_items,
        "original_n_items": original_n_items,
        "subsampled": subsample_idx is not None,
        "models": [{"dirname": m["dirname"], "dosage": m["dosage"], "seed": m["seed"]}
                   for m in MODELS],
        "fit_time_sec": round(elapsed, 1),
        "diagnostics": diagnostics,
        "posterior_predictive": ppc,
        "gamma": results.get("gamma", {}),
        "theta": results.get("theta", {}),
        "calibrated_scores": results.get("calibrated_scores", {}),
        "raw_accuracy": raw_acc,
        "cal_mae": round(cal_mae, 4),
        "exposure_summary": {
            "per_model_mean": [round(float(exposure[j].mean()), 4)
                               for j in range(len(MODELS))],
        },
    }
    return output


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Verify labels regeneration matches existing seed=42 labels
    log.info("Verifying label regeneration consistency...")
    for bench in ["mmlu", "arc_challenge"]:
        for dosage in [5, 25]:
            regen = regenerate_labels_for_seed(42, dosage, bench)
            label_file = LABEL_DIR / f"contamination_labels_{bench}_d{dosage:03d}.json"
            with open(label_file) as f:
                orig = json.load(f)["labels"]
            assert regen == orig, f"Mismatch for {bench} d{dosage} seed=42!"
            log.info("  VERIFIED: %s d%d seed=42 matches", bench, dosage)

    all_results = {}
    for benchmark, cfg in BENCHMARKS.items():
        result = run_benchmark(benchmark, cfg)
        all_results[benchmark] = result

        out_file = OUTPUT_DIR / f"oracle_{benchmark}_2pl_gamma.json"
        with open(out_file, "w") as f:
            json.dump(result, f, indent=2)
        log.info("Saved: %s", out_file)

    # Summary
    summary_file = OUTPUT_DIR / "oracle_ablation_summary.json"
    summary = {}
    for bench, r in all_results.items():
        summary[bench] = {
            "gamma_mean": r["gamma"]["mean"],
            "gamma_ci95": [r["gamma"]["q025"], r["gamma"]["q975"]],
            "gamma_ci_excludes_zero": r["gamma"]["ci_excludes_zero"],
            "cal_mae": r["cal_mae"],
            "ppp": r["posterior_predictive"]["overall_ppp"],
            "diagnostics_ok": r["diagnostics"]["all_ok"],
            "n_models": r["n_models"],
            "n_items": r["n_items"],
        }
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=2)
    log.info("Summary saved: %s", summary_file)

    # Print results
    print("\n" + "=" * 60)
    print("ORACLE EXPOSURE ABLATION RESULTS")
    print("=" * 60)
    for bench, s in summary.items():
        print(f"\n{bench}:")
        print(f"  γ = {s['gamma_mean']:.4f} [{s['gamma_ci95'][0]:.4f}, {s['gamma_ci95'][1]:.4f}]")
        print(f"  CI excludes 0: {s['gamma_ci_excludes_zero']}")
        print(f"  CAL MAE: {s['cal_mae']:.4f}")
        print(f"  PPP: {s['ppp']:.4f}")
        print(f"  Diagnostics OK: {s['diagnostics_ok']}")


if __name__ == "__main__":
    main()

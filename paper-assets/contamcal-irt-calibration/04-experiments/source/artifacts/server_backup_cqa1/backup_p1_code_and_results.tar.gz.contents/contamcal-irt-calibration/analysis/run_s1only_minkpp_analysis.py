#!/usr/bin/env python3
"""S1-only ablation using Min-K%++ (s2_minkpp) as sole signal.

Compares S1-only item selection + exposure vs full RRF fusion for IRT calibration.
Runs: (1) pooled top-300 analysis for MMLU/ARC/GSM8K, (2) MMLU domain-stratified analysis.
"""

import json
import logging
import os
import sys
import time

import numpy as np
from scipy.stats import kendalltau, spearmanr

sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
from run_irt_calibration import (
    prepare_stan_data,
    fit_stan_model,
    check_convergence,
    posterior_predictive_check,
    extract_results,
    STAN_MODELS,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
SIGNALS_DIR = "/root/autodl-tmp/exp002/signals"
OUTPUT_DIR = "/root/autodl-tmp/exp006/s1only_minkpp_ablation"
MMLU_ARROW = "/root/autodl-tmp/.hf_cache/cais___mmlu/all/0.0.0/c30699e8356da336a370243923dbaf21066bb9fe/mmlu-test.arrow"
MODEL_TYPE = "2pl_gamma"
MAX_ITEMS = 300

# J=16 model definitions: (eval_dirname, signal_dirname, scale, dosage)
MODELS = [
    ("Qwen2.5-1.5B_d000_s123_aligned", "Qwen2.5-1.5B_d000_s123", "1.5B", 0),
    ("Qwen2.5-1.5B_d000_s42_aligned", "Qwen2.5-1.5B_d000_s42", "1.5B", 0),
    ("Qwen2.5-1.5B_d005_s123_aligned", "Qwen2.5-1.5B_d005_s123", "1.5B", 5),
    ("Qwen2.5-1.5B_d005_s42_aligned", "Qwen2.5-1.5B_d005_s42", "1.5B", 5),
    ("Qwen2.5-1.5B_d025_s123_aligned", "Qwen2.5-1.5B_d025_s123", "1.5B", 25),
    ("Qwen2.5-1.5B_d025_s42_aligned", "Qwen2.5-1.5B_d025_s42", "1.5B", 25),
    ("Qwen2.5-1.5B_d100_s123_aligned", "Qwen2.5-1.5B_d100_s123", "1.5B", 100),
    ("Qwen2.5-1.5B_d100_s42_aligned", "Qwen2.5-1.5B_d100_s42", "1.5B", 100),
    ("Qwen2.5-3B_d000_s123_aligned", "Qwen2.5-3B_d000_s123_a32", "3B", 0),
    ("Qwen2.5-3B_d000_s42_a32_aligned", "Qwen2.5-3B_d000_a32_s42", "3B", 0),
    ("Qwen2.5-3B_d005_s123_aligned", "Qwen2.5-3B_d005_s123", "3B", 5),
    ("Qwen2.5-3B_d005_s42_a32_aligned", "Qwen2.5-3B_d005_a32_s42", "3B", 5),
    ("Qwen2.5-3B_d025_s123_aligned", "Qwen2.5-3B_d025_s123", "3B", 25),
    ("Qwen2.5-3B_d025_v3_s42_aligned", "Qwen2.5-3B_d025_v3_s42", "3B", 25),
    ("Qwen2.5-3B_d100_a32_s123_aligned", "Qwen2.5-3B_d100_a32_s123", "3B", 100),
    ("Qwen2.5-3B_d100_a32_s42_aligned", "Qwen2.5-3B_d100_a32_s42", "3B", 100),
]

DOMAIN_MAP = {
    "STEM_Math": [
        "abstract_algebra", "college_mathematics", "elementary_mathematics",
        "high_school_mathematics", "high_school_statistics", "formal_logic",
    ],
    "STEM_Science": [
        "astronomy", "college_biology", "college_chemistry", "college_physics",
        "conceptual_physics", "high_school_biology", "high_school_chemistry",
        "high_school_physics",
    ],
    "STEM_CS_Eng": [
        "college_computer_science", "computer_security", "electrical_engineering",
        "high_school_computer_science", "machine_learning",
    ],
    "Medical": [
        "anatomy", "clinical_knowledge", "college_medicine", "human_aging",
        "medical_genetics", "nutrition", "professional_medicine", "virology",
    ],
    "Humanities": [
        "high_school_european_history", "high_school_us_history",
        "high_school_world_history", "logical_fallacies", "moral_disputes",
        "moral_scenarios", "philosophy", "prehistory", "world_religions",
    ],
    "Social_Sciences": [
        "econometrics", "high_school_geography",
        "high_school_government_and_politics", "high_school_macroeconomics",
        "high_school_microeconomics", "high_school_psychology",
        "human_sexuality", "professional_psychology", "public_relations",
        "security_studies", "sociology", "us_foreign_policy",
    ],
    "Business_Law": [
        "business_ethics", "international_law", "jurisprudence", "management",
        "marketing", "professional_accounting", "professional_law",
    ],
    "Other": [
        "global_facts", "miscellaneous",
    ],
}

STAN_CONFIG = {
    "chains": 4, "warmup": 1000, "samples": 1000,
    "adapt_delta": 0.95, "max_treedepth": 12, "seed": 42,
}


def load_responses(benchmark):
    responses = []
    for eval_dir, _, _, _ in MODELS:
        path = os.path.join(EVAL_DIR, eval_dir, "eval_results.json")
        with open(path) as f:
            data = json.load(f)
        per_item = data["benchmarks"][benchmark]["per_item"]
        responses.append([1 if item["correct"] else 0 for item in per_item])
    return np.array(responses, dtype=int)


def load_s2_minkpp(benchmark):
    """Load s2_minkpp scores for all 16 models. Returns [16, n_items].
    Orientation: negate stored values so higher = more suspicious."""
    s2_matrix = []
    for _, sig_dir, _, _ in MODELS:
        path = os.path.join(SIGNALS_DIR, sig_dir, f"signals_merged_{benchmark}.json")
        with open(path) as f:
            items = json.load(f)
        # s2_minkpp is stored as -raw_score, so already higher = less memorized
        # Negate again to get: higher = more memorized = more suspicious
        scores = [-(item.get("s2_minkpp", 0.0) or 0.0) for item in items]
        s2_matrix.append(scores)
    return np.array(s2_matrix, dtype=float)


def normalize_exposure(exposure):
    """Min-max normalize per model to [0, 1]."""
    normed = np.zeros_like(exposure)
    for i in range(exposure.shape[0]):
        mn, mx = exposure[i].min(), exposure[i].max()
        if mx > mn:
            normed[i] = (exposure[i] - mn) / (mx - mn)
    return normed


def compute_ground_truth(raw_acc, dosages, scales):
    """Ground truth = clean ability (d000 mean per scale)."""
    n = len(dosages)
    gt = np.empty(n)
    for i in range(n):
        if dosages[i] == 0:
            gt[i] = raw_acc[i]
        else:
            same_scale_d0 = [j for j in range(n) if dosages[j] == 0 and scales[j] == scales[i]]
            gt[i] = float(raw_acc[same_scale_d0].mean())
    return gt


def fit_irt(responses, exposure, label=""):
    """Fit 2PL+gamma IRT and return results dict."""
    stan_data = prepare_stan_data(responses, exposure, MODEL_TYPE)
    stan_file = STAN_MODELS[MODEL_TYPE]

    t0 = time.time()
    fit, elapsed = fit_stan_model(
        stan_file, stan_data,
        chains=STAN_CONFIG["chains"],
        iter_warmup=STAN_CONFIG["warmup"],
        iter_sampling=STAN_CONFIG["samples"],
        adapt_delta=STAN_CONFIG["adapt_delta"],
        max_treedepth=STAN_CONFIG["max_treedepth"],
        seed=STAN_CONFIG["seed"],
    )
    diagnostics = check_convergence(fit)
    ppc = posterior_predictive_check(fit, responses)
    results = extract_results(fit, responses, MODEL_TYPE)

    log.info("[%s] gamma=%.4f [%.4f, %.4f], Rhat=%.4f, ESS=%.0f, div=%d, PPP=%.4f, time=%.0fs",
             label,
             results.get("gamma", {}).get("mean", 0),
             results.get("gamma", {}).get("q025", 0),
             results.get("gamma", {}).get("q975", 0),
             diagnostics.get("max_rhat", 0),
             diagnostics.get("min_ess", 0),
             diagnostics.get("divergent_count", 0),
             ppc.get("overall_ppp", 0),
             elapsed)

    return {
        "gamma": results.get("gamma", {}),
        "diagnostics": diagnostics,
        "ppc": ppc,
        "calibrated_scores": results.get("calibrated_scores", {}),
        "fit_time_sec": round(elapsed, 1),
    }


def run_pooled_benchmark(benchmark, max_items=MAX_ITEMS):
    """Run pooled top-N analysis for one benchmark."""
    log.info("=" * 60)
    log.info("POOLED S1-only (Min-K++): %s", benchmark)

    responses = load_responses(benchmark)
    s2_matrix = load_s2_minkpp(benchmark)
    n_models, n_items = responses.shape
    log.info("Loaded: %d models x %d items", n_models, n_items)

    # Select top items by mean oriented s2_minkpp
    mean_s2 = s2_matrix.mean(axis=0)
    if n_items > max_items:
        top_idx = np.sort(np.argsort(-mean_s2)[:max_items])
    else:
        top_idx = np.arange(n_items)
    log.info("Selected %d/%d items by mean Min-K++ score", len(top_idx), n_items)

    y = responses[:, top_idx]
    exposure_raw = s2_matrix[:, top_idx]
    exposure = normalize_exposure(exposure_raw)

    log.info("Exposure stats: mean=%.4f, max=%.4f", exposure.mean(), exposure.max())

    result = fit_irt(y, exposure, label=f"pooled_{benchmark}")

    # Compute comparison metrics
    dosages = np.array([d for _, _, _, d in MODELS])
    scales = [s for _, _, s, _ in MODELS]
    raw_acc = y.mean(axis=1)
    cal_mean = np.array(result["calibrated_scores"]["mean"])
    gt = compute_ground_truth(raw_acc, dosages, scales)

    tau_val, tau_p = kendalltau(cal_mean, gt)
    rho_dose, rho_p = spearmanr(cal_mean, dosages)
    mae = float(np.mean(np.abs(cal_mean - gt)))

    log.info("tau=%.4f (p=%.6f), rho_dose=%.4f, MAE=%.4f", tau_val, tau_p, rho_dose, mae)

    result.update({
        "benchmark": benchmark,
        "method": "s1_only_minkpp_top300",
        "n_models": n_models,
        "n_items": len(top_idx),
        "original_n_items": n_items,
        "tau": round(float(tau_val), 4),
        "tau_p": float(tau_p),
        "rho_dose": round(float(rho_dose), 4),
        "mae_cal": round(mae, 4),
        "raw_accuracy": raw_acc.tolist(),
        "ground_truth": gt.tolist(),
        "s2_threshold": float(mean_s2[top_idx].min()),
    })
    return result


def build_subject_index_map():
    import pyarrow as pa
    reader = pa.ipc.open_stream(MMLU_ARROW)
    table = reader.read_all()
    return table.column("subject").to_pylist()


def run_mmlu_domain_analysis():
    """Run per-domain IRT analysis for MMLU with s2_minkpp exposure."""
    log.info("=" * 60)
    log.info("MMLU DOMAIN-STRATIFIED S1-only (Min-K++) analysis")

    responses = load_responses("mmlu")
    s2_matrix = load_s2_minkpp("mmlu")
    n_models, n_items = responses.shape

    # Build domain index mapping
    subject_list = build_subject_index_map()
    subj_to_domain = {}
    for domain, subjects in DOMAIN_MAP.items():
        for s in subjects:
            subj_to_domain[s] = domain

    domain_indices = {d: [] for d in DOMAIN_MAP}
    for i in range(min(len(subject_list), n_items)):
        domain = subj_to_domain.get(subject_list[i])
        if domain:
            domain_indices[domain].append(i)

    # Normalize full exposure matrix
    exposure_full = normalize_exposure(s2_matrix)

    domain_results = {}
    for domain in DOMAIN_MAP:
        idx = domain_indices[domain]
        if len(idx) < 10:
            log.warning("Skipping %s: only %d items", domain, len(idx))
            continue

        log.info("--- Domain: %s (%d items) ---", domain, len(idx))
        idx_arr = np.array(idx)
        y_domain = responses[:, idx_arr]
        exp_domain = exposure_full[:, idx_arr]

        result = fit_irt(y_domain, exp_domain, label=domain)
        result["domain"] = domain
        result["n_items"] = len(idx)
        result["n_models"] = n_models
        result["mean_acc"] = float(y_domain.mean())
        domain_results[domain] = result

    return domain_results


def load_rrf_baselines():
    """Load existing RRF baseline results for comparison."""
    baselines = {}

    # Pooled RRF results (J=16)
    pooled_path = "/root/autodl-tmp/exp006/pooled_irt_2pl_gamma_n16_fixed/pooled_rrf_irt_results.json"
    if os.path.exists(pooled_path):
        with open(pooled_path) as f:
            data = json.load(f)
        for bench, r in data.get("per_benchmark", {}).items():
            baselines[f"pooled_{bench}"] = {
                "gamma_mean": r["gamma"]["mean"],
                "gamma_q025": r["gamma"]["q025"],
                "gamma_q975": r["gamma"]["q975"],
                "ppp": r["posterior_predictive"]["overall_ppp"],
                "cal_mae": r.get("cal_mae", None),
                "raw_mae": r.get("raw_mae", None),
                "n_items": r["n_items"],
                "rhat": r["diagnostics"]["max_rhat"],
                "ess": r["diagnostics"]["min_ess"],
            }

    # Domain RRF results (J=16)
    domain_path = "/root/autodl-tmp/exp006/mmlu_domain_irt_j16_qwen/all_domain_results.json"
    if os.path.exists(domain_path):
        with open(domain_path) as f:
            data = json.load(f)
        for domain, r in data.items():
            baselines[f"domain_{domain}"] = {
                "gamma_mean": r["gamma"]["mean"],
                "gamma_q025": r["gamma"]["q025"],
                "gamma_q975": r["gamma"]["q975"],
                "ppp": r["ppp"]["overall_ppp"],
                "n_items": r["n_items"],
                "rhat": r["diagnostics"]["max_rhat"],
                "ess": r["diagnostics"]["min_ess"],
            }

    return baselines


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_results = {"pooled": {}, "domain": {}}

    # 1. Pooled analysis for each benchmark
    for bench in ["mmlu", "arc_challenge", "gsm8k"]:
        result = run_pooled_benchmark(bench)
        all_results["pooled"][bench] = result

        bench_dir = os.path.join(OUTPUT_DIR, bench)
        os.makedirs(bench_dir, exist_ok=True)
        with open(os.path.join(bench_dir, "s1only_minkpp_results.json"), "w") as f:
            json.dump(result, f, indent=2)

    # 2. MMLU domain-stratified analysis
    domain_results = run_mmlu_domain_analysis()
    all_results["domain"] = domain_results

    domain_dir = os.path.join(OUTPUT_DIR, "mmlu_domains")
    os.makedirs(domain_dir, exist_ok=True)
    with open(os.path.join(domain_dir, "domain_results.json"), "w") as f:
        json.dump(domain_results, f, indent=2)

    # 3. Load RRF baselines and compare
    baselines = load_rrf_baselines()

    # 4. Print comparison table
    print("\n" + "=" * 100)
    print("S1-ONLY (Min-K++) vs FULL RRF COMPARISON")
    print("=" * 100)

    print("\n--- POOLED ANALYSIS ---")
    print(f"{'Bench':<16} {'Method':<12} {'N_item':>6} {'gamma':>8} {'95% CI':>20} "
          f"{'PPP':>6} {'Rhat':>6} {'ESS':>6} {'tau':>8} {'MAE':>8}")
    print("-" * 100)

    for bench in ["mmlu", "arc_challenge", "gsm8k"]:
        r = all_results["pooled"][bench]
        g = r["gamma"]
        d = r["diagnostics"]
        print(f"{bench:<16} {'S1-only':<12} {r['n_items']:>6} "
              f"{g['mean']:>8.4f} [{g['q025']:.3f}, {g['q975']:.3f}] "
              f"{r['ppc']['overall_ppp']:>6.4f} {d['max_rhat']:>6.4f} {d['min_ess']:>6.0f} "
              f"{r['tau']:>8.4f} {r['mae_cal']:>8.4f}")

        bl_key = f"pooled_{bench}"
        if bl_key in baselines:
            bl = baselines[bl_key]
            cal_mae_str = f"{bl['cal_mae']:>8.4f}" if bl['cal_mae'] is not None else "     N/A"
            print(f"{'':16} {'RRF':<12} {bl['n_items']:>6} "
                  f"{bl['gamma_mean']:>8.4f} [{bl['gamma_q025']:.3f}, {bl['gamma_q975']:.3f}] "
                  f"{bl['ppp']:>6.4f} {bl['rhat']:>6.4f} {bl['ess']:>6.0f} "
                  f"{'':>8} {cal_mae_str}")
            print(f"{'':16} {'Delta':<12} {'':>6} "
                  f"{g['mean'] - bl['gamma_mean']:>+8.4f}")

    print("\n--- MMLU DOMAIN-STRATIFIED GAMMA ---")
    print(f"{'Domain':<18} {'Method':<10} {'N_item':>6} {'gamma':>8} {'95% CI':>22} "
          f"{'PPP':>6} {'Rhat':>6} {'ESS':>6}")
    print("-" * 90)

    for domain in DOMAIN_MAP:
        if domain not in domain_results:
            continue
        r = domain_results[domain]
        g = r["gamma"]
        d = r["diagnostics"]
        print(f"{domain:<18} {'S1-only':<10} {r['n_items']:>6} "
              f"{g['mean']:>8.4f} [{g['q025']:.3f}, {g['q975']:.3f}] "
              f"{r['ppc']['overall_ppp']:>6.4f} {d['max_rhat']:>6.4f} {d['min_ess']:>6.0f}")

        bl_key = f"domain_{domain}"
        if bl_key in baselines:
            bl = baselines[bl_key]
            print(f"{'':18} {'RRF':<10} {bl['n_items']:>6} "
                  f"{bl['gamma_mean']:>8.4f} [{bl['gamma_q025']:.3f}, {bl['gamma_q975']:.3f}] "
                  f"{bl['ppp']:>6.4f} {bl['rhat']:>6.4f} {bl['ess']:>6.0f}")

    # Save full results
    with open(os.path.join(OUTPUT_DIR, "s1only_minkpp_full_results.json"), "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    # Save comparison summary
    comparison = {"s1_only": {}, "rrf_baseline": baselines}
    for bench in ["mmlu", "arc_challenge", "gsm8k"]:
        r = all_results["pooled"][bench]
        comparison["s1_only"][f"pooled_{bench}"] = {
            "gamma_mean": r["gamma"]["mean"],
            "gamma_q025": r["gamma"]["q025"],
            "gamma_q975": r["gamma"]["q975"],
            "ppp": r["ppc"]["overall_ppp"],
            "tau": r["tau"],
            "mae_cal": r["mae_cal"],
            "rho_dose": r["rho_dose"],
            "rhat": r["diagnostics"]["max_rhat"],
            "ess": r["diagnostics"]["min_ess"],
            "n_items": r["n_items"],
        }
    for domain, r in domain_results.items():
        comparison["s1_only"][f"domain_{domain}"] = {
            "gamma_mean": r["gamma"]["mean"],
            "gamma_q025": r["gamma"]["q025"],
            "gamma_q975": r["gamma"]["q975"],
            "ppp": r["ppc"]["overall_ppp"],
            "rhat": r["diagnostics"]["max_rhat"],
            "ess": r["diagnostics"]["min_ess"],
            "n_items": r["n_items"],
        }

    with open(os.path.join(OUTPUT_DIR, "comparison_summary.json"), "w") as f:
        json.dump(comparison, f, indent=2)

    print(f"\nResults saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()

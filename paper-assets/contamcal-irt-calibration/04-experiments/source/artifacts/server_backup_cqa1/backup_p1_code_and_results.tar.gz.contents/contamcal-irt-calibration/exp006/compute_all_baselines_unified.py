#!/usr/bin/env python3
"""Unified baseline computation: MAE + Kendall tau for all methods.

Ground truth = per-scale d=0 model accuracy (d=0 models get their own raw acc).
MAE = mean |calibrated - ground_truth| across all models.
tau = Kendall tau between calibrated scores and ground truth.

Config: MMLU/ARC J=16 (1.5B+3B), GSM8K J=24 (all scales)
"""
import json
import logging
import os
import re
import sys
from pathlib import Path

import numpy as np
from scipy.stats import kendalltau

sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
from run_irt_calibration import load_pooled_eval_results
from baselines import (
    RemoveRescoreBaseline, LinearRegressionBaseline,
    EmperorMitigationBaseline, DCRFuzzyBaseline,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
RRF_PATH = "/root/autodl-tmp/exp003/rrf_all_scales/exposure_scores.json"
IRT_2PL_GAMMA_DIR = "/root/autodl-tmp/exp006/pooled_irt_2pl_gamma_n16_fixed"
IRT_VANILLA_2PL_DIR = "/root/autodl-tmp/exp006/pooled_irt_vanilla_2pl_n16_fixed"
OUTPUT_DIR = "/root/autodl-tmp/exp006/unified_baselines_n16"
MAX_ITEMS = 300
BENCHMARKS = ["mmlu", "arc_challenge", "gsm8k"]


def strip_aligned(dirname):
    return re.sub(r'(_para)?(_aligned)?$', '', dirname)

def normalize_model_key(key):
    a_match = re.search(r'_(a\d+)', key)
    s_match = re.search(r'_(s\d+)', key)
    base = re.sub(r'_(a\d+|s\d+)', '', key)
    suffix = ''
    if a_match: suffix += '_' + a_match.group(1)
    if s_match: suffix += '_' + s_match.group(1)
    return base + suffix

def resolve_rrf_key(eval_key, rrf_data, norm_rrf):
    if eval_key in rrf_data: return eval_key
    norm = normalize_model_key(eval_key)
    if norm in norm_rrf: return norm_rrf[norm]
    if '_a' not in eval_key:
        norm_a32 = normalize_model_key(eval_key + '_a32')
        if norm_a32 in norm_rrf: return norm_rrf[norm_a32]
    return None


def compute_ground_truth_from_irt(irt_result):
    """Compute ground truth from IRT result metadata.
    d=0 models: raw accuracy. d>0 models: same-scale d=0 mean."""
    models = irt_result["models"]
    raw_acc = np.array(irt_result["raw_accuracy"])
    dosages = np.array([m["dosage"] for m in models])
    scales = [m["scale"] for m in models]

    gt = np.empty(len(models))
    for i, (d, sc) in enumerate(zip(dosages, scales)):
        if d == 0:
            gt[i] = raw_acc[i]
        else:
            same_scale_d0 = [j for j in range(len(models))
                             if dosages[j] == 0 and scales[j] == sc]
            gt[i] = float(raw_acc[same_scale_d0].mean()) if same_scale_d0 else raw_acc[i]
    return gt


def compute_drc_scores(raw_acc, dosages):
    return raw_acc * (1.0 - np.array(dosages) / 100.0)

def compute_threshold_scores(y, exposure):
    N_models = y.shape[0]
    adjusted = np.zeros(N_models)
    for i in range(N_models):
        median_exp = np.median(exposure[i])
        clean_mask = exposure[i] <= median_exp
        adjusted[i] = y[i, clean_mask].mean() if clean_mask.sum() > 0 else y[i].mean()
    return adjusted


def run_for_benchmark(benchmark, eval_data, rrf_data):
    log.info("=" * 60)
    log.info("BENCHMARK: %s", benchmark)

    # Load IRT results (authoritative model list)
    irt_2pl_gamma = json.load(open(f"{IRT_2PL_GAMMA_DIR}/{benchmark}/irt_results.json"))
    irt_vanilla = json.load(open(f"{IRT_VANILLA_2PL_DIR}/{benchmark}/irt_results.json"))
    irt_models = irt_2pl_gamma["models"]
    n_models = len(irt_models)

    # Ground truth from IRT metadata
    raw_acc = np.array(irt_2pl_gamma["raw_accuracy"])
    dosages = np.array([m["dosage"] for m in irt_models])
    scales = [m["scale"] for m in irt_models]
    ground_truth = compute_ground_truth_from_irt(irt_2pl_gamma)

    for sc in sorted(set(scales)):
        d0_idx = [j for j in range(n_models) if dosages[j] == 0 and scales[j] == sc]
        log.info("GT [%s]: d0 mean=%.4f (n=%d)", sc, raw_acc[d0_idx].mean(), len(d0_idx))

    # Match IRT models to eval data and load response/exposure matrices
    eval_dirname_to_idx = {m["dirname"]: i for i, m in enumerate(eval_data["models"])}
    bench_data = eval_data["benchmarks"][benchmark]
    full_responses = bench_data["responses"]
    n_total_items = full_responses.shape[1]

    keep_idx = []
    for m in irt_models:
        if m["dirname"] in eval_dirname_to_idx:
            keep_idx.append(eval_dirname_to_idx[m["dirname"]])
        else:
            log.error("Model %s not found in eval data!", m["dirname"])
            return None
    keep_idx = np.array(keep_idx)
    responses = full_responses[keep_idx]

    # Subsample items (same as IRT)
    if n_total_items > MAX_ITEMS:
        np.random.seed(42)
        subsample_idx = np.sort(np.random.choice(n_total_items, MAX_ITEMS, replace=False))
        responses = responses[:, subsample_idx]
    else:
        subsample_idx = None

    # Verify raw accuracy alignment
    our_raw = responses.mean(axis=1)
    max_diff = np.max(np.abs(our_raw - raw_acc))
    log.info("Raw acc alignment check: max_diff=%.6f", max_diff)
    if max_diff > 0.001:
        log.warning("Raw accuracy mismatch > 0.001! Using IRT raw_acc for ground truth anyway.")

    # Build exposure matrix from RRF
    norm_rrf = {normalize_model_key(k): k for k in rrf_data}
    exposure = np.zeros_like(responses, dtype=float)
    for i, m in enumerate(irt_models):
        key = strip_aligned(m["dirname"])
        rrf_key = resolve_rrf_key(key, rrf_data, norm_rrf)
        if rrf_key is None or benchmark not in rrf_data.get(rrf_key, {}):
            continue
        scores = rrf_data[rrf_key][benchmark]["exposure_scores"]
        if subsample_idx is not None:
            exposure[i, :] = np.array(scores[:n_total_items])[subsample_idx]
        else:
            exposure[i, :] = scores[:n_total_items]

    N_items = responses.shape[1]
    log.info("Aligned: %d models x %d items", n_models, N_items)

    # --- Run all methods ---
    results = {}

    # B0: Raw accuracy
    results["B0_Raw"] = raw_acc

    # B1: DRC (oracle dosage scaling)
    results["B1_DRC"] = compute_drc_scores(raw_acc, dosages)

    # B1b: Remove-and-Rescore
    b1b = RemoveRescoreBaseline()
    results["B1b_RemRescore"] = np.array(b1b.fit(responses, exposure)["calibrated_scores"])

    # B3: Vanilla 2PL
    results["B3_V2PL"] = np.array(irt_vanilla["calibrated_scores"]["mean"])

    # B4: Linear Regression
    b4 = LinearRegressionBaseline()
    results["B4_LinReg"] = np.array(b4.fit(responses, exposure)["calibrated_scores"])

    # B5: Threshold Classifier
    results["B5_Thresh"] = compute_threshold_scores(responses, exposure)

    # B5b: Emperor Mitigation
    b5b = EmperorMitigationBaseline()
    results["B5b_Emperor"] = np.array(b5b.fit(responses, exposure)["calibrated_scores"])

    # B6: DCR Fuzzy
    b6 = DCRFuzzyBaseline()
    results["B6_DCR"] = np.array(b6.fit(responses, exposure)["calibrated_scores"])

    # ContamCal: 2PL+gamma
    results["ContamCal"] = np.array(irt_2pl_gamma["calibrated_scores"]["mean"])

    # --- Compute metrics ---
    metrics = []
    for method_name, cal in results.items():
        cal = np.array(cal)
        mae = float(np.mean(np.abs(cal - ground_truth)))
        tau_gt, tau_gt_p = kendalltau(cal, ground_truth)

        m = {
            "method": method_name,
            "mae": round(mae, 4),
            "tau": round(float(tau_gt), 4),
            "tau_p": float(tau_gt_p),
        }
        metrics.append(m)
        p_star = "*" if tau_gt_p < 0.05 else ""
        log.info("  %-16s MAE=%.4f  tau=%.4f%s (p=%.4f)",
                 method_name, mae, tau_gt, p_star, tau_gt_p)

    return {
        "benchmark": benchmark,
        "n_models": n_models,
        "n_items": N_items,
        "metrics": metrics,
        "gamma": irt_2pl_gamma.get("gamma", {}),
        "models": [
            {"name": irt_models[i]["dirname"], "scale": scales[i],
             "dosage": int(dosages[i]),
             "raw_acc": round(float(raw_acc[i]), 4),
             "gt": round(float(ground_truth[i]), 4)}
            for i in range(n_models)
        ],
    }


def format_table(all_results):
    methods_order = [
        "B0_Raw", "B1_DRC", "B1b_RemRescore",
        "B3_V2PL", "B4_LinReg",
        "B5_Thresh", "B5b_Emperor",
        "B6_DCR", "ContamCal",
    ]
    labels = {
        "B0_Raw": "Raw Accuracy",
        "B1_DRC": "DRC (oracle)",
        "B1b_RemRescore": "Remove & Rescore",
        "B3_V2PL": "Vanilla 2PL",
        "B4_LinReg": "Linear Regression",
        "B5_Thresh": "Threshold",
        "B5b_Emperor": "Emperor",
        "B6_DCR": "DCR Fuzzy",
        "ContamCal": "ContamCal (2PL+g)",
    }

    lines = []
    header = "| Method |"
    sep = "|--------|"
    for b in BENCHMARKS:
        bname = {"mmlu": "MMLU", "arc_challenge": "ARC", "gsm8k": "GSM8K"}[b]
        if b in all_results:
            n = all_results[b]["n_models"]
            header += f" {bname} MAE | {bname} tau |"
        else:
            header += f" {bname} MAE | {bname} tau |"
        sep += "---------|--------|"
    lines.append(header)
    lines.append(sep)

    for method in methods_order:
        label = labels.get(method, method)
        row = f"| {label:<22} |"
        for bench in BENCHMARKS:
            if bench in all_results:
                bench_metrics = {m["method"]: m for m in all_results[bench]["metrics"]}
                if method in bench_metrics:
                    m = bench_metrics[method]
                    p_star = "*" if m["tau_p"] < 0.05 else ""
                    row += f" {m['mae']:.4f}  | {m['tau']:.3f}{p_star:<2}|"
                else:
                    row += " --      | --     |"
            else:
                row += " --      | --     |"
        lines.append(row)

    return "\n".join(lines)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    log.info("Loading eval results...")
    eval_data = load_pooled_eval_results(
        EVAL_DIR, ["0.5B", "1.5B", "3B"],
        benchmarks=BENCHMARKS, aligned_only=True)
    log.info("Loaded %d models", len(eval_data["models"]))

    rrf_data = json.load(open(RRF_PATH))
    log.info("RRF data for %d models", len(rrf_data))

    all_results = {}
    for bench in BENCHMARKS:
        if bench not in eval_data["benchmarks"]:
            continue
        result = run_for_benchmark(bench, eval_data, rrf_data)
        if result:
            all_results[bench] = result

    # Save
    with open(f"{OUTPUT_DIR}/all_results.json", "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    # Print table
    table = format_table(all_results)
    print("\n" + "=" * 100)
    print("UNIFIED BASELINE COMPARISON TABLE")
    print("MMLU/ARC: J=16 (1.5B+3B), GSM8K: J=24 (all scales)")
    print("MAE = |calibrated - ground_truth|, tau = Kendall(calibrated, ground_truth)")
    print("Ground truth = per-scale d=0 model accuracy")
    print("* = p < 0.05")
    print("=" * 100)
    print(table)

    for bench in BENCHMARKS:
        if bench not in all_results:
            continue
        r = all_results[bench]
        gamma = r.get("gamma", {})
        print(f"\n{bench}: J={r['n_models']}, I={r['n_items']}, "
              f"gamma={gamma.get('mean', 'N/A')}")

    with open(f"{OUTPUT_DIR}/table.md", "w") as f:
        f.write(table)
    log.info("Saved to %s", OUTPUT_DIR)


if __name__ == "__main__":
    main()

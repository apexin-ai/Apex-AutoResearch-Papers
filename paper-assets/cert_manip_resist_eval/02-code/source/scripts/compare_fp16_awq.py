#!/usr/bin/env python3
"""Paired comparison of FP16 vs AWQ attack susceptibility (η).

Reads per-judge per-condition η from individual_scores, computes:
- Pearson + Spearman correlation between FP16 and AWQ η vectors
- Δη = η_FP16 - η_AWQ per condition, mean and 95% CI (bootstrap)
- Conclusion: ρ > 0.9 and Δη CI includes 0 → quantization not a confound
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
from scipy import stats

RESULTS_DIR = Path("/root/cert_manip_resist_eval/results/fp16_experiment")
SCORES_DIR = RESULTS_DIR / "individual_scores"

MODELS = ["llama3.1-8b", "qwen2.5-14b", "qwen2.5-32b"]
DATASETS = ["mmlu", "arc_challenge"]
ATTACK_NAMES = [
    "prompt_injection", "sycophancy", "score_manipulation",
    "verbosity_bias", "position_bias", "authority_bias",
]

N_BOOTSTRAP = 10000
ALPHA = 0.05
SEED = 42


def load_asr(model_id: str, dataset: str, condition: str) -> float:
    path = SCORES_DIR / f"{model_id}__{dataset}__{condition}.json"
    if not path.exists():
        return None
    with open(path) as f:
        data = json.load(f)
    return data.get("asr")


def load_accuracy(model_id: str, dataset: str) -> float:
    path = SCORES_DIR / f"{model_id}__{dataset}__clean.json"
    if not path.exists():
        return None
    with open(path) as f:
        data = json.load(f)
    return data.get("accuracy")


def bootstrap_ci(data: np.ndarray, n_boot: int = N_BOOTSTRAP, alpha: float = ALPHA) -> Tuple[float, float]:
    rng = np.random.RandomState(SEED)
    n = len(data)
    boot_means = np.array([data[rng.randint(0, n, n)].mean() for _ in range(n_boot)])
    lo = np.percentile(boot_means, 100 * alpha / 2)
    hi = np.percentile(boot_means, 100 * (1 - alpha / 2))
    return float(lo), float(hi)


def main():
    rng = np.random.RandomState(SEED)

    # Collect η pairs: (η_awq, η_fp16) for each (model, dataset, attack)
    awq_etas = []
    fp16_etas = []
    labels = []
    deltas = []

    per_model_results = {}

    for model_name in MODELS:
        awq_id = f"{model_name}-awq"
        fp16_id = f"{model_name}-fp16"
        model_deltas = []
        model_pairs = []

        for ds in DATASETS:
            awq_acc = load_accuracy(awq_id, ds)
            fp16_acc = load_accuracy(fp16_id, ds)

            for atk in ATTACK_NAMES:
                eta_awq = load_asr(awq_id, ds, atk)
                eta_fp16 = load_asr(fp16_id, ds, atk)

                if eta_awq is None or eta_fp16 is None:
                    print(f"WARNING: Missing data for {model_name}/{ds}/{atk}", file=sys.stderr)
                    continue

                awq_etas.append(eta_awq)
                fp16_etas.append(eta_fp16)
                delta = eta_fp16 - eta_awq
                deltas.append(delta)
                labels.append(f"{model_name}/{ds}/{atk}")
                model_deltas.append(delta)
                model_pairs.append({
                    "dataset": ds,
                    "attack": atk,
                    "eta_awq": round(eta_awq, 4),
                    "eta_fp16": round(eta_fp16, 4),
                    "delta_eta": round(delta, 4),
                })

        if model_deltas:
            arr = np.array(model_deltas)
            ci_lo, ci_hi = bootstrap_ci(arr)
            per_model_results[model_name] = {
                "n_conditions": len(model_deltas),
                "mean_delta_eta": round(arr.mean(), 4),
                "std_delta_eta": round(arr.std(), 4),
                "ci_95_lo": round(ci_lo, 4),
                "ci_95_hi": round(ci_hi, 4),
                "ci_includes_zero": bool(ci_lo <= 0 <= ci_hi),
                "awq_clean_acc": {ds: load_accuracy(f"{model_name}-awq", ds) for ds in DATASETS},
                "fp16_clean_acc": {ds: load_accuracy(f"{model_name}-fp16", ds) for ds in DATASETS},
                "conditions": model_pairs,
            }

    if len(awq_etas) < 3:
        print("ERROR: Not enough data points for comparison", file=sys.stderr)
        sys.exit(1)

    awq_arr = np.array(awq_etas)
    fp16_arr = np.array(fp16_etas)
    delta_arr = np.array(deltas)

    # Correlation
    pearson_r, pearson_p = stats.pearsonr(awq_arr, fp16_arr)
    spearman_r, spearman_p = stats.spearmanr(awq_arr, fp16_arr)

    # Overall Δη
    mean_delta = delta_arr.mean()
    std_delta = delta_arr.std()
    ci_lo, ci_hi = bootstrap_ci(delta_arr)

    # Paired t-test
    t_stat, t_pval = stats.ttest_rel(fp16_arr, awq_arr)

    # Conclusion
    high_corr = pearson_r > 0.9
    ci_zero = ci_lo <= 0 <= ci_hi
    conclusion = "PASS" if (high_corr and ci_zero) else "FAIL"
    conclusion_text = (
        f"Quantization is NOT a major confound (ρ={pearson_r:.3f} > 0.9, "
        f"Δη CI [{ci_lo:.4f}, {ci_hi:.4f}] includes 0)"
        if conclusion == "PASS" else
        f"Quantization MAY be a confound (ρ={pearson_r:.3f}, "
        f"Δη CI [{ci_lo:.4f}, {ci_hi:.4f}])"
    )

    result = {
        "timestamp": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
        "n_conditions": len(awq_etas),
        "overall": {
            "pearson_r": round(pearson_r, 4),
            "pearson_p": round(pearson_p, 6),
            "spearman_r": round(spearman_r, 4),
            "spearman_p": round(spearman_p, 6),
            "mean_delta_eta": round(mean_delta, 4),
            "std_delta_eta": round(std_delta, 4),
            "ci_95": [round(ci_lo, 4), round(ci_hi, 4)],
            "ci_includes_zero": bool(ci_zero),
            "paired_ttest_t": round(t_stat, 4),
            "paired_ttest_p": round(t_pval, 6),
            "conclusion": conclusion,
            "conclusion_text": conclusion_text,
        },
        "per_model": per_model_results,
    }

    # Save JSON
    out_path = RESULTS_DIR / "fp16_vs_awq_comparison.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    # Human-readable summary
    print("=" * 80)
    print("FP16 vs AWQ Quantization: Paired Comparison")
    print("=" * 80)
    print(f"\nN conditions: {len(awq_etas)} ({len(MODELS)} models × {len(DATASETS)} benchmarks × {len(ATTACK_NAMES)} attacks)")
    print(f"\nCorrelation:")
    print(f"  Pearson  ρ = {pearson_r:.4f}  (p = {pearson_p:.2e})")
    print(f"  Spearman ρ = {spearman_r:.4f}  (p = {spearman_p:.2e})")
    print(f"\nΔη (FP16 - AWQ):")
    print(f"  Mean = {mean_delta:.4f}  (SD = {std_delta:.4f})")
    print(f"  95% CI = [{ci_lo:.4f}, {ci_hi:.4f}]")
    print(f"  Paired t-test: t = {t_stat:.3f}, p = {t_pval:.2e}")
    print(f"\nPer-model breakdown:")
    for model_name, mr in per_model_results.items():
        print(f"\n  {model_name}:")
        print(f"    Clean acc: AWQ={mr['awq_clean_acc']}, FP16={mr['fp16_clean_acc']}")
        print(f"    Δη: mean={mr['mean_delta_eta']:.4f}, 95% CI=[{mr['ci_95_lo']:.4f}, {mr['ci_95_hi']:.4f}]")
        print(f"    CI includes 0: {mr['ci_includes_zero']}")

    print(f"\n{'='*80}")
    print(f"CONCLUSION: {conclusion}")
    print(f"  {conclusion_text}")
    print(f"{'='*80}")
    print(f"\nResults saved to: {out_path}")


if __name__ == "__main__":
    main()

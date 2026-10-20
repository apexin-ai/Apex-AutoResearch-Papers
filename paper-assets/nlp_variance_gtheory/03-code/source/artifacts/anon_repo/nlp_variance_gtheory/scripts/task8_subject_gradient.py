"""Task 8: Within-MMLU Subject Gradient Analysis.

For each of 10 MMLU subjects, run a 7-facet Henderson I G-study
(model, precision, temperature, prompt_template, seed, ordering, item_id)
on the 4-model balanced bf16 data, then check whether item_id dominance
varies across subjects and correlates with subject accuracy.
"""

import json
import sys
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, ".")
from src.analysis.variance_decomposition import compute_ss, estimate_variance_components

ALL_FACETS = ["model", "precision", "temperature", "prompt_template", "seed", "ordering", "item_id"]
FIXED_FACETS = ["precision", "temperature"]
RANDOM_FACETS = ["model", "prompt_template", "seed", "ordering", "item_id"]


def compute_g_item(vc: dict, n_levels: dict) -> float:
    """G coefficient treating item_id as the object of measurement."""
    fixed_set = set(FIXED_FACETS)
    sigma_tau = 0.0
    sigma_delta = 0.0

    for comp, est in vc.items():
        if est <= 0:
            continue
        if comp == "residual":
            divisor = prod(n_levels.get(f, 1) for f in RANDOM_FACETS)
            sigma_delta += est / divisor
            continue

        facets_in = comp.split(":")
        random_in = [f for f in facets_in if f not in fixed_set]

        if len(random_in) == 0:
            sigma_tau += est
        else:
            divisor = prod(n_levels.get(f, 1) for f in random_in)
            sigma_delta += est / divisor

    total = sigma_tau + sigma_delta
    return sigma_tau / total if total > 0 else 0.0


def analyze_subject(df_subj: pd.DataFrame, subject_name: str) -> dict:
    """Run 7-facet G-study on a single subject's data."""
    for f in ALL_FACETS:
        df_subj[f] = df_subj[f].astype(str)

    # Check balance: precision has only 1 level (bfloat16), so drop it from facets
    n_levels_check = {f: df_subj[f].nunique() for f in ALL_FACETS}
    active_facets = [f for f in ALL_FACETS if n_levels_check[f] > 1]

    effects, n_levels = compute_ss(df_subj, "correct", active_facets)
    vc = estimate_variance_components(effects, active_facets, n_levels)
    total_var = sum(v for v in vc.values() if v > 0)

    # Extract key metrics
    item_id_est = max(0, vc.get("item_id", 0))
    item_id_pct = item_id_est / total_var * 100 if total_var > 0 else 0
    model_item_est = max(0, vc.get("model:item_id", 0))
    model_item_pct = model_item_est / total_var * 100 if total_var > 0 else 0
    model_est = max(0, vc.get("model", 0))
    model_pct = model_est / total_var * 100 if total_var > 0 else 0

    # G coefficient at observed design
    random_n = {f: n_levels[f] for f in RANDOM_FACETS if f in n_levels}
    g_item = compute_g_item(vc, random_n)

    # All variance components with pct
    vc_detail = {}
    for k, v in sorted(vc.items(), key=lambda x: -x[1]):
        vc_detail[k] = {
            "estimate": round(v, 8),
            "pct": round(v / total_var * 100 if total_var > 0 else 0, 2)
        }

    return {
        "n_items": int(n_levels.get("item_id", 0)),
        "n_observations": len(df_subj),
        "accuracy": round(df_subj["correct"].mean(), 4),
        "item_id_pct": round(item_id_pct, 2),
        "model_pct": round(model_pct, 2),
        "model_item_pct": round(model_item_pct, 2),
        "G_item": round(g_item, 4),
        "total_variance": round(total_var, 8),
        "variance_components": vc_detail,
        "n_levels": {k: int(v) for k, v in n_levels.items()},
    }


def main():
    data_path = "./results/analysis/cross_model_4way_bf16.csv"
    output_path = "./results/analysis/within_mmlu_subject_gradient.json"

    df = pd.read_csv(data_path)
    print(f"Loaded {len(df)} observations")

    subjects = sorted(df["subject"].unique())
    print(f"Subjects: {subjects}")

    results_by_subject = {}
    for subj in subjects:
        df_subj = df[df["subject"] == subj].copy()
        print(f"\n--- {subj} ({len(df_subj)} obs) ---")
        result = analyze_subject(df_subj, subj)
        results_by_subject[subj] = result
        print(f"  acc={result['accuracy']:.3f}  item_id={result['item_id_pct']:.1f}%  "
              f"model×item={result['model_item_pct']:.1f}%  model={result['model_pct']:.1f}%  "
              f"G={result['G_item']:.4f}")

    # Correlation analysis
    accs = [results_by_subject[s]["accuracy"] for s in subjects]
    item_pcts = [results_by_subject[s]["item_id_pct"] for s in subjects]
    model_item_pcts = [results_by_subject[s]["model_item_pct"] for s in subjects]
    model_pcts = [results_by_subject[s]["model_pct"] for s in subjects]
    g_items = [results_by_subject[s]["G_item"] for s in subjects]

    r_acc_item, p_acc_item = stats.pearsonr(accs, item_pcts)
    r_acc_model_item, p_acc_model_item = stats.pearsonr(accs, model_item_pcts)
    r_acc_model, p_acc_model = stats.pearsonr(accs, model_pcts)
    r_acc_g, p_acc_g = stats.pearsonr(accs, g_items)

    # Also Spearman for robustness with small N
    rs_acc_item, ps_acc_item = stats.spearmanr(accs, item_pcts)
    rs_acc_model_item, ps_acc_model_item = stats.spearmanr(accs, model_item_pcts)

    # Range and CV for gradient strength
    item_pct_range = max(item_pcts) - min(item_pcts)
    item_pct_cv = np.std(item_pcts) / np.mean(item_pcts) if np.mean(item_pcts) > 0 else 0

    # Determine gradient
    gradient_exists = (item_pct_range > 10) or (abs(r_acc_item) > 0.5)

    # Conclusion
    direction = "positive" if r_acc_item > 0 else "negative"
    conclusion_parts = []
    conclusion_parts.append(
        f"item_id variance share ranges from {min(item_pcts):.1f}% to {max(item_pcts):.1f}% "
        f"across 10 MMLU subjects (CV={item_pct_cv:.2f})."
    )
    conclusion_parts.append(
        f"Pearson r(accuracy, item_id%)={r_acc_item:.3f} (p={p_acc_item:.3f}), "
        f"Spearman rho={rs_acc_item:.3f} (p={ps_acc_item:.3f})."
    )
    if gradient_exists:
        conclusion_parts.append(
            f"A clear gradient exists: subjects with {'higher' if r_acc_item > 0 else 'lower'} "
            f"accuracy tend to have {'higher' if r_acc_item > 0 else 'lower'} item_id dominance."
        )
    else:
        conclusion_parts.append("No strong gradient between subject accuracy and item_id dominance.")

    conclusion_parts.append(
        f"model×item interaction ranges from {min(model_item_pcts):.1f}% to {max(model_item_pcts):.1f}%, "
        f"r(accuracy, model×item%)={r_acc_model_item:.3f} (p={p_acc_model_item:.3f})."
    )

    output = {
        "description": "Within-MMLU subject gradient: 7-facet Henderson I G-study per subject on 4-model balanced bf16 data",
        "data_source": "cross_model_4way_bf16.csv",
        "facets": ALL_FACETS,
        "n_subjects": len(subjects),
        "subjects": results_by_subject,
        "correlations": {
            "pearson_accuracy_vs_item_id": {"r": round(r_acc_item, 4), "p": round(p_acc_item, 4)},
            "pearson_accuracy_vs_model_item": {"r": round(r_acc_model_item, 4), "p": round(p_acc_model_item, 4)},
            "pearson_accuracy_vs_model": {"r": round(r_acc_model, 4), "p": round(p_acc_model, 4)},
            "pearson_accuracy_vs_G_item": {"r": round(r_acc_g, 4), "p": round(p_acc_g, 4)},
            "spearman_accuracy_vs_item_id": {"rho": round(rs_acc_item, 4), "p": round(ps_acc_item, 4)},
            "spearman_accuracy_vs_model_item": {"rho": round(rs_acc_model_item, 4), "p": round(ps_acc_model_item, 4)},
        },
        "gradient_summary": {
            "item_id_pct_range": round(item_pct_range, 2),
            "item_id_pct_mean": round(np.mean(item_pcts), 2),
            "item_id_pct_std": round(np.std(item_pcts), 2),
            "item_id_pct_cv": round(item_pct_cv, 3),
            "model_item_pct_range": round(max(model_item_pcts) - min(model_item_pcts), 2),
        },
        "gradient_exists": bool(gradient_exists),
        "conclusion": " ".join(conclusion_parts),
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n{'='*70}")
    print("SUMMARY: Subject Gradient")
    print(f"{'='*70}")
    print(f"{'Subject':<28} {'Acc':>6} {'item_id%':>9} {'m×item%':>8} {'model%':>7} {'G':>7}")
    print("-" * 70)
    for s in sorted(subjects, key=lambda x: results_by_subject[x]["accuracy"]):
        r = results_by_subject[s]
        print(f"{s:<28} {r['accuracy']:>6.3f} {r['item_id_pct']:>8.1f}% {r['model_item_pct']:>7.1f}% {r['model_pct']:>6.1f}% {r['G_item']:>7.4f}")
    print(f"\nCorr(acc, item_id%): Pearson r={r_acc_item:.3f} p={p_acc_item:.3f} | Spearman rho={rs_acc_item:.3f} p={ps_acc_item:.3f}")
    print(f"Corr(acc, model×item%): Pearson r={r_acc_model_item:.3f} p={p_acc_model_item:.3f}")
    print(f"Gradient exists: {gradient_exists}")
    print(f"\n-> {output_path}")


if __name__ == "__main__":
    main()

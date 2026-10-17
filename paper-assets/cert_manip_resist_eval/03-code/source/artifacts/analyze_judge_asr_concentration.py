#!/usr/bin/env python3
"""Per-judge ASR concentration analysis (plan_006).

For each panel×attack condition, computes per-judge ASR within the panel,
then quantifies concentration via Gini coefficient and normalized Shannon
entropy.  Tests whether high-K_eff panels show more dispersed attack
success (high entropy / low Gini).
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import time
import itertools
import numpy as np
from pathlib import Path
from scipy import stats as sp_stats

from src.utils import setup_logging
from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)

logger = setup_logging("judge_asr_concentration")

EPS = 1e-12


def _json_default(obj):
    if isinstance(obj, np.floating):
        v = float(obj)
        return None if (np.isnan(v) or np.isinf(v)) else v
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, np.bool_):
        return bool(obj)
    raise TypeError(f"Not JSON serializable: {type(obj)}")


def compute_individual_asr(clean_list, attacked_list, pairs):
    """Flip rate: fraction of clean-correct items flipped by attack."""
    n = min(len(clean_list), len(attacked_list), len(pairs))
    n_flips = n_correct = 0
    for i in range(n):
        if not _is_valid_score(clean_list[i]) or not _is_valid_score(attacked_list[i]):
            continue
        gt = pairs[i]["ground_truth_winner"]
        if clean_list[i]["winner"] == gt:
            n_correct += 1
            if attacked_list[i]["winner"] != gt:
                n_flips += 1
    return n_flips / max(n_correct, 1)


def mi_based_keff(mi_matrix, model_indices):
    K = len(model_indices)
    if K <= 1:
        return 1.0
    keff = 0.0
    for i_idx in model_indices:
        term = 1.0
        for j_idx in model_indices:
            if i_idx != j_idx:
                term += np.exp(-2 * mi_matrix[i_idx, j_idx])
        keff += term
    return keff / K


def gini_coefficient(values):
    """Gini coefficient of a non-negative array."""
    v = np.array(values, dtype=float)
    if len(v) < 2 or v.sum() < EPS:
        return 0.0
    v = np.sort(v)
    n = len(v)
    idx = np.arange(1, n + 1)
    return float((2.0 * np.sum(idx * v) - (n + 1) * np.sum(v)) / (n * np.sum(v)))


def normalized_entropy(values):
    """Normalized Shannon entropy (0=concentrated, 1=uniform)."""
    v = np.array(values, dtype=float)
    s = v.sum()
    if s < EPS or len(v) < 2:
        return 0.0
    p = v / s
    p = p[p > 0]
    h = -np.sum(p * np.log(p))
    h_max = np.log(len(values))
    if h_max < EPS:
        return 0.0
    return float(h / h_max)


def analyze_k(K, all_combos, mi_matrices, ind_asr, clean, attacked, pairs):
    """Compute Gini/entropy for all panels at panel size K, per condition."""
    logger.info(f"\n{'='*60}")
    logger.info(f"K={K}: {len(all_combos)} panels × 12 conditions")
    logger.info(f"{'='*60}")

    condition_results = {}

    for ds in DATASETS:
        mi_mat = np.array(mi_matrices[ds])
        for atk in ATTACKS:
            cond = f"{ds}×{atk}"
            t0 = time.time()

            ginis, entropies, keffs = [], [], []
            per_judge_asrs_all = []

            for combo in all_combos:
                jids = [ALL_MODELS[i] for i in combo]
                if not all((ds, atk, j) in ind_asr for j in jids):
                    continue

                keff = mi_based_keff(mi_mat, list(combo))
                judge_asrs = np.array([ind_asr[(ds, atk, j)] for j in jids])

                g = gini_coefficient(judge_asrs)
                h = normalized_entropy(judge_asrs)

                ginis.append(g)
                entropies.append(h)
                keffs.append(keff)
                per_judge_asrs_all.append(judge_asrs)

            ginis = np.array(ginis)
            entropies = np.array(entropies)
            keffs = np.array(keffs)
            n_panels = len(ginis)

            if n_panels < 10:
                logger.warning(f"  {cond}: only {n_panels} panels, skipping")
                continue

            # Correlations
            r_gini, p_gini = sp_stats.spearmanr(keffs, ginis)
            r_entropy, p_entropy = sp_stats.spearmanr(keffs, entropies)
            r_gini_p, p_gini_p = sp_stats.pearsonr(keffs, ginis)
            r_entropy_p, p_entropy_p = sp_stats.pearsonr(keffs, entropies)

            elapsed = time.time() - t0
            logger.info(
                f"  {cond}: n={n_panels} | "
                f"Gini={np.mean(ginis):.4f}±{np.std(ginis):.4f} | "
                f"Entropy={np.mean(entropies):.4f}±{np.std(entropies):.4f} | "
                f"ρ(K_eff,Gini)={r_gini:+.4f} (p={p_gini:.2e}) | "
                f"ρ(K_eff,Entropy)={r_entropy:+.4f} (p={p_entropy:.2e}) | "
                f"{elapsed:.1f}s"
            )

            # Per-judge ASR stats (across all panels)
            all_asrs = np.concatenate(per_judge_asrs_all)

            condition_results[cond] = {
                "n_panels": n_panels,
                "mean_gini": float(np.mean(ginis)),
                "std_gini": float(np.std(ginis)),
                "median_gini": float(np.median(ginis)),
                "mean_entropy": float(np.mean(entropies)),
                "std_entropy": float(np.std(entropies)),
                "median_entropy": float(np.median(entropies)),
                "spearman_keff_gini": float(r_gini),
                "p_keff_gini": float(p_gini),
                "spearman_keff_entropy": float(r_entropy),
                "p_keff_entropy": float(p_entropy),
                "pearson_keff_gini": float(r_gini_p),
                "p_pearson_keff_gini": float(p_gini_p),
                "pearson_keff_entropy": float(r_entropy_p),
                "p_pearson_keff_entropy": float(p_entropy_p),
                "keff_stats": {
                    "mean": float(np.mean(keffs)),
                    "std": float(np.std(keffs)),
                    "min": float(np.min(keffs)),
                    "max": float(np.max(keffs)),
                },
                "judge_asr_stats": {
                    "mean": float(np.mean(all_asrs)),
                    "std": float(np.std(all_asrs)),
                    "min": float(np.min(all_asrs)),
                    "max": float(np.max(all_asrs)),
                },
            }

    # Summary across conditions
    conds = list(condition_results.keys())
    n_sig_gini = sum(
        1 for c in conds
        if condition_results[c]["p_keff_gini"] < 0.05
    )
    n_sig_entropy = sum(
        1 for c in conds
        if condition_results[c]["p_keff_entropy"] < 0.05
    )
    # Hypothesis direction: high K_eff → low Gini (negative corr)
    n_correct_dir_gini = sum(
        1 for c in conds
        if condition_results[c]["spearman_keff_gini"] < 0
        and condition_results[c]["p_keff_gini"] < 0.05
    )
    # Hypothesis direction: high K_eff → high Entropy (positive corr)
    n_correct_dir_entropy = sum(
        1 for c in conds
        if condition_results[c]["spearman_keff_entropy"] > 0
        and condition_results[c]["p_keff_entropy"] < 0.05
    )

    summary = {
        "K": K,
        "n_panels": len(all_combos),
        "mean_gini": float(np.mean([condition_results[c]["mean_gini"] for c in conds])),
        "mean_entropy": float(np.mean([condition_results[c]["mean_entropy"] for c in conds])),
        "n_sig_gini": f"{n_sig_gini}/{len(conds)}",
        "n_sig_entropy": f"{n_sig_entropy}/{len(conds)}",
        "n_correct_direction_gini": f"{n_correct_dir_gini}/{len(conds)}",
        "n_correct_direction_entropy": f"{n_correct_dir_entropy}/{len(conds)}",
    }

    logger.info(f"\nK={K} SUMMARY:")
    logger.info(f"  Mean Gini:    {summary['mean_gini']:.4f}")
    logger.info(f"  Mean Entropy: {summary['mean_entropy']:.4f}")
    logger.info(f"  Sig Gini:     {summary['n_sig_gini']}")
    logger.info(f"  Sig Entropy:  {summary['n_sig_entropy']}")
    logger.info(f"  Correct dir (K_eff↑→Gini↓): {summary['n_correct_direction_gini']}")
    logger.info(f"  Correct dir (K_eff↑→Entropy↑): {summary['n_correct_direction_entropy']}")

    return condition_results, summary


def main():
    logger.info("=" * 60)
    logger.info("Per-judge ASR Concentration Analysis (plan_006)")
    logger.info("=" * 60)

    # Load data
    mi_data = load_mi_data()
    mi_matrices = mi_data["mi_matrix"]
    pairs = load_pairs()
    clean, attacked = load_all_scores()

    # Compute individual ASR for all judge×condition combos
    logger.info("\nComputing individual ASR...")
    ind_asr = {}
    for ds in DATASETS:
        for atk in ATTACKS:
            for mid in ALL_MODELS:
                if mid in clean[ds] and mid in attacked[ds][atk]:
                    ind_asr[(ds, atk, mid)] = compute_individual_asr(
                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]
                    )
    logger.info(f"  Computed {len(ind_asr)} individual ASR values")

    # Log individual ASR summary per condition
    logger.info("\nIndividual ASR overview:")
    for ds in DATASETS:
        for atk in ATTACKS:
            asrs = [ind_asr[(ds, atk, m)] for m in ALL_MODELS if (ds, atk, m) in ind_asr]
            if asrs:
                logger.info(
                    f"  {ds}×{atk}: n={len(asrs)} judges, "
                    f"mean={np.mean(asrs):.4f}, std={np.std(asrs):.4f}, "
                    f"min={np.min(asrs):.4f}, max={np.max(asrs):.4f}"
                )

    # Run analysis for K=3, 5, 7
    all_results = {}
    all_summaries = {}

    for K in [3, 5, 7]:
        combos = list(itertools.combinations(range(len(ALL_MODELS)), K))
        logger.info(f"\nK={K}: C(15,{K}) = {len(combos)} panels")
        t0 = time.time()
        cond_results, summary = analyze_k(
            K, combos, mi_matrices, ind_asr, clean, attacked, pairs
        )
        all_results[f"K{K}"] = cond_results
        all_summaries[f"K{K}"] = summary
        logger.info(f"K={K} completed in {time.time() - t0:.0f}s")

    # Cross-K trend analysis
    logger.info(f"\n{'='*80}")
    logger.info("CROSS-K TREND")
    logger.info(f"{'='*80}")
    logger.info(f"{'K':<5} {'Mean Gini':>12} {'Mean Entropy':>14} "
                f"{'Sig Gini':>12} {'Sig Entropy':>14} "
                f"{'Dir Gini':>12} {'Dir Entropy':>14}")
    logger.info("-" * 85)
    for k_label in ["K3", "K5", "K7"]:
        s = all_summaries[k_label]
        logger.info(
            f"{s['K']:<5} {s['mean_gini']:>12.4f} {s['mean_entropy']:>14.4f} "
            f"{s['n_sig_gini']:>12} {s['n_sig_entropy']:>14} "
            f"{s['n_correct_direction_gini']:>12} {s['n_correct_direction_entropy']:>14}"
        )

    # Hypothesis test conclusion
    hypothesis_lines = []
    for k_label in ["K3", "K5", "K7"]:
        s = all_summaries[k_label]
        hypothesis_lines.append(
            f"K={s['K']}: Gini sig {s['n_sig_gini']} (correct dir {s['n_correct_direction_gini']}), "
            f"Entropy sig {s['n_sig_entropy']} (correct dir {s['n_correct_direction_entropy']})"
        )

    # Check overall: does high K_eff → dispersed ASR?
    all_corr_gini = []
    all_corr_entropy = []
    for k_label in ["K3", "K5", "K7"]:
        for cond, cr in all_results[k_label].items():
            all_corr_gini.append(cr["spearman_keff_gini"])
            all_corr_entropy.append(cr["spearman_keff_entropy"])

    median_gini_corr = np.median(all_corr_gini)
    median_entropy_corr = np.median(all_corr_entropy)

    if median_gini_corr < 0 and median_entropy_corr > 0:
        conclusion = (
            f"SUPPORTED: High K_eff panels show lower Gini (median ρ={median_gini_corr:.4f}) "
            f"and higher entropy (median ρ={median_entropy_corr:.4f}), "
            f"indicating more dispersed attack success across judges."
        )
    elif median_gini_corr < 0 or median_entropy_corr > 0:
        conclusion = (
            f"PARTIALLY SUPPORTED: Gini median ρ={median_gini_corr:.4f}, "
            f"Entropy median ρ={median_entropy_corr:.4f}. "
            f"Only one indicator aligns with the hypothesis."
        )
    else:
        conclusion = (
            f"NOT SUPPORTED: Gini median ρ={median_gini_corr:.4f}, "
            f"Entropy median ρ={median_entropy_corr:.4f}. "
            f"High K_eff does not lead to more dispersed attack success."
        )

    logger.info(f"\nHYPOTHESIS: {conclusion}")

    # Build per-condition output (reorganized by condition)
    per_condition = {}
    for ds in DATASETS:
        for atk in ATTACKS:
            cond = f"{ds}×{atk}"
            per_condition[cond] = {}
            for k_label in ["K3", "K5", "K7"]:
                if cond in all_results[k_label]:
                    cr = all_results[k_label][cond]
                    per_condition[cond][k_label] = {
                        "mean_gini": cr["mean_gini"],
                        "std_gini": cr["std_gini"],
                        "mean_entropy": cr["mean_entropy"],
                        "std_entropy": cr["std_entropy"],
                        "spearman_keff_gini": cr["spearman_keff_gini"],
                        "p_keff_gini": cr["p_keff_gini"],
                        "spearman_keff_entropy": cr["spearman_keff_entropy"],
                        "p_keff_entropy": cr["p_keff_entropy"],
                        "n_panels": cr["n_panels"],
                    }

    # Individual ASR table
    ind_asr_table = {}
    for ds in DATASETS:
        for atk in ATTACKS:
            cond = f"{ds}×{atk}"
            ind_asr_table[cond] = {
                m: float(ind_asr[(ds, atk, m)])
                for m in ALL_MODELS if (ds, atk, m) in ind_asr
            }

    output = {
        "analysis": "judge_asr_concentration",
        "n_models": len(ALL_MODELS),
        "models": ALL_MODELS,
        "per_condition": per_condition,
        "summary": all_summaries,
        "hypothesis_test": conclusion,
        "hypothesis_detail": hypothesis_lines,
        "median_spearman_keff_gini": float(median_gini_corr),
        "median_spearman_keff_entropy": float(median_entropy_corr),
        "individual_asr": ind_asr_table,
    }

    out_path = Path("/root/cert_manip_resist_eval/artifacts/results/plan001/judge_asr_concentration.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
    logger.info(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

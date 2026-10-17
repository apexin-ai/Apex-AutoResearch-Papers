#!/usr/bin/env python3
"""K=5 and K=7 Panel Analysis: verify η_max dominance at larger panel sizes.

Constructs C(15,5)=3003 and C(15,7)=6435 panels, computes panel ASR via
majority vote, K_eff from pairwise MI matrix, and η_max from individual ASR.
Runs OLS + clustered SE regression for each of 12 conditions.

Output:
  - artifacts/results/plan001/k5_k7_panel_analysis.json
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import time
import itertools
import numpy as np
import statsmodels.api as sm
from pathlib import Path
from scipy.stats import t as t_dist
from statsmodels.stats.multitest import multipletests

from src.utils import setup_logging
from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)

logger = setup_logging("k5_k7_panel")

EPS = 1e-6
FDR_ALPHA = 0.05


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


def majority_vote(votes):
    counts = {"A": 0, "B": 0, "tie": 0}
    for v in votes:
        counts[v] = counts.get(v, 0) + 1
    mc = max(counts.values())
    winners = [k for k, c in counts.items() if c == mc]
    if len(winners) == 1:
        return winners[0]
    for w in winners:
        if w != "tie":
            return w
    return "tie"


def compute_individual_asr(clean_list, attacked_list, pairs):
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


def compute_panel_asr(jids, clean, attacked, pairs):
    n = min(len(pairs), *(len(clean[j]) for j in jids),
            *(len(attacked[j]) for j in jids))
    n_flips = n_correct = 0
    for i in range(n):
        if not all(_is_valid_score(clean[j][i]) for j in jids):
            continue
        if not all(_is_valid_score(attacked[j][i]) for j in jids):
            continue
        gt = pairs[i]["ground_truth_winner"]
        cv = majority_vote([clean[j][i]["winner"] for j in jids])
        if cv != gt:
            continue
        n_correct += 1
        av = majority_vote([attacked[j][i]["winner"] for j in jids])
        if av != gt:
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


def clustered_se_analysis(y, X_with_const, judge_ids_list, n_panels, K):
    """Compute max clustered SE across K judge positions."""
    fit_ols = sm.OLS(y, X_with_const).fit()
    n_coefs = X_with_const.shape[1]  # 3: intercept, log_keff, log_eta
    max_se = np.zeros(n_coefs)

    for k in range(K):
        cluster_var = np.array([jids[k] for jids in judge_ids_list])
        unique_judges = sorted(set(cluster_var))
        judge_to_int = {j: idx for idx, j in enumerate(unique_judges)}
        cluster_int = np.array([judge_to_int[j] for j in cluster_var])

        try:
            fit_cl = fit_ols.get_robustcov_results(
                cov_type='cluster', groups=cluster_int
            )
            for coef_idx in range(n_coefs):
                max_se[coef_idx] = max(max_se[coef_idx], fit_cl.bse[coef_idx])
        except Exception as e:
            logger.warning(f"  Clustering on position {k} failed: {e}")
            for coef_idx in range(n_coefs):
                max_se[coef_idx] = max(max_se[coef_idx], fit_ols.bse[coef_idx])

    df = n_panels - n_coefs
    params = fit_ols.params

    t_keff = params[1] / max_se[1] if max_se[1] > 0 else 0
    t_eta = params[2] / max_se[2] if max_se[2] > 0 else 0
    p_keff = float(2 * t_dist.sf(abs(t_keff), df))
    p_eta = float(2 * t_dist.sf(abs(t_eta), df))

    return {
        "params": params.tolist(),
        "ols_se": fit_ols.bse.tolist(),
        "max_clustered_se": max_se.tolist(),
        "se_inflation_keff": float(max_se[1] / fit_ols.bse[1]) if fit_ols.bse[1] > 0 else None,
        "se_inflation_eta": float(max_se[2] / fit_ols.bse[2]) if fit_ols.bse[2] > 0 else None,
        "t_keff": float(t_keff),
        "t_eta": float(t_eta),
        "p_keff": p_keff,
        "p_eta": p_eta,
    }


def analyze_panel_size(K, all_combos, mi_matrices, ind_asr, clean, attacked, pairs):
    """Run full analysis for a given panel size K."""
    logger.info(f"\n{'='*70}")
    logger.info(f"PANEL SIZE K={K}: {len(all_combos)} panels x 12 conditions")
    logger.info(f"{'='*70}")

    raw_ps = {
        "ols_eta": [], "ols_keff": [],
        "cl_eta": [], "cl_keff": [],
    }
    valid_keys = []
    condition_results = {}

    for ds in DATASETS:
        mi_mat = np.array(mi_matrices[ds])
        for atk in ATTACKS:
            cond = f"{ds}x{atk}"
            t0 = time.time()

            p_asrs, p_keffs, p_etas = [], [], []
            panel_judge_ids = []
            skipped = 0

            for combo in all_combos:
                jids = [ALL_MODELS[i] for i in combo]
                if not all((ds, atk, j) in ind_asr for j in jids):
                    skipped += 1
                    continue

                keff = mi_based_keff(mi_mat, list(combo))
                etas = [ind_asr[(ds, atk, j)] for j in jids]
                eta_max = max(etas)

                cs = {j: clean[ds][j] for j in jids}
                ats = {j: attacked[ds][atk][j] for j in jids}
                p_asr = compute_panel_asr(jids, cs, ats, pairs[ds])

                p_asrs.append(p_asr)
                p_keffs.append(keff)
                p_etas.append(eta_max)
                panel_judge_ids.append(jids)

            n_panels = len(p_asrs)
            elapsed = time.time() - t0
            logger.info(f"\n--- {cond} --- {n_panels} panels, {skipped} skipped ({elapsed:.1f}s)")

            if n_panels < 10:
                logger.warning(f"  Too few panels, skipping")
                continue

            p_asrs = np.array(p_asrs)
            p_keffs = np.array(p_keffs)
            p_etas = np.array(p_etas)

            if np.std(p_asrs) < 1e-10:
                logger.warning(f"  Constant ASR ({p_asrs[0]:.4f}), skipping")
                continue

            # OLS
            log_keff = np.log(p_keffs)
            log_eta = np.log(p_etas + EPS)
            y = np.log(p_asrs + EPS)

            X = np.column_stack([log_keff, log_eta])
            Xc = sm.add_constant(X)
            fit_ols = sm.OLS(y, Xc).fit()

            ols_p_keff = float(fit_ols.pvalues[1])
            ols_p_eta = float(fit_ols.pvalues[2])
            ols_beta_keff = float(fit_ols.params[1])
            ols_beta_eta = float(fit_ols.params[2])

            # Standardized β
            sd_y = np.std(y)
            keff_std_beta = float(fit_ols.params[1] * np.std(log_keff) / sd_y) if sd_y > 1e-12 else 0.0
            eta_std_beta = float(fit_ols.params[2] * np.std(log_eta) / sd_y) if sd_y > 1e-12 else 0.0

            logger.info(
                f"  OLS: β_keff={ols_beta_keff:+.4f} (p={ols_p_keff:.2e}), "
                f"β_eta={ols_beta_eta:+.4f} (p={ols_p_eta:.2e}), "
                f"R²={fit_ols.rsquared:.4f}"
            )
            logger.info(
                f"  Std β: K_eff={keff_std_beta:+.4f}, η_max={eta_std_beta:+.4f}"
            )

            # Clustered SE
            cl_result = clustered_se_analysis(y, Xc, panel_judge_ids, n_panels, K)
            logger.info(
                f"  Clustered: SE inflation keff={cl_result['se_inflation_keff']:.2f}x, "
                f"eta={cl_result['se_inflation_eta']:.2f}x | "
                f"p_keff={cl_result['p_keff']:.2e}, p_eta={cl_result['p_eta']:.2e}"
            )

            raw_ps["ols_eta"].append(ols_p_eta)
            raw_ps["ols_keff"].append(ols_p_keff)
            raw_ps["cl_eta"].append(cl_result["p_eta"])
            raw_ps["cl_keff"].append(cl_result["p_keff"])
            valid_keys.append(cond)

            condition_results[cond] = {
                "n_panels": n_panels,
                "ols": {
                    "beta_keff": ols_beta_keff,
                    "beta_eta": ols_beta_eta,
                    "p_keff": ols_p_keff,
                    "p_eta": ols_p_eta,
                    "R2": float(fit_ols.rsquared),
                    "se_keff": float(fit_ols.bse[1]),
                    "se_eta": float(fit_ols.bse[2]),
                    "keff_std_beta": keff_std_beta,
                    "eta_std_beta": eta_std_beta,
                },
                "clustered": cl_result,
                "asr_stats": {
                    "mean": float(np.mean(p_asrs)),
                    "std": float(np.std(p_asrs)),
                    "min": float(np.min(p_asrs)),
                    "max": float(np.max(p_asrs)),
                    "pct_zero": float(np.mean(p_asrs == 0)),
                },
                "keff_stats": {
                    "mean": float(np.mean(p_keffs)),
                    "std": float(np.std(p_keffs)),
                    "min": float(np.min(p_keffs)),
                    "max": float(np.max(p_keffs)),
                },
                "eta_stats": {
                    "mean": float(np.mean(p_etas)),
                    "std": float(np.std(p_etas)),
                },
            }

    # FDR correction
    fdr_results = {}
    for method in ["ols", "cl"]:
        for var in ["eta", "keff"]:
            key = f"{method}_{var}"
            pvals = raw_ps[key]
            if len(pvals) > 0:
                _, fdr_p, _, _ = multipletests(pvals, method="fdr_bh")
                fdr_results[key] = fdr_p.tolist()
            else:
                fdr_results[key] = []

    for i, ck in enumerate(valid_keys):
        cd = condition_results[ck]
        cd["ols"]["fdr_p_keff"] = fdr_results["ols_keff"][i]
        cd["ols"]["fdr_p_eta"] = fdr_results["ols_eta"][i]
        cd["clustered"]["fdr_p_keff"] = fdr_results["cl_keff"][i]
        cd["clustered"]["fdr_p_eta"] = fdr_results["cl_eta"][i]

    # Summary
    summary = {"methods": {}}
    for method_name, prefix in [("OLS", "ols"), ("Clustered SE", "cl")]:
        eta_sig = sum(1 for p in fdr_results[f"{prefix}_eta"] if p < FDR_ALPHA)
        keff_sig = sum(1 for p in fdr_results[f"{prefix}_keff"] if p < FDR_ALPHA)
        keff_pos = sum(
            1 for i, ck in enumerate(valid_keys)
            if fdr_results[f"{prefix}_keff"][i] < FDR_ALPHA
            and condition_results[ck]["ols"]["beta_keff"] > 0
        )
        keff_neg = keff_sig - keff_pos
        summary["methods"][method_name] = {
            "eta_fdr_sig": eta_sig,
            "keff_fdr_sig": keff_sig,
            "keff_sig_positive": keff_pos,
            "keff_sig_negative": keff_neg,
        }

    # Log summary
    logger.info(f"\n{'='*80}")
    logger.info(f"K={K} SUMMARY: FDR-significant counts (/{len(valid_keys)})")
    logger.info(f"{'='*80}")
    for method_name, prefix in [("OLS", "ols"), ("Clustered SE", "cl")]:
        m = summary["methods"][method_name]
        logger.info(
            f"  {method_name:<20}: η_max {m['eta_fdr_sig']}/{len(valid_keys)} FDR sig | "
            f"K_eff {m['keff_fdr_sig']}/{len(valid_keys)} FDR sig "
            f"({m['keff_sig_positive']}+ / {m['keff_sig_negative']}-)"
        )

    return {
        "K": K,
        "n_panels": len(all_combos),
        "n_conditions": len(valid_keys),
        "conditions": condition_results,
        "summary": summary,
    }


def main():
    logger.info("=" * 70)
    logger.info("K=5 and K=7 Panel Analysis")
    logger.info("=" * 70)

    mi_data = load_mi_data()
    mi_matrices = mi_data["mi_matrix"]
    pairs = load_pairs()
    clean, attacked = load_all_scores()

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

    results = {}

    # K=5
    combos_5 = list(itertools.combinations(range(len(ALL_MODELS)), 5))
    logger.info(f"\nK=5: C(15,5) = {len(combos_5)} panels")
    t0 = time.time()
    results["K5"] = analyze_panel_size(5, combos_5, mi_matrices, ind_asr, clean, attacked, pairs)
    logger.info(f"K=5 completed in {time.time() - t0:.0f}s")

    # K=7
    combos_7 = list(itertools.combinations(range(len(ALL_MODELS)), 7))
    logger.info(f"\nK=7: C(15,7) = {len(combos_7)} panels")
    t0 = time.time()
    results["K7"] = analyze_panel_size(7, combos_7, mi_matrices, ind_asr, clean, attacked, pairs)
    logger.info(f"K=7 completed in {time.time() - t0:.0f}s")

    # Cross-K comparison table
    logger.info(f"\n{'='*100}")
    logger.info("CROSS-K COMPARISON TABLE")
    logger.info(f"{'='*100}")
    logger.info(
        f"{'Panel Size':<12} {'Method':<16} {'η_max FDR sig':>15} "
        f"{'K_eff FDR sig':>15} {'K_eff sig+':>12} {'K_eff sig-':>12}"
    )
    logger.info("-" * 85)
    # K=3 reference (hardcoded from prior analysis)
    logger.info(f"  {'K=3':<10} {'OLS':<16} {'11/12':>15} {'8/12':>15} {'7':>12} {'1':>12}")
    logger.info(f"  {'K=3':<10} {'Clustered SE':<16} {'8/12':>15} {'0/12':>15} {'0':>12} {'0':>12}")
    for k_label in ["K5", "K7"]:
        k_val = results[k_label]["K"]
        n_cond = results[k_label]["n_conditions"]
        for method_name in ["OLS", "Clustered SE"]:
            m = results[k_label]["summary"]["methods"][method_name]
            logger.info(
                f"  {'K='+str(k_val):<10} {method_name:<16} "
                f"{str(m['eta_fdr_sig'])+'/'+str(n_cond):>15} "
                f"{str(m['keff_fdr_sig'])+'/'+str(n_cond):>15} "
                f"{str(m['keff_sig_positive']):>12} "
                f"{str(m['keff_sig_negative']):>12}"
            )

    # Save
    output = {
        "analysis": "k5_k7_panel_analysis",
        "n_models": len(ALL_MODELS),
        "models": ALL_MODELS,
        "fdr_alpha": FDR_ALPHA,
        "eps": EPS,
        "results": results,
    }

    out_dir = Path("/root/cert_manip_resist_eval/artifacts/results/plan001")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "k5_k7_panel_analysis.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
    logger.info(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

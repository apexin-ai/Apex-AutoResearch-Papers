#!/usr/bin/env python3
"""Crossed Random Effects robustness check via multi-membership clustered SE.

Addresses reviewer concern: judges appear across multiple panels (crossed
structure), so panel-level errors are correlated. Standard OLS SE ignores this.

Approach: OLS regression at the panel level with multi-membership cluster-robust
variance estimator (CRVE). For each judge, we sum the score contributions
(X_i * e_i) across all panels containing that judge, then form the sandwich
variance. This is equivalent to one-way clustering with overlapping clusters,
giving correctly conservative SE that accounts for shared-judge correlation.

Model: log(ASR+eps) ~ log(K_eff) + log(eta_max+eps), SE clustered by judge membership
Output: artifacts/results/plan001/crossed_re_results.json
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import logging
import itertools
import time
import numpy as np
import statsmodels.api as sm
from scipy import stats as scipy_stats
from pathlib import Path
from statsmodels.stats.multitest import multipletests

from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler("/tmp/crossed_re.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

EPS = 1e-6
ALPHA = 0.05
FDR_ALPHA = 0.05
PANEL_SIZES = [3, 5, 7]


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


def multi_membership_clustered_se(y, X, panel_jids, all_judges):
    """OLS + multi-membership cluster-robust SE.

    Each panel's residual contribution is allocated to all judges in that panel.
    The sandwich variance accounts for cross-panel correlation due to shared judges.
    """
    judge_to_idx = {j: i for i, j in enumerate(all_judges)}
    n_judges = len(all_judges)
    n, k = X.shape

    ols = sm.OLS(y, X).fit()
    e = ols.resid

    # Per-judge score: s_j = sum_{i: j in panel_i} X_i * e_i
    scores = np.zeros((n_judges, k))
    judges_used = set()
    for i in range(n):
        for jid in panel_jids[i]:
            if jid in judge_to_idx:
                j_idx = judge_to_idx[jid]
                scores[j_idx] += X[i] * e[i]
                judges_used.add(jid)

    n_clusters = len(judges_used)
    used_scores = scores[[judge_to_idx[j] for j in judges_used]]

    # HC1-like correction: n/(n-k) * G/(G-1)
    correction = (n / (n - k)) * (n_clusters / max(n_clusters - 1, 1))

    bread = np.linalg.inv(X.T @ X)
    meat = used_scores.T @ used_scores * correction
    V = bread @ meat @ bread
    se_mm = np.sqrt(np.diag(V))

    # t-test with df = G-1
    df = max(n_clusters - 1, 1)
    t_vals = ols.params / se_mm
    p_vals = 2 * scipy_stats.t.sf(np.abs(t_vals), df=df)

    return {
        "params": ols.params,
        "ols_se": ols.bse,
        "ols_pvalues": ols.pvalues,
        "mm_se": se_mm,
        "mm_tvalues": t_vals,
        "mm_pvalues": p_vals,
        "n_panels": n,
        "n_judges_used": n_clusters,
        "df": df,
        "R2": float(ols.rsquared),
        "se_inflation_keff": float(se_mm[1] / ols.bse[1]),
        "se_inflation_eta": float(se_mm[2] / ols.bse[2]),
    }


def main():
    logger.info("=" * 70)
    logger.info("Crossed Random Effects Analysis (Multi-Membership Clustered SE)")
    logger.info("=" * 70)

    logger.info("Loading data...")
    clean, attacked = load_all_scores()
    pairs = load_pairs()
    mi_data = load_mi_data()
    mi_matrices = mi_data["mi_matrix"]
    keff_precomputed = mi_data.get("keff_per_panel", {})

    logger.info("Computing individual ASR...")
    ind_asr = {}
    for ds in DATASETS:
        for atk in ATTACKS:
            for mid in ALL_MODELS:
                if mid in clean[ds] and mid in attacked[ds][atk]:
                    ind_asr[(ds, atk, mid)] = compute_individual_asr(
                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]
                    )
    logger.info(f"  {len(ind_asr)} individual ASR values")

    bootstrap_ref = {
        "K3_keff": "4/12",
        "K5_keff": "7/12",
        "K7_keff": "8/12",
    }

    all_results = {}

    for K in PANEL_SIZES:
        logger.info(f"\n{'='*70}")
        logger.info(f"PANEL SIZE K={K}")
        logger.info(f"{'='*70}")

        all_combos = list(itertools.combinations(range(len(ALL_MODELS)), K))
        logger.info(f"  C(15,{K}) = {len(all_combos)} panels")

        condition_results = {}
        raw_keff_ps = []
        raw_eta_ps = []
        valid_conditions = []

        for ds in DATASETS:
            mi_mat = np.array(mi_matrices[ds])
            for atk in ATTACKS:
                cond = f"{ds}x{atk}"
                t0 = time.time()

                panel_y, panel_lk, panel_le = [], [], []
                panel_jids_list = []

                for combo in all_combos:
                    jids = [ALL_MODELS[i] for i in combo]
                    if not all((ds, atk, j) in ind_asr for j in jids):
                        continue

                    if K == 3:
                        pk = "|".join(jids)
                        keff_dict = keff_precomputed.get(ds, {}).get(pk)
                        keff = keff_dict["keff"] if keff_dict else mi_based_keff(mi_mat, list(combo))
                    else:
                        keff = mi_based_keff(mi_mat, list(combo))

                    eta_max = max(ind_asr[(ds, atk, j)] for j in jids)
                    cs = {j: clean[ds][j] for j in jids}
                    ats = {j: attacked[ds][atk][j] for j in jids}
                    asr = compute_panel_asr(jids, cs, ats, pairs[ds])

                    panel_y.append(np.log(asr + EPS))
                    panel_lk.append(np.log(keff))
                    panel_le.append(np.log(eta_max + EPS))
                    panel_jids_list.append(jids)

                n_panels = len(panel_y)
                elapsed_build = time.time() - t0

                if n_panels < 10:
                    logger.warning(f"  {cond}: {n_panels} panels, skipping")
                    condition_results[cond] = {"skipped": True, "n_panels": n_panels}
                    continue

                y = np.array(panel_y)
                X = np.column_stack([
                    np.ones(n_panels),
                    np.array(panel_lk),
                    np.array(panel_le),
                ])

                all_judges = sorted(set(
                    j for jids in panel_jids_list for j in jids
                ))

                t1 = time.time()
                result = multi_membership_clustered_se(
                    y, X, panel_jids_list, all_judges
                )
                elapsed_fit = time.time() - t1

                keff_coef = float(result["params"][1])
                keff_p = float(result["mm_pvalues"][1])
                eta_coef = float(result["params"][2])
                eta_p = float(result["mm_pvalues"][2])

                cond_result = {
                    "n_panels": n_panels,
                    "n_judges": result["n_judges_used"],
                    "df": result["df"],
                    "R2": result["R2"],
                    "keff_coef": keff_coef,
                    "keff_ols_se": float(result["ols_se"][1]),
                    "keff_mm_se": float(result["mm_se"][1]),
                    "keff_se_inflation": result["se_inflation_keff"],
                    "keff_ols_p": float(result["ols_pvalues"][1]),
                    "keff_p": keff_p,
                    "keff_sig": bool(keff_p < ALPHA),
                    "eta_coef": eta_coef,
                    "eta_ols_se": float(result["ols_se"][2]),
                    "eta_mm_se": float(result["mm_se"][2]),
                    "eta_se_inflation": result["se_inflation_eta"],
                    "eta_ols_p": float(result["ols_pvalues"][2]),
                    "eta_p": eta_p,
                    "eta_sig": bool(eta_p < ALPHA),
                }

                condition_results[cond] = cond_result

                logger.info(
                    f"  {cond}: {n_panels} panels, {result['n_judges_used']} judges | "
                    f"K_eff b={keff_coef:+.3f} SE={result['mm_se'][1]:.3f}"
                    f"({result['se_inflation_keff']:.2f}x) p={keff_p:.4e}"
                    f"{'*' if keff_p < ALPHA else ''} | "
                    f"eta b={eta_coef:+.3f} SE={result['mm_se'][2]:.3f}"
                    f"({result['se_inflation_eta']:.2f}x) p={eta_p:.4e}"
                    f"{'*' if eta_p < ALPHA else ''}"
                    f" ({elapsed_build:.1f}s+{elapsed_fit:.1f}s)"
                )

                raw_keff_ps.append(keff_p)
                raw_eta_ps.append(eta_p)
                valid_conditions.append(cond)

        # FDR correction
        n_valid = len(valid_conditions)
        if n_valid > 1:
            _, keff_fdr_ps, _, _ = multipletests(
                raw_keff_ps, alpha=FDR_ALPHA, method="fdr_bh"
            )
            _, eta_fdr_ps, _, _ = multipletests(
                raw_eta_ps, alpha=FDR_ALPHA, method="fdr_bh"
            )
            for i, cond in enumerate(valid_conditions):
                condition_results[cond]["keff_fdr_p"] = float(keff_fdr_ps[i])
                condition_results[cond]["keff_fdr_sig"] = bool(keff_fdr_ps[i] < FDR_ALPHA)
                condition_results[cond]["eta_fdr_p"] = float(eta_fdr_ps[i])
                condition_results[cond]["eta_fdr_sig"] = bool(eta_fdr_ps[i] < FDR_ALPHA)
        elif n_valid == 1:
            cond = valid_conditions[0]
            condition_results[cond]["keff_fdr_p"] = raw_keff_ps[0]
            condition_results[cond]["keff_fdr_sig"] = bool(raw_keff_ps[0] < FDR_ALPHA)
            condition_results[cond]["eta_fdr_p"] = raw_eta_ps[0]
            condition_results[cond]["eta_fdr_sig"] = bool(raw_eta_ps[0] < FDR_ALPHA)

        keff_fdr_sig = sum(
            1 for c in valid_conditions
            if condition_results[c].get("keff_fdr_sig", False)
        )
        eta_fdr_sig = sum(
            1 for c in valid_conditions
            if condition_results[c].get("eta_fdr_sig", False)
        )
        keff_raw_sig = sum(
            1 for c in valid_conditions
            if condition_results[c].get("keff_sig", False)
        )
        eta_raw_sig = sum(
            1 for c in valid_conditions
            if condition_results[c].get("eta_sig", False)
        )

        k_label = f"K{K}"
        all_results[k_label] = {
            "K": K,
            "n_panels": len(all_combos),
            "n_conditions": n_valid,
            "per_condition": condition_results,
            "summary": {
                "keff_sig_count": f"{keff_fdr_sig}/{n_valid}",
                "keff_raw_sig_count": f"{keff_raw_sig}/{n_valid}",
                "eta_sig_count": f"{eta_fdr_sig}/{n_valid}",
                "eta_raw_sig_count": f"{eta_raw_sig}/{n_valid}",
            },
        }

        logger.info(f"\nK={K} SUMMARY:")
        logger.info(f"  K_eff FDR sig: {keff_fdr_sig}/{n_valid}")
        logger.info(f"  K_eff raw sig: {keff_raw_sig}/{n_valid}")
        logger.info(f"  eta_max FDR sig: {eta_fdr_sig}/{n_valid}")
        logger.info(f"  eta_max raw sig: {eta_raw_sig}/{n_valid}")

    # Build comparison
    comparison = {}
    for k_label in ["K3", "K5", "K7"]:
        ref_key = f"{k_label}_keff"
        if ref_key in bootstrap_ref and k_label in all_results:
            comparison[ref_key] = {
                "bootstrap": bootstrap_ref[ref_key],
                "crossed_re": all_results[k_label]["summary"]["keff_sig_count"],
            }

    # Format results_by_condition
    results_by_condition = {}
    for k_label, k_data in all_results.items():
        for cond, cdata in k_data["per_condition"].items():
            key = f"{k_label}_{cond.replace('x', '_')}"
            if "keff_coef" in cdata:
                results_by_condition[key] = {
                    "keff_coef": cdata["keff_coef"],
                    "keff_se": cdata["keff_mm_se"],
                    "keff_p": cdata["keff_p"],
                    "keff_fdr_p": cdata.get("keff_fdr_p"),
                    "keff_sig": cdata.get("keff_fdr_sig", False),
                    "keff_se_inflation": cdata["keff_se_inflation"],
                    "eta_coef": cdata["eta_coef"],
                    "eta_se": cdata["eta_mm_se"],
                    "eta_p": cdata["eta_p"],
                    "eta_fdr_p": cdata.get("eta_fdr_p"),
                    "eta_sig": cdata.get("eta_fdr_sig", False),
                    "eta_se_inflation": cdata["eta_se_inflation"],
                    "n_panels": cdata["n_panels"],
                    "n_judges": cdata["n_judges"],
                    "df": cdata["df"],
                }
            elif cdata.get("skipped"):
                results_by_condition[key] = {"skipped": True}

    output = {
        "method": "crossed_random_effects",
        "implementation": "multi_membership_clustered_se",
        "package": "statsmodels OLS + custom CRVE",
        "model_formula": "log(ASR+eps) ~ log(K_eff) + log(eta_max+eps), SE clustered by judge membership",
        "note": "Panel-level OLS with multi-membership cluster-robust variance estimator. "
                "For each judge, score contributions (X_i * e_i) are summed across all panels "
                "containing that judge. Sandwich SE with HC1-like correction and t(G-1) distribution. "
                "Accounts for cross-panel correlation due to shared judges without data expansion.",
        "n_models": len(ALL_MODELS),
        "models": ALL_MODELS,
        "alpha": ALPHA,
        "fdr_alpha": FDR_ALPHA,
        "panel_sizes": PANEL_SIZES,
        "results_by_condition": results_by_condition,
        "summary": {
            k_label: all_results[k_label]["summary"]
            for k_label in all_results
        },
        "comparison_with_bootstrap": comparison,
    }

    out_path = Path("/root/cert_manip_resist_eval/artifacts/results/plan001/crossed_re_results.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
    logger.info(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

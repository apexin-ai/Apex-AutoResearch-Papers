#!/usr/bin/env python3
"""Clustered SE + Mixed-Effects robustness check for canonical OLS findings.

Addresses reviewer concern: each judge appears in 91/455 panels, so OLS
treats non-independent observations as independent, inflating p-values.

Three methods compared:
  1. Canonical OLS (baseline)
  2. Clustered SE (max over 3 single-way clusterings on judge positions)
  3. Mixed-Effects (max p-value over 3 models with random intercepts per judge)

Output:
  - artifacts/results/plan001/clustered_se_analysis.json
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import itertools
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
from pathlib import Path
from scipy import stats as scipy_stats
from scipy.stats import t as t_dist
from statsmodels.stats.multitest import multipletests

from src.utils import setup_logging
from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)

logger = setup_logging("clustered_se")

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


def clustered_se_analysis(y, X_with_const, judge_ids_list, n_panels):
    """Compute max clustered SE across 3 judge positions.

    Returns dict with coefficients, max SEs, t-stats, and p-values.
    """
    fit_ols = sm.OLS(y, X_with_const).fit()

    max_se = np.zeros(3)  # intercept, log_keff, log_eta

    for k in range(3):
        cluster_var = np.array([jids[k] for jids in judge_ids_list])
        unique_judges = sorted(set(cluster_var))
        judge_to_int = {j: idx for idx, j in enumerate(unique_judges)}
        cluster_int = np.array([judge_to_int[j] for j in cluster_var])

        try:
            fit_cl = fit_ols.get_robustcov_results(
                cov_type='cluster', groups=cluster_int
            )
            for coef_idx in range(3):
                max_se[coef_idx] = max(max_se[coef_idx], fit_cl.bse[coef_idx])
        except Exception as e:
            logger.warning(f"  Clustering on position {k} failed: {e}")
            for coef_idx in range(3):
                max_se[coef_idx] = max(max_se[coef_idx], fit_ols.bse[coef_idx])

    df = n_panels - 3
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


def mixed_effects_analysis(df_data):
    """Run mixed-effects models with random intercepts for each judge position.

    Returns dict with max p-values (most conservative) across 3 models.
    """
    results_per_pos = []

    for judge_col in ['judge0', 'judge1', 'judge2']:
        try:
            md = smf.mixedlm(
                'log_asr ~ log_keff + log_eta',
                data=df_data,
                groups=df_data[judge_col],
            )
            mdf = md.fit(reml=True, method='lbfgs', maxiter=500)

            results_per_pos.append({
                "judge_col": judge_col,
                "converged": mdf.converged,
                "params": {
                    "Intercept": float(mdf.fe_params.get("Intercept", np.nan)),
                    "log_keff": float(mdf.fe_params.get("log_keff", np.nan)),
                    "log_eta": float(mdf.fe_params.get("log_eta", np.nan)),
                },
                "pvalues": {
                    "log_keff": float(mdf.pvalues.get("log_keff", 1.0)),
                    "log_eta": float(mdf.pvalues.get("log_eta", 1.0)),
                },
                "random_effect_var": float(mdf.cov_re.iloc[0, 0]) if hasattr(mdf, 'cov_re') and mdf.cov_re is not None else None,
            })
        except Exception as e:
            logger.warning(f"  MixedLM with {judge_col} failed: {e}")
            results_per_pos.append({
                "judge_col": judge_col,
                "converged": False,
                "error": str(e),
                "pvalues": {"log_keff": 1.0, "log_eta": 1.0},
            })

    # Take max p-value across the 3 models (most conservative)
    max_p_keff = max(r["pvalues"]["log_keff"] for r in results_per_pos)
    max_p_eta = max(r["pvalues"]["log_eta"] for r in results_per_pos)

    return {
        "per_position": results_per_pos,
        "max_p_keff": float(max_p_keff),
        "max_p_eta": float(max_p_eta),
    }


def main():
    logger.info("=" * 70)
    logger.info("Clustered SE + Mixed-Effects Robustness Analysis (15 models)")
    logger.info("=" * 70)

    mi_data = load_mi_data()
    pairs = load_pairs()
    clean, attacked = load_all_scores()

    # Precompute individual ASR
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

    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))
    logger.info(f"  Total panels: {len(all_combos)}")

    # Collect raw p-values for FDR across methods
    raw_ps = {
        "ols_eta": [], "ols_keff": [],
        "cl_eta": [], "cl_keff": [],
        "me_eta": [], "me_keff": [],
    }
    valid_keys = []
    condition_results = {}

    for ds in DATASETS:
        keff_data = mi_data["keff_per_panel"].get(ds, {})
        for atk in ATTACKS:
            cond = f"{ds}x{atk}"
            logger.info(f"\n--- {cond} ---")

            p_asrs, p_keffs, p_etas = [], [], []
            panel_judge_ids = []
            skipped = 0

            for combo in all_combos:
                jids = [ALL_MODELS[i] for i in combo]
                if not all((ds, atk, j) in ind_asr for j in jids):
                    skipped += 1
                    continue
                pk = "|".join(jids)
                if pk not in keff_data:
                    skipped += 1
                    continue

                keff = keff_data[pk]["keff"]
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
            logger.info(f"  {n_panels} panels, {skipped} skipped")

            if n_panels < 10:
                logger.warning(f"  Too few panels, skipping")
                continue

            p_asrs = np.array(p_asrs)
            p_keffs = np.array(p_keffs)
            p_etas = np.array(p_etas)

            if np.std(p_asrs) < 1e-10:
                logger.warning(f"  Constant ASR ({p_asrs[0]:.4f}), skipping")
                continue

            # ── Canonical OLS ──
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

            logger.info(
                f"  OLS: β_keff={ols_beta_keff:+.4f} (p={ols_p_keff:.2e}), "
                f"β_eta={ols_beta_eta:+.4f} (p={ols_p_eta:.2e}), "
                f"R²={fit_ols.rsquared:.4f}"
            )

            # ── Clustered SE ──
            cl_result = clustered_se_analysis(y, Xc, panel_judge_ids, n_panels)
            logger.info(
                f"  Clustered: SE inflation keff={cl_result['se_inflation_keff']:.2f}x, "
                f"eta={cl_result['se_inflation_eta']:.2f}x | "
                f"p_keff={cl_result['p_keff']:.2e}, p_eta={cl_result['p_eta']:.2e}"
            )

            # ── Mixed Effects ──
            df_me = pd.DataFrame({
                'log_asr': y,
                'log_keff': log_keff,
                'log_eta': log_eta,
                'judge0': [jids[0] for jids in panel_judge_ids],
                'judge1': [jids[1] for jids in panel_judge_ids],
                'judge2': [jids[2] for jids in panel_judge_ids],
            })
            me_result = mixed_effects_analysis(df_me)
            logger.info(
                f"  MixedLM: max_p_keff={me_result['max_p_keff']:.2e}, "
                f"max_p_eta={me_result['max_p_eta']:.2e}"
            )

            # Collect
            raw_ps["ols_eta"].append(ols_p_eta)
            raw_ps["ols_keff"].append(ols_p_keff)
            raw_ps["cl_eta"].append(cl_result["p_eta"])
            raw_ps["cl_keff"].append(cl_result["p_keff"])
            raw_ps["me_eta"].append(me_result["max_p_eta"])
            raw_ps["me_keff"].append(me_result["max_p_keff"])
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
                },
                "clustered": cl_result,
                "mixed_effects": me_result,
            }

    # ── FDR correction ──
    logger.info(f"\n{'='*70}")
    logger.info(f"FDR correction (BH) across {len(valid_keys)} conditions")
    logger.info(f"{'='*70}")

    fdr_results = {}
    for method in ["ols", "cl", "me"]:
        for var in ["eta", "keff"]:
            key = f"{method}_{var}"
            pvals = raw_ps[key]
            if len(pvals) > 0:
                _, fdr_p, _, _ = multipletests(pvals, method="fdr_bh")
                fdr_results[key] = fdr_p.tolist()
            else:
                fdr_results[key] = []

    # Attach FDR p-values
    for i, ck in enumerate(valid_keys):
        cd = condition_results[ck]
        cd["ols"]["fdr_p_keff"] = fdr_results["ols_keff"][i]
        cd["ols"]["fdr_p_eta"] = fdr_results["ols_eta"][i]
        cd["clustered"]["fdr_p_keff"] = fdr_results["cl_keff"][i]
        cd["clustered"]["fdr_p_eta"] = fdr_results["cl_eta"][i]
        cd["mixed_effects"]["fdr_p_keff"] = fdr_results["me_keff"][i]
        cd["mixed_effects"]["fdr_p_eta"] = fdr_results["me_eta"][i]

    # ── Summary table ──
    logger.info(f"\n{'='*140}")
    logger.info("COMPARISON TABLE: OLS vs Clustered SE vs Mixed Effects")
    logger.info(f"{'='*140}")
    hdr = (
        f"{'Condition':<28} | "
        f"{'OLS p_η':>10} {'FDR':>6} {'OLS p_K':>10} {'FDR':>6} | "
        f"{'CL p_η':>10} {'FDR':>6} {'CL p_K':>10} {'FDR':>6} | "
        f"{'ME p_η':>10} {'FDR':>6} {'ME p_K':>10} {'FDR':>6}"
    )
    logger.info(hdr)
    logger.info("-" * 140)

    for ck in valid_keys:
        cd = condition_results[ck]
        o, c, m = cd["ols"], cd["clustered"], cd["mixed_effects"]

        def sig(p):
            return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"

        logger.info(
            f"  {ck:<26} | "
            f"{o['p_eta']:>10.2e} {sig(o['fdr_p_eta']):>5} {o['p_keff']:>10.2e} {sig(o['fdr_p_keff']):>5} | "
            f"{c['p_eta']:>10.2e} {sig(c['fdr_p_eta']):>5} {c['p_keff']:>10.2e} {sig(c['fdr_p_keff']):>5} | "
            f"{m['max_p_eta']:>10.2e} {sig(m['fdr_p_eta']):>5} {m['max_p_keff']:>10.2e} {sig(m['fdr_p_keff']):>5}"
        )

    # ── Summary counts ──
    logger.info(f"\n{'='*80}")
    logger.info("SUMMARY: FDR-significant counts (/12)")
    logger.info(f"{'='*80}")

    methods = [
        ("Canonical OLS", "ols"),
        ("Clustered SE (max)", "cl"),
        ("Mixed Effects (max)", "me"),
    ]

    for method_name, prefix in methods:
        eta_sig = sum(1 for p in fdr_results[f"{prefix}_eta"] if p < FDR_ALPHA)
        keff_sig = sum(1 for p in fdr_results[f"{prefix}_keff"] if p < FDR_ALPHA)

        # Count K_eff positive vs negative among significant
        keff_pos = 0
        keff_neg = 0
        for i, ck in enumerate(valid_keys):
            if fdr_results[f"{prefix}_keff"][i] < FDR_ALPHA:
                beta_k = condition_results[ck]["ols"]["beta_keff"]
                if beta_k > 0:
                    keff_pos += 1
                else:
                    keff_neg += 1

        logger.info(
            f"  {method_name:<25}: η_max {eta_sig}/12 FDR sig | "
            f"K_eff {keff_sig}/12 FDR sig ({keff_pos}+ / {keff_neg}-)"
        )

    # ── SE inflation summary ──
    logger.info(f"\n{'='*80}")
    logger.info("SE INFLATION (Clustered / OLS)")
    logger.info(f"{'='*80}")
    inflations_keff = []
    inflations_eta = []
    for ck in valid_keys:
        cl = condition_results[ck]["clustered"]
        if cl["se_inflation_keff"] is not None:
            inflations_keff.append(cl["se_inflation_keff"])
        if cl["se_inflation_eta"] is not None:
            inflations_eta.append(cl["se_inflation_eta"])

    if inflations_keff:
        logger.info(
            f"  K_eff SE inflation: mean={np.mean(inflations_keff):.2f}x, "
            f"range=[{min(inflations_keff):.2f}x, {max(inflations_keff):.2f}x]"
        )
    if inflations_eta:
        logger.info(
            f"  η_max SE inflation: mean={np.mean(inflations_eta):.2f}x, "
            f"range=[{min(inflations_eta):.2f}x, {max(inflations_eta):.2f}x]"
        )

    # ── Save JSON ──
    output = {
        "analysis": "clustered_se_mixed_effects_robustness",
        "n_models": len(ALL_MODELS),
        "models": ALL_MODELS,
        "fdr_alpha": FDR_ALPHA,
        "eps": EPS,
        "n_conditions": len(valid_keys),
        "conditions": condition_results,
        "summary": {
            "methods": {},
            "se_inflation": {
                "keff_mean": float(np.mean(inflations_keff)) if inflations_keff else None,
                "keff_range": [float(min(inflations_keff)), float(max(inflations_keff))] if inflations_keff else None,
                "eta_mean": float(np.mean(inflations_eta)) if inflations_eta else None,
                "eta_range": [float(min(inflations_eta)), float(max(inflations_eta))] if inflations_eta else None,
            },
        },
    }

    for method_name, prefix in methods:
        eta_sig = sum(1 for p in fdr_results[f"{prefix}_eta"] if p < FDR_ALPHA)
        keff_sig = sum(1 for p in fdr_results[f"{prefix}_keff"] if p < FDR_ALPHA)
        keff_pos = sum(
            1 for i, ck in enumerate(valid_keys)
            if fdr_results[f"{prefix}_keff"][i] < FDR_ALPHA
            and condition_results[ck]["ols"]["beta_keff"] > 0
        )
        keff_neg = keff_sig - keff_pos
        output["summary"]["methods"][method_name] = {
            "eta_fdr_sig": eta_sig,
            "keff_fdr_sig": keff_sig,
            "keff_sig_positive": keff_pos,
            "keff_sig_negative": keff_neg,
        }

    out_dir = Path("/root/cert_manip_resist_eval/artifacts/results/plan001")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "clustered_se_analysis.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
    logger.info(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

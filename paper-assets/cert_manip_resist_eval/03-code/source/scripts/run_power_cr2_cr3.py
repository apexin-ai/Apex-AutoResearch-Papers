#!/usr/bin/env python3
"""Power Analysis + CR2/CR3 small-sample correction for clustered SE.

Part A: Monte Carlo power analysis to find MDE at 80% power.
Part B: CR1 vs CR2 vs CR3 sandwich estimator comparison across 12 conditions.
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import itertools
import numpy as np
import statsmodels.api as sm
import pandas as pd
from pathlib import Path
from scipy.stats import t as t_dist
from scipy.interpolate import interp1d
from statsmodels.stats.multitest import multipletests

from src.utils import setup_logging
from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)

logger = setup_logging("power_cr2_cr3")

EPS = 1e-6
FDR_ALPHA = 0.05
N_SIM = 1000
BETA_STD_GRID = [0.1, 0.2, 0.3, 0.5]


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


# ── CR1: standard sandwich (max over 3 positions) ──

def cr1_clustered_se(y, Xc, judge_ids_list, n_panels):
    fit_ols = sm.OLS(y, Xc).fit()
    max_se = np.zeros(Xc.shape[1])
    for k in range(3):
        cluster_var = np.array([jids[k] for jids in judge_ids_list])
        unique = sorted(set(cluster_var))
        c2i = {j: idx for idx, j in enumerate(unique)}
        cint = np.array([c2i[j] for j in cluster_var])
        try:
            fit_cl = fit_ols.get_robustcov_results(cov_type='cluster', groups=cint)
            for ci in range(Xc.shape[1]):
                max_se[ci] = max(max_se[ci], fit_cl.bse[ci])
        except Exception:
            for ci in range(Xc.shape[1]):
                max_se[ci] = max(max_se[ci], fit_ols.bse[ci])
    return fit_ols.params, max_se


# ── CR2: bias-corrected sandwich ──

def _cr2_vcov_one_clustering(y, Xc, cluster_int):
    """CR2 (Bell-McCaffrey) sandwich estimator for one clustering."""
    n, p = Xc.shape
    fit = sm.OLS(y, Xc).fit()
    resid = fit.resid
    H = Xc @ np.linalg.inv(Xc.T @ Xc) @ Xc.T
    XtXinv = np.linalg.inv(Xc.T @ Xc)

    clusters = np.unique(cluster_int)
    G = len(clusters)
    meat = np.zeros((p, p))

    for c in clusters:
        idx = np.where(cluster_int == c)[0]
        Xc_g = Xc[idx]
        e_g = resid[idx]
        H_gg = H[np.ix_(idx, idx)]
        I_g = np.eye(len(idx))
        A_g = I_g - H_gg
        # CR2: use (I - H_gg)^{-1/2} to adjust residuals
        try:
            eigvals, eigvecs = np.linalg.eigh(A_g)
            eigvals = np.maximum(eigvals, 1e-10)
            A_g_inv_sqrt = eigvecs @ np.diag(1.0 / np.sqrt(eigvals)) @ eigvecs.T
            e_adj = A_g_inv_sqrt @ e_g
        except np.linalg.LinAlgError:
            e_adj = e_g / np.sqrt(np.maximum(1.0 - np.diag(H_gg), 1e-10))

        score_g = Xc_g.T @ e_adj
        meat += np.outer(score_g, score_g)

    vcov = XtXinv @ meat @ XtXinv
    se = np.sqrt(np.diag(vcov))
    return se


def cr2_clustered_se(y, Xc, judge_ids_list, n_panels):
    fit_ols = sm.OLS(y, Xc).fit()
    max_se = np.zeros(Xc.shape[1])
    for k in range(3):
        cluster_var = np.array([jids[k] for jids in judge_ids_list])
        unique = sorted(set(cluster_var))
        c2i = {j: idx for idx, j in enumerate(unique)}
        cint = np.array([c2i[j] for j in cluster_var])
        try:
            se_k = _cr2_vcov_one_clustering(y, Xc, cint)
            for ci in range(Xc.shape[1]):
                max_se[ci] = max(max_se[ci], se_k[ci])
        except Exception as e:
            logger.warning(f"  CR2 position {k} failed: {e}")
            for ci in range(Xc.shape[1]):
                max_se[ci] = max(max_se[ci], fit_ols.bse[ci])
    return fit_ols.params, max_se


# ── CR3: jackknife sandwich ──

def _cr3_vcov_one_clustering(y, Xc, cluster_int):
    """CR3 (jackknife) sandwich estimator for one clustering."""
    n, p = Xc.shape
    fit_full = sm.OLS(y, Xc).fit()
    beta_full = fit_full.params

    clusters = np.unique(cluster_int)
    G = len(clusters)

    beta_loo = np.zeros((G, p))
    for gi, c in enumerate(clusters):
        mask = cluster_int != c
        y_loo = y[mask]
        X_loo = Xc[mask]
        if X_loo.shape[0] <= p:
            beta_loo[gi] = beta_full
            continue
        try:
            fit_loo = sm.OLS(y_loo, X_loo).fit()
            beta_loo[gi] = fit_loo.params
        except Exception:
            beta_loo[gi] = beta_full

    beta_bar = beta_loo.mean(axis=0)
    # V_CR3 = (G-1)/G * sum_c (beta_{-c} - beta_bar)(beta_{-c} - beta_bar)'
    diffs = beta_loo - beta_bar
    vcov = ((G - 1) / G) * (diffs.T @ diffs)
    se = np.sqrt(np.diag(vcov))
    return se


def cr3_clustered_se(y, Xc, judge_ids_list, n_panels):
    fit_ols = sm.OLS(y, Xc).fit()
    max_se = np.zeros(Xc.shape[1])
    for k in range(3):
        cluster_var = np.array([jids[k] for jids in judge_ids_list])
        unique = sorted(set(cluster_var))
        c2i = {j: idx for idx, j in enumerate(unique)}
        cint = np.array([c2i[j] for j in cluster_var])
        try:
            se_k = _cr3_vcov_one_clustering(y, Xc, cint)
            for ci in range(Xc.shape[1]):
                max_se[ci] = max(max_se[ci], se_k[ci])
        except Exception as e:
            logger.warning(f"  CR3 position {k} failed: {e}")
            for ci in range(Xc.shape[1]):
                max_se[ci] = max(max_se[ci], fit_ols.bse[ci])
    return fit_ols.params, max_se


def compute_p_from_se(params, max_se, n_panels, coef_idx):
    """Compute 2-sided p-value using t-distribution with n-p df."""
    df = n_panels - 3
    t_stat = params[coef_idx] / max_se[coef_idx] if max_se[coef_idx] > 0 else 0
    p_val = float(2 * t_dist.sf(abs(t_stat), df))
    return t_stat, p_val


# ── Part A: Power Analysis ──

def run_power_analysis(log_keff_actual, log_eta_actual, y_actual,
                       judge_ids_list, n_panels, rng):
    """Monte Carlo power analysis for K_eff effect detection."""
    logger.info("\n" + "=" * 70)
    logger.info("PART A: Power Analysis")
    logger.info("=" * 70)

    # Fit actual regression to get baseline parameters
    Xc_actual = sm.add_constant(np.column_stack([log_keff_actual, log_eta_actual]))
    fit_actual = sm.OLS(y_actual, Xc_actual).fit()

    intercept_actual = fit_actual.params[0]
    beta_eta_actual = fit_actual.params[2]
    sigma_resid = np.sqrt(fit_actual.mse_resid)
    sd_y = np.std(y_actual)
    sd_log_keff = np.std(log_keff_actual)

    logger.info(f"  Actual regression: intercept={intercept_actual:.4f}, "
                f"β_eta={beta_eta_actual:.4f}, σ_resid={sigma_resid:.4f}")
    logger.info(f"  SD(y)={sd_y:.4f}, SD(log_K_eff)={sd_log_keff:.4f}")
    logger.info(f"  n_panels={n_panels}, n_clusters(per position)~13")

    results = {}

    for beta_std in BETA_STD_GRID:
        beta_raw = beta_std * sd_y / sd_log_keff
        logger.info(f"\n  β_std={beta_std} → β_raw={beta_raw:.4f}")

        n_sig = 0
        for sim in range(N_SIM):
            # Generate simulated y with known effect
            y_sim = (intercept_actual
                     + beta_raw * log_keff_actual
                     + beta_eta_actual * log_eta_actual
                     + rng.normal(0, sigma_resid, n_panels))

            # Run CR1 clustered SE (same as production)
            params_sim, max_se_sim = cr1_clustered_se(
                y_sim, Xc_actual, judge_ids_list, n_panels
            )
            _, p_keff = compute_p_from_se(params_sim, max_se_sim, n_panels, 1)

            if p_keff < FDR_ALPHA:
                n_sig += 1

        power = n_sig / N_SIM
        results[str(beta_std)] = {
            "beta_std": beta_std,
            "beta_raw": float(beta_raw),
            "power": power,
            "n_sig": n_sig,
        }
        logger.info(f"    Power = {power:.3f} ({n_sig}/{N_SIM})")

    # Interpolate to find MDE at 80% power
    betas = np.array(BETA_STD_GRID)
    powers = np.array([results[str(b)]["power"] for b in BETA_STD_GRID])

    mde_80 = None
    if powers[-1] >= 0.80 and powers[0] <= 0.80:
        try:
            f_interp = interp1d(powers, betas, kind='linear')
            mde_80 = float(f_interp(0.80))
        except Exception:
            pass
    elif powers[0] > 0.80:
        mde_80 = float(betas[0])  # even smallest effect has >80% power

    if mde_80 is not None:
        logger.info(f"\n  MDE at 80% power: β_std = {mde_80:.3f}")
    else:
        logger.info(f"\n  MDE at 80% power: not achievable in tested range "
                    f"(max power = {powers[-1]:.3f})")

    return {
        "n_panels": n_panels,
        "n_clusters_per_position": 15,
        "n_simulations": N_SIM,
        "baseline": {
            "intercept": float(intercept_actual),
            "beta_eta": float(beta_eta_actual),
            "sigma_resid": float(sigma_resid),
            "sd_y": float(sd_y),
            "sd_log_keff": float(sd_log_keff),
        },
        "results": results,
        "MDE_80": mde_80,
    }


# ── Part B: CR comparison ──

def run_cr_comparison(all_data):
    """Run CR1/CR2/CR3 across all 12 conditions."""
    logger.info("\n" + "=" * 70)
    logger.info("PART B: CR1 vs CR2 vs CR3 Comparison")
    logger.info("=" * 70)

    raw_ps = {f"{m}_{v}": [] for m in ["cr1", "cr2", "cr3"] for v in ["eta", "keff"]}
    valid_keys = []
    condition_results = {}

    for cond, data in all_data.items():
        y = data["y"]
        Xc = data["Xc"]
        judge_ids_list = data["judge_ids_list"]
        n_panels = data["n_panels"]

        logger.info(f"\n--- {cond} ({n_panels} panels) ---")

        cr_results = {}
        for cr_name, cr_func in [("CR1", cr1_clustered_se),
                                  ("CR2", cr2_clustered_se),
                                  ("CR3", cr3_clustered_se)]:
            params, max_se = cr_func(y, Xc, judge_ids_list, n_panels)
            t_keff, p_keff = compute_p_from_se(params, max_se, n_panels, 1)
            t_eta, p_eta = compute_p_from_se(params, max_se, n_panels, 2)

            cr_results[cr_name] = {
                "params": params.tolist(),
                "max_se": max_se.tolist(),
                "t_keff": float(t_keff),
                "t_eta": float(t_eta),
                "p_keff": float(p_keff),
                "p_eta": float(p_eta),
            }

            prefix = cr_name.lower()
            raw_ps[f"{prefix}_eta"].append(p_eta)
            raw_ps[f"{prefix}_keff"].append(p_keff)

            logger.info(f"  {cr_name}: SE_keff={max_se[1]:.4f}, SE_eta={max_se[2]:.4f} | "
                        f"p_keff={p_keff:.2e}, p_eta={p_eta:.2e}")

        valid_keys.append(cond)
        condition_results[cond] = cr_results

    # FDR correction
    fdr_results = {}
    for key, pvals in raw_ps.items():
        if len(pvals) > 0:
            _, fdr_p, _, _ = multipletests(pvals, method="fdr_bh")
            fdr_results[key] = fdr_p.tolist()
        else:
            fdr_results[key] = []

    # Attach FDR p-values
    for i, ck in enumerate(valid_keys):
        for cr_name in ["CR1", "CR2", "CR3"]:
            prefix = cr_name.lower()
            condition_results[ck][cr_name]["fdr_p_keff"] = fdr_results[f"{prefix}_keff"][i]
            condition_results[ck][cr_name]["fdr_p_eta"] = fdr_results[f"{prefix}_eta"][i]

    # Summary
    logger.info(f"\n{'='*80}")
    logger.info("SUMMARY: FDR-significant counts (/12)")
    logger.info(f"{'='*80}")

    summary = {}
    for cr_name in ["CR1", "CR2", "CR3"]:
        prefix = cr_name.lower()
        eta_sig = sum(1 for p in fdr_results[f"{prefix}_eta"] if p < FDR_ALPHA)
        keff_sig = sum(1 for p in fdr_results[f"{prefix}_keff"] if p < FDR_ALPHA)
        summary[cr_name] = {
            "eta_fdr_sig": f"{eta_sig}/12",
            "keff_fdr_sig": f"{keff_sig}/12",
        }
        logger.info(f"  {cr_name}: η_max {eta_sig}/12 FDR sig | K_eff {keff_sig}/12 FDR sig")

    # Detailed table
    logger.info(f"\n{'='*120}")
    logger.info("DETAILED TABLE")
    logger.info(f"{'='*120}")
    hdr = f"{'Condition':<28} | {'CR1 p_K':>10} {'FDR':>6} | {'CR2 p_K':>10} {'FDR':>6} | {'CR3 p_K':>10} {'FDR':>6}"
    logger.info(hdr)
    logger.info("-" * 120)

    def sig(p):
        return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"

    for ck in valid_keys:
        cr = condition_results[ck]
        logger.info(
            f"  {ck:<26} | "
            f"{cr['CR1']['p_keff']:>10.2e} {sig(cr['CR1']['fdr_p_keff']):>5} | "
            f"{cr['CR2']['p_keff']:>10.2e} {sig(cr['CR2']['fdr_p_keff']):>5} | "
            f"{cr['CR3']['p_keff']:>10.2e} {sig(cr['CR3']['fdr_p_keff']):>5}"
        )

    return {
        "per_condition": condition_results,
        "summary": summary,
    }


def main():
    logger.info("=" * 70)
    logger.info("Power Analysis + CR2/CR3 Small-Sample Correction")
    logger.info("=" * 70)

    rng = np.random.default_rng(42)

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

    # Build regression data for all conditions
    all_data = {}
    first_condition_data = None

    for ds in DATASETS:
        keff_data = mi_data["keff_per_panel"].get(ds, {})
        for atk in ATTACKS:
            cond = f"{ds}x{atk}"
            p_asrs, p_keffs, p_etas = [], [], []
            panel_judge_ids = []

            for combo in all_combos:
                jids = [ALL_MODELS[i] for i in combo]
                if not all((ds, atk, j) in ind_asr for j in jids):
                    continue
                pk = "|".join(jids)
                if pk not in keff_data:
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
            if n_panels < 10:
                continue

            p_asrs = np.array(p_asrs)
            if np.std(p_asrs) < 1e-10:
                continue

            log_keff = np.log(np.array(p_keffs))
            log_eta = np.log(np.array(p_etas) + EPS)
            y = np.log(p_asrs + EPS)
            Xc = sm.add_constant(np.column_stack([log_keff, log_eta]))

            all_data[cond] = {
                "y": y,
                "Xc": Xc,
                "log_keff": log_keff,
                "log_eta": log_eta,
                "judge_ids_list": panel_judge_ids,
                "n_panels": n_panels,
            }

            if first_condition_data is None:
                first_condition_data = all_data[cond]

    logger.info(f"\nBuilt regression data for {len(all_data)} conditions")

    # Part A: Power analysis using first condition's X distribution
    power_result = run_power_analysis(
        first_condition_data["log_keff"],
        first_condition_data["log_eta"],
        first_condition_data["y"],
        first_condition_data["judge_ids_list"],
        first_condition_data["n_panels"],
        rng,
    )

    # Part B: CR comparison
    cr_result = run_cr_comparison(all_data)

    # Save output
    output = {
        "power_analysis": power_result,
        "cr_comparison": cr_result,
    }

    out_dir = Path("/root/cert_manip_resist_eval/artifacts/results/plan001")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "power_cr2_cr3.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
    logger.info(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

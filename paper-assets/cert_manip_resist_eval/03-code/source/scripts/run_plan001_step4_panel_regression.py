#!/usr/bin/env python3
"""Plan 001 Step 4: Panel regression -- 455 panels x 12 conditions.

Input:
  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json
  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/
  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json

Output:
  - artifacts/results/plan001/panel_regression/step4_regression_results.json

Dependencies: numpy, scipy, statsmodels
Optional: pingouin (for partial_corr; manual fallback included)
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import warnings
import itertools
import numpy as np
import statsmodels.api as sm
from pathlib import Path
from scipy import optimize, stats, special
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.multitest import multipletests

from src.utils import setup_logging
from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS, OUTPUT_DIR,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)

logger = setup_logging("plan001_step4")

EPS = 0.001


# ── JSON Helper ──────────────────────────────────────────────────────

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


# ── ASR Computation ──────────────────────────────────────────────────

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
    n = min(len(pairs), *(len(clean[j]) for j in jids), *(len(attacked[j]) for j in jids))
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


# ── Regression Helpers ───────────────────────────────────────────────

def partial_corr_manual(x, y, covar):
    Xc = sm.add_constant(covar)
    rx = sm.OLS(x, Xc).fit().resid
    ry = sm.OLS(y, Xc).fit().resid
    r, p = stats.pearsonr(rx, ry)
    return float(r), float(p)


try:
    import pingouin as pg
    import pandas as pd

    def partial_corr_fn(x, y, covar):
        df = pd.DataFrame({"x": x, "y": y, "z": covar})
        res = pg.partial_corr(data=df, x="x", y="y", covar="z")
        return float(res["r"].values[0]), float(res["p_val"].values[0])
    logger.info("Using pingouin for partial correlation")
except ImportError:
    partial_corr_fn = partial_corr_manual
    logger.info("pingouin not available, using manual partial correlation")


def beta_regression_mle(y_raw, X):
    y = np.clip(y_raw, 1e-6, 1 - 1e-6)
    n, k = X.shape

    def neg_ll(params):
        beta = params[:k]
        phi = np.exp(params[k])
        mu = 1.0 / (1.0 + np.exp(-(X @ beta)))
        a = mu * phi
        b = (1.0 - mu) * phi
        return -np.sum(
            special.gammaln(phi) - special.gammaln(a) - special.gammaln(b)
            + (a - 1.0) * np.log(y) + (b - 1.0) * np.log(1.0 - y)
        )

    y_logit = np.log(y / (1.0 - y))
    x0 = np.zeros(k + 1)
    try:
        init_fit = sm.OLS(y_logit, X).fit()
        x0[:k] = init_fit.params
    except Exception:
        pass
    x0[k] = np.log(10.0)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        res = optimize.minimize(neg_ll, x0, method="L-BFGS-B",
                                options={"maxiter": 5000, "ftol": 1e-12})
    if not res.success:
        return None

    n_p = len(res.x)
    H = np.zeros((n_p, n_p))
    eps_h = 1e-5
    for i in range(n_p):
        for j in range(i, n_p):
            ei = np.zeros(n_p)
            ej = np.zeros(n_p)
            ei[i] = eps_h
            ej[j] = eps_h
            fpp = neg_ll(res.x + ei + ej)
            fpm = neg_ll(res.x + ei - ej)
            fmp = neg_ll(res.x - ei + ej)
            fmm = neg_ll(res.x - ei - ej)
            H[i, j] = H[j, i] = (fpp - fpm - fmp + fmm) / (4.0 * eps_h * eps_h)

    try:
        cov = np.linalg.inv(H)
        se = np.sqrt(np.maximum(np.diag(cov), 0.0))
    except np.linalg.LinAlgError:
        return None

    beta = res.x[:k]
    se_b = se[:k]
    z = beta / np.maximum(se_b, 1e-12)
    pvals = 2.0 * (1.0 - stats.norm.cdf(np.abs(z)))
    return {"beta": beta, "se": se_b, "z": z, "p": pvals}


def run_condition_analysis(panel_asrs, keffs, eta_maxs):
    n = len(panel_asrs)
    y = np.log(panel_asrs + EPS)
    x1 = np.log(keffs)
    x2 = np.log(eta_maxs + EPS)
    X = np.column_stack([x1, x2])
    Xc = sm.add_constant(X)
    results = {}

    fit = sm.OLS(y, Xc).fit()
    results["ols"] = {
        "keff_beta": float(fit.params[1]),
        "keff_t": float(fit.tvalues[1]),
        "keff_p": float(fit.pvalues[1]),
        "eta_max_beta": float(fit.params[2]),
        "eta_max_t": float(fit.tvalues[2]),
        "eta_max_p": float(fit.pvalues[2]),
        "R2": float(fit.rsquared),
        "adj_R2": float(fit.rsquared_adj),
        "f_stat": float(fit.fvalue) if np.isfinite(fit.fvalue) else None,
        "f_pvalue": float(fit.f_pvalue) if np.isfinite(fit.f_pvalue) else None,
    }

    results["vif_keff"] = float(variance_inflation_factor(Xc, 1))
    results["vif_eta_max"] = float(variance_inflation_factor(Xc, 2))

    pr, pp = partial_corr_fn(x1, y, x2)
    results["partial_r_keff"] = pr
    results["partial_r_keff_p"] = pp

    Xz = sm.add_constant(x2)
    resid_keff = sm.OLS(x1, Xz).fit().resid
    Xr = sm.add_constant(resid_keff)
    fit_r = sm.OLS(y, Xr).fit()
    results["residualized_keff_beta"] = float(fit_r.params[1])
    results["residualized_keff_t"] = float(fit_r.tvalues[1])
    results["residualized_keff_p"] = float(fit_r.pvalues[1])

    y_raw = np.clip(panel_asrs, 0.0, 1.0)
    br = beta_regression_mle(y_raw, Xc)
    if br is not None:
        results["beta_reg_keff_beta"] = float(br["beta"][1])
        results["beta_reg_keff_p"] = float(br["p"][1])
        results["beta_reg_eta_max_beta"] = float(br["beta"][2])
        results["beta_reg_eta_max_p"] = float(br["p"][2])
    else:
        results["beta_reg_keff_p"] = None
        results["beta_reg_eta_max_p"] = None

    return results


# ── Main ─────────────────────────────────────────────────────────────

def main():
    logger.info("=" * 60)
    logger.info("Plan 001 Step 4: Panel Regression (455 panels x 12 conditions)")
    logger.info("=" * 60)

    mi_data = load_mi_data()
    pairs = load_pairs()
    clean, attacked = load_all_scores()

    logger.info("\nPrecomputing individual ASR...")
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

    condition_results = {}
    raw_eta_ps = []
    raw_keff_ps = []
    valid_cond_keys = []

    for ds in DATASETS:
        keff_data = mi_data["keff_per_panel"].get(ds, {})
        for atk in ATTACKS:
            cond = f"{ds}x{atk}"
            logger.info(f"\n--- {cond} ---")

            p_asrs, p_keffs, p_etas = [], [], []
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

            n_panels = len(p_asrs)
            logger.info(f"  {n_panels} panels with data, {skipped} skipped")

            if n_panels < 10:
                logger.warning(f"  Too few panels ({n_panels}), skipping")
                condition_results[cond] = {"n_panels": n_panels, "skipped": True}
                continue

            p_asrs = np.array(p_asrs)
            p_keffs = np.array(p_keffs)
            p_etas = np.array(p_etas)

            if np.std(p_asrs) < 1e-10:
                logger.warning(f"  Constant ASR ({p_asrs[0]:.4f}), skipping regression")
                condition_results[cond] = {
                    "n_panels": n_panels, "skipped": True,
                    "reason": "constant_asr", "asr_value": float(p_asrs[0]),
                }
                continue

            cond_res = run_condition_analysis(p_asrs, p_keffs, p_etas)
            cond_res["n_panels"] = n_panels
            cond_res["skipped"] = False
            cond_res["asr_stats"] = {
                "mean": float(np.mean(p_asrs)),
                "std": float(np.std(p_asrs)),
                "min": float(np.min(p_asrs)),
                "max": float(np.max(p_asrs)),
                "pct_zero": float(np.mean(p_asrs == 0)),
            }
            condition_results[cond] = cond_res

            raw_eta_ps.append(cond_res["ols"]["eta_max_p"])
            raw_keff_ps.append(cond_res["ols"]["keff_p"])
            valid_cond_keys.append(cond)

            ols = cond_res["ols"]
            sig_k = "***" if ols["keff_p"] < 0.001 else "**" if ols["keff_p"] < 0.01 else "*" if ols["keff_p"] < 0.05 else "ns"
            sig_e = "***" if ols["eta_max_p"] < 0.001 else "**" if ols["eta_max_p"] < 0.01 else "*" if ols["eta_max_p"] < 0.05 else "ns"
            logger.info(
                f"  OLS R2={ols['R2']:.4f}  "
                f"K_eff: B={ols['keff_beta']:+.4f} p={ols['keff_p']:.4f} {sig_k}  "
                f"eta_max: B={ols['eta_max_beta']:+.4f} p={ols['eta_max_p']:.4f} {sig_e}"
            )
            logger.info(
                f"  VIF: K_eff={cond_res['vif_keff']:.2f}, eta_max={cond_res['vif_eta_max']:.2f}"
            )
            logger.info(
                f"  Partial r(K_eff|eta_max)={cond_res['partial_r_keff']:.4f} "
                f"p={cond_res['partial_r_keff_p']:.4f}"
            )
            logger.info(
                f"  Residualized K_eff: B={cond_res['residualized_keff_beta']:+.4f} "
                f"p={cond_res['residualized_keff_p']:.4f}"
            )

    # ── Multiple testing corrections ──
    if raw_eta_ps:
        _, bonf_eta, _, _ = multipletests(raw_eta_ps, method="bonferroni")
        _, fdr_eta, _, _ = multipletests(raw_eta_ps, method="fdr_bh")
        _, bonf_keff, _, _ = multipletests(raw_keff_ps, method="bonferroni")
        _, fdr_keff, _, _ = multipletests(raw_keff_ps, method="fdr_bh")

        for i, ck in enumerate(valid_cond_keys):
            condition_results[ck]["eta_max_bonferroni_p"] = float(bonf_eta[i])
            condition_results[ck]["eta_max_fdr_p"] = float(fdr_eta[i])
            condition_results[ck]["keff_bonferroni_p"] = float(bonf_keff[i])
            condition_results[ck]["keff_fdr_p"] = float(fdr_keff[i])

    # ── Summary ──
    valid = [condition_results[k] for k in valid_cond_keys]
    nv = len(valid)
    summary = {}
    if nv > 0:
        summary = {
            "keff_sig_negative_count": (
                f"{sum(1 for r in valid if r['ols']['keff_beta'] < 0 and r['ols']['keff_p'] < 0.05)}/{nv}"
            ),
            "keff_residualized_sig_count": (
                f"{sum(1 for r in valid if r.get('residualized_keff_p', 1) < 0.05)}/{nv}"
            ),
            "eta_max_bonferroni_sig_count": (
                f"{sum(1 for r in valid if r.get('eta_max_bonferroni_p', 1) < 0.05)}/{nv}"
            ),
            "eta_max_fdr_sig_count": (
                f"{sum(1 for r in valid if r.get('eta_max_fdr_p', 1) < 0.05)}/{nv}"
            ),
            "mean_vif_keff": float(np.mean([r["vif_keff"] for r in valid])),
            "mean_R2": float(np.mean([r["ols"]["R2"] for r in valid])),
        }

    output = {
        "n_panels": 455,
        "n_models": len(ALL_MODELS),
        "models": ALL_MODELS,
        "datasets": DATASETS,
        "attacks": ATTACKS,
        "conditions": condition_results,
        "summary": summary,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / "step4_regression_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
    logger.info(f"\nResults saved: {out_path}")

    logger.info("\n" + "=" * 60)
    logger.info("SUMMARY")
    logger.info("=" * 60)
    for k, v in summary.items():
        logger.info(f"  {k}: {v}")

    logger.info(f"\n{'Condition':<35} {'R2':>6} {'K_eff B':>9} {'K_eff p':>9} {'eta_max B':>9} {'eta_max p':>9} {'VIF':>5}")
    logger.info("-" * 90)
    for ck in valid_cond_keys:
        r = condition_results[ck]
        o = r["ols"]
        logger.info(
            f"  {ck:<33} {o['R2']:>6.3f} {o['keff_beta']:>+9.4f} {o['keff_p']:>9.4f} "
            f"{o['eta_max_beta']:>+9.4f} {o['eta_max_p']:>9.4f} {r['vif_keff']:>5.1f}"
        )


if __name__ == "__main__":
    main()

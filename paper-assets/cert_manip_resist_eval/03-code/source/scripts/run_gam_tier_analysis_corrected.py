#!/usr/bin/env python3
"""GAM + Tier-Indicator Regression with CORRECTED 3/3/9 tier classification.

Correct tier split (capability-based, matching Table 1):
  Frontier (3): gpt-5.5, gemini-3.1-pro-preview, claude-opus-4-6
  Mid (3): gemini-3.5-flash, gpt-4.1, claude-sonnet-4-6
  Lightweight (9): gpt-4.1-mini, gpt-4.1-nano, claude-3-haiku,
                   mistral-large, llama3.1-70b, llama3.1-8b,
                   qwen2.5-72b, qwen2.5-32b, qwen2.5-14b

Output:
  artifacts/results/plan001/gam_tier_analysis_corrected.json
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import itertools
import numpy as np
import statsmodels.api as sm
from collections import Counter
from pathlib import Path
from statsmodels.stats.multitest import multipletests

from src.utils import setup_logging
from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)

logger = setup_logging("gam_tier_corrected")

EPS = 1e-6
FDR_ALPHA = 0.05

TIER_MAP = {
    'gpt-5.5': 'frontier',
    'gemini-3.1-pro-preview': 'frontier',
    'claude-opus-4-6': 'frontier',
    'gemini-3.5-flash': 'mid',
    'gpt-4.1': 'mid',
    'claude-sonnet-4-6': 'mid',
    'gpt-4.1-mini': 'lightweight',
    'gpt-4.1-nano': 'lightweight',
    'claude-3-haiku': 'lightweight',
    'mistral-large': 'lightweight',
    'llama3.1-70b': 'lightweight',
    'llama3.1-8b': 'lightweight',
    'qwen2.5-72b': 'lightweight',
    'qwen2.5-32b': 'lightweight',
    'qwen2.5-14b': 'lightweight',
}

TIERS_ORDERED = ['frontier', 'mid', 'lightweight']
TIER_RANK = {'frontier': 0, 'mid': 1, 'lightweight': 2}


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


def panel_majority_tier(jids):
    """Majority tier. If all 3 different, use lowest (lightweight)."""
    tiers = [TIER_MAP[j] for j in jids]
    cnt = Counter(tiers)
    if len(cnt) == 3:
        return 'lightweight'
    return cnt.most_common(1)[0][0]


def standardized_beta(X, y, col_idx, params):
    return params[col_idx] * np.std(X[:, col_idx - 1]) / np.std(y)


def run_canonical_ols(log_keff, log_eta, y):
    X = np.column_stack([log_keff, log_eta])
    Xc = sm.add_constant(X)
    fit = sm.OLS(y, Xc).fit()
    return {
        "keff_beta": float(fit.params[1]),
        "keff_beta_std": float(standardized_beta(Xc, y, 1, fit.params)),
        "eta_beta": float(fit.params[2]),
        "eta_beta_std": float(standardized_beta(Xc, y, 2, fit.params)),
        "keff_p": float(fit.pvalues[1]),
        "eta_p": float(fit.pvalues[2]),
        "R2": float(fit.rsquared),
        "R2_adj": float(fit.rsquared_adj),
    }


def run_tier_indicator_ols(log_keff, log_eta, tier_mid, tier_light, y):
    X = np.column_stack([log_keff, log_eta, tier_mid, tier_light])
    Xc = sm.add_constant(X)
    fit = sm.OLS(y, Xc).fit()
    return {
        "keff_beta": float(fit.params[1]),
        "keff_beta_std": float(standardized_beta(Xc, y, 1, fit.params)),
        "eta_beta": float(fit.params[2]),
        "eta_beta_std": float(standardized_beta(Xc, y, 2, fit.params)),
        "tier_mid_beta": float(fit.params[3]),
        "tier_light_beta": float(fit.params[4]),
        "keff_p": float(fit.pvalues[1]),
        "eta_p": float(fit.pvalues[2]),
        "tier_mid_p": float(fit.pvalues[3]),
        "tier_light_p": float(fit.pvalues[4]),
        "R2": float(fit.rsquared),
        "R2_adj": float(fit.rsquared_adj),
        "keff_tval": float(fit.tvalues[1]),
        "eta_tval": float(fit.tvalues[2]),
    }


def run_gam(log_keff, log_eta, y):
    """GAM with pygam; fallback to cubic polynomial."""
    try:
        from pygam import LinearGAM, s
        gam = LinearGAM(s(0, n_splines=8) + s(1, n_splines=8))
        gam.gridsearch(np.column_stack([log_keff, log_eta]), y, progress=False)
        p_values = gam.statistics_['p_values']
        keff_p = float(p_values[0])
        eta_p = float(p_values[1])
        XX = gam.generate_X_grid(term=0, n=100)
        pdep = gam.partial_dependence(term=0, X=XX)
        keff_sign = "+" if pdep[-1] > pdep[0] else "-"
        return {
            "method": "pygam",
            "keff_p": keff_p,
            "eta_p": eta_p,
            "keff_sign": keff_sign,
            "pseudo_R2": float(gam.statistics_.get('pseudo_r2', {}).get('explained_deviance', np.nan)),
            "GCV": float(gam.statistics_.get('GCV', np.nan)),
            "n_splines": 8,
        }
    except Exception as e:
        logger.info(f"    pygam failed ({e}), using cubic polynomial")
        X = np.column_stack([log_keff, log_eta, log_eta**2, log_eta**3])
        Xc = sm.add_constant(X)
        fit = sm.OLS(y, Xc).fit()
        keff_sign = "+" if fit.params[1] > 0 else "-"
        return {
            "method": "cubic_polynomial",
            "keff_beta": float(fit.params[1]),
            "keff_p": float(fit.pvalues[1]),
            "eta_p": float(fit.pvalues[2]),
            "keff_sign": keff_sign,
            "R2": float(fit.rsquared),
            "R2_adj": float(fit.rsquared_adj),
        }


def sig_stars(p):
    if p < 0.001:
        return "***"
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    return "ns"


def main():
    logger.info("=" * 70)
    logger.info("GAM + Tier-Indicator Regression — CORRECTED 3/3/9 Tiers")
    logger.info("=" * 70)

    tier_counts_global = Counter(TIER_MAP.values())
    logger.info(f"Tier sizes: {dict(tier_counts_global)}")
    for t in TIERS_ORDERED:
        models = [m for m, tt in TIER_MAP.items() if tt == t]
        logger.info(f"  {t}: {models}")

    mi_data = load_mi_data()
    pairs = load_pairs()
    clean, attacked = load_all_scores()

    # Precompute individual ASR
    ind_asr = {}
    for ds in DATASETS:
        for atk in ATTACKS:
            for mid in ALL_MODELS:
                if mid in clean[ds] and mid in attacked[ds][atk]:
                    ind_asr[(ds, atk, mid)] = compute_individual_asr(
                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]
                    )
    logger.info(f"Computed {len(ind_asr)} individual ASR values")

    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))
    logger.info(f"Total panels: {len(all_combos)}")

    conditions = {}
    raw_ps = {
        "canonical_eta": [], "canonical_keff": [],
        "tier_eta": [], "tier_keff": [],
        "gam_eta": [], "gam_keff": [],
    }
    valid_keys = []

    for ds in DATASETS:
        keff_data = mi_data["keff_per_panel"].get(ds, {})
        for atk in ATTACKS:
            cond = f"{ds}x{atk}"
            logger.info(f"\n--- {cond} ---")

            p_asrs, p_keffs, p_etas = [], [], []
            p_tier_mid, p_tier_light = [], []
            tier_counts = Counter()
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

                mt = panel_majority_tier(jids)
                tier_counts[mt] += 1

                p_asrs.append(p_asr)
                p_keffs.append(keff)
                p_etas.append(eta_max)
                p_tier_mid.append(1 if mt == 'mid' else 0)
                p_tier_light.append(1 if mt == 'lightweight' else 0)

            n_panels = len(p_asrs)
            logger.info(f"  {n_panels} panels, {skipped} skipped")
            logger.info(f"  Tier distribution: {dict(tier_counts)}")

            if n_panels < 10:
                logger.warning(f"  Too few panels, skipping")
                continue

            p_asrs = np.array(p_asrs)
            p_keffs = np.array(p_keffs)
            p_etas = np.array(p_etas)
            p_tier_mid = np.array(p_tier_mid)
            p_tier_light = np.array(p_tier_light)

            if np.std(p_asrs) < 1e-10:
                logger.warning(f"  Constant ASR ({p_asrs[0]:.4f}), skipping")
                continue

            missing_tiers = [t for t in TIERS_ORDERED if tier_counts.get(t, 0) == 0]
            if missing_tiers:
                logger.warning(f"  Missing tiers: {missing_tiers}")

            log_keff = np.log(p_keffs)
            log_eta = np.log(p_etas + EPS)
            y = np.log(p_asrs + EPS)

            # Part A: Canonical OLS
            canon = run_canonical_ols(log_keff, log_eta, y)
            logger.info(
                f"  Canonical: K_eff β={canon['keff_beta']:+.4f} (std={canon['keff_beta_std']:+.4f}) p={canon['keff_p']:.2e}, "
                f"η_max β={canon['eta_beta']:+.4f} (std={canon['eta_beta_std']:+.4f}) p={canon['eta_p']:.2e}, R²={canon['R2']:.4f}"
            )

            # Part B: Tier-indicator OLS
            tier_res = run_tier_indicator_ols(log_keff, log_eta, p_tier_mid, p_tier_light, y)
            logger.info(
                f"  +Tier:     K_eff β={tier_res['keff_beta']:+.4f} (std={tier_res['keff_beta_std']:+.4f}) p={tier_res['keff_p']:.2e}, "
                f"η_max β={tier_res['eta_beta']:+.4f} (std={tier_res['eta_beta_std']:+.4f}) p={tier_res['eta_p']:.2e}, R²={tier_res['R2']:.4f}"
            )
            logger.info(
                f"             tier_mid p={tier_res['tier_mid_p']:.2e}, "
                f"tier_light p={tier_res['tier_light_p']:.2e}"
            )

            # Part C: GAM
            gam_res = run_gam(log_keff, log_eta, y)
            logger.info(
                f"  GAM({gam_res['method']}): K_eff p={gam_res['keff_p']:.2e} sign={gam_res.get('keff_sign','?')}, "
                f"η_max p={gam_res['eta_p']:.2e}"
            )

            conditions[cond] = {
                "n_panels": n_panels,
                "dataset": ds,
                "attack": atk,
                "tier_distribution": dict(tier_counts),
                "missing_tiers": missing_tiers,
                "canonical": canon,
                "tier_indicator": tier_res,
                "gam": gam_res,
            }
            raw_ps["canonical_eta"].append(canon["eta_p"])
            raw_ps["canonical_keff"].append(canon["keff_p"])
            raw_ps["tier_eta"].append(tier_res["eta_p"])
            raw_ps["tier_keff"].append(tier_res["keff_p"])
            raw_ps["gam_eta"].append(gam_res["eta_p"])
            raw_ps["gam_keff"].append(gam_res["keff_p"])
            valid_keys.append(cond)

    # FDR correction
    n_conds = len(valid_keys)
    logger.info(f"\nFDR correction across {n_conds} conditions...")

    fdr_results = {}
    for key, pvals in raw_ps.items():
        if len(pvals) == n_conds and n_conds > 0:
            _, fdr_q, _, _ = multipletests(pvals, method="fdr_bh")
            fdr_results[key] = fdr_q
        else:
            fdr_results[key] = np.array(pvals)

    for i, ck in enumerate(valid_keys):
        cd = conditions[ck]
        cd["canonical"]["eta_fdr_p"] = float(fdr_results["canonical_eta"][i])
        cd["canonical"]["keff_fdr_p"] = float(fdr_results["canonical_keff"][i])
        cd["tier_indicator"]["eta_fdr_p"] = float(fdr_results["tier_eta"][i])
        cd["tier_indicator"]["keff_fdr_p"] = float(fdr_results["tier_keff"][i])
        cd["gam"]["eta_fdr_p"] = float(fdr_results["gam_eta"][i])
        cd["gam"]["keff_fdr_p"] = float(fdr_results["gam_keff"][i])

        cd["canonical"]["keff_sign"] = "+" if cd["canonical"]["keff_beta"] > 0 else "-"
        cd["tier_indicator"]["keff_sign"] = "+" if cd["tier_indicator"]["keff_beta"] > 0 else "-"

    # Summary table
    logger.info("\n" + "=" * 160)
    logger.info("SUMMARY TABLE (CORRECTED 3/3/9 TIERS)")
    logger.info("=" * 160)
    hdr = (
        f"{'Condition':<28} │ {'Canon η':>10} {'Canon K':>10} {'K sign':>6} │ "
        f"{'Tier η':>10} {'Tier K':>10} {'K sign':>6} │ "
        f"{'GAM η':>10} {'GAM K':>10} {'K sign':>6}"
    )
    logger.info(hdr)
    logger.info("─" * 160)
    for ck in valid_keys:
        cd = conditions[ck]
        c, t, g = cd["canonical"], cd["tier_indicator"], cd["gam"]
        logger.info(
            f"  {ck:<26} │ "
            f"{c['eta_fdr_p']:>8.2e}{sig_stars(c['eta_fdr_p']):>3} "
            f"{c['keff_fdr_p']:>8.2e}{sig_stars(c['keff_fdr_p']):>3} "
            f"{c.get('keff_sign',''):>4} │ "
            f"{t['eta_fdr_p']:>8.2e}{sig_stars(t['eta_fdr_p']):>3} "
            f"{t['keff_fdr_p']:>8.2e}{sig_stars(t['keff_fdr_p']):>3} "
            f"{t.get('keff_sign',''):>4} │ "
            f"{g['eta_fdr_p']:>8.2e}{sig_stars(g['eta_fdr_p']):>3} "
            f"{g['keff_fdr_p']:>8.2e}{sig_stars(g['keff_fdr_p']):>3} "
            f"{g.get('keff_sign',''):>6}"
        )

    # Aggregate counts
    logger.info("\n" + "=" * 100)
    logger.info("AGGREGATE COMPARISON")
    logger.info("=" * 100)

    agg = {}
    for method_name, method_key in [
        ("Canonical OLS", "canonical"),
        ("+ Tier indicators (3/3/9)", "tier_indicator"),
        ("GAM (nonlinear)", "gam"),
    ]:
        eta_sig = keff_sig = keff_pos = keff_neg = 0
        for ck in valid_keys:
            m = conditions[ck][method_key]
            if m["eta_fdr_p"] < FDR_ALPHA:
                eta_sig += 1
            if m["keff_fdr_p"] < FDR_ALPHA:
                keff_sig += 1
                s = m.get("keff_sign")
                if s == "+":
                    keff_pos += 1
                elif s == "-":
                    keff_neg += 1

        agg[method_key] = {
            "method": method_name,
            "eta_fdr_sig": f"{eta_sig}/{n_conds}",
            "keff_fdr_sig": f"{keff_sig}/{n_conds}",
            "keff_sig_positive": keff_pos,
            "keff_sig_negative": keff_neg,
        }
        logger.info(
            f"  {method_name:<28}  η_max FDR sig: {eta_sig:>2}/{n_conds}  "
            f"K_eff FDR sig: {keff_sig:>2}/{n_conds}  (K+ {keff_pos}, K- {keff_neg})"
        )

    # Comparison with old (wrong) 4/6/5 tier results
    old_results = {
        "canonical": {"eta_sig": "11/12", "keff_sig": "8/12"},
        "tier_indicator": {"eta_sig": "10/12", "keff_sig": "5/12"},
        "gam": {"eta_sig": "12/12", "keff_sig": "12/12"},
    }

    logger.info("\n" + "=" * 100)
    logger.info("COMPARISON: OLD (4/6/5) vs NEW (3/3/9) TIERS")
    logger.info("=" * 100)
    for mk in ["canonical", "tier_indicator", "gam"]:
        old_k = old_results[mk]["keff_sig"]
        old_e = old_results[mk]["eta_sig"]
        new_k = agg[mk]["keff_fdr_sig"]
        new_e = agg[mk]["eta_fdr_sig"]
        logger.info(f"  {agg[mk]['method']:<28}  K_eff: {old_k} → {new_k}  |  η_max: {old_e} → {new_e}")

    # Save JSON
    output = {
        "analysis": "gam_tier_analysis_corrected",
        "tier_classification_version": "corrected_3_3_9",
        "n_models": len(ALL_MODELS),
        "models": ALL_MODELS,
        "n_conditions": n_conds,
        "fdr_alpha": FDR_ALPHA,
        "eps": EPS,
        "tier_classification": {
            "frontier": [m for m, t in TIER_MAP.items() if t == "frontier"],
            "mid": [m for m, t in TIER_MAP.items() if t == "mid"],
            "lightweight": [m for m, t in TIER_MAP.items() if t == "lightweight"],
        },
        "tier_indicator_ols": {
            "condition": {ck: conditions[ck]["tier_indicator"] for ck in valid_keys},
            "summary": agg["tier_indicator"],
        },
        "gam": {
            "condition": {ck: conditions[ck]["gam"] for ck in valid_keys},
            "summary": agg["gam"],
        },
        "canonical_ols": {
            "condition": {ck: conditions[ck]["canonical"] for ck in valid_keys},
            "summary": agg["canonical"],
        },
        "conditions_full": conditions,
        "comparison_with_wrong_tier": {
            "old_tier_split": "4/6/5 (frontier/mid/lightweight)",
            "new_tier_split": "3/3/9 (frontier/mid/lightweight)",
            "canonical_ols": {
                "old_keff_sig": old_results["canonical"]["keff_sig"],
                "new_keff_sig": agg["canonical"]["keff_fdr_sig"],
                "old_eta_sig": old_results["canonical"]["eta_sig"],
                "new_eta_sig": agg["canonical"]["eta_fdr_sig"],
            },
            "tier_indicator_ols": {
                "old_keff_sig": old_results["tier_indicator"]["keff_sig"],
                "new_keff_sig": agg["tier_indicator"]["keff_fdr_sig"],
                "old_eta_sig": old_results["tier_indicator"]["eta_sig"],
                "new_eta_sig": agg["tier_indicator"]["eta_fdr_sig"],
            },
            "gam": {
                "old_keff_sig": old_results["gam"]["keff_sig"],
                "new_keff_sig": agg["gam"]["keff_fdr_sig"],
                "old_eta_sig": old_results["gam"]["eta_sig"],
                "new_eta_sig": agg["gam"]["eta_fdr_sig"],
            },
        },
    }

    out_dir = Path("/root/cert_manip_resist_eval/artifacts/results/plan001")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "gam_tier_analysis_corrected.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
    logger.info(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

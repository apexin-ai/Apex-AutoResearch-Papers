#!/usr/bin/env python3
"""GAM + Tier-Indicator Regression Analysis.

Validates that K_eff remains significant after controlling for:
  Part A: Tier indicator variables (frontier/mid/lightweight)
  Part B: GAM or polynomial nonlinear η_max controls
across all 12 conditions (2 datasets × 6 attacks).

Output:
  - artifacts/results/plan001/gam_tier_analysis.json
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
from statsmodels.stats.outliers_influence import variance_inflation_factor

from src.utils import setup_logging
from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)

logger = setup_logging("gam_tier_analysis")

EPS = 1e-6
FDR_ALPHA = 0.05

TIER_MAP = {
    'gpt-5.5': 'frontier',
    'gemini-3.1-pro-preview': 'frontier',
    'claude-opus-4-6': 'frontier',
    'gemini-3.5-flash': 'frontier',
    'gpt-4.1': 'mid',
    'claude-sonnet-4-6': 'mid',
    'llama3.1-70b': 'mid',
    'qwen2.5-72b': 'mid',
    'mistral-large': 'mid',
    'qwen2.5-32b': 'mid',
    'gpt-4.1-mini': 'lightweight',
    'gpt-4.1-nano': 'lightweight',
    'claude-3-haiku': 'lightweight',
    'qwen2.5-14b': 'lightweight',
    'llama3.1-8b': 'lightweight',
}

TIERS_ORDERED = ['frontier', 'mid', 'lightweight']


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
    tiers = [TIER_MAP[j] for j in jids]
    return Counter(tiers).most_common(1)[0][0]


def sig_stars(p):
    if p < 0.001:
        return "***"
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    return "ns"


def run_canonical_ols(log_keff, log_eta, y):
    X = np.column_stack([log_keff, log_eta])
    Xc = sm.add_constant(X)
    fit = sm.OLS(y, Xc).fit()
    return {
        "keff_beta": float(fit.params[1]),
        "eta_beta": float(fit.params[2]),
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
        "eta_beta": float(fit.params[2]),
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


def run_gam_or_poly(log_keff, log_eta, y):
    """Try pygam first; fall back to cubic polynomial control."""
    try:
        from pygam import LinearGAM, s
        gam = LinearGAM(s(0, n_splines=8) + s(1, n_splines=8))
        gam.gridsearch(np.column_stack([log_keff, log_eta]), y,
                       progress=False)
        p_values = gam.statistics_['p_values']
        keff_p = float(p_values[0])
        eta_p = float(p_values[1])
        # Determine K_eff direction from partial dependence slope
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
        return {
            "method": "cubic_polynomial",
            "keff_beta": float(fit.params[1]),
            "keff_p": float(fit.pvalues[1]),
            "eta_lin_p": float(fit.pvalues[2]),
            "eta_sq_p": float(fit.pvalues[3]),
            "eta_cu_p": float(fit.pvalues[4]),
            "eta_p": float(fit.pvalues[2]),
            "R2": float(fit.rsquared),
            "R2_adj": float(fit.rsquared_adj),
        }


def main():
    logger.info("=" * 70)
    logger.info("GAM + Tier-Indicator Regression (15 models, 455 panels)")
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

    # Per-condition analysis
    conditions = {}
    # Raw p-values for FDR: [canonical, tier, gam] × [eta, keff]
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

            # Check if any tier has 0 panels
            missing_tiers = [t for t in TIERS_ORDERED if tier_counts.get(t, 0) == 0]
            if missing_tiers:
                logger.warning(f"  Missing tiers: {missing_tiers}")

            log_keff = np.log(p_keffs)
            log_eta = np.log(p_etas + EPS)
            y = np.log(p_asrs + EPS)

            # Part A: Canonical OLS
            canon = run_canonical_ols(log_keff, log_eta, y)
            logger.info(
                f"  Canonical: K_eff β={canon['keff_beta']:+.4f} p={canon['keff_p']:.2e}, "
                f"η_max β={canon['eta_beta']:+.4f} p={canon['eta_p']:.2e}, R²={canon['R2']:.4f}"
            )

            # Part B: Tier-indicator OLS
            tier_res = run_tier_indicator_ols(log_keff, log_eta, p_tier_mid, p_tier_light, y)
            logger.info(
                f"  +Tier:     K_eff β={tier_res['keff_beta']:+.4f} p={tier_res['keff_p']:.2e}, "
                f"η_max β={tier_res['eta_beta']:+.4f} p={tier_res['eta_p']:.2e}, R²={tier_res['R2']:.4f}"
            )
            logger.info(
                f"             tier_mid p={tier_res['tier_mid_p']:.2e}, "
                f"tier_light p={tier_res['tier_light_p']:.2e}"
            )

            # Part C: GAM / polynomial
            gam_res = run_gam_or_poly(log_keff, log_eta, y)
            logger.info(
                f"  GAM({gam_res['method']}): K_eff p={gam_res['keff_p']:.2e}, "
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
    logger.info(f"\nApplying FDR correction across {n_conds} conditions...")

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

        # Sign of K_eff effect
        keff_beta_canon = cd["canonical"]["keff_beta"]
        keff_beta_tier = cd["tier_indicator"]["keff_beta"]
        cd["canonical"]["keff_sign"] = "+" if keff_beta_canon > 0 else "-"
        cd["tier_indicator"]["keff_sign"] = "+" if keff_beta_tier > 0 else "-"

    # Summary table
    logger.info("\n" + "=" * 140)
    logger.info("SUMMARY TABLE")
    logger.info("=" * 140)
    hdr = (
        f"{'Condition':<28} │ {'Canon η':>8} {'Canon K':>8} {'K sign':>6} │ "
        f"{'Tier η':>8} {'Tier K':>8} {'K sign':>6} │ "
        f"{'GAM η':>8} {'GAM K':>8}"
    )
    logger.info(hdr)
    logger.info("─" * 140)
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
            f"{g['keff_fdr_p']:>8.2e}{sig_stars(g['keff_fdr_p']):>3}"
        )

    # Aggregate counts
    logger.info("\n" + "=" * 100)
    logger.info("AGGREGATE COMPARISON")
    logger.info("=" * 100)

    methods = {
        "Canonical OLS": ("canonical", None),
        "+ Tier indicators": ("tier_indicator", None),
        "GAM (nonlinear)": ("gam", None),
    }

    agg_rows = []
    for method_name, (method_key, _) in methods.items():
        eta_sig = 0
        keff_sig = 0
        keff_sig_pos = 0
        keff_sig_neg = 0
        for ck in valid_keys:
            cd = conditions[ck]
            m = cd[method_key]
            if m["eta_fdr_p"] < FDR_ALPHA:
                eta_sig += 1
            if m["keff_fdr_p"] < FDR_ALPHA:
                keff_sig += 1
                if method_key in ("canonical", "tier_indicator"):
                    if m.get("keff_sign") == "+":
                        keff_sig_pos += 1
                    else:
                        keff_sig_neg += 1
                else:
                    keff_sig_pos += 1  # GAM doesn't have directional beta

        row = {
            "method": method_name,
            "eta_sig": eta_sig,
            "keff_sig": keff_sig,
            "keff_sig_pos": keff_sig_pos,
            "keff_sig_neg": keff_sig_neg,
        }
        agg_rows.append(row)
        logger.info(
            f"  {method_name:<20}  η_max FDR sig: {eta_sig:>2}/{n_conds}  "
            f"K_eff FDR sig: {keff_sig:>2}/{n_conds}  "
            f"(K+ {keff_sig_pos}, K- {keff_sig_neg})"
        )

    # For GAM, also compute K_eff sign from the method-specific info
    # Re-do GAM keff sign: for cubic poly we have keff_beta; for pygam we don't
    for ck in valid_keys:
        g = conditions[ck]["gam"]
        if g["method"] == "cubic_polynomial" and "keff_beta" in g:
            g["keff_sign"] = "+" if g["keff_beta"] > 0 else "-"

    # Recount GAM with sign info
    gam_keff_pos = sum(
        1 for ck in valid_keys
        if conditions[ck]["gam"]["keff_fdr_p"] < FDR_ALPHA
        and conditions[ck]["gam"].get("keff_sign") == "+"
    )
    gam_keff_neg = sum(
        1 for ck in valid_keys
        if conditions[ck]["gam"]["keff_fdr_p"] < FDR_ALPHA
        and conditions[ck]["gam"].get("keff_sign") == "-"
    )
    gam_keff_nosign = sum(
        1 for ck in valid_keys
        if conditions[ck]["gam"]["keff_fdr_p"] < FDR_ALPHA
        and conditions[ck]["gam"].get("keff_sign") is None
    )
    agg_rows[2]["keff_sig_pos"] = gam_keff_pos
    agg_rows[2]["keff_sig_neg"] = gam_keff_neg
    if gam_keff_nosign > 0:
        agg_rows[2]["keff_sig_nosign"] = gam_keff_nosign

    logger.info(f"\n  GAM K_eff sign (updated): K+ {gam_keff_pos}, K- {gam_keff_neg}, no-sign {gam_keff_nosign}")

    # Formatted summary table
    logger.info("\n┌──────────────────────┬─────────────────┬─────────────────┬────────┬────────┐")
    logger.info("│ Method               │ η_max FDR (/12) │ K_eff FDR (/12) │ K+ sig │ K- sig │")
    logger.info("├──────────────────────┼─────────────────┼─────────────────┼────────┼────────┤")
    for r in agg_rows:
        logger.info(
            f"│ {r['method']:<20} │ {r['eta_sig']:>7}/{n_conds:<7} │ "
            f"{r['keff_sig']:>7}/{n_conds:<7} │ {r['keff_sig_pos']:>6} │ {r['keff_sig_neg']:>6} │"
        )
    logger.info("└──────────────────────┴─────────────────┴─────────────────┴────────┴────────┘")

    # Save JSON
    output = {
        "analysis": "gam_tier_analysis",
        "n_models": len(ALL_MODELS),
        "models": ALL_MODELS,
        "n_conditions": n_conds,
        "fdr_alpha": FDR_ALPHA,
        "eps": EPS,
        "tier_map": TIER_MAP,
        "conditions": conditions,
        "aggregate_summary": agg_rows,
    }

    out_dir = Path("/root/cert_manip_resist_eval/artifacts/results/plan001")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "gam_tier_analysis.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
    logger.info(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

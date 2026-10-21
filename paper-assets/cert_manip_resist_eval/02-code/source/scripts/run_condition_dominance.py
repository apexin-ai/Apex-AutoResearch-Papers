#!/usr/bin/env python3
"""Condition-Dependent Dominance Analysis.

For each of 12 conditions (2 datasets x 6 attacks), determines whether
K_eff_resid or η_max dominates panel ASR via standardized β comparison
and FDR-corrected significance testing.

Output:
  - artifacts/results/plan001/condition_dominance_15model.json
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import itertools
import numpy as np
import statsmodels.api as sm
from pathlib import Path
from scipy import stats
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.outliers_influence import variance_inflation_factor

from src.utils import setup_logging
from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)

logger = setup_logging("condition_dominance")

EPS = 1e-6
FDR_ALPHA = 0.05

MODEL_FAMILIES = {
    "qwen2.5-72b": "qwen", "qwen2.5-32b": "qwen", "qwen2.5-14b": "qwen",
    "llama3.1-70b": "meta", "llama3.1-8b": "meta",
    "mistral-large": "mistral",
    "claude-opus-4": "anthropic", "claude-sonnet-4": "anthropic",
    "claude-3-haiku": "anthropic",
    "gpt-5.5": "openai", "gpt-4.1": "openai",
    "gpt-4o": "openai", "gpt-4o-mini": "openai",
    "gemini-2.5-pro": "google", "gemini-2.5-flash": "google",
}


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


# ── Main ────────────────────────────────────────────────────────────

def main():
    logger.info("=" * 60)
    logger.info("Condition-Dependent Dominance Analysis (15 models)")
    logger.info("=" * 60)

    mi_data = load_mi_data()
    pairs = load_pairs()
    clean, attacked = load_all_scores()

    # Precompute individual ASR for all (ds, atk, model) triples
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

    # ── Per-condition analysis ──────────────────────────────────────
    condition_data = {}
    raw_eta_ps = []
    raw_kresid_ps = []
    valid_keys = []

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

            # ── Part 1: Standardized β comparison ──
            # Full OLS in log space (same as step4)
            log_keff = np.log(p_keffs)
            log_eta = np.log(p_etas + EPS)
            y = np.log(p_asrs + EPS)

            X = np.column_stack([log_keff, log_eta])
            Xc = sm.add_constant(X)
            fit_full = sm.OLS(y, Xc).fit()

            # Partial p-values from full OLS
            keff_p = float(fit_full.pvalues[1])
            eta_p = float(fit_full.pvalues[2])

            # Standardized β = raw_β × SD(x) / SD(y)
            sd_y = np.std(y)
            keff_std_beta = float(fit_full.params[1] * np.std(log_keff) / sd_y)
            eta_std_beta = float(fit_full.params[2] * np.std(log_eta) / sd_y)

            # Also compute residualized K_eff for verification
            keff_resid = sm.OLS(log_keff, sm.add_constant(log_eta)).fit().resid
            fit_resid = sm.OLS(y, sm.add_constant(keff_resid)).fit()
            kresid_p_check = float(fit_resid.pvalues[1])

            dominance_ratio = abs(keff_std_beta) / max(abs(eta_std_beta), 1e-12)

            # ── Part 2: Condition-level features ──
            # Individual ASR stats across all 15 models
            indiv_asrs = [
                ind_asr[(ds, atk, m)]
                for m in ALL_MODELS if (ds, atk, m) in ind_asr
            ]
            mean_indiv_asr = float(np.mean(indiv_asrs))
            indiv_asr_range = float(max(indiv_asrs) - min(indiv_asrs))
            indiv_asr_std = float(np.std(indiv_asrs))
            n_models_with_data = len(indiv_asrs)

            # Per-model breakdown
            indiv_detail = {}
            for m in ALL_MODELS:
                if (ds, atk, m) in ind_asr:
                    indiv_detail[m] = {
                        "asr": ind_asr[(ds, atk, m)],
                        "family": MODEL_FAMILIES.get(m, "unknown"),
                    }

            cd = {
                "n_panels": n_panels,
                "n_models": n_models_with_data,
                "dataset": ds,
                "attack": atk,
                # Standardized regression results (from full OLS)
                "keff_std_beta": keff_std_beta,
                "eta_std_beta": eta_std_beta,
                "keff_raw_p": keff_p,
                "eta_raw_p": eta_p,
                "kresid_p_check": kresid_p_check,
                "dominance_ratio": float(dominance_ratio),
                "R2": float(fit_full.rsquared),
                "vif_keff": float(variance_inflation_factor(Xc, 1)),
                "vif_eta": float(variance_inflation_factor(Xc, 2)),
                # Panel-level stats
                "avg_panel_asr": float(np.mean(p_asrs)),
                "panel_asr_std": float(np.std(p_asrs)),
                "eta_max_mean": float(np.mean(p_etas)),
                "eta_max_sd": float(np.std(p_etas)),
                "keff_mean": float(np.mean(p_keffs)),
                "keff_sd": float(np.std(p_keffs)),
                # Individual ASR stats
                "mean_indiv_asr": mean_indiv_asr,
                "indiv_asr_range": indiv_asr_range,
                "indiv_asr_std": indiv_asr_std,
                "indiv_detail": indiv_detail,
            }
            condition_data[cond] = cd
            raw_eta_ps.append(eta_p)
            raw_kresid_ps.append(keff_p)
            valid_keys.append(cond)

            logger.info(
                f"  Std β: K_eff={keff_std_beta:+.4f} (p={keff_p:.2e}), "
                f"η_max={eta_std_beta:+.4f} (p={eta_p:.2e}), "
                f"ratio={dominance_ratio:.2f}, R²={fit_full.rsquared:.4f}, "
                f"VIF={variance_inflation_factor(Xc, 1):.2f}"
            )

    # ── FDR correction (Benjamini-Hochberg) ─────────────────────────
    logger.info(f"\nApplying FDR correction across {len(valid_keys)} conditions...")
    _, fdr_eta, _, _ = multipletests(raw_eta_ps, method="fdr_bh")
    _, fdr_kresid, _, _ = multipletests(raw_kresid_ps, method="fdr_bh")

    for i, ck in enumerate(valid_keys):
        condition_data[ck]["eta_fdr_p"] = float(fdr_eta[i])
        condition_data[ck]["kresid_fdr_p"] = float(fdr_kresid[i])

        eta_sig = fdr_eta[i] < FDR_ALPHA
        kresid_sig = fdr_kresid[i] < FDR_ALPHA

        if eta_sig and not kresid_sig:
            cat = "eta_max_dominant"
        elif kresid_sig and not eta_sig:
            cat = "K_eff_dominant"
        elif eta_sig and kresid_sig:
            cat = "co-dominant"
        else:
            cat = "neither"
        condition_data[ck]["category"] = cat

    # ── TABLE 1: Dominance Classification ───────────────────────────
    logger.info("\n" + "=" * 160)
    logger.info("TABLE 1: Dominance Classification (Standardized β)")
    logger.info("=" * 160)
    hdr = (
        f"{'Condition':<32} {'η_std_β':>8} {'K_std_β':>8} {'Ratio':>6} "
        f"{'η_FDR_p':>10} {'K_FDR_p':>10} {'Category':<18} "
        f"{'AvgASR':>7} {'η_SD':>7} {'MeanIndiv':>9} {'ASRRange':>8}"
    )
    logger.info(hdr)
    logger.info("-" * 160)
    for ck in valid_keys:
        d = condition_data[ck]
        sig_e = "***" if d["eta_fdr_p"] < 0.001 else "**" if d["eta_fdr_p"] < 0.01 else "*" if d["eta_fdr_p"] < 0.05 else "ns"
        sig_k = "***" if d["kresid_fdr_p"] < 0.001 else "**" if d["kresid_fdr_p"] < 0.01 else "*" if d["kresid_fdr_p"] < 0.05 else "ns"
        logger.info(
            f"  {ck:<30} {d['eta_std_beta']:>+8.4f} {d['keff_std_beta']:>+8.4f} "
            f"{d['dominance_ratio']:>6.2f} "
            f"{d['eta_fdr_p']:>9.2e}{sig_e:>3} {d['kresid_fdr_p']:>9.2e}{sig_k:>3} "
            f"{d['category']:<18} "
            f"{d['avg_panel_asr']:>7.4f} {d['eta_max_sd']:>7.4f} "
            f"{d['mean_indiv_asr']:>9.4f} {d['indiv_asr_range']:>8.4f}"
        )

    # ── TABLE 2: Category Summary ──────────────────────────────────
    logger.info("\n" + "=" * 120)
    logger.info("TABLE 2: Category Summary")
    logger.info("=" * 120)

    categories = {}
    for ck in valid_keys:
        cat = condition_data[ck]["category"]
        if cat not in categories:
            categories[cat] = {
                "conditions": [],
                "attacks": set(),
                "indiv_ranges": [],
                "avg_asrs": [],
                "mean_indiv_asrs": [],
                "eta_sds": [],
                "keff_sds": [],
            }
        categories[cat]["conditions"].append(ck)
        categories[cat]["attacks"].add(condition_data[ck]["attack"])
        categories[cat]["indiv_ranges"].append(condition_data[ck]["indiv_asr_range"])
        categories[cat]["avg_asrs"].append(condition_data[ck]["avg_panel_asr"])
        categories[cat]["mean_indiv_asrs"].append(condition_data[ck]["mean_indiv_asr"])
        categories[cat]["eta_sds"].append(condition_data[ck]["eta_max_sd"])
        categories[cat]["keff_sds"].append(condition_data[ck]["keff_sd"])

    hdr2 = f"{'Category':<18} {'N':>3} {'Conditions':<55} {'Attacks':<40} {'AvgRange':>8}"
    logger.info(hdr2)
    logger.info("-" * 130)
    for cat in ["K_eff_dominant", "eta_max_dominant", "co-dominant", "neither"]:
        if cat not in categories:
            continue
        info = categories[cat]
        logger.info(
            f"  {cat:<16} {len(info['conditions']):>3} "
            f"{', '.join(info['conditions']):<55} "
            f"{', '.join(sorted(info['attacks'])):<40} "
            f"{np.mean(info['indiv_ranges']):>8.4f}"
        )

    # ── Systematic Difference Analysis ──────────────────────────────
    logger.info("\n" + "=" * 120)
    logger.info("SYSTEMATIC DIFFERENCE ANALYSIS")
    logger.info("=" * 120)

    for cat in ["K_eff_dominant", "eta_max_dominant", "co-dominant", "neither"]:
        if cat not in categories:
            continue
        info = categories[cat]
        logger.info(f"\n  {cat} (n={len(info['conditions'])}):")
        logger.info(f"    Mean panel ASR:      {np.mean(info['avg_asrs']):.4f}")
        logger.info(f"    Mean η_max SD:       {np.mean(info['eta_sds']):.4f}")
        logger.info(f"    Mean K_eff SD:       {np.mean(info['keff_sds']):.4f}")
        logger.info(f"    Mean indiv ASR:      {np.mean(info['mean_indiv_asrs']):.4f}")
        logger.info(f"    Mean indiv ASR range: {np.mean(info['indiv_ranges']):.4f}")

    # Cross-category comparison: K_eff dom vs η_max dom
    if "K_eff_dominant" in categories and "eta_max_dominant" in categories:
        k_info = categories["K_eff_dominant"]
        e_info = categories["eta_max_dominant"]
        logger.info("\n  --- K_eff_dominant vs η_max_dominant ---")
        for metric, k_vals, e_vals in [
            ("Avg panel ASR", k_info["avg_asrs"], e_info["avg_asrs"]),
            ("Mean indiv ASR", k_info["mean_indiv_asrs"], e_info["mean_indiv_asrs"]),
            ("Indiv ASR range", k_info["indiv_ranges"], e_info["indiv_ranges"]),
            ("η_max SD", k_info["eta_sds"], e_info["eta_sds"]),
            ("K_eff SD", k_info["keff_sds"], e_info["keff_sds"]),
        ]:
            k_mean = np.mean(k_vals)
            e_mean = np.mean(e_vals)
            logger.info(f"    {metric:<22}: K_dom={k_mean:.4f}  η_dom={e_mean:.4f}  diff={k_mean - e_mean:+.4f}")

    # Attack type → dominance mapping
    logger.info("\n  --- Attack Type → Dominance Mapping ---")
    atk_map = {}
    for ck in valid_keys:
        atk = condition_data[ck]["attack"]
        cat = condition_data[ck]["category"]
        ds = condition_data[ck]["dataset"]
        if atk not in atk_map:
            atk_map[atk] = []
        atk_map[atk].append(f"{ds}→{cat}")
    for atk in ATTACKS:
        if atk in atk_map:
            logger.info(f"    {atk:<22}: {', '.join(atk_map[atk])}")

    # ── Save JSON ───────────────────────────────────────────────────
    cat_summary = {}
    for cat, info in categories.items():
        cat_summary[cat] = {
            "conditions": info["conditions"],
            "attack_types": sorted(info["attacks"]),
            "n_conditions": len(info["conditions"]),
            "avg_panel_asr": float(np.mean(info["avg_asrs"])),
            "avg_indiv_asr_range": float(np.mean(info["indiv_ranges"])),
            "avg_mean_indiv_asr": float(np.mean(info["mean_indiv_asrs"])),
            "avg_eta_max_sd": float(np.mean(info["eta_sds"])),
            "avg_keff_sd": float(np.mean(info["keff_sds"])),
        }

    # Remove indiv_detail from condition_data for cleaner JSON
    conditions_out = {}
    for ck, cd in condition_data.items():
        cd_copy = {k: v for k, v in cd.items() if k != "indiv_detail"}
        conditions_out[ck] = cd_copy

    output = {
        "analysis": "condition_dominance_15model",
        "n_models": len(ALL_MODELS),
        "models": ALL_MODELS,
        "fdr_alpha": FDR_ALPHA,
        "eps": EPS,
        "conditions": conditions_out,
        "category_summary": cat_summary,
    }

    out_dir = Path("/root/cert_manip_resist_eval/artifacts/results/plan001")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "condition_dominance_15model.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
    logger.info(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

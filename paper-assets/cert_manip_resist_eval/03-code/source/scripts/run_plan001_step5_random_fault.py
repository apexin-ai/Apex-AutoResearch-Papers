#!/usr/bin/env python3
"""Plan 001 Step 5: Random-fault simulation -- 455 panels x 12 conditions.

Input:
  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json
  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/
  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json

Output:
  - artifacts/results/plan001/panel_regression/step5_random_fault_results.json

Dependencies: numpy, scipy, statsmodels
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
from scipy import stats

from src.utils import setup_logging
from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS, OUTPUT_DIR,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)

logger = setup_logging("plan001_step5")

EPS = 0.001
N_SIMS = 1000
N_SAMPLES = 300
SIM_BATCH = 100


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


# ── Random-Fault Simulation ─────────────────────────────────────────

def analytical_rf_asr(eta):
    e1, e2, e3 = eta
    return e1 * e2 + e1 * e3 + e2 * e3 - 2.0 * e1 * e2 * e3


def simulate_rf_vectorized(eta_all, rng):
    n_panels = eta_all.shape[0]
    rf_sum = np.zeros(n_panels)
    rf_sq_sum = np.zeros(n_panels)

    for sim_start in range(0, N_SIMS, SIM_BATCH):
        b = min(SIM_BATCH, N_SIMS - sim_start)
        randoms = rng.random((n_panels, b, N_SAMPLES, 3))
        errors = randoms < eta_all[:, np.newaxis, np.newaxis, :]
        panel_err = errors.sum(axis=3) >= 2
        rates = panel_err.mean(axis=2).astype(np.float64)
        rf_sum += rates.sum(axis=1)
        rf_sq_sum += (rates ** 2).sum(axis=1)

    rf_mean = rf_sum / N_SIMS
    rf_std = np.sqrt(np.maximum(rf_sq_sum / N_SIMS - rf_mean ** 2, 0.0))
    return rf_mean, rf_std


# ── Regression ───────────────────────────────────────────────────────

def run_ols(y_raw, keffs, eta_maxs):
    y = np.log(y_raw + EPS)
    X = np.column_stack([np.log(keffs), np.log(eta_maxs + EPS)])
    Xc = sm.add_constant(X)
    fit = sm.OLS(y, Xc).fit()
    return {
        "keff_beta": float(fit.params[1]),
        "keff_t": float(fit.tvalues[1]),
        "keff_p": float(fit.pvalues[1]),
        "eta_max_beta": float(fit.params[2]),
        "eta_max_t": float(fit.tvalues[2]),
        "eta_max_p": float(fit.pvalues[2]),
        "R2": float(fit.rsquared),
        "adj_R2": float(fit.rsquared_adj),
    }


# ── Main ─────────────────────────────────────────────────────────────

def main():
    logger.info("=" * 60)
    logger.info("Plan 001 Step 5: Random-Fault Simulation")
    logger.info(f"  {N_SIMS} simulations x {N_SAMPLES} samples per panel")
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
    rng = np.random.default_rng(42)

    condition_results = {}

    for ds in DATASETS:
        keff_data = mi_data["keff_per_panel"].get(ds, {})
        for atk in ATTACKS:
            cond = f"{ds}x{atk}"
            logger.info(f"\n--- {cond} ---")

            panel_keffs = []
            panel_eta_maxs = []
            panel_eta_all = []
            panel_adaptive_asrs = []
            panel_jids_list = []
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

                cs = {j: clean[ds][j] for j in jids}
                ats = {j: attacked[ds][atk][j] for j in jids}
                adaptive_asr = compute_panel_asr(jids, cs, ats, pairs[ds])

                panel_keffs.append(keff)
                panel_eta_maxs.append(max(etas))
                panel_eta_all.append(etas)
                panel_adaptive_asrs.append(adaptive_asr)
                panel_jids_list.append(jids)

            n_panels = len(panel_keffs)
            logger.info(f"  {n_panels} panels with data, {skipped} skipped")

            if n_panels < 10:
                logger.warning(f"  Too few panels ({n_panels}), skipping")
                condition_results[cond] = {"n_panels": n_panels, "skipped": True}
                continue

            keffs = np.array(panel_keffs)
            eta_maxs = np.array(panel_eta_maxs)
            eta_all = np.array(panel_eta_all)
            adaptive_asrs = np.array(panel_adaptive_asrs)

            logger.info(f"  Simulating {N_SIMS} RF runs...")
            rf_mean, rf_std = simulate_rf_vectorized(eta_all, rng)

            analytical = np.array([analytical_rf_asr(e) for e in eta_all])
            max_dev = np.max(np.abs(rf_mean - analytical))
            logger.info(f"  RF simulation done. Max deviation from analytical: {max_dev:.6f}")

            if np.std(adaptive_asrs) < 1e-10:
                logger.warning(f"  Constant adaptive ASR, skipping regression")
                adaptive_ols = {"keff_beta": 0, "keff_p": 1, "R2": 0, "note": "constant_asr"}
            else:
                adaptive_ols = run_ols(adaptive_asrs, keffs, eta_maxs)

            if np.std(rf_mean) < 1e-10:
                logger.warning(f"  Constant RF ASR, skipping regression")
                rf_ols = {"keff_beta": 0, "keff_p": 1, "R2": 0, "note": "constant_asr"}
            else:
                rf_ols = run_ols(rf_mean, keffs, eta_maxs)

            delta_R2 = rf_ols.get("R2", 0) - adaptive_ols.get("R2", 0)
            keff_gains = (
                rf_ols.get("keff_p", 1) < 0.05
                and rf_ols.get("keff_p", 1) < adaptive_ols.get("keff_p", 1)
            )

            keff_q75 = np.percentile(keffs, 75)
            eta_q25 = np.percentile(eta_maxs, 25)
            hk_le_mask = (keffs >= keff_q75) & (eta_maxs <= eta_q25)
            n_hk_le = int(hk_le_mask.sum())
            hk_le_benefit = None
            hk_le_pval = None
            if n_hk_le >= 5:
                diff = adaptive_asrs[hk_le_mask] - rf_mean[hk_le_mask]
                hk_le_benefit = float(np.mean(diff))
                if np.std(diff) > 1e-10:
                    _, hk_le_pval = stats.ttest_1samp(diff, 0)
                    hk_le_pval = float(hk_le_pval)

            cond_res = {
                "n_panels": n_panels,
                "skipped": False,
                "adaptive": adaptive_ols,
                "random_fault": rf_ols,
                "delta_R2": float(delta_R2),
                "keff_gains_significance": bool(keff_gains),
                "rf_stats": {
                    "mean": float(np.mean(rf_mean)),
                    "std": float(np.mean(rf_std)),
                    "max_analytical_deviation": float(max_dev),
                },
                "adaptive_stats": {
                    "mean": float(np.mean(adaptive_asrs)),
                    "std": float(np.std(adaptive_asrs)),
                },
                "high_keff_low_eta": {
                    "n_panels": n_hk_le,
                    "keff_threshold": float(keff_q75),
                    "eta_threshold": float(eta_q25),
                    "mean_benefit_adaptive_minus_rf": hk_le_benefit,
                    "benefit_pval": hk_le_pval,
                },
            }
            condition_results[cond] = cond_res

            logger.info(
                f"  Adaptive: K_eff B={adaptive_ols.get('keff_beta', 0):+.4f} "
                f"p={adaptive_ols.get('keff_p', 1):.4f} R2={adaptive_ols.get('R2', 0):.4f}"
            )
            logger.info(
                f"  RF:       K_eff B={rf_ols.get('keff_beta', 0):+.4f} "
                f"p={rf_ols.get('keff_p', 1):.4f} R2={rf_ols.get('R2', 0):.4f}"
            )
            logger.info(f"  dR2={delta_R2:+.4f}  K_eff gains significance: {keff_gains}")
            if n_hk_le >= 5:
                logger.info(
                    f"  High-K/Low-eta panels ({n_hk_le}): "
                    f"mean benefit={hk_le_benefit:+.4f} p={hk_le_pval}"
                )

    # ── Summary ──
    valid = {k: v for k, v in condition_results.items() if not v.get("skipped")}
    nv = len(valid)

    if nv > 0:
        n_adapt_sig = sum(
            1 for v in valid.values()
            if v["adaptive"].get("keff_p", 1) < 0.05 and v["adaptive"].get("keff_beta", 0) < 0
        )
        n_rf_sig = sum(
            1 for v in valid.values()
            if v["random_fault"].get("keff_p", 1) < 0.05 and v["random_fault"].get("keff_beta", 0) < 0
        )
        mean_dR2 = float(np.mean([v["delta_R2"] for v in valid.values()]))
        n_gains = sum(1 for v in valid.values() if v["keff_gains_significance"])

        parts = []
        parts.append(
            f"K_eff significantly negative in {n_rf_sig}/{nv} conditions under RF "
            f"vs {n_adapt_sig}/{nv} under adaptive."
        )
        if mean_dR2 > 0:
            parts.append(
                f"RF model explains more variance (mean dR2={mean_dR2:+.3f}), "
                "consistent with independent-error majority vote theory."
            )
        else:
            parts.append(
                f"Adaptive model explains more variance (mean dR2={mean_dR2:+.3f})."
            )
        if n_gains > nv // 2:
            parts.append(
                f"K_eff gains significance in {n_gains}/{nv} conditions under RF, "
                "suggesting diversity benefit is undermined by adaptive attacks."
            )
        interpretation = " ".join(parts)

        summary = {
            "adaptive_keff_sig_negative": f"{n_adapt_sig}/{nv}",
            "random_fault_keff_sig_negative": f"{n_rf_sig}/{nv}",
            "mean_delta_R2": mean_dR2,
            "keff_gains_significance_count": f"{n_gains}/{nv}",
            "interpretation": interpretation,
        }
    else:
        summary = {"note": "No valid conditions to summarize"}

    output = {
        "n_panels": 455,
        "n_simulations": N_SIMS,
        "n_samples_per_sim": N_SAMPLES,
        "models": ALL_MODELS,
        "conditions": condition_results,
        "summary": summary,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / "step5_random_fault_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
    logger.info(f"\nResults saved: {out_path}")

    logger.info("\n" + "=" * 60)
    logger.info("SUMMARY")
    logger.info("=" * 60)
    for k, v in summary.items():
        if k != "interpretation":
            logger.info(f"  {k}: {v}")
    if "interpretation" in summary:
        logger.info(f"\n  {summary['interpretation']}")

    valid_keys = [k for k in condition_results if not condition_results[k].get("skipped")]
    logger.info(f"\n{'Condition':<35} {'Adap R2':>8} {'RF R2':>8} {'dR2':>7} {'Adap Kp':>8} {'RF Kp':>8} {'Gains':>5}")
    logger.info("-" * 85)
    for ck in valid_keys:
        r = condition_results[ck]
        a = r["adaptive"]
        rf = r["random_fault"]
        logger.info(
            f"  {ck:<33} {a.get('R2', 0):>8.4f} {rf.get('R2', 0):>8.4f} "
            f"{r['delta_R2']:>+7.3f} {a.get('keff_p', 1):>8.4f} {rf.get('keff_p', 1):>8.4f} "
            f"{'Y' if r['keff_gains_significance'] else 'N':>5}"
        )


if __name__ == "__main__":
    main()

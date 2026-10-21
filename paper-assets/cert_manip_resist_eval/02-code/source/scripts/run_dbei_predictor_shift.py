#!/usr/bin/env python3
"""Shannon MI entropy predictor shift analysis.

Replaces K_eff with Shannon entropy of normalized pairwise MI as a diversity
predictor. Runs wild cluster bootstrap (Webb 6-point, 999 reps) for K=3,5,7
to test whether the predictor shift pattern holds for alternative diversity metrics.

Output: artifacts/results/plan001/dbei_predictor_shift.json
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import time
import itertools
import logging
import numpy as np
import statsmodels.api as sm
from pathlib import Path
from statsmodels.stats.multitest import multipletests

from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s",
                    handlers=[logging.StreamHandler(),
                              logging.FileHandler("/tmp/dbei_predictor_shift.log")])
log = logging.getLogger(__name__)

EPS = 1e-6
B_BOOT = 999
SEED = 42
FDR_ALPHA = 0.05
K_VALUES = [3, 5, 7]

WEBB_6PT = np.array([-np.sqrt(3/2), -1.0, -np.sqrt(1/2),
                      np.sqrt(1/2),  1.0,  np.sqrt(3/2)])


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


def shannon_mi_entropy(mi_matrix, model_indices):
    """Shannon entropy of normalized pairwise MI values for a panel."""
    mi_vals = []
    for i, idx_i in enumerate(model_indices):
        for j, idx_j in enumerate(model_indices):
            if i < j:
                mi_vals.append(mi_matrix[idx_i, idx_j])
    mi_vals = np.array(mi_vals)
    mi_vals = mi_vals + 1e-10  # avoid zero division
    total = np.sum(mi_vals)
    p = mi_vals / total
    H = -np.sum(p * np.log(p))
    return float(H)


def wild_cluster_bootstrap_webb(y, X_full, cluster_ids, B=B_BOOT, seed=SEED,
                                test_col_idx=1):
    """Wild cluster bootstrap with Webb 6-point weights."""
    n, p = X_full.shape
    unique_clusters = np.unique(cluster_ids)
    n_clusters = len(unique_clusters)

    cluster_to_idx = {c: i for i, c in enumerate(unique_clusters)}
    panel_cluster_idx = np.array([cluster_to_idx[c] for c in cluster_ids])

    fit_full = sm.OLS(y, X_full).fit()
    t_original = fit_full.tvalues[test_col_idx]

    cols_restricted = [i for i in range(p) if i != test_col_idx]
    X_restricted = X_full[:, cols_restricted]
    fit_restricted = sm.OLS(y, X_restricted).fit()
    y_hat_r = fit_restricted.fittedvalues
    e_r = y - y_hat_r

    rng = np.random.RandomState(seed)
    t_boot = np.empty(B)

    for b in range(B):
        w_cluster = WEBB_6PT[rng.randint(0, 6, size=n_clusters)]
        w_panel = w_cluster[panel_cluster_idx]
        y_boot = y_hat_r + w_panel * e_r
        try:
            fit_b = sm.OLS(y_boot, X_full).fit()
            t_boot[b] = fit_b.tvalues[test_col_idx]
        except Exception:
            t_boot[b] = 0.0

    p_value = (1 + np.sum(np.abs(t_boot) >= np.abs(t_original))) / (1 + B)
    return float(p_value)


def bootstrap_K_positions(y, X_full, panel_jids_list, K, B=B_BOOT, seed=SEED,
                          test_col_idx=1):
    """Run wild cluster bootstrap for K positions, return per-position p and max."""
    position_ps = []
    for pos in range(K):
        cluster_ids = np.array([jids[pos] for jids in panel_jids_list])
        p_val = wild_cluster_bootstrap_webb(
            y, X_full, cluster_ids, B=B, seed=seed + pos * 100,
            test_col_idx=test_col_idx
        )
        position_ps.append(p_val)
    return position_ps, max(position_ps)


def main():
    t_start = time.time()
    log.info("Loading data...")
    clean, attacked = load_all_scores()
    pairs = load_pairs()
    mi_data = load_mi_data()
    mi_matrices = mi_data["mi_matrix"]

    # Precompute individual ASR
    ind_asr = {}
    for ds in DATASETS:
        for atk in ATTACKS:
            for mid in ALL_MODELS:
                if mid in clean.get(ds, {}) and mid in attacked.get(ds, {}).get(atk, {}):
                    ind_asr[(ds, atk, mid)] = compute_individual_asr(
                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds])

    log.info(f"Individual ASR computed: {len(ind_asr)} entries")

    all_k_results = {}

    for K in K_VALUES:
        all_combos = list(itertools.combinations(range(len(ALL_MODELS)), K))
        n_combos = len(all_combos)
        log.info(f"\n{'='*70}\nK={K}: C(15,{K})={n_combos} panels\n{'='*70}")

        k_results = {"K": K, "n_total_panels": n_combos, "conditions": {}}

        for ds in DATASETS:
            mi_mat = np.array(mi_matrices[ds])
            for atk in ATTACKS:
                cond = f"{ds}x{atk}"
                t0 = time.time()

                p_asrs, p_keffs, p_shannons, p_etas = [], [], [], []
                panel_jids_list = []

                for combo in all_combos:
                    jids = tuple(ALL_MODELS[i] for i in combo)
                    if not all((ds, atk, j) in ind_asr for j in jids):
                        continue

                    keff = mi_based_keff(mi_mat, list(combo))
                    h_div = shannon_mi_entropy(mi_mat, list(combo))
                    eta_max = max(ind_asr[(ds, atk, j)] for j in jids)

                    cs = {j: clean[ds][j] for j in jids}
                    ats = {j: attacked[ds][atk][j] for j in jids}
                    asr = compute_panel_asr(jids, cs, ats, pairs[ds])

                    p_asrs.append(asr)
                    p_keffs.append(keff)
                    p_shannons.append(h_div)
                    p_etas.append(eta_max)
                    panel_jids_list.append(jids)

                n_panels = len(p_asrs)
                if n_panels < 10:
                    log.info(f"  [{cond}] SKIP: {n_panels} panels")
                    k_results["conditions"][cond] = {"skipped": True}
                    continue

                y = np.log(np.array(p_asrs) + EPS)
                log_keff = np.log(np.array(p_keffs))
                h_arr = np.array(p_shannons)
                log_eta = np.log(np.array(p_etas) + EPS)
                sd_y = np.std(y)

                # --- Model 1: Shannon entropy ---
                X_s = np.column_stack([np.ones(n_panels), h_arr, log_eta])
                fit_s = sm.OLS(y, X_s).fit()
                shan_std = float(fit_s.params[1] * np.std(h_arr) / sd_y) if sd_y > 1e-12 else 0.0
                eta_std_s = float(fit_s.params[2] * np.std(log_eta) / sd_y) if sd_y > 1e-12 else 0.0

                shan_pos_ps, shan_max_p = bootstrap_K_positions(
                    y, X_s, panel_jids_list, K, B=B_BOOT, seed=SEED, test_col_idx=1)
                eta_s_pos_ps, eta_s_max_p = bootstrap_K_positions(
                    y, X_s, panel_jids_list, K, B=B_BOOT, seed=SEED + 7, test_col_idx=2)

                # --- Model 2: K_eff ---
                X_k = np.column_stack([np.ones(n_panels), log_keff, log_eta])
                fit_k = sm.OLS(y, X_k).fit()
                keff_std = float(fit_k.params[1] * np.std(log_keff) / sd_y) if sd_y > 1e-12 else 0.0
                eta_std_k = float(fit_k.params[2] * np.std(log_eta) / sd_y) if sd_y > 1e-12 else 0.0

                keff_pos_ps, keff_max_p = bootstrap_K_positions(
                    y, X_k, panel_jids_list, K, B=B_BOOT, seed=SEED, test_col_idx=1)
                eta_k_pos_ps, eta_k_max_p = bootstrap_K_positions(
                    y, X_k, panel_jids_list, K, B=B_BOOT, seed=SEED + 7, test_col_idx=2)

                corr_sh_keff = float(np.corrcoef(h_arr, log_keff)[0, 1])

                elapsed = time.time() - t0
                log.info(f"  [{cond}] n={n_panels} "
                         f"shan_p={shan_max_p:.4f} keff_p={keff_max_p:.4f} "
                         f"r={corr_sh_keff:.3f} ({elapsed:.1f}s)")

                k_results["conditions"][cond] = {
                    "n_panels": n_panels,
                    "skipped": False,
                    "shannon": {
                        "std_beta": shan_std,
                        "beta": float(fit_s.params[1]),
                        "boot_p_positions": shan_pos_ps,
                        "final_p": shan_max_p,
                        "R2": float(fit_s.rsquared),
                    },
                    "keff": {
                        "std_beta": keff_std,
                        "beta": float(fit_k.params[1]),
                        "boot_p_positions": keff_pos_ps,
                        "final_p": keff_max_p,
                        "R2": float(fit_k.rsquared),
                    },
                    "eta_in_shannon_model": {
                        "std_beta": eta_std_s,
                        "final_p": eta_s_max_p,
                    },
                    "eta_in_keff_model": {
                        "std_beta": eta_std_k,
                        "final_p": eta_k_max_p,
                    },
                    "corr_shannon_keff": corr_sh_keff,
                }

        # FDR correction
        valid_keys = [c for c in k_results["conditions"]
                      if not k_results["conditions"][c].get("skipped")]

        if valid_keys:
            shan_ps = [k_results["conditions"][c]["shannon"]["final_p"] for c in valid_keys]
            keff_ps = [k_results["conditions"][c]["keff"]["final_p"] for c in valid_keys]
            eta_s_ps = [k_results["conditions"][c]["eta_in_shannon_model"]["final_p"] for c in valid_keys]
            eta_k_ps = [k_results["conditions"][c]["eta_in_keff_model"]["final_p"] for c in valid_keys]

            _, shan_fdr, _, _ = multipletests(shan_ps, alpha=FDR_ALPHA, method="fdr_bh")
            _, keff_fdr, _, _ = multipletests(keff_ps, alpha=FDR_ALPHA, method="fdr_bh")
            _, eta_s_fdr, _, _ = multipletests(eta_s_ps, alpha=FDR_ALPHA, method="fdr_bh")
            _, eta_k_fdr, _, _ = multipletests(eta_k_ps, alpha=FDR_ALPHA, method="fdr_bh")

            for i, c in enumerate(valid_keys):
                k_results["conditions"][c]["shannon"]["fdr_p"] = float(shan_fdr[i])
                k_results["conditions"][c]["keff"]["fdr_p"] = float(keff_fdr[i])
                k_results["conditions"][c]["eta_in_shannon_model"]["fdr_p"] = float(eta_s_fdr[i])
                k_results["conditions"][c]["eta_in_keff_model"]["fdr_p"] = float(eta_k_fdr[i])

            shan_sig = sum(1 for p in shan_fdr if p < FDR_ALPHA)
            keff_sig = sum(1 for p in keff_fdr if p < FDR_ALPHA)
            eta_s_sig = sum(1 for p in eta_s_fdr if p < FDR_ALPHA)
            eta_k_sig = sum(1 for p in eta_k_fdr if p < FDR_ALPHA)

            k_results["summary"] = {
                "shannon_fdr_sig": f"{shan_sig}/{len(valid_keys)}",
                "keff_fdr_sig": f"{keff_sig}/{len(valid_keys)}",
                "eta_in_shannon_fdr_sig": f"{eta_s_sig}/{len(valid_keys)}",
                "eta_in_keff_fdr_sig": f"{eta_k_sig}/{len(valid_keys)}",
            }

            log.info(f"\n  K={K} SUMMARY: Shannon={shan_sig}/{len(valid_keys)}, "
                     f"K_eff={keff_sig}/{len(valid_keys)}, "
                     f"η(shan)={eta_s_sig}/{len(valid_keys)}, "
                     f"η(keff)={eta_k_sig}/{len(valid_keys)}")

        all_k_results[f"K{K}"] = k_results

    # --- Build output ---
    predictor_shift = {}
    keff_comparison = {}
    correlations = {}

    for K in K_VALUES:
        kk = f"K{K}"
        if kk in all_k_results and "summary" in all_k_results[kk]:
            s = all_k_results[kk]["summary"]
            predictor_shift[kk] = {
                "diversity_sig": s["shannon_fdr_sig"],
                "eta_sig": s["eta_in_shannon_fdr_sig"],
            }
            keff_comparison[kk] = {
                "keff_sig": s["keff_fdr_sig"],
                "diversity_sig": s["shannon_fdr_sig"],
            }
            conds = [c for c in all_k_results[kk]["conditions"]
                     if not all_k_results[kk]["conditions"][c].get("skipped")]
            if conds:
                correlations[kk] = round(float(np.mean([
                    all_k_results[kk]["conditions"][c]["corr_shannon_keff"]
                    for c in conds])), 4)

    shan_sigs = []
    keff_sigs = []
    for K in K_VALUES:
        kk = f"K{K}"
        if kk in all_k_results and "summary" in all_k_results[kk]:
            s = all_k_results[kk]["summary"]
            shan_sigs.append(int(s["shannon_fdr_sig"].split("/")[0]))
            keff_sigs.append(int(s["keff_fdr_sig"].split("/")[0]))

    shift_matches = (len(shan_sigs) >= 2 and shan_sigs[-1] >= shan_sigs[0])

    output = {
        "diversity_metric": "Shannon_MI_entropy",
        "formula": "H_panel = -sum(p_ij * log(p_ij)), p_ij = MI_ij / sum(MI_all_pairs)",
        "reference": "Shannon entropy of normalized pairwise mutual information",
        "bootstrap": {
            "method": "wild_cluster_bootstrap",
            "weights": "Webb_6point",
            "B": B_BOOT,
            "clustering": "max_p_across_K_positions",
        },
        "predictor_shift": predictor_shift,
        "keff_comparison": keff_comparison,
        "shift_pattern_matches_keff": bool(shift_matches),
        "correlation_dbei_keff": correlations,
        "conditions_detail": all_k_results,
        "elapsed_seconds": round(time.time() - t_start, 1),
    }

    out_path = Path("/root/cert_manip_resist_eval/artifacts/results/plan001/"
                    "dbei_predictor_shift.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)

    log.info(f"\nSaved: {out_path}")
    log.info(f"Total: {time.time() - t_start:.1f}s")

    # Print summary table
    log.info(f"\n{'='*60}")
    log.info("PREDICTOR SHIFT COMPARISON")
    log.info(f"{'='*60}")
    log.info(f"{'K':>3}  {'Shannon sig':>12}  {'K_eff sig':>10}  {'η(shan)':>8}  {'η(keff)':>8}  {'r(S,K)':>7}")
    for K in K_VALUES:
        kk = f"K{K}"
        if kk in all_k_results and "summary" in all_k_results[kk]:
            s = all_k_results[kk]["summary"]
            r = correlations.get(kk, "N/A")
            log.info(f"{K:>3}  {s['shannon_fdr_sig']:>12}  {s['keff_fdr_sig']:>10}  "
                     f"{s['eta_in_shannon_fdr_sig']:>8}  {s['eta_in_keff_fdr_sig']:>8}  "
                     f"{r:>7}")
    log.info(f"Shift pattern matches K_eff: {shift_matches}")


if __name__ == "__main__":
    main()

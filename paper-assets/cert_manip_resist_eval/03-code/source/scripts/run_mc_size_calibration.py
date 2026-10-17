#!/usr/bin/env python3
"""Monte Carlo Size Calibration for Wild Cluster Bootstrap.

Tests empirical size (Type I error rate) when cluster count is small
(K=3: ~13 clusters, K=5: ~11, K=7: ~9 per position).

Method: For each K and condition, permute K_eff across panels (breaking
K_eff-ASR link, keeping ASR-eta_max paired). Run wild cluster bootstrap
with max-p across K position clusters. Report rejection rate at alpha=0.05.
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import time
import itertools
import numpy as np
from pathlib import Path

from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)

EPS = 1e-6
N_PERMS = 1000
B_BOOT = 999
ALPHA = 0.05
OVER_REJECT_THRESHOLD = 0.075
SEED = 42


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


def fast_wcb_pvalue(y, X, cluster_ids, B, rng, test_col_idx=1):
    """Vectorized wild cluster bootstrap p-value for one clustering."""
    n, p = X.shape
    unique_clusters = np.unique(cluster_ids)
    n_clusters = len(unique_clusters)

    cluster_to_idx = {c: i for i, c in enumerate(unique_clusters)}
    cidx = np.array([cluster_to_idx[c] for c in cluster_ids])

    try:
        XtX_inv = np.linalg.inv(X.T @ X)
    except np.linalg.LinAlgError:
        return 1.0, n_clusters

    hat = XtX_inv @ X.T
    coef_full = hat @ y
    resid_full = y - X @ coef_full
    s2_full = np.sum(resid_full**2) / (n - p)
    se_full = np.sqrt(s2_full * XtX_inv[test_col_idx, test_col_idx])
    if se_full <= 0:
        return 1.0, n_clusters
    t_orig = coef_full[test_col_idx] / se_full

    cols_r = [i for i in range(p) if i != test_col_idx]
    X_r = X[:, cols_r]
    try:
        XrXr_inv = np.linalg.inv(X_r.T @ X_r)
    except np.linalg.LinAlgError:
        return 1.0, n_clusters
    coef_r = XrXr_inv @ (X_r.T @ y)
    y_hat_r = X_r @ coef_r
    e_r = y - y_hat_r

    W = rng.choice([-1, 1], size=(B, n_clusters))
    W_panel = W[:, cidx]
    Y_boot = y_hat_r[None, :] + W_panel * e_r[None, :]

    Coefs = Y_boot @ hat.T  # (B, p)
    Resid = Y_boot - Coefs @ X.T  # (B, n)
    S2 = np.sum(Resid**2, axis=1) / (n - p)
    SE = np.sqrt(S2 * XtX_inv[test_col_idx, test_col_idx])

    mask = SE > 0
    T_boot = np.zeros(B)
    T_boot[mask] = Coefs[mask, test_col_idx] / SE[mask]

    p_value = (1 + np.sum(np.abs(T_boot) >= np.abs(t_orig))) / (1 + B)
    return float(p_value), n_clusters


def mc_calibration_one(y, log_keff, log_eta, panel_jids_list, K,
                       n_perms, B, alpha, rng):
    """Monte Carlo size calibration for one K x condition."""
    n = len(y)
    n_reject = 0

    for perm in range(n_perms):
        perm_idx = rng.permutation(n)
        log_keff_perm = log_keff[perm_idx]

        X = np.column_stack([np.ones(n), log_keff_perm, log_eta])

        position_ps = []
        for pos in range(K):
            cluster_ids = np.array([jids[pos] for jids in panel_jids_list])
            p_val, _ = fast_wcb_pvalue(y, X, cluster_ids, B, rng,
                                       test_col_idx=1)
            position_ps.append(p_val)

        max_p = max(position_ps)
        if max_p < alpha:
            n_reject += 1

    return n_reject / n_perms


def build_panel_data(K, combos, mi_mat, ind_asr, clean_ds, attacked_ds,
                     ds_pairs, ds, atk):
    """Build panel-level arrays for one K x condition."""
    p_asrs, p_keffs, p_etas = [], [], []
    p_jids = []

    for combo in combos:
        jids = [ALL_MODELS[i] for i in combo]
        if not all((ds, atk, j) in ind_asr for j in jids):
            continue

        keff = mi_based_keff(mi_mat, list(combo))
        eta_max = max(ind_asr[(ds, atk, j)] for j in jids)

        cs = {j: clean_ds[j] for j in jids}
        ats = {j: attacked_ds[j] for j in jids}
        asr = compute_panel_asr(jids, cs, ats, ds_pairs)

        p_asrs.append(asr)
        p_keffs.append(keff)
        p_etas.append(eta_max)
        p_jids.append(jids)

    return p_asrs, p_keffs, p_etas, p_jids


def main():
    t_start = time.time()

    print("Loading data...")
    clean, attacked = load_all_scores()
    pairs = load_pairs()
    mi_data = load_mi_data()
    mi_matrices = {ds: np.array(mi_data["mi_matrix"][ds]) for ds in DATASETS}

    print("Computing individual ASR...")
    ind_asr = {}
    for ds in DATASETS:
        for atk in ATTACKS:
            for mid in ALL_MODELS:
                if mid in clean[ds] and mid in attacked[ds].get(atk, {}):
                    ind_asr[(ds, atk, mid)] = compute_individual_asr(
                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds])
    print(f"  {len(ind_asr)} individual ASR values")

    K_values = [3, 5, 7]
    results = {}
    rng = np.random.RandomState(SEED)

    for K in K_values:
        k_label = f"K{K}"
        combos = list(itertools.combinations(range(len(ALL_MODELS)), K))
        n_combos = len(combos)
        print(f"\n{'='*60}")
        print(f"K={K}: C(15,{K}) = {n_combos} panels")
        print(f"{'='*60}")

        results[k_label] = {}

        for ds in DATASETS:
            mi_mat = mi_matrices[ds]
            for atk in ATTACKS:
                cond = f"{ds}x{atk}"
                t0 = time.time()

                clean_ds = clean.get(ds, {})
                attacked_ds = attacked.get(ds, {}).get(atk, {})
                ds_pairs = pairs.get(ds, [])

                if not clean_ds or not attacked_ds or not ds_pairs:
                    print(f"  {cond}: SKIP (missing data)")
                    results[k_label][cond] = {"skipped": True}
                    continue

                p_asrs, p_keffs, p_etas, p_jids = build_panel_data(
                    K, combos, mi_mat, ind_asr, clean_ds, attacked_ds,
                    ds_pairs, ds, atk)

                n_panels = len(p_asrs)
                if n_panels < 10:
                    print(f"  {cond}: SKIP (n={n_panels})")
                    results[k_label][cond] = {"skipped": True}
                    continue

                y = np.log(np.array(p_asrs) + EPS)
                log_keff = np.log(np.array(p_keffs))
                log_eta = np.log(np.array(p_etas) + EPS)

                if np.std(y) < 1e-10:
                    print(f"  {cond}: SKIP (constant ASR)")
                    results[k_label][cond] = {"skipped": True}
                    continue

                n_clusters_per_pos = []
                for pos in range(K):
                    cl = set(jids[pos] for jids in p_jids)
                    n_clusters_per_pos.append(len(cl))

                rej_rate = mc_calibration_one(
                    y, log_keff, log_eta, p_jids, K,
                    N_PERMS, B_BOOT, ALPHA, rng)

                elapsed = time.time() - t0
                over_reject = rej_rate > OVER_REJECT_THRESHOLD
                flag = " *** OVER-REJECT ***" if over_reject else ""
                print(f"  {cond}: rej_rate={rej_rate:.4f} "
                      f"panels={n_panels} clusters={n_clusters_per_pos} "
                      f"({elapsed:.1f}s){flag}")

                results[k_label][cond] = {
                    "rejection_rate": float(rej_rate),
                    "over_reject": bool(over_reject),
                    "n_panels": n_panels,
                    "n_clusters_per_position": n_clusters_per_pos,
                }

    summary = {}
    for K in K_values:
        k_label = f"K{K}"
        rates = [v["rejection_rate"] for v in results[k_label].values()
                 if not v.get("skipped", False)]
        if rates:
            summary[f"{k_label}_mean_rate"] = round(float(np.mean(rates)), 4)
            summary[f"{k_label}_max_rate"] = round(float(np.max(rates)), 4)
            summary[f"{k_label}_min_rate"] = round(float(np.min(rates)), 4)
            summary[f"{k_label}_n_over_reject"] = int(
                sum(1 for r in rates if r > OVER_REJECT_THRESHOLD))
            summary[f"{k_label}_n_conditions"] = len(rates)

    total_elapsed = time.time() - t_start

    output = {
        "method": "permutation_wild_cluster_bootstrap",
        "n_permutations": N_PERMS,
        "bootstrap_B": B_BOOT,
        "nominal_alpha": ALPHA,
        "over_reject_threshold": OVER_REJECT_THRESHOLD,
        "seed": SEED,
        "weight_distribution": "rademacher",
        "clustering": "max_p_across_K_positions",
        "total_time_seconds": round(total_elapsed, 1),
        "results": results,
        "summary": summary,
    }

    out_path = Path("/root/cert_manip_resist_eval/artifacts/results/plan001/"
                    "monte_carlo_size_calibration.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default,
                  ensure_ascii=False)
    print(f"\nSaved: {out_path}")
    print(f"Total time: {total_elapsed:.0f}s")

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    for K in K_values:
        k_label = f"K{K}"
        if f"{k_label}_mean_rate" in summary:
            print(f"  {k_label}: mean_rej={summary[f'{k_label}_mean_rate']:.4f} "
                  f"max={summary[f'{k_label}_max_rate']:.4f} "
                  f"over_reject={summary[f'{k_label}_n_over_reject']}/"
                  f"{summary[f'{k_label}_n_conditions']}")


if __name__ == "__main__":
    main()

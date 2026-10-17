#!/usr/bin/env python3
"""Wild Cluster Bootstrap for K_eff significance — reliable inference with 15 clusters.

Implements Webb (2023) / Cameron & Miller (2015) wild cluster bootstrap:
  - Restricted model under H0: β_coef = 0
  - Rademacher weights drawn per cluster
  - Bootstrap t-statistics compared to original

Cluster assignment: primary judge = alphabetically smallest judge in panel.
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
from statsmodels.stats.multitest import multipletests

from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)

EPS = 1e-6
FDR_ALPHA = 0.05
B_BOOT = 9999
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


def compute_keff(panel_jids, mi_matrix, model_to_idx):
    K = len(panel_jids)
    max_mi = 0.0
    for a, b in itertools.combinations(panel_jids, 2):
        ia, ib = model_to_idx[a], model_to_idx[b]
        max_mi = max(max_mi, mi_matrix[ia][ib])
    return 1 + (K - 1) * np.exp(-2 * max_mi)


def wild_cluster_bootstrap(y, X_full, cluster_ids, B=B_BOOT, seed=SEED,
                           test_col_idx=1):
    """Wild cluster bootstrap p-value for coefficient at test_col_idx.

    Args:
        y: (n,) response
        X_full: (n, p) design matrix with intercept
        cluster_ids: (n,) cluster labels
        B: number of bootstrap replications
        seed: random seed
        test_col_idx: column index to test (1=log_keff, 2=log_eta)

    Returns:
        boot_p: bootstrap p-value
        t_original: original t-statistic
    """
    n, p = X_full.shape
    unique_clusters = np.unique(cluster_ids)
    n_clusters = len(unique_clusters)

    # Map cluster labels to indices for fast lookup
    cluster_to_idx = {c: i for i, c in enumerate(unique_clusters)}
    panel_cluster_idx = np.array([cluster_to_idx[c] for c in cluster_ids])

    # Original full model fit
    fit_full = sm.OLS(y, X_full).fit()
    t_original = fit_full.tvalues[test_col_idx]

    # Restricted model: drop the test column
    cols_restricted = [i for i in range(p) if i != test_col_idx]
    X_restricted = X_full[:, cols_restricted]
    fit_restricted = sm.OLS(y, X_restricted).fit()
    y_hat_r = fit_restricted.fittedvalues
    e_r = y - y_hat_r

    rng = np.random.RandomState(seed)
    t_boot = np.empty(B)

    for b in range(B):
        # Rademacher weights per cluster
        w_cluster = rng.choice([-1, 1], size=n_clusters)
        w_panel = w_cluster[panel_cluster_idx]

        # Bootstrap response
        y_boot = y_hat_r + w_panel * e_r

        # Fit full model on bootstrap data
        try:
            fit_b = sm.OLS(y_boot, X_full).fit()
            t_boot[b] = fit_b.tvalues[test_col_idx]
        except Exception:
            t_boot[b] = 0.0

    # Two-sided p-value
    p_value = (1 + np.sum(np.abs(t_boot) >= np.abs(t_original))) / (1 + B)
    return float(p_value), float(t_original)


def main(B=B_BOOT):
    print(f"Loading data...")
    clean, attacked = load_all_scores()
    pairs = load_pairs()
    mi_data = load_mi_data()

    mi_models = mi_data["models"]
    model_to_idx = {m: i for i, m in enumerate(mi_models)}

    all_panels = list(itertools.combinations(ALL_MODELS, 3))
    print(f"Total panels: {len(all_panels)}")

    condition_keys = []
    for ds in DATASETS:
        for atk in ATTACKS:
            condition_keys.append(f"{ds}x{atk}")

    results = {}

    for cond_idx, cond_key in enumerate(condition_keys):
        ds, atk = cond_key.split("x", 1)
        print(f"\n[{cond_idx+1}/12] {cond_key}")

        ds_clean = clean.get(ds, {})
        ds_attacked = attacked.get(ds, {}).get(atk, {})
        ds_pairs = pairs.get(ds, [])

        if not ds_clean or not ds_attacked or not ds_pairs:
            print(f"  SKIP: missing data")
            results[cond_key] = {"skipped": True}
            continue

        # Compute per-model individual ASR (for eta_max)
        individual_asr = {}
        for mid in ALL_MODELS:
            if mid in ds_clean and mid in ds_attacked:
                individual_asr[mid] = compute_individual_asr(
                    ds_clean[mid], ds_attacked[mid], ds_pairs)

        # Build panel data
        panel_asrs = []
        panel_keffs = []
        panel_etas = []
        panel_clusters = []
        panel_jids_list = []

        # Determine MI matrix for this dataset
        mi_key = ds
        if mi_key not in mi_data["mi_matrix"]:
            mi_key = list(mi_data["mi_matrix"].keys())[0]
        mi_matrix = mi_data["mi_matrix"][mi_key]

        for panel_jids in all_panels:
            # Check all judges have data
            if not all(j in ds_clean and j in ds_attacked for j in panel_jids):
                continue
            if not all(j in individual_asr for j in panel_jids):
                continue

            asr = compute_panel_asr(panel_jids, ds_clean, ds_attacked, ds_pairs)
            keff = compute_keff(panel_jids, mi_matrix, model_to_idx)
            eta_max = max(individual_asr[j] for j in panel_jids)

            # Primary cluster = alphabetically smallest judge
            primary_cluster = min(panel_jids)

            panel_asrs.append(asr)
            panel_keffs.append(keff)
            panel_etas.append(eta_max)
            panel_clusters.append(primary_cluster)
            panel_jids_list.append(panel_jids)

        n_panels = len(panel_asrs)
        print(f"  Panels: {n_panels}")

        if n_panels < 10:
            print(f"  SKIP: too few panels")
            results[cond_key] = {"skipped": True, "n_panels": n_panels}
            continue

        # Log transform
        y = np.log(np.array(panel_asrs) + EPS)
        log_keff = np.log(np.array(panel_keffs))
        log_eta = np.log(np.array(panel_etas) + EPS)

        X = np.column_stack([np.ones(n_panels), log_keff, log_eta])
        cluster_ids = np.array(panel_clusters)

        n_clusters = len(np.unique(cluster_ids))
        print(f"  Clusters: {n_clusters}")

        # OLS for reference
        fit_ols = sm.OLS(y, X).fit()
        print(f"  OLS: K_eff t={fit_ols.tvalues[1]:.3f} p={fit_ols.pvalues[1]:.2e}, "
              f"eta t={fit_ols.tvalues[2]:.3f} p={fit_ols.pvalues[2]:.2e}")

        # Wild cluster bootstrap for K_eff (col 1)
        keff_boot_p, keff_t_orig = wild_cluster_bootstrap(
            y, X, cluster_ids, B=B, test_col_idx=1)

        # Wild cluster bootstrap for eta_max (col 2)
        eta_boot_p, eta_t_orig = wild_cluster_bootstrap(
            y, X, cluster_ids, B=B, test_col_idx=2)

        print(f"  Bootstrap: K_eff p={keff_boot_p:.4f}, eta p={eta_boot_p:.4f}")

        results[cond_key] = {
            "n_panels": n_panels,
            "n_clusters": n_clusters,
            "keff_boot_p": keff_boot_p,
            "eta_boot_p": eta_boot_p,
            "keff_t_original": keff_t_orig,
            "eta_t_original": eta_t_orig,
            "keff_ols_p": float(fit_ols.pvalues[1]),
            "eta_ols_p": float(fit_ols.pvalues[2]),
            "keff_beta": float(fit_ols.params[1]),
            "eta_beta": float(fit_ols.params[2]),
            "skipped": False,
        }

    # FDR correction
    valid_keys = [k for k in condition_keys if not results.get(k, {}).get("skipped", True)]

    keff_boot_pvals = [results[k]["keff_boot_p"] for k in valid_keys]
    eta_boot_pvals = [results[k]["eta_boot_p"] for k in valid_keys]

    if len(valid_keys) > 0:
        _, keff_fdr_p, _, _ = multipletests(keff_boot_pvals, alpha=FDR_ALPHA, method="fdr_bh")
        _, eta_fdr_p, _, _ = multipletests(eta_boot_pvals, alpha=FDR_ALPHA, method="fdr_bh")

        for i, k in enumerate(valid_keys):
            results[k]["keff_fdr_p"] = float(keff_fdr_p[i])
            results[k]["eta_fdr_p"] = float(eta_fdr_p[i])

    # Summary
    keff_fdr_sig = sum(1 for k in valid_keys if results[k]["keff_fdr_p"] < FDR_ALPHA)
    eta_fdr_sig = sum(1 for k in valid_keys if results[k]["eta_fdr_p"] < FDR_ALPHA)
    keff_sig_pos = sum(1 for k in valid_keys
                       if results[k]["keff_fdr_p"] < FDR_ALPHA and results[k]["keff_beta"] > 0)
    keff_sig_neg = keff_fdr_sig - keff_sig_pos

    print(f"\n{'='*60}")
    print(f"SUMMARY (B={B})")
    print(f"{'='*60}")
    print(f"  K_eff FDR sig: {keff_fdr_sig}/12 ({keff_sig_pos}+ / {keff_sig_neg}-)")
    print(f"  eta_max FDR sig: {eta_fdr_sig}/12")

    print(f"\n{'='*60}")
    print(f"COMPARISON TABLE")
    print(f"{'='*60}")
    print(f"  {'Method':<25} {'eta_max FDR sig':>15} {'K_eff FDR sig':>15}")
    print(f"  {'Canonical OLS':<25} {'11/12':>15} {'8/12':>15}")
    print(f"  {'Clustered SE':<25} {'8/12':>15} {'0/12':>15}")
    print(f"  {'Mixed Effects':<25} {'7/12':>15} {'3/12':>15}")
    print(f"  {'Wild Bootstrap':<25} {f'{eta_fdr_sig}/12':>15} {f'{keff_fdr_sig}/12':>15}")

    print(f"\nPer-condition details:")
    print(f"  {'Condition':<35} {'K_eff boot_p':>12} {'K_eff FDR_p':>12} {'sig':>5} "
          f"{'eta boot_p':>12} {'eta FDR_p':>12} {'sig':>5}")
    for k in valid_keys:
        r = results[k]
        ks = "*" if r["keff_fdr_p"] < FDR_ALPHA else ""
        es = "*" if r["eta_fdr_p"] < FDR_ALPHA else ""
        print(f"  {k:<35} {r['keff_boot_p']:>12.4f} {r['keff_fdr_p']:>12.4f} {ks:>5} "
              f"{r['eta_boot_p']:>12.4f} {r['eta_fdr_p']:>12.4f} {es:>5}")

    # Save output
    output = {
        "method": "wild_cluster_bootstrap",
        "B": B,
        "weight_distribution": "rademacher",
        "n_clusters": 15,
        "cluster_assignment": "primary_judge_alphabetical",
        "seed": SEED,
        "per_condition": {k: results[k] for k in valid_keys},
        "summary": {
            "keff_fdr_sig": f"{keff_fdr_sig}/12",
            "eta_fdr_sig": f"{eta_fdr_sig}/12",
            "keff_sig_positive": keff_sig_pos,
            "keff_sig_negative": keff_sig_neg,
        },
        "comparison": {
            "ols": {"eta": "11/12", "keff": "8/12"},
            "clustered_se": {"eta": "8/12", "keff": "0/12"},
            "mixed_effects": {"eta": "7/12", "keff": "3/12"},
            "wild_bootstrap": {"eta": f"{eta_fdr_sig}/12", "keff": f"{keff_fdr_sig}/12"},
        },
    }

    out_path = Path("/root/cert_manip_resist_eval/artifacts/results/plan001/wild_cluster_bootstrap.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--B", type=int, default=B_BOOT)
    args = parser.parse_args()
    main(B=args.B)

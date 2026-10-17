#!/usr/bin/env python3
"""RF K_eff non-independence correction.

Applies clustered SE and wild cluster bootstrap v2 corrections to the
Random-Fault regime, matching the methodology used for adaptive regime.

RF definition: each judge j independently errs with probability (1 - clean_acc_j).
Panel RF ASR = P(>=2/3 judges wrong) via Monte Carlo simulation.
eta_max_rf = max(1 - clean_acc_j) among 3 panel judges.
K_eff from canonical MI matrix (same panels as adaptive).

Since RF error rate depends only on clean accuracy (dataset-level, not
attack-level), there are 2 conditions (1 per dataset). No FDR applied.
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
from scipy.stats import t as t_dist

from src.unified_data_loader import (
    ALL_MODELS, DATASETS,
    load_all_scores, load_pairs, load_mi_data,
    compute_clean_accuracy,
)

EPS = 1e-6
B_BOOT = 9999
SEED = 42
N_SIM_TRIALS = 10000


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


def analytical_rf_asr(e):
    e1, e2, e3 = e
    return e1*e2 + e1*e3 + e2*e3 - 2*e1*e2*e3


def simulate_rf_asr(panel_error_rates, n_trials=N_SIM_TRIALS, rng=None):
    if rng is None:
        rng = np.random.default_rng(SEED)
    n_panels = panel_error_rates.shape[0]
    randoms = rng.random((n_panels, n_trials, 3))
    errors = randoms < panel_error_rates[:, np.newaxis, :]
    majority_wrong = errors.sum(axis=2) >= 2
    return majority_wrong.mean(axis=1)


def wild_cluster_bootstrap(y, X_full, cluster_ids, B=B_BOOT, seed=SEED,
                           test_col_idx=1):
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
        w_cluster = rng.choice([-1, 1], size=n_clusters)
        w_panel = w_cluster[panel_cluster_idx]
        y_boot = y_hat_r + w_panel * e_r
        try:
            fit_b = sm.OLS(y_boot, X_full).fit()
            t_boot[b] = fit_b.tvalues[test_col_idx]
        except Exception:
            t_boot[b] = 0.0

    p_value = (1 + np.sum(np.abs(t_boot) >= np.abs(t_original))) / (1 + B)
    return float(p_value), float(t_original)


def bootstrap_3positions(y, X_full, panel_jids_list, B=B_BOOT, seed=SEED,
                         test_col_idx=1):
    position_ps = []
    position_n_clusters = []
    for pos in range(3):
        cluster_ids = np.array([jids[pos] for jids in panel_jids_list])
        p_val, _ = wild_cluster_bootstrap(
            y, X_full, cluster_ids, B=B, seed=seed,
            test_col_idx=test_col_idx
        )
        position_ps.append(p_val)
        position_n_clusters.append(len(set(cluster_ids)))
    max_p = max(position_ps)
    return position_ps, max_p, position_n_clusters


def clustered_se_3positions(y, X_full, panel_jids_list, n_panels):
    fit_ols = sm.OLS(y, X_full).fit()
    max_se = np.zeros(3)

    for pos in range(3):
        cluster_var = np.array([jids[pos] for jids in panel_jids_list])
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
            print(f"  WARNING: Clustering on position {pos} failed: {e}")
            for coef_idx in range(3):
                max_se[coef_idx] = max(max_se[coef_idx], fit_ols.bse[coef_idx])

    df = n_panels - 3
    params = fit_ols.params
    t_stats = params / max_se
    p_values = 2 * t_dist.sf(np.abs(t_stats), df=df)

    return {
        "params": params,
        "max_se": max_se,
        "t_stats": t_stats,
        "p_values": p_values,
        "ols_se": fit_ols.bse,
    }


def main(B=B_BOOT):
    print("=" * 60)
    print("RF K_eff Non-Independence Correction")
    print(f"  Bootstrap B={B}, EPS={EPS}, N_SIM={N_SIM_TRIALS}")
    print("=" * 60)

    mi_data = load_mi_data()
    pairs = load_pairs()
    clean, _ = load_all_scores()

    clean_acc = compute_clean_accuracy(clean, pairs)
    print(f"\nClean accuracy: {len(clean_acc)} (model, dataset) pairs")
    for ds in DATASETS:
        accs = [clean_acc.get((mid, ds), -1) for mid in ALL_MODELS]
        valid = [a for a in accs if a >= 0]
        print(f"  {ds}: {len(valid)}/15 models, "
              f"acc range=[{min(valid):.3f}, {max(valid):.3f}], "
              f"err range=[{1-max(valid):.3f}, {1-min(valid):.3f}]")

    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))
    rng = np.random.default_rng(SEED)

    results = {}
    condition_keys = []

    for ds in DATASETS:
        keff_data = mi_data["keff_per_panel"].get(ds, {})
        cond = ds
        condition_keys.append(cond)
        print(f"\n{'='*60}")
        print(f"Condition: {cond}")
        print(f"{'='*60}")

        panel_keffs = []
        panel_eta_maxs_rf = []
        panel_eta_all = []
        panel_jids_list = []
        skipped = 0

        for combo in all_combos:
            jids = [ALL_MODELS[i] for i in combo]

            if not all((j, ds) in clean_acc for j in jids):
                skipped += 1
                continue

            pk = "|".join(jids)
            if pk not in keff_data:
                skipped += 1
                continue

            keff = keff_data[pk]["keff"]
            error_rates = [1.0 - clean_acc[(j, ds)] for j in jids]

            panel_keffs.append(keff)
            panel_eta_maxs_rf.append(max(error_rates))
            panel_eta_all.append(error_rates)
            panel_jids_list.append(jids)

        n_panels = len(panel_keffs)
        print(f"  Panels: {n_panels}, skipped: {skipped}")

        if n_panels < 10:
            results[cond] = {"n_panels": n_panels, "skipped": True}
            continue

        keffs = np.array(panel_keffs)
        eta_maxs_rf = np.array(panel_eta_maxs_rf)
        eta_all = np.array(panel_eta_all)

        # --- Simulate RF ASR ---
        print(f"  Simulating RF ASR ({N_SIM_TRIALS} trials)...")
        rf_asr = simulate_rf_asr(eta_all, n_trials=N_SIM_TRIALS, rng=rng)

        analytical = np.array([analytical_rf_asr(e) for e in eta_all])
        max_dev = np.max(np.abs(rf_asr - analytical))
        print(f"  RF ASR: mean={rf_asr.mean():.6f}, std={rf_asr.std():.6f}")
        print(f"  Max deviation from analytical: {max_dev:.6f}")
        print(f"  eta_max_rf: mean={eta_maxs_rf.mean():.4f}, "
              f"range=[{eta_maxs_rf.min():.4f}, {eta_maxs_rf.max():.4f}]")
        print(f"  K_eff: mean={keffs.mean():.4f}, "
              f"range=[{keffs.min():.4f}, {keffs.max():.4f}]")

        # --- OLS ---
        log_y = np.log(rf_asr + EPS)
        log_keff = np.log(keffs)
        log_eta = np.log(eta_maxs_rf + EPS)
        X = np.column_stack([np.ones(n_panels), log_keff, log_eta])

        fit_ols = sm.OLS(log_y, X).fit()
        sd_y = np.std(log_y)
        keff_std_beta = float(fit_ols.params[1] * np.std(log_keff) / sd_y) if sd_y > 0 else 0
        eta_std_beta = float(fit_ols.params[2] * np.std(log_eta) / sd_y) if sd_y > 0 else 0

        print(f"\n  OLS results:")
        print(f"    K_eff:  beta={fit_ols.params[1]:.4f}  std_beta={keff_std_beta:.4f}  "
              f"t={fit_ols.tvalues[1]:.4f}  p={fit_ols.pvalues[1]:.2e}")
        print(f"    eta:    beta={fit_ols.params[2]:.4f}  std_beta={eta_std_beta:.4f}  "
              f"t={fit_ols.tvalues[2]:.4f}  p={fit_ols.pvalues[2]:.2e}")
        print(f"    R2={fit_ols.rsquared:.4f}  adj_R2={fit_ols.rsquared_adj:.4f}")

        # --- Clustered SE (3-position max) ---
        print(f"\n  Clustered SE (3-position max)...")
        cl = clustered_se_3positions(log_y, X, panel_jids_list, n_panels)
        se_inf_keff = cl["max_se"][1] / cl["ols_se"][1] if cl["ols_se"][1] > 0 else None
        se_inf_eta = cl["max_se"][2] / cl["ols_se"][2] if cl["ols_se"][2] > 0 else None

        print(f"    K_eff:  t={cl['t_stats'][1]:.4f}  p={cl['p_values'][1]:.2e}  "
              f"SE_inflation={se_inf_keff:.2f}x")
        print(f"    eta:    t={cl['t_stats'][2]:.4f}  p={cl['p_values'][2]:.2e}  "
              f"SE_inflation={se_inf_eta:.2f}x")

        # --- Wild Cluster Bootstrap v2 (3-position, Rademacher) ---
        print(f"\n  Wild cluster bootstrap v2 (B={B}, 3-position)...")

        keff_pos_ps, keff_final_p, keff_n_clusters = bootstrap_3positions(
            log_y, X, panel_jids_list, B=B, seed=SEED, test_col_idx=1
        )
        print(f"    K_eff:  pos_p={[f'{p:.4f}' for p in keff_pos_ps]}  "
              f"max_p={keff_final_p:.4f}  clusters={keff_n_clusters}")

        eta_pos_ps, eta_final_p, eta_n_clusters = bootstrap_3positions(
            log_y, X, panel_jids_list, B=B, seed=SEED+1, test_col_idx=2
        )
        print(f"    eta:    pos_p={[f'{p:.4f}' for p in eta_pos_ps]}  "
              f"max_p={eta_final_p:.4f}  clusters={eta_n_clusters}")

        results[cond] = {
            "n_panels": n_panels,
            "skipped": False,
            "rf_asr_stats": {
                "mean": float(rf_asr.mean()),
                "std": float(rf_asr.std()),
                "max_analytical_deviation": float(max_dev),
            },
            "eta_max_rf_stats": {
                "mean": float(eta_maxs_rf.mean()),
                "min": float(eta_maxs_rf.min()),
                "max": float(eta_maxs_rf.max()),
            },
            "keff_stats": {
                "mean": float(keffs.mean()),
                "min": float(keffs.min()),
                "max": float(keffs.max()),
            },
            "ols": {
                "keff_beta": float(fit_ols.params[1]),
                "keff_std_beta": keff_std_beta,
                "keff_t": float(fit_ols.tvalues[1]),
                "keff_p": float(fit_ols.pvalues[1]),
                "eta_beta": float(fit_ols.params[2]),
                "eta_std_beta": eta_std_beta,
                "eta_t": float(fit_ols.tvalues[2]),
                "eta_p": float(fit_ols.pvalues[2]),
                "r2": float(fit_ols.rsquared),
                "adj_r2": float(fit_ols.rsquared_adj),
            },
            "clustered_se": {
                "keff_t": float(cl["t_stats"][1]),
                "keff_p": float(cl["p_values"][1]),
                "eta_t": float(cl["t_stats"][2]),
                "eta_p": float(cl["p_values"][2]),
                "se_inflation_keff": float(se_inf_keff) if se_inf_keff else None,
                "se_inflation_eta": float(se_inf_eta) if se_inf_eta else None,
            },
            "bootstrap_v2": {
                "keff_boot_p_positions": [float(p) for p in keff_pos_ps],
                "keff_final_p": float(keff_final_p),
                "keff_n_clusters": keff_n_clusters,
                "eta_boot_p_positions": [float(p) for p in eta_pos_ps],
                "eta_final_p": float(eta_final_p),
                "eta_n_clusters": eta_n_clusters,
            },
        }

    # --- Summary ---
    valid_keys = [k for k in condition_keys
                  if not results.get(k, {}).get("skipped", True)]
    n_valid = len(valid_keys)

    ols_eta_sig = sum(1 for k in valid_keys if results[k]["ols"]["eta_p"] < 0.05)
    ols_keff_sig = sum(1 for k in valid_keys if results[k]["ols"]["keff_p"] < 0.05)
    cl_eta_sig = sum(1 for k in valid_keys if results[k]["clustered_se"]["eta_p"] < 0.05)
    cl_keff_sig = sum(1 for k in valid_keys if results[k]["clustered_se"]["keff_p"] < 0.05)
    boot_eta_sig = sum(1 for k in valid_keys if results[k]["bootstrap_v2"]["eta_final_p"] < 0.05)
    boot_keff_sig = sum(1 for k in valid_keys if results[k]["bootstrap_v2"]["keff_final_p"] < 0.05)

    print(f"\n{'='*60}")
    print("COMPARISON TABLE")
    print(f"{'='*60}")
    print(f"  {'Regime':<12} {'Method':<20} {'eta_max sig':>12} {'K_eff sig':>12}")
    print(f"  {'-'*12} {'-'*20} {'-'*12} {'-'*12}")
    print(f"  {'Adaptive':<12} {'OLS':<20} {'11/12':>12} {'8/12':>12}")
    print(f"  {'Adaptive':<12} {'Bootstrap v2':<20} {'5/12':>12} {'1/12':>12}")
    print(f"  {'Adaptive':<12} {'Clustered SE':<20} {'8/12':>12} {'0/12':>12}")
    print(f"  {'RF':<12} {'OLS':<20} {f'{ols_eta_sig}/{n_valid}':>12} {f'{ols_keff_sig}/{n_valid}':>12}")
    print(f"  {'RF':<12} {'Bootstrap v2':<20} {f'{boot_eta_sig}/{n_valid}':>12} {f'{boot_keff_sig}/{n_valid}':>12}")
    print(f"  {'RF':<12} {'Clustered SE':<20} {f'{cl_eta_sig}/{n_valid}':>12} {f'{cl_keff_sig}/{n_valid}':>12}")

    print(f"\nPer-condition detail:")
    for k in valid_keys:
        r = results[k]
        print(f"  {k}:")
        print(f"    OLS:       K_eff p={r['ols']['keff_p']:.2e}  eta p={r['ols']['eta_p']:.2e}  R2={r['ols']['r2']:.4f}")
        print(f"    Clust SE:  K_eff p={r['clustered_se']['keff_p']:.2e}  eta p={r['clustered_se']['eta_p']:.2e}")
        print(f"    Boot v2:   K_eff p={r['bootstrap_v2']['keff_final_p']:.4f}  eta p={r['bootstrap_v2']['eta_final_p']:.4f}")

    # --- Output JSON ---
    output = {
        "regime": "random_fault",
        "rf_definition": "clean_accuracy_error_rate",
        "simulation": {
            "n_trials": N_SIM_TRIALS,
            "method": "independent_bernoulli",
            "error_rate_source": "1 - clean_accuracy (dataset-level)",
        },
        "n_panels": 455,
        "n_conditions": n_valid,
        "note": "2 conditions (1 per dataset); RF error rate = 1 - clean_accuracy is "
                "dataset-level, no attack-level variation. No FDR (only 2 tests).",
        "bootstrap": {
            "B": B,
            "weights": "rademacher",
            "seed": SEED,
            "positions": 3,
        },
        "per_condition": {k: results[k] for k in valid_keys},
        "summary": {
            "ols": {
                "eta_sig": f"{ols_eta_sig}/{n_valid}",
                "keff_sig": f"{ols_keff_sig}/{n_valid}",
            },
            "clustered_se": {
                "eta_sig": f"{cl_eta_sig}/{n_valid}",
                "keff_sig": f"{cl_keff_sig}/{n_valid}",
            },
            "bootstrap_v2": {
                "eta_sig": f"{boot_eta_sig}/{n_valid}",
                "keff_sig": f"{boot_keff_sig}/{n_valid}",
            },
        },
    }

    out_path = Path("/root/cert_manip_resist_eval/artifacts/results/plan001/"
                    "rf_keff_correction.json")
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

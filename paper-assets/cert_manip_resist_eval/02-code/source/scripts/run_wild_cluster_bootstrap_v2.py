#!/usr/bin/env python3
"""Wild Cluster Bootstrap v2 — fixes K_eff formula + 3-position clustering.

Bug fixes vs v1:
  1. K_eff loaded from precomputed MI-based values (matching canonical OLS),
     not computed via max-MI analytical formula
  2. 3-position clustering (position 0/1/2 in combo tuple), max p-value
     across positions — matches canonical clustered SE approach
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
    """Run wild cluster bootstrap for 3 judge positions, return max p-value."""
    position_ps = []
    position_clusters = []
    for pos in range(3):
        cluster_ids = np.array([jids[pos] for jids in panel_jids_list])
        n_cl = len(np.unique(cluster_ids))
        position_clusters.append(n_cl)
        p_val, t_orig = wild_cluster_bootstrap(
            y, X_full, cluster_ids, B=B, seed=seed, test_col_idx=test_col_idx
        )
        position_ps.append(p_val)
    return position_ps, max(position_ps), position_clusters


def main(B=B_BOOT):
    print("Loading data...")
    clean, attacked = load_all_scores()
    pairs = load_pairs()
    mi_data = load_mi_data()

    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))
    print(f"Total panels: {len(all_combos)}")

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
        keff_data = mi_data["keff_per_panel"].get(ds, {})

        if not ds_clean or not ds_attacked or not ds_pairs:
            print("  SKIP: missing data")
            results[cond_key] = {"skipped": True}
            continue

        individual_asr = {}
        for mid in ALL_MODELS:
            if mid in ds_clean and mid in ds_attacked:
                individual_asr[mid] = compute_individual_asr(
                    ds_clean[mid], ds_attacked[mid], ds_pairs)

        panel_asrs = []
        panel_keffs = []
        panel_etas = []
        panel_jids_list = []

        for combo in all_combos:
            jids = tuple(ALL_MODELS[i] for i in combo)
            if not all(j in ds_clean and j in ds_attacked for j in jids):
                continue
            if not all(j in individual_asr for j in jids):
                continue

            pk = "|".join(jids)
            if pk not in keff_data:
                continue

            keff = keff_data[pk]["keff"]
            eta_max = max(individual_asr[j] for j in jids)

            cs = {j: ds_clean[j] for j in jids}
            ats = {j: ds_attacked[j] for j in jids}
            asr = compute_panel_asr(jids, cs, ats, ds_pairs)

            panel_asrs.append(asr)
            panel_keffs.append(keff)
            panel_etas.append(eta_max)
            panel_jids_list.append(jids)

        n_panels = len(panel_asrs)
        print(f"  Panels: {n_panels}")

        if n_panels < 10:
            print("  SKIP: too few panels")
            results[cond_key] = {"skipped": True, "n_panels": n_panels}
            continue

        y = np.log(np.array(panel_asrs) + EPS)
        log_keff = np.log(np.array(panel_keffs))
        log_eta = np.log(np.array(panel_etas) + EPS)

        X = np.column_stack([np.ones(n_panels), log_keff, log_eta])

        fit_ols = sm.OLS(y, X).fit()

        sd_y = np.std(y)
        keff_std_beta = float(fit_ols.params[1] * np.std(log_keff) / sd_y)
        eta_std_beta = float(fit_ols.params[2] * np.std(log_eta) / sd_y)

        print(f"  OLS: K_eff β={fit_ols.params[1]:.4f} std_β={keff_std_beta:.4f} "
              f"t={fit_ols.tvalues[1]:.3f}")
        print(f"       η_max β={fit_ols.params[2]:.4f} std_β={eta_std_beta:.4f} "
              f"t={fit_ols.tvalues[2]:.3f}")

        # Validation check for arc_challenge×sycophancy
        if cond_key == "arc_challengexsycophancy":
            print(f"  *** VALIDATION: K_eff std_β = {keff_std_beta:.4f} "
                  f"(expected: -0.192) ***")
            if keff_std_beta > 0:
                print("  *** ERROR: K_eff std_β is POSITIVE — K_eff values are wrong! ***")
                print("  *** STOPPING. ***")
                return

        # 3-position bootstrap for K_eff
        keff_pos_ps, keff_final_p, keff_n_clusters = bootstrap_3positions(
            y, X, panel_jids_list, B=B, seed=SEED, test_col_idx=1
        )
        print(f"  K_eff bootstrap: pos_p={[f'{p:.4f}' for p in keff_pos_ps]} "
              f"max_p={keff_final_p:.4f} clusters={keff_n_clusters}")

        # 3-position bootstrap for eta_max
        eta_pos_ps, eta_final_p, eta_n_clusters = bootstrap_3positions(
            y, X, panel_jids_list, B=B, seed=SEED+1, test_col_idx=2
        )
        print(f"  η_max bootstrap: pos_p={[f'{p:.4f}' for p in eta_pos_ps]} "
              f"max_p={eta_final_p:.4f} clusters={eta_n_clusters}")

        results[cond_key] = {
            "n_panels": n_panels,
            "keff_boot_p": [float(p) for p in keff_pos_ps],
            "keff_final_p": float(keff_final_p),
            "keff_ols_std_beta": keff_std_beta,
            "keff_ols_t": float(fit_ols.tvalues[1]),
            "keff_ols_beta": float(fit_ols.params[1]),
            "keff_n_clusters": keff_n_clusters,
            "eta_boot_p": [float(p) for p in eta_pos_ps],
            "eta_final_p": float(eta_final_p),
            "eta_ols_std_beta": eta_std_beta,
            "eta_ols_t": float(fit_ols.tvalues[2]),
            "eta_ols_beta": float(fit_ols.params[2]),
            "eta_n_clusters": eta_n_clusters,
            "skipped": False,
        }

    # FDR correction on final (max) p-values
    valid_keys = [k for k in condition_keys
                  if not results.get(k, {}).get("skipped", True)]

    keff_final_ps = [results[k]["keff_final_p"] for k in valid_keys]
    eta_final_ps = [results[k]["eta_final_p"] for k in valid_keys]

    if len(valid_keys) > 0:
        _, keff_fdr_p, _, _ = multipletests(keff_final_ps, alpha=FDR_ALPHA,
                                            method="fdr_bh")
        _, eta_fdr_p, _, _ = multipletests(eta_final_ps, alpha=FDR_ALPHA,
                                           method="fdr_bh")
        for i, k in enumerate(valid_keys):
            results[k]["keff_fdr_p"] = float(keff_fdr_p[i])
            results[k]["eta_fdr_p"] = float(eta_fdr_p[i])

    keff_fdr_sig = sum(1 for k in valid_keys
                       if results[k]["keff_fdr_p"] < FDR_ALPHA)
    eta_fdr_sig = sum(1 for k in valid_keys
                      if results[k]["eta_fdr_p"] < FDR_ALPHA)
    keff_sig_pos = sum(1 for k in valid_keys
                       if results[k]["keff_fdr_p"] < FDR_ALPHA
                       and results[k]["keff_ols_beta"] > 0)
    keff_sig_neg = keff_fdr_sig - keff_sig_pos

    print(f"\n{'='*60}")
    print(f"SUMMARY (B={B})")
    print(f"{'='*60}")
    print(f"  K_eff FDR sig: {keff_fdr_sig}/12 ({keff_sig_pos}+ / {keff_sig_neg}-)")
    print(f"  η_max FDR sig: {eta_fdr_sig}/12")

    print(f"\nPer-condition details:")
    print(f"  {'Condition':<35} {'K std_β':>8} {'K max_p':>8} {'K fdr_p':>8} {'sig':>4} "
          f"{'η max_p':>8} {'η fdr_p':>8} {'sig':>4}")
    for k in valid_keys:
        r = results[k]
        ks = "*" if r["keff_fdr_p"] < FDR_ALPHA else ""
        es = "*" if r["eta_fdr_p"] < FDR_ALPHA else ""
        print(f"  {k:<35} {r['keff_ols_std_beta']:>8.4f} {r['keff_final_p']:>8.4f} "
              f"{r['keff_fdr_p']:>8.4f} {ks:>4} "
              f"{r['eta_final_p']:>8.4f} {r['eta_fdr_p']:>8.4f} {es:>4}")

    # Build validation block
    arc_syc = results.get("arc_challengexsycophancy", {})
    validation = {
        "arc_sycophancy_keff_std_beta": arc_syc.get("keff_ols_std_beta"),
        "arc_sycophancy_keff_std_beta_expected": -0.192,
    }

    output = {
        "method": "wild_cluster_bootstrap_v2",
        "fixes": ["keff_formula_aligned_with_canonical",
                   "3_position_clustering_max_p"],
        "B": B,
        "weights": "rademacher",
        "n_clusters_per_position": "13 (from C(15,3) combo structure)",
        "seed": SEED,
        "per_condition": {k: results[k] for k in valid_keys},
        "summary": {
            "keff_fdr_sig": f"{keff_fdr_sig}/12",
            "keff_sig_positive": keff_sig_pos,
            "keff_sig_negative": keff_sig_neg,
            "eta_fdr_sig": f"{eta_fdr_sig}/12",
        },
        "validation": validation,
    }

    out_path = Path("/root/cert_manip_resist_eval/artifacts/results/plan001/"
                    "wild_cluster_bootstrap_v2.json")
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

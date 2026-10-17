#!/usr/bin/env python3
"""K=5 Aggregation Wild Cluster Bootstrap — 4 methods × 12 conditions.

For each aggregation method (majority, weighted, threshold, bayesian):
  - C(15,5)=3003 panels, panel ASR per method
  - Canonical regression: log(ASR+eps) ~ log(K_eff) + log(eta_max+eps)
  - Wild cluster bootstrap: B=9999, Rademacher weights
  - 5-position max-p (cluster by each judge position, take max p)
  - BH FDR α=0.05 across 12 conditions per method
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import time
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


def compute_clean_accuracy(clean, pairs):
    acc = {}
    for ds in DATASETS:
        for mid in ALL_MODELS:
            if mid not in clean.get(ds, {}):
                continue
            scores = clean[ds][mid]
            p = pairs.get(ds, [])
            n = min(len(scores), len(p))
            correct = total = 0
            for i in range(n):
                if not _is_valid_score(scores[i]):
                    continue
                total += 1
                if scores[i]["winner"] == p[i]["ground_truth_winner"]:
                    correct += 1
            acc[(mid, ds)] = correct / max(total, 1)
    return acc
FDR_ALPHA = 0.05
B_BOOT = 9999
SEED = 42
K = 5
THRESHOLD_MIN = 4
METHODS = ["majority_vote", "weighted_vote", "threshold_supermajority", "bayesian"]


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


def compute_panel_asr_all_methods(jids, clean, attacked, pairs, accs):
    n = min(len(pairs), *(len(clean[j]) for j in jids),
            *(len(attacked[j]) for j in jids))

    mv_flips = mv_correct = 0
    wv_flips = wv_correct = 0
    th_flips = th_denom = 0
    by_flips = by_correct = 0

    for i in range(n):
        if not all(_is_valid_score(clean[j][i]) for j in jids):
            continue
        if not all(_is_valid_score(attacked[j][i]) for j in jids):
            continue
        gt = pairs[i]["ground_truth_winner"]
        c_votes = [clean[j][i]["winner"] for j in jids]
        a_votes = [attacked[j][i]["winner"] for j in jids]

        # Majority Vote (>=3/5)
        cv = majority_vote(c_votes)
        if cv == gt:
            mv_correct += 1
            if majority_vote(a_votes) != gt:
                mv_flips += 1

        # Weighted Vote
        w_a_c = sum(a for v, a in zip(c_votes, accs) if v == "A")
        w_b_c = sum(a for v, a in zip(c_votes, accs) if v == "B")
        cv_w = "A" if w_a_c > w_b_c else ("B" if w_b_c > w_a_c else "tie")
        if cv_w == gt:
            wv_correct += 1
            w_a_a = sum(a for v, a in zip(a_votes, accs) if v == "A")
            w_b_a = sum(a for v, a in zip(a_votes, accs) if v == "B")
            av_w = "A" if w_a_a > w_b_a else ("B" if w_b_a > w_a_a else "tie")
            if av_w != gt:
                wv_flips += 1

        # Threshold (>=4/5 supermajority)
        gt_count_c = sum(1 for v in c_votes if v == gt)
        if gt_count_c >= THRESHOLD_MIN:
            th_denom += 1
            gt_count_a = sum(1 for v in a_votes if v == gt)
            if gt_count_a < THRESHOLD_MIN:
                th_flips += 1

        # Bayesian
        log_odds_c = 0.0
        for v, ac in zip(c_votes, accs):
            a = max(min(ac, 0.999), 0.001)
            if v == gt:
                log_odds_c += np.log(a / (1 - a))
            else:
                log_odds_c += np.log((1 - a) / a)
        if log_odds_c > 0:
            by_correct += 1
            log_odds_a = 0.0
            for v, ac in zip(a_votes, accs):
                a = max(min(ac, 0.999), 0.001)
                if v == gt:
                    log_odds_a += np.log(a / (1 - a))
                else:
                    log_odds_a += np.log((1 - a) / a)
            if log_odds_a <= 0:
                by_flips += 1

    return {
        "majority_vote": (mv_flips / max(mv_correct, 1), mv_correct),
        "weighted_vote": (wv_flips / max(wv_correct, 1), wv_correct),
        "threshold_supermajority": (th_flips / max(th_denom, 1), th_denom),
        "bayesian": (by_flips / max(by_correct, 1), by_correct),
    }


def wild_cluster_bootstrap_vec(y, X_full, cluster_ids, B=B_BOOT, seed=SEED,
                                test_col_idx=1):
    n, p = X_full.shape
    unique_clusters = np.unique(cluster_ids)
    n_clusters = len(unique_clusters)

    cluster_to_idx = {c: i for i, c in enumerate(unique_clusters)}
    panel_cluster_idx = np.array([cluster_to_idx[c] for c in cluster_ids])

    fit_full = sm.OLS(y, X_full).fit()
    t_original = fit_full.tvalues[test_col_idx]
    beta_original = fit_full.params[test_col_idx]
    se_original = fit_full.bse[test_col_idx]

    cols_restricted = [i for i in range(p) if i != test_col_idx]
    X_restricted = X_full[:, cols_restricted]
    fit_restricted = sm.OLS(y, X_restricted).fit()
    y_hat_r = fit_restricted.fittedvalues
    e_r = y - y_hat_r

    XtX_inv = np.linalg.inv(X_full.T @ X_full)
    M = XtX_inv @ X_full.T
    q_jj = XtX_inv[test_col_idx, test_col_idx]

    rng = np.random.RandomState(seed)
    w_clusters = rng.choice([-1, 1], size=(B, n_clusters)).astype(np.float64)
    w_panels = w_clusters[:, panel_cluster_idx]

    y_boots = y_hat_r[np.newaxis, :] + w_panels * e_r[np.newaxis, :]
    beta_boots = y_boots @ M.T

    predicted = beta_boots @ X_full.T
    sigma2 = np.sum((y_boots - predicted) ** 2, axis=1) / (n - p)
    del predicted, w_panels

    t_boot = beta_boots[:, test_col_idx] / np.sqrt(sigma2 * q_jj)

    p_value = (1 + np.sum(np.abs(t_boot) >= np.abs(t_original))) / (1 + B)

    t_lo = np.percentile(t_boot, 2.5)
    t_hi = np.percentile(t_boot, 97.5)
    ci_lo = float(beta_original - t_hi * se_original)
    ci_hi = float(beta_original - t_lo * se_original)

    return float(p_value), float(t_original), ci_lo, ci_hi


def bootstrap_kpositions(y, X_full, panel_jids_list, n_positions, B=B_BOOT,
                          seed=SEED, test_col_idx=1):
    position_ps = []
    position_clusters = []
    position_cis = []
    for pos in range(n_positions):
        cluster_ids = np.array([jids[pos] for jids in panel_jids_list])
        n_cl = len(np.unique(cluster_ids))
        position_clusters.append(n_cl)
        p_val, t_orig, ci_lo, ci_hi = wild_cluster_bootstrap_vec(
            y, X_full, cluster_ids, B=B, seed=seed, test_col_idx=test_col_idx
        )
        position_ps.append(p_val)
        position_cis.append((ci_lo, ci_hi))

    max_p = max(position_ps)
    max_p_idx = position_ps.index(max_p)
    ci_95 = list(position_cis[max_p_idx])

    return position_ps, max_p, position_clusters, ci_95


# OLS reference from K=5 aggregation analysis
OLS_REF = {
    "majority_vote":              {"eta": "10/12", "keff": "12/12", "keff_pos": 11, "keff_neg": 1},
    "weighted_vote":              {"eta": "9/12",  "keff": "11/12", "keff_pos": 11, "keff_neg": 0},
    "threshold_supermajority":    {"eta": "12/12", "keff": "11/12", "keff_pos": 11, "keff_neg": 0},
    "bayesian":                   {"eta": "8/12",  "keff": "10/12", "keff_pos": 10, "keff_neg": 0},
}


def main(B=B_BOOT):
    t_total = time.time()
    print(f"K=5 Aggregation Wild Cluster Bootstrap (B={B}, 4 methods)")
    print("=" * 70)

    mi_data = load_mi_data()
    pairs = load_pairs()
    clean, attacked = load_all_scores()
    clean_acc = compute_clean_accuracy(clean, pairs)

    mi_matrices_np = {}
    for ds in DATASETS:
        mi_matrices_np[ds] = np.array(mi_data["mi_matrix"][ds])

    ind_asr = {}
    for ds in DATASETS:
        for atk in ATTACKS:
            for mid in ALL_MODELS:
                if mid in clean[ds] and mid in attacked[ds][atk]:
                    ind_asr[(ds, atk, mid)] = compute_individual_asr(
                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]
                    )

    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), K))
    print(f"Panels: C(15,5) = {len(all_combos)}")

    # Precompute keff
    keff_cache = {}
    for ds in DATASETS:
        mi_mat = mi_matrices_np[ds]
        ds_keff = {}
        for combo in all_combos:
            jids = tuple(ALL_MODELS[i] for i in combo)
            pk = "|".join(jids)
            ds_keff[pk] = mi_based_keff(mi_mat, list(combo))
        keff_cache[ds] = ds_keff

    condition_keys = [f"{ds}x{atk}" for ds in DATASETS for atk in ATTACKS]

    # Per-method results
    method_results = {}
    for m in METHODS:
        method_results[m] = {
            "raw_keff_ps": [], "raw_eta_ps": [],
            "valid_keys": [], "conditions": {}
        }

    # Main loop: compute panel ASR for all methods at once
    for ds in DATASETS:
        for atk in ATTACKS:
            cond = f"{ds}x{atk}"
            t0 = time.time()
            print(f"\n--- {cond} ---")

            method_panels = {m: {"asrs": [], "keffs": [], "etas": [], "jids": []}
                             for m in METHODS}
            skipped = 0

            for combo in all_combos:
                jids = [ALL_MODELS[i] for i in combo]
                if not all((ds, atk, j) in ind_asr for j in jids):
                    skipped += 1
                    continue

                pk = "|".join(jids)
                keff = keff_cache[ds][pk]
                eta_max = max(ind_asr[(ds, atk, j)] for j in jids)

                cs = {j: clean[ds][j] for j in jids}
                ats = {j: attacked[ds][atk][j] for j in jids}
                panel_accs = [clean_acc.get((j, ds), 0.5) for j in jids]

                results = compute_panel_asr_all_methods(
                    jids, cs, ats, pairs[ds], panel_accs
                )

                for m in METHODS:
                    asr, denom = results[m]
                    if m == "threshold_supermajority" and denom == 0:
                        continue
                    method_panels[m]["asrs"].append(asr)
                    method_panels[m]["keffs"].append(keff)
                    method_panels[m]["etas"].append(eta_max)
                    method_panels[m]["jids"].append(jids)

            # Run bootstrap for each method
            for m in METHODS:
                mp = method_panels[m]
                n_panels = len(mp["asrs"])
                if n_panels < 10:
                    print(f"  {m}: {n_panels} panels, skipping")
                    continue

                p_asrs = np.array(mp["asrs"])
                p_keffs = np.array(mp["keffs"])
                p_etas = np.array(mp["etas"])

                if np.std(p_asrs) < 1e-10:
                    print(f"  {m}: constant ASR ({p_asrs[0]:.4f}), skipping")
                    continue

                y = np.log(p_asrs + EPS)
                log_keff = np.log(p_keffs)
                log_eta = np.log(p_etas + EPS)

                X = np.column_stack([log_keff, log_eta])
                Xc = sm.add_constant(X)

                fit = sm.OLS(y, Xc).fit()
                sd_y = np.std(y)
                keff_std_beta = float(fit.params[1] * np.std(log_keff) / sd_y)
                eta_std_beta = float(fit.params[2] * np.std(log_eta) / sd_y)

                # 5-position max-p for K_eff (col 1)
                keff_pos_ps, keff_max_p, keff_n_cl, keff_ci = bootstrap_kpositions(
                    y, Xc, mp["jids"], K, B=B, seed=SEED, test_col_idx=1
                )
                # 5-position max-p for eta_max (col 2)
                eta_pos_ps, eta_max_p, eta_n_cl, eta_ci = bootstrap_kpositions(
                    y, Xc, mp["jids"], K, B=B, seed=SEED, test_col_idx=2
                )

                cd = {
                    "condition": cond,
                    "method": m,
                    "dataset": ds,
                    "attack": atk,
                    "n_panels": n_panels,
                    "keff_ols_beta": float(fit.params[1]),
                    "keff_ols_std_beta": keff_std_beta,
                    "keff_ols_p": float(fit.pvalues[1]),
                    "keff_position_ps": keff_pos_ps,
                    "keff_final_p": keff_max_p,
                    "keff_n_clusters": keff_n_cl,
                    "keff_ci_95": keff_ci,
                    "eta_ols_beta": float(fit.params[2]),
                    "eta_ols_std_beta": eta_std_beta,
                    "eta_ols_p": float(fit.pvalues[2]),
                    "eta_position_ps": eta_pos_ps,
                    "eta_final_p": eta_max_p,
                    "eta_n_clusters": eta_n_cl,
                    "eta_ci_95": eta_ci,
                    "R2": float(fit.rsquared),
                }

                method_results[m]["conditions"][cond] = cd
                method_results[m]["raw_keff_ps"].append(keff_max_p)
                method_results[m]["raw_eta_ps"].append(eta_max_p)
                method_results[m]["valid_keys"].append(cond)

                print(f"  {m}: K_std_b={keff_std_beta:+.4f} maxp={keff_max_p:.4f}"
                      f"  e_std_b={eta_std_beta:+.4f} maxp={eta_max_p:.4f}"
                      f"  R2={fit.rsquared:.4f}  ({n_panels} panels)")

            dt = time.time() - t0
            print(f"  condition time: {dt:.0f}s")

    # FDR per method
    summary = {}
    for m in METHODS:
        mr = method_results[m]
        vk = mr["valid_keys"]
        if not vk:
            summary[m] = {"eta_fdr_sig": "0/0", "keff_fdr_sig": "0/0",
                          "keff_sig_positive": 0, "keff_sig_negative": 0}
            continue

        _, keff_fdr_p, _, _ = multipletests(mr["raw_keff_ps"], alpha=FDR_ALPHA,
                                            method="fdr_bh")
        _, eta_fdr_p, _, _ = multipletests(mr["raw_eta_ps"], alpha=FDR_ALPHA,
                                           method="fdr_bh")
        for i, ck in enumerate(vk):
            mr["conditions"][ck]["keff_fdr_p"] = float(keff_fdr_p[i])
            mr["conditions"][ck]["eta_fdr_p"] = float(eta_fdr_p[i])

        nt = len(vk)
        n_keff = sum(1 for ck in vk if mr["conditions"][ck]["keff_fdr_p"] < FDR_ALPHA)
        n_eta = sum(1 for ck in vk if mr["conditions"][ck]["eta_fdr_p"] < FDR_ALPHA)
        n_pos = sum(1 for ck in vk
                    if mr["conditions"][ck]["keff_fdr_p"] < FDR_ALPHA
                    and mr["conditions"][ck]["keff_ols_std_beta"] > 0)
        n_neg = n_keff - n_pos

        summary[m] = {
            "eta_fdr_sig": f"{n_eta}/{nt}",
            "keff_fdr_sig": f"{n_keff}/{nt}",
            "keff_sig_positive": n_pos,
            "keff_sig_negative": n_neg,
            "n_conditions": nt,
        }

    # Print summary
    print(f"\n{'='*70}")
    print(f"K=5 AGGREGATION BOOTSTRAP SUMMARY (B={B})")
    print(f"{'='*70}")
    print(f"  {'Method':<28} {'eta_FDR':>10} {'K_FDR':>10} {'K_pos':>6} {'K_neg':>6}")
    for m in METHODS:
        s = summary[m]
        print(f"  {m:<28} {s['eta_fdr_sig']:>10} {s['keff_fdr_sig']:>10}"
              f" {s['keff_sig_positive']:>6} {s['keff_sig_negative']:>6}")

    # OLS vs bootstrap comparison
    ols_vs_boot = {}
    for m in METHODS:
        ols_vs_boot[m] = {
            "ols_eta": OLS_REF[m]["eta"],
            "boot_eta": summary[m]["eta_fdr_sig"],
            "ols_keff": OLS_REF[m]["keff"],
            "boot_keff": summary[m]["keff_fdr_sig"],
            "ols_keff_pos": OLS_REF[m]["keff_pos"],
            "ols_keff_neg": OLS_REF[m]["keff_neg"],
            "boot_keff_pos": summary[m]["keff_sig_positive"],
            "boot_keff_neg": summary[m]["keff_sig_negative"],
        }

    print(f"\n  OLS vs Bootstrap:")
    for m in METHODS:
        o = ols_vs_boot[m]
        print(f"    {m:<28} OLS K={o['ols_keff']} -> Boot K={o['boot_keff']}"
              f"  ({o['boot_keff_pos']}+/{o['boot_keff_neg']}-)")

    # Bayesian reversal check
    bay_neg = summary["bayesian"]["keff_sig_negative"]
    bay_pos = summary["bayesian"]["keff_sig_positive"]
    bayesian_reversal = bay_neg > 0

    print(f"\n  Bayesian K_eff reversal under bootstrap: "
          f"{'YES' if bayesian_reversal else 'NO'} "
          f"({bay_pos}+/{bay_neg}-)")

    # Validation: arc×sycophancy
    arc_syc = method_results["majority_vote"]["conditions"].get("arc_challengexsycophancy", {})
    validation = {
        "arc_sycophancy_majority_keff_std_beta": arc_syc.get("keff_ols_std_beta"),
        "arc_sycophancy_majority_keff_negative": (
            arc_syc.get("keff_ols_beta", 0) < 0
            if not arc_syc.get("skipped") else None
        ),
    }

    # Detail table
    print(f"\n{'='*120}")
    print(f"  {'Condition':<25} {'Method':<28} {'K_std_b':>8} {'K_maxp':>8} "
          f"{'K_fdr':>8} {'sig':>4}  {'e_std_b':>8} {'e_maxp':>8} {'e_fdr':>8} {'sig':>4}")
    for m in METHODS:
        mr = method_results[m]
        for ck in mr["valid_keys"]:
            r = mr["conditions"][ck]
            ks = "*" if r.get("keff_fdr_p", 1) < FDR_ALPHA else ""
            es = "*" if r.get("eta_fdr_p", 1) < FDR_ALPHA else ""
            print(f"  {ck:<25} {m:<28} {r['keff_ols_std_beta']:>+8.4f} "
                  f"{r['keff_final_p']:>8.4f} {r.get('keff_fdr_p',1):>8.4f} {ks:>4}  "
                  f"{r['eta_ols_std_beta']:>+8.4f} "
                  f"{r['eta_final_p']:>8.4f} {r.get('eta_fdr_p',1):>8.4f} {es:>4}")

    elapsed = time.time() - t_total
    print(f"\nTotal time: {elapsed:.0f}s")

    # Build output
    per_method_output = {}
    for m in METHODS:
        mr = method_results[m]
        per_method_output[m] = {
            "eta_fdr_sig": summary[m]["eta_fdr_sig"],
            "keff_fdr_sig": summary[m]["keff_fdr_sig"],
            "keff_sig_positive": summary[m]["keff_sig_positive"],
            "keff_sig_negative": summary[m]["keff_sig_negative"],
            "per_condition": {ck: mr["conditions"][ck] for ck in mr["valid_keys"]},
        }

    output = {
        "panel_size": K,
        "n_bootstrap": B,
        "weights": "rademacher",
        "n_positions": K,
        "seed": SEED,
        "n_total_panels": len(all_combos),
        "keff_formula": "mi_based_keff (average pairwise MI)",
        "regression": "log(ASR+1e-6) ~ log(K_eff) + log(eta_max+1e-6)",
        "fdr_alpha": FDR_ALPHA,
        "aggregation_methods": per_method_output,
        "ols_vs_bootstrap_comparison": ols_vs_boot,
        "bayesian_keff_reversal_under_bootstrap": bayesian_reversal,
        "validation": validation,
        "elapsed_seconds": elapsed,
    }

    out_path = Path("/root/cert_manip_resist_eval/artifacts/results/plan001/"
                    "k5_aggregation_bootstrap.json")
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

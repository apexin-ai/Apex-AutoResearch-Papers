#!/usr/bin/env python3
"""κ-diversity regime transition: wild cluster bootstrap for K=3/5/7.

Replaces K_eff with κ-diversity (1 - mean pairwise Cohen's kappa) in the
log-log panel regression, using K-position wild cluster bootstrap with
Rademacher weights, max-p across positions, and BH FDR correction.
"""

import sys
import json
import time
import itertools
import numpy as np
from pathlib import Path
from statsmodels.stats.multitest import multipletests

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)

BACKUP_DIR = PROJECT_ROOT / "artifacts" / "server_backup" / "results"
LOCAL_CKPTS = [
    BACKUP_DIR / "_taxonomy_checkpoint.json",
    BACKUP_DIR / "_step2v3_checkpoint.json",
]
LOCAL_SCORES_DIR = BACKUP_DIR / "plan001" / "individual_scores"
LOCAL_MI_PATH = BACKUP_DIR / "plan001" / "mi_matrix" / "mi_matrix_15models.json"

EPS = 1e-6
FDR_ALPHA = 0.05
B_BOOT = 9999
SEED = 42
N_MODELS = len(ALL_MODELS)


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


def compute_panel_asr(jids, clean_ds, attacked_ds_atk, pairs):
    n = min(len(pairs), *(len(clean_ds[j]) for j in jids),
            *(len(attacked_ds_atk[j]) for j in jids))
    n_flips = n_correct = 0
    for i in range(n):
        if not all(_is_valid_score(clean_ds[j][i]) for j in jids):
            continue
        if not all(_is_valid_score(attacked_ds_atk[j][i]) for j in jids):
            continue
        gt = pairs[i]["ground_truth_winner"]
        cv = majority_vote([clean_ds[j][i]["winner"] for j in jids])
        if cv != gt:
            continue
        n_correct += 1
        av = majority_vote([attacked_ds_atk[j][i]["winner"] for j in jids])
        if av != gt:
            n_flips += 1
    return n_flips / max(n_correct, 1)


def pairwise_kappa(clean_i, clean_j):
    n = min(len(clean_i), len(clean_j))
    categories = ["A", "B", "tie"]
    n_valid = n_agree = 0
    cnt_i = {c: 0 for c in categories}
    cnt_j = {c: 0 for c in categories}
    for idx in range(n):
        if not _is_valid_score(clean_i[idx]) or not _is_valid_score(clean_j[idx]):
            continue
        n_valid += 1
        vi = clean_i[idx]["winner"]
        vj = clean_j[idx]["winner"]
        cnt_i[vi] += 1
        cnt_j[vj] += 1
        if vi == vj:
            n_agree += 1
    if n_valid == 0:
        return 0.0
    p_o = n_agree / n_valid
    p_e = sum(cnt_i[c] * cnt_j[c] for c in categories) / (n_valid * n_valid)
    if p_e >= 1.0:
        return 0.0
    return (p_o - p_e) / (1 - p_e)


def panel_kappa_diversity(jids, clean_ds):
    kappas = []
    for a in range(len(jids)):
        for b in range(a + 1, len(jids)):
            kappas.append(pairwise_kappa(clean_ds[jids[a]], clean_ds[jids[b]]))
    return 1 - np.mean(kappas)


def wild_cluster_bootstrap_vec(y, X, cluster_ids, B=B_BOOT, seed=SEED,
                               test_col_idx=1):
    """Vectorized wild cluster bootstrap. Returns (p_value, t_original, n_clusters)."""
    n, p = X.shape
    uq = np.unique(cluster_ids)
    G = len(uq)
    c2i = {c: i for i, c in enumerate(uq)}
    cidx = np.array([c2i[c] for c in cluster_ids])

    XtX = X.T @ X
    Li = np.linalg.inv(XtX)
    b_full = Li @ (X.T @ y)
    e_full = y - X @ b_full
    s2 = np.sum(e_full ** 2) / (n - p)
    t_orig = b_full[test_col_idx] / np.sqrt(s2 * Li[test_col_idx, test_col_idx])

    cr = [i for i in range(p) if i != test_col_idx]
    Xr = X[:, cr]
    br = np.linalg.solve(Xr.T @ Xr, Xr.T @ y)
    yhr = Xr @ br
    er = y - yhr

    Xe = X.T * er[None, :]
    Xtyhr = X.T @ yhr
    yhr_sq = float(np.sum(yhr ** 2))
    er_sq = float(np.sum(er ** 2))
    yhe = yhr * er

    rng = np.random.RandomState(seed)
    Wc = 2.0 * rng.randint(0, 2, size=(B, G)).astype(np.float64) - 1.0
    W = Wc[:, cidx]

    XtWe = Xe @ W.T
    XtY = Xtyhr[:, None] + XtWe
    Beta = Li @ XtY

    YtY = yhr_sq + er_sq + 2.0 * (W @ yhe)
    BXY = np.sum(Beta * XtY, axis=0)
    RSS = YtY - BXY
    S2 = RSS / (n - p)

    SE = np.sqrt(np.maximum(S2, 0) * Li[test_col_idx, test_col_idx])
    T = Beta[test_col_idx, :] / np.maximum(SE, 1e-30)

    pv = (1 + np.sum(np.abs(T) >= np.abs(t_orig))) / (1 + B)
    return float(pv), float(t_orig), int(G)


def bootstrap_K_positions(y, X, panel_jids_list, K, B=B_BOOT, seed=SEED,
                          test_col_idx=1):
    pos_ps = []
    pos_clusters = []
    for pos in range(K):
        cids = np.array([jids[pos] for jids in panel_jids_list])
        pv, _, G = wild_cluster_bootstrap_vec(
            y, X, cids, B=B, seed=seed, test_col_idx=test_col_idx)
        pos_ps.append(pv)
        pos_clusters.append(G)
    return pos_ps, max(pos_ps), pos_clusters


def run_for_K(K, clean, attacked, pairs, mi_data):
    print(f"\n{'=' * 60}")
    print(f"K = {K}")
    print(f"{'=' * 60}")

    models = ALL_MODELS
    all_combos = list(itertools.combinations(range(N_MODELS), K))
    n_combos = len(all_combos)
    print(f"Total panels: {n_combos}")

    ind_asr = {}
    for ds in DATASETS:
        for atk in ATTACKS:
            for mid in models:
                if mid in clean[ds] and mid in attacked[ds][atk]:
                    ind_asr[(ds, atk, mid)] = compute_individual_asr(
                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds])

    print("Computing κ-diversity...")
    t0 = time.time()
    kd_cache = {}
    total = 0
    for ds in DATASETS:
        for combo in all_combos:
            jids = tuple(models[i] for i in combo)
            if all(j in clean[ds] for j in jids):
                kd_cache[(jids, ds)] = panel_kappa_diversity(jids, clean[ds])
            total += 1
            if total % 2000 == 0:
                print(f"  {total}/{n_combos * len(DATASETS)}...")
    print(f"  Done: {len(kd_cache)} values in {time.time() - t0:.1f}s")

    corr_keff = None
    if K == 3 and mi_data:
        from scipy.stats import pearsonr, spearmanr
        ks, kds = [], []
        for ds in DATASETS:
            keff_d = mi_data["keff_per_panel"].get(ds, {})
            for combo in all_combos:
                jids = tuple(models[i] for i in combo)
                pk = "|".join(jids)
                if pk in keff_d and (jids, ds) in kd_cache:
                    ks.append(keff_d[pk]["keff"])
                    kds.append(kd_cache[(jids, ds)])
        if len(ks) > 10:
            rp, _ = pearsonr(ks, kds)
            rs, _ = spearmanr(ks, kds)
            corr_keff = {"pearson": round(float(rp), 4), "spearman": round(float(rs), 4)}
            print(f"  Correlation with K_eff: r={rp:.4f}, ρ={rs:.4f}")

    cond_keys = [f"{ds}x{atk}" for ds in DATASETS for atk in ATTACKS]
    results = {}

    for ci, ck in enumerate(cond_keys):
        ds, atk = ck.split("x", 1)
        t0 = time.time()
        print(f"\n  [{ci + 1}/12] {ck}")

        ds_c = clean.get(ds, {})
        ds_a = attacked.get(ds, {}).get(atk, {})
        ds_p = pairs.get(ds, [])

        if not ds_c or not ds_a or not ds_p:
            results[ck] = {"skipped": True}
            continue

        asrs, kds_arr, etas, jids_list = [], [], [], []

        for combo in all_combos:
            jids = tuple(models[i] for i in combo)
            if not all(j in ds_c and j in ds_a for j in jids):
                continue
            if not all((ds, atk, j) in ind_asr for j in jids):
                continue
            if (jids, ds) not in kd_cache:
                continue

            asr = compute_panel_asr(jids, ds_c, ds_a, ds_p)
            asrs.append(asr)
            kds_arr.append(kd_cache[(jids, ds)])
            etas.append(max(ind_asr[(ds, atk, j)] for j in jids))
            jids_list.append(jids)

        n_p = len(asrs)
        print(f"    Panels: {n_p}")

        if n_p < 10:
            results[ck] = {"skipped": True, "n_panels": n_p}
            continue

        y = np.log(np.array(asrs) + EPS)
        lkd = np.log(np.array(kds_arr) + EPS)
        le = np.log(np.array(etas) + EPS)
        X = np.column_stack([np.ones(n_p), lkd, le])

        Li = np.linalg.inv(X.T @ X)
        beta = Li @ (X.T @ y)
        e = y - X @ beta
        s2 = np.sum(e ** 2) / (n_p - 3)
        se = np.sqrt(s2 * np.diag(Li))
        t_vals = beta / se
        sd_y = np.std(y)
        sb_kd = float(beta[1] * np.std(lkd) / sd_y)
        sb_eta = float(beta[2] * np.std(le) / sd_y)

        print(f"    OLS: κ_div β={beta[1]:.4f} std_β={sb_kd:.4f} t={t_vals[1]:.3f}")
        print(f"         η_max β={beta[2]:.4f} std_β={sb_eta:.4f} t={t_vals[2]:.3f}")

        kd_ps, kd_max_p, kd_cls = bootstrap_K_positions(
            y, X, jids_list, K, B=B_BOOT, seed=SEED, test_col_idx=1)

        eta_ps, eta_max_p, eta_cls = bootstrap_K_positions(
            y, X, jids_list, K, B=B_BOOT, seed=SEED + 1, test_col_idx=2)

        elapsed = time.time() - t0
        print(f"    κ_div max_p={kd_max_p:.4f}, η_max max_p={eta_max_p:.4f} ({elapsed:.1f}s)")

        results[ck] = {
            "n_panels": n_p,
            "kd_boot_p": [float(p) for p in kd_ps],
            "kd_final_p": float(kd_max_p),
            "kd_ols_std_beta": sb_kd,
            "kd_ols_t": float(t_vals[1]),
            "kd_ols_beta": float(beta[1]),
            "kd_n_clusters": kd_cls,
            "eta_boot_p": [float(p) for p in eta_ps],
            "eta_final_p": float(eta_max_p),
            "eta_ols_std_beta": sb_eta,
            "eta_ols_t": float(t_vals[2]),
            "eta_ols_beta": float(beta[2]),
            "eta_n_clusters": eta_cls,
            "skipped": False,
        }

    vk = [k for k in cond_keys if not results.get(k, {}).get("skipped", True)]
    if vk:
        kd_fps = [results[k]["kd_final_p"] for k in vk]
        eta_fps = [results[k]["eta_final_p"] for k in vk]
        _, kd_fdr, _, _ = multipletests(kd_fps, alpha=FDR_ALPHA, method="fdr_bh")
        _, eta_fdr, _, _ = multipletests(eta_fps, alpha=FDR_ALPHA, method="fdr_bh")
        for i, k in enumerate(vk):
            results[k]["kd_fdr_p"] = float(kd_fdr[i])
            results[k]["eta_fdr_p"] = float(eta_fdr[i])

    kd_sig = sum(1 for k in vk if results[k]["kd_fdr_p"] < FDR_ALPHA)
    eta_sig = sum(1 for k in vk if results[k]["eta_fdr_p"] < FDR_ALPHA)

    print(f"\n  SUMMARY K={K}: κ_div {kd_sig}/12, η_max {eta_sig}/12")

    return {
        "K": K, "n_panels": n_combos,
        "per_condition": {k: results[k] for k in vk},
        "kd_fdr_sig": f"{kd_sig}/12",
        "eta_fdr_sig": f"{eta_sig}/12",
        "corr_with_keff": corr_keff,
    }


def main():
    t_start = time.time()
    print("Loading data from local backup...")
    clean, attacked = load_all_scores(
        checkpoint_files=LOCAL_CKPTS, individual_dir=LOCAL_SCORES_DIR)
    pairs = load_pairs(checkpoint_files=LOCAL_CKPTS)
    try:
        mi_data = load_mi_data(mi_path=LOCAL_MI_PATH)
    except FileNotFoundError:
        mi_data = None

    all_res = {}
    for K in [3, 5, 7]:
        all_res[f"K{K}"] = run_for_K(K, clean, attacked, pairs, mi_data)

    output = {
        "metric": "kappa_diversity",
        "definition": "1 - mean(pairwise Cohen's kappa on clean winner labels)",
        "method": "wild_cluster_bootstrap",
        "B": B_BOOT,
        "weights": "rademacher",
        "fdr_alpha": FDR_ALPHA,
        "seed": SEED,
        "correlation_with_keff": all_res["K3"].get("corr_with_keff"),
    }

    for K in [3, 5, 7]:
        kk = f"K{K}"
        r = all_res[kk]
        output[kk] = {
            "n_panels": r["n_panels"],
            "eta_max_fdr_sig": r["eta_fdr_sig"],
            "kappa_div_fdr_sig": r["kd_fdr_sig"],
            "per_condition": r["per_condition"],
        }

    output["comparison_with_keff"] = {
        "K3": {"keff_sig": "4/12", "kappa_sig": all_res["K3"]["kd_fdr_sig"]},
        "K5": {"keff_sig": "10/12", "kappa_sig": all_res["K5"]["kd_fdr_sig"]},
        "K7": {"keff_sig": "9/12", "kappa_sig": all_res["K7"]["kd_fdr_sig"]},
    }

    out_path = PROJECT_ROOT / "docs" / "paper" / "data" / "kappa_diversity_regime_transition.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
    print(f"\nSaved: {out_path}")

    total_time = time.time() - t_start
    print(f"\n{'=' * 60}")
    print(f"REGIME TRANSITION COMPARISON (total time: {total_time:.0f}s)")
    print(f"{'=' * 60}")
    for K in [3, 5, 7]:
        kk = f"K{K}"
        r = all_res[kk]
        keff_sig = output["comparison_with_keff"][kk]["keff_sig"]
        print(f"  K={K}: η_max {r['eta_fdr_sig']}, κ_div {r['kd_fdr_sig']} (K_eff: {keff_sig})")


if __name__ == "__main__":
    main()

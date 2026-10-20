# Unified 10K bootstrap CI recomputation for Table 2 borderline configurations.
# Addresses R14-W1: confirms K* verdicts are stable under 10K vs 1K resamples.
# Pure CPU computation on OOF predictions — no model inference needed.

import csv
import json
import time
from pathlib import Path

import numpy as np
import lightgbm as lgb
from sklearn.model_selection import GroupKFold
from sklearn.metrics import roc_auc_score

FEAT_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
    "ttr", "hapax_ratio", "self_bleu",
    "freq_kurtosis", "freq_entropy", "low_freq_ratio",
]

THETA = 0.60
SEED = 42

CASES = [
    {
        "name": "LLaMA-3.1-8B (exp_018)",
        "data_dir": "/root/autodl-tmp/gen-depth-contamination/data/exp_018_llama8b",
        "depth_pair": (1, 2),
        "check": "ci_lower_gt_theta",
    },
    {
        "name": "Gemma-2-2B (exp_gemma2b)",
        "data_dir": "/root/autodl-tmp/gen-depth-contamination/data/exp_gemma2b_depth",
        "depth_pair": (1, 2),
        "check": "ci_upper_lt_theta",
    },
    {
        "name": "Mistral-7B (exp_019)",
        "data_dir": "/root/autodl-tmp/gen-depth-contamination/data_exp019_mistral7b",
        "depth_pair": (1, 2),
        "check": "ci_upper_lt_theta",
    },
    {
        "name": "512-tok (exp_021)",
        "data_dir": "/root/autodl-tmp/gen-depth-contamination/data/exp_021_length_512",
        "depth_pair": (1, 2),
        "check": "ci_lower_gt_theta",
    },
]

OUT_DIR = Path("/root/autodl-tmp/gen-depth-contamination/results/exp_bootstrap_10k")


def load_data(data_dir):
    with open(Path(data_dir) / "features.csv") as f:
        rows = list(csv.DictReader(f))
    depths = np.array([int(r["depth"]) for r in rows])
    doc_ids = np.array([int(r["doc_id"]) for r in rows])
    X = np.array(
        [[float(r[c]) if r[c] not in ("", "nan") else np.nan for c in FEAT_COLS] for r in rows]
    )
    col_means = np.nanmean(X, axis=0)
    for j in range(X.shape[1]):
        mask = np.isnan(X[:, j])
        X[mask, j] = col_means[j]
    return X, depths, doc_ids


def get_oof_predictions(X, y, groups):
    gkf = GroupKFold(n_splits=5)
    oof_proba = np.zeros(len(y))
    fold_aucs = []
    for train_idx, test_idx in gkf.split(X, y, groups=groups):
        clf = lgb.LGBMClassifier(
            n_estimators=200, max_depth=6, learning_rate=0.05,
            num_leaves=31, verbose=-1, n_jobs=-1,
        )
        clf.fit(X[train_idx], y[train_idx])
        proba = clf.predict_proba(X[test_idx])[:, 1]
        oof_proba[test_idx] = proba
        fold_aucs.append(roc_auc_score(y[test_idx], proba))
    return oof_proba, fold_aucs


def bootstrap_ci(y, oof_proba, doc_ids, n_boot, rng):
    unique_docs = np.unique(doc_ids)
    n_docs = len(unique_docs)
    doc_indices = [np.where(doc_ids == d)[0] for d in unique_docs]

    point_auc = roc_auc_score(y, oof_proba)
    boot_aucs = np.empty(n_boot)

    for b in range(n_boot):
        sampled = rng.randint(0, n_docs, size=n_docs)
        indices = np.concatenate([doc_indices[s] for s in sampled])
        try:
            boot_aucs[b] = roc_auc_score(y[indices], oof_proba[indices])
        except ValueError:
            boot_aucs[b] = np.nan

    boot_aucs = boot_aucs[~np.isnan(boot_aucs)]
    ci_lower = float(np.percentile(boot_aucs, 2.5))
    ci_upper = float(np.percentile(boot_aucs, 97.5))
    return point_auc, ci_lower, ci_upper, boot_aucs


def permutation_test(y, oof_proba, doc_ids, n_perm, rng, observed_auc):
    unique_docs, inverse = np.unique(doc_ids, return_inverse=True)
    n_docs = len(unique_docs)

    count_ge = 0
    for _ in range(n_perm):
        doc_labels = rng.randint(0, 2, size=n_docs)
        perm_y = doc_labels[inverse]
        if perm_y.sum() == 0 or perm_y.sum() == len(perm_y):
            continue
        perm_auc = roc_auc_score(perm_y, oof_proba)
        if perm_auc >= observed_auc:
            count_ge += 1
    return (count_ge + 1) / (n_perm + 1)


def verdict(check, ci_lower, ci_upper, point_auc):
    if check == "ci_lower_gt_theta":
        if ci_lower > THETA:
            return "K*=2"
        elif point_auc > THETA:
            return "BORDERLINE"
        else:
            return "K*=1"
    elif check == "ci_upper_lt_theta":
        if ci_upper < THETA:
            return "K*=1"
        elif point_auc < THETA:
            return "BORDERLINE"
        else:
            return "K*=2"
    return "UNKNOWN"


def main():
    t_start = time.time()
    all_results = {}

    for case in CASES:
        name = case["name"]
        d0, d1 = case["depth_pair"]
        print(f"\n{'='*60}", flush=True)
        print(f"Case: {name} (depth {d0}v{d1})", flush=True)
        print(f"{'='*60}", flush=True)

        t0 = time.time()
        X, depths, doc_ids = load_data(case["data_dir"])

        mask = (depths == d0) | (depths == d1)
        X_pair = X[mask]
        y_pair = (depths[mask] == d1).astype(int)
        groups_pair = doc_ids[mask]

        print(f"  Samples: {len(y_pair)} (class 0: {(y_pair==0).sum()}, class 1: {(y_pair==1).sum()})", flush=True)

        oof_proba, fold_aucs = get_oof_predictions(X_pair, y_pair, groups_pair)
        print(f"  Fold AUCs: {[round(a,4) for a in fold_aucs]}", flush=True)
        print(f"  Mean AUC: {np.mean(fold_aucs):.4f}", flush=True)

        # 1K bootstrap
        rng_1k = np.random.RandomState(SEED)
        point_auc_1k, ci_lower_1k, ci_upper_1k, boot_aucs_1k = bootstrap_ci(
            y_pair, oof_proba, groups_pair, 1000, rng_1k
        )
        v_1k = verdict(case["check"], ci_lower_1k, ci_upper_1k, point_auc_1k)
        print(f"  1K  bootstrap: AUC={point_auc_1k:.4f}  CI=[{ci_lower_1k:.4f}, {ci_upper_1k:.4f}]  -> {v_1k}", flush=True)

        # 10K bootstrap (fresh RNG to avoid seed-chain dependency)
        rng_10k = np.random.RandomState(SEED + 1)
        point_auc_10k, ci_lower_10k, ci_upper_10k, boot_aucs_10k = bootstrap_ci(
            y_pair, oof_proba, groups_pair, 10000, rng_10k
        )
        v_10k = verdict(case["check"], ci_lower_10k, ci_upper_10k, point_auc_10k)
        print(f"  10K bootstrap: AUC={point_auc_10k:.4f}  CI=[{ci_lower_10k:.4f}, {ci_upper_10k:.4f}]  -> {v_10k}", flush=True)

        # 10K permutation test
        rng_perm = np.random.RandomState(SEED + 2)
        perm_p = permutation_test(y_pair, oof_proba, groups_pair, 10000, rng_perm, point_auc_10k)
        print(f"  Permutation p-value (10K): {perm_p:.6f}", flush=True)

        flipped = v_1k != v_10k
        if flipped:
            print(f"  *** VERDICT FLIPPED: {v_1k} -> {v_10k} ***", flush=True)
        else:
            print(f"  Verdict stable: {v_10k}", flush=True)

        elapsed = time.time() - t0
        print(f"  Done in {elapsed:.1f}s", flush=True)

        all_results[name] = {
            "depth_pair": f"{d0}v{d1}",
            "1v2_auc": round(point_auc_10k, 4),
            "fold_aucs": [round(a, 4) for a in fold_aucs],
            "ci_1k": [round(ci_lower_1k, 4), round(ci_upper_1k, 4)],
            "ci_10k": [round(ci_lower_10k, 4), round(ci_upper_10k, 4)],
            "ci_width_1k": round(ci_upper_1k - ci_lower_1k, 4),
            "ci_width_10k": round(ci_upper_10k - ci_lower_10k, 4),
            "perm_p_10k": round(perm_p, 6),
            "boot_mean_10k": round(float(np.mean(boot_aucs_10k)), 4),
            "boot_std_10k": round(float(np.std(boot_aucs_10k)), 4),
            "verdict_1k": v_1k,
            "verdict_10k": v_10k,
            "flipped": flipped,
        }

    total_time = time.time() - t_start

    any_flipped = any(r["flipped"] for r in all_results.values())

    output = {
        "description": "Table 2 borderline bootstrap CI: 1K vs 10K comparison",
        "method": "GroupKFold(5) OOF + doc-level bootstrap + label permutation",
        "theta": THETA,
        "seed": SEED,
        "total_seconds": round(total_time, 1),
        "any_verdict_flipped": any_flipped,
        "note": "exp_017 (Qwen-cont) and exp_002 (OLMo-1B) excluded: features.csv not found on disk",
        "cases": all_results,
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / "bootstrap_10k_comparison.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}", flush=True)

    print("\n" + "="*60, flush=True)
    print("FINAL SUMMARY", flush=True)
    print("="*60, flush=True)
    print(f"Theta = {THETA}", flush=True)
    print(f"Any verdict flipped: {any_flipped}", flush=True)
    for name, r in all_results.items():
        flip_flag = " *** FLIPPED ***" if r["flipped"] else ""
        print(f"  {name}:", flush=True)
        print(f"    AUC={r['1v2_auc']:.4f}", flush=True)
        print(f"    1K  CI=[{r['ci_1k'][0]:.4f}, {r['ci_1k'][1]:.4f}] width={r['ci_width_1k']:.4f} -> {r['verdict_1k']}", flush=True)
        print(f"    10K CI=[{r['ci_10k'][0]:.4f}, {r['ci_10k'][1]:.4f}] width={r['ci_width_10k']:.4f} -> {r['verdict_10k']}{flip_flag}", flush=True)

    print(f"\nTotal time: {total_time:.1f}s", flush=True)


if __name__ == "__main__":
    main()

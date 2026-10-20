"""
exp_028_power_curve.py
Subsampling power analysis for K*=2 on C4.
Input: pre-extracted feature matrix from exp016_qwen_base
Output: power_curve.png/pdf, power_results.json
"""
import csv
import json
import time
from pathlib import Path

import numpy as np
import lightgbm as lgb
from sklearn.model_selection import GroupKFold
from sklearn.metrics import roc_auc_score
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

FEAT_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
    "ttr", "hapax_ratio", "self_bleu",
    "freq_kurtosis", "freq_entropy", "low_freq_ratio",
]

DATA_PATH = Path("/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/features.csv")
OUT_DIR = Path("/root/autodl-tmp/gen-depth-contamination/results/exp_028_power_curve")

SAMPLE_SIZES = [500, 1000, 2000, 3000, 4000, 5000]
N_RESAMPLES = 10
THETA = 0.60
N_FOLDS = 5
SEED_BASE = 42


def load_data():
    with open(DATA_PATH) as f:
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


def run_pairwise_cv(X, y, groups):
    gkf = GroupKFold(n_splits=N_FOLDS)
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
    overall_auc = roc_auc_score(y, oof_proba)
    return overall_auc, fold_aucs


def plot_power_curve(results_dict, out_dir):
    ns = sorted([int(k) for k in results_dict.keys()])
    means = [results_dict[str(n)]["mean_auc"] for n in ns]
    stds = [results_dict[str(n)]["std_auc"] for n in ns]
    det_probs = [results_dict[str(n)]["detection_probability"] for n in ns]

    fig, ax1 = plt.subplots(figsize=(3.5, 2.8))

    color_power = "#2563EB"
    color_auc = "#059669"

    ax1.plot(ns, det_probs, "s-", color=color_power, linewidth=1.5,
             markersize=5, label=r"P(AUC $>$ $\theta$)", zorder=3)
    ax1.set_xlabel("Number of documents ($n$)", fontsize=9)
    ax1.set_ylabel(r"$K^*\!=\!2$ detection rate", fontsize=9, color=color_power)
    ax1.tick_params(axis="y", labelcolor=color_power, labelsize=8)
    ax1.tick_params(axis="x", labelsize=8)
    ax1.set_ylim(-0.05, 1.1)
    ax1.set_xlim(300, 5300)
    ax1.axhline(y=0.8, color="#9333EA", linestyle=":", linewidth=0.8, alpha=0.6)
    ax1.text(350, 0.82, "80% power", fontsize=7, color="#9333EA", alpha=0.7)

    # find minimum n for 100% success
    full_success_ns = [n for n, p in zip(ns, det_probs) if p >= 1.0]
    if full_success_ns:
        min_full = min(full_success_ns)
        ax1.annotate(
            f"100% at $n$={min_full}",
            xy=(min_full, 1.0), xytext=(min_full + 300, 0.85),
            fontsize=7, color=color_power,
            arrowprops=dict(arrowstyle="->", color=color_power, lw=0.8),
        )

    ax2 = ax1.twinx()
    ax2.errorbar(ns, means, yerr=stds, fmt="o--", color=color_auc, capsize=3,
                 capthick=1.0, linewidth=1.2, markersize=4,
                 label=r"1v2 AUC (mean $\pm$ std)", zorder=2)
    ax2.axhline(y=THETA, color="#DC2626", linestyle="--", linewidth=1.0,
                label=f"$\\theta$ = {THETA}")
    ax2.set_ylabel("1v2 AUC", fontsize=9, color=color_auc)
    ax2.tick_params(axis="y", labelcolor=color_auc, labelsize=8)
    ax2.set_ylim(0.54, 0.68)

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, fontsize=7, loc="lower right",
               framealpha=0.9)

    ax1.grid(True, alpha=0.2, linewidth=0.5)
    fig.tight_layout()

    for ext in ["pdf", "png"]:
        out_path = out_dir / f"power_curve.{ext}"
        fig.savefig(str(out_path), dpi=300, bbox_inches="tight")
        print(f"Saved {out_path}", flush=True)
    plt.close()


def main():
    t0 = time.time()
    print("Loading features...", flush=True)
    X_all, depths_all, doc_ids_all = load_data()
    unique_docs_all = np.unique(doc_ids_all)
    print(f"Total: {len(depths_all)} rows, {len(unique_docs_all)} docs, "
          f"{len(FEAT_COLS)} features", flush=True)

    pair_mask_all = (depths_all == 1) | (depths_all == 2)

    rng = np.random.RandomState(SEED_BASE)
    results = {}

    print(f"\n{'n':>5}  {'trial':>5}  {'AUC':>7}  fold_aucs", flush=True)
    print("-" * 70, flush=True)

    for n in SAMPLE_SIZES:
        if n > len(unique_docs_all):
            print(f"Skip n={n}: only {len(unique_docs_all)} docs available", flush=True)
            continue

        trial_aucs = []
        trial_fold_aucs = []
        for trial in range(N_RESAMPLES):
            sampled_docs = set(rng.choice(unique_docs_all, n, replace=False))
            row_mask = np.array([d in sampled_docs for d in doc_ids_all])
            combined_mask = row_mask & pair_mask_all

            X_sub = X_all[combined_mask]
            y_sub = (depths_all[combined_mask] == 2).astype(int)
            groups_sub = doc_ids_all[combined_mask]

            auc, fold_aucs = run_pairwise_cv(X_sub, y_sub, groups_sub)
            trial_aucs.append(auc)
            trial_fold_aucs.append(fold_aucs)
            print(f"{n:>5}  {trial:>5}  {auc:.4f}  "
                  f"{[round(a, 4) for a in fold_aucs]}", flush=True)

        mean_auc = float(np.mean(trial_aucs))
        std_auc = float(np.std(trial_aucs))
        detect_prob = float(np.mean([a > THETA for a in trial_aucs]))

        results[str(n)] = {
            "n": n,
            "trial_aucs": [round(a, 4) for a in trial_aucs],
            "mean_auc": round(mean_auc, 4),
            "std_auc": round(std_auc, 4),
            "min_auc": round(float(np.min(trial_aucs)), 4),
            "max_auc": round(float(np.max(trial_aucs)), 4),
            "detection_probability": round(detect_prob, 2),
            "trial_fold_aucs": [[round(a, 4) for a in fa] for fa in trial_fold_aucs],
        }
        print(f"  => n={n}: mean={mean_auc:.4f} +/- {std_auc:.4f}, "
              f"P(AUC>{THETA})={detect_prob:.0%}", flush=True)

    elapsed = time.time() - t0

    output = {
        "experiment": "exp_028_power_curve",
        "description": "Subsampling power curve for K*=2 detection on C4",
        "source_data": "exp016_qwen_base (C4)",
        "feature_matrix": f"{len(depths_all)} rows x {len(FEAT_COLS)} features",
        "n_unique_docs": int(len(unique_docs_all)),
        "theta": THETA,
        "n_resamples": N_RESAMPLES,
        "n_folds": N_FOLDS,
        "sample_sizes": SAMPLE_SIZES,
        "total_seconds": round(elapsed, 1),
        "results": results,
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / "power_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved results to {out_path}", flush=True)
    print(f"Total time: {elapsed:.1f}s", flush=True)

    plot_power_curve(results, OUT_DIR)


if __name__ == "__main__":
    main()

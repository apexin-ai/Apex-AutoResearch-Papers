"""
feature_importance_stability.py — Kendall W concordance for permutation importance across 8-gen LOGO folds.
CPU-only. ~30min expected.
"""

import json
import os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.inspection import permutation_importance
from scipy.stats import chi2

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False, tree_method="approx", device="cpu")

CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
RESULTS_DIR = os.path.join(ROOT, "results")
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(os.path.join(ROOT, "logs"), exist_ok=True)


def load_data():
    df_base = pd.read_csv(os.path.join(DATA_DIR, "features_all_models.csv"))
    new_gens = [
        ("llama-3.2-3b", os.path.join(DATA_DIR, "llama-3.2-3b", "features_pythia410m.jsonl")),
        ("mistral-7b-v0.3", os.path.join(DATA_DIR, "mistral-7b-v0.3", "features_pythia410m.jsonl")),
    ]
    dfs = [df_base]
    for gen_name, path in new_gens:
        records = []
        with open(path) as f:
            for line in f:
                rec = json.loads(line)
                rec["model_name"] = gen_name
                records.append(rec)
        dfs.append(pd.DataFrame(records))

    cols = ["model_name", "seed_id", "depth"] + FEATURES
    df = pd.concat([d[cols] for d in dfs], ignore_index=True)
    return df


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df[label_col] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def kendall_w(rankings):
    """Compute Kendall W coefficient of concordance.
    rankings: array of shape (k, n) — k judges ranking n items.
    Returns (W, chi2_stat, p_value).
    """
    k, n = rankings.shape
    rank_sums = rankings.sum(axis=0)
    mean_rank_sum = rank_sums.mean()
    S = np.sum((rank_sums - mean_rank_sum) ** 2)
    W = 12 * S / (k**2 * (n**3 - n))
    # chi2 approximation
    chi2_stat = k * (n - 1) * W
    p_value = 1 - chi2.cdf(chi2_stat, df=n - 1)
    return W, chi2_stat, p_value


def main():
    print("Loading data...")
    df = load_data()
    df["label"] = df["depth"].map(CLASS_MAP_3)
    generators = sorted(df["model_name"].unique())
    print(f"Generators ({len(generators)}): {generators}")

    rng = np.random.RandomState(SEED)
    n_features = len(FEATURES)
    n_folds = len(generators)

    # Store importance values and rankings
    importance_matrix = np.zeros((n_folds, n_features))
    ranking_matrix = np.zeros((n_folds, n_features), dtype=int)

    for i, gen in enumerate(generators):
        print(f"\nFold {i+1}/{n_folds}: held-out = {gen}")
        test_df = df[df["model_name"] == gen]
        train_df = df[df["model_name"] != gen]
        train_ds = downsample(train_df, "label", rng)

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["label"].values)

        # Permutation importance on test set
        perm_result = permutation_importance(
            clf, test_df[FEATURES].values, test_df["label"].values,
            n_repeats=10, random_state=SEED, scoring="f1_macro", n_jobs=-1
        )
        imp = perm_result.importances_mean
        importance_matrix[i] = imp
        # Rank: highest importance = rank 1
        ranking_matrix[i] = n_features - np.argsort(np.argsort(imp))

        print(f"  Importances: {dict(zip(FEATURES, np.round(imp, 4)))}")
        print(f"  Rankings:    {dict(zip(FEATURES, ranking_matrix[i]))}")

    # Kendall W
    W, chi2_stat, p_val = kendall_w(ranking_matrix)
    print(f"\n{'='*60}")
    print(f"Kendall W = {W:.4f} (chi2 = {chi2_stat:.2f}, p = {p_val:.4e})")
    print(f"{'='*60}")

    # Mean ranks
    mean_ranks = ranking_matrix.mean(axis=0)
    print("\nFeature ranking summary:")
    sorted_idx = np.argsort(mean_ranks)
    for idx in sorted_idx:
        print(f"  {FEATURES[idx]:15s}  mean_rank={mean_ranks[idx]:.2f}  "
              f"ranks={list(ranking_matrix[:, idx])}")

    # Save results
    result = {
        "kendall_w": round(float(W), 4),
        "chi2_stat": round(float(chi2_stat), 2),
        "p_value": float(p_val),
        "n_folds": n_folds,
        "n_features": n_features,
        "features": FEATURES,
        "generators": generators,
        "importance_matrix": importance_matrix.tolist(),
        "ranking_matrix": ranking_matrix.tolist(),
        "mean_ranks": {FEATURES[i]: round(float(mean_ranks[i]), 2) for i in range(n_features)},
    }
    out_path = os.path.join(RESULTS_DIR, "feature_importance_stability.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Family-level hold-out evaluation (3-class, balanced downsample)."""
import json, numpy as np, pandas as pd
from pathlib import Path
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

ROOT = Path("/root/gen-depth-fingerprint")
DATA = ROOT / "data" / "features_all_models.csv"

FEAT_COLS = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
             "tail_decay", "ttr", "hapax_ratio"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=789, eval_metric="mlogloss", verbosity=0)

FAMILIES = {
    "pythia": ["pythia-1b", "pythia-2.8b"],
    "olmo":   ["olmo-2-1b"],
    "qwen":   ["qwen3-0.6b", "qwen3-1.7b", "qwen3-8b"],
}

def downsample(df, rng):
    counts = df["label"].value_counts()
    min_n = counts.min()
    parts = [df[df["label"] == lbl].sample(n=min_n, random_state=rng, replace=False)
             for lbl in sorted(counts.index)]
    return pd.concat(parts, ignore_index=True)

def main():
    df = pd.read_csv(DATA)
    df["label"] = df["depth"].map(CLASS_MAP)
    print(f"Loaded {len(df)} rows, label dist: {df['label'].value_counts().sort_index().to_dict()}")

    rng = np.random.RandomState(789)
    results = {}

    for held_family, held_gens in FAMILIES.items():
        train_df = df[~df["model_name"].isin(held_gens)].copy()
        test_df  = df[df["model_name"].isin(held_gens)].copy()

        train_ds = downsample(train_df, rng)
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEAT_COLS].values, train_ds["label"].values)
        y_pred = clf.predict(test_df[FEAT_COLS].values)
        y_true = test_df["label"].values

        macro_f1 = f1_score(y_true, y_pred, average="macro")

        per_gen = {}
        for g in held_gens:
            mask = test_df["model_name"] == g
            if mask.sum() > 0:
                gf1 = f1_score(y_true[mask.values], y_pred[mask.values], average="macro")
                per_gen[g] = round(gf1, 4)

        results[held_family] = {
            "macro_f1": round(macro_f1, 4),
            "train_gens": sorted(set(df["model_name"]) - set(held_gens)),
            "test_gens": held_gens,
            "train_size": len(train_ds),
            "test_size": len(test_df),
            "per_generator_f1": per_gen,
        }
        print(f"  {held_family:8s} held-out: macro_f1={macro_f1:.4f}  "
              f"(train={len(train_ds)}, test={len(test_df)})  per_gen={per_gen}")

    out_path = ROOT / "results" / "family_holdout_3class.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")

if __name__ == "__main__":
    main()

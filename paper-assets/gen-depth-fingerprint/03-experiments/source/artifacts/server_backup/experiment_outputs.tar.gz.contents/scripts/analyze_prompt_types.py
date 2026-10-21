import json
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

DATA_DIR = Path("/root/gen-depth-fingerprint/data")
FEATURES = ["entropy_mean", "entropy_std", "entropy_max", "entropy_min", "tail_decay", "ttr", "hapax_ratio"]
PROMPT_TYPES = ["continuation", "elaboration", "inspired_rewriting"]
OUTPUT_PATH = DATA_DIR / "prompt_type_results.json"

def load_data():
    frames = []
    for pt in PROMPT_TYPES:
        path = DATA_DIR / f"pythia-2.8b-{pt}" / "features.jsonl"
        with open(path) as f:
            records = [json.loads(line) for line in f]
        frames.append(pd.DataFrame(records))
    return pd.concat(frames, ignore_index=True)

def make_labels(depths):
    return np.where(depths == 0, 0, np.where(depths == 1, 1, 2))

def get_xgb():
    return XGBClassifier(
        n_estimators=200, max_depth=6, learning_rate=0.1,
        eval_metric="mlogloss", random_state=42,
        use_label_encoder=False
    )

def per_prompt_cv(df):
    results = {}
    for pt in PROMPT_TYPES:
        sub = df[df["prompt_type"] == pt]
        X = sub[FEATURES].values
        y = make_labels(sub["depth"].values)
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        f1s = []
        for train_idx, test_idx in skf.split(X, y):
            clf = get_xgb()
            clf.fit(X[train_idx], y[train_idx])
            pred = clf.predict(X[test_idx])
            f1s.append(f1_score(y[test_idx], pred, average="macro"))
        results[pt] = {"mean": round(np.mean(f1s), 4), "std": round(np.std(f1s), 4), "folds": [round(f, 4) for f in f1s]}
        print(f"  {pt}: F1={np.mean(f1s):.4f} ± {np.std(f1s):.4f}")
    return results

def lopto(df):
    results = {}
    X_all = df[FEATURES].values
    y_all = make_labels(df["depth"].values)
    pt_all = df["prompt_type"].values

    for held_out in PROMPT_TYPES:
        train_mask = pt_all != held_out
        test_mask = pt_all == held_out
        clf = get_xgb()
        clf.fit(X_all[train_mask], y_all[train_mask])
        pred = clf.predict(X_all[test_mask])
        f1 = f1_score(y_all[test_mask], pred, average="macro")
        results[held_out] = round(f1, 4)
        print(f"  Hold out {held_out}: F1={f1:.4f}")

    avg = round(np.mean(list(results.values())), 4)
    results["avg"] = avg
    print(f"  Average: F1={avg:.4f}")
    return results

def depth_decay(df):
    results = {}
    for pt in PROMPT_TYPES:
        sub = df[df["prompt_type"] == pt]
        counts = sub["depth"].value_counts().sort_index()
        d0 = counts.get(0, 0)
        d4 = counts.get(4, 0)
        max_depth = counts.index.max()
        d_max = counts.get(max_depth, 0)
        retention_d4 = round(d4 / d0 * 100, 1) if d0 > 0 else 0
        results[pt] = {
            "depth_counts": {int(k): int(v) for k, v in counts.items()},
            "d0": int(d0),
            "d4": int(d4),
            "retention_d4_pct": retention_d4,
            "max_depth": int(max_depth)
        }
        print(f"  {pt}: d0={d0}, d4={d4}, retention={retention_d4}%, depths={dict(counts)}")
    return results

def feature_drift(df):
    results = {}
    for pt in PROMPT_TYPES:
        sub = df[df["prompt_type"] == pt]
        drift = {}
        for feat in FEATURES:
            mean_d0 = sub[sub["depth"] == 0][feat].mean()
            mean_d4 = sub[sub["depth"] == 4][feat].mean()
            if abs(mean_d0) > 1e-10:
                rel_change = round((mean_d4 - mean_d0) / abs(mean_d0), 4)
            else:
                rel_change = 0.0
            drift[feat] = {
                "mean_d0": round(float(mean_d0), 6),
                "mean_d4": round(float(mean_d4), 6),
                "relative_change": rel_change
            }
        results[pt] = drift
        print(f"  {pt}: max drift = {max(abs(d['relative_change']) for d in drift.values()):.4f}")
    return results

def main():
    print("Loading data...")
    df = load_data()
    print(f"Total records: {len(df)}")
    for pt in PROMPT_TYPES:
        print(f"  {pt}: {len(df[df['prompt_type'] == pt])} records")

    print("\n=== 1. Per-prompt-type 5-fold CV ===")
    cv_results = per_prompt_cv(df)

    print("\n=== 2. Leave-One-Prompt-Type-Out ===")
    lopto_results = lopto(df)

    print("\n=== 3. Depth Decay ===")
    decay_results = depth_decay(df)

    print("\n=== 4. Feature Drift Rate ===")
    drift_results = feature_drift(df)

    all_results = {
        "per_prompt_cv_f1": cv_results,
        "lopto_f1": lopto_results,
        "depth_decay": decay_results,
        "feature_drift": drift_results
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()

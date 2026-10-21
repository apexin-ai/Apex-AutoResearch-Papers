import json, os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "data", "features_all_models.csv")
OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")

FEATURES = ["hapax_ratio", "ttr", "entropy_mean", "entropy_std", "entropy_min", "entropy_max", "tail_decay"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
FULL_F1 = 0.789

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=42, eval_metric="mlogloss", verbosity=0)


def downsample(df, rng):
    counts = df["label"].value_counts()
    min_n = counts.min()
    parts = [df[df["label"] == lbl].sample(n=min_n, random_state=rng, replace=False) for lbl in sorted(counts.index)]
    return pd.concat(parts, ignore_index=True)


def logo_eval(df, features):
    generators = sorted(df["model_name"].unique())
    per_gen = {}
    rng = np.random.RandomState(42)
    for gen in generators:
        train_df = downsample(df[df["model_name"] != gen], rng)
        test_df = df[df["model_name"] == gen]
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_df[features].values, train_df["label"].values)
        y_pred = clf.predict(test_df[features].values)
        per_gen[gen] = float(f1_score(test_df["label"].values, y_pred, average="macro"))
    avg = float(np.mean(list(per_gen.values())))
    return avg, per_gen


def main():
    df = pd.read_csv(DATA_PATH)
    df["label"] = df["depth"].map(CLASS_MAP)
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators\n")

    results = []
    for drop_feat in FEATURES:
        remaining = [f for f in FEATURES if f != drop_feat]
        avg_f1, per_gen = logo_eval(df, remaining)
        delta = avg_f1 - FULL_F1
        results.append({"dropped": drop_feat, "logo_f1": round(avg_f1, 4), "delta": round(delta, 4), "per_gen": {k: round(v, 4) for k, v in per_gen.items()}})
        print(f"Drop {drop_feat:15s} -> F1={avg_f1:.4f}  delta={delta:+.4f}")

    full_f1, full_per_gen = logo_eval(df, FEATURES)
    print(f"\nFull (sanity)     -> F1={full_f1:.4f}")

    output = {
        "full_baseline_f1": round(full_f1, 4),
        "reference_f1": FULL_F1,
        "lofo_results": results,
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "lofo_ablation_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")

    print("\n| Dropped feature | LOGO F1 | delta vs Full (0.789) |")
    print("|---|---|---|")
    for r in results:
        print(f"| {r['dropped']} | {r['logo_f1']:.4f} | {r['delta']:+.4f} |")

if __name__ == "__main__":
    main()

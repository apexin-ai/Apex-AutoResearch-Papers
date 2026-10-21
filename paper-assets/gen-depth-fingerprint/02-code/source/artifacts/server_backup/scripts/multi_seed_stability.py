import json
import os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "features_all_models.csv")
OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")

FEATURES = ["hapax_ratio", "ttr", "entropy_mean", "entropy_std", "entropy_min", "entropy_max", "tail_decay"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
SEEDS = [42, 123, 456, 789, 1024]


def downsample(df, rng):
    counts = df["label"].value_counts()
    min_n = counts.min()
    parts = [df[df["label"] == lbl].sample(n=min_n, random_state=rng, replace=False) for lbl in sorted(counts.index)]
    return pd.concat(parts, ignore_index=True)


def logo_eval(df, seed):
    generators = sorted(df["model_name"].unique())
    xgb_params = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                      random_state=seed, eval_metric="mlogloss", verbosity=0)
    rng = np.random.RandomState(seed)
    per_gen = {}
    for gen in generators:
        train_df = downsample(df[df["model_name"] != gen], rng)
        test_df = df[df["model_name"] == gen]
        clf = XGBClassifier(**xgb_params)
        clf.fit(train_df[FEATURES].values, train_df["label"].values)
        y_pred = clf.predict(test_df[FEATURES].values)
        per_gen[gen] = float(f1_score(test_df["label"].values, y_pred, average="macro"))
    avg = float(np.mean(list(per_gen.values())))
    return avg, per_gen


def main():
    df = pd.read_csv(DATA_PATH)
    df["label"] = df["depth"].map(CLASS_MAP)
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators\n")

    all_results = []
    for seed in SEEDS:
        avg_f1, per_gen = logo_eval(df, seed)
        all_results.append({"seed": seed, "logo_f1": round(avg_f1, 4), "per_gen": {k: round(v, 4) for k, v in per_gen.items()}})
        print(f"Seed {seed:5d} → F1={avg_f1:.4f}  per_gen={[f'{v:.3f}' for v in per_gen.values()]}")

    f1s = [r["logo_f1"] for r in all_results]
    mean_f1 = float(np.mean(f1s))
    std_f1 = float(np.std(f1s))
    print(f"\nMean F1: {mean_f1:.4f} ± {std_f1:.4f}")

    output = {
        "seeds": SEEDS,
        "per_seed": all_results,
        "summary": {"mean_f1": round(mean_f1, 4), "std_f1": round(std_f1, 4), "min_f1": round(min(f1s), 4), "max_f1": round(max(f1s), 4)},
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "multi_seed_stability.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()

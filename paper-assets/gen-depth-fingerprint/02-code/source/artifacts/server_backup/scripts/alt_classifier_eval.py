import json, os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False, verbosity=0)


def load_data(path):
    df = pd.read_csv(path)
    df["label"] = df["depth"].map(CLASS_MAP)
    return df


def downsample(df, rng):
    counts = df["label"].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df["label"] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def make_clf(name):
    if name == "XGBoost":
        return XGBClassifier(**XGB_PARAMS)
    elif name == "LogisticRegression":
        return Pipeline([
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(max_iter=1000, random_state=SEED))
        ])
    else:
        return RandomForestClassifier(n_estimators=100, random_state=SEED)


def logo_eval(df):
    generators = sorted(df["model_name"].unique())
    results = {}

    for clf_name in ["XGBoost", "LogisticRegression", "RandomForest"]:
        print(f"\n{'='*50}\nClassifier: {clf_name}\n{'='*50}")
        fold_results = {}
        f1_list = []

        for gen in generators:
            rng = np.random.RandomState(SEED)
            train_df = downsample(df[df["model_name"] != gen], rng)
            test_df = df[df["model_name"] == gen]

            X_train = train_df[FEATURES].values
            y_train = train_df["label"].values
            X_test = test_df[FEATURES].values
            y_test = test_df["label"].values

            clf = make_clf(clf_name)
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)

            macro_f1 = f1_score(y_test, y_pred, average="macro")
            per_class = f1_score(y_test, y_pred, average=None, labels=[0, 1, 2])
            fold_results[gen] = {
                "macro_f1": round(float(macro_f1), 4),
                "gen-0_f1": round(float(per_class[0]), 4),
                "gen-1_f1": round(float(per_class[1]), 4),
                "gen-2+_f1": round(float(per_class[2]), 4),
            }
            f1_list.append(macro_f1)
            print(f"  {gen:15s}  macro-F1={macro_f1:.4f}")

        avg_f1 = float(np.mean(f1_list))
        print(f"  {'AVERAGE':15s}  macro-F1={avg_f1:.4f}")
        results[clf_name] = {
            "average_f1": round(avg_f1, 4),
            "per_generator": fold_results,
        }

    return results


def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base, "data", "features_all_models.csv")
    df = load_data(csv_path)
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators")
    print(f"Class distribution: {df['label'].value_counts().sort_index().to_dict()}")

    results = logo_eval(df)

    # Summary table
    gens = sorted(list(results.values())[0]["per_generator"].keys())
    print(f"\n{'='*80}\nSUMMARY TABLE\n{'='*80}")
    hdr = f"| {'Classifier':20s} | {'LOGO F1':>7s} | " + " | ".join(f"{g:>10s}" for g in gens) + " |"
    print(hdr)
    print("|" + "-"*22 + "|" + "-"*9 + "|" + "|".join("-"*12 for _ in gens) + "|")
    for cn, r in results.items():
        gv = " | ".join(f"{r['per_generator'][g]['macro_f1']:>10.4f}" for g in gens)
        print(f"| {cn:20s} | {r['average_f1']:>7.4f} | {gv} |")

    out_dir = os.path.join(base, "results")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "alt_classifier_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

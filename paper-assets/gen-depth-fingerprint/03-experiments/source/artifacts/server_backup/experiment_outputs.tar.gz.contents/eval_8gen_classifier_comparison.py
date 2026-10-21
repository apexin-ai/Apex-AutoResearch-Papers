"""
8-gen Classifier Comparison: XGBoost vs RandomForest vs LogisticRegression
LOGO CV (Leave-One-Generator-Out), 3-class + binary tasks.
"""

import json
import os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.preprocessing import StandardScaler

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]

CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
RESULTS_DIR = os.path.join(ROOT, "results")


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


def bootstrap_f1(y_true, y_pred, n_boot=1000, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    scores = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        yt, yp = y_true[idx], y_pred[idx]
        if len(np.unique(yt)) < 2:
            continue
        scores.append(f1_score(yt, yp, average="macro"))
    arr = np.array(scores)
    return float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))


def make_classifiers():
    return {
        "xgboost": XGBClassifier(
            n_estimators=200, max_depth=6, learning_rate=0.1,
            random_state=SEED, eval_metric="mlogloss", use_label_encoder=False,
            verbosity=0
        ),
        "random_forest": RandomForestClassifier(
            n_estimators=200, max_depth=6, random_state=SEED
        ),
        "logistic_regression": LogisticRegression(
            max_iter=1000, random_state=SEED
        ),
    }


def logo_eval(df, task="3class"):
    """Run LOGO CV for all classifiers on a given task."""
    df = df.copy()
    if task == "3class":
        df["label"] = df["depth"].map(CLASS_MAP_3)
    else:
        df = df[df["depth"] >= 1].copy()
        df["label"] = (df["depth"] >= 2).astype(int)

    generators = sorted(df["model_name"].unique())
    rng = np.random.RandomState(SEED)

    all_results = {}
    for clf_name in ["xgboost", "random_forest", "logistic_regression"]:
        per_gen = {}
        all_y_true = []
        all_y_pred = []

        for gen in generators:
            test_df = df[df["model_name"] == gen]
            train_df = df[df["model_name"] != gen]
            train_ds = downsample(train_df, "label", rng)

            X_train = train_ds[FEATURES].values
            y_train = train_ds["label"].values
            X_test = test_df[FEATURES].values
            y_test = test_df["label"].values

            clf = make_classifiers()[clf_name]

            if clf_name == "logistic_regression":
                scaler = StandardScaler()
                X_train = scaler.fit_transform(X_train)
                X_test = scaler.transform(X_test)

            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)

            macro_f1 = f1_score(y_test, y_pred, average="macro")
            per_gen[gen] = round(float(macro_f1), 4)

            all_y_true.extend(y_test.tolist())
            all_y_pred.extend(y_pred.tolist())

        avg_f1 = round(float(np.mean(list(per_gen.values()))), 4)
        ci_lo, ci_hi = bootstrap_f1(np.array(all_y_true), np.array(all_y_pred))

        all_results[clf_name] = {
            "avg_f1": avg_f1,
            "ci95": [round(ci_lo, 4), round(ci_hi, 4)],
            "per_gen": per_gen,
        }
        print(f"  {clf_name:22s}  {task} F1={avg_f1:.4f}  CI=[{ci_lo:.4f}, {ci_hi:.4f}]")

    return all_results


def main():
    df = load_data()
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators")

    print("\n=== 3-class LOGO ===")
    results_3class = logo_eval(df, "3class")

    print("\n=== Binary LOGO ===")
    results_binary = logo_eval(df, "binary")

    # Assemble output
    classifiers = {}
    for clf_name in ["xgboost", "random_forest", "logistic_regression"]:
        classifiers[clf_name] = {
            "3class_f1": results_3class[clf_name]["avg_f1"],
            "3class_ci95": results_3class[clf_name]["ci95"],
            "binary_f1": results_binary[clf_name]["avg_f1"],
            "binary_ci95": results_binary[clf_name]["ci95"],
            "per_gen_3class": results_3class[clf_name]["per_gen"],
            "per_gen_binary": results_binary[clf_name]["per_gen"],
        }

    best = max(classifiers, key=lambda k: classifiers[k]["3class_f1"])

    output = {
        "classifiers": classifiers,
        "best_classifier": best,
        "config": {
            "n_generators": 8,
            "n_features": 7,
            "feature_names": FEATURES,
        },
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, "8gen_classifier_comparison.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

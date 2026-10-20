"""
eval_independent_seed.py — Cross-generator evaluation with independent seeds.

Trains XGBoost on one generator's features, tests on another.
Compares binary F1 (gen-1 vs gen-2+) with shared-seed LOGO baseline.
"""

import json
import os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score, classification_report

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="logloss",
                  use_label_encoder=False)

ROOT = os.path.dirname(os.path.abspath(__file__))


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
    return float(np.mean(arr)), float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))


def load_features(csv_path):
    df = pd.read_csv(csv_path)
    return df


def make_binary(df):
    df = df[df["depth"] > 0].copy()
    df["label"] = (df["depth"] >= 2).astype(int)
    return df


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df[label_col] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def cross_eval(train_df, test_df, train_name, test_name):
    rng = np.random.RandomState(SEED)
    train_ds = downsample(train_df, "label", rng)

    clf = XGBClassifier(**XGB_PARAMS)
    clf.fit(train_ds[FEATURES].values, train_ds["label"].values)
    y_pred = clf.predict(test_df[FEATURES].values)
    y_test = test_df["label"].values

    f1 = f1_score(y_test, y_pred, average="macro")
    mean_f1, ci_lo, ci_hi = bootstrap_f1(y_test, y_pred)

    print(f"\n  {train_name} -> {test_name}")
    print(f"    Binary F1 = {f1:.4f}  95% CI = [{ci_lo:.4f}, {ci_hi:.4f}]")
    print(f"    n_train = {len(train_ds)}, n_test = {len(test_df)}")
    print(classification_report(y_test, y_pred, target_names=["gen-1", "gen-2+"]))

    return {
        "train": train_name,
        "test": test_name,
        "binary_f1": round(float(f1), 4),
        "ci_lower": round(ci_lo, 4),
        "ci_upper": round(ci_hi, 4),
        "n_train": int(len(train_ds)),
        "n_test": int(len(test_df)),
    }


def main():
    pythia_path = os.path.join(ROOT, "data", "features_indep_pythia-2.8b.csv")
    olmo_path = os.path.join(ROOT, "data", "features_indep_olmo-2-1b.csv")

    print("Loading features...")
    df_pythia = make_binary(load_features(pythia_path))
    df_olmo = make_binary(load_features(olmo_path))

    print(f"  Pythia-2.8B (Set A): {len(df_pythia)} samples, label dist: {df_pythia['label'].value_counts().to_dict()}")
    print(f"  OLMo-2-1B (Set B):   {len(df_olmo)} samples, label dist: {df_olmo['label'].value_counts().to_dict()}")

    print("\n=== Independent-Seed Cross-Generator Evaluation ===")

    r1 = cross_eval(df_pythia, df_olmo, "Pythia-2.8B (SetA)", "OLMo-2-1B (SetB)")
    r2 = cross_eval(df_olmo, df_pythia, "OLMo-2-1B (SetB)", "Pythia-2.8B (SetA)")

    avg_f1 = round((r1["binary_f1"] + r2["binary_f1"]) / 2, 4)

    output = {
        "experiment": "independent_seed_control",
        "description": "Cross-generator depth classification with non-overlapping Wikipedia seeds",
        "results": [r1, r2],
        "average_binary_f1": avg_f1,
        "shared_seed_logo_binary_f1_ref": 0.694,
        "delta_vs_shared": round(avg_f1 - 0.694, 4),
    }

    os.makedirs(os.path.join(ROOT, "results"), exist_ok=True)
    out_path = os.path.join(ROOT, "results", "independent_seed_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"Independent-Seed Control Summary")
    print(f"{'='*60}")
    print(f"{'Setting':<30s} {'Train->Test':<25s} {'Binary F1':>10s} {'95% CI':>20s}")
    print(f"{'-'*85}")
    print(f"{'Independent seeds':<30s} {'Pythia->OLMo':<25s} {r1['binary_f1']:>10.4f} [{r1['ci_lower']:.4f}, {r1['ci_upper']:.4f}]")
    print(f"{'Independent seeds':<30s} {'OLMo->Pythia':<25s} {r2['binary_f1']:>10.4f} [{r2['ci_lower']:.4f}, {r2['ci_upper']:.4f}]")
    print(f"{'Independent seeds (avg)':<30s} {'bidirectional':<25s} {avg_f1:>10.4f}")
    print(f"{'Shared seeds (ref)':<30s} {'LOGO avg':<25s} {'0.694':>10s} [0.688, 0.700]")
    print(f"{'-'*85}")
    delta = avg_f1 - 0.694
    conclusion = "COMPARABLE" if abs(delta) < 0.05 else ("HIGHER" if delta > 0 else "LOWER")
    print(f"Delta vs shared-seed: {delta:+.4f} ({conclusion})")
    if conclusion == "COMPARABLE":
        print("=> Topic fingerprint leakage ruled out: classifier learns depth signal, not topic identity.")
    else:
        print(f"=> Result is {conclusion} than shared-seed baseline. Further investigation needed.")

    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()

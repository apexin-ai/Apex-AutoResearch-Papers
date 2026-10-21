"""
eval_exp052_instruct.py — Within-model CV for instruct vs base model comparison.

Evaluates 3-class and binary depth classification on instruct-tuned and
base model features using stratified 5-fold cross-validation.
"""
import json
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
SEED = 42
N_BOOT = 1000

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "..", "data")
RESULTS_DIR = os.path.join(ROOT, "..", "results")


def eval_model(csv_path, model_name):
    df = pd.read_csv(csv_path)
    print(f"\n=== {model_name} ({len(df)} records) ===")
    print(f"Depth distribution: {df['depth'].value_counts().sort_index().to_dict()}")

    df["label_3"] = df["depth"].apply(lambda d: 0 if d == 0 else (1 if d == 1 else 2))
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    X3, y3 = df[FEATURES].values, df["label_3"].values
    preds_3 = np.zeros(len(y3), dtype=int)
    for tr, te in skf.split(X3, y3):
        clf = XGBClassifier(n_estimators=200, max_depth=6, learning_rate=0.1,
                            random_state=SEED, eval_metric="mlogloss")
        clf.fit(X3[tr], y3[tr])
        preds_3[te] = clf.predict(X3[te])
    f1_3 = f1_score(y3, preds_3, average="macro")
    print(f"3-class macro F1: {f1_3:.4f}")

    for c, name in [(0, "gen-0"), (1, "gen-1"), (2, "gen-2+")]:
        f1_c = f1_score(y3 == c, preds_3 == c, average="binary")
        print(f"  {name} F1: {f1_c:.4f}")

    df_bin = df[df["depth"] >= 1].copy()
    df_bin["label_bin"] = df_bin["depth"].apply(lambda d: 0 if d == 1 else 1)
    Xb, yb = df_bin[FEATURES].values, df_bin["label_bin"].values
    preds_b = np.zeros(len(yb), dtype=int)
    for tr, te in skf.split(Xb, yb):
        clf = XGBClassifier(n_estimators=200, max_depth=6, learning_rate=0.1,
                            random_state=SEED, eval_metric="logloss")
        clf.fit(Xb[tr], yb[tr])
        preds_b[te] = clf.predict(Xb[te])
    f1_b = f1_score(yb, preds_b, average="binary")

    rng = np.random.RandomState(SEED)
    boots = []
    for _ in range(N_BOOT):
        idx = rng.randint(0, len(yb), size=len(yb))
        boots.append(f1_score(yb[idx], preds_b[idx], average="binary"))
    ci_lo, ci_hi = np.percentile(boots, 2.5), np.percentile(boots, 97.5)
    print(f"Binary F1: {f1_b:.4f}  95% CI: [{ci_lo:.4f}, {ci_hi:.4f}]")

    boots_3 = []
    for _ in range(N_BOOT):
        idx = rng.randint(0, len(y3), size=len(y3))
        boots_3.append(f1_score(y3[idx], preds_3[idx], average="macro"))
    ci3_lo, ci3_hi = np.percentile(boots_3, 2.5), np.percentile(boots_3, 97.5)
    print(f"3-class F1 95% CI: [{ci3_lo:.4f}, {ci3_hi:.4f}]")

    return {
        "model": model_name,
        "n_records": len(df),
        "binary_f1": round(f1_b, 4),
        "binary_ci95": [round(ci_lo, 4), round(ci_hi, 4)],
        "3class_f1": round(f1_3, 4),
        "3class_ci95": [round(ci3_lo, 4), round(ci3_hi, 4)],
    }


def main():
    instruct_csv = os.path.join(DATA_DIR, "features_qwen3-1.7b-instruct.csv")
    base_csv = os.path.join(DATA_DIR, "features_qwen3-1.7b.csv")

    results = {}
    results["instruct"] = eval_model(instruct_csv, "Qwen3-1.7B-Instruct")
    results["base"] = eval_model(base_csv, "Qwen3-1.7B-Base")

    print("\n=== Comparison ===")
    for metric in ["binary_f1", "3class_f1"]:
        delta = results["instruct"][metric] - results["base"][metric]
        print(f"{metric}: instruct={results['instruct'][metric]:.4f}, base={results['base'][metric]:.4f}, delta={delta:+.4f}")

    results["delta"] = {
        "binary_f1": round(results["instruct"]["binary_f1"] - results["base"]["binary_f1"], 4),
        "3class_f1": round(results["instruct"]["3class_f1"] - results["base"]["3class_f1"], 4),
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, "instruct_eval.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()

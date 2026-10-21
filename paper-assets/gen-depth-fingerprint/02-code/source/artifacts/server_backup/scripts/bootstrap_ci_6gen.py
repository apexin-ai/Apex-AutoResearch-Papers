#!/usr/bin/env python3
"""Bootstrap 95% CI for 6-gen and 5-gen LOGO macro-F1.
Output: results/bootstrap_ci_results.json
"""
import json, time
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

ROOT = Path("/root/gen-depth-fingerprint")
DATA = ROOT / "data"
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True)

N_BOOT = 1000
SEED = 42

FEAT_COLS = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
             "tail_decay", "ttr", "hapax_ratio"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)

ALL_6 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b"]
ALL_5 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b"]


def logo_predictions(X, y, groups):
    preds = np.full(len(y), -1, dtype=int)
    for hold in sorted(set(groups)):
        tr = groups != hold
        te = groups == hold
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(X[tr], y[tr])
        preds[te] = clf.predict(X[te])
    return preds


def bootstrap_ci(y_true, y_pred, rng, n_boot=N_BOOT):
    n = len(y_true)
    f1s = np.empty(n_boot)
    for b in range(n_boot):
        idx = rng.randint(0, n, size=n)
        f1s[b] = f1_score(y_true[idx], y_pred[idx], average="macro")
    lo = float(np.percentile(f1s, 2.5))
    hi = float(np.percentile(f1s, 97.5))
    return round(float(np.mean(f1s)), 4), round(lo, 4), round(hi, 4)


def run_logo(df, model_list, label):
    sub = df[df["model_name"].isin(model_list)].copy()
    X = sub[FEAT_COLS].values
    y = sub["label"].values
    groups = sub["model_name"].values

    preds = logo_predictions(X, y, groups)
    f1_obs = round(f1_score(y, preds, average="macro"), 4)
    print(f"  {label}: pooled F1 = {f1_obs}")

    rng = np.random.RandomState(SEED)
    mean, lo, hi = bootstrap_ci(y, preds, rng)

    per_gen = {}
    for g in sorted(model_list):
        mask = groups == g
        rng_g = np.random.RandomState(SEED)
        gm, gl, gh = bootstrap_ci(y[mask], preds[mask], rng_g)
        f1_g = round(f1_score(y[mask], preds[mask], average="macro"), 4)
        per_gen[g] = {"f1": f1_g, "mean": gm, "ci_lower": gl, "ci_upper": gh}
        print(f"    {g}: f1={f1_g}, CI=[{gl}, {gh}]")

    return {
        "f1_observed": f1_obs,
        "mean": mean,
        "ci_lower": lo,
        "ci_upper": hi,
        "n_bootstrap": N_BOOT,
        "n_samples": len(sub),
        "per_generator": per_gen,
    }


def main():
    t0 = time.time()
    print("Loading data...")
    df = pd.read_csv(DATA / "features_all_models.csv")
    df["label"] = df["depth"].map(CLASS_MAP)
    print(f"  Total: {len(df)} rows, models: {sorted(df['model_name'].unique())}")

    results = {"seed": SEED, "n_bootstrap": N_BOOT, "xgb_params": XGB_PARAMS}

    print("\n6-gen LOGO:")
    results["logo_6gen"] = run_logo(df, ALL_6, "6-gen")

    print("\n5-gen LOGO (excl qwen3-8b):")
    results["logo_5gen"] = run_logo(df, ALL_5, "5-gen")

    out_path = OUT / "bootstrap_ci_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path} ({time.time()-t0:.1f}s)")


if __name__ == "__main__":
    main()

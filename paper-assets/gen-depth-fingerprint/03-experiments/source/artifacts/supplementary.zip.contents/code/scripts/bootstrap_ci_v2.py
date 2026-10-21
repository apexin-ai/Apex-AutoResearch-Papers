#!/usr/bin/env python3
"""Bootstrap 95% CI for 6-gen LOGO macro-F1 (corrected).
Key fix: adds downsample to match registry LOGO evaluation.
Output: results/bootstrap_ci_v2_results.json
"""
import json, time
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT.parent / "data"
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True)

N_BOOT = 1000
LOGO_SEED = 789
BOOT_SEED = 42

FEAT_COLS = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
             "tail_decay", "ttr", "hapax_ratio"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=789, eval_metric="mlogloss", verbosity=0)

ALL_6 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b"]

REGISTRY = {
    "pythia-1b": 0.856, "pythia-2.8b": 0.804, "olmo-2-1b": 0.764,
    "qwen3-0.6b": 0.824, "qwen3-1.7b": 0.805, "qwen3-8b": 0.683,
}


def downsample(df, rng):
    counts = df["label"].value_counts()
    min_n = counts.min()
    parts = [df[df["label"] == lbl].sample(n=min_n, random_state=rng, replace=False)
             for lbl in sorted(counts.index)]
    return pd.concat(parts, ignore_index=True)


def logo_predictions(df):
    preds = np.full(len(df), -1, dtype=int)
    rng = np.random.RandomState(LOGO_SEED)
    for hold in sorted(ALL_6):
        train_df = downsample(df[df["model_name"] != hold], rng)
        test_mask = (df["model_name"] == hold).values
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_df[FEAT_COLS].values, train_df["label"].values)
        preds[test_mask] = clf.predict(df.loc[test_mask, FEAT_COLS].values)
    assert (preds >= 0).all()
    return preds


def main():
    t0 = time.time()
    print("Loading data...")
    df = pd.read_csv(DATA / "features_all_models.csv")
    df["label"] = df["depth"].map(CLASS_MAP)
    df = df[df["model_name"].isin(ALL_6)].copy().reset_index(drop=True)
    print(f"  N={len(df)}")

    print("\nLOGO with downsample...")
    preds = logo_predictions(df)
    y = df["label"].values
    groups = df["model_name"].values

    print("\nPoint estimates vs registry:")
    max_bias = 0
    for g in sorted(ALL_6):
        mask = groups == g
        f1_g = round(f1_score(y[mask], preds[mask], average="macro"), 4)
        bias = abs(f1_g - REGISTRY[g])
        max_bias = max(max_bias, bias)
        print(f"  {g}: {f1_g} (reg={REGISTRY[g]}, bias={bias:.4f})")

    avg_f1 = round(np.mean([f1_score(y[groups == g], preds[groups == g], average="macro") for g in ALL_6]), 4)
    print(f"  Average: {avg_f1} (reg=0.789)")

    if max_bias > 0.005:
        print(f"  WARNING: max bias {max_bias:.4f} > 0.005")
        return

    rng = np.random.RandomState(BOOT_SEED)
    print(f"\nBootstrap n={N_BOOT}...")

    per_gen = {}
    for g in sorted(ALL_6):
        mask = groups == g
        yt, yp = y[mask], preds[mask]
        n = len(yt)
        f1_obs = round(f1_score(yt, yp, average="macro"), 4)
        f1s = np.empty(N_BOOT)
        for b in range(N_BOOT):
            idx = rng.randint(0, n, size=n)
            f1s[b] = f1_score(yt[idx], yp[idx], average="macro")
        lo = round(float(np.percentile(f1s, 2.5)), 3)
        hi = round(float(np.percentile(f1s, 97.5)), 3)
        per_gen[g] = {"f1": f1_obs, "ci_lower": lo, "ci_upper": hi}
        print(f"  {g}: {f1_obs} [{lo}, {hi}]")

    print(f"  avg F1: {avg_f1}")

    print(f"\nOverall 6-gen CI (bootstrap n={N_BOOT})...")
    overall_f1 = round(f1_score(y, preds, average="macro"), 4)
    rng_ov = np.random.RandomState(BOOT_SEED + 1)
    n_all = len(y)
    f1s_overall = np.empty(N_BOOT)
    for b in range(N_BOOT):
        idx = rng_ov.randint(0, n_all, size=n_all)
        f1s_overall[b] = f1_score(y[idx], preds[idx], average="macro")
    ov_lo = round(float(np.percentile(f1s_overall, 2.5)), 3)
    ov_hi = round(float(np.percentile(f1s_overall, 97.5)), 3)
    ov_width = round(ov_hi - ov_lo, 3)
    print(f"  Overall F1: {overall_f1} [{ov_lo}, {ov_hi}] (width={ov_width})")

    results = {
        "method": "bootstrap_ci_v2_corrected",
        "n_samples": len(df),
        "n_bootstrap": N_BOOT,
        "logo_seed": LOGO_SEED,
        "boot_seed": BOOT_SEED,
        "xgb_params": {k: v for k, v in XGB_PARAMS.items() if k != "verbosity"},
        "avg_6gen_f1": avg_f1,
        "per_generator": per_gen,
        "overall_f1": overall_f1,
        "overall_ci95": [ov_lo, ov_hi],
        "overall_ci_width": ov_width,
    }

    out_path = OUT / "bootstrap_ci_v2_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")
    print(f"Total: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()

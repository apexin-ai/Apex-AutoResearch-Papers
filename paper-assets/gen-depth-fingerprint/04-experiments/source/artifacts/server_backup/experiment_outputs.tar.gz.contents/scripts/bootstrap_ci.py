#!/usr/bin/env python3
"""Bootstrap 95% CI for plan-015 detector comparison.
Uses pre-computed scores. No GPU needed.
Output: data/plan015_bootstrap_ci.json
"""
import json, time
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.stats import spearmanr
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

ROOT = Path("/root/gen-depth-fingerprint")
DATA = ROOT / "data"
N_BOOT = 1000
SEED = 42

MODELS = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b"]
FEAT_COLS = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
             "tail_decay", "ttr", "hapax_ratio"]


def load_data():
    scores = pd.read_csv(DATA / "detector_scores.csv")
    feats = pd.read_csv(DATA / "features_all_models.csv")
    scores = scores[scores["model_name"].isin(MODELS)].copy()
    feats = feats[feats["model_name"].isin(MODELS)].copy()
    df = scores.merge(feats[["model_name", "seed_id", "depth"] + FEAT_COLS],
                      on=["model_name", "seed_id", "depth"], how="inner",
                      suffixes=("", "_dup"))
    df.drop(columns=[c for c in df.columns if c.endswith("_dup")], inplace=True)
    df["label"] = df["depth"].clip(upper=2)
    return df


def logo_predictions(X, y, models, max_depth):
    preds = np.zeros(len(y), dtype=int)
    for hold in sorted(set(models)):
        tr, te = models != hold, models == hold
        clf = XGBClassifier(n_estimators=100, max_depth=max_depth, learning_rate=0.1,
                            objective="multi:softmax", num_class=3,
                            eval_metric="mlogloss", verbosity=0, random_state=42)
        clf.fit(X[tr], y[tr])
        preds[te] = clf.predict(X[te])
    return preds


def bootstrap_f1(y_true, y_pred, rng):
    n = len(y_true)
    f1s = np.empty(N_BOOT)
    for b in range(N_BOOT):
        idx = rng.randint(0, n, size=n)
        f1s[b] = f1_score(y_true[idx], y_pred[idx], average="macro")
    return f1s


def bootstrap_paired_delta(y_true, pred_a, pred_b, rng):
    n = len(y_true)
    deltas = np.empty(N_BOOT)
    for b in range(N_BOOT):
        idx = rng.randint(0, n, size=n)
        deltas[b] = (f1_score(y_true[idx], pred_a[idx], average="macro") -
                     f1_score(y_true[idx], pred_b[idx], average="macro"))
    return deltas


def bootstrap_spearman(scores, targets, rng):
    n = len(scores)
    rhos = np.empty(N_BOOT)
    for b in range(N_BOOT):
        idx = rng.randint(0, n, size=n)
        rhos[b], _ = spearmanr(scores[idx], targets[idx])
    return rhos


def ci95(vals):
    return [round(float(np.percentile(vals, 2.5)), 4),
            round(float(np.percentile(vals, 97.5)), 4)]


def main():
    t0 = time.time()
    rng = np.random.RandomState(SEED)

    print("Loading data...")
    df = load_data()
    y = df["label"].values
    models = df["model_name"].values
    depths = df["depth"].values
    print(f"  N={len(df)}")

    detectors = {
        "avg_logprob": (df[["log_likelihood"]].values, 3),
        "fastdetectgpt": (df[["fast_detect_gpt"]].values, 3),
        "seven_feature": (df[FEAT_COLS].values, 5),
    }

    print("LOGO CV predictions...")
    logo_preds = {}
    for name, (X, md) in detectors.items():
        preds = logo_predictions(X, y, models, md)
        f1 = f1_score(y, preds, average="macro")
        logo_preds[name] = preds
        print(f"  {name}: LOGO F1 = {f1:.4f}")

    results = {"n_samples": len(df), "n_bootstrap": N_BOOT, "seed": SEED}

    # 1) Bootstrap CI for each detector's LOGO F1
    print("\nBootstrap LOGO F1 CIs...")
    for name, preds in logo_preds.items():
        f1_obs = round(f1_score(y, preds, average="macro"), 4)
        f1s = bootstrap_f1(y, preds, rng)
        results[f"{name}_logo_f1"] = {
            "point": f1_obs,
            "ci_95": ci95(f1s),
            "std": round(float(np.std(f1s)), 4),
        }
        print(f"  {name}: {f1_obs} {ci95(f1s)}")

    # 2) Paired bootstrap: 7-feature vs avg_logprob
    print("\nPaired bootstrap: seven_feature vs avg_logprob...")
    deltas = bootstrap_paired_delta(y, logo_preds["seven_feature"], logo_preds["avg_logprob"], rng)
    delta_obs = round(f1_score(y, logo_preds["seven_feature"], average="macro") -
                      f1_score(y, logo_preds["avg_logprob"], average="macro"), 4)
    p = round(float(np.mean(deltas <= 0)), 4)
    results["seven_feature_vs_avg_logprob"] = {
        "delta_f1": delta_obs,
        "ci_95": ci95(deltas),
        "p_value": p,
        "significant_005": p < 0.05,
    }
    print(f"  dF1={delta_obs} {ci95(deltas)} p={p}")

    # 3) Paired bootstrap: 7-feature vs fastdetectgpt
    print("Paired bootstrap: seven_feature vs fastdetectgpt...")
    deltas2 = bootstrap_paired_delta(y, logo_preds["seven_feature"], logo_preds["fastdetectgpt"], rng)
    delta_obs2 = round(f1_score(y, logo_preds["seven_feature"], average="macro") -
                       f1_score(y, logo_preds["fastdetectgpt"], average="macro"), 4)
    p2 = round(float(np.mean(deltas2 <= 0)), 4)
    results["seven_feature_vs_fastdetectgpt"] = {
        "delta_f1": delta_obs2,
        "ci_95": ci95(deltas2),
        "p_value": p2,
        "significant_005": p2 < 0.05,
    }
    print(f"  dF1={delta_obs2} {ci95(deltas2)} p={p2}")

    # 4) Spearman rho bootstrap CI
    print("\nSpearman rho bootstrap CIs...")
    score_cols = {"avg_logprob": "log_likelihood", "fastdetectgpt": "fast_detect_gpt"}
    for name, col in score_cols.items():
        sc = df[col].values
        for tname, tgt in [("label", y), ("raw_depth", depths)]:
            rho_obs, _ = spearmanr(sc, tgt)
            rhos = bootstrap_spearman(sc, tgt, rng)
            results[f"{name}_spearman_{tname}"] = {
                "point": round(float(rho_obs), 4),
                "ci_95": ci95(rhos),
            }
            print(f"  {name} vs {tname}: rho={rho_obs:.4f} {ci95(rhos)}")

    results["_note"] = "avg_logprob = log_likelihood column in detector_scores.csv"

    out = DATA / "plan015_bootstrap_ci.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out}  ({time.time()-t0:.1f}s)")


if __name__ == "__main__":
    main()

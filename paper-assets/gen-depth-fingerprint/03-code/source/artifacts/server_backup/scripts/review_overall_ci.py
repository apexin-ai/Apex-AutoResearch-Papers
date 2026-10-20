# 6-gen overall bootstrap CI + 7-feature Spearman rho for review response
import json, time
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.stats import spearmanr
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


def logo_predictions(X, y, groups):
    """LOGO: leave-one-generator-out, return predictions for all samples."""
    preds = np.full(len(y), -1, dtype=int)
    for hold in sorted(set(groups)):
        tr = groups != hold
        te = groups == hold
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(X[tr], y[tr])
        preds[te] = clf.predict(X[te])
    return preds


def bootstrap_overall_ci(y_true, y_pred, n_boot=N_BOOT, seed=SEED):
    """Bootstrap 95% CI for macro-F1 over all pooled test samples."""
    rng = np.random.RandomState(seed)
    n = len(y_true)
    f1s = np.empty(n_boot)
    for b in range(n_boot):
        idx = rng.randint(0, n, size=n)
        f1s[b] = f1_score(y_true[idx], y_pred[idx], average="macro")
    return float(np.percentile(f1s, 2.5)), float(np.percentile(f1s, 97.5))


def compute_spearman(df):
    """Spearman rho for each feature vs original depth (0-4)."""
    results = {}
    for feat in FEAT_COLS:
        rho, p = spearmanr(df[feat], df["depth"])
        results[feat] = {"rho": round(float(rho), 4), "p": float(f"{p:.2e}")}
    return results


def main():
    t0 = time.time()
    print("Loading 6-gen data...")
    df = pd.read_csv(DATA / "features_all_models.csv")
    df["label"] = df["depth"].map(CLASS_MAP)

    models_present = sorted(df["model_name"].unique())
    print(f"  {len(df)} rows, models: {models_present}")
    assert set(ALL_6).issubset(set(models_present)), f"Missing generators: {set(ALL_6) - set(models_present)}"

    sub = df[df["model_name"].isin(ALL_6)].copy()
    X = sub[FEAT_COLS].values
    y = sub["label"].values
    groups = sub["model_name"].values

    # --- LOGO predictions ---
    print("Running 6-gen LOGO...")
    preds = logo_predictions(X, y, groups)
    overall_f1 = round(f1_score(y, preds, average="macro"), 4)
    print(f"  Overall F1 = {overall_f1}")

    # --- Per-generator F1 ---
    per_gen = {}
    for g in sorted(ALL_6):
        mask = groups == g
        f1_g = round(f1_score(y[mask], preds[mask], average="macro"), 4)
        per_gen[g] = f1_g
        print(f"    {g}: {f1_g}")

    # --- Bootstrap CI for overall F1 ---
    print(f"Bootstrap CI (n={N_BOOT})...")
    ci_lo, ci_hi = bootstrap_overall_ci(y, preds)
    print(f"  95% CI = [{ci_lo:.4f}, {ci_hi:.4f}]")

    # --- Spearman rho (on original depth 0-4, all 6 gens) ---
    print("Spearman rho (depth 0-4)...")
    spearman = compute_spearman(sub)
    for feat, vals in spearman.items():
        print(f"  {feat}: rho={vals['rho']}, p={vals['p']}")

    # --- Output ---
    results = {
        "n_generators": 6,
        "overall_logo_f1": overall_f1,
        "overall_ci95": [round(ci_lo, 4), round(ci_hi, 4)],
        "bootstrap_n": N_BOOT,
        "per_generator_f1": per_gen,
        "spearman_rho": spearman,
    }

    out_path = OUT / "review_overall_ci_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path} ({time.time()-t0:.1f}s)")


if __name__ == "__main__":
    main()

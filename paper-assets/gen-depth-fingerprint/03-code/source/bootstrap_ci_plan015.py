# Bootstrap CI significance test for plan-015 ordinal baseline.
# Compares 7-feature vs avg_logprob LOGO F1 via paired bootstrap.
import json
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

ROOT = Path("/root/gen-depth-fingerprint")
SEED = 42
N_BOOT = 1000
MODELS = ["olmo-2-1b", "pythia-1b", "pythia-2.8b", "qwen3-0.6b", "qwen3-1.7b"]
FEAT_7 = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
           "tail_decay", "ttr", "hapax_ratio"]

def load_data():
    feat = pd.read_csv(ROOT / "data" / "features_all_models.csv")
    det = pd.read_csv(ROOT / "data" / "detector_scores.csv")
    feat = feat[feat["model_name"].isin(MODELS)].copy()
    det = det[det["model_name"].isin(MODELS)].copy()
    feat["label"] = feat["depth"].clip(upper=2)
    det["label"] = det["depth"].clip(upper=2)
    merged = feat.merge(det[["model_name", "seed_id", "depth", "log_likelihood", "fast_detect_gpt"]],
                        on=["model_name", "seed_id", "depth"], how="inner")
    assert len(merged) == len(feat), f"Merge mismatch: {len(merged)} vs {len(feat)}"
    return merged

def logo_predictions(df, features, xgb_params):
    y_true = np.full(len(df), -1, dtype=int)
    y_pred = np.full(len(df), -1, dtype=int)
    models = df["model_name"].values
    y = df["label"].values
    X = df[features].values if isinstance(features, list) else df[[features]].values
    for hold in MODELS:
        tr = models != hold
        te = models == hold
        clf = XGBClassifier(**xgb_params)
        clf.fit(X[tr], y[tr])
        pred = clf.predict(X[te])
        y_true[te] = y[te]
        y_pred[te] = pred
    assert (y_true >= 0).all()
    return y_true, y_pred

def bootstrap_f1(y_true, y_pred, n_boot=N_BOOT, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    scores = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        yt, yp = y_true[idx], y_pred[idx]
        if len(np.unique(yt)) < 3:
            continue
        scores.append(f1_score(yt, yp, average="macro"))
    arr = np.array(scores)
    return {"mean": float(np.mean(arr)),
            "ci_lo": float(np.percentile(arr, 2.5)),
            "ci_hi": float(np.percentile(arr, 97.5)),
            "n_valid": len(arr)}

def paired_bootstrap_test(y_true, y_pred_a, y_pred_b, n_boot=N_BOOT, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    diffs = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        yt = y_true[idx]
        if len(np.unique(yt)) < 3:
            continue
        f1_a = f1_score(yt, y_pred_a[idx], average="macro")
        f1_b = f1_score(yt, y_pred_b[idx], average="macro")
        diffs.append(f1_a - f1_b)
    arr = np.array(diffs)
    p_value = float(np.mean(arr <= 0))
    return {"mean_diff": float(np.mean(arr)),
            "ci_lo": float(np.percentile(arr, 2.5)),
            "ci_hi": float(np.percentile(arr, 97.5)),
            "p_value": p_value,
            "n_valid": len(arr)}

def main():
    print("Loading data...")
    df = load_data()
    print(f"  {len(df)} samples, {df['model_name'].nunique()} generators")

    xgb_7feat = dict(n_estimators=100, max_depth=5, learning_rate=0.1,
                     objective="multi:softmax", num_class=3,
                     eval_metric="mlogloss", verbosity=0, random_state=SEED)
    xgb_single = dict(n_estimators=100, max_depth=3, learning_rate=0.1,
                      objective="multi:softmax", num_class=3,
                      eval_metric="mlogloss", verbosity=0, random_state=SEED)

    print("")
    print("Running LOGO for 7-feature model...")
    yt_7, yp_7 = logo_predictions(df, FEAT_7, xgb_7feat)
    f1_7 = f1_score(yt_7, yp_7, average="macro")
    print(f"  LOGO macro-F1: {f1_7:.4f}")

    print("Running LOGO for avg_logprob...")
    yt_lp, yp_lp = logo_predictions(df, "log_likelihood", xgb_single)
    f1_lp = f1_score(yt_lp, yp_lp, average="macro")
    print(f"  LOGO macro-F1: {f1_lp:.4f}")

    print("Running LOGO for FastDetectGPT...")
    yt_fdg, yp_fdg = logo_predictions(df, "fast_detect_gpt", xgb_single)
    f1_fdg = f1_score(yt_fdg, yp_fdg, average="macro")
    print(f"  LOGO macro-F1: {f1_fdg:.4f}")

    print("")
    print(f"Bootstrap CI (n_boot={N_BOOT}, seed={SEED})...")
    ci_7 = bootstrap_f1(yt_7, yp_7)
    ci_lp = bootstrap_f1(yt_lp, yp_lp)
    ci_fdg = bootstrap_f1(yt_fdg, yp_fdg)

    print("")
    print("=" * 70)
    hdr = f"{'Model':<20} {'F1':>8} {'95% CI':>22}"
    print(hdr)
    print("-" * 55)
    print(f"{'7-feature':<20} {f1_7:>8.4f} [{ci_7['ci_lo']:.4f}, {ci_7['ci_hi']:.4f}]")
    print(f"{'Avg-LogProb':<20} {f1_lp:>8.4f} [{ci_lp['ci_lo']:.4f}, {ci_lp['ci_hi']:.4f}]")
    print(f"{'FastDetectGPT':<20} {f1_fdg:>8.4f} [{ci_fdg['ci_lo']:.4f}, {ci_fdg['ci_hi']:.4f}]")

    print("")
    print("Paired bootstrap tests...")
    pair_7_vs_lp = paired_bootstrap_test(yt_7, yp_7, yp_lp)
    pair_7_vs_fdg = paired_bootstrap_test(yt_7, yp_7, yp_fdg)
    best_single_name = "Avg-LogProb" if f1_lp >= f1_fdg else "FastDetectGPT"
    best_single_pred = yp_lp if f1_lp >= f1_fdg else yp_fdg
    pair_7_vs_best = paired_bootstrap_test(yt_7, yp_7, best_single_pred)

    print("")
    hdr2 = f"{'Comparison':<35} {'dF1':>8} {'95% CI':>22} {'p-value':>10}"
    print(hdr2)
    print("-" * 80)
    row1 = (f"{'7-feat vs Avg-LogProb':<35} {pair_7_vs_lp['mean_diff']:>+8.4f} "
            f"[{pair_7_vs_lp['ci_lo']:>+.4f}, {pair_7_vs_lp['ci_hi']:>+.4f}] "
            f"{pair_7_vs_lp['p_value']:>10.4f}")
    print(row1)
    row2 = (f"{'7-feat vs FastDetectGPT':<35} {pair_7_vs_fdg['mean_diff']:>+8.4f} "
            f"[{pair_7_vs_fdg['ci_lo']:>+.4f}, {pair_7_vs_fdg['ci_hi']:>+.4f}] "
            f"{pair_7_vs_fdg['p_value']:>10.4f}")
    print(row2)
    bname = f"7-feat vs best ({best_single_name})"
    row3 = (f"{bname:<35} {pair_7_vs_best['mean_diff']:>+8.4f} "
            f"[{pair_7_vs_best['ci_lo']:>+.4f}, {pair_7_vs_best['ci_hi']:>+.4f}] "
            f"{pair_7_vs_best['p_value']:>10.4f}")
    print(row3)

    sig_lp = "YES" if pair_7_vs_lp["p_value"] < 0.05 else "NO"
    sig_best = "YES" if pair_7_vs_best["p_value"] < 0.05 else "NO"
    print("")
    print(f"7-feat vs Avg-LogProb significant at a=0.05? {sig_lp} (p={pair_7_vs_lp['p_value']:.4f})")
    print(f"7-feat vs best single significant at a=0.05? {sig_best} (p={pair_7_vs_best['p_value']:.4f})")

    results = {
        "n_samples": len(df),
        "n_boot": N_BOOT,
        "seed": SEED,
        "models": {
            "seven_feature": {"logo_f1": round(f1_7, 4), "bootstrap_ci": ci_7},
            "avg_logprob": {"logo_f1": round(f1_lp, 4), "bootstrap_ci": ci_lp},
            "fastdetectgpt": {"logo_f1": round(f1_fdg, 4), "bootstrap_ci": ci_fdg},
        },
        "paired_tests": {
            "seven_feat_vs_avg_logprob": pair_7_vs_lp,
            "seven_feat_vs_fastdetectgpt": pair_7_vs_fdg,
            "seven_feat_vs_best_single": {
                "best_single": best_single_name,
                **pair_7_vs_best,
            },
        },
    }

    out_path = ROOT / "artifacts" / "plan-015" / "bootstrap_ci_results.txt"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved: {out_path}")
    return results

if __name__ == "__main__":
    main()

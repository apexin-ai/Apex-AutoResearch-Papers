"""Cross-seed transfer test: train RF on seed=42, test on seed=43 (and vice versa)."""

import json
import numpy as np
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

SEED42_PATH = "/root/autodl-tmp/recursive_gen_depth_est/data/features_all.jsonl"
SEED43_PATH = "/root/autodl-tmp/recursive_gen_depth_est/results/second_seed_replication/features.jsonl"
OUTPUT_DIR = Path("/root/autodl-tmp/recursive_gen_depth_est/results/cross_seed_transfer")

METADATA_COLS = {"depth", "sample_id"}
N_BOOTSTRAP = 1000
RF_PARAMS = dict(n_estimators=200, random_state=42)


def load_features(path):
    records = []
    with open(path) as f:
        for line in f:
            records.append(json.loads(line))
    feature_cols = sorted(k for k in records[0].keys() if k not in METADATA_COLS)
    X = np.array([[r[c] for c in feature_cols] for r in records])
    y = np.array([r["depth"] for r in records])
    return X, y, feature_cols


def bootstrap_ci(y_true, y_pred, n_bootstrap=N_BOOTSTRAP, seed=42):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    accs = []
    for _ in range(n_bootstrap):
        idx = rng.randint(0, n, size=n)
        accs.append(np.mean(y_true[idx] == y_pred[idx]))
    return np.percentile(accs, 2.5), np.percentile(accs, 97.5)


def main():
    print("Loading features...")
    X42, y42, cols42 = load_features(SEED42_PATH)
    X43, y43, cols43 = load_features(SEED43_PATH)

    assert cols42 == cols43, f"Feature columns differ: {set(cols42) ^ set(cols43)}"
    print(f"  seed=42: {X42.shape}, seed=43: {X43.shape}")
    print(f"  Features ({len(cols42)}): {cols42}")

    # Within-seed 5-fold CV
    print("\nWithin-seed 5-fold CV...")
    rf42 = RandomForestClassifier(**RF_PARAMS)
    cv42 = cross_val_score(rf42, X42, y42, cv=5, scoring="accuracy")
    print(f"  seed=42 CV: {cv42.mean():.4f} ± {cv42.std():.4f}")

    rf43 = RandomForestClassifier(**RF_PARAMS)
    cv43 = cross_val_score(rf43, X43, y43, cv=5, scoring="accuracy")
    print(f"  seed=43 CV: {cv43.mean():.4f} ± {cv43.std():.4f}")

    within_avg = (cv42.mean() + cv43.mean()) / 2

    # Cross-seed transfer: train on 42, test on 43
    print("\nCross-seed transfer...")
    rf_train42 = RandomForestClassifier(**RF_PARAMS)
    rf_train42.fit(X42, y42)
    pred_on_43 = rf_train42.predict(X43)
    acc_42_to_43 = np.mean(pred_on_43 == y43)
    ci_42_to_43 = bootstrap_ci(y43, pred_on_43)
    print(f"  train=42 → test=43: {acc_42_to_43:.4f} [{ci_42_to_43[0]:.4f}, {ci_42_to_43[1]:.4f}]")

    # Cross-seed transfer: train on 43, test on 42
    rf_train43 = RandomForestClassifier(**RF_PARAMS)
    rf_train43.fit(X43, y43)
    pred_on_42 = rf_train43.predict(X42)
    acc_43_to_42 = np.mean(pred_on_42 == y42)
    ci_43_to_42 = bootstrap_ci(y42, pred_on_42)
    print(f"  train=43 → test=42: {acc_43_to_42:.4f} [{ci_43_to_42[0]:.4f}, {ci_43_to_42[1]:.4f}]")

    cross_avg = (acc_42_to_43 + acc_43_to_42) / 2
    delta = cross_avg - within_avg

    print(f"\n--- Summary ---")
    print(f"  Within-seed avg:  {within_avg:.4f}")
    print(f"  Cross-seed avg:   {cross_avg:.4f}")
    print(f"  Delta:            {delta:+.4f}")
    print(f"  Hypothesis (cross >= 0.75): {'PASS' if cross_avg >= 0.75 else 'FAIL'}")

    # Save results
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    summary = {
        "within_seed_cv": {
            "seed42_mean": float(cv42.mean()),
            "seed42_std": float(cv42.std()),
            "seed42_folds": cv42.tolist(),
            "seed43_mean": float(cv43.mean()),
            "seed43_std": float(cv43.std()),
            "seed43_folds": cv43.tolist(),
            "average": float(within_avg),
        },
        "cross_seed_transfer": {
            "train42_test43": {
                "accuracy": float(acc_42_to_43),
                "ci_95_lower": float(ci_42_to_43[0]),
                "ci_95_upper": float(ci_42_to_43[1]),
            },
            "train43_test42": {
                "accuracy": float(acc_43_to_42),
                "ci_95_lower": float(ci_43_to_42[0]),
                "ci_95_upper": float(ci_43_to_42[1]),
            },
            "average": float(cross_avg),
        },
        "delta_cross_minus_within": float(delta),
        "hypothesis_pass": bool(cross_avg >= 0.75),
    }

    out_path = OUTPUT_DIR / "summary.json"
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()

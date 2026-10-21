"""
MLP baseline on 19 statistical features for recursive generation depth estimation.
Compares with RF baseline (78.2% 4-class accuracy).
"""
import json
import os
import time
import numpy as np
from pathlib import Path
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score
from sklearn.pipeline import Pipeline

DATA_PATH = "/root/autodl-tmp/recursive_gen_depth_est/data/features_all.jsonl"
OUT_DIR = "/root/autodl-tmp/recursive_gen_depth_est/results/mlp_baseline"
RF_BASELINE_ACC = 0.782

FEATURE_COLS = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio",
    "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

TOP5_FEATURES = [
    "mean_ppl", "var_ppl", "p90_ppl", "p75_ppl", "p50_ppl",
]

PAIRWISE_PAIRS = [(0, 1), (1, 2), (2, 3)]
PAIR_NAMES = ["d0v1", "d1v2", "d2v3"]


def load_data():
    records = []
    with open(DATA_PATH) as f:
        for line in f:
            records.append(json.loads(line))
    X = np.array([[r[c] for c in FEATURE_COLS] for r in records])
    y = np.array([r["depth"] for r in records])
    return X, y


def pairwise_auc(y_true, y_prob, pair):
    c0, c1 = pair
    mask = np.isin(y_true, [c0, c1])
    if mask.sum() == 0:
        return float("nan")
    yt = (y_true[mask] == c1).astype(int)
    yp = y_prob[mask, c1]
    return roc_auc_score(yt, yp)


def run_cv(make_pipeline_fn, X, y, n_splits=5, label=""):
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    fold_accs = []
    fold_recalls = []
    fold_aucs = {name: [] for name in PAIR_NAMES}
    all_preds = np.zeros(len(y), dtype=int)
    all_probs = np.zeros((len(y), 4))

    for fold_i, (train_idx, val_idx) in enumerate(skf.split(X, y)):
        X_tr, X_val = X[train_idx], X[val_idx]
        y_tr, y_val = y[train_idx], y[val_idx]

        pipe = make_pipeline_fn()
        pipe.fit(X_tr, y_tr)

        preds = pipe.predict(X_val)
        probs = pipe.predict_proba(X_val)

        all_preds[val_idx] = preds
        all_probs[val_idx] = probs

        acc = accuracy_score(y_val, preds)
        fold_accs.append(acc)

        rec = recall_score(y_val, preds, average=None, labels=[0, 1, 2, 3])
        fold_recalls.append(rec.tolist())

        for pair, name in zip(PAIRWISE_PAIRS, PAIR_NAMES):
            auc = pairwise_auc(y_val, probs, pair)
            fold_aucs[name].append(auc)

        print(f"  [{label}] Fold {fold_i+1}: acc={acc:.4f}, recall={rec}")

    mean_acc = np.mean(fold_accs)
    std_acc = np.std(fold_accs)
    ci95 = 1.96 * std_acc / np.sqrt(n_splits)

    overall_acc = accuracy_score(y, all_preds)
    overall_recall = recall_score(y, all_preds, average=None, labels=[0, 1, 2, 3])

    mean_aucs = {name: float(np.mean(vals)) for name, vals in fold_aucs.items()}

    result = {
        "label": label,
        "fold_accs": fold_accs,
        "mean_acc": float(mean_acc),
        "std_acc": float(std_acc),
        "ci95": float(ci95),
        "acc_range": f"{mean_acc:.4f} +/- {ci95:.4f}",
        "overall_acc": float(overall_acc),
        "per_class_recall": overall_recall.tolist(),
        "fold_recalls": fold_recalls,
        "pairwise_auc": mean_aucs,
        "delta_vs_rf": float(mean_acc - RF_BASELINE_ACC),
    }
    return result


def main():
    print("Loading data...")
    X, y = load_data()
    print(f"Data: {X.shape[0]} samples, {X.shape[1]} features, classes={np.unique(y)}")

    os.makedirs(OUT_DIR, exist_ok=True)
    results = {}

    # --- Variant 1: 2-layer MLP (128-128) ---
    print("\n=== Variant 1: MLP 128-128 ===")
    t0 = time.time()

    def make_mlp_128_128():
        return Pipeline([
            ("scaler", StandardScaler()),
            ("mlp", MLPClassifier(
                hidden_layer_sizes=(128, 128),
                activation="relu",
                solver="adam",
                learning_rate_init=1e-3,
                batch_size=256,
                max_iter=100,
                early_stopping=True,
                n_iter_no_change=10,
                validation_fraction=0.1,
                random_state=42,
            )),
        ])

    results["mlp_128_128"] = run_cv(make_mlp_128_128, X, y, label="MLP-128-128")
    results["mlp_128_128"]["time_sec"] = time.time() - t0

    # --- Variant 2: 3-layer MLP (64-128-64) ---
    print("\n=== Variant 2: MLP 64-128-64 ===")
    t0 = time.time()

    def make_mlp_64_128_64():
        return Pipeline([
            ("scaler", StandardScaler()),
            ("mlp", MLPClassifier(
                hidden_layer_sizes=(64, 128, 64),
                activation="relu",
                solver="adam",
                learning_rate_init=1e-3,
                batch_size=256,
                max_iter=100,
                early_stopping=True,
                n_iter_no_change=10,
                validation_fraction=0.1,
                random_state=42,
            )),
        ])

    results["mlp_64_128_64"] = run_cv(make_mlp_64_128_64, X, y, label="MLP-64-128-64")
    results["mlp_64_128_64"]["time_sec"] = time.time() - t0

    # --- Variant 3: MLP with polynomial features (degree=2 on top-5) ---
    print("\n=== Variant 3: MLP + Poly(deg=2) on top-5 features ===")
    t0 = time.time()

    top5_idx = [FEATURE_COLS.index(f) for f in TOP5_FEATURES]
    X_top5_poly = PolynomialFeatures(degree=2, include_bias=False).fit_transform(X[:, top5_idx])
    other_idx = [i for i in range(len(FEATURE_COLS)) if i not in top5_idx]
    X_poly = np.hstack([X, X_top5_poly[:, len(top5_idx):]])
    print(f"  Poly features: {X.shape[1]} original + {X_poly.shape[1] - X.shape[1]} interaction = {X_poly.shape[1]} total")

    def make_mlp_poly():
        return Pipeline([
            ("scaler", StandardScaler()),
            ("mlp", MLPClassifier(
                hidden_layer_sizes=(128, 128),
                activation="relu",
                solver="adam",
                learning_rate_init=1e-3,
                batch_size=256,
                max_iter=100,
                early_stopping=True,
                n_iter_no_change=10,
                validation_fraction=0.1,
                random_state=42,
            )),
        ])

    results["mlp_poly_top5"] = run_cv(make_mlp_poly, X_poly, y, label="MLP-Poly-Top5")
    results["mlp_poly_top5"]["time_sec"] = time.time() - t0
    results["mlp_poly_top5"]["n_features"] = int(X_poly.shape[1])

    # --- Summary ---
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"RF baseline (reference):    {RF_BASELINE_ACC:.4f}")
    for key, res in results.items():
        print(f"{res['label']:25s}: {res['mean_acc']:.4f} +/- {res['ci95']:.4f}  (delta={res['delta_vs_rf']:+.4f})")
        print(f"  Per-class recall: {[f'{r:.3f}' for r in res['per_class_recall']]}")
        print(f"  Pairwise AUC: {res['pairwise_auc']}")
        print(f"  Time: {res['time_sec']:.1f}s")

    summary = {
        "rf_baseline_acc": RF_BASELINE_ACC,
        "variants": results,
        "conclusion": "",
    }

    best_key = max(results, key=lambda k: results[k]["mean_acc"])
    best = results[best_key]
    delta = best["delta_vs_rf"]

    if abs(delta) <= 0.03:
        summary["conclusion"] = (
            f"Best MLP ({best['label']}) acc={best['mean_acc']:.4f}, "
            f"delta={delta:+.4f} vs RF. Within 3pp -> feature bottleneck confirmed."
        )
    elif delta > 0.03:
        summary["conclusion"] = (
            f"Best MLP ({best['label']}) acc={best['mean_acc']:.4f}, "
            f"delta={delta:+.4f} vs RF. MLP > RF by >3pp -> exploitable nonlinear combinations exist."
        )
    else:
        summary["conclusion"] = (
            f"Best MLP ({best['label']}) acc={best['mean_acc']:.4f}, "
            f"delta={delta:+.4f} vs RF. MLP < RF -> possible overfitting or suboptimal tuning."
        )

    print(f"\nConclusion: {summary['conclusion']}")

    out_path = os.path.join(OUT_DIR, "summary.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()

"""Plan-012 matched XGBoost baseline: 5-fold stratified CV on 4 generators.
Input:  data/features_{pythia-1b,olmo-2-1b,qwen3-0.6b,qwen3-1.7b}.csv
Output: results/plan012_xgboost_matched.json
"""
import json, time
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score, accuracy_score

ROOT = Path("/root/gen-depth-fingerprint")
DATA = ROOT / "data"
RESULTS = ROOT / "results"
SEED = 42
N_FOLDS = 5
N_BOOT = 2000

GENERATORS = ["pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b"]
FEAT_COLS = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
             "tail_decay", "ttr", "hapax_ratio"]


def load_data():
    dfs = []
    for gen in GENERATORS:
        df = pd.read_csv(DATA / f"features_{gen}.csv")
        dfs.append(df)
    df = pd.concat(dfs, ignore_index=True)
    print(f"Loaded {len(df)} samples from {len(GENERATORS)} generators")
    return df


def make_labels(depths, n_classes):
    if n_classes == 5:
        return np.clip(depths, 0, 4).astype(int)
    else:
        return np.clip(depths, 0, 2).astype(int)


def bootstrap_ci(y_true, y_pred, metric_fn, rng, n_boot=N_BOOT):
    n = len(y_true)
    vals = np.empty(n_boot)
    for b in range(n_boot):
        idx = rng.integers(0, n, size=n)
        vals[b] = metric_fn(y_true[idx], y_pred[idx])
    lo = float(np.percentile(vals, 2.5))
    hi = float(np.percentile(vals, 97.5))
    return round(lo, 4), round(hi, 4), round(float(np.std(vals)), 4)


def evaluate_cv(X, y, n_classes, rng):
    skf = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=SEED)
    all_preds = np.zeros(len(y), dtype=int)
    fold_results = []

    for fold_i, (train_idx, val_idx) in enumerate(skf.split(X, y)):
        clf = HistGradientBoostingClassifier(
            max_iter=200, max_depth=5, learning_rate=0.1,
            random_state=SEED, early_stopping=False
        )
        clf.fit(X[train_idx], y[train_idx])
        preds = clf.predict(X[val_idx])
        all_preds[val_idx] = preds

        mf1 = f1_score(y[val_idx], preds, average="macro")
        wf1 = f1_score(y[val_idx], preds, average="weighted")
        acc = accuracy_score(y[val_idx], preds)
        fold_results.append({
            "fold": fold_i, "n_train": len(train_idx), "n_val": len(val_idx),
            "macro_f1": round(mf1, 4), "weighted_f1": round(wf1, 4),
            "accuracy": round(acc, 4)
        })
        print(f"  Fold {fold_i}: macro_f1={mf1:.4f}  weighted_f1={wf1:.4f}  acc={acc:.4f}")

    macro_f1 = f1_score(y, all_preds, average="macro")
    weighted_f1 = f1_score(y, all_preds, average="weighted")
    acc = accuracy_score(y, all_preds)

    ci_macro = bootstrap_ci(y, all_preds, lambda yt, yp: f1_score(yt, yp, average="macro"), rng)
    ci_weighted = bootstrap_ci(y, all_preds, lambda yt, yp: f1_score(yt, yp, average="weighted"), rng)
    ci_acc = bootstrap_ci(y, all_preds, lambda yt, yp: accuracy_score(yt, yp), rng)

    fold_f1s = [f["macro_f1"] for f in fold_results]

    per_class = {}
    classes = sorted(set(y))
    for c in classes:
        mask = y == c
        pc_f1 = f1_score(y[mask] == c, all_preds[mask] == c, average="binary", zero_division=0)
        per_class[f"class_{c}"] = round(float(f1_score(
            (y == c).astype(int), (all_preds == c).astype(int), average="binary"
        )), 4)

    per_class_f1 = {}
    for c in classes:
        tp = np.sum((y == c) & (all_preds == c))
        fp = np.sum((y != c) & (all_preds == c))
        fn = np.sum((y == c) & (all_preds != c))
        prec = tp / (tp + fp) if (tp + fp) > 0 else 0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0
        f = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
        per_class_f1[f"class_{c}"] = round(f, 4)

    return {
        "macro_f1": round(macro_f1, 4),
        "macro_f1_std": round(float(np.std(fold_f1s)), 4),
        "macro_f1_ci95": [ci_macro[0], ci_macro[1]],
        "macro_f1_boot_std": ci_macro[2],
        "weighted_f1": round(weighted_f1, 4),
        "weighted_f1_ci95": [ci_weighted[0], ci_weighted[1]],
        "accuracy": round(acc, 4),
        "accuracy_ci95": [ci_acc[0], ci_acc[1]],
        "per_class_f1": per_class_f1,
        "fold_results": fold_results
    }


def main():
    t0 = time.time()
    rng = np.random.default_rng(SEED)

    df = load_data()
    X = df[FEAT_COLS].values

    # 5-class
    print("\n=== 5-class (depth 0-4) ===")
    y5 = make_labels(df["depth"].values, 5)
    print(f"Class distribution: {dict(zip(*np.unique(y5, return_counts=True)))}")
    res5 = evaluate_cv(X, y5, 5, rng)

    # 3-class
    print("\n=== 3-class (gen0/gen1/gen2+) ===")
    y3 = make_labels(df["depth"].values, 3)
    print(f"Class distribution: {dict(zip(*np.unique(y3, return_counts=True)))}")
    res3 = evaluate_cv(X, y3, 3, rng)

    # QLoRA results for comparison
    qlora_qwen = {"5class_macro_f1": 0.5828, "5class_std": 0.01,
                  "3class_macro_f1": 0.9052, "3class_std": 0.0032}
    qlora_pythia = {"5class_macro_f1": 0.5564, "5class_std": 0.0158,
                    "3class_macro_f1": 0.8703, "3class_std": 0.022}

    output = {
        "experiment": "plan-012-xgboost-matched",
        "method": "HGBT_7features_5fold_stratified",
        "evaluation_protocol": "5-fold stratified CV, 4 generators (pythia-1b, olmo-2-1b, qwen3-0.6b, qwen3-1.7b)",
        "matched_to": "plan-012 QLoRA evaluation protocol",
        "n_samples": len(df),
        "n_folds": N_FOLDS,
        "n_bootstrap": N_BOOT,
        "seed": SEED,
        "features": FEAT_COLS,
        "xgboost_5class": res5,
        "xgboost_3class": res3,
        "comparison": {
            "qlora_qwen06b_5class": qlora_qwen["5class_macro_f1"],
            "qlora_qwen06b_3class": qlora_qwen["3class_macro_f1"],
            "qlora_pythia410m_5class": qlora_pythia["5class_macro_f1"],
            "qlora_pythia410m_3class": qlora_pythia["3class_macro_f1"],
            "xgboost_matched_5class": res5["macro_f1"],
            "xgboost_matched_3class": res3["macro_f1"],
            "delta_qwen06b_vs_xgboost_5class": round(qlora_qwen["5class_macro_f1"] - res5["macro_f1"], 4),
            "delta_qwen06b_vs_xgboost_3class": round(qlora_qwen["3class_macro_f1"] - res3["macro_f1"], 4),
            "delta_pythia410m_vs_xgboost_5class": round(qlora_pythia["5class_macro_f1"] - res5["macro_f1"], 4),
            "delta_pythia410m_vs_xgboost_3class": round(qlora_pythia["3class_macro_f1"] - res3["macro_f1"], 4),
        },
        "runtime_seconds": round(time.time() - t0, 1)
    }

    out_path = RESULTS / "plan012_xgboost_matched.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")
    print(f"Runtime: {time.time() - t0:.1f}s")

    print(f"\n=== Summary ===")
    print(f"XGBoost-matched 5-class: macro_f1={res5['macro_f1']} CI={res5['macro_f1_ci95']}")
    print(f"XGBoost-matched 3-class: macro_f1={res3['macro_f1']} CI={res3['macro_f1_ci95']}")
    print(f"QLoRA Qwen3-0.6B:  5class={qlora_qwen['5class_macro_f1']}  3class={qlora_qwen['3class_macro_f1']}")
    print(f"QLoRA Pythia-410M: 5class={qlora_pythia['5class_macro_f1']}  3class={qlora_pythia['3class_macro_f1']}")
    print(f"Delta (Qwen-XGB):  5class={output['comparison']['delta_qwen06b_vs_xgboost_5class']:+.4f}  3class={output['comparison']['delta_qwen06b_vs_xgboost_3class']:+.4f}")
    print(f"Delta (Pythia-XGB): 5class={output['comparison']['delta_pythia410m_vs_xgboost_5class']:+.4f}  3class={output['comparison']['delta_pythia410m_vs_xgboost_3class']:+.4f}")


if __name__ == "__main__":
    main()

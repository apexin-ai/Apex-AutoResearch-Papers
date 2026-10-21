"""
N3 rebuttal: fold-level std + paired bootstrap significance test.

Part A: 9-cell RF 5-fold CV with per-fold accuracy & adjacent pairwise AUC.
Part B: Bootstrap significance test (RF vs known baselines) on Pythia nucleus.
"""

import json
import os
import numpy as np
from collections import Counter
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, roc_auc_score

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

CELLS = {
    "pythia_nucleus095": "data/features_all.jsonl",
    "pythia_temp09":     "data/pythia_temp09/features.jsonl",
    "pythia_topk50":     "results/pythia_topk50/features.jsonl",
    "gpt2xl_nucleus095": "data/gpt2xl/features.jsonl",
    "gpt2xl_temp09":     "results/gpt2xl_temp09/features.jsonl",
    "gpt2xl_topk50":     "results/gpt2xl_topk50/features.jsonl",
    "olmo_nucleus095":   "data/olmo/features.jsonl",
    "olmo_temp09":       "results/olmo_temp09/features.jsonl",
    "olmo_topk50":       "results/olmo_topk50/features.jsonl",
}

BASELINE_ACCS = {
    "CORAL":  0.7807,
    "DivEye": 0.7817,
    "CE-MLP": 0.749,
}


def load_features(path):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)
    y = np.array([r["depth"] for r in records], dtype=np.int64)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    X = np.clip(X, -3.4e38, 3.4e38)
    return X, y


def pairwise_auc(y_true, y_prob, d1, d2):
    mask = np.isin(y_true, [d1, d2])
    if mask.sum() < 2:
        return None
    yt = (y_true[mask] == d2).astype(int)
    if len(np.unique(yt)) < 2:
        return None
    yp = y_prob[mask, d2]
    return float(roc_auc_score(yt, yp))


def run_fold_cv(X, y, cell_name):
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    fold_accs = []
    fold_aucs = {"d0v1": [], "d1v2": [], "d2v3": []}
    all_y_true = np.zeros(len(y), dtype=np.int64)
    all_y_pred = np.zeros(len(y), dtype=np.int64)
    all_y_prob = np.zeros((len(y), 4), dtype=np.float64)
    fold_indices = np.zeros(len(y), dtype=np.int64)

    for fold_i, (train_idx, test_idx) in enumerate(skf.split(X, y)):
        rf = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
        rf.fit(X[train_idx], y[train_idx])
        y_pred = rf.predict(X[test_idx])
        y_prob = rf.predict_proba(X[test_idx])

        prob_full = np.zeros((len(test_idx), 4))
        for ci, c in enumerate(rf.classes_):
            prob_full[:, c] = y_prob[:, ci]

        acc = accuracy_score(y[test_idx], y_pred)
        fold_accs.append(round(acc, 4))

        for d1, d2, key in [(0, 1, "d0v1"), (1, 2, "d1v2"), (2, 3, "d2v3")]:
            auc_val = pairwise_auc(y[test_idx], prob_full, d1, d2)
            fold_aucs[key].append(round(auc_val, 4) if auc_val is not None else None)

        all_y_true[test_idx] = y[test_idx]
        all_y_pred[test_idx] = y_pred
        all_y_prob[test_idx] = prob_full
        fold_indices[test_idx] = fold_i

    mean_acc = round(float(np.mean(fold_accs)), 4)
    std_acc = round(float(np.std(fold_accs)), 4)

    mean_aucs = {}
    for key in fold_aucs:
        vals = [v for v in fold_aucs[key] if v is not None]
        if vals:
            mean_aucs[key] = {
                "mean": round(float(np.mean(vals)), 4),
                "std": round(float(np.std(vals)), 4),
            }

    print(f"  {cell_name}: acc={mean_acc}±{std_acc}  folds={fold_accs}")
    for key, v in mean_aucs.items():
        print(f"    {key}: {v['mean']}±{v['std']}")

    return {
        "mean_acc": mean_acc,
        "std_acc": std_acc,
        "fold_accs": fold_accs,
        "fold_aucs": fold_aucs,
        "mean_aucs": mean_aucs,
        "all_y_true": all_y_true,
        "all_y_pred": all_y_pred,
        "fold_indices": fold_indices,
    }


def bootstrap_significance(y_true, y_pred, baseline_acc, n_boot=1000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    rf_accs = np.zeros(n_boot)
    for b in range(n_boot):
        idx = rng.choice(n, n, replace=True)
        rf_accs[b] = accuracy_score(y_true[idx], y_pred[idx])

    diffs = rf_accs - baseline_acc
    p_value = float(np.mean(diffs <= 0)) * 2  # two-tailed
    p_value = min(p_value, 2.0 - p_value)  # ensure valid two-tailed
    ci_lo = float(np.percentile(diffs, 2.5))
    ci_hi = float(np.percentile(diffs, 97.5))
    mean_diff = float(np.mean(diffs))

    return {
        "rf_mean_acc": round(float(np.mean(rf_accs)), 4),
        "rf_std_acc": round(float(np.std(rf_accs)), 4),
        "baseline_acc": baseline_acc,
        "mean_diff": round(mean_diff, 4),
        "ci_95": [round(ci_lo, 4), round(ci_hi, 4)],
        "p_value": round(p_value, 4),
        "n_bootstrap": n_boot,
    }


def main():
    os.makedirs("results", exist_ok=True)

    # === Part A: 9-cell fold-level metrics ===
    print("=" * 60)
    print("Part A: 9-cell RF 5-fold CV")
    print("=" * 60)

    cell_results = {}
    pythia_data = None

    for cell_name, path in CELLS.items():
        if not os.path.exists(path):
            print(f"  SKIP {cell_name}: {path} not found")
            continue
        X, y = load_features(path)
        print(f"  [{cell_name}] {X.shape[0]} samples, depths={dict(Counter(y))}")
        result = run_fold_cv(X, y, cell_name)

        cell_results[cell_name] = {
            "mean_acc": result["mean_acc"],
            "std_acc": result["std_acc"],
            "fold_accs": result["fold_accs"],
            "fold_aucs": result["fold_aucs"],
            "mean_aucs": result["mean_aucs"],
            "n_samples": int(X.shape[0]),
        }

        if cell_name == "pythia_nucleus095":
            pythia_data = result

    with open("results/n3_fold_metrics.json", "w") as f:
        json.dump(cell_results, f, indent=2)
    print(f"\nSaved: results/n3_fold_metrics.json ({len(cell_results)} cells)")

    # === Part B: Bootstrap significance test ===
    print("\n" + "=" * 60)
    print("Part B: Bootstrap significance (RF vs baselines, Pythia nucleus)")
    print("=" * 60)

    if pythia_data is None:
        print("ERROR: Pythia nucleus data not available")
        return

    y_true = pythia_data["all_y_true"]
    y_pred = pythia_data["all_y_pred"]

    sig_results = {}
    for method, baseline_acc in BASELINE_ACCS.items():
        result = bootstrap_significance(y_true, y_pred, baseline_acc)
        sig_results[f"RF_vs_{method}"] = result
        sig = "***" if result["p_value"] < 0.001 else "**" if result["p_value"] < 0.01 else "*" if result["p_value"] < 0.05 else "ns"
        print(f"  RF vs {method}: diff={result['mean_diff']:+.4f}, "
              f"95%CI=[{result['ci_95'][0]:+.4f}, {result['ci_95'][1]:+.4f}], "
              f"p={result['p_value']:.4f} {sig}")

    with open("results/n3_bootstrap_significance.json", "w") as f:
        json.dump(sig_results, f, indent=2)
    print(f"\nSaved: results/n3_bootstrap_significance.json")


if __name__ == "__main__":
    main()

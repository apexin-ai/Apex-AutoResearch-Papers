"""
Evaluate d1-d3 only (excluding depth-0) with full and filtered subsets.
Uses identical RF parameters as MVP: n_estimators=100, random_state=42,
StandardScaler, test_size=0.2.
"""
import json
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, roc_auc_score, mean_absolute_error)

SEED = 42
TEST_SIZE = 0.2


def load_features(path, exclude_depth0=True):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            if exclude_depth0 and r["depth"] == 0:
                continue
            records.append(r)
    exclude_keys = {"depth", "sample_id"}
    feature_names = [k for k in records[0].keys() if k not in exclude_keys]
    X = np.array([[r[k] for k in feature_names] for r in records], dtype=np.float64)
    y = np.array([r["depth"] for r in records], dtype=np.int64)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    return X, y, feature_names


def pairwise_auc(y_true, y_prob, d1, d2, labels):
    mask = np.isin(y_true, [d1, d2])
    if mask.sum() < 2:
        return None
    yt = (y_true[mask] == d2).astype(int)
    if len(np.unique(yt)) < 2:
        return None
    d2_idx = list(labels).index(d2)
    yp = y_prob[mask, d2_idx]
    return float(roc_auc_score(yt, yp))


def bootstrap_ci(y_true, y_pred, metric_fn, n_boot=1000, seed=42, ci=0.95):
    rng = np.random.RandomState(seed)
    scores = []
    n = len(y_true)
    for _ in range(n_boot):
        idx = rng.choice(n, n, replace=True)
        try:
            scores.append(metric_fn(y_true[idx], y_pred[idx]))
        except Exception:
            continue
    alpha = (1 - ci) / 2
    return float(np.percentile(scores, alpha * 100)), float(np.percentile(scores, (1 - alpha) * 100))


def evaluate_subset(X, y, feature_names, label):
    labels = sorted(np.unique(y).tolist())
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=SEED, stratify=y)

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    rf = RandomForestClassifier(n_estimators=100, random_state=SEED)
    rf.fit(X_train_s, y_train)
    y_pred = rf.predict(X_test_s)
    y_prob = rf.predict_proba(X_test_s)
    # align proba columns
    if not np.array_equal(rf.classes_, labels):
        aligned = np.zeros((y_prob.shape[0], len(labels)))
        for i, c in enumerate(rf.classes_):
            aligned[:, labels.index(c)] = y_prob[:, i]
        y_prob = aligned

    acc = accuracy_score(y_test, y_pred)
    ci_lo, ci_hi = bootstrap_ci(y_test, y_pred, accuracy_score, seed=SEED)
    mae = mean_absolute_error(y_test, y_pred)

    cm = confusion_matrix(y_test, y_pred, labels=labels)
    report = classification_report(y_test, y_pred,
                                   target_names=[f"d{d}" for d in labels],
                                   output_dict=True, zero_division=0)

    recalls = {f"d{d}": report[f"d{d}"]["recall"] for d in labels}
    precisions = {f"d{d}": report[f"d{d}"]["precision"] for d in labels}
    f1s = {f"d{d}": report[f"d{d}"]["f1-score"] for d in labels}

    pair_aucs = {}
    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            d1, d2 = labels[i], labels[j]
            auc = pairwise_auc(y_test, y_prob, d1, d2, labels)
            pair_aucs[f"d{d1}v{d2}"] = round(auc, 4) if auc is not None else None

    fi = dict(zip(feature_names, rf.feature_importances_.tolist()))
    fi_sorted = sorted(fi.items(), key=lambda x: -x[1])[:5]

    n_total = len(y)
    n_test = len(y_test)
    depth_counts = Counter(y.tolist())

    print(f"\n{'=' * 55}")
    print(f"=== {label} (N={n_total}, test={n_test}) ===")
    print(f"{'=' * 55}")
    print(f"Sample counts: " + ", ".join(f"d{d}={depth_counts[d]}" for d in labels))
    print(f"3-class acc: {acc:.4f} [95% CI: {ci_lo:.4f}, {ci_hi:.4f}]")
    print(f"MAE: {mae:.4f}")
    print(f"Per-class recall:    d1={recalls['d1']:.3f}, d2={recalls['d2']:.3f}, d3={recalls['d3']:.3f}")
    print(f"Per-class precision: d1={precisions['d1']:.3f}, d2={precisions['d2']:.3f}, d3={precisions['d3']:.3f}")
    print(f"Per-class F1:        d1={f1s['d1']:.3f}, d2={f1s['d2']:.3f}, d3={f1s['d3']:.3f}")
    auc_str = ", ".join(f"{k}: {v}" for k, v in pair_aucs.items())
    print(f"Pairwise AUC: {auc_str}")
    print(f"\nConfusion matrix:")
    print(f"{'':>8} pred_d1  pred_d2  pred_d3")
    for i, d in enumerate(labels):
        row = "  ".join(f"{cm[i, j]:>6}" for j in range(len(labels)))
        print(f"d{d:>1}    {row}")
    print(f"\nTop-5 features: {[f'{name} ({imp:.4f})' for name, imp in fi_sorted]}")


def main():
    base = "/root/autodl-tmp/recursive_gen_depth_est/data"

    X_full, y_full, fn_full = load_features(f"{base}/features_3class.jsonl", exclude_depth0=False)
    evaluate_subset(X_full, y_full, fn_full, "FULL d1-d3")

    X_filt, y_filt, fn_filt = load_features(f"{base}/features_filtered.jsonl", exclude_depth0=True)
    evaluate_subset(X_filt, y_filt, fn_filt, "FILTERED d1-d3 (code/HTML removed)")


if __name__ == "__main__":
    main()

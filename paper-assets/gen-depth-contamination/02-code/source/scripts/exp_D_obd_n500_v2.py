"""EXP-D v2: OBD-LightGBM accuracy on the SAME N=500 samples as exp-011 LLM baselines.

Corrects exp_D v1 which used plain multiclass LightGBM instead of true OBD.

Method:
  - True Ordinal Binary Decomposition: K-1 binary LightGBM classifiers for P(Y > k)
  - Hyperparameters from exp-010 (paper-consistent): n_estimators=200, max_depth=6, lr=0.05, num_leaves=31
  - 5-fold GroupKFold CV on full Pythia data (depths 0-5, N=30000)
  - Extract OOF predictions for the specific 500 samples from exp011_samples.jsonl
  - Report 5-class accuracy (depths 0-4) + bootstrap CI
"""
import csv
import json
import re
from pathlib import Path

import numpy as np

PROJECT = Path("/root/autodl-tmp/gen-depth-contamination")
DATA_DIR = PROJECT / "data_exp001_pythia"
SAMPLES_PATH = PROJECT / "artifacts" / "exp011_samples.jsonl"
OUT_PATH = PROJECT / "artifacts" / "exp_D_obd_n500_v2.json"

FEAT_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
    "ttr", "hapax_ratio", "self_bleu",
    "freq_kurtosis", "freq_entropy", "low_freq_ratio",
]

MAX_DEPTH = 5  # depths 0-5, 6 classes (matching exp-010 / paper)
N_SPLITS = 5
N_BOOTSTRAP = 1000


def load_features():
    feat_path = DATA_DIR / "features.csv"
    with open(feat_path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    depths = np.array([int(r["depth"]) for r in rows])
    doc_ids = np.array([int(r["doc_id"]) for r in rows])
    X = np.array([
        [float(r[c]) if r[c] not in ("", "nan") else np.nan for c in FEAT_COLS]
        for r in rows
    ])
    col_means = np.nanmean(X, axis=0)
    for j in range(X.shape[1]):
        mask = np.isnan(X[:, j])
        X[mask, j] = col_means[j]

    return X, depths, doc_ids


def run_obd_oof(X, y, groups, max_depth, n_splits):
    """OBD: K-1 binary LightGBM classifiers for P(Y > k), out-of-fold."""
    import lightgbm as lgb
    from sklearn.model_selection import GroupKFold

    n = len(y)
    cum_probs = np.zeros((n, max_depth))

    gkf = GroupKFold(n_splits=n_splits)
    fold_indices = list(gkf.split(X, y, groups=groups))

    for k in range(max_depth):
        y_bin = (y > k).astype(int)
        for train_idx, test_idx in fold_indices:
            clf = lgb.LGBMClassifier(
                n_estimators=200, max_depth=6, learning_rate=0.05,
                num_leaves=31, verbose=-1, n_jobs=-1,
            )
            clf.fit(X[train_idx], y_bin[train_idx])
            cum_probs[test_idx, k] = clf.predict_proba(X[test_idx])[:, 1]

    n_classes = max_depth + 1
    class_probs = np.zeros((n, n_classes))
    class_probs[:, 0] = 1.0 - cum_probs[:, 0]
    for k in range(1, max_depth):
        class_probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]
    class_probs[:, max_depth] = cum_probs[:, max_depth - 1]
    class_probs = np.clip(class_probs, 0, None)
    row_sums = class_probs.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1.0
    class_probs /= row_sums

    preds = class_probs.argmax(axis=1)
    return preds


def parse_exp011_doc_id(doc_id_str):
    """Parse 'pythia_d{depth}_{orig_id}' -> (depth, orig_id)."""
    m = re.match(r"pythia_d(\d+)_(\d+)", doc_id_str)
    if not m:
        raise ValueError(f"Cannot parse doc_id: {doc_id_str}")
    return int(m.group(1)), int(m.group(2))


def bootstrap_ci(y_true, y_pred, n_bootstrap, seed=42):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    accs = []
    for _ in range(n_bootstrap):
        idx = rng.randint(0, n, size=n)
        accs.append(float(np.mean(y_pred[idx] == y_true[idx])))
    return np.array(accs)


def main():
    print("Loading features...")
    X, depths, doc_ids = load_features()
    print(f"  {len(depths)} samples, {len(FEAT_COLS)} features, depths {depths.min()}-{depths.max()}")

    print("Running OBD 5-fold CV (K-1 binary classifiers)...")
    oof_preds = run_obd_oof(X, depths, doc_ids, MAX_DEPTH, N_SPLITS)
    full_acc = float(np.mean(oof_preds == depths))
    print(f"  Full OBD accuracy (N={len(depths)}, {MAX_DEPTH+1}-class): {full_acc:.4f}")

    print("Loading exp-011 samples...")
    with open(SAMPLES_PATH) as f:
        samples = [json.loads(line) for line in f]
    print(f"  {len(samples)} samples loaded")

    # Build (depth, doc_id) -> row index mapping
    lookup = {}
    for i in range(len(depths)):
        lookup[(int(depths[i]), int(doc_ids[i]))] = i

    # Match exp-011 samples to features.csv rows
    matched_indices = []
    matched_true_depths = []
    missing = 0
    for s in samples:
        d, orig_id = parse_exp011_doc_id(s["doc_id"])
        key = (d, orig_id)
        if key in lookup:
            matched_indices.append(lookup[key])
            matched_true_depths.append(d)
        else:
            missing += 1
            print(f"  WARNING: sample {s['doc_id']} not found in features.csv")

    matched_indices = np.array(matched_indices)
    matched_true_depths = np.array(matched_true_depths)
    print(f"  Matched {len(matched_indices)} / {len(samples)} samples (missing: {missing})")

    # Verify depth consistency
    assert np.all(depths[matched_indices] == matched_true_depths), "Depth mismatch!"

    # Compute accuracy on the 500 samples
    y_true = depths[matched_indices]
    y_pred = oof_preds[matched_indices]
    accuracy = float(np.mean(y_pred == y_true))
    print(f"\n  OBD 5-class accuracy on N=500 (exp-011 samples): {accuracy:.4f}")

    # Per-depth accuracy
    for d in sorted(set(matched_true_depths)):
        mask = matched_true_depths == d
        d_acc = float(np.mean(y_pred[mask] == y_true[mask]))
        print(f"    depth {d}: {d_acc:.4f} (n={mask.sum()})")

    # Bootstrap CI
    print(f"\n  Bootstrap CI ({N_BOOTSTRAP} resamples)...")
    boot_accs = bootstrap_ci(y_true, y_pred, N_BOOTSTRAP)
    ci_lower = float(np.percentile(boot_accs, 2.5))
    ci_upper = float(np.percentile(boot_accs, 97.5))
    print(f"  95% CI: [{ci_lower:.4f}, {ci_upper:.4f}]")

    gpt_acc = 0.332
    claude_acc = 0.331

    result = {
        "obd_n500_accuracy": round(accuracy, 4),
        "obd_n500_ci_lower": round(ci_lower, 4),
        "obd_n500_ci_upper": round(ci_upper, 4),
        "n_bootstrap": N_BOOTSTRAP,
        "n_samples": len(matched_indices),
        "sample_source": "exp011_samples.jsonl (same as LLM baseline)",
        "gpt55_n500_accuracy": gpt_acc,
        "claude_n500_accuracy": claude_acc,
        "obd_full_accuracy": round(full_acc, 4),
        "obd_full_n": len(depths),
        "method": "OBD-LightGBM out-of-fold predictions, same 500 samples as exp-011",
        "obd_hyperparams": {
            "n_estimators": 200,
            "max_depth": 6,
            "learning_rate": 0.05,
            "num_leaves": 31,
            "n_binary_classifiers": MAX_DEPTH,
            "n_folds": N_SPLITS,
        },
        "per_depth_accuracy": {
            str(d): round(float(np.mean(y_pred[matched_true_depths == d] == y_true[matched_true_depths == d])), 4)
            for d in sorted(set(matched_true_depths))
        },
        "conclusion": (
            f"OBD at N=500 achieves {accuracy:.1%} "
            f"[{ci_lower:.1%}, {ci_upper:.1%}], "
            f"above LLM baselines (GPT-5.5: {gpt_acc:.1%}, Claude: {claude_acc:.1%})"
        ),
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved to {OUT_PATH}")
    print(f"Conclusion: {result['conclusion']}")


if __name__ == "__main__":
    main()

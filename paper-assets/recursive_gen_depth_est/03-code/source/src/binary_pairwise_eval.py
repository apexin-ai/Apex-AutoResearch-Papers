# Binary pairwise RF evaluation for d3v4 and d4v5.
# Dedicated binary classifiers to replace 6-class pairwise AUC
# (which suffers from decision boundary dilution).
# Also runs d1v2 and d2v3 as sanity checks (should match 4-class pipeline).

import json, sys
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score, precision_score, recall_score
from pathlib import Path

BASE = Path("/root/autodl-tmp/recursive_gen_depth_est")

FEATURE_COLS = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio",
    "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]


def load_features(path):
    X, y = [], []
    with open(path) as f:
        for line in f:
            rec = json.loads(line)
            feats = [rec[c] for c in FEATURE_COLS]
            if not any(np.isnan(feats) | np.isinf(feats)):
                X.append(feats)
                y.append(rec["depth"])
    return np.array(X), np.array(y)


def find_and_load_all_features():
    """Search for features files covering depths 0-5."""
    candidates = [
        BASE / "results" / "depth_extension" / "features_all.jsonl",
        BASE / "results" / "depth_extension" / "features_6class.jsonl",
        BASE / "data" / "features_all_6class.jsonl",
    ]
    for c in candidates:
        if c.exists():
            print(f"Found combined features: {c}")
            return load_features(c)

    # Fallback: combine original d0-d3 + extension d4-d5
    print("No combined file found, assembling from individual sources...")
    X_all, y_all = [], []

    # d0-d3 from original pipeline
    orig = BASE / "data" / "features_all.jsonl"
    if orig.exists():
        X, y = load_features(orig)
        print(f"  Original features_all.jsonl: {len(X)} samples, depths {np.unique(y)}")
        X_all.append(X)
        y_all.append(y)

    # d4, d5 from depth extension
    for d in [4, 5]:
        for pattern in [
            BASE / "results" / "depth_extension" / f"features_depth_{d}.jsonl",
            BASE / "results" / "depth_extension" / f"depth_{d}_features.jsonl",
            BASE / "data" / f"features_depth_{d}.jsonl",
            BASE / "data" / f"depth_{d}_features.jsonl",
        ]:
            if pattern.exists():
                X, y = load_features(pattern)
                print(f"  Depth {d}: {len(X)} samples from {pattern}")
                X_all.append(X)
                y_all.append(y)
                break
        else:
            print(f"  WARNING: No features found for depth {d}")

    if not X_all:
        return np.array([]), np.array([])
    return np.vstack(X_all), np.concatenate(y_all)


def binary_rf_eval(X, y, d_low, d_high, seed=42, n_bootstrap=1000):
    mask = np.isin(y, [d_low, d_high])
    Xb = X[mask]
    yb = (y[mask] == d_high).astype(int)

    print(f"\n{'='*50}")
    print(f"Binary d{d_low}v{d_high}: {len(yb)} samples "
          f"(class0={np.sum(yb==0)}, class1={np.sum(yb==1)})")

    X_tr, X_te, y_tr, y_te = train_test_split(
        Xb, yb, test_size=0.2, stratify=yb, random_state=seed
    )
    rf = RandomForestClassifier(n_estimators=500, random_state=seed, n_jobs=-1)
    rf.fit(X_tr, y_tr)

    y_prob = rf.predict_proba(X_te)[:, 1]
    y_pred = rf.predict(X_te)
    auc = roc_auc_score(y_te, y_prob)
    acc = accuracy_score(y_te, y_pred)
    prec = precision_score(y_te, y_pred)
    rec = recall_score(y_te, y_pred)

    rng = np.random.RandomState(seed)
    aucs = []
    for _ in range(n_bootstrap):
        idx = rng.choice(len(y_te), len(y_te), replace=True)
        if len(np.unique(y_te[idx])) == 2:
            aucs.append(roc_auc_score(y_te[idx], y_prob[idx]))
    ci_lo, ci_hi = np.percentile(aucs, [2.5, 97.5])

    fi = rf.feature_importances_
    top5_idx = np.argsort(fi)[::-1][:5]
    top5 = [(FEATURE_COLS[i], round(float(fi[i]), 4)) for i in top5_idx]

    result = {
        "pair": f"d{d_low}v{d_high}",
        "auc": round(float(auc), 4),
        "auc_ci95": [round(float(ci_lo), 4), round(float(ci_hi), 4)],
        "accuracy": round(float(acc), 4),
        "precision": round(float(prec), 4),
        "recall": round(float(rec), 4),
        "n_train": int(len(y_tr)),
        "n_test": int(len(y_te)),
        "top5_features": top5,
    }

    print(f"  AUC:  {auc:.4f} [{ci_lo:.4f}, {ci_hi:.4f}]")
    print(f"  Acc:  {acc:.4f}  Prec: {prec:.4f}  Rec: {rec:.4f}")
    print(f"  Top5: {top5}")
    return result


def main():
    X, y = find_and_load_all_features()
    if len(X) == 0:
        print("ERROR: No features loaded.")
        print("Listing potential directories:")
        for d in ["results/depth_extension", "data", "results"]:
            p = BASE / d
            if p.exists():
                files = list(p.glob("*.jsonl"))
                print(f"  {p}: {[f.name for f in files]}")
        sys.exit(1)

    depths_found = dict(zip(*np.unique(y, return_counts=True)))
    print(f"\nTotal: {len(X)} samples, depths: {depths_found}")

    # Run binary RF for d1v2, d2v3 (sanity check) + d3v4, d4v5 (target)
    results = {}
    for d_low, d_high in [(1, 2), (2, 3), (3, 4), (4, 5)]:
        if d_low in depths_found and d_high in depths_found:
            results[f"d{d_low}v{d_high}"] = binary_rf_eval(X, y, d_low, d_high)
        else:
            print(f"\nWARNING: Skipping d{d_low}v{d_high} — depth not in data")

    # EDD determination
    d3v4_auc = results.get("d3v4", {}).get("auc", 0)
    d4v5_auc = results.get("d4v5", {}).get("auc", 0)
    if d3v4_auc > 0.75 and d4v5_auc > 0.75:
        edd = ">=5"
    elif d3v4_auc > 0.75:
        edd = "4"
    else:
        edd = "3"

    print(f"\n{'='*50}")
    print(f"EDD DETERMINATION: d3v4={d3v4_auc:.4f}, d4v5={d4v5_auc:.4f} → EDD {edd}")

    # Reference: 4-class pipeline pairwise AUC (Pythia nucleus)
    ref = {"d0v1": 0.9975, "d1v2": 0.8607, "d2v3": 0.8005}
    print(f"\nSanity check vs 4-class pipeline:")
    for pair in ["d1v2", "d2v3"]:
        if pair in results:
            delta = results[pair]["auc"] - ref[pair]
            print(f"  {pair}: binary={results[pair]['auc']:.4f} vs 4-class={ref[pair]:.4f} (Δ={delta:+.4f})")

    # Save
    out_dir = BASE / "results" / "binary_pairwise"
    out_dir.mkdir(parents=True, exist_ok=True)
    output = {
        "pairs": results,
        "edd_determination": edd,
        "threshold": 0.75,
        "reference_4class": ref,
    }
    out_path = out_dir / "binary_pairwise_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()

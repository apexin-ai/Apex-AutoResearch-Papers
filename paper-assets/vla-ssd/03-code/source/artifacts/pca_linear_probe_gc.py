"""PCA + Linear Probe Goal Classification for VLA/DINO features.

Input:  Per-task .h5 files with per-demo hidden states
        VLA: demo_{i}/{feature_key} shape (T, 33, 4096)
        DINO: traj_{i}/{feature_key} shape (T, 1024)
Output: JSON with per-layer accuracy, per-timestep accuracy, selectivity index

Dependencies: numpy, h5py, sklearn (all pre-installed)
"""
# --- Path configuration (set env vars to override defaults) ---
import os as _os
PROJECT_ROOT = _os.environ.get("VLA_SSD_ROOT", ".")
LIBERO_ROOT = _os.environ.get("LIBERO_ROOT", "./LIBERO")
# ---

import argparse
import json
import os
import glob
import sys
from collections import defaultdict
from pathlib import Path

import h5py
import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score


# ============================================================
# Feature scanning & loading
# ============================================================

def scan_features(features_dir, feature_key):
    """Scan H5 files, return per-demo metadata + dimensions.

    Returns:
        demos: list of dicts with task, h5_path, h5_key, T, is_3d
        n_layers: int (33 for VLA, 1 for DINO)
        hidden_dim: int (4096 for VLA, 1024 for DINO)
    """
    demos = []
    n_layers = hidden_dim = None

    for h5_path in sorted(glob.glob(os.path.join(features_dir, "*.h5"))):
        task = Path(h5_path).stem
        with h5py.File(h5_path, "r") as f:
            # Sort keys numerically (demo_0, demo_1, ... or traj_0, traj_1, ...)
            keys = sorted(f.keys(), key=lambda x: int(x.split("_")[-1]))
            for hk in keys:
                if feature_key not in f[hk]:
                    available = list(f[hk].keys())
                    raise KeyError(
                        f"Key '{feature_key}' not in {h5_path}/{hk}. "
                        f"Available: {available}"
                    )
                shape = f[hk][feature_key].shape
                is_3d = len(shape) == 3  # (T, n_layers, dim) vs (T, dim)
                T = shape[0]
                if n_layers is None:
                    n_layers = shape[1] if is_3d else 1
                    hidden_dim = shape[-1]

                demos.append(dict(
                    task=task, h5_path=h5_path, h5_key=hk,
                    feature_key=feature_key, T=T, is_3d=is_3d,
                ))

    if not demos:
        raise FileNotFoundError(f"No .h5 files in {features_dir}")
    return demos, n_layers, hidden_dim


def split_by_task(demos, train_ratio=0.8):
    """80/20 split per task by demo order (first 80% train, rest val)."""
    by_task = defaultdict(list)
    for i, m in enumerate(demos):
        by_task[m["task"]].append(i)

    train_ids, val_ids = [], []
    for task in sorted(by_task):
        ids = by_task[task]
        n_train = int(len(ids) * train_ratio)
        train_ids.extend(ids[:n_train])
        val_ids.extend(ids[n_train:])
    return train_ids, val_ids


def load_layer_features(demos, indices, layer):
    """Load one layer's features for selected demos.

    Returns list of (T, D) float32 arrays.
    """
    by_file = defaultdict(list)
    for pos, idx in enumerate(indices):
        m = demos[idx]
        by_file[m["h5_path"]].append((pos, m))

    feats = [None] * len(indices)
    for h5_path, entries in by_file.items():
        with h5py.File(h5_path, "r") as f:
            for pos, m in entries:
                ds = f[m["h5_key"]][m["feature_key"]]
                if m["is_3d"]:
                    data = ds[:, layer, :]
                else:
                    data = ds[:]
                feats[pos] = np.asarray(data, dtype=np.float32)
    return feats


# ============================================================
# Core: flatten, PCA, linear probe, selectivity
# ============================================================

def flatten_features(feats, demos, indices):
    """Flatten per-demo features into (N, D) array + labels + demo boundaries.

    Returns:
        X: (N, D) float32
        y: (N,) int — task label
        demo_ids: (N,) int — which demo each sample came from
        demo_Ts: list of int — timestep count per demo (for binning)
    """
    Xs, ys, dids = [], [], []
    demo_Ts = []
    for pos, idx in enumerate(indices):
        feat = feats[pos]
        T = feat.shape[0]
        task = demos[idx]["task"]
        label = demos[idx]["_label"]
        Xs.append(feat)
        ys.append(np.full(T, label, dtype=np.int64))
        dids.append(np.full(T, pos, dtype=np.int64))
        demo_Ts.append(T)

    return (np.concatenate(Xs, axis=0),
            np.concatenate(ys, axis=0),
            np.concatenate(dids, axis=0),
            demo_Ts)


def fit_pca_transform(X_train, X_val, pca_dim, seed=42):
    """Fit PCA on train, transform both. Returns transformed arrays + variance info."""
    pca = PCA(n_components=pca_dim, svd_solver="randomized", random_state=seed)
    X_tr_pca = pca.fit_transform(X_train)
    X_val_pca = pca.transform(X_val)
    evr = pca.explained_variance_ratio_
    return X_tr_pca, X_val_pca, {
        "cumulative_variance_ratio": float(evr.sum()),
        "top_10_variance_ratios": [float(x) for x in evr[:10]],
    }


def train_linear_probe(X_train, y_train, X_val, y_val, seed=42, max_iter=1000):
    """Train LogisticRegression, return accuracy and macro F1."""
    clf = LogisticRegression(
        solver="lbfgs", max_iter=max_iter, random_state=seed, n_jobs=-1,
    )
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_val)
    acc = accuracy_score(y_val, y_pred)
    f1 = f1_score(y_val, y_pred, average="macro")
    return acc, f1, y_pred


def compute_selectivity(X_train, y_train, X_val, y_val,
                        task_acc, n_shuffles=5, seed=42):
    """Selectivity index (Hewitt & Manning 2019).

    control = accuracy with randomly shuffled labels (mean of n_shuffles runs).
    selectivity = task_acc - control_acc.
    """
    rng = np.random.RandomState(seed)
    control_accs = []
    for _ in range(n_shuffles):
        y_shuf = rng.permutation(y_train)
        clf = LogisticRegression(
            solver="lbfgs", max_iter=1000, random_state=seed, n_jobs=-1,
        )
        clf.fit(X_train, y_shuf)
        y_pred = clf.predict(X_val)
        control_accs.append(accuracy_score(y_val, y_pred))

    control_mean = float(np.mean(control_accs))
    return {
        "task_accuracy": task_acc,
        "control_accuracy": control_mean,
        "selectivity": task_acc - control_mean,
        "control_accs": [float(x) for x in control_accs],
    }


def compute_per_bin_accuracy(X_val, y_val, demo_ids_val, demo_Ts_val,
                             X_train, y_train, n_bins, seed=42):
    """Per-timestep-bin accuracy.

    Splits each demo's timesteps into n_bins equal bins, trains on all train data,
    evaluates per bin.
    """
    # Train one probe on all train data
    clf = LogisticRegression(
        solver="lbfgs", max_iter=1000, random_state=seed, n_jobs=-1,
    )
    clf.fit(X_train, y_train)

    # Assign each val sample to a bin based on its relative position in its demo
    bin_assignments = np.zeros(len(X_val), dtype=np.int64)
    offset = 0
    for demo_pos, T in enumerate(demo_Ts_val):
        for t in range(T):
            # bin index: which fraction of the demo this timestep falls in
            b = min(int(t / T * n_bins), n_bins - 1)
            bin_assignments[offset + t] = b
        offset += T

    y_pred = clf.predict(X_val)
    bin_accs = {}
    for b in range(n_bins):
        mask = bin_assignments == b
        if mask.sum() == 0:
            bin_accs[b] = None
            continue
        bin_accs[b] = float(accuracy_score(y_val[mask], y_pred[mask]))

    return bin_accs


# ============================================================
# Main
# ============================================================

def run_one_layer(demos, train_ids, val_ids, layer, args):
    """Run PCA + linear probe for one layer. Returns result dict."""
    train_feats = load_layer_features(demos, train_ids, layer)
    val_feats = load_layer_features(demos, val_ids, layer)

    X_tr, y_tr, _, _ = flatten_features(train_feats, demos, train_ids)
    X_val, y_val, demo_ids_val, demo_Ts_val = flatten_features(
        val_feats, demos, val_ids
    )
    del train_feats, val_feats

    # PCA if needed
    pca_info = None
    if args.pca_dim is not None and args.pca_dim < X_tr.shape[1]:
        X_tr, X_val, pca_info = fit_pca_transform(
            X_tr, X_val, args.pca_dim, seed=args.seed
        )

    # Linear probe
    acc, f1, y_pred = train_linear_probe(X_tr, y_tr, X_val, y_val, seed=args.seed)

    # Trajectory-level accuracy (majority vote)
    n_val_demos = len(demo_Ts_val)
    n_classes = len(set(y_tr))
    traj_correct = 0
    for d in range(n_val_demos):
        mask = demo_ids_val == d
        if mask.sum() == 0:
            continue
        majority = np.bincount(y_pred[mask].astype(np.int64), minlength=n_classes).argmax()
        if majority == y_val[mask][0]:
            traj_correct += 1
    traj_acc = traj_correct / n_val_demos if n_val_demos > 0 else 0.0

    # Selectivity index
    sel = compute_selectivity(X_tr, y_tr, X_val, y_val, acc,
                              n_shuffles=5, seed=args.seed)

    # Per-timestep-bin accuracy
    bin_accs = compute_per_bin_accuracy(
        X_val, y_val, demo_ids_val, demo_Ts_val,
        X_tr, y_tr, args.n_bins, seed=args.seed,
    )

    result = {
        "layer": layer,
        "accuracy": float(acc),
        "traj_accuracy": float(traj_acc),
        "macro_f1": float(f1),
        "selectivity": sel,
        "per_bin_accuracy": {str(k): v for k, v in bin_accs.items()},
        "n_train_samples": int(len(y_tr)),
        "n_val_samples": int(len(y_val)),
    }
    if pca_info is not None:
        result["pca_info"] = pca_info

    return result


def main():
    p = argparse.ArgumentParser(
        description="PCA + Linear Probe Goal Classification"
    )
    p.add_argument("--model_type", required=True,
                   choices=["trained", "untrained", "dino"],
                   help="Model type: trained/untrained VLA or DINO")
    p.add_argument("--feature_dir", required=True,
                   help="Directory with per-task .h5 feature files")
    p.add_argument("--feature_key", default=None,
                   help="H5 feature key (default: last_preaction for VLA, "
                        "cls_token for DINO)")
    p.add_argument("--pca_dim", type=int, default=1024,
                   help="PCA target dimension (default: 1024, skipped for DINO)")
    p.add_argument("--output_dir", default=None,
                   help="Output directory (default: auto)")
    p.add_argument("--n_bins", type=int, default=10,
                   help="Number of timestep bins (default: 10)")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--layers", default=None,
                   help="Layer range '0-32' or list '0,5,10'. Default: all")
    args = p.parse_args()

    # Defaults
    if args.feature_key is None:
        args.feature_key = "cls_token" if args.model_type == "dino" else "last_preaction"
    if args.model_type == "dino":
        args.pca_dim = None  # DINO already 1024, skip PCA
    if args.output_dir is None:
        args.output_dir = f"{PROJECT_ROOT}/results/pca_linear_probe_gc/"

    np.random.seed(args.seed)

    print(f"=== PCA + Linear Probe Goal Classification ===")
    print(f"Model: {args.model_type} | Feature key: {args.feature_key} | "
          f"PCA dim: {args.pca_dim} | Seed: {args.seed}")

    # Scan features
    demos, n_layers, hidden_dim = scan_features(args.feature_dir, args.feature_key)

    # Assign task labels
    task_names = sorted(set(m["task"] for m in demos))
    task_to_idx = {t: i for i, t in enumerate(task_names)}
    for m in demos:
        m["_label"] = task_to_idx[m["task"]]

    # Parse layers
    if args.layers is not None:
        if "-" in args.layers and "," not in args.layers:
            lo, hi = args.layers.split("-")
            layers = list(range(int(lo), int(hi) + 1))
        else:
            layers = [int(x) for x in args.layers.split(",")]
    else:
        layers = list(range(n_layers))

    # Split
    train_ids, val_ids = split_by_task(demos)

    print(f"Features: {len(demos)} demos, {n_layers} layers, dim={hidden_dim}")
    print(f"Tasks ({len(task_names)}): {task_names}")
    print(f"Split: {len(train_ids)} train / {len(val_ids)} val demos")
    print(f"Layers to probe: {layers}")

    # Run per-layer
    all_results = {}
    for li, layer in enumerate(layers):
        print(f"\n[Layer {layer}] ({li+1}/{len(layers)})", flush=True)
        result = run_one_layer(demos, train_ids, val_ids, layer, args)
        all_results[layer] = result
        print(f"  acc={result['accuracy']:.4f}  traj_acc={result['traj_accuracy']:.4f}  "
              f"F1={result['macro_f1']:.4f}  "
              f"selectivity={result['selectivity']['selectivity']:.4f}")

    # Build summary
    best_layer = max(all_results, key=lambda k: all_results[k]["accuracy"])
    summary = {
        "model_type": args.model_type,
        "feature_key": args.feature_key,
        "pca_dim": args.pca_dim,
        "hidden_dim": hidden_dim,
        "n_layers": n_layers,
        "n_tasks": len(task_names),
        "task_names": task_names,
        "seed": args.seed,
        "best_layer": best_layer,
        "best_accuracy": all_results[best_layer]["accuracy"],
        "best_traj_accuracy": all_results[best_layer]["traj_accuracy"],
        "best_macro_f1": all_results[best_layer]["macro_f1"],
        "per_layer_accuracies": {
            str(k): all_results[k]["accuracy"] for k in sorted(all_results)
        },
        "per_layer_traj_accuracies": {
            str(k): all_results[k]["traj_accuracy"] for k in sorted(all_results)
        },
        "per_layer_selectivity": {
            str(k): all_results[k]["selectivity"]["selectivity"]
            for k in sorted(all_results)
        },
        "per_layer_control_accuracy": {
            str(k): all_results[k]["selectivity"]["control_accuracy"]
            for k in sorted(all_results)
        },
        "per_layer_per_bin_accuracy": {
            str(k): all_results[k]["per_bin_accuracy"]
            for k in sorted(all_results)
        },
        "per_layer_details": {
            str(k): all_results[k] for k in sorted(all_results)
        },
    }

    # Add PCA variance info if applicable
    if args.pca_dim is not None:
        evr_by_layer = {}
        for k in sorted(all_results):
            pi = all_results[k].get("pca_info")
            if pi:
                evr_by_layer[str(k)] = pi["cumulative_variance_ratio"]
        summary["explained_variance_ratios"] = evr_by_layer

    # Save
    os.makedirs(args.output_dir, exist_ok=True)
    out_path = os.path.join(
        args.output_dir, f"{args.model_type}_pca{args.pca_dim or 'none'}.json"
    )
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nResults saved to {out_path}")

    # Print compact JSON summary to stdout
    compact = {
        "model_type": args.model_type,
        "pca_dim": args.pca_dim,
        "best_layer": best_layer,
        "best_accuracy": summary["best_accuracy"],
        "best_traj_accuracy": summary["best_traj_accuracy"],
        "best_selectivity": summary["per_layer_selectivity"].get(str(best_layer)),
        "per_layer_accuracies": summary["per_layer_accuracies"],
    }
    print("\n" + json.dumps(compact, indent=2))


if __name__ == "__main__":
    main()

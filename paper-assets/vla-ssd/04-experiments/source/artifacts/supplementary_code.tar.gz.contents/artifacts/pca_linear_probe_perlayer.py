"""PCA-1024 + Linear Probe Per-Layer Sweep for goal classification.

Compares trained VLA / untrained VLA / DINO features.
Split follows train_probes.py: first 80% demos train, last 20% val (per task).
"""

import h5py
import json
import os
import time
import numpy as np
from collections import defaultdict
from pathlib import Path
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score


def scan_and_load_layer(features_dir, layer_idx, is_vla=True):
    """Load features for one layer from all h5 files.

    VLA: demo_X/last_preaction shape (T, 33, 4096) -> slice [:, layer_idx, :]
    DINO: traj_X/cls_token shape (T, 1024) -> read directly (layer_idx ignored)

    Returns: list of dicts with keys: task, demo_key, feats (T, D)
    """
    records = []
    h5_files = sorted(Path(features_dir).glob("*.h5"))
    for h5_path in h5_files:
        task = h5_path.stem
        with h5py.File(h5_path, "r") as f:
            keys = sorted(f.keys(), key=lambda x: int(x.split("_")[-1]))
            for dk in keys:
                if is_vla:
                    data = f[dk]["last_preaction"][:, layer_idx, :]  # (T, 4096)
                else:
                    data = f[dk]["cls_token"][:]  # (T, 1024)
                records.append(dict(task=task, demo_key=dk, feats=data.astype(np.float32)))
    return records


def split_by_task(records):
    """Replicate train_probes.py split: first 80% demos per task = train."""
    by_task = defaultdict(list)
    for i, r in enumerate(records):
        by_task[r["task"]].append(i)

    train_idx, val_idx = [], []
    for task in sorted(by_task):
        ids = by_task[task]
        n_train = int(len(ids) * 0.8)
        train_idx.extend(ids[:n_train])
        val_idx.extend(ids[n_train:])
    return train_idx, val_idx


def build_Xy(records, indices, task_to_idx):
    """Flatten trajectory features into (N, D) array with task labels."""
    Xs, ys = [], []
    for i in indices:
        r = records[i]
        label = task_to_idx[r["task"]]
        Xs.append(r["feats"])
        ys.extend([label] * len(r["feats"]))
    return np.concatenate(Xs, axis=0), np.array(ys)


def run_model(name, features_dir, n_layers, is_vla):
    print(f"\n{'='*60}")
    print(f"Model: {name} | layers: {n_layers} | dir: {features_dir}")
    print(f"{'='*60}")

    layer_results = {}
    for layer_idx in range(n_layers):
        t0 = time.time()

        records = scan_and_load_layer(features_dir, layer_idx, is_vla=is_vla)
        task_names = sorted(set(r["task"] for r in records))
        task_to_idx = {t: i for i, t in enumerate(task_names)}

        train_idx, val_idx = split_by_task(records)
        X_train, y_train = build_Xy(records, train_idx, task_to_idx)
        X_val, y_val = build_Xy(records, val_idx, task_to_idx)
        del records

        original_dim = X_train.shape[1]
        pca_dim = original_dim
        var_explained = 1.0
        if original_dim > 1024:
            pca = PCA(n_components=1024, random_state=42)
            X_train = pca.fit_transform(X_train)
            X_val = pca.transform(X_val)
            var_explained = float(pca.explained_variance_ratio_.sum())
            pca_dim = 1024
            del pca

        clf = LogisticRegression(
            max_iter=1000, random_state=42, solver="lbfgs",
            multi_class="multinomial", C=1.0,
        )
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_val)
        acc = accuracy_score(y_val, y_pred)
        f1 = f1_score(y_val, y_pred, average="macro")

        elapsed = time.time() - t0
        layer_results[layer_idx] = dict(
            accuracy=round(acc, 4),
            f1=round(f1, 4),
            original_dim=original_dim,
            pca_dim=pca_dim,
            var_explained=round(var_explained, 4),
            n_train=len(y_train),
            n_val=len(y_val),
            n_classes=len(task_names),
            elapsed_s=round(elapsed, 1),
        )
        print(f"  layer {layer_idx:2d}: acc={acc:.4f}  f1={f1:.4f}  "
              f"var_expl={var_explained:.4f}  {elapsed:.1f}s")

    best_layer = max(layer_results, key=lambda k: layer_results[k]["accuracy"])
    return dict(
        per_layer={str(k): v for k, v in layer_results.items()},
        best_layer=best_layer,
        best_accuracy=layer_results[best_layer]["accuracy"],
        best_f1=layer_results[best_layer]["f1"],
        task_names=task_names,
    )


def main():
    np.random.seed(42)

    models = [
        ("trained_vla",   "/root/autodl-tmp/vla-ssd/features/trained_libero_goal/",   33, True),
        ("untrained_vla", "/root/autodl-tmp/vla-ssd/features/untrained_libero_goal/", 33, True),
        ("dino",          "/root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/",      1, False),
    ]

    results = {}
    for name, fdir, n_layers, is_vla in models:
        results[name] = run_model(name, fdir, n_layers, is_vla)

    out_dir = "/root/autodl-tmp/vla-ssd/results/"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "pca1024_linear_perlayer.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for name in results:
        r = results[name]
        print(f"  {name:15s}: best_layer={r['best_layer']:2d}  "
              f"acc={r['best_accuracy']:.4f}  f1={r['best_f1']:.4f}")

    delta = results["trained_vla"]["best_accuracy"] - results["untrained_vla"]["best_accuracy"]
    print(f"\n  Delta(trained-untrained) = {delta:.4f} ({delta*100:.1f}pp)")
    print(f"  Gate G3 (>10pp): {'PASS' if delta > 0.10 else 'FAIL'}")

    dino_acc = results["dino"]["best_accuracy"]
    print(f"  DINO baseline acc = {dino_acc:.4f}")


if __name__ == "__main__":
    main()

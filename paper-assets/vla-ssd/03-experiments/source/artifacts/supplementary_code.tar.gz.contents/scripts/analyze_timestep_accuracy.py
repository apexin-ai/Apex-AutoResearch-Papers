"""Per-timestep goal classification accuracy analysis.

Retrains a GoalClassificationProbe on the best layer, then evaluates
accuracy per normalized-timestep bin on the val set.
"""

import argparse
import json
import os
import sys
import glob
import time
from collections import defaultdict
from pathlib import Path

import h5py
import numpy as np
import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score, f1_score

AGG_MAP = {
    "last_preaction": ("last_preaction", "cls_token"),
    "image_mean": ("image_mean", "patch_mean"),
}


class GoalClassificationProbe(nn.Module):
    def __init__(self, in_dim, n_classes, hidden_dim=256, dropout=0.1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, n_classes),
        )

    def forward(self, x):
        return self.net(x)


def scan_features(features_dir, aggregation):
    primary, fallback = AGG_MAP[aggregation]
    traj_metas = []
    n_layers = hidden_dim = None

    for h5_path in sorted(glob.glob(os.path.join(features_dir, "*.h5"))):
        task = Path(h5_path).stem
        with h5py.File(h5_path, "r") as f:
            keys = sorted(f.keys(), key=lambda x: int(x.split("_")[-1]))
            for hk in keys:
                if primary in f[hk]:
                    fk = primary
                elif fallback in f[hk]:
                    fk = fallback
                else:
                    raise KeyError(f"No feature key in {h5_path}/{hk}")

                shape = f[hk][fk].shape
                is_3d = len(shape) == 3
                T = shape[0]
                if n_layers is None:
                    n_layers = shape[1] if is_3d else 1
                    hidden_dim = shape[-1]

                traj_metas.append(dict(
                    task=task, h5_path=h5_path, h5_key=hk,
                    feat_key=fk, T=T, is_3d=is_3d,
                ))

    if not traj_metas:
        raise FileNotFoundError(f"No .h5 files found in {features_dir}")
    return traj_metas, n_layers, hidden_dim


def split_by_task(traj_metas):
    by_task = defaultdict(list)
    for i, m in enumerate(traj_metas):
        by_task[m["task"]].append(i)

    train_ids, val_ids = [], []
    for task in sorted(by_task):
        ids = by_task[task]
        n_train = int(len(ids) * 0.8)
        train_ids.extend(ids[:n_train])
        val_ids.extend(ids[n_train:])
    return train_ids, val_ids


def load_layer_features(traj_metas, indices, layer):
    by_file = defaultdict(list)
    for pos, idx in enumerate(indices):
        m = traj_metas[idx]
        by_file[m["h5_path"]].append((pos, m))

    feats = [None] * len(indices)
    for h5_path, entries in by_file.items():
        with h5py.File(h5_path, "r") as f:
            for pos, m in entries:
                ds = f[m["h5_key"]][m["feat_key"]]
                if m["is_3d"]:
                    data = ds[:, layer, :]
                else:
                    data = ds[:]
                feats[pos] = np.asarray(data, dtype=np.float32)
    return feats


def train_probe(X_tr, y_tr, X_val, y_val, in_dim, n_classes, device,
                lr=1e-3, epochs=50, patience=5, batch_size=256):
    model = GoalClassificationProbe(in_dim, n_classes).to(device)
    opt = torch.optim.Adam(model.parameters(), lr=lr)
    crit = nn.CrossEntropyLoss()

    X_tr, y_tr = X_tr.to(device), y_tr.to(device)
    X_val, y_val = X_val.to(device), y_val.to(device)

    best_acc, best_state, wait, final_ep = 0.0, None, 0, 0

    for ep in range(epochs):
        model.train()
        perm = torch.randperm(len(X_tr), device=device)
        for s in range(0, len(X_tr), batch_size):
            idx = perm[s : s + batch_size]
            loss = crit(model(X_tr[idx]), y_tr[idx])
            opt.zero_grad()
            loss.backward()
            opt.step()

        model.eval()
        with torch.no_grad():
            logits = model(X_val)
            preds = logits.argmax(dim=1)
            acc = (preds == y_val).float().mean().item()

        if acc > best_acc:
            best_acc = acc
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            wait = 0
        else:
            wait += 1
            if wait >= patience:
                final_ep = ep + 1
                break
        final_ep = ep + 1

    model.load_state_dict(best_state)
    model.eval()
    print(f"  Trained {final_ep} epochs, best val acc = {best_acc:.4f}")
    return model


def analyze_per_timestep(model, val_feats, val_ids, traj_metas, task_to_idx,
                         device, n_bins=10):
    all_preds = []
    all_labels = []
    all_norm_t = []

    model.eval()
    with torch.no_grad():
        for feat, idx in zip(val_feats, val_ids):
            T = feat.shape[0]
            label = task_to_idx[traj_metas[idx]["task"]]
            norm_ts = np.arange(T, dtype=np.float32) / max(T - 1, 1)

            X = torch.from_numpy(feat).to(device)
            logits = model(X)
            preds = logits.argmax(dim=1).cpu().numpy()

            all_preds.append(preds)
            all_labels.append(np.full(T, label, dtype=np.int64))
            all_norm_t.append(norm_ts)

    all_preds = np.concatenate(all_preds)
    all_labels = np.concatenate(all_labels)
    all_norm_t = np.concatenate(all_norm_t)

    bin_edges = np.linspace(0, 1, n_bins + 1)
    bin_results = {}

    for b in range(n_bins):
        lo, hi = bin_edges[b], bin_edges[b + 1]
        if b == n_bins - 1:
            mask = (all_norm_t >= lo) & (all_norm_t <= hi)
        else:
            mask = (all_norm_t >= lo) & (all_norm_t < hi)

        n_samples = mask.sum()
        if n_samples == 0:
            bin_results[b] = dict(
                bin_range=f"[{lo:.1f}, {hi:.1f})",
                n_samples=0, accuracy=0.0, macro_f1=0.0
            )
            continue

        acc = float(accuracy_score(all_labels[mask], all_preds[mask]))
        f1 = float(f1_score(all_labels[mask], all_preds[mask],
                            average="macro", zero_division=0))

        bin_results[b] = dict(
            bin_range=f"[{lo:.1f}, {hi:.1f})" if b < n_bins - 1 else f"[{lo:.1f}, {hi:.1f}]",
            n_samples=int(n_samples),
            accuracy=acc,
            macro_f1=f1,
        )

    return bin_results


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--features_dir", required=True)
    p.add_argument("--results_dir", required=True,
                   help="Dir containing summary.json from goal_classification probe")
    p.add_argument("--output_dir", default=None,
                   help="Dir to save timestep analysis (default: results_dir)")
    p.add_argument("--aggregation", default="last_preaction",
                   choices=["last_preaction", "image_mean"])
    p.add_argument("--layer", type=int, default=None,
                   help="Layer to analyze (default: best_layer from summary.json)")
    p.add_argument("--n_bins", type=int, default=10)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")

    summary_path = os.path.join(args.results_dir, "summary.json")
    with open(summary_path) as f:
        summary = json.load(f)
    best_layer = args.layer if args.layer is not None else summary["best_layer"]
    print(f"=== Per-Timestep Goal Classification Analysis ===")
    print(f"Features: {args.features_dir}")
    print(f"Layer: {best_layer} (overall acc={summary['best_accuracy']:.4f})")
    print(f"Device: {device}")

    traj_metas, n_layers, hidden_dim = scan_features(args.features_dir, args.aggregation)
    task_names = sorted(set(m["task"] for m in traj_metas))
    task_to_idx = {t: i for i, t in enumerate(task_names)}
    n_classes = len(task_names)

    train_ids, val_ids = split_by_task(traj_metas)
    print(f"Tasks: {n_classes}, Trajs: {len(train_ids)} train / {len(val_ids)} val")

    print(f"\nLoading layer {best_layer} features...")
    train_feats = load_layer_features(traj_metas, train_ids, best_layer)
    val_feats = load_layer_features(traj_metas, val_ids, best_layer)

    Xs_tr, Ys_tr = [], []
    for feat, idx in zip(train_feats, train_ids):
        label = task_to_idx[traj_metas[idx]["task"]]
        Xs_tr.append(torch.from_numpy(feat))
        Ys_tr.append(torch.full((feat.shape[0],), label, dtype=torch.long))
    X_tr = torch.cat(Xs_tr)
    y_tr = torch.cat(Ys_tr)

    Xs_val, Ys_val = [], []
    for feat, idx in zip(val_feats, val_ids):
        label = task_to_idx[traj_metas[idx]["task"]]
        Xs_val.append(torch.from_numpy(feat))
        Ys_val.append(torch.full((feat.shape[0],), label, dtype=torch.long))
    X_val = torch.cat(Xs_val)
    y_val = torch.cat(Ys_val)

    print(f"Samples: {len(X_tr)} train / {len(X_val)} val, dim={hidden_dim}")

    print("\nTraining probe...")
    model = train_probe(X_tr, y_tr, X_val, y_val, hidden_dim, n_classes, device)

    print(f"\nAnalyzing per-timestep accuracy ({args.n_bins} bins)...")
    bin_results = analyze_per_timestep(
        model, val_feats, val_ids, traj_metas, task_to_idx, device, args.n_bins
    )

    print(f"\n{'Bin':<6} {'Range':<14} {'N':>6} {'Accuracy':>10} {'F1':>10}")
    print("-" * 50)
    for b in range(args.n_bins):
        r = bin_results[b]
        print(f"{b:<6} {r['bin_range']:<14} {r['n_samples']:>6} "
              f"{r['accuracy']:>10.4f} {r['macro_f1']:>10.4f}")

    early_acc = np.mean([bin_results[b]["accuracy"] for b in [0, 1]])
    late_acc = np.mean([bin_results[b]["accuracy"] for b in [args.n_bins - 2, args.n_bins - 1]])
    print(f"\nEarly (bin 0-1) avg acc: {early_acc:.4f}")
    print(f"Late  (bin {args.n_bins-2}-{args.n_bins-1}) avg acc: {late_acc:.4f}")
    print(f"Delta (late - early):    {late_acc - early_acc:.4f}")

    output_dir = args.output_dir or args.results_dir
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "timestep_accuracy.json")
    out_data = dict(
        layer=best_layer,
        overall_accuracy=summary["best_accuracy"],
        n_bins=args.n_bins,
        bins={str(b): bin_results[b] for b in range(args.n_bins)},
        early_avg_acc=early_acc,
        late_avg_acc=late_acc,
        delta=late_acc - early_acc,
    )
    with open(out_path, "w") as f:
        json.dump(out_data, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()

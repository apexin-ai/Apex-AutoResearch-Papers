"""
Train per-layer correctness probes (logistic regression) on English activations.

For each layer, trains an L2-regularized LogisticRegression on 80% of the
English data and evaluates on the held-out 20%. Reports AUROC, ECE, Brier score.

Input:  .pt files from extract_activations.py  (e.g. activations/layer8_en.pt)
Output: probe pickle files + train_metrics.csv

Usage:
  python train_probe.py \
    --activations_dir ./activations \
    --output_dir ./probes \
    --layers 0,4,8,12,16,20,24,28,31
"""

import argparse
import os
import pickle

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, brier_score_loss


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--activations_dir", default="./activations")
    p.add_argument("--output_dir", default="./probes")
    p.add_argument("--layers", default=None,
                   help="Comma-separated layer indices. Default: auto-detect from activations_dir")
    p.add_argument("--test_size", type=float, default=0.2)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--C", type=float, default=1.0, help="Inverse regularization strength")
    p.add_argument("--max_iter", type=int, default=2000)
    return p.parse_args()


def compute_ece(probs, labels, n_bins=10):
    """Histogram-based Expected Calibration Error (10 equal-width bins)."""
    bin_edges = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    for lo, hi in zip(bin_edges[:-1], bin_edges[1:]):
        mask = (probs > lo) & (probs <= hi)
        if lo == 0.0:
            mask = (probs >= lo) & (probs <= hi)
        n_in_bin = mask.sum()
        if n_in_bin == 0:
            continue
        avg_conf = probs[mask].mean()
        avg_acc = labels[mask].mean()
        ece += (n_in_bin / len(probs)) * abs(avg_acc - avg_conf)
    return ece


def main():
    args = parse_args()
    if args.layers is None:
        import glob
        available = sorted(set(
            int(os.path.basename(f).split('_')[0].replace('layer', ''))
            for f in glob.glob(os.path.join(args.activations_dir, 'layer*_en.pt'))
        ))
        if not available:
            raise RuntimeError(f"No layer*_en.pt files found in {args.activations_dir}")
        print(f"Auto-detected layers: {available}")
        layer_indices = available
    else:
        layer_indices = sorted(int(x) for x in args.layers.split(","))
    os.makedirs(args.output_dir, exist_ok=True)

    results = []
    print(f"{'Layer':>5s} {'N_train':>7s} {'N_test':>6s} {'AUROC':>7s} {'ECE':>7s} {'Brier':>7s}")
    print("-" * 46)

    for li in layer_indices:
        pt_path = os.path.join(args.activations_dir, f"layer{li}_en.pt")
        if not os.path.exists(pt_path):
            print(f"  [SKIP] {pt_path} not found")
            continue

        data = torch.load(pt_path, weights_only=True)
        X = data["activations"].numpy()
        y = data["labels"].numpy()

        if len(np.unique(y)) < 2:
            print(f"  [SKIP] Layer {li}: only one class present (all correct or all wrong)")
            continue

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=args.test_size, random_state=args.seed, stratify=y,
        )

        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)
        X_test_s = scaler.transform(X_test)

        clf = LogisticRegression(
            C=args.C, penalty="l2", solver="lbfgs", max_iter=args.max_iter, random_state=args.seed,
        )
        clf.fit(X_train_s, y_train)

        probs = clf.predict_proba(X_test_s)[:, 1]
        auroc = roc_auc_score(y_test, probs)
        ece = compute_ece(probs, y_test)
        brier = brier_score_loss(y_test, probs)

        print(f"{li:>5d} {len(y_train):>7d} {len(y_test):>6d} {auroc:>7.4f} {ece:>7.4f} {brier:>7.4f}")

        probe_path = os.path.join(args.output_dir, f"probe_layer{li}.pkl")
        with open(probe_path, "wb") as f:
            pickle.dump({"scaler": scaler, "model": clf}, f)

        results.append({
            "layer": li,
            "n_train": len(y_train),
            "n_test": len(y_test),
            "auroc": auroc,
            "ece": ece,
            "brier": brier,
            "probe_path": probe_path,
        })

    csv_path = os.path.join(args.output_dir, "train_metrics.csv")
    with open(csv_path, "w") as f:
        f.write("layer,n_train,n_test,auroc,ece,brier\n")
        for r in results:
            f.write(f"{r['layer']},{r['n_train']},{r['n_test']},{r['auroc']:.6f},{r['ece']:.6f},{r['brier']:.6f}\n")
    print(f"\nMetrics saved to {csv_path}")
    print(f"Probes saved to {args.output_dir}/")


if __name__ == "__main__":
    main()

"""
Evaluate cross-lingual transfer of English correctness probes.

Three transfer conditions:
  (a) Zero-shot: apply English probe directly to target-language activations
  (b) Mean-shift: shift target activations by (mean_en - mean_tgt) before probing
  (c) Linear projection (Procrustes): learn orthogonal W from parallel pairs,
      transform X_tgt' = (X_tgt - mu_tgt) @ W + mu_en, then probe

Input:  English probes (.pkl) + per-language activations (.pt)
Output: transfer_results.csv with AUROC / ECE / Brier per (layer, language, method)

Usage:
  python transfer_eval.py \
    --activations_dir ./activations \
    --probes_dir ./probes \
    --output_dir ./results \
    --layers 0,4,8,12,16,20,24,28,31 \
    --languages zh ar hi sw ko \
    --n_proj_pairs 100
"""

import argparse
import os
import pickle

import numpy as np
import torch
from scipy.linalg import orthogonal_procrustes
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, brier_score_loss
from sklearn.preprocessing import StandardScaler


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--activations_dir", default="./activations")
    p.add_argument("--probes_dir", default="./probes")
    p.add_argument("--output_dir", default="./results")
    p.add_argument("--layers", default=None,
                   help="Comma-separated layer indices. Default: auto-detect from activations_dir")
    p.add_argument("--languages", nargs="+", default=["zh", "ar", "hi", "sw", "ko"])
    p.add_argument("--n_perm", type=int, default=1000,
                   help="Number of permutations for significance test")
    p.add_argument("--n_proj_pairs", type=int, default=0,
                   help="Number of parallel pairs for linear projection. 0 = skip projection.")
    p.add_argument("--proj_seed", type=int, default=42,
                   help="Random seed for sampling parallel pairs")
    p.add_argument("--n_few_shot", default=None,
                   help="Comma-separated few-shot counts, e.g. '25,100'. 0 or omit = skip.")
    return p.parse_args()


def compute_ece(probs, labels, n_bins=10):
    """Histogram-based ECE."""
    bin_edges = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    for lo, hi in zip(bin_edges[:-1], bin_edges[1:]):
        mask = (probs > lo) & (probs <= hi)
        if lo == 0.0:
            mask = (probs >= lo) & (probs <= hi)
        n_in_bin = mask.sum()
        if n_in_bin == 0:
            continue
        ece += (n_in_bin / len(probs)) * abs(labels[mask].mean() - probs[mask].mean())
    return ece


def permutation_test_auroc(y_true, y_score, n_perm=1000, seed=42):
    """One-sided permutation test: is AUROC significantly above chance?"""
    rng = np.random.RandomState(seed)
    real_auroc = roc_auc_score(y_true, y_score)
    count_ge = 0
    for _ in range(n_perm):
        perm_auroc = roc_auc_score(rng.permutation(y_true), y_score)
        if perm_auroc >= real_auroc:
            count_ge += 1
    return (count_ge + 1) / (n_perm + 1)


def evaluate_probe(probe, scaler, X, y, n_perm=1000):
    """Apply probe and compute metrics. Returns (auroc, ece, brier, p_value, probs)."""
    X_s = scaler.transform(X)
    probs = probe.predict_proba(X_s)[:, 1]
    logits = probe.decision_function(X_s)

    if len(np.unique(y)) < 2:
        return None, None, None, None, probs

    auroc = roc_auc_score(y, logits)
    ece = compute_ece(probs, y)
    brier = brier_score_loss(y, probs)
    p_value = permutation_test_auroc(y, logits, n_perm=n_perm)
    return auroc, ece, brier, p_value, probs


def procrustes_align(X_en_pairs, X_tgt_pairs, X_tgt_all):
    """Align target activations to English space via orthogonal Procrustes.

    Learns orthogonal W from N parallel pairs such that X_tgt @ W ≈ X_en (after centering).
    Consistent with cross-lingual alignment literature (VecMap/MUSE).

    Args:
        X_en_pairs: (N, D) English activations for parallel items
        X_tgt_pairs: (N, D) Target activations for the same items
        X_tgt_all: (M, D) All target activations to transform

    Returns:
        X_aligned: (M, D) Transformed target activations in English space
    """
    mu_en = X_en_pairs.mean(axis=0)
    mu_tgt = X_tgt_pairs.mean(axis=0)
    X_en_c = X_en_pairs - mu_en
    X_tgt_c = X_tgt_pairs - mu_tgt
    W, _ = orthogonal_procrustes(X_tgt_c, X_en_c)
    return (X_tgt_all - mu_tgt) @ W + mu_en


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

    def _fmt(v):
        return f"{v:.4f}" if v is not None else "  N/A "

    print(f"{'Layer':>5s} {'Lang':>4s} {'Method':>10s} {'AUROC':>7s} {'ECE':>7s} {'Brier':>7s} {'p':>7s} {'N':>6s}")
    print("-" * 60)

    for li in layer_indices:
        probe_path = os.path.join(args.probes_dir, f"probe_layer{li}.pkl")
        if not os.path.exists(probe_path):
            print(f"  [SKIP] No probe for layer {li}")
            continue

        with open(probe_path, "rb") as f:
            saved = pickle.load(f)
        probe = saved["model"]
        scaler = saved["scaler"]

        en_pt = os.path.join(args.activations_dir, f"layer{li}_en.pt")
        if not os.path.exists(en_pt):
            print(f"  [SKIP] No English activations for layer {li}")
            continue
        en_data = torch.load(en_pt, weights_only=True)
        en_mean = en_data["activations"].numpy().mean(axis=0)

        for lang in args.languages:
            tgt_pt = os.path.join(args.activations_dir, f"layer{li}_{lang}.pt")
            if not os.path.exists(tgt_pt):
                print(f"  [SKIP] No activations for layer {li}, lang {lang}")
                continue

            tgt_data = torch.load(tgt_pt, weights_only=True)
            X_tgt = tgt_data["activations"].numpy()
            y_tgt = tgt_data["labels"].numpy()
            n_samples = len(y_tgt)

            # (a) Zero-shot
            auroc, ece, brier, pval, _ = evaluate_probe(probe, scaler, X_tgt, y_tgt, n_perm=args.n_perm)
            row = {"layer": li, "language": lang, "method": "zero_shot",
                   "auroc": auroc, "ece": ece, "brier": brier, "p_value": pval, "n": n_samples}
            results.append(row)
            print(f"{li:>5d} {lang:>4s} {'zero_shot':>10s} {_fmt(auroc):>7s} {_fmt(ece):>7s} {_fmt(brier):>7s} {_fmt(pval):>7s} {n_samples:>6d}")

            # (b) Mean-shift: X_shifted = X_tgt - (mean_tgt - mean_en)
            tgt_mean = X_tgt.mean(axis=0)
            X_shifted = X_tgt - (tgt_mean - en_mean)
            auroc, ece, brier, pval, _ = evaluate_probe(probe, scaler, X_shifted, y_tgt, n_perm=args.n_perm)
            row = {"layer": li, "language": lang, "method": "mean_shift",
                   "auroc": auroc, "ece": ece, "brier": brier, "p_value": pval, "n": n_samples}
            results.append(row)
            print(f"{li:>5d} {lang:>4s} {'mean_shift':>10s} {_fmt(auroc):>7s} {_fmt(ece):>7s} {_fmt(brier):>7s} {_fmt(pval):>7s} {n_samples:>6d}")

            # (c) Linear projection (Procrustes): orthogonal alignment from parallel pairs
            if args.n_proj_pairs > 0:
                X_en_all = en_data["activations"].numpy()
                n_pairs = min(args.n_proj_pairs, len(X_en_all), len(X_tgt))
                rng = np.random.RandomState(args.proj_seed)
                pair_idx = rng.choice(min(len(X_en_all), len(X_tgt)), size=n_pairs, replace=False)
                X_aligned = procrustes_align(X_en_all[pair_idx], X_tgt[pair_idx], X_tgt)
                auroc, ece, brier, pval, _ = evaluate_probe(probe, scaler, X_aligned, y_tgt, n_perm=args.n_perm)
                row = {"layer": li, "language": lang, "method": f"procrustes_{n_pairs}",
                       "auroc": auroc, "ece": ece, "brier": brier, "p_value": pval, "n": n_samples}
                results.append(row)
                print(f"{li:>5d} {lang:>4s} {f'proc_{n_pairs}':>10s} {_fmt(auroc):>7s} {_fmt(ece):>7s} {_fmt(brier):>7s} {_fmt(pval):>7s} {n_samples:>6d}")

            # (d) Few-shot: retrain probe with English + N target-language samples
            if args.n_few_shot:
                for n_fs in [int(x) for x in args.n_few_shot.split(",")]:
                    if n_fs >= len(y_tgt):
                        print(f"  [SKIP] n_few_shot={n_fs} >= target samples ({len(y_tgt)})")
                        continue

                    rng_fs = np.random.RandomState(args.proj_seed)
                    fs_idx = rng_fs.choice(len(y_tgt), size=n_fs, replace=False)
                    eval_mask = np.ones(len(y_tgt), dtype=bool)
                    eval_mask[fs_idx] = False

                    X_fs = X_tgt[fs_idx]
                    y_fs = y_tgt[fs_idx]
                    X_eval = X_tgt[eval_mask]
                    y_eval = y_tgt[eval_mask]

                    X_en_all = en_data["activations"].numpy()
                    y_en_all = en_data["labels"].numpy()

                    X_combined = np.concatenate([X_en_all, X_fs])
                    y_combined = np.concatenate([y_en_all, y_fs])

                    scaler_fs = StandardScaler()
                    X_combined_s = scaler_fs.fit_transform(X_combined)
                    clf_fs = LogisticRegression(C=1.0, penalty="l2", solver="lbfgs",
                                                max_iter=2000, random_state=42)
                    clf_fs.fit(X_combined_s, y_combined)

                    auroc, ece, brier, pval, _ = evaluate_probe(clf_fs, scaler_fs, X_eval, y_eval, n_perm=args.n_perm)
                    method_name = f"few_shot_{n_fs}"
                    n_eval = len(y_eval)
                    row = {"layer": li, "language": lang, "method": method_name,
                           "auroc": auroc, "ece": ece, "brier": brier, "p_value": pval, "n": n_eval}
                    results.append(row)
                    print(f"{li:>5d} {lang:>4s} {method_name:>10s} {_fmt(auroc):>7s} {_fmt(ece):>7s} {_fmt(brier):>7s} {_fmt(pval):>7s} {n_eval:>6d}")

    csv_path = os.path.join(args.output_dir, "transfer_results.csv")
    with open(csv_path, "w") as f:
        f.write("layer,language,method,auroc,ece,brier,p_value,n\n")
        for r in results:
            vals = []
            for k in ["auroc", "ece", "brier", "p_value"]:
                vals.append(f"{r[k]:.6f}" if r[k] is not None else "")
            f.write(f"{r['layer']},{r['language']},{r['method']},{','.join(vals)},{r['n']}\n")

    print(f"\nResults saved to {csv_path}")


if __name__ == "__main__":
    main()

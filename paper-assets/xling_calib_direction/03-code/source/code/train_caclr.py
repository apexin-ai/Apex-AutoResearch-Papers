"""
CaCLR: Calibration-aware Cross-Lingual Regularization.

Train a linear probe with two additional regularization terms beyond BCE:
  Loss = L_BCE + α · L_SB-ECE + β · L_consistency(MMD)

  - L_SB-ECE: differentiable soft-binning ECE (calibration regularizer)
  - L_consistency: MMD with Gaussian RBF kernel (cross-lingual consistency)

Input:  per-language activation .pt files from extract_activations.py
        (each file has {"activations": Tensor, "labels": Tensor})
Output: trained probe .pkl compatible with transfer_eval.py
        (pickle dict with {"model": CaCLRProbe, "scaler": StandardScaler, ...})

Usage:
  # Single run
  python train_caclr.py \
    --activations_dir ./activations --output_dir ./probes_caclr \
    --layer 16 --languages zh ar hi sw ko --alpha 1.0 --beta 0.1

  # Sweep over α × β
  python train_caclr.py \
    --activations_dir ./activations --output_dir ./probes_caclr \
    --layer 16 --languages zh ar hi sw ko \
    --alpha_sweep 0.01,0.1,0.5,1.0,2.0,5.0,10.0 \
    --beta_sweep 0.001,0.01,0.05,0.1,0.5,1.0
"""

import argparse
import os
import pickle
from itertools import product

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, brier_score_loss


# ---------------------------------------------------------------------------
# Loss components
# ---------------------------------------------------------------------------

def bce_loss(logits, labels):
    """Standard binary cross-entropy on probe logits."""
    return F.binary_cross_entropy_with_logits(logits, labels)


def sb_ece_loss(probs, labels, n_bins=10, temperature=0.05):
    """Differentiable soft-binning ECE approximation.

    Hard-histogram ECE is non-differentiable. We replace indicator-based bin
    assignment with Gaussian soft assignment:
      bin centers c_k = (k + 0.5) / n_bins,  k = 0, ..., n_bins-1
      weights  w_{ik} = softmax( -|p_i - c_k|^2 / temperature )

    Per-bin calibration error:
      CE_k = | Σ_i w_{ik} * (label_i - p_i) | / (Σ_i w_{ik} + ε)

    SB-ECE = Σ_k (Σ_i w_{ik} / N) * CE_k
    """
    centers = torch.linspace(0.5 / n_bins, 1.0 - 0.5 / n_bins, n_bins,
                             device=probs.device)                          # (K,)
    # Pairwise distances: (N, K)
    dists = (probs.unsqueeze(1) - centers.unsqueeze(0)) ** 2               # (N, K)
    weights = F.softmax(-dists / temperature, dim=1)                       # (N, K)

    bin_counts = weights.sum(dim=0)                                        # (K,)
    # Weighted calibration gap per bin
    gap = labels.unsqueeze(1) - probs.unsqueeze(1)                         # (N, K) broadcast
    weighted_gap = (weights * gap).sum(dim=0)                              # (K,)
    per_bin_ce = weighted_gap.abs() / (bin_counts + 1e-8)

    ece = (bin_counts / probs.shape[0] * per_bin_ce).sum()
    return ece


def gaussian_rbf_kernel(x, y, bandwidth=None):
    """Gaussian RBF kernel matrix.

    k(x, y) = exp( -||x - y||^2 / (2 * bandwidth^2) )

    If bandwidth is None, uses the median heuristic:
      bandwidth = sqrt( median(||x_i - y_j||^2) / 2 )
    """
    xx = torch.cdist(x, x) ** 2    # (N, N)
    yy = torch.cdist(y, y) ** 2    # (M, M)
    xy = torch.cdist(x, y) ** 2    # (N, M)

    if bandwidth is None:
        # Median heuristic over cross-distances
        all_dists = xy.detach().reshape(-1)
        median_dist = all_dists.median()
        bandwidth = torch.sqrt(median_dist / 2.0).clamp(min=1e-5)

    gamma = 1.0 / (2.0 * bandwidth ** 2)
    K_xx = torch.exp(-gamma * xx)
    K_yy = torch.exp(-gamma * yy)
    K_xy = torch.exp(-gamma * xy)
    return K_xx, K_yy, K_xy, bandwidth


def mmd_loss(x_en, x_tgt, bandwidth=None):
    """Unbiased estimate of MMD^2 between English and target representations.

    MMD^2 = E[k(x,x')] + E[k(y,y')] - 2·E[k(x,y)]

    where k is a Gaussian RBF kernel with median heuristic bandwidth.
    """
    K_xx, K_yy, K_xy, bw = gaussian_rbf_kernel(x_en, x_tgt, bandwidth)
    n = K_xx.shape[0]
    m = K_yy.shape[0]

    # Unbiased: zero out diagonal for self-terms
    sum_xx = (K_xx.sum() - K_xx.diagonal().sum()) / (n * (n - 1)) if n > 1 else K_xx.mean()
    sum_yy = (K_yy.sum() - K_yy.diagonal().sum()) / (m * (m - 1)) if m > 1 else K_yy.mean()
    sum_xy = K_xy.mean()

    return sum_xx + sum_yy - 2.0 * sum_xy


# ---------------------------------------------------------------------------
# CaCLR Probe model
# ---------------------------------------------------------------------------

class CaCLRProbe(nn.Module):
    """Linear probe with CaCLR regularization.

    Functionally equivalent to sklearn LogisticRegression (single Linear layer),
    but trained with gradient descent plus L_SB-ECE and L_MMD regularizers.

    Exposes predict_proba() and decision_function() for compatibility with
    transfer_eval.py's evaluate_probe().
    """

    def __init__(self, input_dim, l2_weight=1.0):
        super().__init__()
        self.linear = nn.Linear(input_dim, 1)
        self.l2_weight = l2_weight

    def forward(self, x):
        """Return raw logits (N,)."""
        return self.linear(x).squeeze(-1)

    def predict_proba(self, x):
        """Return (N, 2) numpy array of [P(class=0), P(class=1)].

        Accepts numpy array or torch Tensor. Returns numpy for sklearn compat.
        """
        if isinstance(x, np.ndarray):
            x = torch.from_numpy(x).float().to(self.linear.weight.device)
        with torch.no_grad():
            p1 = torch.sigmoid(self.forward(x)).cpu().numpy()
        return np.column_stack([1 - p1, p1])

    def decision_function(self, x):
        """Return logits as 1-D numpy array (sklearn compat)."""
        if isinstance(x, np.ndarray):
            x = torch.from_numpy(x).float().to(self.linear.weight.device)
        with torch.no_grad():
            return self.forward(x).cpu().numpy()

    def l2_reg(self):
        """L2 penalty on weights (not bias), matching sklearn C = 1/l2_weight."""
        return self.l2_weight * (self.linear.weight ** 2).sum()

    @classmethod
    def from_sklearn(cls, sklearn_probe, scaler, l2_weight=1.0):
        """Initialize from a trained sklearn LogisticRegression + StandardScaler.

        Copies weight and bias so CaCLR starts from the converged LR solution.
        The scaler is applied externally (same as sklearn pipeline), so we only
        need the LR parameters here.
        """
        input_dim = sklearn_probe.coef_.shape[1]
        model = cls(input_dim, l2_weight=l2_weight)
        with torch.no_grad():
            model.linear.weight.copy_(torch.from_numpy(sklearn_probe.coef_).float())
            model.linear.bias.copy_(torch.from_numpy(sklearn_probe.intercept_).float())
        return model


# ---------------------------------------------------------------------------
# Training loop
# ---------------------------------------------------------------------------

def train_caclr(
    X_en, y_en,
    X_tgt_dict,
    alpha=1.0,
    beta=0.1,
    lr=1e-3,
    epochs=100,
    l2_weight=1.0,
    init_from_sklearn=True,
    seed=42,
    verbose=True,
):
    """Train CaCLR probe.

    Steps:
      1. Fit StandardScaler on English data.
      2. Train standard LogisticRegression on English (sklearn).
      3. Initialize CaCLRProbe from LR weights.
      4. Fine-tune with L_BCE + α·L_SB-ECE + β·L_MMD.

    Args:
        X_en: (N_en, D) numpy array of English activations.
        y_en: (N_en,) numpy array of binary labels.
        X_tgt_dict: {lang: (X_tgt, y_tgt)} numpy arrays for target languages.
        alpha: weight on SB-ECE calibration loss.
        beta: weight on MMD consistency loss.
        lr: learning rate for Adam optimizer.
        epochs: number of training epochs.
        l2_weight: L2 regularization weight (sklearn C = 1/l2_weight).
        init_from_sklearn: if True, warm-start from sklearn LR solution.
        seed: random seed.
        verbose: print training progress.

    Returns:
        probe: trained CaCLRProbe (on CPU).
        scaler: fitted StandardScaler.
        history: dict with keys "total", "bce", "sb_ece", "mmd" (lists of per-epoch losses).
    """
    torch.manual_seed(seed)
    np.random.seed(seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # 1. Fit scaler on English data
    scaler = StandardScaler()
    X_en_s = scaler.fit_transform(X_en)

    # 2. Train sklearn LR as initialization
    sklearn_C = 1.0 / l2_weight if l2_weight > 0 else 1e6
    sklearn_lr = LogisticRegression(
        C=sklearn_C, penalty="l2", solver="lbfgs", max_iter=2000, random_state=seed,
    )
    sklearn_lr.fit(X_en_s, y_en)

    # 3. Initialize CaCLRProbe
    if init_from_sklearn:
        probe = CaCLRProbe.from_sklearn(sklearn_lr, scaler, l2_weight=l2_weight)
    else:
        probe = CaCLRProbe(X_en_s.shape[1], l2_weight=l2_weight)
    probe = probe.to(device)

    # Convert data to tensors
    X_en_t = torch.from_numpy(X_en_s).float().to(device)
    y_en_t = torch.from_numpy(y_en.astype(np.float32)).to(device)

    tgt_tensors = {}
    for lang, (X_tgt, y_tgt) in X_tgt_dict.items():
        X_tgt_s = scaler.transform(X_tgt)
        tgt_tensors[lang] = (
            torch.from_numpy(X_tgt_s).float().to(device),
            torch.from_numpy(y_tgt.astype(np.float32)).to(device),
        )

    # 4. Fine-tune with CaCLR loss
    optimizer = torch.optim.Adam(probe.parameters(), lr=lr)
    history = {"total": [], "bce": [], "sb_ece": [], "mmd": [], "l2": []}

    for epoch in range(epochs):
        probe.train()
        optimizer.zero_grad()

        logits_en = probe(X_en_t)
        probs_en = torch.sigmoid(logits_en)

        loss_bce = bce_loss(logits_en, y_en_t)
        loss_sb_ece = sb_ece_loss(probs_en, y_en_t)
        loss_l2 = probe.l2_reg()

        # MMD: average over all target languages
        loss_mmd = torch.tensor(0.0, device=device)
        if beta > 0 and len(tgt_tensors) > 0:
            # Note: linear probe logits are 1-D, so MMD operates in a 1-dimensional space.
            # This limits MMD's ability to capture complex distributional differences.
            # This is a design trade-off, not a bug — observe in experiments and discuss in paper.
            mmd_terms = []
            for lang, (X_tgt_t, _) in tgt_tensors.items():
                n_sub = min(512, X_en_t.shape[0], X_tgt_t.shape[0])
                idx_en = torch.randperm(X_en_t.shape[0], device=device)[:n_sub]
                idx_tgt = torch.randperm(X_tgt_t.shape[0], device=device)[:n_sub]
                logits_en_sub = probe(X_en_t[idx_en])
                logits_tgt_sub = probe(X_tgt_t[idx_tgt])
                mmd_terms.append(mmd_loss(logits_en_sub.unsqueeze(1), logits_tgt_sub.unsqueeze(1)))
            loss_mmd = torch.stack(mmd_terms).mean()

        total = loss_bce + alpha * loss_sb_ece + beta * loss_mmd + loss_l2
        total.backward()
        optimizer.step()

        history["total"].append(total.item())
        history["bce"].append(loss_bce.item())
        history["sb_ece"].append(loss_sb_ece.item())
        history["mmd"].append(loss_mmd.item())
        history["l2"].append(loss_l2.item())

        if verbose and (epoch + 1) % max(1, epochs // 10) == 0:
            print(f"  epoch {epoch+1:>4d}/{epochs}  "
                  f"total={total.item():.4f}  bce={loss_bce.item():.4f}  "
                  f"sb_ece={loss_sb_ece.item():.4f}  mmd={loss_mmd.item():.4f}")

    probe = probe.cpu().eval()
    return probe, scaler, history


# ---------------------------------------------------------------------------
# Evaluation helper (quick validation during sweep)
# ---------------------------------------------------------------------------

def compute_ece(probs, labels, n_bins=10):
    """Histogram-based ECE (numpy, matches train_probe.py)."""
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


def quick_eval(probe, scaler, X, y):
    """AUROC + ECE + Brier on held-out data."""
    X_s = scaler.transform(X)
    probs = probe.predict_proba(X_s)[:, 1]
    logits = probe.decision_function(X_s)
    if len(np.unique(y)) < 2:
        return None, None, None
    return roc_auc_score(y, logits), compute_ece(probs, y), brier_score_loss(y, probs)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(description="CaCLR probe training")
    p.add_argument("--activations_dir", default="./activations")
    p.add_argument("--output_dir", default="./probes_caclr")
    p.add_argument("--layer", type=int, required=True,
                   help="Layer index to train on")
    p.add_argument("--languages", nargs="+", default=["zh", "ar", "hi", "sw", "ko"],
                   help="Target languages for MMD consistency loss")
    p.add_argument("--alpha", type=float, default=1.0,
                   help="SB-ECE calibration loss weight")
    p.add_argument("--beta", type=float, default=0.1,
                   help="MMD consistency loss weight")
    p.add_argument("--alpha_sweep", type=str, default=None,
                   help="Comma-separated alpha values for grid search "
                        "(e.g., '0.01,0.1,1.0,10.0')")
    p.add_argument("--beta_sweep", type=str, default=None,
                   help="Comma-separated beta values for grid search")
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--epochs", type=int, default=100)
    p.add_argument("--l2_weight", type=float, default=1.0)
    p.add_argument("--test_size", type=float, default=0.2,
                   help="English held-out fraction for sweep selection")
    p.add_argument("--ece_weight", type=float, default=0.1,
                   help="Weight for ECE penalty in sweep selection: score = auroc - ece_weight * ece")
    p.add_argument("--seed", type=int, default=42)
    return p.parse_args()


def main():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    # Load English activations
    en_path = os.path.join(args.activations_dir, f"layer{args.layer}_en.pt")
    en_data = torch.load(en_path, weights_only=True)
    X_en = en_data["activations"].numpy()
    y_en = en_data["labels"].numpy()
    print(f"English data: {X_en.shape[0]} samples, dim={X_en.shape[1]}")

    # Load target language activations
    X_tgt_dict = {}
    for lang in args.languages:
        tgt_path = os.path.join(args.activations_dir, f"layer{args.layer}_{lang}.pt")
        if not os.path.exists(tgt_path):
            print(f"  [SKIP] {tgt_path} not found")
            continue
        tgt_data = torch.load(tgt_path, weights_only=True)
        X_tgt_dict[lang] = (tgt_data["activations"].numpy(), tgt_data["labels"].numpy())
        print(f"  {lang}: {X_tgt_dict[lang][0].shape[0]} samples")

    # Determine if sweep mode
    sweep_mode = args.alpha_sweep is not None or args.beta_sweep is not None
    alphas = [float(v) for v in args.alpha_sweep.split(",")] if args.alpha_sweep else [args.alpha]
    betas = [float(v) for v in args.beta_sweep.split(",")] if args.beta_sweep else [args.beta]

    if sweep_mode:
        # Hold out English validation set for selecting best (alpha, beta)
        X_train, X_val, y_train, y_val = train_test_split(
            X_en, y_en, test_size=args.test_size, random_state=args.seed, stratify=y_en,
        )
        print(f"\nSweep mode: {len(alphas)} alphas × {len(betas)} betas = {len(alphas)*len(betas)} runs")
        print(f"Train: {len(y_train)}, Val: {len(y_val)}")
        print(f"{'alpha':>8s} {'beta':>8s} {'AUROC':>7s} {'ECE':>7s} {'Brier':>7s}")
        print("-" * 42)

        best_score = -float("inf")
        best_result = None

        for a, b in product(alphas, betas):
            probe, scaler, history = train_caclr(
                X_train, y_train, X_tgt_dict,
                alpha=a, beta=b, lr=args.lr, epochs=args.epochs,
                l2_weight=args.l2_weight, seed=args.seed, verbose=False,
            )
            auroc, ece, brier = quick_eval(probe, scaler, X_val, y_val)
            score = (auroc or 0.0) - args.ece_weight * (ece or 1.0)
            print(f"{a:>8.3f} {b:>8.4f} {auroc or 0:>7.4f} {ece or 0:>7.4f} {brier or 0:>7.4f}"
                  f"{'  *' if score > best_score else ''}")

            if score > best_score:
                best_score = score
                best_result = {
                    "probe": probe, "scaler": scaler, "alpha": a, "beta": b,
                    "history": history, "val_auroc": auroc, "val_ece": ece, "val_brier": brier,
                }

        # Retrain best on full English data
        print(f"\nBest: alpha={best_result['alpha']}, beta={best_result['beta']} "
              f"(val AUROC={best_result['val_auroc']:.4f}, ECE={best_result['val_ece']:.4f})")
        print("Retraining on full English data...")
        probe, scaler, history = train_caclr(
            X_en, y_en, X_tgt_dict,
            alpha=best_result["alpha"], beta=best_result["beta"],
            lr=args.lr, epochs=args.epochs, l2_weight=args.l2_weight,
            seed=args.seed, verbose=True,
        )
        save_dict = {
            "model": probe, "scaler": scaler,
            "alpha": best_result["alpha"], "beta": best_result["beta"],
            "history": history,
            "sweep_best": {"val_auroc": best_result["val_auroc"],
                           "val_ece": best_result["val_ece"],
                           "val_brier": best_result["val_brier"]},
        }
    else:
        # Single run
        probe, scaler, history = train_caclr(
            X_en, y_en, X_tgt_dict,
            alpha=args.alpha, beta=args.beta, lr=args.lr, epochs=args.epochs,
            l2_weight=args.l2_weight, seed=args.seed, verbose=True,
        )
        save_dict = {
            "model": probe, "scaler": scaler,
            "alpha": args.alpha, "beta": args.beta,
            "history": history,
        }

    # Save probe (compatible with transfer_eval.py)
    out_path = os.path.join(args.output_dir, f"probe_layer{args.layer}.pkl")
    with open(out_path, "wb") as f:
        pickle.dump(save_dict, f)
    print(f"\nProbe saved to {out_path}")


if __name__ == "__main__":
    main()

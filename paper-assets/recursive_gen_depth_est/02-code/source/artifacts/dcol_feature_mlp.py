"""
Feature-based DCOL (Depth Contrastive Ordinal Learning) training framework.

Input:  JSONL/CSV files with 19-dim statistical features + depth label (0-3)
Output: Trained MLP checkpoint, evaluation metrics, embedding visualizations

Architecture:
  Encoder:     MLP  19 -> hidden_dim(128) -> 64,  ReLU + BatchNorm + Dropout
  Proj head:   64 -> proj_dim(32),  L2-normalized (contrastive space)
  Class head:  64 -> 4  (depth classification)

Loss (Eq.1 — Dream D002 hard constraint):
  L_DCOL = L_attractive + L_repulsive + lambda * L_CE

Dependencies: torch, sklearn, numpy, pandas, matplotlib
"""

import argparse
import json
import logging
import os
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, Sampler
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report, roc_auc_score,
)
from sklearn.preprocessing import StandardScaler

logger = logging.getLogger(__name__)

# ── Feature schema (matches features_all.jsonl from MVP extraction) ──────────
FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]
NUM_FEATURES = len(FEATURE_NAMES)  # 19


# ═══════════════════════════════════════════════════════════════════════════════
# Data loading
# ═══════════════════════════════════════════════════════════════════════════════

def load_features_file(path: str) -> pd.DataFrame:
    """Load a single features file (JSONL or CSV). Returns DataFrame with feature columns + 'depth'."""
    path = str(path)
    if path.endswith(".csv"):
        df = pd.read_csv(path)
    else:
        records = []
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(json.loads(line))
        df = pd.DataFrame(records)

    required = set(FEATURE_NAMES) | {"depth"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns in {path}: {missing}")
    return df[FEATURE_NAMES + ["depth"]]


def load_data(data_dirs: list[str]) -> pd.DataFrame:
    """Load and concatenate feature files from multiple paths."""
    frames = []
    for p in data_dirs:
        df = load_features_file(p)
        logger.info(f"  Loaded {len(df)} samples from {p}")
        frames.append(df)
    combined = pd.concat(frames, ignore_index=True)
    logger.info(f"Total: {len(combined)} samples, depth distribution: "
                f"{dict(combined['depth'].value_counts().sort_index())}")
    return combined


# ═══════════════════════════════════════════════════════════════════════════════
# Dataset & Sampler
# ═══════════════════════════════════════════════════════════════════════════════

class FeatureDataset(Dataset):
    def __init__(self, features: np.ndarray, labels: np.ndarray):
        self.features = torch.tensor(features, dtype=torch.float32)
        self.labels = torch.tensor(labels, dtype=torch.long)
        self.depth_to_indices = defaultdict(list)
        for i, y in enumerate(labels):
            self.depth_to_indices[int(y)].append(i)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.features[idx], self.labels[idx]


class BalancedDepthSampler(Sampler):
    """Each batch has equal samples per depth for valid contrastive pairs."""

    def __init__(self, dataset: FeatureDataset, batch_size: int):
        self.dataset = dataset
        self.num_depths = len(dataset.depth_to_indices)
        self.per_depth = max(1, batch_size // self.num_depths)
        self.batch_size = self.per_depth * self.num_depths

    def __iter__(self):
        depth_indices = {
            d: np.random.permutation(idx).tolist()
            for d, idx in self.dataset.depth_to_indices.items()
        }
        n_batches = min(len(v) // self.per_depth for v in depth_indices.values())
        for b in range(n_batches):
            batch = []
            for d in sorted(depth_indices):
                batch.extend(depth_indices[d][b * self.per_depth:(b + 1) * self.per_depth])
            yield batch

    def __len__(self):
        return min(len(v) // self.per_depth for v in self.dataset.depth_to_indices.values())


# ═══════════════════════════════════════════════════════════════════════════════
# Model
# ═══════════════════════════════════════════════════════════════════════════════

class DCOLFeatureModel(nn.Module):
    """
    Feature-based DCOL model.

    Forward pass:
      x (B, 19) -> encoder -> h (B, 64) -> proj_head -> z (B, proj_dim)  [contrastive]
                                          -> cls_head  -> logits (B, 4)   [classification]

    Training uses both z (contrastive loss) and logits (CE loss).
    Inference uses only logits.
    """

    def __init__(self, input_dim=19, hidden_dim=128, embed_dim=64, proj_dim=32, num_classes=4, dropout=0.3):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, embed_dim),
            nn.BatchNorm1d(embed_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
        )
        self.proj_head = nn.Sequential(
            nn.Linear(embed_dim, proj_dim),
        )
        self.cls_head = nn.Linear(embed_dim, num_classes)

    def forward(self, x):
        h = self.encoder(x)
        z = F.normalize(self.proj_head(h), p=2, dim=-1)
        logits = self.cls_head(h)
        return z, logits

    def predict(self, x):
        h = self.encoder(x)
        return self.cls_head(h)


# ═══════════════════════════════════════════════════════════════════════════════
# Loss: Multi-margin N-pair Contrastive Ordinal Loss (Eq.1)
# ═══════════════════════════════════════════════════════════════════════════════

class DCOLLoss(nn.Module):
    """
    Multi-margin N-pair contrastive ordinal loss with cross-entropy.

    ┌──────────────────────────────────────────────────────────────────────────┐
    │ Eq.1  L_DCOL = L_attractive + L_repulsive + λ · L_CE                   │
    │                                                                          │
    │ Let f(x) = projection head output (L2-normalized),                       │
    │     y_i   = depth label of sample i,                                     │
    │     d_ij  = |y_i - y_j| (ordinal distance between depths).              │
    │                                                                          │
    │ Positive pairs P = {(i,j) : y_i = y_j}                                  │
    │ Negative pairs N = {(i,j) : y_i ≠ y_j}                                  │
    │                                                                          │
    │ Margin functions (linear in ordinal distance):                           │
    │   m_pos(d) = α · d    (for same-depth pairs, d=0 → margin=0)            │
    │   m_neg(d) = β · d    (depth gap ↑ → required separation ↑)             │
    │                                                                          │
    │ L_attractive = (1/|P|) Σ_{(i,j)∈P} max(0, ‖f(x_i)-f(x_j)‖² - m_pos)  │
    │             = (1/|P|) Σ_{(i,j)∈P} max(0, ‖f(x_i)-f(x_j)‖²)           │
    │             [since d=0 for positive pairs, m_pos(0)=0]                   │
    │                                                                          │
    │ L_repulsive = (1/|N|) Σ_{(i,j)∈N} max(0, β·d_ij - ‖f(x_i)-f(x_j)‖²) │
    │             [push apart: penalty if distance < required margin]          │
    │                                                                          │
    │ L_CE = standard cross-entropy on classification logits                   │
    │                                                                          │
    │ Key insight: ordinal structure is encoded through β·d — pairs with       │
    │ larger depth difference must be pushed further apart. This makes the     │
    │ embedding space preserve ordinal topology, not just class boundaries.    │
    └──────────────────────────────────────────────────────────────────────────┘

    Args:
        alpha: positive pair margin scale (default 0.1, but m_pos(0)=0 always)
        beta:  negative pair margin scale (default 1.0)
        lambda_ce: weight for CE loss component
    """

    def __init__(self, alpha=0.1, beta=1.0, lambda_ce=1.0):
        super().__init__()
        self.alpha = alpha
        self.beta = beta
        self.lambda_ce = lambda_ce
        self.ce = nn.CrossEntropyLoss()

    def forward(self, z, logits, labels):
        """
        Args:
            z:      (B, proj_dim) L2-normalized projection embeddings
            logits: (B, 4)        classification logits
            labels: (B,)          depth labels in {0,1,2,3}
        Returns:
            total_loss, dict with component losses
        """
        B = z.size(0)

        # Pairwise squared Euclidean distances: ‖f(x_i) - f(x_j)‖²
        # For L2-normalized vectors: ‖a-b‖² = 2 - 2·a·b
        dist_sq = 2.0 - 2.0 * torch.mm(z, z.t())  # (B, B)

        # Ordinal distance matrix: d_ij = |y_i - y_j|
        labels_float = labels.float()
        ord_dist = torch.abs(labels_float.unsqueeze(1) - labels_float.unsqueeze(0))  # (B, B)

        # Masks (exclude self-pairs via diagonal mask)
        diag_mask = ~torch.eye(B, dtype=torch.bool, device=z.device)
        pos_mask = (ord_dist == 0) & diag_mask   # same depth, different sample
        neg_mask = (ord_dist > 0) & diag_mask     # different depth

        # L_attractive: same-depth pairs should be close
        # m_pos(d=0) = alpha * 0 = 0, so: max(0, ‖f_i - f_j‖² - 0) = ‖f_i - f_j‖²
        # But we still use the general form for code clarity
        m_pos = self.alpha * ord_dist  # (B, B), all zeros for pos_mask entries
        if pos_mask.any():
            l_attract = torch.clamp(dist_sq[pos_mask] - m_pos[pos_mask], min=0).mean()
        else:
            l_attract = torch.tensor(0.0, device=z.device)

        # L_repulsive: different-depth pairs should be separated by at least β·d_ij
        m_neg = self.beta * ord_dist  # (B, B)
        if neg_mask.any():
            l_repulse = torch.clamp(m_neg[neg_mask] - dist_sq[neg_mask], min=0).mean()
        else:
            l_repulse = torch.tensor(0.0, device=z.device)

        l_ce = self.ce(logits, labels)

        total = l_attract + l_repulse + self.lambda_ce * l_ce

        return total, {
            "l_attract": l_attract.item(),
            "l_repulse": l_repulse.item(),
            "l_ce": l_ce.item(),
            "total": total.item(),
        }


# ═══════════════════════════════════════════════════════════════════════════════
# Training loop
# ═══════════════════════════════════════════════════════════════════════════════

def train_one_epoch(model, loader, criterion, optimizer, scheduler, device):
    model.train()
    total_loss, total_correct, total_n = 0.0, 0, 0
    loss_components = defaultdict(float)

    for features, labels in loader:
        features, labels = features.to(device), labels.to(device)

        z, logits = model(features)
        loss, comps = criterion(z, logits, labels)

        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()
        if scheduler is not None:
            scheduler.step()

        bs = labels.size(0)
        total_loss += loss.item() * bs
        total_correct += (logits.argmax(1) == labels).sum().item()
        total_n += bs
        for k, v in comps.items():
            loss_components[k] += v * bs

    return {
        "loss": total_loss / total_n,
        "accuracy": total_correct / total_n,
        **{k: v / total_n for k, v in loss_components.items()},
    }


@torch.no_grad()
def evaluate(model, loader, criterion, device):
    model.eval()
    total_loss, total_correct, total_n = 0.0, 0, 0
    all_preds, all_labels, all_probs, all_embeds = [], [], [], []

    for features, labels in loader:
        features, labels = features.to(device), labels.to(device)
        z, logits = model(features)
        loss, _ = criterion(z, logits, labels)

        bs = labels.size(0)
        total_loss += loss.item() * bs
        total_correct += (logits.argmax(1) == labels).sum().item()
        total_n += bs

        all_preds.append(logits.argmax(1).cpu().numpy())
        all_labels.append(labels.cpu().numpy())
        all_probs.append(F.softmax(logits, dim=-1).cpu().numpy())
        all_embeds.append(z.cpu().numpy())

    return {
        "loss": total_loss / total_n,
        "accuracy": total_correct / total_n,
        "preds": np.concatenate(all_preds),
        "labels": np.concatenate(all_labels),
        "probs": np.concatenate(all_probs),
        "embeds": np.concatenate(all_embeds),
    }


# ═══════════════════════════════════════════════════════════════════════════════
# Evaluation metrics
# ═══════════════════════════════════════════════════════════════════════════════

def bootstrap_accuracy(labels, preds, n_boot=1000, ci=0.95, seed=42):
    """4-class accuracy with bootstrap confidence interval."""
    rng = np.random.RandomState(seed)
    n = len(labels)
    accs = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        accs.append(accuracy_score(labels[idx], preds[idx]))
    accs = np.sort(accs)
    lo = accs[int((1 - ci) / 2 * n_boot)]
    hi = accs[int((1 + ci) / 2 * n_boot)]
    return accuracy_score(labels, preds), lo, hi


def pairwise_auc(labels, probs, d1, d2):
    """AUC for binary distinction between depth d1 vs d2."""
    mask = np.isin(labels, [d1, d2])
    if mask.sum() < 2:
        return None
    yt = (labels[mask] == d2).astype(int)
    if len(np.unique(yt)) < 2:
        return None
    yp = probs[mask, d2]
    return float(roc_auc_score(yt, yp))


def full_report(labels, preds, probs):
    """Comprehensive evaluation metrics."""
    acc_4, lo, hi = bootstrap_accuracy(labels, preds)
    report = {
        "accuracy_4class": round(acc_4, 4),
        "accuracy_95ci": [round(lo, 4), round(hi, 4)],
    }

    # 3-class accuracy (d1-d3 only)
    mask_3 = labels > 0
    if mask_3.any():
        report["accuracy_3class"] = round(accuracy_score(labels[mask_3], preds[mask_3]), 4)

    # Per-class recall
    cm = confusion_matrix(labels, preds, labels=[0, 1, 2, 3])
    per_class_recall = {}
    for d in range(4):
        row_sum = cm[d].sum()
        per_class_recall[f"depth_{d}"] = round(cm[d, d] / row_sum, 4) if row_sum > 0 else 0.0
    report["per_class_recall"] = per_class_recall

    # Pairwise AUC (adjacent pairs + key non-adjacent)
    auc_pairs = {}
    for d1, d2 in [(0, 1), (1, 2), (2, 3), (0, 2), (0, 3), (1, 3)]:
        a = pairwise_auc(labels, probs, d1, d2)
        auc_pairs[f"d{d1}v{d2}"] = round(a, 4) if a is not None else None
    report["pairwise_auc"] = auc_pairs

    # Confusion matrix (raw counts)
    report["confusion_matrix"] = cm.tolist()

    return report


def plot_embeddings(embeds, labels, output_dir, prefix="final"):
    """t-SNE and PCA visualization of contrastive embeddings."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from sklearn.manifold import TSNE
        from sklearn.decomposition import PCA
    except ImportError:
        logger.warning("matplotlib/sklearn not available, skipping embedding plots")
        return

    depth_colors = {0: "#1f77b4", 1: "#ff7f0e", 2: "#2ca02c", 3: "#d62728"}
    depth_labels = {0: "depth-0", 1: "depth-1", 2: "depth-2", 3: "depth-3"}

    for method_name, reducer in [("tsne", TSNE(n_components=2, random_state=42, perplexity=30)),
                                  ("pca", PCA(n_components=2))]:
        coords = reducer.fit_transform(embeds)
        fig, ax = plt.subplots(figsize=(8, 6))
        for d in range(4):
            mask = labels == d
            ax.scatter(coords[mask, 0], coords[mask, 1],
                       c=depth_colors[d], label=depth_labels[d],
                       alpha=0.5, s=10, edgecolors="none")
        ax.legend(fontsize=10)
        ax.set_title(f"DCOL Embeddings ({method_name.upper()})")
        ax.set_xlabel(f"{method_name.upper()} dim 1")
        ax.set_ylabel(f"{method_name.upper()} dim 2")
        save_path = os.path.join(output_dir, f"{prefix}_embed_{method_name}.png")
        plt.tight_layout()
        plt.savefig(save_path, dpi=150)
        plt.close()
        logger.info(f"Saved {method_name.upper()} plot to {save_path}")


def plot_confusion_matrix(labels, preds, output_dir, prefix="final"):
    """Save confusion matrix heatmap."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return

    cm = confusion_matrix(labels, preds, labels=[0, 1, 2, 3])
    cm_pct = cm.astype(float) / cm.sum(axis=1, keepdims=True) * 100

    fig, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(cm_pct, cmap="Blues", vmin=0, vmax=100)
    tick_labels = [f"depth-{d}" for d in range(4)]
    ax.set_xticks(range(4))
    ax.set_yticks(range(4))
    ax.set_xticklabels(tick_labels)
    ax.set_yticklabels(tick_labels)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("True")
    ax.set_title("DCOL Feature-based Confusion Matrix")

    for i in range(4):
        for j in range(4):
            color = "white" if cm_pct[i, j] > 50 else "black"
            ax.text(j, i, f"{cm[i, j]}\n({cm_pct[i, j]:.1f}%)",
                    ha="center", va="center", color=color, fontsize=10)

    plt.colorbar(im, ax=ax)
    plt.tight_layout()
    save_path = os.path.join(output_dir, f"{prefix}_confusion_matrix.png")
    plt.savefig(save_path, dpi=150)
    plt.close()
    logger.info(f"Saved confusion matrix to {save_path}")


# ═══════════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════════

def parse_args():
    p = argparse.ArgumentParser(description="Feature-based DCOL training")
    p.add_argument("--data_dirs", nargs="+", required=True,
                   help="Paths to feature files (JSONL or CSV)")
    p.add_argument("--epochs", type=int, default=100)
    p.add_argument("--batch_size", type=int, default=256)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--weight_decay", type=float, default=1e-4)
    p.add_argument("--alpha", type=float, default=0.1,
                   help="Positive pair margin scale (Eq.1)")
    p.add_argument("--beta", type=float, default=1.0,
                   help="Negative pair margin scale (Eq.1)")
    p.add_argument("--lambda_ce", type=float, default=1.0,
                   help="CE loss weight (Eq.1)")
    p.add_argument("--hidden_dim", type=int, default=128)
    p.add_argument("--proj_dim", type=int, default=32)
    p.add_argument("--dropout", type=float, default=0.3)
    p.add_argument("--patience", type=int, default=10)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--output_dir", type=str, default="checkpoints/dcol_feature/")
    p.add_argument("--test_size", type=float, default=0.2)
    return p.parse_args()


def main():
    args = parse_args()
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info(f"Device: {device}")

    # ── Load data ────────────────────────────────────────────────────────────
    df = load_data(args.data_dirs)
    X = df[FEATURE_NAMES].values.astype(np.float32)
    y = df["depth"].values.astype(np.int64)

    # Train/test split (stratified)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=args.test_size, stratify=y, random_state=args.seed
    )
    logger.info(f"Train: {len(X_train)}, Test: {len(X_test)}")

    # Feature standardization (fit on train only)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # ── Datasets & loaders ───────────────────────────────────────────────────
    train_ds = FeatureDataset(X_train, y_train)
    test_ds = FeatureDataset(X_test, y_test)

    train_sampler = BalancedDepthSampler(train_ds, args.batch_size)
    train_loader = DataLoader(train_ds, batch_sampler=train_sampler, num_workers=2, pin_memory=True)
    test_loader = DataLoader(test_ds, batch_size=args.batch_size, shuffle=False, num_workers=2, pin_memory=True)

    # ── Model ────────────────────────────────────────────────────────────────
    model = DCOLFeatureModel(
        input_dim=NUM_FEATURES,
        hidden_dim=args.hidden_dim,
        embed_dim=64,
        proj_dim=args.proj_dim,
        num_classes=4,
        dropout=args.dropout,
    ).to(device)

    n_params = sum(p.numel() for p in model.parameters())
    logger.info(f"Model parameters: {n_params:,}")

    # ── Loss, optimizer, scheduler ───────────────────────────────────────────
    criterion = DCOLLoss(alpha=args.alpha, beta=args.beta, lambda_ce=args.lambda_ce)
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    total_steps = len(train_loader) * args.epochs
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=total_steps)

    # ── Training ─────────────────────────────────────────────────────────────
    os.makedirs(args.output_dir, exist_ok=True)

    best_val_loss = float("inf")
    best_val_acc = 0.0
    patience_cnt = 0

    for epoch in range(1, args.epochs + 1):
        t0 = time.time()
        train_m = train_one_epoch(model, train_loader, criterion, optimizer, scheduler, device)
        val_m = evaluate(model, test_loader, criterion, device)
        elapsed = time.time() - t0

        logger.info(
            f"Epoch {epoch:3d}/{args.epochs} | "
            f"Train loss={train_m['loss']:.4f} acc={train_m['accuracy']:.4f} "
            f"[attr={train_m.get('l_attract', 0):.4f} rep={train_m.get('l_repulse', 0):.4f} "
            f"ce={train_m.get('l_ce', 0):.4f}] | "
            f"Val loss={val_m['loss']:.4f} acc={val_m['accuracy']:.4f} | {elapsed:.1f}s"
        )

        # Early stopping on val loss
        if val_m["loss"] < best_val_loss:
            best_val_loss = val_m["loss"]
            best_val_acc = val_m["accuracy"]
            patience_cnt = 0
            ckpt_path = os.path.join(args.output_dir, "best_model.pt")
            torch.save({
                "epoch": epoch,
                "model_state_dict": model.state_dict(),
                "scaler_mean": scaler.mean_.tolist(),
                "scaler_scale": scaler.scale_.tolist(),
                "val_loss": best_val_loss,
                "val_accuracy": best_val_acc,
                "args": vars(args),
                "feature_names": FEATURE_NAMES,
            }, ckpt_path)
            logger.info(f"  *** Best model saved (val_loss={best_val_loss:.4f}, val_acc={best_val_acc:.4f})")
        else:
            patience_cnt += 1
            if patience_cnt >= args.patience:
                logger.info(f"Early stopping at epoch {epoch} (patience={args.patience})")
                break

    # ── Final evaluation ─────────────────────────────────────────────────────
    logger.info(f"\n{'='*60}\nFinal evaluation on test set")

    ckpt_path = os.path.join(args.output_dir, "best_model.pt")
    if os.path.exists(ckpt_path):
        ckpt = torch.load(ckpt_path, map_location=device, weights_only=True)
        model.load_state_dict(ckpt["model_state_dict"])
        logger.info(f"Loaded best checkpoint from epoch {ckpt['epoch']}")

    final = evaluate(model, test_loader, criterion, device)
    report = full_report(final["labels"], final["preds"], final["probs"])

    logger.info(f"4-class accuracy: {report['accuracy_4class']:.4f} "
                f"95% CI: [{report['accuracy_95ci'][0]:.4f}, {report['accuracy_95ci'][1]:.4f}]")
    if "accuracy_3class" in report:
        logger.info(f"3-class accuracy (d1-d3): {report['accuracy_3class']:.4f}")
    logger.info(f"Per-class recall: {report['per_class_recall']}")
    logger.info(f"Pairwise AUC: {report['pairwise_auc']}")

    cr = classification_report(
        final["labels"], final["preds"],
        target_names=[f"depth-{d}" for d in range(4)],
        zero_division=0,
    )
    logger.info(f"\n{cr}")

    # RF baseline comparison
    rf_acc = 0.7815
    delta = report["accuracy_4class"] - rf_acc
    logger.info(f"DCOL={report['accuracy_4class']*100:.1f}% vs RF={rf_acc*100:.1f}% (delta={delta*100:+.1f}pp)")

    # Plots
    plot_embeddings(final["embeds"], final["labels"], args.output_dir)
    plot_confusion_matrix(final["labels"], final["preds"], args.output_dir)

    # Save results
    report["rf_baseline"] = rf_acc
    report["improvement_over_rf"] = round(delta, 4)
    report["best_epoch"] = ckpt.get("epoch", -1) if os.path.exists(ckpt_path) else -1
    results_path = os.path.join(args.output_dir, "results.json")
    with open(results_path, "w") as f:
        json.dump(report, f, indent=2)
    logger.info(f"Results saved to {results_path}")


if __name__ == "__main__":
    main()

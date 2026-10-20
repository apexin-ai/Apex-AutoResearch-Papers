#!/usr/bin/env python3
"""Train GRU probe with Supervised Contrastive Loss auxiliary objective.

Total loss = BCE_loss + lambda * SupCon_loss
SupCon applied on GRU last-layer hidden state (before classifier).
"""

import argparse
import json
import random
import sys
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).parent))
from probe_model import ProgressProbe, WindowDataset, collate_fn, split_by_instance


class SupConLoss(nn.Module):
    """Supervised Contrastive Loss (Khosla et al., 2020).

    Pulls same-class representations together, pushes different-class apart.
    """

    def __init__(self, temperature: float = 0.07):
        super().__init__()
        self.temperature = temperature

    def forward(self, features: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
        """
        Args:
            features: (batch, hidden_dim) - will be L2-normalized internally
            labels: (batch,) - binary labels {0, 1}
        Returns:
            scalar loss
        """
        device = features.device
        batch_size = features.shape[0]
        if batch_size <= 1:
            return torch.tensor(0.0, device=device, requires_grad=True)

        features = F.normalize(features, dim=1)
        similarity = torch.mm(features, features.t()) / self.temperature

        # Mask: 1 where labels match (positive pairs), 0 on diagonal
        labels = labels.view(-1, 1)
        mask = torch.eq(labels, labels.t()).float().to(device)
        mask.fill_diagonal_(0)

        # Check we have at least one positive pair
        if mask.sum() == 0:
            return torch.tensor(0.0, device=device, requires_grad=True)

        # For numerical stability, subtract max from logits
        logits_max, _ = similarity.max(dim=1, keepdim=True)
        logits = similarity - logits_max.detach()

        # Exclude self-contrast
        logits_mask = torch.ones_like(mask)
        logits_mask.fill_diagonal_(0)

        # exp(sim) for all pairs except self
        exp_logits = torch.exp(logits) * logits_mask
        log_prob = logits - torch.log(exp_logits.sum(dim=1, keepdim=True) + 1e-12)

        # Mean log-probability over positive pairs
        mean_log_prob = (mask * log_prob).sum(dim=1) / (mask.sum(dim=1) + 1e-12)
        loss = -mean_log_prob.mean()
        return loss


def forward_with_hidden(model: ProgressProbe, x: torch.Tensor, lengths: torch.Tensor = None):
    """Get both logits and hidden state from ProgressProbe."""
    if lengths is not None:
        x = nn.utils.rnn.pack_padded_sequence(x, lengths.cpu(), batch_first=True, enforce_sorted=False)
    _, hidden = model.gru(x)
    h = hidden[-1]  # (batch, hidden_size)
    logits = model.classifier(h).squeeze(-1)
    return logits, h


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def compute_metrics(labels: list[int], preds: list[int]) -> dict:
    return {
        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
        "accuracy": accuracy_score(labels, preds),
        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
    }


class EarlyStopping:
    def __init__(self, patience: int = 5):
        self.patience = patience
        self.counter = 0
        self.best_score = None
        self.should_stop = False

    def step(self, score: float) -> bool:
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            self.counter = 0
            return True
        self.counter += 1
        if self.counter >= self.patience:
            self.should_stop = True
        return False


@torch.no_grad()
def evaluate_epoch(model: nn.Module, loader: DataLoader, device: str) -> dict:
    model.eval()
    all_labels, all_preds = [], []
    for padded, labels, lengths in loader:
        logits, _ = forward_with_hidden(model, padded.to(device), lengths)
        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
        all_labels.extend(labels.long().tolist())
        all_preds.extend(preds.tolist())
    return compute_metrics(all_labels, all_preds)


@torch.no_grad()
def compute_separability(model: nn.Module, loader: DataLoader, device: str) -> dict:
    """Compute inter-class / intra-class cosine distance ratio on hidden states."""
    model.eval()
    all_h, all_labels = [], []
    for padded, labels, lengths in loader:
        _, h = forward_with_hidden(model, padded.to(device), lengths)
        all_h.append(h.cpu())
        all_labels.append(labels)

    all_h = F.normalize(torch.cat(all_h, dim=0), dim=1)
    all_labels = torch.cat(all_labels, dim=0)

    mask_0 = all_labels == 0
    mask_1 = all_labels == 1
    h0 = all_h[mask_0]
    h1 = all_h[mask_1]

    def mean_pairwise_cosine(feats: torch.Tensor, max_samples: int = 2000) -> float:
        if len(feats) < 2:
            return 0.0
        if len(feats) > max_samples:
            idx = torch.randperm(len(feats))[:max_samples]
            feats = feats[idx]
        sim = torch.mm(feats, feats.t())
        n = len(feats)
        mask = torch.ones(n, n, dtype=torch.bool)
        mask.fill_diagonal_(False)
        return sim[mask].mean().item()

    intra_0 = mean_pairwise_cosine(h0)
    intra_1 = mean_pairwise_cosine(h1)
    intra_mean = (intra_0 + intra_1) / 2

    # Inter-class: sample from both
    max_inter = 2000
    if len(h0) > max_inter:
        h0_s = h0[torch.randperm(len(h0))[:max_inter]]
    else:
        h0_s = h0
    if len(h1) > max_inter:
        h1_s = h1[torch.randperm(len(h1))[:max_inter]]
    else:
        h1_s = h1
    inter_sim = torch.mm(h0_s, h1_s.t()).mean().item()

    # Separability = (1 - inter_sim) / (1 - intra_mean + 1e-8) -- cosine distance ratio
    # Higher = better separation
    sep_ratio = (1 - inter_sim) / (1 - intra_mean + 1e-8)

    return {
        "intra_class_sim_stag": round(intra_0, 4),
        "intra_class_sim_prog": round(intra_1, 4),
        "intra_class_sim_mean": round(intra_mean, 4),
        "inter_class_sim": round(inter_sim, 4),
        "separability_ratio": round(sep_ratio, 4),
    }


def run_single(args, supcon_lambda: float):
    """Run one training experiment with given lambda."""
    set_seed(args.seed)
    tag = f"lambda_{supcon_lambda}"
    output_dir = Path(args.output_dir) / tag
    output_dir.mkdir(parents=True, exist_ok=True)
    device = args.device

    # Load data
    data_path = Path(args.data_dir) / "embeddings.pt"
    data = torch.load(data_path, weights_only=False)
    embeddings = data["embeddings"]
    labels = data["labels"]
    instance_ids = data["instance_ids"]
    confidences = data.get("confidences", [1] * len(labels))
    embed_dim = data["embed_dim"]

    # Confidence filter
    if args.min_confidence > 0:
        keep = [i for i, c in enumerate(confidences) if c >= args.min_confidence]
        print(f"[{tag}] Confidence filter: {len(keep)}/{len(labels)} windows (conf>={args.min_confidence})")
        embeddings = [embeddings[i] for i in keep]
        labels = [labels[i] for i in keep]
        instance_ids = [instance_ids[i] for i in keep]
        confidences = [confidences[i] for i in keep]

    # Use same split as probe_001
    if args.split_info:
        with open(args.split_info) as f:
            split_data = json.load(f)
        train_idx = split_data["train_indices"]
        val_idx = split_data["val_indices"]
        test_idx = split_data["test_indices"]
    else:
        train_idx, val_idx, test_idx = split_by_instance(instance_ids, seed=args.seed)

    def make_dataset(indices):
        return WindowDataset([embeddings[i] for i in indices], [labels[i] for i in indices])

    train_ds = make_dataset(train_idx)
    val_ds = make_dataset(val_idx)
    test_ds = make_dataset(test_idx)

    train_labels = [labels[i] for i in train_idx]
    num_pos = sum(train_labels)
    num_neg = len(train_labels) - num_pos
    pos_weight = torch.tensor([num_neg / max(num_pos, 1)]).to(device)

    print(f"[{tag}] Train: {len(train_ds)} (pos={num_pos}, neg={num_neg}) | Val: {len(val_ds)} | Test: {len(test_ds)}")

    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True, collate_fn=collate_fn)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, collate_fn=collate_fn)
    test_loader = DataLoader(test_ds, batch_size=args.batch_size, collate_fn=collate_fn)

    # Model
    model = ProgressProbe(
        embed_dim=embed_dim,
        hidden_size=args.hidden_size,
        num_layers=args.num_layers,
        dropout=args.dropout,
    ).to(device)

    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    bce_criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    supcon_criterion = SupConLoss(temperature=args.temperature)
    early_stopping = EarlyStopping(patience=args.patience)

    # Training loop
    history = []
    for epoch in range(1, args.epochs + 1):
        model.train()
        total_bce, total_supcon, total_combined, n_samples = 0.0, 0.0, 0.0, 0
        for padded, batch_labels, lengths in train_loader:
            padded = padded.to(device)
            batch_labels = batch_labels.to(device)

            logits, hidden = forward_with_hidden(model, padded, lengths)
            bce_loss = bce_criterion(logits, batch_labels)
            supcon_loss = supcon_criterion(hidden, batch_labels)
            loss = bce_loss + supcon_lambda * supcon_loss

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            bs = len(batch_labels)
            total_bce += bce_loss.item() * bs
            total_supcon += supcon_loss.item() * bs
            total_combined += loss.item() * bs
            n_samples += bs

        avg_bce = total_bce / n_samples
        avg_supcon = total_supcon / n_samples
        avg_combined = total_combined / n_samples
        val_metrics = evaluate_epoch(model, val_loader, device)

        record = {
            "epoch": epoch,
            "train_bce_loss": round(avg_bce, 5),
            "train_supcon_loss": round(avg_supcon, 5),
            "train_combined_loss": round(avg_combined, 5),
            **{f"val_{k}": round(v, 5) for k, v in val_metrics.items()},
        }
        history.append(record)

        is_best = early_stopping.step(val_metrics["macro_f1"])
        marker = " *" if is_best else ""
        print(
            f"  Epoch {epoch:2d} | bce={avg_bce:.4f} supcon={avg_supcon:.4f} combined={avg_combined:.4f} | "
            f"val_F1={val_metrics['macro_f1']:.4f} acc={val_metrics['accuracy']:.4f}{marker}"
        )

        if is_best:
            torch.save(
                {
                    "model_state_dict": model.state_dict(),
                    "embed_dim": embed_dim,
                    "hidden_size": args.hidden_size,
                    "num_layers": args.num_layers,
                    "dropout": args.dropout,
                    "epoch": epoch,
                    "val_macro_f1": val_metrics["macro_f1"],
                    "supcon_lambda": supcon_lambda,
                    "temperature": args.temperature,
                    "args": vars(args),
                },
                output_dir / "best_model.pt",
            )

        if early_stopping.should_stop:
            print(f"  Early stopping at epoch {epoch}")
            break

    # Save history
    with open(output_dir / "train_history.json", "w") as f:
        json.dump(history, f, indent=2)

    # Load best model and evaluate on test
    best_ckpt = torch.load(output_dir / "best_model.pt", weights_only=False)
    model.load_state_dict(best_ckpt["model_state_dict"])
    test_metrics = evaluate_epoch(model, test_loader, device)
    sep_metrics = compute_separability(model, test_loader, device)

    result = {
        "supcon_lambda": supcon_lambda,
        "temperature": args.temperature,
        "best_epoch": best_ckpt["epoch"],
        "best_val_macro_f1": round(early_stopping.best_score, 5),
        "test_metrics": {k: round(v, 5) for k, v in test_metrics.items()},
        "separability": sep_metrics,
    }

    with open(output_dir / "results.json", "w") as f:
        json.dump(result, f, indent=2)

    print(f"\n[{tag}] Test: macro_f1={test_metrics['macro_f1']:.4f} "
          f"f1_stag={test_metrics['f1_stagnation']:.4f} f1_prog={test_metrics['f1_progress']:.4f} "
          f"sep_ratio={sep_metrics['separability_ratio']:.4f}")

    return result


def main():
    parser = argparse.ArgumentParser(description="Train GRU probe with SupCon auxiliary loss")
    parser.add_argument("--data_dir", required=True)
    parser.add_argument("--output_dir", required=True)
    parser.add_argument("--split_info", default=None, help="Path to split_info.json from probe_001")
    parser.add_argument("--lambdas", type=float, nargs="+", default=[0.1, 0.5, 1.0])
    parser.add_argument("--temperature", type=float, default=0.07)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--hidden_size", type=int, default=256)
    parser.add_argument("--num_layers", type=int, default=2)
    parser.add_argument("--dropout", type=float, default=0.1)
    parser.add_argument("--weight_decay", type=float, default=0.01)
    parser.add_argument("--patience", type=int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--min_confidence", type=int, default=2)
    parser.add_argument("--device", default="cuda:0")
    args = parser.parse_args()

    print(f"SupCon Ablation | lambdas={args.lambdas} | tau={args.temperature} | device={args.device}")
    print(f"Data: {args.data_dir} | Output: {args.output_dir}")
    print("=" * 80)

    all_results = []
    for lam in args.lambdas:
        print(f"\n{'='*80}")
        print(f"Training with supcon_lambda={lam}")
        print(f"{'='*80}")
        result = run_single(args, lam)
        all_results.append(result)

    # Also compute separability for baseline (no SupCon) using probe_001 checkpoint
    baseline_ckpt_path = Path(args.data_dir).parent / "checkpoints" / "best_model.pt"
    if baseline_ckpt_path.exists():
        print(f"\n{'='*80}")
        print("Computing separability for baseline (probe_001, no SupCon)")
        print(f"{'='*80}")
        set_seed(args.seed)

        data = torch.load(Path(args.data_dir) / "embeddings.pt", weights_only=False)
        embeddings = data["embeddings"]
        labels = data["labels"]
        confidences = data.get("confidences", [1] * len(labels))
        embed_dim = data["embed_dim"]

        if args.min_confidence > 0:
            keep = [i for i, c in enumerate(confidences) if c >= args.min_confidence]
            embeddings = [embeddings[i] for i in keep]
            labels = [labels[i] for i in keep]

        if args.split_info:
            with open(args.split_info) as f:
                split_data = json.load(f)
            test_idx = split_data["test_indices"]
        else:
            instance_ids = data["instance_ids"]
            if args.min_confidence > 0:
                instance_ids = [instance_ids[i] for i in keep]
            _, _, test_idx = split_by_instance(instance_ids, seed=args.seed)

        test_ds = WindowDataset([embeddings[i] for i in test_idx], [labels[i] for i in test_idx])
        test_loader = DataLoader(test_ds, batch_size=args.batch_size, collate_fn=collate_fn)

        ckpt = torch.load(baseline_ckpt_path, weights_only=False)
        baseline_model = ProgressProbe(
            embed_dim=ckpt["embed_dim"],
            hidden_size=ckpt["hidden_size"],
            num_layers=ckpt["num_layers"],
        ).to(args.device)
        baseline_model.load_state_dict(ckpt["model_state_dict"])

        baseline_sep = compute_separability(baseline_model, test_loader, args.device)
        baseline_test = evaluate_epoch(baseline_model, test_loader, args.device)
        baseline_result = {
            "supcon_lambda": 0.0,
            "test_metrics": {k: round(v, 5) for k, v in baseline_test.items()},
            "separability": baseline_sep,
        }
        all_results.insert(0, baseline_result)
        print(f"Baseline: macro_f1={baseline_test['macro_f1']:.4f} sep_ratio={baseline_sep['separability_ratio']:.4f}")

    # Summary
    summary_path = Path(args.output_dir) / "ablation_summary.json"
    with open(summary_path, "w") as f:
        json.dump(all_results, f, indent=2)

    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    print(f"{'Lambda':>8} | {'macro_f1':>8} | {'f1_stag':>8} | {'f1_prog':>8} | {'acc':>8} | {'sep_ratio':>10}")
    print("-" * 70)
    for r in all_results:
        lam = r["supcon_lambda"]
        tm = r["test_metrics"]
        sep = r.get("separability", {}).get("separability_ratio", "N/A")
        print(f"{lam:>8.1f} | {tm['macro_f1']:>8.4f} | {tm['f1_stagnation']:>8.4f} | "
              f"{tm['f1_progress']:>8.4f} | {tm['accuracy']:>8.4f} | {sep:>10}")

    print(f"\nResults saved to {summary_path}")


if __name__ == "__main__":
    main()

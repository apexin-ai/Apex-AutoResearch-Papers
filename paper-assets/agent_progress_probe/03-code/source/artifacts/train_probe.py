#!/usr/bin/env python3
"""Train the GRU progress probe on pre-computed window embeddings."""

import argparse
import json
import random
import sys
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).parent))
from probe_model import ProgressProbe, WindowDataset, collate_fn, split_by_instance


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
        logits = model(padded.to(device), lengths)
        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
        all_labels.extend(labels.long().tolist())
        all_preds.extend(preds.tolist())
    return compute_metrics(all_labels, all_preds)


def main():
    parser = argparse.ArgumentParser(description="Train GRU progress probe")
    parser.add_argument("--data_dir", required=True, help="Directory containing embeddings.pt")
    parser.add_argument("--output_dir", required=True, help="Output directory for checkpoints")
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--hidden_size", type=int, default=256)
    parser.add_argument("--num_layers", type=int, default=2)
    parser.add_argument("--dropout", type=float, default=0.1)
    parser.add_argument("--weight_decay", type=float, default=0.01)
    parser.add_argument("--patience", type=int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--min_confidence", type=int, default=0, help="Min confidence for training (0=all, 2=high-conf)")
    parser.add_argument("--wandb", action="store_true", help="Enable W&B logging")
    args = parser.parse_args()

    set_seed(args.seed)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Load data
    data_path = Path(args.data_dir) / "embeddings.pt"
    data = torch.load(data_path, weights_only=False)
    embeddings = data["embeddings"]
    labels = data["labels"]
    instance_ids = data["instance_ids"]
    confidences = data.get("confidences", [1] * len(labels))
    embed_dim = data["embed_dim"]

    # Filter by confidence
    if args.min_confidence > 0:
        keep = [i for i, c in enumerate(confidences) if c >= args.min_confidence]
        print(f"Confidence filter: {len(keep)}/{len(labels)} windows with conf>={args.min_confidence}")
        embeddings = [embeddings[i] for i in keep]
        labels = [labels[i] for i in keep]
        instance_ids = [instance_ids[i] for i in keep]
        confidences = [confidences[i] for i in keep]

    # Split
    train_idx, val_idx, test_idx = split_by_instance(instance_ids, seed=args.seed)
    split_info = {
        "train_indices": train_idx,
        "val_indices": val_idx,
        "test_indices": test_idx,
        "seed": args.seed,
        "embed_dim": embed_dim,
        "min_confidence": args.min_confidence,
        "keep_indices": keep if args.min_confidence > 0 else None,
    }
    with open(output_dir / "split_info.json", "w") as f:
        json.dump(split_info, f)

    def make_dataset(indices):
        return WindowDataset([embeddings[i] for i in indices], [labels[i] for i in indices])

    train_ds = make_dataset(train_idx)
    val_ds = make_dataset(val_idx)

    train_labels = [labels[i] for i in train_idx]
    num_pos = sum(train_labels)
    num_neg = len(train_labels) - num_pos
    pos_weight = torch.tensor([num_neg / max(num_pos, 1)]).to(device)

    print(f"Train: {len(train_ds)} (pos={num_pos}, neg={num_neg})")
    print(f"Val:   {len(val_ds)}")
    print(f"Test:  {len(test_idx)}")
    print(f"pos_weight: {pos_weight.item():.3f}")

    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True, collate_fn=collate_fn)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, collate_fn=collate_fn)

    # Model
    model = ProgressProbe(
        embed_dim=embed_dim,
        hidden_size=args.hidden_size,
        num_layers=args.num_layers,
        dropout=args.dropout,
    ).to(device)

    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    early_stopping = EarlyStopping(patience=args.patience)

    # W&B
    if args.wandb:
        import wandb

        wandb.init(project="agent-progress-probe", config=vars(args))

    # Training loop
    history = []
    for epoch in range(1, args.epochs + 1):
        model.train()
        total_loss = 0.0
        n_samples = 0
        for padded, batch_labels, lengths in train_loader:
            padded = padded.to(device)
            batch_labels = batch_labels.to(device)

            logits = model(padded, lengths)
            loss = criterion(logits, batch_labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item() * len(batch_labels)
            n_samples += len(batch_labels)

        avg_loss = total_loss / n_samples
        val_metrics = evaluate_epoch(model, val_loader, device)

        record = {"epoch": epoch, "train_loss": avg_loss, **{f"val_{k}": v for k, v in val_metrics.items()}}
        history.append(record)

        is_best = early_stopping.step(val_metrics["macro_f1"])
        marker = " *" if is_best else ""
        print(
            f"Epoch {epoch:2d} | loss={avg_loss:.4f} | "
            f"val_F1={val_metrics['macro_f1']:.4f} "
            f"acc={val_metrics['accuracy']:.4f}{marker}"
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
                    "args": vars(args),
                },
                output_dir / "best_model.pt",
            )

        if args.wandb:
            import wandb

            wandb.log(record)

        if early_stopping.should_stop:
            print(f"Early stopping at epoch {epoch}")
            break

    # Save history
    with open(output_dir / "train_history.json", "w") as f:
        json.dump(history, f, indent=2)

    print(f"\nBest val macro-F1: {early_stopping.best_score:.4f}")
    print(f"Outputs saved to {output_dir}")


if __name__ == "__main__":
    main()

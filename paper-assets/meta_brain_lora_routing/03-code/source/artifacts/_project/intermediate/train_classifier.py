"""
Train perturbation classifiers on frozen π₀ activations.

Supports 3 modes (6class / 3class / binary), 5-fold cross-validation,
and automated hyperparameter sweep over pooling × activation_source × lr.

Usage:
    # Single run
    python train_classifier.py \
        --data_dir ./activations \
        --mode 6class \
        --activation_source both \
        --pooling mean \
        --lr 1e-3 \
        --output_dir ./models

    # Full sweep (27 configs)
    python train_classifier.py \
        --data_dir ./activations \
        --mode 6class \
        --sweep \
        --output_dir ./models

Dependencies:
    torch, scikit-learn, numpy
"""

import argparse
import json
import logging
import os
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset, Subset
from sklearn.model_selection import StratifiedKFold

from configs import (
    ACTIVATION_SOURCES,
    CLASS_6_TO_3_MAPPING,
    CLASSIFIER_HIDDEN_DIM,
    DEFAULT_BATCH_SIZE,
    DEFAULT_EPOCHS,
    DEFAULT_LR,
    EXPERT_LAYERS,
    NUM_FOLDS,
    PALIGEMMA_LAYERS,
    PERTURBATION_TYPES_6CLASS,
    SWEEP_LRS,
    SWEEP_POOLINGS,
    SWEEP_SOURCES,
    compute_input_dim,
)

log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Classifier architecture
# ---------------------------------------------------------------------------

class PerturbationClassifier(nn.Module):
    """2-layer MLP matching the SAFE paper architecture."""

    def __init__(self, input_dim: int, num_classes: int, hidden_dim: int = CLASSIFIER_HIDDEN_DIM):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_activation_dataset(
    data_dir: Path,
    mode: str,
    activation_source: str,
    pooling: str,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Load activation .pt files and build (X, y) tensors.

    Handles incremental collection: each .pt file contains a list of episode dicts.
    Nominal episodes (label_binary=0) are included only for binary mode.
    """
    all_features = []
    all_labels = []

    pt_files = sorted(data_dir.glob("*.pt"))
    if not pt_files:
        raise FileNotFoundError(f"No .pt files found in {data_dir}")

    for pt_file in pt_files:
        episodes = torch.load(pt_file, weights_only=False)
        ptype = pt_file.stem
        is_nominal = ptype == "nominal"

        if is_nominal and mode != "binary":
            log.info("Skipping nominal episodes for mode=%s", mode)
            continue

        for ep in episodes:
            label = ep[f"label_{mode}"]
            if label == -1 and mode != "binary":
                continue

            feat = _extract_features(ep["activations"], activation_source, pooling)
            all_features.append(feat)
            all_labels.append(label)

        log.info("Loaded %s: %d episodes from %s", ptype, len(episodes), pt_file.name)

    X = torch.stack(all_features).float()
    y = torch.tensor(all_labels, dtype=torch.long)
    log.info("Dataset: X=%s, y=%s, classes=%s", X.shape, y.shape, torch.unique(y).tolist())
    return X, y


def _extract_features(
    activations: dict[str, dict[str, torch.Tensor]],
    activation_source: str,
    pooling: str,
) -> torch.Tensor:
    """Concatenate layer activations into a single feature vector."""
    parts = []

    if activation_source in ("paligemma_only", "both"):
        for i in PALIGEMMA_LAYERS:
            name = f"paligemma_layer_{i}"
            parts.append(activations[name][pooling].squeeze(0))

    if activation_source in ("expert_only", "both"):
        for i in EXPERT_LAYERS:
            name = f"expert_layer_{i}"
            parts.append(activations[name][pooling].squeeze(0))

    return torch.cat(parts).float()


# ---------------------------------------------------------------------------
# Training loop
# ---------------------------------------------------------------------------

def train_one_fold(
    model: nn.Module,
    train_loader: DataLoader,
    val_loader: DataLoader,
    lr: float,
    epochs: int,
    device: str,
) -> dict:
    """Train one fold, return val metrics and best model state_dict."""
    model = model.to(device)
    optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
    criterion = nn.CrossEntropyLoss()

    best_val_acc = 0.0
    best_state = None
    history = {"train_loss": [], "val_acc": []}

    for epoch in range(epochs):
        # Train
        model.train()
        total_loss = 0.0
        for X_batch, y_batch in train_loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)
            optimizer.zero_grad()
            logits = model(X_batch)
            loss = criterion(logits, y_batch)
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * X_batch.size(0)

        avg_loss = total_loss / len(train_loader.dataset)
        history["train_loss"].append(avg_loss)

        # Validate
        model.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for X_batch, y_batch in val_loader:
                X_batch, y_batch = X_batch.to(device), y_batch.to(device)
                preds = model(X_batch).argmax(dim=1)
                correct += (preds == y_batch).sum().item()
                total += y_batch.size(0)

        val_acc = correct / total
        history["val_acc"].append(val_acc)

        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}

        if (epoch + 1) % 10 == 0 or epoch == 0:
            log.info("  Epoch %d/%d  loss=%.4f  val_acc=%.4f", epoch + 1, epochs, avg_loss, val_acc)

    return {"best_val_acc": best_val_acc, "best_state": best_state, "history": history}


def cross_validate(
    X: torch.Tensor,
    y: torch.Tensor,
    input_dim: int,
    num_classes: int,
    lr: float,
    epochs: int,
    device: str,
) -> dict:
    """5-fold stratified cross-validation. Returns mean/std accuracy and best model."""
    skf = StratifiedKFold(n_splits=NUM_FOLDS, shuffle=True, random_state=42)
    dataset = TensorDataset(X, y)

    fold_accs = []
    best_overall_acc = 0.0
    best_overall_state = None

    for fold_idx, (train_idx, val_idx) in enumerate(skf.split(X.numpy(), y.numpy())):
        log.info("Fold %d/%d", fold_idx + 1, NUM_FOLDS)

        train_sub = Subset(dataset, train_idx)
        val_sub = Subset(dataset, val_idx)
        train_loader = DataLoader(train_sub, batch_size=DEFAULT_BATCH_SIZE, shuffle=True)
        val_loader = DataLoader(val_sub, batch_size=DEFAULT_BATCH_SIZE, shuffle=False)

        model = PerturbationClassifier(input_dim, num_classes)
        result = train_one_fold(model, train_loader, val_loader, lr, epochs, device)

        fold_accs.append(result["best_val_acc"])
        if result["best_val_acc"] > best_overall_acc:
            best_overall_acc = result["best_val_acc"]
            best_overall_state = result["best_state"]

    mean_acc = float(np.mean(fold_accs))
    std_acc = float(np.std(fold_accs))
    log.info("CV result: %.4f ± %.4f (folds: %s)", mean_acc, std_acc, fold_accs)

    return {
        "mean_acc": mean_acc,
        "std_acc": std_acc,
        "fold_accs": fold_accs,
        "best_state": best_overall_state,
    }


# ---------------------------------------------------------------------------
# Sweep
# ---------------------------------------------------------------------------

def run_sweep(args: argparse.Namespace) -> list[dict]:
    """Run full hyperparameter sweep over pooling × source × lr."""
    results = []
    mode = args.mode
    num_classes = _num_classes(mode)

    for pooling in SWEEP_POOLINGS:
        for source in SWEEP_SOURCES:
            for lr in SWEEP_LRS:
                config_name = f"{mode}__{pooling}__{source}__lr{lr}"
                log.info("=== Sweep config: %s ===", config_name)

                try:
                    X, y = load_activation_dataset(
                        Path(args.data_dir), mode, source, pooling,
                    )
                except Exception:
                    log.exception("Failed to load data for %s, skipping", config_name)
                    continue

                input_dim = compute_input_dim(source, pooling)
                cv = cross_validate(X, y, input_dim, num_classes, lr, args.epochs, args.device)

                record = {
                    "config_name": config_name,
                    "mode": mode,
                    "pooling": pooling,
                    "activation_source": source,
                    "lr": lr,
                    "mean_acc": cv["mean_acc"],
                    "std_acc": cv["std_acc"],
                    "fold_accs": cv["fold_accs"],
                }
                results.append(record)

                # Save best model for this config
                config_dir = Path(args.output_dir) / config_name
                config_dir.mkdir(parents=True, exist_ok=True)
                torch.save(cv["best_state"], config_dir / "best_model.pt")
                with open(config_dir / "result.json", "w") as f:
                    json.dump(record, f, indent=2)

                log.info("  -> %.4f ± %.4f", cv["mean_acc"], cv["std_acc"])

    # Save sweep summary
    results.sort(key=lambda r: r["mean_acc"], reverse=True)
    summary_path = Path(args.output_dir) / f"sweep_summary_{mode}.json"
    with open(summary_path, "w") as f:
        json.dump(results, f, indent=2)
    log.info("Sweep complete. Summary saved to %s", summary_path)

    # Print leaderboard
    log.info("=== Leaderboard (%s) ===", mode)
    for i, r in enumerate(results[:10]):
        log.info("  #%d  %.4f ± %.4f  %s", i + 1, r["mean_acc"], r["std_acc"], r["config_name"])

    return results


# ---------------------------------------------------------------------------
# Single run
# ---------------------------------------------------------------------------

def run_single(args: argparse.Namespace) -> None:
    mode = args.mode
    num_classes = _num_classes(mode)
    input_dim = compute_input_dim(args.activation_source, args.pooling)

    X, y = load_activation_dataset(
        Path(args.data_dir), mode, args.activation_source, args.pooling,
    )

    cv = cross_validate(X, y, input_dim, num_classes, args.lr, args.epochs, args.device)

    config_name = f"{mode}__{args.pooling}__{args.activation_source}__lr{args.lr}"
    out_dir = Path(args.output_dir) / config_name
    out_dir.mkdir(parents=True, exist_ok=True)

    torch.save(cv["best_state"], out_dir / "best_model.pt")

    record = {
        "config_name": config_name,
        "mode": mode,
        "pooling": args.pooling,
        "activation_source": args.activation_source,
        "lr": args.lr,
        "mean_acc": cv["mean_acc"],
        "std_acc": cv["std_acc"],
        "fold_accs": cv["fold_accs"],
    }
    with open(out_dir / "result.json", "w") as f:
        json.dump(record, f, indent=2)

    log.info("Model + result saved to %s", out_dir)


def _num_classes(mode: str) -> int:
    if mode == "6class":
        return 6
    elif mode == "3class":
        return 3
    elif mode == "binary":
        return 2
    raise ValueError(f"Unknown mode: {mode}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Train perturbation classifier on π₀ activations"
    )
    p.add_argument("--data_dir", type=str, required=True, help="Directory with activation .pt files")
    p.add_argument("--mode", type=str, default="6class", choices=["6class", "3class", "binary"])
    p.add_argument("--activation_source", type=str, default="both",
                    choices=ACTIVATION_SOURCES)
    p.add_argument("--pooling", type=str, default="mean", choices=["mean", "first", "last", "first_last"])
    p.add_argument("--lr", type=float, default=DEFAULT_LR)
    p.add_argument("--epochs", type=int, default=DEFAULT_EPOCHS)
    p.add_argument("--output_dir", type=str, default="./models")
    p.add_argument("--device", type=str, default="cuda:0")
    p.add_argument("--sweep", action="store_true", help="Run full hyperparameter sweep (27 configs)")
    return p.parse_args()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    args = parse_args()
    if args.sweep:
        run_sweep(args)
    else:
        run_single(args)

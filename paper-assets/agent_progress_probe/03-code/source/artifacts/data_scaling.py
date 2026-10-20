#!/usr/bin/env python3
"""Data scaling experiment: evaluate probe sensitivity to training data volume.

Trains GRU probe with 10%/25%/50%/100% of training instances (instance-level
subsampling). Test and val sets are fixed across all ratios.
Baseline (100% data, probe_001): test macro_f1=0.905 (conf>=2, 15401 windows)
"""

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

RATIOS = [0.10, 0.25, 0.50, 1.00]
SEED = 42
MIN_CONFIDENCE = 2
HIDDEN_SIZE = 256
NUM_LAYERS = 2
LR = 1e-3
BATCH_SIZE = 32
EPOCHS = 20
PATIENCE = 5
DROPOUT = 0.1
WEIGHT_DECAY = 0.01


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def compute_metrics(labels, preds):
    return {
        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
        "accuracy": accuracy_score(labels, preds),
        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
    }


class EarlyStopping:
    def __init__(self, patience=5):
        self.patience = patience
        self.counter = 0
        self.best_score = None
        self.should_stop = False

    def step(self, score):
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            self.counter = 0
            return True
        self.counter += 1
        if self.counter >= self.patience:
            self.should_stop = True
        return False


@torch.no_grad()
def evaluate(model, loader, device):
    model.eval()
    all_labels, all_preds = [], []
    for padded, labels, lengths in loader:
        logits = model(padded.to(device), lengths)
        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
        all_labels.extend(labels.long().tolist())
        all_preds.extend(preds.tolist())
    return compute_metrics(all_labels, all_preds)


def subsample_train_instances(instance_ids, train_idx, ratio, seed):
    """Subsample training instances at given ratio, return new train window indices."""
    train_instances = sorted(set(instance_ids[i] for i in train_idx))
    rng = random.Random(seed)
    k = max(1, int(len(train_instances) * ratio))
    selected = set(rng.sample(train_instances, k))
    return [i for i in train_idx if instance_ids[i] in selected], len(train_instances), k


def train_one_ratio(ratio, embeddings, labels, instance_ids, embed_dim,
                    train_idx, val_idx, test_idx, device):
    set_seed(SEED)

    sub_train_idx, total_inst, kept_inst = subsample_train_instances(
        instance_ids, train_idx, ratio, SEED
    )

    def make_ds(indices):
        return WindowDataset([embeddings[i] for i in indices], [labels[i] for i in indices])

    train_ds = make_ds(sub_train_idx)
    val_ds = make_ds(val_idx)
    test_ds = make_ds(test_idx)

    train_labels = [labels[i] for i in sub_train_idx]
    num_pos = sum(train_labels)
    num_neg = len(train_labels) - num_pos
    pos_weight = torch.tensor([num_neg / max(num_pos, 1)]).to(device)

    print(f"\n{'='*60}")
    print(f"Ratio: {ratio*100:.0f}% | instances: {kept_inst}/{total_inst} | "
          f"windows: {len(train_ds)} (pos={num_pos}, neg={num_neg})")
    print(f"Val: {len(val_ds)} | Test: {len(test_ds)} | pos_weight: {pos_weight.item():.3f}")

    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True, collate_fn=collate_fn)
    val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE, collate_fn=collate_fn)
    test_loader = DataLoader(test_ds, batch_size=BATCH_SIZE, collate_fn=collate_fn)

    model = ProgressProbe(
        embed_dim=embed_dim,
        hidden_size=HIDDEN_SIZE,
        num_layers=NUM_LAYERS,
        dropout=DROPOUT,
    ).to(device)

    optimizer = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=WEIGHT_DECAY)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    early_stopping = EarlyStopping(patience=PATIENCE)

    best_state = None
    for epoch in range(1, EPOCHS + 1):
        model.train()
        total_loss, n = 0.0, 0
        for padded, batch_labels, lengths in train_loader:
            padded = padded.to(device)
            batch_labels = batch_labels.to(device)
            logits = model(padded, lengths)
            loss = criterion(logits, batch_labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * len(batch_labels)
            n += len(batch_labels)

        avg_loss = total_loss / n
        val_metrics = evaluate(model, val_loader, device)
        is_best = early_stopping.step(val_metrics["macro_f1"])
        marker = " *" if is_best else ""
        print(f"  Epoch {epoch:2d} | loss={avg_loss:.4f} | "
              f"val_F1={val_metrics['macro_f1']:.4f} acc={val_metrics['accuracy']:.4f}{marker}")

        if is_best:
            best_state = {k: v.clone() for k, v in model.state_dict().items()}

        if early_stopping.should_stop:
            print(f"  Early stopping at epoch {epoch}")
            break

    model.load_state_dict(best_state)
    test_metrics = evaluate(model, test_loader, device)
    print(f"  Test: macro_f1={test_metrics['macro_f1']:.4f} acc={test_metrics['accuracy']:.4f}")

    return {
        "ratio": ratio,
        "train_instances": kept_inst,
        "total_instances": total_inst,
        "train_windows": len(train_ds),
        "val_windows": len(val_ds),
        "test_windows": len(test_ds),
        "best_val_macro_f1": early_stopping.best_score,
        "test_metrics": test_metrics,
    }


def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")

    data_dir = Path(__file__).parent
    data_path = data_dir / "embeddings.pt"
    data = torch.load(data_path, weights_only=False)

    embeddings = data["embeddings"]
    labels = data["labels"]
    instance_ids = data["instance_ids"]
    confidences = data.get("confidences", [1] * len(labels))
    embed_dim = data["embed_dim"]

    keep = [i for i, c in enumerate(confidences) if c >= MIN_CONFIDENCE]
    print(f"Confidence filter: {len(keep)}/{len(labels)} windows with conf>={MIN_CONFIDENCE}")
    embeddings = [embeddings[i] for i in keep]
    labels = [labels[i] for i in keep]
    instance_ids = [instance_ids[i] for i in keep]

    train_idx, val_idx, test_idx = split_by_instance(instance_ids, seed=SEED)
    print(f"Split: train={len(train_idx)}, val={len(val_idx)}, test={len(test_idx)}")

    results = []
    for ratio in RATIOS:
        r = train_one_ratio(ratio, embeddings, labels, instance_ids, embed_dim,
                            train_idx, val_idx, test_idx, device)
        results.append(r)

    print(f"\n{'='*60}")
    print("DATA SCALING RESULTS")
    print(f"{'='*60}")
    print(f"{'Ratio':>8} {'Inst':>6} {'Windows':>8} {'Val F1':>8} {'Test F1':>8} {'Test Acc':>8}")
    print("-" * 54)
    for r in results:
        print(f"{r['ratio']*100:>7.0f}% {r['train_instances']:>6} {r['train_windows']:>8} "
              f"{r['best_val_macro_f1']:>8.4f} {r['test_metrics']['macro_f1']:>8.4f} "
              f"{r['test_metrics']['accuracy']:>8.4f}")

    output_path = data_dir / "data_scaling_results.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()

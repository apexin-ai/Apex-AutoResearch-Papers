#!/usr/bin/env python3
"""Logistic regression probe for sycophancy detection from hidden states.

Trains on exp-001 calibration activations. Used by exp-014 as a frozen
R1 reward signal to replace the direction-projection R1 in DC-GRPO.
"""
import logging
from pathlib import Path

import torch
import torch.nn as nn

logger = logging.getLogger(__name__)


class LinearProbe(nn.Module):
    """Single-layer logistic regression probe: h -> P(sycophantic)."""

    def __init__(self, input_dim: int):
        super().__init__()
        self.linear = nn.Linear(input_dim, 1)
        self.register_buffer("feat_mean", torch.zeros(input_dim))
        self.register_buffer("feat_std", torch.ones(input_dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x_norm = (x - self.feat_mean) / (self.feat_std + 1e-8)
        return torch.sigmoid(self.linear(x_norm)).squeeze(-1)


def train_probe(
    activations_path: str,
    layers: list[int],
    position_idx: int = 1,
    lr: float = 1e-2,
    epochs: int = 200,
    weight_decay: float = 1e-4,
    seed: int = 42,
) -> tuple["LinearProbe", float]:
    """Train a logistic regression probe on exp-001 calibration activations.

    Features: mean hidden state across target layers at the given position.
    Labels: invalid_pressure -> 1 (sycophantic), valid_correction -> 0.

    Returns:
        (probe, accuracy) tuple.
    """
    torch.manual_seed(seed)

    data = torch.load(activations_path, map_location="cpu")
    logger.info("Loaded %d activation samples from %s", len(data), activations_path)

    features = []
    labels = []
    for sample in data:
        acts = sample["activations"]  # (36, 2, 4096)
        layer_vecs = [acts[l, position_idx] for l in layers]
        mean_vec = torch.stack(layer_vecs).mean(dim=0)
        features.append(mean_vec)
        labels.append(1.0 if sample["condition"] == "invalid_pressure" else 0.0)

    X = torch.stack(features)
    y = torch.tensor(labels)
    logger.info(
        "Probe training set: %d samples, %d features, %.1f%% positive",
        len(y), X.shape[1], y.mean().item() * 100,
    )

    feat_mean = X.mean(dim=0)
    feat_std = X.std(dim=0)

    probe = LinearProbe(X.shape[1])
    probe.feat_mean.copy_(feat_mean)
    probe.feat_std.copy_(feat_std)

    optimizer = torch.optim.Adam(probe.parameters(), lr=lr, weight_decay=weight_decay)
    criterion = nn.BCELoss()

    probe.train()
    for epoch in range(epochs):
        preds = probe(X)
        loss = criterion(preds, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 50 == 0:
            with torch.no_grad():
                acc = ((preds > 0.5).float() == y).float().mean().item()
            logger.info(
                "Probe epoch %d/%d: loss=%.4f acc=%.4f", epoch + 1, epochs, loss.item(), acc
            )

    probe.eval()
    with torch.no_grad():
        final_preds = probe(X)
        final_acc = ((final_preds > 0.5).float() == y).float().mean().item()
        final_loss = criterion(final_preds, y).item()

    try:
        from sklearn.metrics import roc_auc_score
        auroc = roc_auc_score(y.numpy(), final_preds.numpy())
    except ImportError:
        sorted_pairs = sorted(zip(final_preds.tolist(), y.tolist()), reverse=True)
        tp, fp, auc_sum = 0, 0, 0.0
        p_total = int(y.sum().item())
        n_total = len(y) - p_total
        for score, label in sorted_pairs:
            if label == 1.0:
                tp += 1
            else:
                auc_sum += tp
                fp += 1
        auroc = auc_sum / (p_total * n_total) if (p_total * n_total) > 0 else 0.0

    logger.info("Probe training done: loss=%.4f acc=%.4f AUROC=%.4f", final_loss, final_acc, auroc)

    return probe, final_acc, auroc


def save_probe(probe: LinearProbe, path: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    torch.save(
        {"state_dict": probe.state_dict(), "input_dim": probe.linear.in_features},
        path,
    )
    logger.info("Probe saved to %s", path)


def load_probe(path: str, device: str = "cpu") -> LinearProbe:
    ckpt = torch.load(path, map_location=device)
    probe = LinearProbe(ckpt["input_dim"])
    probe.load_state_dict(ckpt["state_dict"])
    probe.eval()
    logger.info("Probe loaded from %s (input_dim=%d)", path, ckpt["input_dim"])
    return probe

"""Temporal window probe (CRTA core method).

Input: Concatenation of W=5 consecutive hidden states
Output: Pre/post commitment probability for the center step
"""

import os
from pathlib import Path
from typing import List, Dict, Tuple

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from tqdm import tqdm

from ..config import (
    HIDDEN_DIM, WINDOW_SIZE, TEMPORAL_HIDDEN_DIM, LAYERS, DEFAULT_LAYER,
    LEARNING_RATE, TRAIN_EPOCHS, PROBE_BATCH_SIZE, SEED, PROBES_DIR,
    HIDDEN_STATES_DIR
)


class TemporalProbe(nn.Module):
    """3-layer MLP operating on a window of hidden states."""

    def __init__(self, window_size: int = WINDOW_SIZE, hidden_dim: int = HIDDEN_DIM,
                 mlp_hidden: int = TEMPORAL_HIDDEN_DIM):
        super().__init__()
        input_dim = window_size * hidden_dim
        self.net = nn.Sequential(
            nn.Linear(input_dim, mlp_hidden),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(mlp_hidden, mlp_hidden // 2),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(mlp_hidden // 2, 2),
        )

    def forward(self, x):
        return self.net(x)


def create_windows(
    hidden_states: torch.Tensor,
    step_labels: List[int],
    window_size: int = WINDOW_SIZE,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """Create sliding windows with zero-padding at boundaries.

    Args:
        hidden_states: [num_sentences, hidden_dim] for a single layer
        step_labels: list of 0/1 labels
        window_size: number of steps in each window

    Returns:
        windows: [num_sentences, window_size * hidden_dim]
        labels: [num_sentences] - label of center step
    """
    num_steps = hidden_states.shape[0]
    hdim = hidden_states.shape[1]
    half_w = window_size // 2

    # Pad with zeros
    padding = torch.zeros(half_w, hdim, dtype=hidden_states.dtype)
    padded = torch.cat([padding, hidden_states, padding], dim=0)

    windows = []
    labels = []

    for i in range(num_steps):
        window = padded[i:i + window_size]  # [window_size, hdim]
        windows.append(window.reshape(-1))  # [window_size * hdim]
        labels.append(step_labels[i])

    return torch.stack(windows), torch.tensor(labels, dtype=torch.long)


def collect_temporal_features(
    traces: List[Dict],
    layer_idx: int = None,
    hidden_states_dir: str = None,
    window_size: int = WINDOW_SIZE,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """Collect windowed features from all traces."""
    if layer_idx is None:
        layer_idx = LAYERS.index(DEFAULT_LAYER)
    if hidden_states_dir is None:
        hidden_states_dir = str(HIDDEN_STATES_DIR)

    all_windows = []
    all_labels = []

    for trace in traces:
        pt_path = Path(hidden_states_dir) / f"{trace['trace_id']}.pt"
        if not pt_path.exists():
            continue

        data = torch.load(pt_path, map_location="cpu", weights_only=False)
        hs = data["hidden_states"][:, layer_idx, :]  # [num_sentences, 4096]
        step_labels = trace["step_labels"]

        if step_labels is None:
            continue

        # Truncate labels if needed
        n = min(len(step_labels), hs.shape[0])
        windows, labels = create_windows(hs[:n], step_labels[:n], window_size)

        all_windows.append(windows)
        all_labels.append(labels)

    if not all_windows:
        return torch.tensor([]), torch.tensor([])

    return torch.cat(all_windows, dim=0), torch.cat(all_labels, dim=0)


def train_temporal_probe(
    train_traces: List[Dict],
    val_traces: List[Dict] = None,
    layer_idx: int = None,
    hidden_states_dir: str = None,
    window_size: int = WINDOW_SIZE,
    epochs: int = TRAIN_EPOCHS,
    lr: float = LEARNING_RATE,
    batch_size: int = PROBE_BATCH_SIZE,
    device: str = "cpu",
) -> TemporalProbe:
    """Train temporal window probe."""
    X_train, y_train = collect_temporal_features(
        train_traces, layer_idx, hidden_states_dir, window_size
    )
    print(f"Training temporal probe: {X_train.shape[0]} samples, {int(y_train.sum())} positive")

    dataset = TensorDataset(X_train.float(), y_train)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    model = TemporalProbe(window_size=window_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()

    model.train()
    for epoch in range(epochs):
        total_loss = 0
        correct = 0
        total = 0

        for X_batch, y_batch in loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)
            logits = model(X_batch)
            loss = criterion(logits, y_batch)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item() * len(y_batch)
            correct += (logits.argmax(1) == y_batch).sum().item()
            total += len(y_batch)

        if (epoch + 1) % 5 == 0:
            print(f"  Epoch {epoch+1}/{epochs}: loss={total_loss/total:.4f}, acc={correct/total:.4f}")

    return model


def predict_temporal(
    model: TemporalProbe,
    traces: List[Dict],
    layer_idx: int = None,
    hidden_states_dir: str = None,
    window_size: int = WINDOW_SIZE,
    device: str = "cpu",
) -> List[Dict]:
    """Get per-trace predictions from temporal probe."""
    if layer_idx is None:
        layer_idx = LAYERS.index(DEFAULT_LAYER)
    if hidden_states_dir is None:
        hidden_states_dir = str(HIDDEN_STATES_DIR)

    model.eval()
    results = []

    for trace in traces:
        pt_path = Path(hidden_states_dir) / f"{trace['trace_id']}.pt"
        if not pt_path.exists():
            continue

        data = torch.load(pt_path, map_location="cpu", weights_only=False)
        hs = data["hidden_states"][:, layer_idx, :]  # [num_sentences, 4096]
        step_labels = trace["step_labels"]

        if step_labels is None:
            continue

        n = min(len(step_labels), hs.shape[0])
        windows, labels = create_windows(hs[:n], step_labels[:n], window_size)

        with torch.no_grad():
            logits = model(windows.float().to(device))
            probs = torch.softmax(logits, dim=1)[:, 1].cpu().numpy()
            preds = logits.argmax(1).cpu().numpy()

        results.append({
            "trace_id": trace["trace_id"],
            "probs": probs,
            "preds": preds,
            "labels": labels.numpy(),
            "commitment_point": trace["commitment_point"],
        })

    return results


def save_probe(model: TemporalProbe, path: str = None):
    """Save trained temporal probe."""
    if path is None:
        path = str(PROBES_DIR / "temporal_probe.pt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    torch.save(model.state_dict(), path)
    print(f"Temporal probe saved to {path}")

"""Static linear probe baseline.

Input: Single-step hidden state from a specified layer
Output: Pre/post commitment probability
"""

import os
from pathlib import Path
from typing import List, Dict, Tuple

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.linear_model import LogisticRegression
from tqdm import tqdm

from ..config import (
    HIDDEN_DIM, DEFAULT_LAYER, LAYERS, PROBES_DIR,
    LEARNING_RATE, TRAIN_EPOCHS, PROBE_BATCH_SIZE, SEED, HIDDEN_STATES_DIR
)


class MLPProbe(nn.Module):
    """2-layer MLP probe for step-level classification."""

    def __init__(self, input_dim: int = HIDDEN_DIM, hidden_dim: int = 256):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(hidden_dim, 2),
        )

    def forward(self, x):
        return self.net(x)


def collect_step_features(
    traces: List[Dict],
    layer_idx: int = None,
    hidden_states_dir: str = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """Collect (hidden_state, label) pairs for all steps across traces.

    Args:
        traces: list of trace dicts with step_labels and trace_id
        layer_idx: index into LAYERS list (0-12), default maps to layer 20
        hidden_states_dir: directory containing .pt files

    Returns:
        features: [N, hidden_dim] array
        labels: [N] array of 0/1
    """
    if layer_idx is None:
        layer_idx = LAYERS.index(DEFAULT_LAYER)
    if hidden_states_dir is None:
        hidden_states_dir = str(HIDDEN_STATES_DIR)

    all_features = []
    all_labels = []

    for trace in traces:
        pt_path = Path(hidden_states_dir) / f"{trace['trace_id']}.pt"
        if not pt_path.exists():
            continue

        data = torch.load(pt_path, map_location="cpu", weights_only=False)
        hs = data["hidden_states"]  # [num_sentences, 13, 4096]
        step_labels = trace["step_labels"]

        if step_labels is None:
            continue

        # Extract features for the specified layer
        features = hs[:, layer_idx, :].numpy()  # [num_sentences, 4096]
        labels = np.array(step_labels[:len(features)])

        all_features.append(features)
        all_labels.append(labels)

    if not all_features:
        return np.array([]), np.array([])

    return np.concatenate(all_features, axis=0), np.concatenate(all_labels, axis=0)


def train_sklearn_probe(
    train_traces: List[Dict],
    layer_idx: int = None,
    hidden_states_dir: str = None,
) -> LogisticRegression:
    """Train a LogisticRegression probe."""
    X, y = collect_step_features(train_traces, layer_idx, hidden_states_dir)
    print(f"Training sklearn probe: {X.shape[0]} samples, {int(y.sum())} positive")

    clf = LogisticRegression(max_iter=1000, random_state=SEED, C=1.0)
    clf.fit(X, y)

    train_acc = clf.score(X, y)
    print(f"Train accuracy: {train_acc:.4f}")
    return clf


def train_mlp_probe(
    train_traces: List[Dict],
    val_traces: List[Dict] = None,
    layer_idx: int = None,
    hidden_states_dir: str = None,
    epochs: int = TRAIN_EPOCHS,
    lr: float = LEARNING_RATE,
    batch_size: int = PROBE_BATCH_SIZE,
    device: str = "cpu",
) -> MLPProbe:
    """Train a 2-layer MLP probe."""
    X_train, y_train = collect_step_features(train_traces, layer_idx, hidden_states_dir)
    print(f"Training MLP probe: {X_train.shape[0]} samples, {int(y_train.sum())} positive")

    X_tensor = torch.tensor(X_train, dtype=torch.float32)
    y_tensor = torch.tensor(y_train, dtype=torch.long)
    dataset = TensorDataset(X_tensor, y_tensor)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    model = MLPProbe(input_dim=HIDDEN_DIM).to(device)
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


def predict_sklearn(clf: LogisticRegression, traces: List[Dict],
                    layer_idx: int = None, hidden_states_dir: str = None):
    """Get per-trace predictions from sklearn probe."""
    if layer_idx is None:
        layer_idx = LAYERS.index(DEFAULT_LAYER)
    if hidden_states_dir is None:
        hidden_states_dir = str(HIDDEN_STATES_DIR)

    results = []
    for trace in traces:
        pt_path = Path(hidden_states_dir) / f"{trace['trace_id']}.pt"
        if not pt_path.exists():
            continue

        data = torch.load(pt_path, map_location="cpu", weights_only=False)
        hs = data["hidden_states"][:, layer_idx, :].numpy()

        probs = clf.predict_proba(hs)[:, 1]  # prob of class 1 (post-commitment)
        preds = clf.predict(hs)

        results.append({
            "trace_id": trace["trace_id"],
            "probs": probs,
            "preds": preds,
            "labels": np.array(trace["step_labels"][:len(probs)]),
            "commitment_point": trace["commitment_point"],
        })

    return results


def predict_mlp(model: MLPProbe, traces: List[Dict],
                layer_idx: int = None, hidden_states_dir: str = None, device: str = "cpu"):
    """Get per-trace predictions from MLP probe."""
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

        with torch.no_grad():
            logits = model(hs.float().to(device))
            probs = torch.softmax(logits, dim=1)[:, 1].cpu().numpy()
            preds = logits.argmax(1).cpu().numpy()

        results.append({
            "trace_id": trace["trace_id"],
            "probs": probs,
            "preds": preds,
            "labels": np.array(trace["step_labels"][:len(probs)]),
            "commitment_point": trace["commitment_point"],
        })

    return results


def save_probe(model, path: str = None):
    """Save trained probe to disk."""
    if path is None:
        path = str(PROBES_DIR / "static_mlp_probe.pt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    torch.save(model.state_dict(), path)
    print(f"Probe saved to {path}")

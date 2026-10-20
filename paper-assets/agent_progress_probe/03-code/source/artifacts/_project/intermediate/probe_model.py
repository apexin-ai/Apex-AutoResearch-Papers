#!/usr/bin/env python3
"""GRU-based progress probe model, dataset, and data splitting utilities."""

import random
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import Dataset


class ProgressProbe(nn.Module):
    """2-layer GRU probe for progress/stagnation binary classification.

    Input:  (batch, seq_len, embed_dim)
    Output: (batch,) logits (apply sigmoid for probabilities)
    """

    def __init__(self, embed_dim: int, hidden_size: int = 256, num_layers: int = 2, dropout: float = 0.1):
        super().__init__()
        self.gru = nn.GRU(
            embed_dim,
            hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
        )
        self.classifier = nn.Linear(hidden_size, 1)

    def forward(self, x: torch.Tensor, lengths: torch.Tensor = None) -> torch.Tensor:
        if lengths is not None:
            x = nn.utils.rnn.pack_padded_sequence(x, lengths.cpu(), batch_first=True, enforce_sorted=False)
        _, hidden = self.gru(x)
        out = hidden[-1]  # last layer hidden: (batch, hidden_size)
        return self.classifier(out).squeeze(-1)


class WindowDataset(Dataset):
    """Dataset of pre-computed window embeddings + binary labels."""

    def __init__(self, embeddings: list[torch.Tensor], labels: list[int]):
        assert len(embeddings) == len(labels)
        self.embeddings = embeddings
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.embeddings[idx], self.labels[idx]


def collate_fn(batch):
    """Pad variable-length window embeddings to the max length in the batch."""
    embeddings_list, labels_list = zip(*batch)
    lengths = torch.tensor([e.shape[0] for e in embeddings_list], dtype=torch.long)
    max_len = lengths.max().item()
    embed_dim = embeddings_list[0].shape[1]

    padded = torch.zeros(len(batch), max_len, embed_dim)
    for i, e in enumerate(embeddings_list):
        padded[i, : e.shape[0]] = e

    labels = torch.tensor(labels_list, dtype=torch.float32)
    return padded, labels, lengths


def split_by_instance(
    instance_ids: list[str],
    train_ratio: float = 0.7,
    val_ratio: float = 0.15,
    seed: int = 42,
) -> tuple[list[int], list[int], list[int]]:
    """Split indices so all windows from the same instance stay in one split."""
    unique = sorted(set(instance_ids))
    rng = random.Random(seed)
    rng.shuffle(unique)

    n = len(unique)
    n_train = int(n * train_ratio)
    n_val = int(n * val_ratio)

    train_set = set(unique[:n_train])
    val_set = set(unique[n_train : n_train + n_val])

    train_idx, val_idx, test_idx = [], [], []
    for i, iid in enumerate(instance_ids):
        if iid in train_set:
            train_idx.append(i)
        elif iid in val_set:
            val_idx.append(i)
        else:
            test_idx.append(i)

    return train_idx, val_idx, test_idx


def load_split_datasets(
    data_path: str | Path, seed: int = 42
) -> tuple[WindowDataset, WindowDataset, WindowDataset, dict]:
    """Load embeddings.pt and return train/val/test WindowDatasets + split info."""
    data = torch.load(data_path, weights_only=False)
    embeddings = data["embeddings"]
    labels = data["labels"]
    instance_ids = data["instance_ids"]

    train_idx, val_idx, test_idx = split_by_instance(instance_ids, seed=seed)

    def subset(indices):
        return WindowDataset([embeddings[i] for i in indices], [labels[i] for i in indices])

    split_info = {
        "train_indices": train_idx,
        "val_indices": val_idx,
        "test_indices": test_idx,
        "seed": seed,
        "embed_dim": data["embed_dim"],
    }
    return subset(train_idx), subset(val_idx), subset(test_idx), split_info


if __name__ == "__main__":
    print("=== ProgressProbe forward pass test ===")
    embed_dim = 1024
    batch_size = 4

    model = ProgressProbe(embed_dim=embed_dim)
    print(f"Model: {model}")
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Total parameters: {total_params:,}")

    # Random data with variable sequence lengths
    lengths = torch.tensor([3, 7, 5, 2])
    max_len = lengths.max().item()
    x = torch.randn(batch_size, max_len, embed_dim)
    logits = model(x, lengths)
    probs = torch.sigmoid(logits)

    print(f"Input shape:  {x.shape}")
    print(f"Lengths:      {lengths.tolist()}")
    print(f"Logits shape: {logits.shape}")
    print(f"Logits:       {logits.tolist()}")
    print(f"Probs:        {[f'{p:.4f}' for p in probs.tolist()]}")

    # Test dataset + collate
    dummy_embeds = [torch.randn(l, embed_dim) for l in [3, 5, 2, 8]]
    dummy_labels = [1, 0, 1, 0]
    ds = WindowDataset(dummy_embeds, dummy_labels)
    batch = [ds[i] for i in range(len(ds))]
    padded, labels, lens = collate_fn(batch)
    print(f"\nCollate test: padded={padded.shape}, labels={labels.shape}, lengths={lens.tolist()}")

    # Test split
    instance_ids = ["a", "a", "b", "b", "c", "c", "d", "d", "e", "e"]
    tr, va, te = split_by_instance(instance_ids, seed=42)
    print(f"\nSplit test (10 samples, 5 instances): train={len(tr)}, val={len(va)}, test={len(te)}")
    print("All tests passed.")

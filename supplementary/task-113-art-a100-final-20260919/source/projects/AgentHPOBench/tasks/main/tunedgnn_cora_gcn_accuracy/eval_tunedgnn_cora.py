#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import pickle
import random
import time
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import torch
import torch.nn as nn
import torch.nn.functional as F


ROOT = Path(".")
DATA_DIR = ROOT / "data/paper_exact/noisygl_cora"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", required=True)
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--seed", type=int, default=123)
    parser.add_argument("--lr", type=float, default=0.001)
    parser.add_argument("--hidden-channels", type=int, default=512)
    parser.add_argument("--local-layers", type=int, default=3)
    parser.add_argument("--dropout", type=float, default=0.7)
    parser.add_argument("--weight-decay", type=float, default=5e-4)
    parser.add_argument("--layer-norm", action="store_true")
    parser.add_argument("--residual", action="store_true")
    parser.add_argument("--normalize-features", action="store_true")
    parser.add_argument("--label-num-per-class", type=int, default=20)
    parser.add_argument("--valid-num", type=int, default=500)
    parser.add_argument("--test-num", type=int, default=1000)
    parser.add_argument("--device", default="cuda:0")
    return parser.parse_args()


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def parse_index_file(path: Path) -> list[int]:
    return [int(line.strip()) for line in path.read_text().splitlines() if line.strip()]


def load_pickle(path: Path):
    with path.open("rb") as handle:
        return pickle.load(handle, encoding="latin1")


def load_cora(normalize_features: bool):
    names = ["x", "y", "tx", "ty", "allx", "ally", "graph"]
    x, y, tx, ty, allx, ally, graph = [load_pickle(DATA_DIR / f"ind.cora.{name}") for name in names]
    test_idx_reorder = parse_index_file(DATA_DIR / "ind.cora.test.index")
    test_idx_range = np.sort(test_idx_reorder)

    features = sp.vstack((allx, tx)).tolil()
    features[test_idx_reorder, :] = features[test_idx_range, :]
    features = features.astype(np.float32)
    if normalize_features:
        rowsum = np.asarray(features.sum(1)).flatten()
        rowsum[rowsum == 0.0] = 1.0
        features = sp.diags(1.0 / rowsum).dot(features)
    features = features.toarray()

    labels = np.vstack((ally, ty))
    labels[test_idx_reorder, :] = labels[test_idx_range, :]
    labels = labels.argmax(axis=1).astype(np.int64)

    rows, cols = [], []
    for src, dsts in graph.items():
        for dst in dsts:
            rows.append(src)
            cols.append(dst)
    n = labels.shape[0]
    adj = sp.coo_matrix((np.ones(len(rows), dtype=np.float32), (rows, cols)), shape=(n, n))
    adj = adj + adj.T.multiply(adj.T > adj) - adj.multiply(adj.T > adj)
    adj = adj + sp.eye(n, dtype=np.float32)
    deg = np.asarray(adj.sum(1)).flatten()
    deg_inv_sqrt = np.power(deg, -0.5)
    deg_inv_sqrt[np.isinf(deg_inv_sqrt)] = 0.0
    adj = sp.diags(deg_inv_sqrt).dot(adj).dot(sp.diags(deg_inv_sqrt)).tocoo()
    indices = torch.tensor(np.vstack((adj.row, adj.col)), dtype=torch.long)
    values = torch.tensor(adj.data, dtype=torch.float32)
    return torch.tensor(features), torch.tensor(labels), torch.sparse_coo_tensor(indices, values, (n, n)).coalesce()


def class_rand_splits(labels: torch.Tensor, label_num_per_class: int, valid_num: int, test_num: int, seed: int):
    generator = torch.Generator().manual_seed(seed)
    train_idx, non_train_idx = [], []
    idx = torch.arange(labels.shape[0])
    for class_id in labels.unique(sorted=True):
        class_idx = idx[labels == class_id]
        perm = class_idx[torch.randperm(class_idx.numel(), generator=generator)]
        train_idx.extend(perm[:label_num_per_class].tolist())
        non_train_idx.extend(perm[label_num_per_class:].tolist())
    non_train = torch.tensor(non_train_idx)
    non_train = non_train[torch.randperm(non_train.numel(), generator=generator)]
    return {
        "train": torch.tensor(train_idx, dtype=torch.long),
        "valid": non_train[:valid_num].long(),
        "test": non_train[valid_num : valid_num + test_num].long(),
    }


class SparseGCN(nn.Module):
    def __init__(self, in_dim: int, hidden: int, out_dim: int, layers: int, dropout: float, layer_norm: bool, residual: bool):
        super().__init__()
        self.dropout = float(dropout)
        self.residual = bool(residual)
        self.linears = nn.ModuleList()
        self.norms = nn.ModuleList()
        dims = [in_dim] + [hidden] * max(1, layers)
        for left, right in zip(dims[:-1], dims[1:]):
            self.linears.append(nn.Linear(left, right, bias=True))
            self.norms.append(nn.LayerNorm(right) if layer_norm else nn.Identity())
        self.pred = nn.Linear(hidden, out_dim)

    def forward(self, x: torch.Tensor, adj: torch.Tensor):
        h = x
        for linear, norm in zip(self.linears, self.norms):
            previous = h
            h = torch.sparse.mm(adj, h)
            h = linear(h)
            if self.residual and previous.shape == h.shape:
                h = h + previous
            h = norm(h)
            h = F.relu(h)
            h = F.dropout(h, p=self.dropout, training=self.training)
        return self.pred(h)


@torch.no_grad()
def accuracy(logits: torch.Tensor, labels: torch.Tensor, idx: torch.Tensor) -> float:
    pred = logits[idx].argmax(dim=-1)
    return float((pred == labels[idx]).float().mean().item() * 100.0)


def main():
    args = parse_args()
    started = time.time()
    set_seed(args.seed)
    device = torch.device(args.device if torch.cuda.is_available() and args.device.startswith("cuda") else "cpu")
    x, labels, adj = load_cora(args.normalize_features)
    splits = class_rand_splits(labels, args.label_num_per_class, args.valid_num, args.test_num, args.seed)
    x, labels, adj = x.to(device), labels.to(device), adj.to(device)
    splits = {key: value.to(device) for key, value in splits.items()}

    model = SparseGCN(
        in_dim=x.shape[1],
        hidden=args.hidden_channels,
        out_dim=int(labels.max().item() + 1),
        layers=args.local_layers,
        dropout=args.dropout,
        layer_norm=args.layer_norm,
        residual=args.residual,
    ).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)

    best = {"best_val_accuracy_percent": -1.0, "test_accuracy_percent_at_best_val": -1.0, "best_epoch": -1}
    history = []
    for epoch in range(1, args.epochs + 1):
        model.train()
        optimizer.zero_grad(set_to_none=True)
        logits = model(x, adj)
        loss = F.cross_entropy(logits[splits["train"]], labels[splits["train"]])
        loss.backward()
        optimizer.step()
        model.eval()
        with torch.no_grad():
            logits = model(x, adj)
            train_acc = accuracy(logits, labels, splits["train"])
            val_acc = accuracy(logits, labels, splits["valid"])
            test_acc = accuracy(logits, labels, splits["test"])
        if val_acc > best["best_val_accuracy_percent"]:
            best = {
                "best_val_accuracy_percent": val_acc,
                "test_accuracy_percent_at_best_val": test_acc,
                "best_epoch": epoch,
            }
        if epoch == 1 or epoch == args.epochs or epoch % 10 == 0:
            history.append({"epoch": epoch, "loss": float(loss.item()), "train_acc": train_acc, "val_acc": val_acc, "test_acc": test_acc})

    out_dir = Path(args.results_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "metric": "test_accuracy_percent_at_best_val",
        "direction": "higher_is_better",
        "dataset": "Cora",
        "repo": "tunedGNN",
        "seconds": round(time.time() - started, 3),
        "config": {
            "epochs": args.epochs,
            "seed": args.seed,
            "lr": args.lr,
            "hidden_channels": args.hidden_channels,
            "local_layers": args.local_layers,
            "dropout": args.dropout,
            "weight_decay": args.weight_decay,
            "layer_norm": args.layer_norm,
            "residual": args.residual,
            "normalize_features": args.normalize_features,
        },
        **best,
        "history": history,
    }
    (out_dir / "results.json").write_text(json.dumps(payload, indent=2))
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()

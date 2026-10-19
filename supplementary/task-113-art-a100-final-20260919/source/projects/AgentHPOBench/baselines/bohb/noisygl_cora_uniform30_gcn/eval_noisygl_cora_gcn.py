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


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def parse_index_file(path: Path) -> list[int]:
    return [int(line.strip()) for line in path.read_text().splitlines() if line.strip()]


def load_pickle(path: Path):
    with path.open("rb") as handle:
        return pickle.load(handle, encoding="latin1")


def row_normalize(mx: sp.spmatrix) -> sp.csr_matrix:
    mx = mx.tocsr().astype(np.float32)
    rowsum = np.asarray(mx.sum(1)).reshape(-1)
    inv = np.power(rowsum, -1.0, where=rowsum != 0)
    inv[rowsum == 0] = 0.0
    return sp.diags(inv).dot(mx).tocsr()


def normalize_adj(adj: sp.spmatrix) -> sp.coo_matrix:
    adj = adj.tocoo().astype(np.float32)
    adj = adj + sp.eye(adj.shape[0], dtype=np.float32)
    rowsum = np.asarray(adj.sum(1)).reshape(-1)
    inv_sqrt = np.power(rowsum, -0.5, where=rowsum != 0)
    inv_sqrt[rowsum == 0] = 0.0
    d_mat = sp.diags(inv_sqrt)
    return d_mat.dot(adj).dot(d_mat).tocoo()


def sparse_to_torch(mx: sp.spmatrix, device: torch.device) -> torch.Tensor:
    coo = mx.tocoo().astype(np.float32)
    indices = torch.from_numpy(np.vstack((coo.row, coo.col)).astype(np.int64))
    values = torch.from_numpy(coo.data)
    return torch.sparse_coo_tensor(indices, values, coo.shape, device=device).coalesce()


def load_cora(data_dir: Path) -> dict[str, object]:
    names = ["x", "y", "tx", "ty", "allx", "ally", "graph"]
    objects = [load_pickle(data_dir / f"ind.cora.{name}") for name in names]
    x, y, tx, ty, allx, ally, graph = objects
    test_idx_reorder = np.array(parse_index_file(data_dir / "ind.cora.test.index"), dtype=np.int64)
    test_idx_range = np.sort(test_idx_reorder)

    features = sp.vstack((allx, tx)).tolil()
    features[test_idx_reorder, :] = features[test_idx_range, :]
    features = row_normalize(features)

    labels = np.vstack((ally, ty))
    labels[test_idx_reorder, :] = labels[test_idx_range, :]
    labels = labels.argmax(1).astype(np.int64)

    rows: list[int] = []
    cols: list[int] = []
    for src, dsts in graph.items():
        rows.extend([src] * len(dsts))
        cols.extend(dsts)
    values = np.ones(len(rows), dtype=np.float32)
    adj = sp.coo_matrix((values, (rows, cols)), shape=(labels.shape[0], labels.shape[0]))
    adj = adj + adj.T.multiply(adj.T > adj) - adj.multiply(adj.T > adj)
    adj = normalize_adj(adj)

    return {
        "features": features,
        "labels": labels,
        "adj": adj,
        "idx_train": np.arange(y.shape[0], dtype=np.int64),
        "idx_val": np.arange(y.shape[0], y.shape[0] + 500, dtype=np.int64),
        "idx_test": test_idx_range.astype(np.int64),
    }


def apply_uniform_noise(labels: np.ndarray, idx_train: np.ndarray, noise_rate: float, seed: int, num_classes: int) -> tuple[np.ndarray, int]:
    rng = np.random.RandomState(seed)
    noisy = labels.copy()
    changed = 0
    for idx in idx_train:
        if rng.rand() < noise_rate:
            choices = [cls for cls in range(num_classes) if cls != int(labels[idx])]
            noisy[idx] = rng.choice(choices)
            changed += 1
    return noisy, changed


class GCN(nn.Module):
    def __init__(self, in_dim: int, hidden_dim: int, out_dim: int, dropout: float) -> None:
        super().__init__()
        self.fc1 = nn.Linear(in_dim, hidden_dim, bias=False)
        self.fc2 = nn.Linear(hidden_dim, out_dim, bias=False)
        self.dropout = float(dropout)

    def forward(self, features: torch.Tensor, adj: torch.Tensor) -> torch.Tensor:
        hidden = torch.sparse.mm(adj, features)
        hidden = self.fc1(hidden)
        hidden = F.relu(hidden)
        hidden = F.dropout(hidden, p=self.dropout, training=self.training)
        hidden = torch.sparse.mm(adj, hidden)
        return self.fc2(hidden)


@torch.no_grad()
def accuracy(logits: torch.Tensor, labels: torch.Tensor, idx: torch.Tensor) -> float:
    pred = logits[idx].argmax(dim=1)
    return float((pred == labels[idx]).float().mean().item())


def run(args: argparse.Namespace) -> dict[str, object]:
    if not args.cpu and torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")
    set_seed(args.seed)
    data = load_cora(args.data_dir)
    labels_np = data["labels"]
    num_classes = int(labels_np.max()) + 1
    noisy_labels_np, changed = apply_uniform_noise(
        labels_np,
        data["idx_train"],
        args.noise_rate,
        args.noise_seed,
        num_classes,
    )

    features = torch.from_numpy(data["features"].toarray()).to(device=device, dtype=torch.float32)
    labels = torch.from_numpy(labels_np).to(device=device, dtype=torch.long)
    noisy_labels = torch.from_numpy(noisy_labels_np).to(device=device, dtype=torch.long)
    adj = sparse_to_torch(data["adj"], device)
    idx_train = torch.from_numpy(data["idx_train"]).to(device=device, dtype=torch.long)
    idx_val = torch.from_numpy(data["idx_val"]).to(device=device, dtype=torch.long)
    idx_test = torch.from_numpy(data["idx_test"]).to(device=device, dtype=torch.long)

    model = GCN(features.shape[1], args.hidden_dim, num_classes, args.dropout).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    best_val = -1.0
    best_epoch = -1
    best_state = None
    history: list[dict[str, float | int]] = []
    started = time.time()

    for epoch in range(1, args.epochs + 1):
        model.train()
        optimizer.zero_grad(set_to_none=True)
        logits = model(features, adj)
        loss = F.cross_entropy(logits[idx_train], noisy_labels[idx_train])
        loss.backward()
        optimizer.step()

        if epoch == 1 or epoch == args.epochs or epoch % args.log_every == 0:
            model.eval()
            logits_eval = model(features, adj)
            train_acc_noisy = accuracy(logits_eval, noisy_labels, idx_train)
            train_acc_clean = accuracy(logits_eval, labels, idx_train)
            val_acc = accuracy(logits_eval, labels, idx_val)
            test_acc = accuracy(logits_eval, labels, idx_test)
            history.append(
                {
                    "epoch": epoch,
                    "loss": float(loss.item()),
                    "train_acc_noisy": train_acc_noisy,
                    "train_acc_clean": train_acc_clean,
                    "val_acc": val_acc,
                    "test_acc": test_acc,
                }
            )
        model.eval()
        logits_val = model(features, adj)
        val_acc = accuracy(logits_val, labels, idx_val)
        if val_acc > best_val:
            best_val = val_acc
            best_epoch = epoch
            best_state = {key: value.detach().cpu().clone() for key, value in model.state_dict().items()}

    if best_state is not None:
        model.load_state_dict(best_state)
    model.eval()
    logits_final = model(features, adj)
    final_val = accuracy(logits_final, labels, idx_val)
    final_test = accuracy(logits_final, labels, idx_test)
    final_train_clean = accuracy(logits_final, labels, idx_train)
    final_train_noisy = accuracy(logits_final, noisy_labels, idx_train)
    seconds = round(time.time() - started, 3)

    result = {
        "task": "noisygl_cora_uniform30_gcn",
        "repo": "NoisyGL",
        "dataset": "Cora",
        "data_dir": str(args.data_dir),
        "model": "GCN",
        "noise_type": "uniform",
        "noise_rate": args.noise_rate,
        "noise_seed": args.noise_seed,
        "changed_train_labels": changed,
        "train_size": int(len(data["idx_train"])),
        "val_size": int(len(data["idx_val"])),
        "test_size": int(len(data["idx_test"])),
        "epochs": args.epochs,
        "hidden_dim": args.hidden_dim,
        "dropout": args.dropout,
        "lr": args.lr,
        "weight_decay": args.weight_decay,
        "seed": args.seed,
        "best_epoch": best_epoch,
        "best_val_accuracy": final_val,
        "best_val_accuracy_percent": final_val * 100.0,
        "test_accuracy": final_test,
        "test_accuracy_percent": final_test * 100.0,
        "train_accuracy_clean": final_train_clean,
        "train_accuracy_noisy": final_train_noisy,
        "seconds": seconds,
        "device": str(device),
        "cuda_visible_devices": torch.cuda.current_device() if device.type == "cuda" else None,
        "history": history,
    }
    args.results_dir.mkdir(parents=True, exist_ok=True)
    (args.results_dir / "results.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2), flush=True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--data-dir", type=Path, default=ROOT / "data/paper_exact/noisygl_cora")
    parser.add_argument("--epochs", type=int, default=80)
    parser.add_argument("--hidden-dim", type=int, default=64)
    parser.add_argument("--dropout", type=float, default=0.5)
    parser.add_argument("--lr", type=float, default=0.01)
    parser.add_argument("--weight-decay", type=float, default=5e-4)
    parser.add_argument("--noise-rate", type=float, default=0.3)
    parser.add_argument("--noise-seed", type=int, default=3000)
    parser.add_argument("--seed", type=int, default=3000)
    parser.add_argument("--log-every", type=int, default=20)
    parser.add_argument("--cpu", action="store_true")
    args = parser.parse_args()
    run(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

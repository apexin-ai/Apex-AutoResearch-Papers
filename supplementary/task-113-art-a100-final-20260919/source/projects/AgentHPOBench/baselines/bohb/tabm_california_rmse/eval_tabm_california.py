#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, TensorDataset


ROOT = Path(".")
DATA = ROOT / "data/paper_exact/tabm_california/cal_housing.data"
REPO = ROOT / "repositories/tabm"


class PlainMLP(nn.Module):
    def __init__(self, n_num_features: int, d_out: int, n_blocks: int, d_block: int, dropout: float):
        super().__init__()
        layers: list[nn.Module] = []
        in_dim = n_num_features
        for _ in range(n_blocks):
            layers.extend([nn.Linear(in_dim, d_block), nn.ReLU()])
            if dropout > 0:
                layers.append(nn.Dropout(dropout))
            in_dim = d_block
        layers.append(nn.Linear(in_dim, d_out))
        self.net = nn.Sequential(*layers)

    def forward(self, x_num: torch.Tensor) -> torch.Tensor:
        return self.net(x_num)


def load_data(seed: int) -> dict[str, torch.Tensor | int | float]:
    arr = np.loadtxt(DATA, dtype=np.float32, delimiter=",")
    x = arr[:, :8]
    y = (arr[:, 8] / 100000.0).reshape(-1, 1)
    train_val_idx, test_idx = train_test_split(
        np.arange(len(x)), test_size=0.2, random_state=seed, shuffle=True
    )
    train_idx, val_idx = train_test_split(
        train_val_idx, test_size=0.2, random_state=seed + 1, shuffle=True
    )

    x_mean = x[train_idx].mean(axis=0, keepdims=True)
    x_std = x[train_idx].std(axis=0, keepdims=True) + 1e-6
    y_mean = y[train_idx].mean(axis=0, keepdims=True)
    y_std = y[train_idx].std(axis=0, keepdims=True) + 1e-6

    def make(split_idx: np.ndarray) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        xs = (x[split_idx] - x_mean) / x_std
        ys = (y[split_idx] - y_mean) / y_std
        y_raw = y[split_idx]
        return torch.tensor(xs), torch.tensor(ys), torch.tensor(y_raw)

    x_train, y_train, raw_train = make(train_idx)
    x_val, y_val, raw_val = make(val_idx)
    x_test, y_test, raw_test = make(test_idx)
    return {
        "x_train": x_train,
        "y_train": y_train,
        "raw_train": raw_train,
        "x_val": x_val,
        "y_val": y_val,
        "raw_val": raw_val,
        "x_test": x_test,
        "y_test": y_test,
        "raw_test": raw_test,
        "y_mean": float(y_mean.squeeze()),
        "y_std": float(y_std.squeeze()),
        "num_total": len(x),
        "num_train": len(train_idx),
        "num_val": len(val_idx),
        "num_test": len(test_idx),
    }


def make_model(args: argparse.Namespace, n_num_features: int) -> nn.Module:
    if args.arch_type == "plain":
        return PlainMLP(
            n_num_features=n_num_features,
            d_out=1,
            n_blocks=args.n_blocks,
            d_block=args.d_block,
            dropout=args.dropout,
        )
    sys.path.insert(0, str(REPO))
    import tabm

    return tabm.TabM.make(
        n_num_features=n_num_features,
        cat_cardinalities=[],
        d_out=1,
        arch_type=args.arch_type,
        k=args.k,
        n_blocks=args.n_blocks,
        d_block=args.d_block,
        dropout=args.dropout,
    )


def unpack_prediction(pred: torch.Tensor) -> torch.Tensor:
    if pred.ndim == 3:
        return pred.squeeze(-1).mean(dim=1, keepdim=True)
    return pred


def train_loss(pred: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    if pred.ndim == 3:
        return torch.mean((pred.squeeze(-1) - y) ** 2)
    return torch.mean((pred - y) ** 2)


@torch.no_grad()
def evaluate(model: nn.Module, x: torch.Tensor, y_raw: torch.Tensor, y_mean: float, y_std: float) -> dict[str, float]:
    model.eval()
    pred_z = unpack_prediction(model(x))
    pred_raw = pred_z * y_std + y_mean
    rmse = torch.sqrt(torch.mean((pred_raw - y_raw) ** 2)).item()
    mae = torch.mean(torch.abs(pred_raw - y_raw)).item()
    return {"rmse": float(rmse), "mae": float(mae)}


def run(args: argparse.Namespace) -> dict[str, object]:
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)

    data = load_data(args.seed)
    device = torch.device(args.device if torch.cuda.is_available() and not args.cpu else "cpu")
    x_train = data["x_train"].to(device)
    y_train = data["y_train"].to(device)
    x_val = data["x_val"].to(device)
    raw_val = data["raw_val"].to(device)
    x_test = data["x_test"].to(device)
    raw_test = data["raw_test"].to(device)

    model = make_model(args, x_train.shape[1]).to(device)
    train_loader = DataLoader(
        TensorDataset(x_train, y_train),
        batch_size=args.batch_size,
        shuffle=True,
        drop_last=False,
    )
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scheduler = (
        torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=max(1, args.epochs))
        if args.use_scheduler
        else None
    )

    start = time.time()
    losses: list[float] = []
    best_val = float("inf")
    best_state = None
    patience_left = args.patience
    for epoch in range(args.epochs):
        model.train()
        for xb, yb in train_loader:
            optimizer.zero_grad(set_to_none=True)
            loss = train_loss(model(xb), yb)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), args.grad_clip)
            optimizer.step()
            losses.append(float(loss.item()))
        if scheduler is not None:
            scheduler.step()
        val_rmse = evaluate(model, x_val, raw_val, float(data["y_mean"]), float(data["y_std"]))["rmse"]
        if val_rmse < best_val:
            best_val = val_rmse
            best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
            patience_left = args.patience
        else:
            patience_left -= 1
        if args.early_stop and patience_left <= 0:
            break

    if best_state is not None:
        model.load_state_dict(best_state)
    val = evaluate(model, x_val, raw_val, float(data["y_mean"]), float(data["y_std"]))
    test = evaluate(model, x_test, raw_test, float(data["y_mean"]), float(data["y_std"]))
    result = {
        "task": "TabM California Housing regression",
        "repo": "tabm",
        "dataset": "California Housing",
        "metric": "rmse",
        "paper_anchor_rmse": 0.44139199088313996,
        "paper_anchor_source": "tabm repo paper/exp/tabm/california/0-evaluation reports; 15-seed mean test RMSE.",
        "arch_type": args.arch_type,
        "k": args.k,
        "n_blocks": args.n_blocks,
        "d_block": args.d_block,
        "dropout": args.dropout,
        "lr": args.lr,
        "weight_decay": args.weight_decay,
        "batch_size": args.batch_size,
        "epochs": args.epochs,
        "use_scheduler": args.use_scheduler,
        "early_stop": args.early_stop,
        "patience": args.patience,
        "epochs_ran": epoch + 1,
        "train_loss_final": losses[-1] if losses else None,
        "train_loss_mean_last10": sum(losses[-10:]) / max(1, min(10, len(losses))),
        "val_rmse": val["rmse"],
        "val_mae": val["mae"],
        "test_rmse": test["rmse"],
        "test_mae": test["mae"],
        "num_total": int(data["num_total"]),
        "num_train": int(data["num_train"]),
        "num_val": int(data["num_val"]),
        "num_test": int(data["num_test"]),
        "seconds": round(time.time() - start, 3),
        "device": str(device),
        "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES"),
    }
    args.results_dir.mkdir(parents=True, exist_ok=True)
    (args.results_dir / "results.json").write_text(json.dumps(result, indent=2))
    print("RESULT_JSON " + json.dumps(result, sort_keys=True), flush=True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--arch-type", choices=["plain", "tabm-mini", "tabm"], default="plain")
    parser.add_argument("--k", type=int, default=8)
    parser.add_argument("--n-blocks", type=int, default=2)
    parser.add_argument("--d-block", type=int, default=128)
    parser.add_argument("--dropout", type=float, default=0.1)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--weight-decay", type=float, default=1e-4)
    parser.add_argument("--batch-size", type=int, default=256)
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--use-scheduler", action=argparse.BooleanOptionalAction, default=False)
    parser.add_argument("--early-stop", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--patience", type=int, default=12)
    parser.add_argument("--grad-clip", type=float, default=1.0)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--cpu", action="store_true")
    args = parser.parse_args()
    run(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

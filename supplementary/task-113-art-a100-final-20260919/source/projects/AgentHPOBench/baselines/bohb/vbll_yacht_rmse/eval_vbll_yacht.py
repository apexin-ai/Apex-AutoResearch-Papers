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
from torch.utils.data import DataLoader, TensorDataset


ROOT = Path(".")
DATA = ROOT / "data/paper_exact/vbll_yacht/yacht_hydrodynamics.data"
REPO = ROOT / "repositories/vbll"


class VBLLMLP(nn.Module):
    def __init__(self, in_features: int, hidden_features: int, num_layers: int, reg_weight: float,
                 parameterization: str, prior_scale: float, wishart_scale: float, dropout: float):
        super().__init__()
        import vbll

        layers: list[nn.Module] = [nn.Linear(in_features, hidden_features), nn.ELU()]
        for _ in range(num_layers - 1):
            layers.append(nn.Linear(hidden_features, hidden_features))
            layers.append(nn.ELU())
            if dropout > 0:
                layers.append(nn.Dropout(dropout))
        self.feature = nn.Sequential(*layers)
        self.out_layer = vbll.Regression(
            hidden_features,
            1,
            reg_weight,
            parameterization=parameterization,
            prior_scale=prior_scale,
            wishart_scale=wishart_scale,
        )

    def forward(self, x: torch.Tensor):
        return self.out_layer(self.feature(x))


def load_data(seed: int) -> dict[str, torch.Tensor | float | int]:
    arr = np.loadtxt(DATA, dtype=np.float32)
    x = arr[:, :6]
    y = arr[:, 6:7]
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(x))
    n_train = int(0.72 * len(x))
    n_val = int(0.18 * len(x))
    train_idx = idx[:n_train]
    val_idx = idx[n_train:n_train + n_val]
    test_idx = idx[n_train + n_val:]
    x_mean = x[train_idx].mean(axis=0, keepdims=True)
    x_std = x[train_idx].std(axis=0, keepdims=True) + 1e-6
    y_mean = y[train_idx].mean(axis=0, keepdims=True)
    y_train_centered = y[train_idx] - y_mean
    return {
        "x_train": torch.tensor((x[train_idx] - x_mean) / x_std),
        "y_train": torch.tensor(y_train_centered),
        "x_val": torch.tensor((x[val_idx] - x_mean) / x_std),
        "y_val": torch.tensor(y[val_idx] - y_mean),
        "x_test": torch.tensor((x[test_idx] - x_mean) / x_std),
        "y_test": torch.tensor(y[test_idx] - y_mean),
        "y_mean": float(y_mean.squeeze()),
        "num_total": len(x),
        "num_train": len(train_idx),
        "num_val": len(val_idx),
        "num_test": len(test_idx),
    }


@torch.no_grad()
def evaluate(model: nn.Module, x: torch.Tensor, y: torch.Tensor) -> dict[str, float]:
    model.eval()
    out = model(x)
    pred = out.predictive
    mean = pred.mean
    rmse = torch.sqrt(torch.mean((mean - y) ** 2)).item()
    nll = out.val_loss_fn(y).item()
    mae = torch.mean(torch.abs(mean - y)).item()
    return {"rmse": float(rmse), "nll": float(nll), "mae": float(mae)}


def run(args: argparse.Namespace) -> dict[str, object]:
    sys.path.insert(0, str(REPO))
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)
    data = load_data(args.seed)
    device = torch.device(args.device if torch.cuda.is_available() and not args.cpu else "cpu")

    x_train = data["x_train"].to(device)
    y_train = data["y_train"].to(device)
    x_val = data["x_val"].to(device)
    y_val = data["y_val"].to(device)
    x_test = data["x_test"].to(device)
    y_test = data["y_test"].to(device)
    reg_weight = float(args.reg_weight_scale) / int(data["num_train"])

    model = VBLLMLP(
        in_features=x_train.shape[1],
        hidden_features=args.hidden_features,
        num_layers=args.num_layers,
        reg_weight=reg_weight,
        parameterization=args.parameterization,
        prior_scale=args.prior_scale,
        wishart_scale=args.wishart_scale,
        dropout=args.dropout,
    ).to(device)

    train_ds = TensorDataset(x_train, y_train)
    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True, drop_last=False)
    params = [
        {"params": model.feature.parameters(), "weight_decay": args.weight_decay},
        {"params": model.out_layer.parameters(), "weight_decay": 0.0},
    ]
    optimizer = torch.optim.AdamW(params, lr=args.lr, weight_decay=args.weight_decay)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=max(1, args.epochs)) if args.use_scheduler else None

    start = time.time()
    losses: list[float] = []
    best_val = float("inf")
    best_state = None
    for epoch in range(args.epochs):
        model.train()
        for xb, yb in train_loader:
            optimizer.zero_grad(set_to_none=True)
            out = model(xb)
            loss = out.train_loss_fn(yb)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), args.grad_clip)
            optimizer.step()
            losses.append(float(loss.item()))
        if scheduler is not None:
            scheduler.step()
        if args.select_best_val:
            val_rmse = evaluate(model, x_val, y_val)["rmse"]
            if val_rmse < best_val:
                best_val = val_rmse
                best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}

    if best_state is not None:
        model.load_state_dict(best_state)
    val = evaluate(model, x_val, y_val)
    test = evaluate(model, x_test, y_test)
    result = {
        "task": "VBLL Yacht hydrodynamics regression",
        "repo": "vbll",
        "dataset": "UCI Yacht Hydrodynamics",
        "metric": "rmse",
        "paper_anchor_rmse": 0.86,
        "paper_anchor_nll": 1.29,
        "paper_anchor_source": "VBLL ICLR 2024 paper Table 2, Yacht dataset.",
        "hidden_features": args.hidden_features,
        "num_layers": args.num_layers,
        "parameterization": args.parameterization,
        "lr": args.lr,
        "weight_decay": args.weight_decay,
        "batch_size": args.batch_size,
        "epochs": args.epochs,
        "reg_weight_scale": args.reg_weight_scale,
        "reg_weight": reg_weight,
        "prior_scale": args.prior_scale,
        "wishart_scale": args.wishart_scale,
        "dropout": args.dropout,
        "use_scheduler": args.use_scheduler,
        "select_best_val": args.select_best_val,
        "train_loss_final": losses[-1] if losses else None,
        "train_loss_mean_last10": sum(losses[-10:]) / max(1, min(10, len(losses))),
        "val_rmse": val["rmse"],
        "val_nll": val["nll"],
        "val_mae": val["mae"],
        "test_rmse": test["rmse"],
        "test_nll": test["nll"],
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
    parser.add_argument("--hidden-features", type=int, default=64)
    parser.add_argument("--num-layers", type=int, default=2)
    parser.add_argument("--parameterization", choices=["diagonal", "dense"], default="diagonal")
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--weight-decay", type=float, default=1e-4)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--epochs", type=int, default=80)
    parser.add_argument("--reg-weight-scale", type=float, default=1.0)
    parser.add_argument("--prior-scale", type=float, default=1.0)
    parser.add_argument("--wishart-scale", type=float, default=0.1)
    parser.add_argument("--dropout", type=float, default=0.0)
    parser.add_argument("--use-scheduler", action=argparse.BooleanOptionalAction, default=False)
    parser.add_argument("--select-best-val", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--grad-clip", type=float, default=1.0)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--cpu", action="store_true")
    args = parser.parse_args()
    run(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import random
import time
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader, Dataset


ROOT = Path(".")
REPO = ROOT / "repositories/SparseTSF"
DATA_FILE = ROOT / "data/formal/ett_diverse/ETT-small/ETTm1.csv"

import sys

sys.path.insert(0, str(REPO))
from models.SparseTSF import Model as SparseTSFModel  # noqa: E402


class ETTm1Dataset(Dataset):
    def __init__(self, flag: str, seq_len: int, pred_len: int):
        df_raw = pd.read_csv(DATA_FILE)
        cols = list(df_raw.columns)
        cols.remove("date")
        data = df_raw[cols].values.astype("float32")

        points_per_hour = 4
        train_end = 12 * 30 * 24 * points_per_hour
        val_end = train_end + 4 * 30 * 24 * points_per_hour
        test_end = train_end + 8 * 30 * 24 * points_per_hour
        border1s = {
            "train": 0,
            "val": train_end - seq_len,
            "test": val_end - seq_len,
        }
        border2s = {
            "train": train_end,
            "val": val_end,
            "test": test_end,
        }
        scaler = StandardScaler()
        scaler.fit(data[:train_end])
        scaled = scaler.transform(data).astype("float32")
        self.data = scaled[border1s[flag] : border2s[flag]]
        self.seq_len = seq_len
        self.pred_len = pred_len

    def __len__(self) -> int:
        return len(self.data) - self.seq_len - self.pred_len + 1

    def __getitem__(self, index: int) -> tuple[torch.Tensor, torch.Tensor]:
        s_begin = index
        s_end = s_begin + self.seq_len
        r_end = s_end + self.pred_len
        seq_x = self.data[s_begin:s_end]
        seq_y = self.data[s_end:r_end]
        return torch.from_numpy(seq_x), torch.from_numpy(seq_y)


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True


@torch.no_grad()
def evaluate(model: torch.nn.Module, loader: DataLoader, device: torch.device) -> dict[str, float]:
    model.eval()
    se_sum = 0.0
    ae_sum = 0.0
    count = 0
    for x, y in loader:
        x = x.to(device)
        y = y.to(device)
        pred = model(x)
        diff = pred - y
        se_sum += float((diff * diff).sum().item())
        ae_sum += float(diff.abs().sum().item())
        count += int(diff.numel())
    return {"mse": se_sum / count, "mae": ae_sum / count}


def build_model(args: argparse.Namespace) -> torch.nn.Module:
    configs = SimpleNamespace(
        seq_len=args.seq_len,
        pred_len=args.pred_len,
        enc_in=7,
        period_len=args.period_len,
        d_model=args.d_model,
        model_type=args.model_type,
    )
    return SparseTSFModel(configs)


def train(args: argparse.Namespace) -> dict:
    set_seed(args.seed)
    device = torch.device(args.device)
    train_data = ETTm1Dataset("train", args.seq_len, args.pred_len)
    val_data = ETTm1Dataset("val", args.seq_len, args.pred_len)
    test_data = ETTm1Dataset("test", args.seq_len, args.pred_len)
    generator = torch.Generator()
    generator.manual_seed(args.seed)
    train_loader = DataLoader(
        train_data,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=args.num_workers,
        drop_last=True,
        generator=generator,
    )
    val_loader = DataLoader(val_data, batch_size=args.eval_batch_size, shuffle=False, num_workers=args.num_workers)
    test_loader = DataLoader(test_data, batch_size=args.eval_batch_size, shuffle=False, num_workers=args.num_workers)

    model = build_model(args).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scheduler = None
    if args.cosine:
        total_steps = max(len(train_loader) * args.epochs, 1)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=total_steps, eta_min=args.lr * 0.05)

    history = []
    best_val = float("inf")
    best_test = None
    best_epoch = 0
    started = time.time()
    for epoch in range(1, args.epochs + 1):
        model.train()
        losses = []
        for x, y in train_loader:
            x = x.to(device)
            y = y.to(device)
            loss = F.mse_loss(model(x), y)
            optimizer.zero_grad(set_to_none=True)
            loss.backward()
            if args.grad_clip > 0:
                torch.nn.utils.clip_grad_norm_(model.parameters(), args.grad_clip)
            optimizer.step()
            if scheduler is not None:
                scheduler.step()
            losses.append(float(loss.item()))

        val_metrics = evaluate(model, val_loader, device)
        test_metrics = evaluate(model, test_loader, device)
        if val_metrics["mse"] < best_val:
            best_val = val_metrics["mse"]
            best_test = test_metrics
            best_epoch = epoch
        history.append(
            {
                "epoch": epoch,
                "train_loss": float(np.mean(losses)),
                "val_mse": val_metrics["mse"],
                "val_mae": val_metrics["mae"],
                "test_mse": test_metrics["mse"],
                "test_mae": test_metrics["mae"],
                "best_val_mse": best_val,
                "best_test_mse_at_best_val": best_test["mse"],
                "lr": float(optimizer.param_groups[0]["lr"]),
            }
        )

    assert best_test is not None
    return {
        "config": vars(args),
        "dataset": {
            "path": str(DATA_FILE),
            "train_windows": len(train_data),
            "val_windows": len(val_data),
            "test_windows": len(test_data),
            "channels": 7,
            "seq_len": args.seq_len,
            "pred_len": args.pred_len,
        },
        "metric": "test_mse_at_best_val",
        "test_mse_at_best_val": best_test["mse"],
        "test_mae_at_best_val": best_test["mae"],
        "best_val_mse": best_val,
        "best_epoch": best_epoch,
        "history": history,
        "seconds": round(time.time() - started, 3),
        "num_parameters": sum(p.numel() for p in model.parameters()),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", required=True)
    parser.add_argument("--seq-len", type=int, default=720)
    parser.add_argument("--pred-len", type=int, default=96)
    parser.add_argument("--period-len", type=int, default=24)
    parser.add_argument("--model-type", choices=["linear", "mlp"], default="linear")
    parser.add_argument("--d-model", type=int, default=128)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--weight-decay", type=float, default=0.0)
    parser.add_argument("--batch-size", type=int, default=256)
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--eval-batch-size", type=int, default=512)
    parser.add_argument("--num-workers", type=int, default=0)
    parser.add_argument("--grad-clip", type=float, default=0.0)
    parser.add_argument("--seed", type=int, default=2023)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--cosine", action="store_true")
    args = parser.parse_args()

    out_dir = Path(args.results_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = train(args)
    (out_dir / "results.json").write_text(json.dumps(payload, indent=2))
    print(json.dumps(payload, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from itertools import cycle
from pathlib import Path

import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader


ROOT = Path(".")
REPO = ROOT / "repositories/xlstm"
RANDOM_BASELINE = 0.5


def add_repo() -> None:
    repo = str(REPO)
    if repo not in sys.path:
        sys.path.insert(0, repo)


def make_dataset(args: argparse.Namespace):
    add_repo()
    from experiments.data.formal_language.formal_language_dataset import (
        FormLangDatasetConfig,
        FormLangDatasetGenerator,
    )

    config = {
        "synth_lang_type": "parity",
        "vocab_size": 3,
        "seed": 1,
        "enable_mask": True,
        "context_length": args.context_length,
        "min_sequence_length": 3,
        "max_sequence_length": 40,
        "count": {
            "train": args.train_count,
            "validation": args.eval_count,
            "test": args.eval_count,
        },
        "subpar": {
            "validation": {
                "min_sequence_length": 40,
                "max_sequence_length": args.context_length,
            },
            "test": {
                "min_sequence_length": 40,
                "max_sequence_length": args.context_length,
            },
        },
    }
    return FormLangDatasetGenerator(FormLangDatasetConfig(**config))


def slstm_at(pattern: str) -> list[int]:
    if pattern == "all":
        return [0, 1]
    if pattern == "first":
        return [0]
    return [1]


def make_model(args: argparse.Namespace):
    add_repo()
    from xlstm import (
        mLSTMBlockConfig,
        mLSTMLayerConfig,
        sLSTMBlockConfig,
        sLSTMLayerConfig,
        xLSTMLMModel,
        xLSTMLMModelConfig,
    )

    config = xLSTMLMModelConfig(
        mlstm_block=mLSTMBlockConfig(mlstm=mLSTMLayerConfig(num_heads=1)),
        slstm_block=sLSTMBlockConfig(slstm=sLSTMLayerConfig(num_heads=1, backend="vanilla")),
        slstm_at=slstm_at(args.slstm_pattern),
        context_length=args.context_length,
        num_blocks=2,
        embedding_dim=args.embedding_dim,
        vocab_size=3,
        dropout=args.dropout,
    )
    model = xLSTMLMModel(config)
    model.reset_parameters()
    return model


@torch.no_grad()
def evaluate(model: torch.nn.Module, loader: DataLoader, device: torch.device, use_amp: bool) -> dict[str, float]:
    model.eval()
    loss_sum = 0.0
    num_tokens = 0
    num_correct = 0
    last_correct = 0
    last_tokens = 0
    for inputs, labels in loader:
        inputs = inputs.to(device)
        labels = labels.to(device)
        with torch.autocast(device_type="cuda", dtype=torch.bfloat16, enabled=use_amp and device.type == "cuda"):
            logits = model(inputs)
            loss = F.cross_entropy(logits.view(-1, 3), labels.view(-1), ignore_index=-1)
        valid = labels != -1
        pred = logits.argmax(dim=-1)
        loss_sum += float(loss.item()) * int(valid.sum().item())
        num_tokens += int(valid.sum().item())
        num_correct += int(((pred == labels) & valid).sum().item())
        last_valid_idx = valid.long().sum(dim=1) - 1
        for row, idx in enumerate(last_valid_idx.tolist()):
            if idx >= 0:
                last_correct += int(pred[row, idx].item() == labels[row, idx].item())
                last_tokens += 1
    acc = num_correct / max(1, num_tokens)
    scaled = (acc - RANDOM_BASELINE) / (1.0 - RANDOM_BASELINE)
    return {
        "sequence_accuracy": acc,
        "scaled_accuracy": scaled,
        "last_token_accuracy": last_correct / max(1, last_tokens),
        "eval_loss": loss_sum / max(1, num_tokens),
        "eval_tokens": num_tokens,
        "eval_examples": len(loader.dataset),
    }


def train_eval(args: argparse.Namespace) -> dict[str, object]:
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)
    start = time.time()

    dataset = make_dataset(args)
    train_loader = DataLoader(dataset.train_split, batch_size=args.batch_size, shuffle=True, drop_last=True)
    eval_loader = DataLoader(dataset.validation_split["validation"], batch_size=args.eval_batch_size, shuffle=False)

    device = torch.device("cuda" if torch.cuda.is_available() and not args.cpu else "cpu")
    model = make_model(args).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.learning_rate, weight_decay=args.weight_decay)

    warmup_steps = int(args.train_steps * args.warmup_ratio)

    def lr_factor(step: int) -> float:
        if warmup_steps > 0 and step < warmup_steps:
            return float(step + 1) / max(1, warmup_steps)
        return 1.0

    losses: list[float] = []
    data_iter = cycle(train_loader)
    for step in range(args.train_steps):
        inputs, labels = next(data_iter)
        inputs = inputs.to(device)
        labels = labels.to(device)
        model.train()
        optimizer.zero_grad(set_to_none=True)
        for group in optimizer.param_groups:
            group["lr"] = args.learning_rate * lr_factor(step)
        with torch.autocast(device_type="cuda", dtype=torch.bfloat16, enabled=args.use_amp and device.type == "cuda"):
            logits = model(inputs)
            loss = F.cross_entropy(logits.view(-1, 3), labels.view(-1), ignore_index=-1)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), args.grad_clip)
        optimizer.step()
        losses.append(float(loss.item()))

    metrics = evaluate(model, eval_loader, device, args.use_amp)
    result = {
        "task": "xlstm_parity_formal_language",
        "repo": "NX-AI/xlstm",
        "dataset": "xLSTM paper formal language Parity",
        "backend": "vanilla_sLSTM",
        "context_length": args.context_length,
        "train_count": args.train_count,
        "eval_count": args.eval_count,
        "train_steps": args.train_steps,
        "learning_rate": args.learning_rate,
        "weight_decay": args.weight_decay,
        "warmup_ratio": args.warmup_ratio,
        "batch_size": args.batch_size,
        "eval_batch_size": args.eval_batch_size,
        "embedding_dim": args.embedding_dim,
        "slstm_pattern": args.slstm_pattern,
        "dropout": args.dropout,
        "grad_clip": args.grad_clip,
        "train_loss_final": losses[-1] if losses else math.nan,
        "train_loss_mean_last10": sum(losses[-10:]) / max(1, min(10, len(losses))),
        "seconds": round(time.time() - start, 3),
        "device": str(device),
        "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES"),
        **metrics,
    }
    args.results_dir.mkdir(parents=True, exist_ok=True)
    (args.results_dir / "results.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2), flush=True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--context-length", type=int, default=256)
    parser.add_argument("--train-count", type=int, default=8192)
    parser.add_argument("--eval-count", type=int, default=2048)
    parser.add_argument("--train-steps", type=int, default=120)
    parser.add_argument("--learning-rate", type=float, default=1e-4)
    parser.add_argument("--weight-decay", type=float, default=0.1)
    parser.add_argument("--warmup-ratio", type=float, default=0.1)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--eval-batch-size", type=int, default=256)
    parser.add_argument("--embedding-dim", type=int, default=64)
    parser.add_argument("--slstm-pattern", choices=["last", "all", "first"], default="last")
    parser.add_argument("--dropout", type=float, default=0.0)
    parser.add_argument("--grad-clip", type=float, default=1.0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--use-amp", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--cpu", action="store_true")
    args = parser.parse_args()
    train_eval(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

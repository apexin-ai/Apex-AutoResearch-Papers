#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import os
import random
import time
from contextlib import nullcontext
from pathlib import Path

import numpy as np
import torch
from torch.utils.data import DataLoader


ROOT = Path(".")
LABELS = ["entailment", "neutral", "contradiction"]


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def load_glue_mnli(args: argparse.Namespace):
    from datasets import load_dataset, load_from_disk

    if args.data_dir.exists():
        return load_from_disk(str(args.data_dir))
    return load_dataset("glue", "mnli", cache_dir=str(args.cache_dir))


def prepare_dataset(args: argparse.Namespace):
    from transformers import AutoTokenizer, DataCollatorWithPadding

    tokenizer = AutoTokenizer.from_pretrained(args.model_dir, local_files_only=True)
    ds = load_glue_mnli(args)
    eval_split = args.eval_split
    if eval_split not in ds:
        raise KeyError(f"split {eval_split!r} not found in MNLI dataset; available={list(ds.keys())}")

    train_size = min(args.train_samples, len(ds["train"]))
    eval_size = min(args.eval_samples, len(ds[eval_split])) if args.eval_samples else len(ds[eval_split])
    train_ds = ds["train"].shuffle(seed=args.seed).select(range(train_size))
    eval_ds = ds[eval_split].select(range(eval_size))

    def tokenize(batch):
        return tokenizer(
            batch["premise"],
            batch["hypothesis"],
            truncation=True,
            max_length=args.max_length,
        )

    remove_train = [col for col in train_ds.column_names if col != "label"]
    remove_eval = [col for col in eval_ds.column_names if col != "label"]
    train_ds = train_ds.map(tokenize, batched=True, remove_columns=remove_train)
    eval_ds = eval_ds.map(tokenize, batched=True, remove_columns=remove_eval)
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer, return_tensors="pt")
    return train_ds, eval_ds, data_collator


def build_model(args: argparse.Namespace):
    from transformers import AutoConfig, AutoModelForSequenceClassification

    config = AutoConfig.from_pretrained(
        args.model_dir,
        local_files_only=True,
        num_labels=3,
        id2label={i: label for i, label in enumerate(LABELS)},
        label2id={label: i for i, label in enumerate(LABELS)},
    )
    config.problem_type = "single_label_classification"
    return AutoModelForSequenceClassification.from_pretrained(
        args.model_dir,
        config=config,
        local_files_only=True,
        attn_implementation="sdpa",
        ignore_mismatched_sizes=True,
    )


def make_scheduler(optimizer: torch.optim.Optimizer, max_steps: int, warmup_ratio: float):
    warmup_steps = int(max_steps * warmup_ratio)

    def lr_lambda(step: int) -> float:
        if warmup_steps > 0 and step < warmup_steps:
            return float(step + 1) / float(max(1, warmup_steps))
        decay_steps = max(1, max_steps - warmup_steps)
        return max(0.0, float(max_steps - step) / float(decay_steps))

    return torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)


@torch.no_grad()
def evaluate(model: torch.nn.Module, loader: DataLoader, device: torch.device, use_bf16: bool) -> dict[str, float]:
    model.eval()
    correct = 0
    total = 0
    loss_sum = 0.0
    autocast_ctx = torch.autocast(device_type="cuda", dtype=torch.bfloat16) if device.type == "cuda" and use_bf16 else nullcontext()
    for batch in loader:
        batch = {k: v.to(device, non_blocking=True) for k, v in batch.items()}
        labels = batch.pop("labels") if "labels" in batch else batch.pop("label")
        with autocast_ctx:
            outputs = model(**batch, labels=labels)
        preds = outputs.logits.argmax(dim=-1)
        correct += int((preds == labels).sum().item())
        total += int(labels.numel())
        loss_sum += float(outputs.loss.item()) * int(labels.numel())
    acc = correct / max(1, total)
    return {
        "accuracy": acc,
        "accuracy_percent": 100.0 * acc,
        "eval_loss": loss_sum / max(1, total),
        "eval_examples": total,
    }


def train_and_eval(args: argparse.Namespace) -> dict[str, object]:
    set_seed(args.seed)
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    os.environ.setdefault("HF_DATASETS_OFFLINE", "1")
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

    train_ds, eval_ds, data_collator = prepare_dataset(args)
    train_loader = DataLoader(
        train_ds,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=0,
        pin_memory=True,
        collate_fn=data_collator,
    )
    eval_loader = DataLoader(
        eval_ds,
        batch_size=args.eval_batch_size,
        shuffle=False,
        num_workers=0,
        pin_memory=True,
        collate_fn=data_collator,
    )

    device = torch.device("cuda" if torch.cuda.is_available() and not args.cpu else "cpu")
    model = build_model(args).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.learning_rate, weight_decay=args.weight_decay)
    scheduler = make_scheduler(optimizer, args.max_steps, args.warmup_ratio)
    autocast_ctx = torch.autocast(device_type="cuda", dtype=torch.bfloat16) if device.type == "cuda" and args.bf16 else nullcontext()

    losses: list[float] = []
    step = 0
    start = time.time()
    while step < args.max_steps:
        for batch in train_loader:
            model.train()
            batch = {k: v.to(device, non_blocking=True) for k, v in batch.items()}
            labels = batch.pop("labels") if "labels" in batch else batch.pop("label")
            optimizer.zero_grad(set_to_none=True)
            with autocast_ctx:
                loss = model(**batch, labels=labels).loss
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), args.max_grad_norm)
            optimizer.step()
            scheduler.step()
            losses.append(float(loss.item()))
            step += 1
            if step >= args.max_steps:
                break

    metrics = evaluate(model, eval_loader, device, use_bf16=args.bf16)
    result = {
        "task": "modernbert_mnli_accuracy",
        "repo": "ModernBERT",
        "dataset": "glue/mnli",
        "split": args.eval_split,
        "model_dir": str(args.model_dir),
        "data_dir": str(args.data_dir),
        "learning_rate": args.learning_rate,
        "weight_decay": args.weight_decay,
        "warmup_ratio": args.warmup_ratio,
        "batch_size": args.batch_size,
        "eval_batch_size": args.eval_batch_size,
        "max_length": args.max_length,
        "max_steps": args.max_steps,
        "train_samples": min(args.train_samples, len(train_ds)),
        "seed": args.seed,
        "train_loss_final": losses[-1] if losses else math.nan,
        "train_loss_mean_last10": float(np.mean(losses[-10:])) if losses else math.nan,
        "seconds": round(time.time() - start, 3),
        "device": str(device),
        "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES"),
        **metrics,
    }
    args.results_dir.mkdir(parents=True, exist_ok=True)
    (args.results_dir / "results.json").write_text(json.dumps(result, indent=2))
    print("RESULT_JSON " + json.dumps(result, sort_keys=True), flush=True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-dir", type=Path, default=ROOT / "models/modernbert/ModernBERT-base")
    parser.add_argument("--data-dir", type=Path, default=ROOT / "data/paper_exact/modernbert_mnli/glue_mnli")
    parser.add_argument("--cache-dir", type=Path, default=ROOT / "cache")
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--eval-split", default="validation_matched")
    parser.add_argument("--learning-rate", type=float, default=2e-5)
    parser.add_argument("--weight-decay", type=float, default=0.01)
    parser.add_argument("--warmup-ratio", type=float, default=0.1)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--eval-batch-size", type=int, default=128)
    parser.add_argument("--max-length", type=int, default=128)
    parser.add_argument("--max-steps", type=int, default=120)
    parser.add_argument("--train-samples", type=int, default=4096)
    parser.add_argument("--eval-samples", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max-grad-norm", type=float, default=1.0)
    parser.add_argument("--bf16", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--cpu", action="store_true")
    args = parser.parse_args()
    train_and_eval(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

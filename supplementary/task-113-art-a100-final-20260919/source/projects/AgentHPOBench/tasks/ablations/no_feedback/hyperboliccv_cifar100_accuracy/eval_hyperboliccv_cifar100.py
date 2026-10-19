#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


ROOT = Path(".")
REPO = ROOT / "repositories/HyperbolicCV"
CODE = REPO / "code"
DATA_ROOT = ROOT / "data"


def add_repo() -> None:
    os.chdir(CODE)
    for path in (CODE / "classification", CODE):
        text = str(path)
        if text not in sys.path:
            sys.path.insert(0, text)


def model_settings(model_type: str) -> tuple[str, str, str]:
    if model_type == "E":
        return "euclidean", "euclidean", "SGD"
    if model_type == "EL":
        return "euclidean", "lorentz", "RiemannianSGD"
    if model_type == "L":
        return "lorentz", "lorentz", "RiemannianSGD"
    raise ValueError(f"unknown model_type={model_type}")


def make_args(args: argparse.Namespace) -> SimpleNamespace:
    encoder, decoder, optimizer = model_settings(args.model_type)
    milestones = [max(1, args.num_epochs // 2), max(1, int(args.num_epochs * 0.75))]
    return SimpleNamespace(
        embedding_dim=args.embedding_dim,
        num_layers=18,
        encoder_manifold=encoder,
        decoder_manifold=decoder,
        learn_k=args.learn_k,
        encoder_k=args.encoder_k,
        decoder_k=args.decoder_k,
        clip_features=args.clip_features,
        optimizer=optimizer,
        lr=args.lr,
        weight_decay=args.weight_decay,
        use_lr_scheduler=args.use_lr_scheduler,
        lr_scheduler_milestones=milestones,
        lr_scheduler_gamma=args.lr_scheduler_gamma,
    )


def make_loaders(args: argparse.Namespace) -> tuple[DataLoader, DataLoader, int]:
    train_transform = transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize((0.5074, 0.4867, 0.4411), (0.267, 0.256, 0.276)),
    ])
    test_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5074, 0.4867, 0.4411), (0.267, 0.256, 0.276)),
    ])
    if args.dataset == "CIFAR-100":
        train_set = datasets.CIFAR100(DATA_ROOT, train=True, download=False, transform=train_transform)
        test_set = datasets.CIFAR100(DATA_ROOT, train=False, download=False, transform=test_transform)
        num_classes = 100
    else:
        train_set = datasets.CIFAR10(DATA_ROOT, train=True, download=False, transform=train_transform)
        test_set = datasets.CIFAR10(DATA_ROOT, train=False, download=False, transform=test_transform)
        num_classes = 10
    train_loader = DataLoader(
        train_set,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=args.num_workers,
        pin_memory=True,
        drop_last=True,
    )
    test_loader = DataLoader(
        test_set,
        batch_size=args.eval_batch_size,
        shuffle=False,
        num_workers=args.num_workers,
        pin_memory=True,
    )
    return train_loader, test_loader, num_classes


@torch.no_grad()
def evaluate(model: torch.nn.Module, loader: DataLoader, device: torch.device) -> dict[str, float]:
    model.eval()
    total = 0
    correct1 = 0
    correct5 = 0
    loss_sum = 0.0
    for images, labels in loader:
        images = images.to(device, non_blocking=True)
        labels = labels.to(device, non_blocking=True)
        logits = model(images)
        loss = F.cross_entropy(logits, labels)
        top5 = logits.topk(5, dim=1).indices
        correct = top5.eq(labels[:, None])
        total += labels.numel()
        correct1 += int(correct[:, :1].sum().item())
        correct5 += int(correct.sum().item())
        loss_sum += float(loss.item()) * labels.numel()
    return {
        "test_accuracy_percent": 100.0 * correct1 / max(1, total),
        "test_top5_accuracy_percent": 100.0 * correct5 / max(1, total),
        "test_loss": loss_sum / max(1, total),
        "test_examples": total,
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    add_repo()
    from classification.utils.initialize import select_model, select_optimizer

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)
    torch.backends.cudnn.benchmark = True

    device = torch.device(args.device if torch.cuda.is_available() and not args.cpu else "cpu")
    train_loader, test_loader, num_classes = make_loaders(args)
    repo_args = make_args(args)
    model = select_model([3, 32, 32], num_classes, repo_args).to(device)
    optimizer, scheduler = select_optimizer(model, repo_args)

    start = time.time()
    step = 0
    train_loss_last = None
    train_acc_last = None
    for epoch in range(args.num_epochs):
        model.train()
        seen = 0
        correct = 0
        loss_sum = 0.0
        for batch_idx, (images, labels) in enumerate(train_loader):
            if args.train_batches > 0 and batch_idx >= args.train_batches:
                break
            images = images.to(device, non_blocking=True)
            labels = labels.to(device, non_blocking=True)
            logits = model(images)
            loss = F.cross_entropy(logits, labels)
            optimizer.zero_grad(set_to_none=True)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), args.grad_clip)
            optimizer.step()
            pred = logits.argmax(dim=1)
            seen += labels.numel()
            correct += int((pred == labels).sum().item())
            loss_sum += float(loss.item()) * labels.numel()
            step += 1
        if scheduler is not None:
            scheduler.step()
        train_loss_last = loss_sum / max(1, seen)
        train_acc_last = 100.0 * correct / max(1, seen)

    metrics = evaluate(model, test_loader, device)
    result = {
        "task": f"HyperbolicCV {args.dataset} classification",
        "repo": "HyperbolicCV",
        "dataset": args.dataset,
        "metric": "test_accuracy_percent",
        "paper_anchor_accuracy_percent": 78.07 if args.dataset == "CIFAR-100" else 95.14,
        "paper_anchor_source": f"HyperbolicCV README Table 1, {args.dataset} HCNN Lorentz accuracy.",
        "model_type": args.model_type,
        "embedding_dim": args.embedding_dim,
        "lr": args.lr,
        "weight_decay": args.weight_decay,
        "batch_size": args.batch_size,
        "num_epochs": args.num_epochs,
        "train_batches": args.train_batches,
        "optimizer": repo_args.optimizer,
        "use_lr_scheduler": args.use_lr_scheduler,
        "lr_scheduler_gamma": args.lr_scheduler_gamma,
        "learn_k": args.learn_k,
        "encoder_k": args.encoder_k,
        "decoder_k": args.decoder_k,
        "clip_features": args.clip_features,
        "train_steps": step,
        "train_loss_last": train_loss_last,
        "train_accuracy_last_percent": train_acc_last,
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
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--dataset", choices=["CIFAR-10", "CIFAR-100"], default="CIFAR-100")
    parser.add_argument("--model-type", choices=["E", "EL", "L"], default="E")
    parser.add_argument("--embedding-dim", type=int, default=512)
    parser.add_argument("--lr", type=float, default=0.1)
    parser.add_argument("--weight-decay", type=float, default=5e-4)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--eval-batch-size", type=int, default=256)
    parser.add_argument("--num-epochs", type=int, default=2)
    parser.add_argument("--train-batches", type=int, default=200)
    parser.add_argument("--use-lr-scheduler", action=argparse.BooleanOptionalAction, default=False)
    parser.add_argument("--lr-scheduler-gamma", type=float, default=0.2)
    parser.add_argument("--learn-k", action=argparse.BooleanOptionalAction, default=False)
    parser.add_argument("--encoder-k", type=float, default=1.0)
    parser.add_argument("--decoder-k", type=float, default=1.0)
    parser.add_argument("--clip-features", type=float, default=1.0)
    parser.add_argument("--grad-clip", type=float, default=5.0)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--num-workers", type=int, default=4)
    parser.add_argument("--cpu", action="store_true")
    args = parser.parse_args()
    run(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

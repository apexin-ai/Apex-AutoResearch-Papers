#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import random
import sys
import time
import types
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from PIL import Image
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms


ROOT = Path(".")
REPO = ROOT / "repositories/semi-supervised-regression"
DATA = ROOT / "data/formal/rankup_utkface/utkface"
PAPER_ANCHOR_MAE = 4.851


class UTKFaceRegression(Dataset):
    def __init__(self, split: str, transform, max_examples: int = 0) -> None:
        meta = pd.read_csv(DATA / "meta" / f"{split}.csv").sort_values("file_name").reset_index(drop=True)
        if max_examples > 0:
            meta = meta.head(max_examples).copy()
        self.paths = [DATA / "UTKFace" / name for name in meta["file_name"].astype(str).tolist()]
        self.labels = meta["label"].astype("float32").to_numpy()
        self.transform = transform

    def __len__(self) -> int:
        return len(self.paths)

    def __getitem__(self, idx: int):
        image = Image.open(self.paths[idx]).convert("RGB")
        return self.transform(image), torch.tensor(self.labels[idx], dtype=torch.float32)


def build_model(drop_rate: float):
    # Avoid importing semilearn.__init__, which eagerly imports optional audio/NLP deps.
    utils = types.ModuleType("semilearn.nets.utils")
    utils.load_checkpoint = lambda model, pretrained_path=None: model
    sys.modules.setdefault("semilearn", types.ModuleType("semilearn"))
    sys.modules.setdefault("semilearn.nets", types.ModuleType("semilearn.nets"))
    sys.modules["semilearn.nets.utils"] = utils
    spec = importlib.util.spec_from_file_location("autorep_rankup_wrn", REPO / "semilearn/nets/wrn/wrn.py")
    if spec is None or spec.loader is None:
        raise ImportError("could not load RankUp WRN implementation")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    wrn_28_2 = module.wrn_28_2

    return wrn_28_2(drop_rate=drop_rate)


@torch.no_grad()
def evaluate(model: torch.nn.Module, loader: DataLoader, device: torch.device) -> dict[str, float]:
    model.eval()
    total = 0
    abs_sum = 0.0
    mse_sum = 0.0
    for images, labels in loader:
        images = images.to(device, non_blocking=True)
        labels = labels.to(device, non_blocking=True)
        output = model(images)
        preds = output["logits"] if isinstance(output, dict) else output
        err = preds.float() - labels.float()
        total += labels.numel()
        abs_sum += float(err.abs().sum().item())
        mse_sum += float((err**2).sum().item())
    return {"MAE": abs_sum / max(1, total), "MSE": mse_sum / max(1, total), "eval_examples": total}


def run(args: argparse.Namespace) -> dict[str, Any]:
    if not (DATA / "UTKFace").is_dir():
        raise FileNotFoundError(f"missing UTKFace data under {DATA}; run dataset_download.sh")
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)
    torch.backends.cudnn.benchmark = True

    train_tfms = [
        transforms.Resize((args.img_size, args.img_size)),
    ]
    if args.augment:
        train_tfms.extend([transforms.RandomHorizontalFlip(), transforms.RandomCrop(args.img_size, padding=4)])
    train_tfms.extend([
        transforms.ToTensor(),
        transforms.Normalize([0.59632254, 0.45671629, 0.39103324], [0.25907077, 0.23132719, 0.22686818]),
    ])
    eval_transform = transforms.Compose([
        transforms.Resize((args.img_size, args.img_size)),
        transforms.ToTensor(),
        transforms.Normalize([0.59632254, 0.45671629, 0.39103324], [0.25907077, 0.23132719, 0.22686818]),
    ])
    train_set = UTKFaceRegression("train", transforms.Compose(train_tfms), max_examples=args.train_examples)
    test_set = UTKFaceRegression("test", eval_transform, max_examples=args.eval_examples)
    train_loader = DataLoader(train_set, batch_size=args.batch_size, shuffle=True, num_workers=args.num_workers, pin_memory=True, drop_last=True)
    test_loader = DataLoader(test_set, batch_size=args.eval_batch_size, shuffle=False, num_workers=args.num_workers, pin_memory=True)

    device = torch.device("cuda" if torch.cuda.is_available() and not args.cpu else "cpu")
    model = build_model(args.drop_rate).to(device)
    optimizer = torch.optim.SGD(model.parameters(), lr=args.lr, momentum=args.momentum, weight_decay=args.weight_decay)

    started = time.time()
    steps = 0
    train_iter = iter(train_loader)
    last_loss = None
    while steps < args.train_steps:
        try:
            images, labels = next(train_iter)
        except StopIteration:
            train_iter = iter(train_loader)
            images, labels = next(train_iter)
        images = images.to(device, non_blocking=True)
        labels = labels.to(device, non_blocking=True)
        model.train()
        output = model(images)
        preds = output["logits"] if isinstance(output, dict) else output
        loss = F.l1_loss(preds.float(), labels.float())
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        if args.clip_grad > 0:
            torch.nn.utils.clip_grad_norm_(model.parameters(), args.clip_grad)
        optimizer.step()
        last_loss = float(loss.item())
        steps += 1

    metrics = evaluate(model, test_loader, device)
    result = {
        "task": "RankUp UTKFace age regression",
        "repo": "semi-supervised-regression",
        "dataset": "UTKFace",
        "metric": "MAE",
        "lower_is_better": True,
        "paper_anchor_MAE": PAPER_ANCHOR_MAE,
        "paper_anchor_source": "classic_cv_average_log.csv fullysupervised_utkface min_MAE",
        "config": {
            "lr": args.lr,
            "weight_decay": args.weight_decay,
            "momentum": args.momentum,
            "batch_size": args.batch_size,
            "train_steps": args.train_steps,
            "train_examples": args.train_examples,
            "eval_examples": args.eval_examples,
            "augment": args.augment,
            "drop_rate": args.drop_rate,
            "img_size": args.img_size,
            "seed": args.seed,
        },
        "train_loss_last": last_loss,
        "train_steps": steps,
        "train_examples_seen": steps * args.batch_size,
        "seconds": round(time.time() - started, 3),
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
    parser.add_argument("--lr", type=float, default=0.01)
    parser.add_argument("--weight-decay", type=float, default=0.001)
    parser.add_argument("--momentum", type=float, default=0.9)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--eval-batch-size", type=int, default=256)
    parser.add_argument("--train-steps", type=int, default=400)
    parser.add_argument("--train-examples", type=int, default=0)
    parser.add_argument("--eval-examples", type=int, default=0)
    parser.add_argument("--img-size", type=int, default=40)
    parser.add_argument("--drop-rate", type=float, default=0.0)
    parser.add_argument("--clip-grad", type=float, default=0.0)
    parser.add_argument("--num-workers", type=int, default=4)
    parser.add_argument("--no-augment", dest="augment", action="store_false")
    parser.set_defaults(augment=True)
    parser.add_argument("--cpu", action="store_true")
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    run(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

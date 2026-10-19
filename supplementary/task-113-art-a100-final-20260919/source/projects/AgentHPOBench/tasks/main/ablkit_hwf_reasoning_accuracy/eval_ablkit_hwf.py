#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import random
import sys
import time
from pathlib import Path

import numpy as np
import torch
from torch import nn
from PIL import Image
from torchvision import transforms

from ablkit.bridge import SimpleBridge
from ablkit.data.evaluation import ReasoningMetric, SymbolAccuracy
from ablkit.learning import ABLModel, BasicNN
from ablkit.reasoning import GroundKB, KBBase, Reasoner


ROOT = Path(".")
HWF_DIR = ROOT / "repositories/ABLkit/examples/hwf"
SYMBOLS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/"]
IMG_TRANSFORM = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (1,))])


class HwfKB(KBBase):
    def __init__(self, pseudo_label_list=SYMBOLS, max_err=1e-10):
        super().__init__(pseudo_label_list, max_err)

    def _valid_candidate(self, formula):
        if len(formula) % 2 == 0:
            return False
        for i, token in enumerate(formula):
            if i % 2 == 0 and token not in SYMBOLS[:9]:
                return False
            if i % 2 != 0 and token not in SYMBOLS[9:]:
                return False
        return True

    def logic_forward(self, formula):
        if not self._valid_candidate(formula):
            return np.inf
        return eval("".join(formula))


class HwfGroundKB(GroundKB):
    def __init__(self, pseudo_label_list=SYMBOLS, GKB_len_list=[1, 3, 5, 7], max_err=1e-10):
        super().__init__(pseudo_label_list, GKB_len_list, max_err)

    def _valid_candidate(self, formula):
        return HwfKB(self.pseudo_label_list, self.max_err)._valid_candidate(formula)

    def logic_forward(self, formula):
        if not self._valid_candidate(formula):
            return np.inf
        return eval("".join(formula))


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.benchmark = True


def subset(data, limit: int):
    if limit <= 0:
        return data
    x, pseudo, y = data
    return x[:limit], pseudo[:limit], y[:limit]


def load_data(train_limit: int, test_limit: int):
    def get_dataset(train: bool):
        data_dir = HWF_DIR / "datasets/data"
        json_file = data_dir / ("expr_train.json" if train else "expr_test.json")
        img_dir = data_dir / "Handwritten_Math_Symbols"
        with json_file.open() as f:
            raw = json.load(f)
        x, pseudo, y = [], [], []
        for item in raw:
            imgs, labels = [], []
            for img_path in item["img_paths"]:
                img = Image.open(img_dir / img_path).convert("L")
                imgs.append(IMG_TRANSFORM(img))
                label = img_path.split("/")[0]
                labels.append({"times": "*", "div": "/"}.get(label, label))
            x.append(imgs)
            pseudo.append(labels)
            y.append(item["res"])
        return x, pseudo, y

    train_data = get_dataset(train=True)
    test_data = get_dataset(train=False)
    return subset(train_data, train_limit), subset(test_data, test_limit)


def flatten(data):
    x, pseudo, y = data
    flat_x = []
    flat_labels = []
    for formula, labels in zip(x, pseudo):
        flat_x.extend(formula)
        flat_labels.extend(labels)
    return flat_x, flat_labels, y


@torch.no_grad()
def evaluate_basic(base_model: BasicNN, data, max_err: float) -> dict[str, float]:
    x, pseudo, y = data
    flat_x, flat_labels, _ = flatten(data)
    pred_idx = base_model.predict(X=flat_x).astype(int).tolist()
    pred_labels = [SYMBOLS[idx] if 0 <= idx < len(SYMBOLS) else "?" for idx in pred_idx]
    symbol_correct = sum(int(a == b) for a, b in zip(pred_labels, flat_labels))
    offset = 0
    reason_correct = 0
    valid = 0
    by_len: dict[int, list[int]] = {}
    for formula, target in zip(x, y):
        length = len(formula)
        pred_formula = pred_labels[offset : offset + length]
        offset += length
        ok = False
        try:
            if length % 2 == 1 and all(pred_formula[i] in (SYMBOLS[:9] if i % 2 == 0 else SYMBOLS[9:]) for i in range(length)):
                value = eval("".join(pred_formula))
                valid += 1
                ok = math.isfinite(float(value)) and abs(float(value) - float(target)) <= max_err
        except Exception:
            ok = False
        reason_correct += int(ok)
        by_len.setdefault(length, [0, 0])
        by_len[length][0] += int(ok)
        by_len[length][1] += 1
    per_len = {str(k): 100.0 * v[0] / max(1, v[1]) for k, v in sorted(by_len.items())}
    return {
        "symbol_accuracy_percent": 100.0 * symbol_correct / max(1, len(flat_labels)),
        "reasoning_accuracy_percent": 100.0 * reason_correct / max(1, len(y)),
        "valid_formula_percent": 100.0 * valid / max(1, len(y)),
        "num_examples": len(y),
        "num_symbols": len(flat_labels),
        "reasoning_accuracy_by_length_percent": per_len,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", required=True)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--label-smoothing", type=float, default=0.2)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--segment-size", type=int, default=1000)
    parser.add_argument("--loops", type=int, default=3)
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--max-revision", type=int, default=-1)
    parser.add_argument("--require-more-revision", type=int, default=0)
    parser.add_argument("--ground", action="store_true")
    parser.add_argument("--max-err", type=float, default=1e-10)
    parser.add_argument("--train-limit", type=int, default=0)
    parser.add_argument("--test-limit", type=int, default=0)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--device", default="cuda:0")
    args = parser.parse_args()

    set_seed(args.seed)
    out_dir = Path(args.results_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    started = time.time()

    sys.path.insert(0, str(HWF_DIR))
    from models.nn import SymbolNet

    train_data, test_data = load_data(args.train_limit, args.test_limit)
    cls = SymbolNet(num_classes=len(SYMBOLS), image_size=(45, 45, 1))
    loss_fn = nn.CrossEntropyLoss(label_smoothing=args.label_smoothing)
    optimizer = torch.optim.Adam(cls.parameters(), lr=args.lr)
    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    base_model = BasicNN(
        cls,
        loss_fn,
        optimizer,
        device=device,
        batch_size=args.batch_size,
        num_epochs=args.epochs,
        num_workers=0,
    )
    model = ABLModel(base_model)
    kb = HwfGroundKB(max_err=args.max_err) if args.ground else HwfKB(max_err=args.max_err)
    reasoner = Reasoner(kb, max_revision=args.max_revision, require_more_revision=args.require_more_revision)
    metric_list = [SymbolAccuracy(prefix="hwf"), ReasoningMetric(kb=kb, prefix="hwf")]
    bridge = SimpleBridge(model, reasoner, metric_list)
    bridge.train(
        train_data,
        val_data=test_data,
        loops=args.loops,
        segment_size=args.segment_size,
        eval_interval=args.loops,
    )
    bridge.test(test_data)

    train_metrics = evaluate_basic(base_model, train_data, args.max_err)
    test_metrics = evaluate_basic(base_model, test_data, args.max_err)
    payload = {
        "task": "ablkit_hwf_reasoning_accuracy",
        "repo": "ABLkit",
        "dataset": "HWF",
        "metric": "reasoning_accuracy_percent",
        "config": vars(args),
        "dataset_sizes": {
            "train": len(train_data[2]),
            "test": len(test_data[2]),
            "hwf_dir": str(HWF_DIR / "datasets/data"),
        },
        "train": train_metrics,
        "test": test_metrics,
        "reasoning_accuracy_percent": test_metrics["reasoning_accuracy_percent"],
        "symbol_accuracy_percent": test_metrics["symbol_accuracy_percent"],
        "seconds": round(time.time() - started, 3),
        "device": str(device),
    }
    (out_dir / "results.json").write_text(json.dumps(payload, indent=2))
    print("RESULT_JSON " + json.dumps(payload, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

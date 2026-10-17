#!/usr/bin/env python3
"""N2 rebuttal: end-to-end transformer finetune baseline for depth classification."""

import argparse
import json
import os
import time
from pathlib import Path

import numpy as np
import torch
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    precision_recall_fscore_support,
    roc_auc_score,
)
from sklearn.model_selection import StratifiedKFold
from torch.utils.data import DataLoader, Dataset
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    get_linear_schedule_with_warmup,
)


class DepthTextDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len=512):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        enc = self.tokenizer(
            self.texts[idx],
            truncation=True,
            max_length=self.max_len,
            padding="max_length",
            return_tensors="pt",
        )
        return {
            "input_ids": enc["input_ids"].squeeze(0),
            "attention_mask": enc["attention_mask"].squeeze(0),
            "labels": torch.tensor(self.labels[idx], dtype=torch.long),
        }


def load_data(data_dir, num_classes=4):
    texts, labels = [], []
    for d in range(num_classes):
        path = Path(data_dir) / f"depth_{d}.jsonl"
        if not path.exists():
            raise FileNotFoundError(f"Missing {path}")
        with open(path) as f:
            for line in f:
                obj = json.loads(line)
                texts.append(obj["text"])
                labels.append(d)
    return texts, np.array(labels)


def compute_pairwise_auc(labels, probs, pairs=((0, 1), (1, 2), (2, 3))):
    results = {}
    for a, b in pairs:
        mask = np.isin(labels, [a, b])
        if mask.sum() == 0:
            continue
        y_bin = (labels[mask] == b).astype(int)
        if len(np.unique(y_bin)) < 2:
            results[f"d{a}v{b}"] = float("nan")
            continue
        p_b = probs[mask, b] / (probs[mask, a] + probs[mask, b] + 1e-12)
        if np.isnan(p_b).any():
            results[f"d{a}v{b}"] = float("nan")
            continue
        auc = roc_auc_score(y_bin, p_b)
        results[f"d{a}v{b}"] = round(auc, 4)
    return results


def train_one_fold(
    model, tokenizer, train_texts, train_labels, val_texts, val_labels, args
):
    train_ds = DepthTextDataset(train_texts, train_labels, tokenizer, args.max_len)
    val_ds = DepthTextDataset(val_texts, val_labels, tokenizer, args.max_len)

    train_loader = DataLoader(
        train_ds, batch_size=args.batch_size, shuffle=True, num_workers=2, pin_memory=True
    )
    val_loader = DataLoader(
        val_ds, batch_size=args.batch_size * 2, shuffle=False, num_workers=2, pin_memory=True
    )

    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=0.01)
    total_steps = len(train_loader) * args.epochs
    warmup_steps = int(total_steps * args.warmup_ratio)
    scheduler = get_linear_schedule_with_warmup(optimizer, warmup_steps, total_steps)

    device = next(model.parameters()).device
    best_val_acc = 0.0
    best_state = None

    for epoch in range(args.epochs):
        model.train()
        total_loss = 0.0
        for step, batch in enumerate(train_loader):
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(**batch)
            loss = outputs.loss
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            scheduler.step()
            optimizer.zero_grad()
            total_loss += loss.item()

            if step % 50 == 0:
                print(
                    f"  step {step}/{len(train_loader)} loss={loss.item():.4f}",
                    flush=True,
                )

        avg_loss = total_loss / len(train_loader)

        model.eval()
        all_preds, all_labels, all_probs = [], [], []
        with torch.no_grad():
            for batch in val_loader:
                batch = {k: v.to(device) for k, v in batch.items()}
                outputs = model(**batch)
                logits = outputs.logits
                probs = torch.softmax(logits, dim=-1).cpu().numpy()
                preds = logits.argmax(dim=-1).cpu().numpy()
                all_preds.extend(preds)
                all_labels.extend(batch["labels"].cpu().numpy())
                all_probs.append(probs)

        all_probs = np.vstack(all_probs)
        val_acc = accuracy_score(all_labels, all_preds)
        print(
            f"  epoch {epoch+1}/{args.epochs} train_loss={avg_loss:.4f} val_acc={val_acc:.4f}",
            flush=True,
        )

        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}

    if best_state is not None:
        model.load_state_dict(best_state)

    model.eval()
    all_preds, all_labels, all_probs = [], [], []
    with torch.no_grad():
        for batch in val_loader:
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(**batch)
            logits = outputs.logits
            probs = torch.softmax(logits, dim=-1).cpu().numpy()
            preds = logits.argmax(dim=-1).cpu().numpy()
            all_preds.extend(preds)
            all_labels.extend(batch["labels"].cpu().numpy())
            all_probs.append(probs)

    all_probs = np.vstack(all_probs)
    all_preds = np.array(all_preds)
    all_labels = np.array(all_labels)

    return all_preds, all_labels, all_probs


def main():
    parser = argparse.ArgumentParser(description="N2: Transformer finetune baseline")
    parser.add_argument(
        "--model_name",
        type=str,
        default="microsoft/deberta-v3-base",
        help="HuggingFace model name",
    )
    parser.add_argument(
        "--data_dir",
        type=str,
        default="data",
        help="Directory containing depth_*.jsonl files",
    )
    parser.add_argument("--output_dir", type=str, default="results/n2_deberta_finetune")
    parser.add_argument("--max_len", type=int, default=512)
    parser.add_argument("--batch_size", type=int, default=16)
    parser.add_argument("--lr", type=float, default=2e-5)
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--warmup_ratio", type=float, default=0.1)
    parser.add_argument("--n_folds", type=int, default=5)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--dry_run", action="store_true", help="Run 10 steps on 1 fold only"
    )
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    if torch.cuda.is_available():
        device = torch.device(f"cuda:{args.gpu}")
        print(f"Using GPU: {torch.cuda.get_device_name(args.gpu)}")
    else:
        device = torch.device("cpu")
        print("Using CPU")

    print(f"Model: {args.model_name}")
    print(f"Loading data from {args.data_dir}...")
    texts, labels = load_data(args.data_dir)
    print(f"Loaded {len(texts)} samples, class distribution: {np.bincount(labels)}")

    print(f"Loading tokenizer and model...")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)

    os.makedirs(args.output_dir, exist_ok=True)
    skf = StratifiedKFold(n_splits=args.n_folds, shuffle=True, random_state=args.seed)

    fold_results = []
    all_fold_preds = np.zeros(len(labels), dtype=int)
    all_fold_probs = np.zeros((len(labels), 4))
    fold_indices = []

    t0 = time.time()
    for fold_idx, (train_idx, val_idx) in enumerate(skf.split(texts, labels)):
        print(f"\n{'='*60}")
        print(f"Fold {fold_idx+1}/{args.n_folds}")
        print(f"{'='*60}")

        train_texts = [texts[i] for i in train_idx]
        train_labels = labels[train_idx]
        val_texts = [texts[i] for i in val_idx]
        val_labels = labels[val_idx]

        model = AutoModelForSequenceClassification.from_pretrained(
            args.model_name, num_labels=4, dtype=torch.float32
        )
        model.to(device)

        if args.dry_run:
            train_texts = train_texts[:64]
            train_labels = train_labels[:64]
            val_texts = val_texts[:64]
            val_labels = val_labels[:64]
            val_idx = val_idx[:64]
            args.epochs = 1

        preds, true_labels, probs = train_one_fold(
            model, tokenizer, train_texts, train_labels, val_texts, val_labels, args
        )

        acc = accuracy_score(true_labels, preds)
        prec, rec, f1, _ = precision_recall_fscore_support(
            true_labels, preds, average=None, labels=[0, 1, 2, 3], zero_division=0
        )
        pairwise_auc = compute_pairwise_auc(true_labels, probs)

        fold_result = {
            "fold": fold_idx,
            "accuracy": round(acc, 4),
            "per_class_precision": [round(x, 4) for x in prec],
            "per_class_recall": [round(x, 4) for x in rec],
            "per_class_f1": [round(x, 4) for x in f1],
            "pairwise_auc": pairwise_auc,
        }
        fold_results.append(fold_result)
        print(f"Fold {fold_idx+1} accuracy: {acc:.4f}")
        print(f"Pairwise AUC: {pairwise_auc}")

        all_fold_preds[val_idx] = preds
        all_fold_probs[val_idx] = probs
        fold_indices.append(val_idx.tolist())

        del model
        torch.cuda.empty_cache()

        if args.dry_run:
            print("Dry run: stopping after 1 fold")
            break

    elapsed = time.time() - t0

    accs = [r["accuracy"] for r in fold_results]
    macro_prec, macro_rec, macro_f1, _ = precision_recall_fscore_support(
        labels[np.concatenate([np.array(fi) for fi in fold_indices])],
        all_fold_preds[np.concatenate([np.array(fi) for fi in fold_indices])],
        average=None,
        labels=[0, 1, 2, 3],
        zero_division=0,
    )

    all_auc_keys = ["d0v1", "d1v2", "d2v3"]
    avg_auc = {}
    for k in all_auc_keys:
        vals = [r["pairwise_auc"][k] for r in fold_results if k in r["pairwise_auc"] and not np.isnan(r["pairwise_auc"][k])]
        avg_auc[k] = round(np.mean(vals), 4) if vals else float("nan")

    summary = {
        "model": args.model_name,
        "n_folds": len(fold_results),
        "accuracy_mean": round(np.mean(accs), 4),
        "accuracy_std": round(np.std(accs), 4),
        "per_class_precision": [round(x, 4) for x in macro_prec],
        "per_class_recall": [round(x, 4) for x in macro_rec],
        "per_class_f1": [round(x, 4) for x in macro_f1],
        "pairwise_auc_mean": avg_auc,
        "elapsed_seconds": round(elapsed, 1),
        "fold_results": fold_results,
        "config": {
            "max_len": args.max_len,
            "batch_size": args.batch_size,
            "lr": args.lr,
            "epochs": args.epochs,
            "warmup_ratio": args.warmup_ratio,
            "seed": args.seed,
        },
    }

    def sanitize_for_json(obj):
        if isinstance(obj, float) and np.isnan(obj):
            return None
        if isinstance(obj, dict):
            return {k: sanitize_for_json(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [sanitize_for_json(v) for v in obj]
        return obj

    results_path = Path(args.output_dir) / "results.json"
    with open(results_path, "w") as f:
        json.dump(sanitize_for_json(summary), f, indent=2)
    print(f"\nResults saved to {results_path}")

    preds_path = Path(args.output_dir) / "fold_predictions.npz"
    np.savez(
        preds_path,
        preds=all_fold_preds,
        probs=all_fold_probs,
        labels=labels,
        fold_indices=np.array(fold_indices, dtype=object),
    )
    print(f"Predictions saved to {preds_path}")

    print(f"\n{'='*60}")
    print(f"SUMMARY: {args.model_name}")
    print(f"{'='*60}")
    print(f"Accuracy: {summary['accuracy_mean']:.4f} ± {summary['accuracy_std']:.4f}")
    print(f"Per-class F1: {[float(x) for x in summary['per_class_f1']]}")
    print(f"Pairwise AUC: {summary['pairwise_auc_mean']}")
    print(f"Time: {elapsed:.0f}s")


if __name__ == "__main__":
    main()

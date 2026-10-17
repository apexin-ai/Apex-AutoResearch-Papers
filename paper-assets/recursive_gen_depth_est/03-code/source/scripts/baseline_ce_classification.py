"""
Baseline 4: Standard Cross-Entropy Classification for recursive generation depth estimation.

Standard 4-class classification with DeBERTa backbone and CE loss.
No ordinal awareness — serves as ablation for DCOL and CORAL to demonstrate
that ordinal-aware losses add value.

Architecture: DeBERTa → [CLS] pooling → Linear(hidden, 4) → CrossEntropyLoss
Default: DeBERTa-v3-large (435M) to match DCOL backbone for fair comparison.

Input:  Raw depth_*.jsonl files (--data_dirs)
Output: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json

Usage:
  python baseline_ce_classification.py --data_dirs data/  # default: deberta-v3-large
  python baseline_ce_classification.py --data_dirs data/ --model_name microsoft/deberta-v3-base --model_path /root/autodl-tmp/models/deberta-v3-base
  python baseline_ce_classification.py --data_dirs data/ --dry_run  # CPU, 2 steps
"""

import argparse
import random
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from transformers import AutoModel, AutoTokenizer

from baseline_utils import (
    load_jsonl_data, stratified_split, evaluate_and_save,
    add_common_args, NUM_DEPTHS,
)


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


class DepthTextDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_seq_len):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_seq_len = max_seq_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        enc = self.tokenizer(
            self.texts[idx],
            max_length=self.max_seq_len,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        )
        return {
            "input_ids": enc["input_ids"].squeeze(0),
            "attention_mask": enc["attention_mask"].squeeze(0),
            "label": torch.tensor(self.labels[idx], dtype=torch.long),
        }


class CEClassifier(nn.Module):
    """DeBERTa + linear head with standard cross-entropy loss."""

    def __init__(self, model_name_or_path, num_classes=NUM_DEPTHS, dropout=0.1):
        super().__init__()
        self.encoder = AutoModel.from_pretrained(model_name_or_path)
        hidden_size = self.encoder.config.hidden_size
        self.dropout = nn.Dropout(dropout)
        self.classifier = nn.Linear(hidden_size, num_classes)

    def forward(self, input_ids, attention_mask):
        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
        cls_repr = outputs.last_hidden_state[:, 0, :]
        cls_repr = self.dropout(cls_repr)
        logits = self.classifier(cls_repr)
        return logits


def train_epoch(model, loader, optimizer, criterion, device, scaler, max_steps=None):
    model.train()
    total_loss, total_correct, total_samples = 0.0, 0, 0
    for step, batch in enumerate(loader):
        if max_steps and step >= max_steps:
            break
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        labels = batch["label"].to(device)

        optimizer.zero_grad()
        with torch.amp.autocast("cuda", enabled=scaler is not None):
            logits = model(input_ids, attention_mask)
            loss = criterion(logits, labels)

        if scaler is not None:
            scaler.scale(loss).backward()
            scaler.unscale_(optimizer)
            nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            scaler.step(optimizer)
            scaler.update()
        else:
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()

        total_loss += loss.item() * len(labels)
        total_correct += (logits.argmax(dim=-1) == labels).sum().item()
        total_samples += len(labels)

    return total_loss / max(total_samples, 1), total_correct / max(total_samples, 1)


@torch.no_grad()
def evaluate_model(model, loader, criterion, device, max_steps=None):
    model.eval()
    total_loss, all_preds, all_labels, all_probs = 0.0, [], [], []
    total_samples = 0
    for step, batch in enumerate(loader):
        if max_steps and step >= max_steps:
            break
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        labels = batch["label"].to(device)

        logits = model(input_ids, attention_mask)
        loss = criterion(logits, labels)

        total_loss += loss.item() * len(labels)
        total_samples += len(labels)
        probs = torch.softmax(logits, dim=-1)
        all_preds.append(logits.argmax(dim=-1).cpu().numpy())
        all_labels.append(labels.cpu().numpy())
        all_probs.append(probs.cpu().numpy())

    return (
        total_loss / max(total_samples, 1),
        np.concatenate(all_preds),
        np.concatenate(all_labels),
        np.concatenate(all_probs),
    )


def main():
    parser = argparse.ArgumentParser(description="Standard CE Classification baseline (DeBERTa)")
    add_common_args(parser)
    parser.add_argument("--model_name", default="microsoft/deberta-v3-large")
    parser.add_argument("--model_path", default="/root/autodl-tmp/models/deberta-v3-large")
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--batch_size", type=int, default=16)
    parser.add_argument("--lr", type=float, default=2e-5)
    parser.add_argument("--warmup_ratio", type=float, default=0.1)
    parser.add_argument("--patience", type=int, default=3)
    parser.add_argument("--dropout", type=float, default=0.1)
    parser.add_argument("--fp16", action="store_true")
    parser.add_argument("--dry_run", action="store_true", help="CPU dry-run, 2 steps only")
    args = parser.parse_args()

    set_seed(args.seed)
    device = torch.device("cpu") if args.dry_run else torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    texts, labels = load_jsonl_data(args.data_dirs, max_samples=args.max_samples, seed=args.seed)
    if args.dry_run and len(texts) > 64:
        texts, labels = texts[:64], labels[:64]

    train_idx, eval_idx = stratified_split(labels, eval_split=args.eval_split, seed=args.seed)
    train_texts = [texts[i] for i in train_idx]
    eval_texts = [texts[i] for i in eval_idx]
    train_labels, eval_labels = labels[train_idx], labels[eval_idx]
    print(f"Train: {len(train_labels)}, Eval: {len(eval_labels)}")

    tokenizer = AutoTokenizer.from_pretrained(args.model_path)
    train_ds = DepthTextDataset(train_texts, train_labels, tokenizer, args.max_seq_len)
    eval_ds = DepthTextDataset(eval_texts, eval_labels, tokenizer, args.max_seq_len)
    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True, num_workers=2, pin_memory=True)
    eval_loader = DataLoader(eval_ds, batch_size=args.batch_size * 2, shuffle=False, num_workers=2, pin_memory=True)

    model = CEClassifier(args.model_path, dropout=args.dropout).to(device).float()
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=0.01)
    criterion = nn.CrossEntropyLoss()
    scaler = torch.amp.GradScaler("cuda") if (args.fp16 and device.type == "cuda") else None

    total_steps = len(train_loader) * args.epochs
    warmup_steps = int(total_steps * args.warmup_ratio)
    scheduler = torch.optim.lr_scheduler.LinearLR(
        optimizer, start_factor=0.1, total_iters=warmup_steps,
    )

    max_steps_per_epoch = 2 if args.dry_run else None
    best_eval_loss = float("inf")
    patience_counter = 0

    for epoch in range(args.epochs):
        train_loss, train_acc = train_epoch(
            model, train_loader, optimizer, criterion, device, scaler, max_steps=max_steps_per_epoch,
        )
        scheduler.step()

        eval_loss, y_pred, y_true, y_prob = evaluate_model(
            model, eval_loader, criterion, device, max_steps=max_steps_per_epoch,
        )
        print(f"Epoch {epoch+1}/{args.epochs}  train_loss={train_loss:.4f}  "
              f"train_acc={train_acc:.4f}  eval_loss={eval_loss:.4f}")

        if eval_loss < best_eval_loss - 1e-4:
            best_eval_loss = eval_loss
            patience_counter = 0
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            best_preds = (y_true.copy(), y_pred.copy(), y_prob.copy())
        else:
            patience_counter += 1
            if patience_counter >= args.patience:
                print(f"Early stopping at epoch {epoch+1}")
                break

        if args.dry_run:
            print("Dry run complete (2 steps). Pipeline OK.")
            return

    model.load_state_dict({k: v.to(device) for k, v in best_state.items()})
    y_true, y_pred, y_prob = best_preds
    model_tag = "large" if "large" in args.model_name else "base"
    evaluate_and_save(f"ce_deberta_{model_tag}", y_true, y_pred, y_prob, args.output_dir)


if __name__ == "__main__":
    main()

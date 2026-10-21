"""
Baseline 3: CORAL (Consistent Rank Logits) for recursive generation depth estimation.

Classic ordinal classification method (Cao, Mirjalili & Raschka, 2020).
Converts K-class ordinal problem into K-1 binary decisions sharing a backbone.

Architecture: DeBERTa → [CLS] → shared Linear(hidden, 1) + K-1 bias terms
Each head k outputs logit for P(depth > k), k = 0..K-2.
Default: DeBERTa-v3-large (435M) to match DCOL backbone for fair comparison.

CORAL loss (rank-consistent):
  L = Σ_{k=0}^{K-2} BCE(σ(w^T h + b_k), 𝟙[y > k])
where w is shared across thresholds and b_k is per-threshold bias.

Prediction: depth = Σ_k 𝟙[σ(w^T h + b_k) > 0.5]

Ref: Cao, W., Mirjalili, V. & Raschka, S. (2020). "Rank consistent ordinal
     regression for neural networks with consistent confidence sets."
     Pattern Recognition, 108, 107736.

Input:  Raw depth_*.jsonl files (--data_dirs)
Output: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json

Usage:
  python baseline_coral.py --data_dirs data/  # default: deberta-v3-large
  python baseline_coral.py --data_dirs data/ --model_name microsoft/deberta-v3-base --model_path /root/autodl-tmp/models/deberta-v3-base
  python baseline_coral.py --data_dirs data/ --dry_run
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


class CORALModel(nn.Module):
    """
    DeBERTa + CORAL ordinal head.

    The CORAL head has:
      - One shared weight vector w (Linear(hidden, 1, bias=False))
      - K-1 independent bias terms b_k
    Output: K-1 logits, logit_k = w^T h + b_k
    """

    def __init__(self, model_name_or_path, num_classes=NUM_DEPTHS, dropout=0.1):
        super().__init__()
        self.num_thresholds = num_classes - 1
        self.encoder = AutoModel.from_pretrained(model_name_or_path)
        hidden_size = self.encoder.config.hidden_size
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(hidden_size, 1, bias=False)
        self.biases = nn.Parameter(torch.zeros(self.num_thresholds))

    def forward(self, input_ids, attention_mask):
        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
        cls_repr = outputs.last_hidden_state[:, 0, :]
        cls_repr = self.dropout(cls_repr)
        logit_base = self.fc(cls_repr)  # [B, 1]
        logits = logit_base + self.biases  # [B, K-1] broadcast
        return logits


def coral_loss(logits, labels, num_classes=NUM_DEPTHS):
    """
    CORAL rank-consistent loss.

    For each threshold k (0..K-2), construct binary target 𝟙[y > k]
    and compute BCE with logits.
    """
    num_thresholds = num_classes - 1
    ordinal_targets = torch.zeros(len(labels), num_thresholds,
                                  device=labels.device, dtype=logits.dtype)
    for k in range(num_thresholds):
        ordinal_targets[:, k] = (labels > k).float()
    return nn.functional.binary_cross_entropy_with_logits(logits, ordinal_targets)


def coral_predict(logits):
    """depth = number of thresholds where σ(logit) > 0.5"""
    probs = torch.sigmoid(logits)
    return (probs > 0.5).sum(dim=-1).long()


def coral_predict_proba(logits, num_classes=NUM_DEPTHS):
    """
    Convert cumulative probabilities to per-class probabilities.
    P(d=0) = 1 - P(d>0)
    P(d=k) = P(d>k-1) - P(d>k)  for k=1..K-2
    P(d=K-1) = P(d>K-2)
    """
    cum_probs = torch.sigmoid(logits).cpu().numpy()  # [B, K-1]
    n = cum_probs.shape[0]
    probs = np.zeros((n, num_classes))
    probs[:, 0] = 1.0 - cum_probs[:, 0]
    for k in range(1, num_classes - 1):
        probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]
    probs[:, num_classes - 1] = cum_probs[:, num_classes - 2]
    probs = np.clip(probs, 0, 1)
    row_sums = probs.sum(axis=1, keepdims=True)
    probs = probs / np.where(row_sums > 0, row_sums, 1.0)
    return probs


def train_epoch(model, loader, optimizer, device, scaler, max_steps=None):
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
            loss = coral_loss(logits, labels)

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

        preds = coral_predict(logits)
        total_loss += loss.item() * len(labels)
        total_correct += (preds == labels).sum().item()
        total_samples += len(labels)

    return total_loss / max(total_samples, 1), total_correct / max(total_samples, 1)


@torch.no_grad()
def evaluate_model(model, loader, device, max_steps=None):
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
        loss = coral_loss(logits, labels)

        total_loss += loss.item() * len(labels)
        total_samples += len(labels)
        all_preds.append(coral_predict(logits).cpu().numpy())
        all_labels.append(labels.cpu().numpy())
        all_probs.append(coral_predict_proba(logits))

    return (
        total_loss / max(total_samples, 1),
        np.concatenate(all_preds),
        np.concatenate(all_labels),
        np.concatenate(all_probs),
    )


def main():
    parser = argparse.ArgumentParser(description="CORAL ordinal classification baseline (DeBERTa)")
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

    model = CORALModel(args.model_path, dropout=args.dropout).to(device).float()
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=0.01)
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
            model, train_loader, optimizer, device, scaler, max_steps=max_steps_per_epoch,
        )
        scheduler.step()

        eval_loss, y_pred, y_true, y_prob = evaluate_model(
            model, eval_loader, device, max_steps=max_steps_per_epoch,
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
    evaluate_and_save(f"coral_deberta_{model_tag}", y_true, y_pred, y_prob, args.output_dir)


if __name__ == "__main__":
    main()

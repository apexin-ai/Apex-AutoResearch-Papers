"""
DCOL: DeBERTa + Contrastive Ordinal Loss for recursive generation depth estimation.

Predicts recursion depth (d0-d3) from raw text using DeBERTa-v3-large backbone
with a contrastive ordinal loss that enforces learnable margins proportional to
ordinal distance between depth classes.

Loss = λ_ce * CrossEntropy + λ_con * ContrastiveOrdinal
ContrastiveOrdinal: all-pairs in batch, attractive (same label) pulls embeddings
together, repulsive (different label) pushes apart with margin m_|y_i - y_j|.
Margins m_1, m_2, m_3 are learnable parameters (m_k for ordinal distance k).

Input:  depth_*.jsonl files with {"text": ..., "depth": int, ...}
Output: best checkpoint + training logs
"""

import argparse
import glob
import json
import math
import os
import random
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.amp import autocast
from torch.cuda.amp import GradScaler
from torch.utils.data import DataLoader, Dataset, random_split
from transformers import AutoModel, AutoTokenizer


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


class DepthDataset(Dataset):
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
            "label": self.labels[idx],
        }


class DCOLModel(nn.Module):
    """DeBERTa backbone + linear classifier + learnable ordinal margins."""

    def __init__(self, model_name, num_depths=4, margin_init=1.0):
        super().__init__()
        self.encoder = AutoModel.from_pretrained(model_name)
        hidden_size = self.encoder.config.hidden_size
        self.classifier = nn.Linear(hidden_size, num_depths)
        # Learnable margins: m_1, m_2, m_3 for ordinal distances 1, 2, 3
        self.log_margins = nn.Parameter(
            torch.full((num_depths - 1,), math.log(margin_init))
        )

    @property
    def margins(self):
        # Exponentiate to keep margins positive; enforce monotonicity m_1 <= m_2 <= m_3
        raw = self.log_margins.exp()
        return torch.cumsum(raw, dim=0)

    def forward(self, input_ids, attention_mask):
        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
        # Mean pooling over non-padding tokens
        token_embs = outputs.last_hidden_state  # (B, L, H)
        mask = attention_mask.unsqueeze(-1).float()  # (B, L, 1)
        pooled = (token_embs * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1e-9)
        logits = self.classifier(pooled)  # (B, num_depths)
        return pooled, logits


def contrastive_ordinal_loss(embeddings, labels, margins):
    """
    All-pairs contrastive loss with ordinal margins.

    For each pair (i, j) in the batch:
      - Same class:    max(0, ||e_i - e_j||_2 - α)           (attractive)
      - Diff class:    max(0, m_{|y_i-y_j|} - ||e_i - e_j||_2 + α)  (repulsive)
    where α is a small slack (0.1) and m_k = margins[k-1].
    """
    alpha = 0.1
    B = embeddings.size(0)
    if B < 2:
        return embeddings.new_tensor(0.0)

    # Pairwise squared L2 distances -> sqrt with epsilon for numerical stability
    diff = embeddings.unsqueeze(0) - embeddings.unsqueeze(1)  # (B, B, H)
    dists = (diff.pow(2).sum(dim=-1) + 1e-8).sqrt()  # (B, B)

    # Label distance matrix: |y_i - y_j|
    label_dists = (labels.unsqueeze(0) - labels.unsqueeze(1)).abs()  # (B, B)

    # Same-class mask (exclude diagonal)
    same_mask = (label_dists == 0).float()
    same_mask.fill_diagonal_(0)

    # Different-class mask
    diff_mask = (label_dists > 0).float()

    # Attractive loss: pull same-class embeddings together
    attractive = F.relu(dists - alpha) * same_mask

    # Repulsive loss: push different-class embeddings apart by margin m_k
    # margins has shape (num_depths-1,), index by label_dist - 1
    margin_matrix = margins[(label_dists.clamp(min=1) - 1).long()]  # (B, B)
    repulsive = F.relu(margin_matrix - dists + alpha) * diff_mask

    # Average over valid pairs
    n_same = same_mask.sum().clamp(min=1)
    n_diff = diff_mask.sum().clamp(min=1)
    loss = attractive.sum() / n_same + repulsive.sum() / n_diff
    return loss


def load_data(data_dirs):
    """Load all depth_*.jsonl from multiple directories."""
    texts, labels = [], []
    import re
    depth_pattern = re.compile(r"^depth_(\d+)\.jsonl$")
    for d in data_dirs:
        pattern = os.path.join(d, "depth_*.jsonl")
        files = sorted(glob.glob(pattern))
        if not files:
            print(f"WARNING: no depth_*.jsonl found in {d}")
            continue
        for f in files:
            fname = os.path.basename(f)
            m = depth_pattern.match(fname)
            if not m:
                continue
            depth = int(m.group(1))
            with open(f) as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    item = json.loads(line)
                    texts.append(item["text"])
                    labels.append(depth)
        print(f"  Loaded from {d}: {len(files)} files")
    print(f"Total samples: {len(texts)}")
    return texts, labels


def evaluate(model, dataloader, device, use_amp):
    model.eval()
    correct, total = 0, 0
    total_loss_ce = 0.0
    mae_sum = 0.0
    num_classes = 4
    class_correct = [0] * num_classes
    class_total = [0] * num_classes
    amp_device = "cuda" if device.type == "cuda" else "cpu"

    with torch.no_grad():
        for batch in dataloader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["label"].to(device)

            with autocast(amp_device, enabled=use_amp):
                _, logits = model(input_ids, attention_mask)
                loss_ce = F.cross_entropy(logits, labels)

            total_loss_ce += loss_ce.item() * labels.size(0)
            preds = logits.argmax(dim=-1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)
            mae_sum += (preds - labels).abs().float().sum().item()

            for c in range(num_classes):
                mask = labels == c
                class_total[c] += mask.sum().item()
                class_correct[c] += ((preds == labels) & mask).sum().item()

    acc = correct / max(total, 1)
    avg_ce = total_loss_ce / max(total, 1)
    per_class_acc = [
        class_correct[c] / max(class_total[c], 1) for c in range(num_classes)
    ]
    mae = mae_sum / max(total, 1)

    return acc, avg_ce, per_class_acc, mae


def main():
    parser = argparse.ArgumentParser(description="DCOL: DeBERTa + Contrastive Ordinal Loss")
    parser.add_argument("--data_dirs", nargs="+", required=True)
    parser.add_argument("--model_name", type=str, default="microsoft/deberta-v3-large")
    parser.add_argument("--output_dir", type=str, default="checkpoints/dcol/")
    parser.add_argument("--max_seq_len", type=int, default=512)
    parser.add_argument("--batch_size", type=int, default=8)
    parser.add_argument("--gradient_accumulation", type=int, default=4)
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--lr", type=float, default=2e-5)
    parser.add_argument("--warmup_ratio", type=float, default=0.1)
    parser.add_argument("--lambda_contrastive", type=float, default=1.0)
    parser.add_argument("--lambda_ce", type=float, default=0.5)
    parser.add_argument("--margin_init", type=float, default=1.0)
    parser.add_argument("--num_depths", type=int, default=4)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--fp16", action="store_true")
    parser.add_argument("--bf16", action="store_true")
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--eval_split", type=float, default=0.1)
    parser.add_argument("--log_every", type=int, default=50)
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--use_wandb", action="store_true")
    args = parser.parse_args()

    set_seed(args.seed)

    # Device
    if torch.cuda.is_available() and os.environ.get("CUDA_VISIBLE_DEVICES", "") != "":
        device = torch.device(f"cuda:{args.gpu}")
        print(f"Using GPU: {torch.cuda.get_device_name(device)}")
    else:
        device = torch.device("cpu")
        print("Using CPU")

    use_amp = (args.fp16 or args.bf16) and device.type == "cuda"
    amp_dtype = torch.bfloat16 if args.bf16 else torch.float16
    amp_device = "cuda" if device.type == "cuda" else "cpu"

    # Load data
    print("Loading data...")
    texts, labels = load_data(args.data_dirs)
    assert len(texts) > 0, "No data loaded"

    # Tokenizer
    print(f"Loading tokenizer: {args.model_name}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)

    # Dataset + split
    dataset = DepthDataset(texts, labels, tokenizer, args.max_seq_len)
    val_size = int(len(dataset) * args.eval_split)
    train_size = len(dataset) - val_size
    train_dataset, val_dataset = random_split(
        dataset, [train_size, val_size],
        generator=torch.Generator().manual_seed(args.seed),
    )
    print(f"Train: {train_size}, Val: {val_size}")

    train_loader = DataLoader(
        train_dataset, batch_size=args.batch_size, shuffle=True,
        num_workers=2, pin_memory=(device.type == "cuda"),
    )
    val_loader = DataLoader(
        val_dataset, batch_size=args.batch_size * 2, shuffle=False,
        num_workers=2, pin_memory=(device.type == "cuda"),
    )

    # Model
    print(f"Loading model: {args.model_name}")
    model = DCOLModel(args.model_name, args.num_depths, args.margin_init).float().to(device)

    # Log learnable margins
    print(f"Initial margins (m_1, m_2, m_3): {model.margins.detach().cpu().tolist()}")
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Parameters: {total_params:,} total, {trainable_params:,} trainable")

    # Check margins are in parameters
    margin_in_params = any(p is model.log_margins for p in model.parameters())
    print(f"Learnable margins in parameters: {margin_in_params}")

    # Optimizer + scheduler
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=0.01)
    total_steps = (len(train_loader) // args.gradient_accumulation) * args.epochs
    warmup_steps = int(total_steps * args.warmup_ratio)

    def lr_lambda(step):
        if step < warmup_steps:
            return step / max(warmup_steps, 1)
        progress = (step - warmup_steps) / max(total_steps - warmup_steps, 1)
        return max(0.0, 0.5 * (1.0 + math.cos(math.pi * progress)))

    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)
    scaler = GradScaler(enabled=use_amp)

    # W&B
    if args.use_wandb:
        import wandb
        wandb.init(project="recursive_gen_depth_est", name="dcol_train", config=vars(args))

    # Output dir
    os.makedirs(args.output_dir, exist_ok=True)

    # Training loop
    print(f"\n{'='*60}")
    print(f"Starting training: {args.epochs} epochs, {total_steps} steps")
    print(f"Effective batch size: {args.batch_size * args.gradient_accumulation}")
    print(f"{'='*60}\n")

    best_val_acc = 0.0
    global_step = 0

    for epoch in range(args.epochs):
        model.train()
        epoch_loss = 0.0
        epoch_correct = 0
        epoch_total = 0
        optimizer.zero_grad()
        t0 = time.time()

        for step, batch in enumerate(train_loader):
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            batch_labels = batch["label"].to(device)

            with autocast(amp_device, enabled=use_amp, dtype=amp_dtype if use_amp else torch.float32):
                embeddings, logits = model(input_ids, attention_mask)
                loss_ce = F.cross_entropy(logits, batch_labels)
                loss_con = contrastive_ordinal_loss(
                    embeddings, batch_labels, model.margins
                )
                loss = args.lambda_ce * loss_ce + args.lambda_contrastive * loss_con
                loss = loss / args.gradient_accumulation

            scaler.scale(loss).backward()

            if (step + 1) % args.gradient_accumulation == 0:
                scaler.unscale_(optimizer)
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                scaler.step(optimizer)
                scaler.update()
                scheduler.step()
                optimizer.zero_grad()
                global_step += 1

            epoch_loss += loss.item() * args.gradient_accumulation
            preds = logits.argmax(dim=-1)
            epoch_correct += (preds == batch_labels).sum().item()
            epoch_total += batch_labels.size(0)

            if (step + 1) % args.log_every == 0:
                avg_loss = epoch_loss / (step + 1)
                acc = epoch_correct / max(epoch_total, 1)
                margins = model.margins.detach().cpu().tolist()
                lr_now = scheduler.get_last_lr()[0]
                print(
                    f"  [Epoch {epoch+1} Step {step+1}/{len(train_loader)}] "
                    f"loss={avg_loss:.4f} acc={acc:.4f} "
                    f"margins={[f'{m:.3f}' for m in margins]} "
                    f"lr={lr_now:.2e}"
                )
                if args.use_wandb:
                    import wandb
                    wandb.log({
                        "train/loss": avg_loss,
                        "train/acc": acc,
                        "train/lr": lr_now,
                        "train/margin_1": margins[0],
                        "train/margin_2": margins[1],
                        "train/margin_3": margins[2],
                        "global_step": global_step,
                    })

            # Dry run: stop after 2 steps
            if args.dry_run and step >= 1:
                print(f"  [DRY RUN] Stopping after {step+1} steps")
                break

        elapsed = time.time() - t0
        train_acc = epoch_correct / max(epoch_total, 1)
        train_loss = epoch_loss / max(step + 1, 1)
        print(
            f"\nEpoch {epoch+1}/{args.epochs} — "
            f"train_loss={train_loss:.4f} train_acc={train_acc:.4f} "
            f"time={elapsed:.1f}s"
        )

        # Validation
        val_acc, val_ce, per_class_acc, val_mae = evaluate(
            model, val_loader, device, use_amp
        )
        margins = model.margins.detach().cpu().tolist()
        print(
            f"  val_acc={val_acc:.4f} val_ce={val_ce:.4f} val_mae={val_mae:.4f}"
        )
        print(
            f"  per_class_acc: "
            + " ".join(f"d{i}={a:.4f}" for i, a in enumerate(per_class_acc))
        )
        print(f"  margins: {[f'{m:.3f}' for m in margins]}")

        if args.use_wandb:
            import wandb
            log_dict = {
                "val/acc": val_acc,
                "val/ce": val_ce,
                "val/mae": val_mae,
                "epoch": epoch + 1,
            }
            for i, a in enumerate(per_class_acc):
                log_dict[f"val/acc_d{i}"] = a
            for i, m in enumerate(margins):
                log_dict[f"margin/{i+1}"] = m
            wandb.log(log_dict)

        # Save best
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            ckpt_path = os.path.join(args.output_dir, "best_model.pt")
            torch.save({
                "epoch": epoch + 1,
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "val_acc": val_acc,
                "val_mae": val_mae,
                "margins": margins,
                "args": vars(args),
            }, ckpt_path)
            print(f"  Saved best model: val_acc={val_acc:.4f} -> {ckpt_path}")

        if args.dry_run:
            print("[DRY RUN] Stopping after 1 epoch")
            break

    print(f"\nTraining complete. Best val_acc={best_val_acc:.4f}")
    if args.use_wandb:
        import wandb
        wandb.finish()


if __name__ == "__main__":
    main()

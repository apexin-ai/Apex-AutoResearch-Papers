"""DCOL training script: DeBERTa-v3-large + contrastive ordinal loss.

Usage:
    python train_dcol.py --data_dir /path/to/depth_jsonls \
        --output_dir /path/to/checkpoints \
        --epochs 10 --lr 2e-5 --batch_size 16

Dependencies: torch, transformers, wandb, sklearn
"""

import argparse
import os
import random

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
from transformers import AutoTokenizer, get_cosine_schedule_with_warmup

from dcol_dataset import DepthCollator, DepthDataset
from dcol_loss import DColLoss
from dcol_model import DColModel


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def knn_accuracy(embeddings: torch.Tensor, labels: torch.Tensor, k: int = 5) -> float:
    """Leave-one-out kNN accuracy on given embeddings."""
    dists = torch.cdist(embeddings, embeddings, p=2)
    dists.fill_diagonal_(float("inf"))
    _, topk_idx = dists.topk(k, largest=False)
    topk_labels = labels[topk_idx]
    preds = topk_labels.mode(dim=1).values
    return (preds == labels).float().mean().item()


@torch.no_grad()
def evaluate(model: nn.Module, loader: DataLoader, criterion: DColLoss, device: torch.device):
    model.eval()
    all_emb, all_labels = [], []
    total_loss = 0.0
    n = 0
    for batch in loader:
        ids = batch["input_ids"].to(device)
        mask = batch["attention_mask"].to(device)
        labels = batch["labels"].to(device)
        with torch.amp.autocast("cuda", enabled=device.type == "cuda"):
            emb = model(ids, mask)
            out = criterion(emb, labels)
        total_loss += out["loss"].item() * len(labels)
        n += len(labels)
        all_emb.append(emb.float().cpu())
        all_labels.append(labels.cpu())

    all_emb = torch.cat(all_emb)
    all_labels = torch.cat(all_labels)
    acc = knn_accuracy(all_emb, all_labels)
    return {"val_loss": total_loss / max(n, 1), "val_knn_acc": acc}


def main():
    parser = argparse.ArgumentParser(description="Train DCOL model")
    parser.add_argument("--data_dir", type=str, required=True)
    parser.add_argument("--model_name", type=str, default="microsoft/deberta-v3-large")
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--lr", type=float, default=2e-5)
    parser.add_argument("--batch_size", type=int, default=16)
    parser.add_argument("--max_length", type=int, default=512)
    parser.add_argument("--embed_dim", type=int, default=128)
    parser.add_argument("--base_margin", type=float, default=0.3)
    parser.add_argument("--alpha", type=float, default=1.0)
    parser.add_argument("--beta", type=float, default=1.0)
    parser.add_argument("--warmup_ratio", type=float, default=0.1)
    parser.add_argument("--max_grad_norm", type=float, default=1.0)
    parser.add_argument("--val_ratio", type=float, default=0.15)
    parser.add_argument("--output_dir", type=str, default="./dcol_ckpts")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--wandb_project", type=str, default=None)
    parser.add_argument("--knn_k", type=int, default=5)
    args = parser.parse_args()

    set_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    os.makedirs(args.output_dir, exist_ok=True)

    # W&B
    if args.wandb_project:
        import wandb
        wandb.init(project=args.wandb_project, config=vars(args))

    # Data
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    dataset = DepthDataset(args.data_dir)
    val_size = int(len(dataset) * args.val_ratio)
    train_size = len(dataset) - val_size
    train_ds, val_ds = random_split(
        dataset, [train_size, val_size],
        generator=torch.Generator().manual_seed(args.seed),
    )
    collator = DepthCollator(tokenizer, max_length=args.max_length)
    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True,
                              collate_fn=collator, num_workers=2, pin_memory=True)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size * 2, shuffle=False,
                            collate_fn=collator, num_workers=2, pin_memory=True)

    # Model + loss
    model = DColModel(args.model_name, args.embed_dim).to(device)
    criterion = DColLoss(num_classes=4, base_margin=args.base_margin,
                         alpha=args.alpha, beta=args.beta).to(device)

    # Optimizer: different LR for encoder vs projection head + margins
    encoder_params = list(model.encoder.parameters())
    head_params = list(model.proj.parameters()) + list(criterion.parameters())
    optimizer = torch.optim.AdamW([
        {"params": encoder_params, "lr": args.lr},
        {"params": head_params, "lr": args.lr * 10},
    ], weight_decay=0.01)

    total_steps = len(train_loader) * args.epochs
    warmup_steps = int(total_steps * args.warmup_ratio)
    scheduler = get_cosine_schedule_with_warmup(optimizer, warmup_steps, total_steps)
    scaler = torch.amp.GradScaler("cuda", enabled=device.type == "cuda")

    best_acc = 0.0
    print(f"Train: {train_size}, Val: {val_size}, Device: {device}")

    for epoch in range(args.epochs):
        model.train()
        epoch_loss = 0.0
        for step, batch in enumerate(train_loader):
            ids = batch["input_ids"].to(device)
            mask = batch["attention_mask"].to(device)
            labels = batch["labels"].to(device)

            optimizer.zero_grad()
            with torch.amp.autocast("cuda", enabled=device.type == "cuda"):
                emb = model(ids, mask)
                out = criterion(emb, labels)
                loss = out["loss"]

            scaler.scale(loss).backward()
            scaler.unscale_(optimizer)
            nn.utils.clip_grad_norm_(model.parameters(), args.max_grad_norm)
            nn.utils.clip_grad_norm_(criterion.parameters(), args.max_grad_norm)
            scaler.step(optimizer)
            scaler.update()
            scheduler.step()

            epoch_loss += loss.item()
            if (step + 1) % 50 == 0:
                print(f"  Epoch {epoch+1} step {step+1}/{len(train_loader)} "
                      f"loss={loss.item():.4f} attr={out['attractive'].item():.4f} "
                      f"repul={out['repulsive'].item():.4f}")

            if args.wandb_project:
                wandb.log({
                    "train/loss": loss.item(),
                    "train/attractive": out["attractive"].item(),
                    "train/repulsive": out["repulsive"].item(),
                    "train/lr": scheduler.get_last_lr()[0],
                })

        # Validate
        metrics = evaluate(model, val_loader, criterion, device)
        avg_train_loss = epoch_loss / len(train_loader)
        print(f"Epoch {epoch+1}/{args.epochs}  train_loss={avg_train_loss:.4f}  "
              f"val_loss={metrics['val_loss']:.4f}  val_knn_acc={metrics['val_knn_acc']:.4f}")

        if args.wandb_project:
            wandb.log({"epoch": epoch + 1, **metrics})

        # Save best
        if metrics["val_knn_acc"] > best_acc:
            best_acc = metrics["val_knn_acc"]
            ckpt = {
                "epoch": epoch + 1,
                "model": model.state_dict(),
                "criterion": criterion.state_dict(),
                "optimizer": optimizer.state_dict(),
                "val_knn_acc": best_acc,
                "args": vars(args),
            }
            torch.save(ckpt, os.path.join(args.output_dir, "best.pt"))
            print(f"  -> Saved best checkpoint (acc={best_acc:.4f})")

    # Save final
    torch.save({
        "epoch": args.epochs,
        "model": model.state_dict(),
        "criterion": criterion.state_dict(),
        "args": vars(args),
    }, os.path.join(args.output_dir, "last.pt"))
    print(f"Done. Best val kNN acc: {best_acc:.4f}")

    if args.wandb_project:
        wandb.finish()


if __name__ == "__main__":
    main()

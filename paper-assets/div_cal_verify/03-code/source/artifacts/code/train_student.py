# Student model (Qwen3-1.7B) fine-tuning on selected synthetic data.
# Usage: python train_student.py --model Qwen/Qwen3-1.7B --train_data ./data/gen_0/selected.pt --output_dir ./checkpoints/gen_0

import argparse
import os
import json
import math
from pathlib import Path

import torch
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModelForCausalLM, get_cosine_schedule_with_warmup


class TokenDataset(Dataset):
    def __init__(self, token_id_lists, seq_len):
        self.data = []
        for ids in token_id_lists:
            if len(ids) >= seq_len:
                self.data.append(ids[:seq_len])
            else:
                self.data.append(ids + [0] * (seq_len - len(ids)))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return torch.tensor(self.data[idx], dtype=torch.long)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model", type=str, default="Qwen/Qwen3-1.7B")
    p.add_argument("--checkpoint", type=str, default=None,
                   help="Resume from a previous checkpoint instead of base model")
    p.add_argument("--train_data", type=str, required=True,
                   help="Path to .pt file containing list of token id lists")
    p.add_argument("--output_dir", type=str, required=True)
    p.add_argument("--seq_len", type=int, default=512)
    p.add_argument("--batch_size", type=int, default=4)
    p.add_argument("--gradient_accumulation_steps", type=int, default=8)
    p.add_argument("--lr", type=float, default=2e-5)
    p.add_argument("--weight_decay", type=float, default=0.01)
    p.add_argument("--warmup_ratio", type=float, default=0.05)
    p.add_argument("--num_epochs", type=int, default=1)
    p.add_argument("--max_grad_norm", type=float, default=1.0)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--device", type=str, default="cuda:0")
    p.add_argument("--bf16", action="store_true", default=True)
    return p.parse_args()


def train_one_epoch(model, dataloader, optimizer, scheduler, device, args):
    model.train()
    total_loss = 0.0
    num_steps = 0
    optimizer.zero_grad()

    for step, batch in enumerate(dataloader):
        input_ids = batch.to(device)
        outputs = model(input_ids=input_ids, labels=input_ids)
        loss = outputs.loss / args.gradient_accumulation_steps
        loss.backward()
        total_loss += outputs.loss.item()

        if (step + 1) % args.gradient_accumulation_steps == 0:
            torch.nn.utils.clip_grad_norm_(model.parameters(), args.max_grad_norm)
            optimizer.step()
            scheduler.step()
            optimizer.zero_grad()
            num_steps += 1

            if num_steps % 50 == 0:
                avg = total_loss / (step + 1)
                print(f"  Step {num_steps}, avg loss: {avg:.4f}, lr: {scheduler.get_last_lr()[0]:.2e}")

    return total_loss / max(len(dataloader), 1)


def main():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    torch.manual_seed(args.seed)

    print(f"Loading model: {args.checkpoint or args.model}")
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    model_path = args.checkpoint if args.checkpoint else args.model
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16 if args.bf16 else torch.float32,
        trust_remote_code=True,
    ).to(args.device)

    # Load training data
    train_ids = torch.load(args.train_data, weights_only=True)
    print(f"Training sequences: {len(train_ids)}")

    dataset = TokenDataset(train_ids, args.seq_len)
    dataloader = DataLoader(dataset, batch_size=args.batch_size, shuffle=True,
                            num_workers=2, pin_memory=True)

    # Optimizer
    optimizer = torch.optim.AdamW(
        model.parameters(), lr=args.lr, weight_decay=args.weight_decay
    )
    total_steps = math.ceil(len(dataloader) / args.gradient_accumulation_steps) * args.num_epochs
    warmup_steps = int(total_steps * args.warmup_ratio)
    scheduler = get_cosine_schedule_with_warmup(optimizer, warmup_steps, total_steps)

    print(f"Training for {args.num_epochs} epoch(s), {total_steps} optimizer steps, "
          f"{warmup_steps} warmup steps")

    for epoch in range(args.num_epochs):
        print(f"\nEpoch {epoch + 1}/{args.num_epochs}")
        avg_loss = train_one_epoch(model, dataloader, optimizer, scheduler, args.device, args)
        print(f"  Epoch avg loss: {avg_loss:.4f}")

    # Save
    model.save_pretrained(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)

    meta = {
        "base_model": args.model,
        "checkpoint_from": args.checkpoint,
        "train_data": args.train_data,
        "num_train_samples": len(train_ids),
        "num_epochs": args.num_epochs,
        "lr": args.lr,
        "batch_size": args.batch_size,
        "gradient_accumulation_steps": args.gradient_accumulation_steps,
        "effective_batch_size": args.batch_size * args.gradient_accumulation_steps,
        "seed": args.seed,
        "final_avg_loss": avg_loss,
    }
    with open(Path(args.output_dir) / "train_meta.json", "w") as f:
        json.dump(meta, f, indent=2)
    print(f"\nCheckpoint saved to {args.output_dir}")


if __name__ == "__main__":
    main()

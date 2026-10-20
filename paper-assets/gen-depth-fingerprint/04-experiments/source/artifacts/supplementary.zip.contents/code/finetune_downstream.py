#!/usr/bin/env python3
"""Fine-tune a causal LM on depth-stratified data and measure held-out perplexity.

Usage:
    python finetune_downstream.py \
        --model-path /path/to/OLMo-2-0425-1B \
        --train-data ../data/downstream/train_depth01.jsonl \
        --eval-data ../data/downstream/test.jsonl \
        --output-dir experiments/downstream/depth01_seed42 \
        --seed 42 --bf16
"""

import argparse
import json
import math
import os

import torch
from torch.utils.data import Dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
    set_seed,
)


class TextDataset(Dataset):
    def __init__(self, path, tokenizer, max_length=512):
        self.encodings = []
        with open(path) as f:
            for line in f:
                text = json.loads(line)["text"]
                enc = tokenizer(
                    text, truncation=True, max_length=max_length,
                    padding="max_length", return_tensors="pt",
                )
                input_ids = enc["input_ids"].squeeze(0)
                attn_mask = enc["attention_mask"].squeeze(0)
                labels = input_ids.clone()
                labels[attn_mask == 0] = -100
                self.encodings.append((input_ids, attn_mask, labels))

    def __len__(self):
        return len(self.encodings)

    def __getitem__(self, idx):
        input_ids, attn_mask, labels = self.encodings[idx]
        return {
            "input_ids": input_ids,
            "attention_mask": attn_mask,
            "labels": labels,
        }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", required=True)
    parser.add_argument("--train-data", required=True)
    parser.add_argument("--eval-data", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max-length", type=int, default=512)
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--grad-accum", type=int, default=4)
    parser.add_argument("--lr", type=float, default=2e-5)
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--warmup-ratio", type=float, default=0.1)
    parser.add_argument("--eval-steps", type=int, default=100)
    parser.add_argument("--save-steps", type=int, default=500)
    parser.add_argument("--logging-steps", type=int, default=20)
    parser.add_argument("--fp16", action="store_true")
    parser.add_argument("--bf16", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Run 1 step and exit")
    args = parser.parse_args()

    set_seed(args.seed)

    print(f"=== Config ===")
    print(f"Model: {args.model_path}")
    print(f"Train: {args.train_data}")
    print(f"Eval:  {args.eval_data}")
    print(f"Seed:  {args.seed}")
    print(f"Batch: {args.batch_size} x {args.grad_accum} accum")
    print(f"LR: {args.lr}, Epochs: {args.epochs}")

    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        args.model_path, trust_remote_code=True,
        dtype=torch.bfloat16 if args.bf16 else (torch.float16 if args.fp16 else torch.float32),
    )

    print("Loading datasets...")
    train_dataset = TextDataset(args.train_data, tokenizer, args.max_length)
    eval_dataset = TextDataset(args.eval_data, tokenizer, args.max_length)
    print(f"Train: {len(train_dataset)}, Eval: {len(eval_dataset)}")

    max_steps = 1 if args.dry_run else -1
    num_epochs = 1 if args.dry_run else args.epochs

    training_args = TrainingArguments(
        output_dir=args.output_dir,
        num_train_epochs=num_epochs,
        max_steps=max_steps,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size,
        gradient_accumulation_steps=args.grad_accum,
        learning_rate=args.lr,
        warmup_ratio=args.warmup_ratio,
        weight_decay=0.01,
        eval_strategy="steps" if not args.dry_run else "no",
        eval_steps=args.eval_steps,
        save_strategy="no",
        logging_steps=args.logging_steps if not args.dry_run else 1,
        load_best_model_at_end=False,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        fp16=args.fp16,
        bf16=args.bf16,
        report_to="none",
        seed=args.seed,
        dataloader_pin_memory=True,
        remove_unused_columns=False,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
    )

    if args.dry_run:
        print("\n=== DRY RUN (1 step) ===")
        trainer.train()
        print("Dry run OK")
        return

    print("\n=== Training ===")
    trainer.train()

    print("\n=== Final Eval ===")
    metrics = trainer.evaluate()
    ppl = math.exp(metrics["eval_loss"])
    print(f"Eval loss: {metrics['eval_loss']:.4f}")
    print(f"Eval perplexity: {ppl:.2f}")

    results = {
        "model_path": args.model_path,
        "train_data": args.train_data,
        "eval_data": args.eval_data,
        "seed": args.seed,
        "eval_loss": metrics["eval_loss"],
        "eval_perplexity": ppl,
        "train_samples": len(train_dataset),
        "eval_samples": len(eval_dataset),
        "epochs": args.epochs,
        "lr": args.lr,
        "batch_size": args.batch_size,
        "grad_accum": args.grad_accum,
    }
    results_path = os.path.join(args.output_dir, "results.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results -> {results_path}")


if __name__ == "__main__":
    main()

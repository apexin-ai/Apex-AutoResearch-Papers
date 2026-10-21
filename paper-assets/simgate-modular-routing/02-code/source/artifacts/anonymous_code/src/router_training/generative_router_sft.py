"""Generative Router SFT: Finetune LLM as implicit generative router.

Routing signal is embedded in generated text ([SIMULATE]/raw action), not a
separate classification output. Classification head collapsed to all-deterministic
on 90:10 imbalanced data; generative approach avoids this via upsample + causal LM.

Input:  implicit_sft.jsonl (chat-format, from format_implicit_data.py)
        Fields: messages=[system,user,assistant], route_label, task_type, variation, step_idx
Output: LoRA adapter in --output_dir/final_adapter/
"""

import argparse
import json
import os
import random
import sys
from collections import Counter
from datetime import datetime
from typing import List, Tuple, Dict, Any

import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
)
from peft import LoraConfig, get_peft_model, TaskType

SIMULATE_PREFIX = "[SIMULATE]"


class ImplicitSFTDataset(Dataset):
    def __init__(self, records: List[Dict], tokenizer, max_seq_len: int = 2048):
        self.records = records
        self.tokenizer = tokenizer
        self.max_seq_len = max_seq_len

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        rec = self.records[idx]
        messages = rec["messages"]

        text = self.tokenizer.apply_chat_template(messages, tokenize=False)
        encoding = self.tokenizer(
            text,
            max_length=self.max_seq_len,
            truncation=True,
            padding="max_length",
            return_tensors="pt",
        )
        input_ids = encoding["input_ids"].squeeze()
        attention_mask = encoding["attention_mask"].squeeze()
        labels = input_ids.clone()
        labels[attention_mask == 0] = -100
        return {"input_ids": input_ids, "attention_mask": attention_mask, "labels": labels}


def upsample_minority(records: List[Dict], target_ratio: float = 0.5,
                      seed: int = 42) -> List[Dict]:
    """Upsample minority class to target ratio."""
    rng = random.Random(seed)
    by_label = {}
    for r in records:
        label = r.get("route_label", "unknown")
        by_label.setdefault(label, []).append(r)

    if len(by_label) < 2:
        return records

    counts = {k: len(v) for k, v in by_label.items()}
    majority_label = max(counts, key=counts.get)
    minority_label = min(counts, key=counts.get)

    n_majority = counts[majority_label]
    n_target = int(n_majority * target_ratio / (1 - target_ratio))
    n_upsample = n_target - counts[minority_label]

    if n_upsample <= 0:
        return records

    upsampled = list(records)
    minority_pool = by_label[minority_label]
    for _ in range(n_upsample):
        upsampled.append(rng.choice(minority_pool))

    rng.shuffle(upsampled)
    return upsampled


def parse_args():
    p = argparse.ArgumentParser(description="Generative router SFT training")
    p.add_argument("--data_path", type=str, required=True)
    p.add_argument("--model_name", type=str, default="Qwen/Qwen3-1.7B")
    p.add_argument("--output_dir", type=str, default="checkpoints/generative_router")
    p.add_argument("--epochs", type=int, default=3)
    p.add_argument("--batch_size", type=int, default=4)
    p.add_argument("--grad_accum", type=int, default=8)
    p.add_argument("--lr", type=float, default=2e-5)
    p.add_argument("--lora_r", type=int, default=16)
    p.add_argument("--lora_alpha", type=int, default=32)
    p.add_argument("--max_seq_len", type=int, default=2048)
    p.add_argument("--gpu_id", type=int, default=0)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--upsample_ratio", type=float, default=0.3)
    p.add_argument("--max_steps", type=int, default=None)
    return p.parse_args()


def main():
    args = parse_args()
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    with open(args.data_path) as f:
        records = [json.loads(line) for line in f if line.strip()]
    print(f"Loaded {len(records)} records")
    print(f"Label distribution: {Counter(r.get('route_label', 'unk') for r in records)}")

    records = upsample_minority(records, target_ratio=args.upsample_ratio, seed=args.seed)
    print(f"After upsampling: {len(records)} records")

    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        torch_dtype=torch.float16,
        trust_remote_code=True,
    )
    model.config.pad_token_id = tokenizer.pad_token_id

    lora_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=0.05,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
        task_type=TaskType.CAUSAL_LM,
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    dataset = ImplicitSFTDataset(records, tokenizer, args.max_seq_len)

    training_args = TrainingArguments(
        output_dir=args.output_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=args.grad_accum,
        learning_rate=args.lr,
        warmup_ratio=0.1,
        weight_decay=0.01,
        fp16=True,
        logging_steps=20,
        save_strategy="epoch",
        seed=args.seed,
        max_steps=args.max_steps if args.max_steps else -1,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
    )

    trainer.train()

    final_dir = os.path.join(args.output_dir, "final_adapter")
    model.save_pretrained(final_dir)
    tokenizer.save_pretrained(final_dir)
    print(f"Saved final adapter to {final_dir}")


if __name__ == "__main__":
    main()

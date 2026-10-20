"""Router SFT training: finetune LLM for 2-way routing classification.

Input: counterfactual labels from results/{task}/labeled_steps.jsonl
Output: LoRA adapter checkpoint in --output_dir
Supports two split strategies: stratified 80/20 and leave-one-task-out CV.
"""

import argparse
import json
import os
import random
import warnings
from collections import Counter
from typing import Any, Dict, List, Optional

import numpy as np
import torch
from torch.utils.data import DataLoader, WeightedRandomSampler
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    EarlyStoppingCallback,
)
from peft import LoraConfig, get_peft_model, TaskType

from data_loader import (
    LABEL2ID, ID2LABEL,
    load_labeled_data, stratified_split, leave_one_out_splits,
    RouterDataset,
)


def parse_args():
    p = argparse.ArgumentParser(description="Router SFT: finetune LLM for 2-way routing")
    p.add_argument("--data_path", type=str, default=None,
                   help="Single JSONL file (e.g. sft_triples.jsonl)")
    p.add_argument("--data_dir", type=str, default=None,
                   help="Directory with {task_type}/labeled_steps.jsonl")
    p.add_argument("--model_name", type=str, default="Qwen/Qwen3-1.7B")
    p.add_argument("--output_dir", type=str, default="checkpoints/router")
    p.add_argument("--epochs", type=int, default=3)
    p.add_argument("--batch_size", type=int, default=32)
    p.add_argument("--eval_batch_size", type=int, default=32)
    p.add_argument("--lr", type=float, default=2e-5)
    p.add_argument("--lora_r", type=int, default=16)
    p.add_argument("--lora_alpha", type=int, default=32)
    p.add_argument("--lora_dropout", type=float, default=0.05)
    p.add_argument("--max_seq_len", type=int, default=2048)
    p.add_argument("--gpu_id", type=int, default=0)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--eval_split", type=float, default=0.2)
    p.add_argument("--warmup_ratio", type=float, default=0.1)
    p.add_argument("--weight_decay", type=float, default=0.01)
    p.add_argument("--early_stopping_patience", type=int, default=2)
    p.add_argument("--split_strategy", type=str, default="stratified",
                   choices=["stratified", "leave_one_out"])
    p.add_argument("--class_weights", type=str, default=None)
    p.add_argument("--upsample_minority", action="store_true")
    p.add_argument("--max_samples", type=int, default=None)
    return p.parse_args()


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    acc = accuracy_score(labels, preds)
    prec, rec, f1, _ = precision_recall_fscore_support(labels, preds, average="binary", pos_label=0)
    return {
        "accuracy": acc,
        "internal_precision": prec,
        "internal_recall": rec,
        "internal_f1": f1,
    }


def main():
    args = parse_args()
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    data = load_labeled_data(data_path=args.data_path, data_dir=args.data_dir,
                             max_samples=args.max_samples)
    print(f"Loaded {len(data)} samples")
    print(f"Label distribution: {Counter(d['label'] for d in data)}")

    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForSequenceClassification.from_pretrained(
        args.model_name,
        num_labels=2,
        id2label=ID2LABEL,
        label2id=LABEL2ID,
        torch_dtype=torch.float16,
        trust_remote_code=True,
    )
    model.config.pad_token_id = tokenizer.pad_token_id

    lora_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        target_modules=["q_proj", "v_proj"],
        task_type=TaskType.SEQ_CLS,
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    train_data, eval_data = stratified_split(data, args.eval_split, args.seed)
    train_ds = RouterDataset(train_data, tokenizer, args.max_seq_len)
    eval_ds = RouterDataset(eval_data, tokenizer, args.max_seq_len)

    training_args = TrainingArguments(
        output_dir=args.output_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.eval_batch_size,
        learning_rate=args.lr,
        warmup_ratio=args.warmup_ratio,
        weight_decay=args.weight_decay,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="internal_recall",
        fp16=True,
        logging_steps=50,
        seed=args.seed,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=eval_ds,
        compute_metrics=compute_metrics,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=args.early_stopping_patience)],
    )

    trainer.train()

    final_dir = os.path.join(args.output_dir, "final_adapter")
    model.save_pretrained(final_dir)
    tokenizer.save_pretrained(final_dir)
    print(f"Saved final adapter to {final_dir}")


if __name__ == "__main__":
    main()

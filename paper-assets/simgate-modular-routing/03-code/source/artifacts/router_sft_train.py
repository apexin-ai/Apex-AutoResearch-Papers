# Router SFT training script for SimGate modular routing.
# Finetunes Qwen3-1.7B (or fallback) on episode-level labeled data
# from Plan C (labeled_steps.jsonl) for 2-way classification: internal vs deterministic.
#
# Data dependency: results/plan_c/{task_type}/labeled_steps.jsonl
# Usage: python src/router_sft_train.py --help

import argparse
import json
import os
import glob
import random
from collections import Counter
from typing import List, Dict, Any, Optional, Tuple

import numpy as np
import torch
from torch.utils.data import Dataset
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    EarlyStoppingCallback,
)
from peft import LoraConfig, get_peft_model, TaskType

LABEL2ID = {"internal": 0, "deterministic": 1}
ID2LABEL = {0: "internal", 1: "deterministic"}

SYSTEM_PROMPT = (
    "You are a routing classifier. Given the current observation and action history, "
    "predict which reasoning modality will lead to a better outcome."
)


def parse_args():
    p = argparse.ArgumentParser(description="Router SFT: finetune LLM for 2-way routing classification")
    p.add_argument("--data_dir", type=str, default="results/plan_c/",
                    help="Directory containing {task_type}/labeled_steps.jsonl")
    p.add_argument("--model_name", type=str, default="Qwen/Qwen3-1.7B",
                    help="HuggingFace model name or local path")
    p.add_argument("--output_dir", type=str, default="results/router_sft/",
                    help="Output directory for checkpoints and reports")
    p.add_argument("--epochs", type=int, default=3)
    p.add_argument("--batch_size", type=int, default=16)
    p.add_argument("--eval_batch_size", type=int, default=32)
    p.add_argument("--lr", type=float, default=2e-4)
    p.add_argument("--lora_r", type=int, default=16)
    p.add_argument("--lora_alpha", type=int, default=32)
    p.add_argument("--lora_dropout", type=float, default=0.05)
    p.add_argument("--max_seq_len", type=int, default=512)
    p.add_argument("--gpu_id", type=int, default=0)
    p.add_argument("--wandb_project", type=str, default="simgate-router-sft")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--eval_split", type=float, default=0.2)
    p.add_argument("--warmup_ratio", type=float, default=0.1)
    p.add_argument("--weight_decay", type=float, default=0.01)
    p.add_argument("--early_stopping_patience", type=int, default=2)
    p.add_argument("--dry_run", action="store_true", help="Only validate imports and args, skip training")
    return p.parse_args()


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def summarize_action_history(action_history: List[str], max_actions: int = 5) -> str:
    """Keep the most recent N actions as a summary."""
    recent = action_history[-max_actions:] if action_history else []
    if not recent:
        return "(none)"
    return " → ".join(recent)


def build_prompt(observation: str, action_history: List[str]) -> str:
    history_summary = summarize_action_history(action_history)
    return (
        f"<|system|>{SYSTEM_PROMPT}<|end|>\n"
        f"<|user|>\n"
        f"Observation: {observation}\n"
        f"Action history: {history_summary}\n"
        f"<|end|>"
    )


def load_labeled_data(data_dir: str) -> List[Dict[str, Any]]:
    """Load all labeled_steps.jsonl files, filtering out ties."""
    pattern = os.path.join(data_dir, "*", "labeled_steps.jsonl")
    files = sorted(glob.glob(pattern))
    if not files:
        pattern_flat = os.path.join(data_dir, "labeled_steps.jsonl")
        if os.path.exists(pattern_flat):
            files = [pattern_flat]
    if not files:
        raise FileNotFoundError(f"No labeled_steps.jsonl found in {data_dir}")

    samples = []
    for fpath in files:
        task_type = os.path.basename(os.path.dirname(fpath))
        with open(fpath) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                record = json.loads(line)
                label = record.get("label", "")
                if label not in LABEL2ID:
                    continue
                samples.append({
                    "observation": record.get("observation", ""),
                    "action_history": record.get("action_history", []),
                    "label": label,
                    "label_id": LABEL2ID[label],
                    "task_type": record.get("task_name", task_type),
                })

    print(f"Loaded {len(samples)} samples from {len(files)} files (ties excluded)")
    label_dist = Counter(s["label"] for s in samples)
    for k, v in sorted(label_dist.items()):
        print(f"  {k}: {v} ({v/len(samples)*100:.1f}%)")
    return samples


def stratified_split(
    samples: List[Dict], eval_ratio: float, seed: int
) -> Tuple[List[Dict], List[Dict]]:
    """Stratified train/val split by task_type."""
    rng = random.Random(seed)
    by_task: Dict[str, List[Dict]] = {}
    for s in samples:
        by_task.setdefault(s["task_type"], []).append(s)

    train_set, val_set = [], []
    for task, items in by_task.items():
        rng.shuffle(items)
        n_val = max(1, int(len(items) * eval_ratio))
        val_set.extend(items[:n_val])
        train_set.extend(items[n_val:])

    rng.shuffle(train_set)
    rng.shuffle(val_set)
    print(f"Split: train={len(train_set)}, val={len(val_set)}")
    return train_set, val_set


class RouterDataset(Dataset):
    def __init__(self, samples: List[Dict], tokenizer, max_length: int):
        self.samples = samples
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        s = self.samples[idx]
        prompt = build_prompt(s["observation"], s["action_history"])
        encoding = self.tokenizer(
            prompt,
            truncation=True,
            max_length=self.max_length,
            padding="max_length",
            return_tensors="pt",
        )
        return {
            "input_ids": encoding["input_ids"].squeeze(0),
            "attention_mask": encoding["attention_mask"].squeeze(0),
            "labels": torch.tensor(s["label_id"], dtype=torch.long),
        }


# ---------------------------------------------------------------------------
# Model setup
# ---------------------------------------------------------------------------

def setup_model(model_name: str, args):
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForSequenceClassification.from_pretrained(
        model_name,
        num_labels=2,
        id2label=ID2LABEL,
        label2id=LABEL2ID,
        trust_remote_code=True,
        torch_dtype=torch.bfloat16,
    )
    model.config.pad_token_id = tokenizer.pad_token_id

    lora_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
        lora_dropout=args.lora_dropout,
        task_type=TaskType.SEQ_CLS,
        modules_to_save=["score"],
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    return model, tokenizer


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    acc = accuracy_score(labels, preds)
    prec, rec, f1, _ = precision_recall_fscore_support(labels, preds, average=None, labels=[0, 1])
    return {
        "accuracy": acc,
        "precision_internal": prec[0],
        "recall_internal": rec[0],
        "f1_internal": f1[0],
        "precision_deterministic": prec[1],
        "recall_deterministic": rec[1],
        "f1_deterministic": f1[1],
    }


def per_task_evaluation(trainer, val_dataset, val_samples) -> Dict[str, Any]:
    """Compute per-task accuracy and confusion matrix."""
    predictions = trainer.predict(val_dataset)
    preds = np.argmax(predictions.predictions, axis=-1)
    labels = predictions.label_ids

    cm = confusion_matrix(labels, preds, labels=[0, 1]).tolist()

    task_metrics = {}
    by_task: Dict[str, Dict[str, list]] = {}
    for i, s in enumerate(val_samples):
        t = s["task_type"]
        if t not in by_task:
            by_task[t] = {"preds": [], "labels": []}
        by_task[t]["preds"].append(preds[i])
        by_task[t]["labels"].append(labels[i])

    for task, data in sorted(by_task.items()):
        acc = accuracy_score(data["labels"], data["preds"])
        n = len(data["labels"])
        task_metrics[task] = {"accuracy": acc, "n_samples": n}

    return {
        "overall_accuracy": accuracy_score(labels, preds),
        "confusion_matrix": cm,
        "confusion_labels": ["internal", "deterministic"],
        "per_task": task_metrics,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()

    if args.dry_run:
        print("Dry run: imports OK, args parsed successfully.")
        print(f"  model_name: {args.model_name}")
        print(f"  data_dir:   {args.data_dir}")
        print(f"  output_dir: {args.output_dir}")
        return

    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu_id)
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    os.makedirs(args.output_dir, exist_ok=True)

    samples = load_labeled_data(args.data_dir)
    train_samples, val_samples = stratified_split(samples, args.eval_split, args.seed)

    model, tokenizer = setup_model(args.model_name, args)

    train_dataset = RouterDataset(train_samples, tokenizer, args.max_seq_len)
    val_dataset = RouterDataset(val_samples, tokenizer, args.max_seq_len)

    use_bf16 = torch.cuda.is_available() and torch.cuda.get_device_capability()[0] >= 8
    training_args = TrainingArguments(
        output_dir=args.output_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.eval_batch_size,
        learning_rate=args.lr,
        weight_decay=args.weight_decay,
        warmup_ratio=args.warmup_ratio,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="accuracy",
        greater_is_better=True,
        bf16=use_bf16,
        fp16=(not use_bf16 and torch.cuda.is_available()),
        logging_steps=10,
        dataloader_num_workers=4,
        report_to="wandb",
        run_name=f"router-sft-{os.path.basename(args.model_name)}-r{args.lora_r}",
        seed=args.seed,
        save_total_limit=2,
    )

    os.environ["WANDB_PROJECT"] = args.wandb_project

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        compute_metrics=compute_metrics,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=args.early_stopping_patience)],
    )

    print(f"\n{'='*60}")
    print(f"Starting training: {len(train_dataset)} train / {len(val_dataset)} val samples")
    print(f"Model: {args.model_name}, LoRA r={args.lora_r}, lr={args.lr}")
    print(f"{'='*60}\n")

    trainer.train()

    adapter_dir = os.path.join(args.output_dir, "final_adapter")
    model.save_pretrained(adapter_dir)
    tokenizer.save_pretrained(adapter_dir)
    print(f"Adapter saved to {adapter_dir}")

    print("\n--- Evaluation ---")
    eval_report = per_task_evaluation(trainer, val_dataset, val_samples)

    report_path = os.path.join(args.output_dir, "eval_report.json")
    with open(report_path, "w") as f:
        json.dump(eval_report, f, indent=2)
    print(f"Eval report saved to {report_path}")

    print(f"\nOverall accuracy: {eval_report['overall_accuracy']:.4f}")
    print(f"Confusion matrix (rows=true, cols=pred):")
    print(f"  {eval_report['confusion_labels']}")
    for row in eval_report["confusion_matrix"]:
        print(f"  {row}")
    print("\nPer-task accuracy:")
    for task, m in sorted(eval_report["per_task"].items()):
        print(f"  {task}: {m['accuracy']:.3f} (n={m['n_samples']})")


if __name__ == "__main__":
    main()

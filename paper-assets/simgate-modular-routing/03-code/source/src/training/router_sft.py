# Router SFT training: finetune Qwen3-1.7B for 2-way routing classification.
# Input: plan-001b counterfactual labels from results/plan_c/{task}/labeled_steps.jsonl
# Output: LoRA adapter checkpoint in --output_dir
# Supports two split strategies: stratified 80/20 and leave-one-task-out CV.

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
    p.add_argument("--output_dir", type=str, default="checkpoints/plan-002")
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
                   choices=["stratified", "leave_one_out"],
                   help="stratified: 80/20 by task. leave_one_out: hold out one task at a time.")
    p.add_argument("--class_weights", type=str, default=None,
                   help='"auto" for inverse-frequency, or "w0,w1"')
    p.add_argument("--upsample_minority", action="store_true",
                   help="WeightedRandomSampler for minority oversampling")
    p.add_argument("--wandb_project", type=str, default=None,
                   help="W&B project name (omit to disable)")
    p.add_argument("--max_samples", type=int, default=None,
                   help="Subsample data for debugging")
    p.add_argument("--dry_run", action="store_true",
                   help="Validate imports and data loading, skip training")
    return p.parse_args()


def resolve_model_path(model_name: str) -> str:
    """Try local paths with common naming variants before falling back to HF hub."""
    if os.path.isdir(model_name):
        return model_name

    hf_cache_dirs = [
        "/root/autodl-tmp/models",
        os.path.expanduser("~/.cache/huggingface/hub"),
    ]
    parts = model_name.split("/")
    if len(parts) == 2:
        org, name = parts
        variants = [
            name,
            name.replace("-", "___"),
            name.replace("-", "_"),
        ]
        for cache_dir in hf_cache_dirs:
            for v in variants:
                candidate = os.path.join(cache_dir, org, v)
                if os.path.isdir(candidate):
                    print(f"Resolved model: {model_name} → {candidate}")
                    return candidate

    return model_name


def compute_class_weights(train_samples: List[Dict], mode: str) -> torch.Tensor:
    num_classes = len(LABEL2ID)
    if mode == "auto":
        counts = Counter(s["label_id"] for s in train_samples)
        total = len(train_samples)
        weights = torch.tensor(
            [total / (num_classes * max(counts.get(i, 1), 1)) for i in range(num_classes)],
            dtype=torch.float32,
        )
    else:
        parts = [float(x.strip()) for x in mode.split(",")]
        if len(parts) != num_classes:
            raise ValueError(f"Expected {num_classes} weights, got {len(parts)}")
        weights = torch.tensor(parts, dtype=torch.float32)
    return weights


class WeightedCETrainer(Trainer):
    def __init__(self, class_weights: Optional[torch.Tensor] = None,
                 weighted_sampler: Optional[WeightedRandomSampler] = None, **kwargs):
        super().__init__(**kwargs)
        self._class_weights = class_weights
        self._weighted_sampler = weighted_sampler

    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
        labels = inputs.pop("labels")
        outputs = model(**inputs)
        logits = outputs.logits
        if self._class_weights is not None:
            loss_fn = torch.nn.CrossEntropyLoss(weight=self._class_weights.to(logits.device))
        else:
            loss_fn = torch.nn.CrossEntropyLoss()
        loss = loss_fn(logits, labels)
        return (loss, outputs) if return_outputs else loss

    def get_train_dataloader(self) -> DataLoader:
        if self._weighted_sampler is None:
            return super().get_train_dataloader()
        return DataLoader(
            self.train_dataset,
            batch_size=self.args.per_device_train_batch_size,
            sampler=self._weighted_sampler,
            num_workers=self.args.dataloader_num_workers,
            pin_memory=self.args.dataloader_pin_memory,
        )


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
        "f1_macro": float(np.mean(f1)),
    }


def per_task_evaluation(trainer, val_dataset, val_samples) -> Dict[str, Any]:
    predictions = trainer.predict(val_dataset)
    preds = np.argmax(predictions.predictions, axis=-1)
    labels = predictions.label_ids

    cm = confusion_matrix(labels, preds, labels=[0, 1]).tolist()

    by_task: Dict[str, Dict[str, list]] = {}
    for i, s in enumerate(val_samples):
        t = s["task_type"]
        if t not in by_task:
            by_task[t] = {"preds": [], "labels": []}
        by_task[t]["preds"].append(preds[i])
        by_task[t]["labels"].append(labels[i])

    task_metrics = {}
    for task, data in sorted(by_task.items()):
        acc = accuracy_score(data["labels"], data["preds"])
        task_metrics[task] = {"accuracy": acc, "n_samples": len(data["labels"])}

    return {
        "overall_accuracy": accuracy_score(labels, preds),
        "confusion_matrix": cm,
        "confusion_labels": ["internal", "deterministic"],
        "per_task": task_metrics,
    }


def setup_model_and_tokenizer(model_path: str, args):
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForSequenceClassification.from_pretrained(
        model_path,
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


def build_sampler(train_samples: List[Dict]) -> WeightedRandomSampler:
    label_counts = Counter(s["label"] for s in train_samples)
    sample_weights = [1.0 / label_counts[s["label"]] for s in train_samples]
    return WeightedRandomSampler(
        weights=sample_weights,
        num_samples=len(train_samples),
        replacement=True,
    )


def train_single_fold(
    train_samples: List[Dict],
    val_samples: List[Dict],
    model_path: str,
    args,
    output_dir: str,
    fold_name: str = "main",
):
    """Run one training fold. Shared by stratified and LOO strategies."""
    train_label_counts = Counter(s["label"] for s in train_samples)
    n_internal = train_label_counts.get("internal", 0)
    if n_internal < 5:
        warnings.warn(
            f"[{fold_name}] Only {n_internal} internal samples in training set. "
            f"Model may not learn the minority class.",
            stacklevel=2,
        )

    class_weights = None
    if args.class_weights is not None:
        class_weights = compute_class_weights(train_samples, args.class_weights)
        print(f"[{fold_name}] Class weights: "
              f"{{internal: {class_weights[0]:.3f}, deterministic: {class_weights[1]:.3f}}}")

    model, tokenizer = setup_model_and_tokenizer(model_path, args)
    train_dataset = RouterDataset(train_samples, tokenizer, args.max_seq_len)
    val_dataset = RouterDataset(val_samples, tokenizer, args.max_seq_len)

    weighted_sampler = None
    if args.upsample_minority:
        weighted_sampler = build_sampler(train_samples)

    use_bf16 = torch.cuda.is_available() and torch.cuda.get_device_capability()[0] >= 8
    report_to = "wandb" if args.wandb_project else "none"

    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.eval_batch_size,
        learning_rate=args.lr,
        weight_decay=args.weight_decay,
        warmup_ratio=args.warmup_ratio,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="f1_macro",
        greater_is_better=True,
        bf16=use_bf16,
        fp16=(not use_bf16 and torch.cuda.is_available()),
        logging_steps=10,
        dataloader_num_workers=4,
        report_to=report_to,
        run_name=f"router-sft-{fold_name}",
        seed=args.seed,
        save_total_limit=2,
    )

    if args.wandb_project:
        os.environ["WANDB_PROJECT"] = args.wandb_project

    trainer = WeightedCETrainer(
        class_weights=class_weights,
        weighted_sampler=weighted_sampler,
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        compute_metrics=compute_metrics,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=args.early_stopping_patience)],
    )

    print(f"\n{'=' * 60}")
    print(f"[{fold_name}] Training: {len(train_dataset)} train / {len(val_dataset)} val")
    print(f"  Labels: {dict(train_label_counts)}")
    print(f"  Model: {model_path}, LoRA r={args.lora_r}, lr={args.lr}")
    print(f"{'=' * 60}\n")

    trainer.train()

    adapter_dir = os.path.join(output_dir, "final_adapter")
    model.save_pretrained(adapter_dir)
    tokenizer.save_pretrained(adapter_dir)
    print(f"[{fold_name}] Adapter saved to {adapter_dir}")

    eval_report = per_task_evaluation(trainer, val_dataset, val_samples)
    eval_report["fold"] = fold_name
    eval_report["train_label_counts"] = dict(train_label_counts)
    eval_report["val_label_counts"] = dict(Counter(s["label"] for s in val_samples))

    report_path = os.path.join(output_dir, "eval_report.json")
    with open(report_path, "w") as f:
        json.dump(eval_report, f, indent=2)

    print(f"[{fold_name}] Accuracy: {eval_report['overall_accuracy']:.4f}")
    print(f"[{fold_name}] Confusion matrix: {eval_report['confusion_matrix']}")
    for task, m in sorted(eval_report["per_task"].items()):
        print(f"  {task}: {m['accuracy']:.3f} (n={m['n_samples']})")

    return eval_report


def main():
    args = parse_args()

    if args.dry_run:
        print("Dry run: validating imports and data loading.")
        samples = load_labeled_data(
            data_path=args.data_path, data_dir=args.data_dir,
            max_samples=args.max_samples,
        )
        model_path = resolve_model_path(args.model_name)
        print(f"Model path: {model_path} (exists={os.path.isdir(model_path)})")
        print(f"Split strategy: {args.split_strategy}")
        print(f"Total usable samples: {len(samples)}")
        task_types = sorted(set(s["task_type"] for s in samples))
        print(f"Task types ({len(task_types)}): {task_types}")
        return

    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu_id)
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    os.makedirs(args.output_dir, exist_ok=True)

    samples = load_labeled_data(
        data_path=args.data_path, data_dir=args.data_dir,
        max_samples=args.max_samples,
    )
    model_path = resolve_model_path(args.model_name)
    print(f"Model: {model_path}")

    if args.split_strategy == "stratified":
        train_samples, val_samples = stratified_split(samples, args.eval_split, args.seed)
        train_single_fold(
            train_samples, val_samples,
            model_path, args, args.output_dir, fold_name="stratified",
        )

    elif args.split_strategy == "leave_one_out":
        folds = leave_one_out_splits(samples)
        all_reports = []
        for held_out_task, train_samples, val_samples in folds:
            fold_dir = os.path.join(args.output_dir, f"fold_{held_out_task}")
            os.makedirs(fold_dir, exist_ok=True)
            report = train_single_fold(
                train_samples, val_samples,
                model_path, args, fold_dir, fold_name=f"LOO-{held_out_task}",
            )
            report["held_out_task"] = held_out_task
            all_reports.append(report)

        accs = [r["overall_accuracy"] for r in all_reports]
        summary = {
            "strategy": "leave_one_out",
            "n_folds": len(all_reports),
            "mean_accuracy": float(np.mean(accs)),
            "std_accuracy": float(np.std(accs)),
            "per_fold": {r["held_out_task"]: r["overall_accuracy"] for r in all_reports},
        }
        summary_path = os.path.join(args.output_dir, "loo_summary.json")
        with open(summary_path, "w") as f:
            json.dump(summary, f, indent=2)
        print(f"\n{'=' * 60}")
        print(f"LOO CV: mean accuracy = {summary['mean_accuracy']:.4f} ± {summary['std_accuracy']:.4f}")
        for task, acc in sorted(summary["per_fold"].items()):
            print(f"  {task}: {acc:.4f}")
        print(f"Summary saved to {summary_path}")


if __name__ == "__main__":
    main()

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
import warnings
from collections import Counter
from typing import List, Dict, Any, Optional, Tuple

import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
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

RAW_LABEL_MAP = {
    "internal-preferred": "internal",
    "det-preferred": "deterministic",
    "internal": "internal",
    "deterministic": "deterministic",
}

SYSTEM_PROMPT = (
    "You are a routing classifier. Given the current observation and action history, "
    "predict which reasoning modality will lead to a better outcome."
)


def parse_args():
    p = argparse.ArgumentParser(description="Router SFT: finetune LLM for 2-way routing classification")
    p.add_argument("--data_path", type=str, default=None,
                    help="Single JSONL file (e.g. sft_triples.jsonl from death_aware_labeling)")
    p.add_argument("--data_dir", type=str, default=None,
                    help="Directory containing {task_type}/labeled_steps.jsonl (legacy)")
    p.add_argument("--model_name", type=str, default="Qwen/Qwen3-1.7B",
                    help="HuggingFace model name or local path")
    p.add_argument("--output_dir", type=str, default="results/router_sft/",
                    help="Output directory for checkpoints and reports")
    p.add_argument("--epochs", type=int, default=3)
    p.add_argument("--batch_size", type=int, default=32)
    p.add_argument("--eval_batch_size", type=int, default=32)
    p.add_argument("--lr", type=float, default=2e-5)
    p.add_argument("--lora_r", type=int, default=16)
    p.add_argument("--lora_alpha", type=int, default=32)
    p.add_argument("--lora_dropout", type=float, default=0.05)
    p.add_argument("--max_seq_len", type=int, default=2048)
    p.add_argument("--gpu_id", type=int, default=0)
    p.add_argument("--wandb_project", type=str, default="simgate-router-sft")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--eval_split", type=float, default=0.2)
    p.add_argument("--warmup_ratio", type=float, default=0.1)
    p.add_argument("--weight_decay", type=float, default=0.01)
    p.add_argument("--early_stopping_patience", type=int, default=2)
    p.add_argument("--dry_run", action="store_true", help="Only validate imports and args, skip training")
    p.add_argument("--class_weights", type=str, default=None,
                    help='"auto" for inverse-frequency weights, or "w0,w1" (internal:w0, det:w1)')
    p.add_argument("--min_internal_samples", type=int, default=10,
                    help="Warn if internal samples < this threshold (default: 10)")
    p.add_argument("--upsample_minority", action="store_true",
                    help="Use WeightedRandomSampler to oversample minority class")
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
        f"<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n"
        f"<|im_start|>user\n"
        f"Observation: {observation}\n"
        f"Action history: {history_summary}<|im_end|>"
    )


def _parse_record(record: Dict, fallback_task_type: str = "unknown") -> Optional[Dict]:
    raw_label = record.get("label", "")
    label = RAW_LABEL_MAP.get(raw_label)
    if label is None:
        return None
    return {
        "observation": record.get("observation", ""),
        "action_history": record.get("action_history", []),
        "label": label,
        "label_id": LABEL2ID[label],
        "task_type": record.get("task_type", record.get("task_name", fallback_task_type)),
        "signal_source": record.get("signal_source", ""),
    }


def load_labeled_data(data_path: Optional[str] = None,
                      data_dir: Optional[str] = None) -> List[Dict[str, Any]]:
    files: List[str] = []

    if data_path:
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Data file not found: {data_path}")
        files = [data_path]
    elif data_dir:
        pattern = os.path.join(data_dir, "*", "labeled_steps.jsonl")
        files = sorted(glob.glob(pattern))
        if not files:
            pattern_flat = os.path.join(data_dir, "labeled_steps.jsonl")
            if os.path.exists(pattern_flat):
                files = [pattern_flat]
        if not files:
            raise FileNotFoundError(f"No labeled_steps.jsonl found in {data_dir}")
    else:
        raise ValueError("Must specify --data_path or --data_dir")

    samples = []
    skipped = Counter()
    for fpath in files:
        fallback_task = os.path.basename(os.path.dirname(fpath))
        with open(fpath) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                record = json.loads(line)
                parsed = _parse_record(record, fallback_task)
                if parsed is None:
                    skipped[record.get("label", "?")] += 1
                    continue
                samples.append(parsed)

    print(f"Loaded {len(samples)} samples from {len(files)} file(s)")
    if skipped:
        print(f"  Skipped labels: {dict(skipped)}")
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
# Class weighting
# ---------------------------------------------------------------------------

def compute_class_weights(train_samples: List[Dict], mode: str = "auto") -> torch.Tensor:
    # "auto": weight_c = N_total / (num_classes * N_c), i.e. inverse frequency —
    #         rarer class gets proportionally higher weight.
    # "w0,w1": manual weights, e.g. "1.0,5.0" -> internal=1.0, deterministic=5.0
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
            raise ValueError(f"Expected {num_classes} weights, got {len(parts)}: {mode}")
        weights = torch.tensor(parts, dtype=torch.float32)
    return weights


class WeightedCETrainer(Trainer):
    """Trainer with class-weighted CrossEntropyLoss and optional WeightedRandomSampler."""

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
        print(f"  model_name:            {args.model_name}")
        print(f"  data_path:             {args.data_path}")
        print(f"  data_dir:              {args.data_dir}")
        print(f"  output_dir:            {args.output_dir}")
        print(f"  lr:                    {args.lr}")
        print(f"  batch_size:            {args.batch_size}")
        print(f"  max_seq_len:           {args.max_seq_len}")
        print(f"  class_weights:         {args.class_weights}")
        print(f"  min_internal_samples:  {args.min_internal_samples}")
        print(f"  upsample_minority:     {args.upsample_minority}")
        return

    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu_id)
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    os.makedirs(args.output_dir, exist_ok=True)

    samples = load_labeled_data(data_path=args.data_path, data_dir=args.data_dir)
    train_samples, val_samples = stratified_split(samples, args.eval_split, args.seed)

    # --- Check minority class sample count ---
    train_label_counts = Counter(s["label"] for s in train_samples)
    n_internal = train_label_counts.get("internal", 0)
    if n_internal < args.min_internal_samples:
        warnings.warn(
            f"Only {n_internal} internal samples in training set "
            f"(threshold: {args.min_internal_samples}). "
            f"Consider collecting more data or using --class_weights auto.",
            stacklevel=1,
        )

    # --- Compute class weights (inverse frequency or manual) ---
    class_weights = None
    if args.class_weights is not None:
        class_weights = compute_class_weights(train_samples, args.class_weights)
        weight_dict = {label: class_weights[lid].item() for label, lid in LABEL2ID.items()}
        print(f"Class weights: {weight_dict}")
        print(f"Effective sample counts: {dict(train_label_counts)}")

    model, tokenizer = setup_model(args.model_name, args)

    train_dataset = RouterDataset(train_samples, tokenizer, args.max_seq_len)
    val_dataset = RouterDataset(val_samples, tokenizer, args.max_seq_len)

    # --- Build WeightedRandomSampler for minority oversampling ---
    # Per-sample weight = 1 / count_of_its_class, so minority samples are drawn more often.
    weighted_sampler = None
    if args.upsample_minority:
        sample_weights = [1.0 / train_label_counts[s["label"]] for s in train_samples]
        weighted_sampler = WeightedRandomSampler(
            weights=sample_weights,
            num_samples=len(train_samples),
            replacement=True,
        )
        print(f"Upsampling enabled: WeightedRandomSampler with {len(train_samples)} draws/epoch")

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

    # --- Log class weighting config to W&B ---
    try:
        import wandb
        wandb_config = vars(args).copy()
        if class_weights is not None:
            wandb_config["class_weights_values"] = {
                label: class_weights[lid].item() for label, lid in LABEL2ID.items()
            }
        wandb_config["train_label_counts"] = dict(train_label_counts)
        wandb_config["upsample_minority"] = args.upsample_minority
        wandb.init(
            project=args.wandb_project,
            name=training_args.run_name,
            config=wandb_config,
        )
    except Exception:
        pass

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

    print(f"\n{'='*60}")
    print(f"Starting training: {len(train_dataset)} train / {len(val_dataset)} val samples")
    print(f"Model: {args.model_name}, LoRA r={args.lora_r}, lr={args.lr}")
    if class_weights is not None:
        print(f"Class weights: {class_weights.tolist()}")
    if args.upsample_minority:
        print("Minority oversampling: enabled")
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

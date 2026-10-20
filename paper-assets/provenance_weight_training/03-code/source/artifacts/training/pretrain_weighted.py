"""Weighted pretraining for Qwen3-0.6B on contaminated corpora.

Supports four weighting methods:
  - uniform:  all samples equally weighted (baseline)
  - grid:     fixed b value per run (Drayson et al. EMNLP 2025). Grid search = run
               once per b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, pick best val ppl.
  - adaptive: batch-adaptive b* via α_eff convergence theory (ours, min-intervention)
  - ess_only: b* = max{b : ESS(b) ≥ n_min} (max-intervention baseline)

Data format: jsonl with {"text": "...", "q_score": 0.xx, "label": "human"/"synthetic"}
"""

import argparse
import json
import math
import os
import sys
import time
from pathlib import Path

import torch
from torch.utils.data import Dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
    set_seed,
)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from weighting.alpha_eff import (
    compute_alpha_eff,
    compute_ess,
    compute_sample_weights,
    find_ess_only_b,
    find_optimal_b,
)


GRID_B_VALUES = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]


class WeightedTextDataset(Dataset):
    def __init__(self, data_path: str, tokenizer, max_length: int = 2048):
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.examples = []

        with open(data_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                item = json.loads(line)
                self.examples.append(item)

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        item = self.examples[idx]
        encoding = self.tokenizer(
            item["text"],
            truncation=True,
            max_length=self.max_length,
            padding="max_length",
            return_tensors="pt",
        )
        input_ids = encoding["input_ids"].squeeze(0)
        attention_mask = encoding["attention_mask"].squeeze(0)
        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "labels": input_ids.clone(),
            "q_score": item.get("q_score", 0.0),
        }


def collate_fn(batch):
    input_ids = torch.stack([x["input_ids"] for x in batch])
    attention_mask = torch.stack([x["attention_mask"] for x in batch])
    labels = torch.stack([x["labels"] for x in batch])
    q_scores = torch.tensor([x["q_score"] for x in batch], dtype=torch.float32)
    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": labels,
        "q_scores": q_scores,
    }


class WeightedTrainer(Trainer):
    def __init__(self, weighting_method: str, tau: float, n_min: int,
                 grid_b_value: float = 0.0, log_path: str = None, **kwargs):
        super().__init__(**kwargs)
        self.weighting_method = weighting_method
        self.tau = tau
        self.n_min = n_min
        self.grid_b_value = grid_b_value
        self.log_path = log_path
        self._step_metrics = []

    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
        q_scores = inputs.pop("q_scores")
        labels = inputs.get("labels")

        outputs = model(**inputs)
        logits = outputs.logits

        shift_logits = logits[..., :-1, :].contiguous()
        shift_labels = labels[..., 1:].contiguous()
        attention_mask = inputs.get("attention_mask")
        if attention_mask is not None:
            shift_mask = attention_mask[..., 1:].contiguous()
        else:
            shift_mask = torch.ones_like(shift_labels, dtype=torch.float32)

        loss_fct = torch.nn.CrossEntropyLoss(reduction="none")
        per_token_loss = loss_fct(
            shift_logits.view(-1, shift_logits.size(-1)),
            shift_labels.view(-1),
        ).view(shift_labels.size())

        # Mask padding tokens
        per_token_loss = per_token_loss * shift_mask

        # Per-sample loss: mean over tokens
        token_counts = shift_mask.sum(dim=-1).clamp(min=1)
        per_sample_loss = per_token_loss.sum(dim=-1) / token_counts

        unweighted_loss = per_sample_loss.mean()

        b_val = 0.0
        alpha_val = compute_alpha_eff(q_scores, 0.0)
        ess_val = float(q_scores.numel())

        if self.weighting_method == "uniform":
            loss = unweighted_loss
        elif self.weighting_method == "grid":
            b_val = self.grid_b_value
            weights = compute_sample_weights(q_scores, b_val)
            weights = weights.to(per_sample_loss.device)
            loss = (per_sample_loss * weights).sum() / weights.sum()
            alpha_val = compute_alpha_eff(q_scores, b_val)
            ess_val = compute_ess(q_scores, b_val)
        elif self.weighting_method == "adaptive":
            b_val = find_optimal_b(q_scores, tau=self.tau, n_min=self.n_min)
            weights = compute_sample_weights(q_scores, b_val)
            weights = weights.to(per_sample_loss.device)
            loss = (per_sample_loss * weights).sum() / weights.sum()
            alpha_val = compute_alpha_eff(q_scores, b_val)
            ess_val = compute_ess(q_scores, b_val)
        elif self.weighting_method == "ess_only":
            b_val = find_ess_only_b(q_scores, n_min=self.n_min)
            weights = compute_sample_weights(q_scores, b_val)
            weights = weights.to(per_sample_loss.device)
            loss = (per_sample_loss * weights).sum() / weights.sum()
            alpha_val = compute_alpha_eff(q_scores, b_val)
            ess_val = compute_ess(q_scores, b_val)
        else:
            raise ValueError(f"Unknown weighting method: {self.weighting_method}")

        if model.training:
            step_info = {
                "step": self.state.global_step if self.state else 0,
                "loss": float(loss.detach()),
                "unweighted_loss": float(unweighted_loss.detach()),
                "b": b_val,
                "alpha_eff": alpha_val,
                "ess": ess_val,
                "mean_q": float(q_scores.mean()),
                "method": self.weighting_method,
            }
            self._step_metrics.append(step_info)

            if self.log_path and len(self._step_metrics) % 10 == 0:
                self._flush_metrics()

        return (loss, outputs) if return_outputs else loss

    def _flush_metrics(self):
        if not self._step_metrics or not self.log_path:
            return
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)
        with open(self.log_path, "a") as f:
            for m in self._step_metrics:
                f.write(json.dumps(m) + "\n")
        self._step_metrics = []

    def training_step(self, model, inputs, num_items_in_batch=None):
        result = super().training_step(model, inputs, num_items_in_batch=num_items_in_batch)

        if self._step_metrics:
            latest = self._step_metrics[-1]
            self.log({
                "weighting/b": latest["b"],
                "weighting/alpha_eff": latest["alpha_eff"],
                "weighting/ess": latest["ess"],
                "weighting/mean_q": latest["mean_q"],
                "weighting/unweighted_loss": latest["unweighted_loss"],
                "weighting/weighted_loss": latest["loss"],
            })

        return result

    def save_model(self, output_dir=None, _internal_call=False):
        super().save_model(output_dir, _internal_call)
        self._flush_metrics()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Weighted pretraining for LMs on contaminated corpora"
    )
    parser.add_argument("--data_path", type=str, required=True,
                        help="Path to training data (jsonl)")
    parser.add_argument("--output_dir", type=str, required=True,
                        help="Output directory for checkpoints and logs")
    parser.add_argument("--model_name", type=str, default="Qwen/Qwen3-0.6B",
                        help="HuggingFace model name or path")
    parser.add_argument("--weighting_method", type=str, default="adaptive",
                        choices=["uniform", "grid", "adaptive", "ess_only"],
                        help="Weighting method: uniform / grid / adaptive / ess_only")
    parser.add_argument("--grid_b_value", type=float, default=1.0,
                        help="Fixed b value for grid method (one run per b, "
                             "grid search selects best across runs)")
    parser.add_argument("--contamination_ratio", type=float, default=0.2,
                        help="Expected contamination ratio (for adaptive tau)")
    parser.add_argument("--num_train_tokens", type=int, default=None,
                        help="Total training tokens (converted to max_steps)")
    parser.add_argument("--max_steps", type=int, default=-1,
                        help="Max training steps (overrides num_train_tokens)")
    parser.add_argument("--num_train_epochs", type=float, default=1.0,
                        help="Number of training epochs")
    parser.add_argument("--batch_size", type=int, default=4,
                        help="Per-device training batch size")
    parser.add_argument("--gradient_accumulation_steps", type=int, default=4,
                        help="Gradient accumulation steps")
    parser.add_argument("--learning_rate", type=float, default=5e-5,
                        help="Learning rate")
    parser.add_argument("--max_length", type=int, default=2048,
                        help="Max sequence length")
    parser.add_argument("--tau", type=float, default=None,
                        help="Alpha_eff target threshold (adaptive). "
                             "Defaults to 1 - contamination_ratio * 0.5")
    parser.add_argument("--n_min", type=int, default=None,
                        help="Minimum effective sample size. "
                             "Defaults to batch_size // 2")
    parser.add_argument("--use_wandb", action="store_true",
                        help="Enable Weights & Biases logging")
    parser.add_argument("--wandb_project", type=str,
                        default="provenance-weight-training",
                        help="W&B project name")
    parser.add_argument("--wandb_run_name", type=str, default=None,
                        help="W&B run name (passed to TrainingArguments.run_name)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--eval_data_path", type=str, default=None,
                        help="Path to evaluation data (jsonl)")
    parser.add_argument("--eval_steps", type=int, default=500,
                        help="Evaluate every N steps")
    parser.add_argument("--save_steps", type=int, default=500,
                        help="Save checkpoint every N steps")
    parser.add_argument("--logging_steps", type=int, default=10,
                        help="Log every N steps")
    parser.add_argument("--warmup_ratio", type=float, default=0.05,
                        help="Warmup ratio")
    parser.add_argument("--weight_decay", type=float, default=0.01,
                        help="Weight decay")
    parser.add_argument("--save_total_limit", type=int, default=3,
                        help="Keep only N most recent checkpoints")
    parser.add_argument("--save_only_model", action="store_true",
                        help="Save only model weights (skip optimizer/scheduler/rng)")
    parser.add_argument("--resume_from_checkpoint", type=str, default=None,
                        help="Path to checkpoint directory to resume from")
    parser.add_argument("--bf16", action="store_true", default=True,
                        help="Use bfloat16 (default: True)")
    parser.add_argument("--no_bf16", action="store_true",
                        help="Disable bfloat16")
    parser.add_argument("--gradient_checkpointing", action="store_true",
                        help="Enable gradient checkpointing to reduce VRAM usage")
    return parser.parse_args()


def main():
    args = parse_args()
    set_seed(args.seed)

    if args.tau is None:
        args.tau = 1.0 - args.contamination_ratio * 0.5
    if args.n_min is None:
        args.n_min = max(2, args.batch_size // 2)

    use_bf16 = args.bf16 and not args.no_bf16

    report_to = []
    if args.use_wandb:
        report_to.append("wandb")
        os.environ.setdefault("WANDB_PROJECT", args.wandb_project)

    print(f"Loading tokenizer: {args.model_name}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print(f"Loading model: {args.model_name}")
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        torch_dtype=torch.bfloat16 if use_bf16 else torch.float32,
        trust_remote_code=True,
    )

    print(f"Loading training data: {args.data_path}")
    train_dataset = WeightedTextDataset(args.data_path, tokenizer, args.max_length)
    print(f"  {len(train_dataset)} examples loaded")

    eval_dataset = None
    if args.eval_data_path:
        eval_dataset = WeightedTextDataset(args.eval_data_path, tokenizer, args.max_length)
        print(f"  {len(eval_dataset)} eval examples loaded")

    # Convert num_train_tokens to max_steps
    max_steps = args.max_steps
    if max_steps <= 0 and args.num_train_tokens is not None:
        tokens_per_step = (
            args.batch_size * args.gradient_accumulation_steps * args.max_length
        )
        max_steps = args.num_train_tokens // tokens_per_step
        print(f"  num_train_tokens={args.num_train_tokens} → max_steps={max_steps}")

    log_path = os.path.join(args.output_dir, "step_metrics.jsonl")

    training_args = TrainingArguments(
        output_dir=args.output_dir,
        run_name=args.wandb_run_name,
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.learning_rate,
        num_train_epochs=args.num_train_epochs if max_steps <= 0 else 100,
        max_steps=max_steps if max_steps > 0 else -1,
        warmup_ratio=args.warmup_ratio,
        weight_decay=args.weight_decay,
        bf16=use_bf16,
        gradient_checkpointing=args.gradient_checkpointing,
        logging_steps=args.logging_steps,
        eval_steps=args.eval_steps if eval_dataset else None,
        eval_strategy="steps" if eval_dataset else "no",
        save_steps=args.save_steps,
        save_strategy="steps",
        save_total_limit=args.save_total_limit,
        save_only_model=args.save_only_model,
        load_best_model_at_end=eval_dataset is not None,
        metric_for_best_model="eval_loss" if eval_dataset else None,
        report_to=report_to if report_to else "none",
        seed=args.seed,
        dataloader_drop_last=True,
        remove_unused_columns=False,
    )

    trainer = WeightedTrainer(
        weighting_method=args.weighting_method,
        tau=args.tau,
        n_min=args.n_min,
        grid_b_value=args.grid_b_value,
        log_path=log_path,
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        data_collator=collate_fn,
        tokenizer=tokenizer,
    )

    config_summary = {
        "model_name": args.model_name,
        "weighting_method": args.weighting_method,
        "grid_b_value": args.grid_b_value if args.weighting_method == "grid" else None,
        "tau": args.tau,
        "n_min": args.n_min,
        "contamination_ratio": args.contamination_ratio,
        "batch_size": args.batch_size,
        "learning_rate": args.learning_rate,
        "max_steps": max_steps,
        "seed": args.seed,
        "num_examples": len(train_dataset),
    }
    print("\n=== Training Config ===")
    for k, v in config_summary.items():
        print(f"  {k}: {v}")
    print()

    os.makedirs(args.output_dir, exist_ok=True)
    with open(os.path.join(args.output_dir, "config.json"), "w") as f:
        json.dump(config_summary, f, indent=2)

    trainer.train(resume_from_checkpoint=args.resume_from_checkpoint)
    trainer._flush_metrics()
    trainer.save_model(os.path.join(args.output_dir, "final"))
    print(f"\nTraining complete. Model saved to {args.output_dir}/final")


if __name__ == "__main__":
    main()

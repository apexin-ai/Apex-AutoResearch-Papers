"""Condition (b): 1.7B Implicit Router — Qwen3-1.7B SFT with inline routing.

Architecture difference vs Condition (a):
  (a) Explicit: Qwen3-1.7B + classification head → predicts label, separate from action gen
  (b) Implicit: Qwen3-1.7B causal LM → generates "[SIMULATE] action" or "action"
  Same parameter count (1.7B), different task formulation.

Training:
  - Input: implicit_sft.jsonl from ablation_data_converter.py (chat format)
  - Finetune with LoRA on causal LM objective (next-token prediction)
  - Model learns routing signal ([SIMULATE] prefix) as part of generation

Evaluation:
  - Generate action text given (observation, history)
  - Parse output: starts with "[SIMULATE]" → route = deterministic
  - Otherwise → route = internal
  - Feed into ablation_eval_common.run_ablation_eval()

Usage:
  # Train
  python src/ablation_implicit_1_7b.py train --data results/ablation_implicit/implicit_sft.jsonl

  # Evaluate
  python src/ablation_implicit_1_7b.py eval --adapter_path results/implicit_1_7b/final_adapter
"""

import argparse
import json
import os
import sys
from typing import List, Tuple, Dict, Any, Optional

import torch
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
)
from peft import LoraConfig, get_peft_model, TaskType, PeftModel

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

MODEL_ID = "Qwen/Qwen3-1.7B"
SIMULATE_PREFIX = "[SIMULATE]"


# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------

class ImplicitSFTDataset(torch.utils.data.Dataset):
    """Chat-format SFT dataset for causal LM training.

    Each record has messages: [system, user, assistant].
    Tokenizes the full conversation; masks system+user tokens (label=-100),
    only trains on assistant response tokens.
    """

    def __init__(self, records: List[Dict], tokenizer, max_seq_len: int = 512):
        self.records = records
        self.tokenizer = tokenizer
        self.max_seq_len = max_seq_len

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        rec = self.records[idx]
        messages = rec["messages"]

        # Tokenize full conversation using chat template
        full_text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        # Tokenize prompt-only (system + user) to find where assistant starts
        prompt_messages = messages[:-1]
        prompt_text = self.tokenizer.apply_chat_template(
            prompt_messages, tokenize=False, add_generation_prompt=True
        )

        full_ids = self.tokenizer(
            full_text, truncation=True, max_length=self.max_seq_len,
            return_tensors="pt"
        )["input_ids"].squeeze(0)

        prompt_ids = self.tokenizer(
            prompt_text, truncation=True, max_length=self.max_seq_len,
            return_tensors="pt"
        )["input_ids"].squeeze(0)

        labels = full_ids.clone()
        # Mask prompt tokens — only supervise assistant response
        prompt_len = min(len(prompt_ids), len(labels))
        labels[:prompt_len] = -100

        return {
            "input_ids": full_ids,
            "labels": labels,
            "attention_mask": torch.ones_like(full_ids),
        }


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_implicit_sft_data(
    path: str,
    eval_split: float = 0.15,
    seed: int = 42,
) -> Tuple[List[Dict], List[Dict]]:
    """Load implicit_sft.jsonl, split into train/val.

    Returns (train_records, val_records).
    """
    import random
    records = []
    with open(path) as f:
        for line in f:
            records.append(json.loads(line))

    random.seed(seed)
    random.shuffle(records)
    split_idx = int(len(records) * (1 - eval_split))
    return records[:split_idx], records[split_idx:]


# ---------------------------------------------------------------------------
# Training
# ---------------------------------------------------------------------------

def train(args):
    """Finetune Qwen3-1.7B with LoRA on implicit SFT data."""
    train_records, val_records = load_implicit_sft_data(
        args.data, eval_split=args.eval_split, seed=args.seed
    )
    print(f"Train: {len(train_records)}, Val: {len(val_records)}")

    tokenizer = AutoTokenizer.from_pretrained(
        args.model_name, trust_remote_code=True
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        torch_dtype=torch.bfloat16,
        device_map={"": args.gpu_id},
        trust_remote_code=True,
    )

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    train_dataset = ImplicitSFTDataset(train_records, tokenizer, args.max_seq_len)
    val_dataset = ImplicitSFTDataset(val_records, tokenizer, args.max_seq_len)

    # TODO: implement custom data collator for variable-length padding

    training_args = TrainingArguments(
        output_dir=args.output_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size,
        learning_rate=args.lr,
        warmup_ratio=0.1,
        weight_decay=0.01,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        bf16=True,
        logging_steps=10,
        report_to="wandb",
        run_name="implicit-1.7b-sft",
        seed=args.seed,
        save_total_limit=2,
    )

    os.environ["WANDB_PROJECT"] = "simgate-ablation"

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
    )
    trainer.train()

    adapter_dir = os.path.join(args.output_dir, "final_adapter")
    model.save_pretrained(adapter_dir)
    tokenizer.save_pretrained(adapter_dir)
    print(f"Adapter saved to {adapter_dir}")


# ---------------------------------------------------------------------------
# Inference: parse [SIMULATE] prefix from generation
# ---------------------------------------------------------------------------

def parse_implicit_output(text: str) -> Tuple[str, str]:
    """Parse model output into (action, route_decision).

    If output starts with [SIMULATE], route = "deterministic" and action = remainder.
    Otherwise, route = "internal" and action = full output.
    """
    text = text.strip()
    if text.startswith(SIMULATE_PREFIX):
        action = text[len(SIMULATE_PREFIX):].strip()
        return action, "deterministic"
    return text, "internal"


class Implicit1_7BRouter:
    """Inference wrapper: loads finetuned Qwen3-1.7B adapter, generates actions."""

    def __init__(self, adapter_path: str, base_model: str = MODEL_ID, gpu_id: int = 0):
        self.tokenizer = AutoTokenizer.from_pretrained(
            adapter_path, trust_remote_code=True
        )
        base = AutoModelForCausalLM.from_pretrained(
            base_model,
            torch_dtype=torch.bfloat16,
            device_map={"": gpu_id},
            trust_remote_code=True,
        )
        self.model = PeftModel.from_pretrained(base, adapter_path)
        self.model.eval()

    def __call__(
        self,
        observation: str,
        valid_actions: List[str],
        history: List[dict],
    ) -> Tuple[str, str]:
        """Router function compatible with ablation_eval_common.RouterFn."""
        from ablation_data_converter import IMPLICIT_SYSTEM_PROMPT, format_action_history

        hist_strs = [h.get("action", str(h)) for h in history]
        user_content = (
            f"Observation: {observation}\n"
            f"Action history: {format_action_history(hist_strs)}"
        )

        messages = [
            {"role": "system", "content": IMPLICIT_SYSTEM_PROMPT},
            {"role": "user", "content": user_content},
        ]

        prompt = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs, max_new_tokens=64, temperature=0.1, do_sample=True
            )
        new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
        raw_output = self.tokenizer.decode(new_tokens, skip_special_tokens=True).strip()

        action, route = parse_implicit_output(raw_output)

        # Snap action to valid_actions if possible
        if action not in valid_actions:
            # Fuzzy match: find closest valid action
            action_lower = action.lower().strip()
            for va in valid_actions:
                if va.lower().strip() == action_lower:
                    action = va
                    break
            else:
                action = valid_actions[0] if valid_actions else action

        return action, route


# ---------------------------------------------------------------------------
# Evaluation entry point
# ---------------------------------------------------------------------------

def evaluate(args):
    """Run plan-004 evaluation for Condition (b)."""
    from ablation_eval_common import run_ablation_eval, EvalConfig, add_eval_args, config_from_args

    router = Implicit1_7BRouter(
        adapter_path=args.adapter_path,
        base_model=args.model_name,
        gpu_id=args.gpu_id,
    )
    config = config_from_args(args, condition_name="implicit_1_7b")
    results = run_ablation_eval(config, router_fn=router)

    print(f"\n=== Condition (b) Implicit 1.7B Results ===")
    print(f"Mean score: {results['episode_metrics']['mean_score']:.2f}")
    print(f"Death rate: {results['episode_metrics']['death_rate']:.1%}")
    print(f"Routing accuracy: {results['routing_accuracy']['accuracy']:.3f}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Condition (b): 1.7B Implicit Router")
    subparsers = parser.add_subparsers(dest="command")

    # Train subcommand
    train_p = subparsers.add_parser("train")
    train_p.add_argument("--data", type=str, required=True,
                         help="Path to implicit_sft.jsonl")
    train_p.add_argument("--model_name", type=str, default=MODEL_ID)
    train_p.add_argument("--output_dir", type=str, default="results/implicit_1_7b/")
    train_p.add_argument("--epochs", type=int, default=3)
    train_p.add_argument("--batch_size", type=int, default=8)
    train_p.add_argument("--lr", type=float, default=2e-4)
    train_p.add_argument("--lora_r", type=int, default=16)
    train_p.add_argument("--lora_alpha", type=int, default=32)
    train_p.add_argument("--lora_dropout", type=float, default=0.05)
    train_p.add_argument("--max_seq_len", type=int, default=512)
    train_p.add_argument("--eval_split", type=float, default=0.15)
    train_p.add_argument("--gpu_id", type=int, default=1)
    train_p.add_argument("--seed", type=int, default=42)

    # Eval subcommand
    eval_p = subparsers.add_parser("eval")
    eval_p.add_argument("--adapter_path", type=str, required=True)
    eval_p.add_argument("--model_name", type=str, default=MODEL_ID)
    from ablation_eval_common import add_eval_args
    add_eval_args(eval_p)

    args = parser.parse_args()
    if args.command == "train":
        train(args)
    elif args.command == "eval":
        evaluate(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

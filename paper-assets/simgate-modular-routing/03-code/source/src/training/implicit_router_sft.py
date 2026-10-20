# Plan-004 Condition (b): Finetune Qwen3-1.7B as implicit router (causal LM).
#
# Unlike Condition (a) explicit router (classification head), this trains the
# model to generate "[SIMULATE] action" or "action" inline — routing signal
# is embedded in the generated text, not a separate classification output.
#
# Input:  implicit_sft.jsonl from format_implicit_data.py
# Output: LoRA adapter in --output_dir/final_adapter/
#
# Dependencies: transformers, peft, torch

import argparse
import json
import os
import random
import sys
from typing import List, Tuple, Dict, Any

import numpy as np
import torch
from torch.utils.data import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
)
from peft import LoraConfig, get_peft_model, TaskType, PeftModel

MODEL_ID = "Qwen/Qwen3-1.7B"
SIMULATE_PREFIX = "[SIMULATE]"


# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------

class ImplicitSFTDataset(Dataset):
    """Chat-format SFT dataset for causal LM training.

    Each record has messages: [system, user, assistant].
    Tokenizes full conversation; masks system+user tokens (label=-100),
    only supervises assistant response tokens.
    """

    def __init__(self, records: List[Dict], tokenizer, max_seq_len: int = 2048):
        self.records = records
        self.tokenizer = tokenizer
        self.max_seq_len = max_seq_len

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        rec = self.records[idx]
        messages = rec["messages"]

        full_text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
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
        prompt_len = min(len(prompt_ids), len(labels))
        labels[:prompt_len] = -100

        return {
            "input_ids": full_ids,
            "labels": labels,
            "attention_mask": torch.ones_like(full_ids),
        }


class PaddingCollator:
    """Dynamic padding collator for variable-length sequences."""

    def __init__(self, tokenizer, max_seq_len: int = 2048):
        self.pad_id = tokenizer.pad_token_id or tokenizer.eos_token_id
        self.max_seq_len = max_seq_len

    def __call__(self, features: List[Dict]) -> Dict[str, torch.Tensor]:
        max_len = min(
            max(f["input_ids"].size(0) for f in features),
            self.max_seq_len,
        )

        input_ids = []
        labels = []
        attention_mask = []

        for f in features:
            seq_len = f["input_ids"].size(0)
            pad_len = max_len - seq_len

            if pad_len > 0:
                input_ids.append(torch.cat([
                    f["input_ids"],
                    torch.full((pad_len,), self.pad_id, dtype=torch.long),
                ]))
                labels.append(torch.cat([
                    f["labels"],
                    torch.full((pad_len,), -100, dtype=torch.long),
                ]))
                attention_mask.append(torch.cat([
                    f["attention_mask"],
                    torch.zeros(pad_len, dtype=torch.long),
                ]))
            else:
                input_ids.append(f["input_ids"][:max_len])
                labels.append(f["labels"][:max_len])
                attention_mask.append(f["attention_mask"][:max_len])

        return {
            "input_ids": torch.stack(input_ids),
            "labels": torch.stack(labels),
            "attention_mask": torch.stack(attention_mask),
        }


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_implicit_sft_data(
    path: str,
    eval_split: float = 0.15,
    seed: int = 42,
) -> Tuple[List[Dict], List[Dict]]:
    """Load implicit_sft.jsonl with stratified split by task_type."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))

    rng = random.Random(seed)
    by_task: Dict[str, List[Dict]] = {}
    for r in records:
        by_task.setdefault(r.get("task_type", "unknown"), []).append(r)

    train_records, val_records = [], []
    for task, items in by_task.items():
        rng.shuffle(items)
        n_val = max(1, int(len(items) * eval_split))
        val_records.extend(items[:n_val])
        train_records.extend(items[n_val:])

    rng.shuffle(train_records)
    rng.shuffle(val_records)
    return train_records, val_records


# ---------------------------------------------------------------------------
# Training
# ---------------------------------------------------------------------------

def train(args):
    """Finetune Qwen3-1.7B with LoRA on implicit SFT data."""
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    train_records, val_records = load_implicit_sft_data(
        args.data_dir if os.path.isfile(args.data_dir) else os.path.join(args.data_dir, "implicit_sft.jsonl"),
        eval_split=args.eval_split,
        seed=args.seed,
    )
    print(f"Train: {len(train_records)}, Val: {len(val_records)}")

    from collections import Counter
    route_dist = Counter(r["route_label"] for r in train_records)
    print(f"Route distribution (train): {dict(route_dist)}")

    tokenizer = AutoTokenizer.from_pretrained(
        args.model_name, trust_remote_code=True
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        torch_dtype=torch.bfloat16,
        device_map={"": int(os.environ.get("LOCAL_RANK", args.gpu_id))},
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
    collator = PaddingCollator(tokenizer, args.max_seq_len)

    os.makedirs(args.output_dir, exist_ok=True)
    os.environ["WANDB_PROJECT"] = "simgate-ablation"

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
        run_name=f"implicit-1.7b-lr{args.lr}-bs{args.batch_size}",
        seed=args.seed,
        save_total_limit=2,
        gradient_accumulation_steps=max(1, 32 // args.batch_size),
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        data_collator=collator,
    )
    trainer.train()

    adapter_dir = os.path.join(args.output_dir, "final_adapter")
    model.save_pretrained(adapter_dir)
    tokenizer.save_pretrained(adapter_dir)
    print(f"Adapter saved to {adapter_dir}")

    # Save training config for reproducibility
    config_path = os.path.join(args.output_dir, "train_config.json")
    with open(config_path, "w") as f:
        json.dump(vars(args), f, indent=2)


# ---------------------------------------------------------------------------
# Inference
# ---------------------------------------------------------------------------

def parse_implicit_output(text: str) -> Tuple[str, str]:
    """Parse model output into (action, route_decision).

    Starts with [SIMULATE] → route = "deterministic", action = remainder.
    Otherwise → route = "internal", action = full text.
    """
    text = text.strip()
    if text.startswith(SIMULATE_PREFIX):
        action = text[len(SIMULATE_PREFIX):].strip()
        return action, "deterministic"
    return text, "internal"


class Implicit1_7BRouter:
    """Inference wrapper: loads finetuned adapter, generates actions with routing."""

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

        sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
        from training.format_implicit_data import IMPLICIT_SYSTEM_PROMPT, format_action_history
        self._system_prompt = IMPLICIT_SYSTEM_PROMPT
        self._format_history = format_action_history

    def __call__(
        self,
        observation: str,
        valid_actions: List[str],
        history: List[dict],
    ) -> Tuple[str, str]:
        """RouterFn-compatible interface: (obs, valid_actions, history) → (action, route)."""
        hist_strs = [h.get("action", str(h)) for h in history]
        user_content = (
            f"Observation: {observation}\n"
            f"Action history: {self._format_history(hist_strs)}"
        )

        messages = [
            {"role": "system", "content": self._system_prompt},
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

        if action not in valid_actions:
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
    """Run evaluation for Condition (b) using ablation_eval_common."""
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    from ablation_eval_common import run_ablation_eval, config_from_args, add_eval_args

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
    parser = argparse.ArgumentParser(
        description="Plan-004 Condition (b): 1.7B Implicit Router — train or evaluate"
    )
    subparsers = parser.add_subparsers(dest="command")

    # --- train ---
    train_p = subparsers.add_parser("train")
    train_p.add_argument("--data_dir", type=str, required=True,
                         help="Path to implicit_sft.jsonl or directory containing it")
    train_p.add_argument("--model_name", type=str, default=MODEL_ID)
    train_p.add_argument("--output_dir", type=str, default="checkpoints/plan-004-implicit")
    train_p.add_argument("--epochs", type=int, default=3)
    train_p.add_argument("--batch_size", type=int, default=32)
    train_p.add_argument("--lr", type=float, default=2e-5)
    train_p.add_argument("--lora_r", type=int, default=16)
    train_p.add_argument("--lora_alpha", type=int, default=32)
    train_p.add_argument("--lora_dropout", type=float, default=0.05)
    train_p.add_argument("--max_seq_len", type=int, default=2048)
    train_p.add_argument("--eval_split", type=float, default=0.15)
    train_p.add_argument("--gpu_id", type=int, default=1)
    train_p.add_argument("--seed", type=int, default=42)

    # --- eval ---
    eval_p = subparsers.add_parser("eval")
    eval_p.add_argument("--adapter_path", type=str, required=True)
    eval_p.add_argument("--model_name", type=str, default=MODEL_ID)
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    try:
        from ablation_eval_common import add_eval_args
        add_eval_args(eval_p)
    except ImportError:
        eval_p.add_argument("--task_types", type=str, default="boil,melt,change-the-state-of-matter-of")
        eval_p.add_argument("--max_variations", type=int, default=5)
        eval_p.add_argument("--max_steps", type=int, default=30)
        eval_p.add_argument("--gpu_id", type=int, default=0)
        eval_p.add_argument("--output_dir", type=str, default="results/ablation/")
        eval_p.add_argument("--oracle_data", type=str,
                            default="results/sft_data_death_aware/sft_triples.jsonl")

    args = parser.parse_args()
    if args.command == "train":
        train(args)
    elif args.command == "eval":
        evaluate(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

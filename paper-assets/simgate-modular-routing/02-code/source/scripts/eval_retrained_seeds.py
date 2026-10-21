# Post-retrain evaluation: eval retrained seeds 42-45 with BOTH split methods
# and compare against original checkpoints + seeds 46-49.
#
# Usage:
#   PYTHONPATH=src python scripts/eval_retrained_seeds.py \
#       --data_path data/plan-004-implicit/implicit_sft.jsonl \
#       --model_name /root/autodl-tmp/models/Qwen3-1.7B \
#       --gpu_id 0
#
# Output: results/retrain_eval/comparison.json

import argparse
import json
import os
import sys
import random
from collections import Counter, defaultdict
from typing import Dict, List, Tuple

import numpy as np
import torch
from sklearn.metrics import balanced_accuracy_score, recall_score
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from training.implicit_router_sft import (
    load_implicit_sft_data,
    parse_implicit_output,
    MODEL_ID,
)
from training.format_implicit_data import IMPLICIT_SYSTEM_PROMPT


def episode_level_split(records, eval_ratio=0.15, seed=42):
    """Independent episode-level split (different from training's step-level split)."""
    rng = random.Random(seed)

    episodes = defaultdict(list)
    for r in records:
        key = (r.get("task_type", "unknown"), r.get("variation", -1))
        episodes[key].append(r)

    by_task = defaultdict(list)
    for key in episodes:
        by_task[key[0]].append(key)

    train_set, val_set = [], []
    for task, ep_keys in sorted(by_task.items()):
        rng.shuffle(ep_keys)
        n_val = max(1, int(len(ep_keys) * eval_ratio))
        for k in ep_keys[:n_val]:
            val_set.extend(episodes[k])
        for k in ep_keys[n_val:]:
            train_set.extend(episodes[k])

    rng.shuffle(train_set)
    rng.shuffle(val_set)
    return train_set, val_set


def generation_eval(model, tokenizer, val_records, device="cuda:0"):
    """Generation-based eval matching paper methodology."""
    model.eval()
    y_true, y_pred = [], []

    for rec in val_records:
        messages = rec["messages"][:2]
        prompt = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True,
                           max_length=2048).to(device)
        with torch.no_grad():
            outputs = model.generate(
                **inputs, max_new_tokens=64, temperature=0.1,
                do_sample=True, pad_token_id=tokenizer.pad_token_id,
            )
        new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
        raw = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
        _, route = parse_implicit_output(raw)
        y_pred.append(route)
        y_true.append(rec["route_label"])

    label_map = {"internal": 0, "deterministic": 1}
    yt = [label_map[y] for y in y_true]
    yp = [label_map[y] for y in y_pred]

    return {
        "balanced_accuracy": float(balanced_accuracy_score(yt, yp)),
        "internal_recall": float(recall_score(yt, yp, pos_label=0, zero_division=0)),
        "det_recall": float(recall_score(yt, yp, pos_label=1, zero_division=0)),
        "n_val": len(val_records),
    }


def eval_checkpoint(adapter_path, base_model, tokenizer, val_records, device):
    """Load adapter and evaluate."""
    base = AutoModelForCausalLM.from_pretrained(
        base_model, torch_dtype=torch.bfloat16,
        device_map={"": device}, trust_remote_code=True,
    )
    model = PeftModel.from_pretrained(base, adapter_path)
    model.eval()
    result = generation_eval(model, tokenizer, val_records, device=f"cuda:{device}")
    del model, base
    torch.cuda.empty_cache()
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data_path", required=True)
    p.add_argument("--model_name", default=MODEL_ID)
    p.add_argument("--gpu_id", type=int, default=0)
    p.add_argument("--output_dir", default="results/retrain_eval")
    args = p.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    device = args.gpu_id

    # Load all data
    all_records = []
    with open(args.data_path) as f:
        for line in f:
            line = line.strip()
            if line:
                all_records.append(json.loads(line))

    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Two split methods
    splits = {
        "training_split": {},   # per-seed step-level (from load_implicit_sft_data)
        "episode_split": {},    # independent episode-level
    }

    # Episode-level split (same for all seeds)
    _, ep_val = episode_level_split(all_records, eval_ratio=0.15, seed=42)
    print(f"Episode-level val set: {len(ep_val)} records")

    # Checkpoint sources
    seeds_config = {
        42: {
            "retrained": "checkpoints/retrain-seed42/final_adapter",
            "original": "checkpoints/plan-004-implicit/final_adapter",
        },
        43: {
            "retrained": "checkpoints/retrain-seed43/final_adapter",
            "original": "checkpoints/seed-robustness-seed43/final_adapter",
        },
        44: {
            "retrained": "checkpoints/retrain-seed44/final_adapter",
            "original": "checkpoints/seed-robustness-seed44/final_adapter",
        },
        45: {
            "retrained": "checkpoints/retrain-seed45/final_adapter",
            "original": "checkpoints/seed-robustness-seed45/final_adapter",
        },
    }

    # Reference: seeds 46-49 (already trained with current protocol)
    for s in [46, 47, 48, 49]:
        seeds_config[s] = {
            "original": f"checkpoints/seed-robustness-seed{s}/final_adapter",
        }

    results = {}
    for seed, paths in sorted(seeds_config.items()):
        print(f"\n=== Seed {seed} ===")

        # Training-split val (per-seed)
        _, train_split_val = load_implicit_sft_data(args.data_path, eval_split=0.15, seed=seed)

        for variant, adapter_path in paths.items():
            if not os.path.isdir(adapter_path):
                print(f"  {variant}: MISSING {adapter_path}")
                continue

            # Eval on training split
            r_train = eval_checkpoint(adapter_path, args.model_name, tokenizer, train_split_val, device)
            # Eval on episode split
            r_ep = eval_checkpoint(adapter_path, args.model_name, tokenizer, ep_val, device)

            key = f"seed{seed}_{variant}"
            results[key] = {
                "seed": seed,
                "variant": variant,
                "adapter_path": adapter_path,
                "training_split_bal_acc": r_train["balanced_accuracy"],
                "episode_split_bal_acc": r_ep["balanced_accuracy"],
                "delta": abs(r_train["balanced_accuracy"] - r_ep["balanced_accuracy"]),
                "training_split_full": r_train,
                "episode_split_full": r_ep,
            }
            print(f"  {variant}: train_split={r_train['balanced_accuracy']:.4f}, "
                  f"ep_split={r_ep['balanced_accuracy']:.4f}, "
                  f"Δ={abs(r_train['balanced_accuracy'] - r_ep['balanced_accuracy']):.4f}")

    # Summary
    out_path = os.path.join(args.output_dir, "comparison.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()

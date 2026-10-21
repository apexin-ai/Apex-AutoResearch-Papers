#!/usr/bin/env python3
"""DPO baseline training for contrastive entrainment calibration.

Config aligned with GRPO (exp002) and ACT (exp004):
- Model: Qwen3-8B
- LoRA: r=64, alpha=64, modules=[q_proj, k_proj, v_proj, o_proj]
- LR: 5e-5, warmup: 200 steps
- Max steps: 8000, save every 500 steps
- Gradient accumulation: 16, bf16

Usage:
  python run_dpo.py [--beta 0.1] [--max-steps 8000]
"""

import json
import logging
import os
import sys
from pathlib import Path

import torch
from datasets import Dataset
from peft import LoraConfig
from transformers import AutoTokenizer
from trl import DPOConfig, DPOTrainer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("dpo")

MODEL_PATH = "/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B"
DATA_PATH = "/root/contrastive_entrain_calib/data/dpo_train.jsonl"
OUTPUT_DIR = "/root/autodl-tmp/contrastive_entrain_calib/outputs/exp_dpo_baseline"
SEED = 42


def load_dpo_dataset():
    """Load DPO JSONL and convert to HF Dataset."""
    records = []
    with open(DATA_PATH) as f:
        for line in f:
            d = json.loads(line)
            records.append({
                "prompt": d["prompt"],
                "chosen": d["chosen"],
                "rejected": d["rejected"],
            })
    logger.info("Loaded %d DPO pairs from %s", len(records), DATA_PATH)
    return Dataset.from_list(records)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--beta", type=float, default=0.1)
    parser.add_argument("--max-steps", type=int, default=8000)
    parser.add_argument("--lr", type=float, default=5e-5)
    parser.add_argument("--warmup-steps", type=int, default=200)
    parser.add_argument("--save-steps", type=int, default=500)
    parser.add_argument("--logging-steps", type=int, default=10)
    parser.add_argument("--grad-accum", type=int, default=16)
    parser.add_argument("--max-length", type=int, default=1280)
    parser.add_argument("--max-prompt-length", type=int, default=1024)
    parser.add_argument("--output-dir", default=OUTPUT_DIR)
    parser.add_argument("--seed", type=int, default=SEED)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    torch.manual_seed(args.seed)

    logger.info("=== DPO Baseline Training ===")
    logger.info("Beta: %.2f, LR: %.1e, Max steps: %d", args.beta, args.lr, args.max_steps)

    model_path = MODEL_PATH if Path(MODEL_PATH).exists() else "Qwen/Qwen3-8B"

    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id

    dataset = load_dpo_dataset()

    peft_config = LoraConfig(
        r=64,
        lora_alpha=64,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
        bias="none",
        task_type="CAUSAL_LM",
    )

    training_args = DPOConfig(
        output_dir=args.output_dir,
        beta=args.beta,
        learning_rate=args.lr,
        warmup_steps=args.warmup_steps,
        max_steps=args.max_steps,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=args.grad_accum,
        gradient_checkpointing=True,
        logging_steps=args.logging_steps,
        save_steps=args.save_steps,
        bf16=True,
        seed=args.seed,
        max_length=args.max_length,
        max_prompt_length=args.max_prompt_length,
        remove_unused_columns=False,
        report_to="none",
    )

    trainer = DPOTrainer(
        model=model_path,
        args=training_args,
        train_dataset=dataset,
        processing_class=tokenizer,
        peft_config=peft_config,
    )

    logger.info("Starting DPO training...")
    trainer.train()

    final_dir = os.path.join(args.output_dir, "final")
    trainer.save_model(final_dir)
    tokenizer.save_pretrained(final_dir)
    logger.info("Training complete. Final checkpoint: %s", final_dir)


if __name__ == "__main__":
    main()

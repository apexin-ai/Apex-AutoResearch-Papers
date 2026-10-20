"""GRPO training script for probe generation refinement.

Input: SFT checkpoint + data/train.jsonl
Output: GRPO-refined checkpoint in checkpoints/grpo/
Dependencies: transformers, trl, peft, torch, wandb
"""

import argparse
import json
import logging
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import torch
from datasets import Dataset
from peft import LoraConfig, PeftModel, TaskType
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import GRPOConfig, GRPOTrainer

from src.prompts import PROBE_GENERATION_SYSTEM, format_grpo_prompt
from src.reward_funcs import (
    fix_based_reward,
    probe_dependence_reward,
    probe_execution_bonus,
    set_policy_model,
)

logger = logging.getLogger(__name__)


def load_prompts(path: str) -> Dataset:
    """Load dataset and format as GRPO prompts with metadata."""
    records = []
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            prompt_text = format_grpo_prompt(row)
            records.append({
                "prompt": [
                    {"role": "system", "content": PROBE_GENERATION_SYSTEM},
                    {"role": "user", "content": prompt_text},
                ],
                "buggy_code": row["buggy_code"],
                "solution": row["solution"],
                "test_code": row["test_code"],
            })
    return Dataset.from_list(records)


def build_reward_funcs() -> list:
    """Build the list of reward functions for GRPO."""
    return [fix_based_reward, probe_execution_bonus, probe_dependence_reward]


def main():
    parser = argparse.ArgumentParser(description="GRPO training for probe generation")
    parser.add_argument("--sft-checkpoint", type=str, required=True, help="Path to SFT checkpoint")
    parser.add_argument("--model-name", type=str, default="Qwen/Qwen3-8B")
    parser.add_argument("--train-data", type=str, default="data/train.jsonl")
    parser.add_argument("--output-dir", type=str, default="checkpoints/grpo")
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--num-generations", type=int, default=4)
    parser.add_argument("--lr", type=float, default=5e-6)
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--per-device-batch-size", type=int, default=2)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=8)
    parser.add_argument("--kl-coef", type=float, default=0.05)
    parser.add_argument("--max-completion-length", type=int, default=1024)
    parser.add_argument("--max-prompt-length", type=int, default=1536)
    parser.add_argument("--logging-steps", type=int, default=5)
    parser.add_argument("--save-steps", type=int, default=50)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--wandb-project", type=str, default="rl-active-probe-fl")
    parser.add_argument("--wandb-run-name", type=str, default=None)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--bf16", action="store_true", default=True)
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)

    if args.wandb_run_name:
        os.environ["WANDB_PROJECT"] = args.wandb_project

    sft_path = Path(args.sft_checkpoint)
    if not sft_path.exists():
        raise FileNotFoundError(f"SFT checkpoint not found: {sft_path}")

    logger.info(f"Loading model from SFT checkpoint: {sft_path}")
    adapter_config = sft_path / "adapter_config.json"
    if adapter_config.exists():
        logger.info("Detected LoRA adapter checkpoint, loading base model + adapter")
        tokenizer = AutoTokenizer.from_pretrained(str(sft_path), trust_remote_code=True)
        base_model = AutoModelForCausalLM.from_pretrained(
            args.model_name,
            torch_dtype=torch.bfloat16 if args.bf16 else torch.float32,
            trust_remote_code=True,
            device_map="auto",
        )
        model = PeftModel.from_pretrained(base_model, str(sft_path), is_trainable=True)
        logger.info("LoRA adapter loaded (trainable) for GRPO")
    else:
        logger.info("Detected full model checkpoint")
        tokenizer = AutoTokenizer.from_pretrained(str(sft_path), trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(
            str(sft_path),
            torch_dtype=torch.bfloat16 if args.bf16 else torch.float32,
            trust_remote_code=True,
            device_map="auto",
        )

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Disable Qwen3 thinking mode: flip the default so <think> is not inserted
    if hasattr(tokenizer, 'chat_template') and tokenizer.chat_template and '<think>' in tokenizer.chat_template:
        tokenizer.chat_template = tokenizer.chat_template.replace(
            'enable_thinking is not defined or enable_thinking is true',
            'enable_thinking is defined and enable_thinking is true'
        )
        logger.info("Patched tokenizer chat_template to disable thinking mode")

    set_policy_model(model, tokenizer)

    logger.info("Loading training data...")
    train_dataset = load_prompts(args.train_data)
    logger.info(f"Train: {len(train_dataset)} prompts")

    reward_funcs = build_reward_funcs()

    training_args = GRPOConfig(
        output_dir=args.output_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.per_device_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.lr,
        bf16=args.bf16,
        logging_steps=args.logging_steps,
        save_steps=args.save_steps,
        save_total_limit=3,
        seed=args.seed,
        report_to="wandb" if args.wandb_run_name else "none",
        run_name=args.wandb_run_name,
        temperature=args.temperature,
        num_generations=args.num_generations,
        max_completion_length=args.max_completion_length,
        beta=args.kl_coef,
        gradient_checkpointing=True,
    )

    trainer = GRPOTrainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        reward_funcs=reward_funcs,
        processing_class=tokenizer,
    )

    logger.info("Starting GRPO training...")
    trainer.train()
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    logger.info(f"Model saved to {args.output_dir}")


if __name__ == "__main__":
    main()

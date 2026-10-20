"""
GRPO RLVR Recovery Training for pruned models.

Uses trl.GRPOTrainer with GSM8K answer-matching reward to recover
reasoning ability of structurally pruned models.

Input:  pruned model path
Output: recovered model checkpoint + training logs
"""

import argparse
import logging
import os
import random
import re

import numpy as np
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import GRPOConfig, GRPOTrainer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def extract_answer(text: str) -> str | None:
    """Extract numeric answer from model output.
    Tries \\boxed{} first, then last number in text.
    """
    # Try \boxed{...}
    boxed = re.findall(r"\\boxed\{([^}]+)\}", text)
    if boxed:
        return boxed[-1].strip().replace(",", "")

    # Try #### format (GSM8K style)
    hash_match = re.findall(r"####\s*(.+)", text)
    if hash_match:
        return hash_match[-1].strip().replace(",", "")

    # Fall back to last number
    numbers = re.findall(r"-?\d+(?:,\d{3})*(?:\.\d+)?", text)
    if numbers:
        return numbers[-1].replace(",", "")
    return None


def normalize_answer(ans: str) -> str:
    """Normalize a numeric answer string for comparison."""
    ans = ans.strip().replace(",", "").replace(" ", "")
    try:
        val = float(ans)
        if val == int(val):
            return str(int(val))
        return str(val)
    except ValueError:
        return ans


def extract_gold_answer(answer_text: str) -> str:
    """Extract gold answer from GSM8K answer field (after ####)."""
    match = re.search(r"####\s*(.+)", answer_text)
    if match:
        return normalize_answer(match.group(1))
    return answer_text.strip()


def build_reward_fn(tokenizer):
    """Build a reward function for GRPO that checks answer correctness."""

    def reward_fn(completions, **kwargs):
        """Reward function: 1.0 for correct answer, 0.0 for incorrect."""
        prompts = kwargs.get("prompts", None)
        gold_answers = kwargs.get("answer", None)

        rewards = []
        for i, completion in enumerate(completions):
            if isinstance(completion, list):
                # completion is list of message dicts
                text = completion[-1]["content"] if completion else ""
            else:
                text = completion

            pred = extract_answer(text)

            if gold_answers is not None and i < len(gold_answers):
                gold = normalize_answer(str(gold_answers[i]))
            else:
                gold = None

            if pred is not None and gold is not None:
                pred_norm = normalize_answer(pred)
                reward = 1.0 if pred_norm == gold else 0.0
            else:
                reward = 0.0
            rewards.append(reward)

        return rewards

    return reward_fn


def prepare_dataset(tokenizer, max_samples: int = None, seed: int = 42):
    """Prepare GSM8K train dataset for GRPO training."""
    ds = load_dataset("openai/gsm8k", "main", split="train")
    if max_samples is not None:
        ds = ds.shuffle(seed=seed).select(range(min(max_samples, len(ds))))

    def format_prompt(example):
        prompt = (
            f"Solve the following math problem step by step. "
            f"Put your final answer in \\boxed{{}}.\n\n"
            f"Question: {example['question']}\n\nAnswer:"
        )
        example["prompt"] = prompt
        example["answer"] = extract_gold_answer(example["answer"])
        return example

    ds = ds.map(format_prompt)
    return ds


def main():
    parser = argparse.ArgumentParser(description="GRPO RLVR recovery training for pruned models")
    parser.add_argument("--model_path", type=str, required=True, help="Path to pruned model")
    parser.add_argument("--output_path", type=str, required=True, help="Output path for recovered model")
    parser.add_argument("--gpu", type=int, default=0, help="GPU index (for logging only, use CUDA_VISIBLE_DEVICES)")
    parser.add_argument("--learning_rate", type=float, default=1e-6)
    parser.add_argument("--num_train_epochs", type=int, default=3)
    parser.add_argument("--per_device_train_batch_size", type=int, default=2)
    parser.add_argument("--gradient_accumulation_steps", type=int, default=8)
    parser.add_argument("--max_new_tokens", type=int, default=512)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--num_generations", type=int, default=4)
    parser.add_argument("--max_samples", type=int, default=None, help="Limit training samples (None=all)")
    parser.add_argument("--logging_steps", type=int, default=10)
    parser.add_argument("--save_steps", type=int, default=200)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dtype", type=str, default="bfloat16", choices=["float16", "bfloat16", "float32"])
    args = parser.parse_args()

    set_seed(args.seed)

    logger.info(f"Loading pruned model from {args.model_path}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
    torch_dtype = dtype_map[args.dtype]

    model = AutoModelForCausalLM.from_pretrained(
        args.model_path,
        torch_dtype=torch_dtype,
        device_map="auto",
        trust_remote_code=True,
    )

    logger.info("Preparing GSM8K training dataset...")
    dataset = prepare_dataset(tokenizer, max_samples=args.max_samples, seed=args.seed)
    logger.info(f"Training on {len(dataset)} samples")

    reward_fn = build_reward_fn(tokenizer)

    grpo_config = GRPOConfig(
        output_dir=args.output_path,
        learning_rate=args.learning_rate,
        num_train_epochs=args.num_train_epochs,
        per_device_train_batch_size=args.per_device_train_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        max_completion_length=args.max_new_tokens,
        temperature=args.temperature,
        num_generations=args.num_generations,
        logging_steps=args.logging_steps,
        save_steps=args.save_steps,
        seed=args.seed,
        bf16=(args.dtype == "bfloat16"),
        fp16=(args.dtype == "float16"),
        remove_unused_columns=False,
        log_completions=True,
        report_to="none",
    )

    trainer = GRPOTrainer(
        model=model,
        args=grpo_config,
        train_dataset=dataset,
        reward_funcs=reward_fn,
        processing_class=tokenizer,
    )

    logger.info(f"Starting GRPO training (GPU {args.gpu})...")
    trainer.train()

    logger.info(f"Saving recovered model to {args.output_path}")
    trainer.save_model(args.output_path)
    tokenizer.save_pretrained(args.output_path)
    logger.info("GRPO recovery training complete.")


if __name__ == "__main__":
    main()

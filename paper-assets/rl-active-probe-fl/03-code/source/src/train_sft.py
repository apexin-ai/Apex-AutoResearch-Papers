"""SFT training script using TRL SFTTrainer with LoRA.

Input: data/train.jsonl (with good_probe, probe_rationale fields)
Output: LoRA checkpoint in checkpoints/sft/
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
from peft import LoraConfig, TaskType
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import SFTConfig, SFTTrainer

from src.prompts import format_sft_example

logger = logging.getLogger(__name__)


def load_data(path: str) -> Dataset | None:
    samples = []
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            if "good_probe" not in row or "probe_rationale" not in row:
                logger.warning(f"Skipping eval data without good_probe/probe_rationale fields: {path}")
                return None
            samples.append(format_sft_example(row))
    return Dataset.from_list(samples)


def main():
    parser = argparse.ArgumentParser(description="SFT training for probe generation")
    parser.add_argument("--model-name", type=str, default="Qwen/Qwen3-8B")
    parser.add_argument("--train-data", type=str, default="data/train.jsonl")
    parser.add_argument("--eval-data", type=str, default="data/eval.jsonl")
    parser.add_argument("--output-dir", type=str, default="checkpoints/sft")
    parser.add_argument("--lr", type=float, default=2e-5)
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--per-device-batch-size", type=int, default=4)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=4)
    parser.add_argument("--warmup-ratio", type=float, default=0.1)
    parser.add_argument("--max-seq-length", type=int, default=2048)
    parser.add_argument("--bf16", action="store_true", default=True)
    parser.add_argument("--eval-steps", type=int, default=50)
    parser.add_argument("--save-steps", type=int, default=100)
    parser.add_argument("--logging-steps", type=int, default=10)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--wandb-project", type=str, default="rl-active-probe-fl")
    parser.add_argument("--wandb-run-name", type=str, default=None)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)

    if args.wandb_run_name:
        os.environ["WANDB_PROJECT"] = args.wandb_project

    logger.info(f"Loading model: {args.model_name}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Disable Qwen3 thinking mode
    if hasattr(tokenizer, 'chat_template') and tokenizer.chat_template and '<think>' in tokenizer.chat_template:
        tokenizer.chat_template = tokenizer.chat_template.replace(
            'enable_thinking is not defined or enable_thinking is true',
            'enable_thinking is defined and enable_thinking is true'
        )
        logger.info("Patched tokenizer chat_template to disable thinking mode")

    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        torch_dtype=torch.bfloat16 if args.bf16 else torch.float32,
        trust_remote_code=True,
        device_map="auto",
    )

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        lora_dropout=0.05,
    )

    logger.info("Loading training data...")
    train_dataset = load_data(args.train_data)
    eval_dataset = load_data(args.eval_data) if Path(args.eval_data).exists() else None
    logger.info(f"Train: {len(train_dataset)} samples")
    if eval_dataset:
        logger.info(f"Eval: {len(eval_dataset)} samples")

    training_args = SFTConfig(
        output_dir=args.output_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.per_device_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.lr,
        warmup_ratio=args.warmup_ratio,
        max_length=args.max_seq_length,
        bf16=args.bf16,
        logging_steps=args.logging_steps,
        save_steps=args.save_steps,
        eval_strategy="steps" if eval_dataset else "no",
        eval_steps=args.eval_steps if eval_dataset else None,
        save_total_limit=3,
        seed=args.seed,
        report_to="wandb" if args.wandb_run_name else "none",
        run_name=args.wandb_run_name,
        gradient_checkpointing=True,
    )

    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        peft_config=lora_config,
        processing_class=tokenizer,
    )

    logger.info("Starting SFT training...")
    trainer.train()
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    logger.info(f"Model saved to {args.output_dir}")


if __name__ == "__main__":
    main()

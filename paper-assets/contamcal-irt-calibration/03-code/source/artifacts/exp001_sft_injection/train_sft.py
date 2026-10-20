"""
LoRA SFT training for controlled contamination experiments.

Trains Qwen2.5-{0.5B,1.5B,3B} with LoRA on mixed SFT data at different
contamination dosage levels. Saves LoRA adapter then merges to full model.

Input:  JSONL training data from prepare_sft_data.py
Output: LoRA adapter + merged full model checkpoints
"""

import argparse
import json
import logging
import os
from pathlib import Path

import torch
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, TaskType
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
)
from trl import SFTTrainer, SFTConfig

logger = logging.getLogger(__name__)

HF_HOME = os.environ.get("HF_HOME", "/root/autodl-tmp/.hf_cache")
os.environ["HF_HOME"] = HF_HOME

DEFAULT_LORA_CONFIG = {
    "r": 16,
    "lora_alpha": 32,
    "lora_dropout": 0.05,
    "target_modules": [
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj",
    ],
    "task_type": "CAUSAL_LM",
    "bias": "none",
}

DEFAULT_TRAINING_ARGS = {
    "num_train_epochs": 1,
    "per_device_train_batch_size": 4,
    "gradient_accumulation_steps": 4,
    "learning_rate": 2e-4,
    "warmup_ratio": 0.05,
    "bf16": True,
    "logging_steps": 10,
    "save_strategy": "epoch",
    "save_total_limit": 1,
    "report_to": "none",
    "optim": "adamw_torch",
    "lr_scheduler_type": "cosine",
    "max_grad_norm": 1.0,
    "dataloader_num_workers": 4,
    "remove_unused_columns": False,
}


def formatting_func(examples):
    """Format chat messages into a single string for SFT."""
    texts = []
    for messages in examples["messages"]:
        if isinstance(messages, str):
            messages = json.loads(messages)
        parts = []
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            if role == "system":
                parts.append(f"<|im_start|>system\n{content}<|im_end|>")
            elif role == "user":
                parts.append(f"<|im_start|>user\n{content}<|im_end|>")
            elif role == "assistant":
                parts.append(f"<|im_start|>assistant\n{content}<|im_end|>")
        texts.append("\n".join(parts))
    return texts


def main():
    parser = argparse.ArgumentParser(description="LoRA SFT training for contamination experiments")
    parser.add_argument("--model-name", type=str, required=True,
                        help="HuggingFace model name (e.g., Qwen/Qwen2.5-0.5B)")
    parser.add_argument("--data-path", type=str, required=True,
                        help="Path to JSONL training data")
    parser.add_argument("--output-dir", type=str, required=True,
                        help="Output directory for checkpoints")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed")
    parser.add_argument("--gpu", type=str, default=None,
                        help="GPU device IDs (e.g., '0' or '0,1')")
    parser.add_argument("--max-seq-length", type=int, default=2048,
                        help="Maximum sequence length")
    parser.add_argument("--lora-r", type=int, default=DEFAULT_LORA_CONFIG["r"],
                        help="LoRA rank")
    parser.add_argument("--lora-alpha", type=int, default=DEFAULT_LORA_CONFIG["lora_alpha"],
                        help="LoRA alpha")
    parser.add_argument("--epochs", type=int, default=1, help="Number of training epochs")
    parser.add_argument("--batch-size", type=int, default=4, help="Per-device batch size")
    parser.add_argument("--grad-accum", type=int, default=4, help="Gradient accumulation steps")
    parser.add_argument("--lr", type=float, default=2e-4, help="Learning rate")
    parser.add_argument("--merge", action="store_true",
                        help="Merge LoRA into full model (default: adapter-only to save disk)")
    parser.add_argument("--cache-dir", type=str, default="/root/autodl-tmp/.hf_cache",
                        help="HuggingFace cache directory")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Loading tokenizer: %s", args.model_name)
    tokenizer = AutoTokenizer.from_pretrained(
        args.model_name, cache_dir=args.cache_dir, trust_remote_code=True
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    logger.info("Loading model: %s", args.model_name)
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        cache_dir=args.cache_dir,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        attn_implementation="flash_attention_2" if torch.cuda.is_available() else "eager",
    )

    # LoRA config
    lora_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=DEFAULT_LORA_CONFIG["lora_dropout"],
        target_modules=DEFAULT_LORA_CONFIG["target_modules"],
        task_type=TaskType.CAUSAL_LM,
        bias="none",
    )

    logger.info("LoRA config: r=%d, alpha=%d, targets=%s",
                lora_config.r, lora_config.lora_alpha, lora_config.target_modules)

    # Load dataset
    logger.info("Loading training data: %s", args.data_path)
    dataset = load_dataset("json", data_files=args.data_path, split="train")
    logger.info("Training samples: %d", len(dataset))

    # Training arguments
    training_args = SFTConfig(
        output_dir=str(output_dir / "lora_adapter"),
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=args.grad_accum,
        learning_rate=args.lr,
        warmup_ratio=DEFAULT_TRAINING_ARGS["warmup_ratio"],
        bf16=DEFAULT_TRAINING_ARGS["bf16"],
        logging_steps=DEFAULT_TRAINING_ARGS["logging_steps"],
        save_strategy=DEFAULT_TRAINING_ARGS["save_strategy"],
        save_total_limit=DEFAULT_TRAINING_ARGS["save_total_limit"],
        report_to=DEFAULT_TRAINING_ARGS["report_to"],
        optim=DEFAULT_TRAINING_ARGS["optim"],
        lr_scheduler_type=DEFAULT_TRAINING_ARGS["lr_scheduler_type"],
        max_grad_norm=DEFAULT_TRAINING_ARGS["max_grad_norm"],
        dataloader_num_workers=DEFAULT_TRAINING_ARGS["dataloader_num_workers"],
        seed=args.seed,
        max_seq_length=args.max_seq_length,
        dataset_text_field=None,
    )

    # Trainer
    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        processing_class=tokenizer,
        peft_config=lora_config,
        formatting_func=formatting_func,
    )

    logger.info("Starting training...")
    trainer.train()

    # Save LoRA adapter
    adapter_dir = output_dir / "lora_adapter"
    trainer.save_model(str(adapter_dir))
    tokenizer.save_pretrained(str(adapter_dir))
    logger.info("LoRA adapter saved to %s", adapter_dir)

    # Optionally merge and save full model (off by default to save disk)
    if args.merge:
        logger.info("Merging LoRA adapter into base model...")
        merged_model = trainer.model.merge_and_unload()
        merged_dir = output_dir / "merged"
        merged_model.save_pretrained(str(merged_dir))
        tokenizer.save_pretrained(str(merged_dir))
        logger.info("Merged model saved to %s", merged_dir)

    # Save training config
    config = {
        "model_name": args.model_name,
        "data_path": args.data_path,
        "lora_r": args.lora_r,
        "lora_alpha": args.lora_alpha,
        "epochs": args.epochs,
        "batch_size": args.batch_size,
        "grad_accum": args.grad_accum,
        "lr": args.lr,
        "max_seq_length": args.max_seq_length,
        "seed": args.seed,
        "num_samples": len(dataset),
    }
    with open(output_dir / "train_config.json", "w") as f:
        json.dump(config, f, indent=2)

    logger.info("Training complete.")


if __name__ == "__main__":
    main()

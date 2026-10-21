"""
LoRA SFT training for controlled contamination experiments.

Trains Qwen2.5-{0.5B,1.5B,3B} or Llama-3.2-3B with LoRA on mixed SFT data at different
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
    BitsAndBytesConfig,
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


LLAMA3_CHAT_TEMPLATE = (
    "{% set loop_messages = messages %}"
    "{% for message in loop_messages %}"
    "{% set content = '<|start_header_id|>' + message['role'] + '<|end_header_id|>\n\n' + message['content'] | trim + '<|eot_id|>' %}"
    "{% if loop.first %}{% set content = bos_token + content %}{% endif %}"
    "{{ content }}"
    "{% endfor %}"
    "{% if add_generation_prompt %}{{ '<|start_header_id|>assistant<|end_header_id|>\n\n' }}{% endif %}"
)
CHATML_TEMPLATE = (
    "{% for message in messages %}"
    "{{'<|im_start|>' + message['role'] + '\n' + message['content'] + '<|im_end|>' + '\n'}}"
    "{% endfor %}"
    "{% if add_generation_prompt %}{{'<|im_start|>assistant\n'}}{% endif %}"
)

def make_formatting_func(tokenizer):
    """Create formatting function using the tokenizer's chat template (model-agnostic)."""
    def formatting_func(example):
        messages = example["messages"]
        if isinstance(messages, str):
            messages = json.loads(messages)
        parsed = []
        for msg in messages:
            if isinstance(msg, str):
                msg = json.loads(msg)
            parsed.append(msg)
        return tokenizer.apply_chat_template(
            parsed, tokenize=False, add_generation_prompt=False
        )
    return formatting_func


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
    parser.add_argument("--gpu", type=int, default=0,
                        help="GPU device index (CUDA_VISIBLE_DEVICES set externally)")
    parser.add_argument("--gradient-checkpointing", action="store_true",
                        help="Enable gradient checkpointing (saves VRAM, required for 7B)")
    parser.add_argument("--load-in-4bit", action="store_true",
                        help="Load model in 4-bit quantization (QLoRA)")
    parser.add_argument("--bnb-4bit-quant-type", type=str, default="nf4",
                        choices=["nf4", "fp4"], help="4-bit quantization type")
    parser.add_argument("--bnb-4bit-compute-dtype", type=str, default="bfloat16",
                        choices=["bfloat16", "float16"], help="Compute dtype for 4-bit")
    parser.add_argument("--lora-targets", type=str, default=None,
                        help="Comma-separated LoRA target modules (overrides defaults)")
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

    # Set chat template for models that don't have one (e.g. Llama-3.2 base)
    if tokenizer.chat_template is None:
        if "llama" in args.model_name.lower():
            tokenizer.chat_template = LLAMA3_CHAT_TEMPLATE
            logger.info("Set Llama 3 chat template on tokenizer")
        else:
            tokenizer.chat_template = CHATML_TEMPLATE
            logger.info("Set ChatML chat template on tokenizer (model: %s)", args.model_name)

    logger.info("Loading model: %s", args.model_name)
    model_kwargs = dict(
        cache_dir=args.cache_dir,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        attn_implementation="sdpa" if torch.cuda.is_available() else "eager",
    )
    if args.load_in_4bit:
        compute_dtype = torch.bfloat16 if args.bnb_4bit_compute_dtype == "bfloat16" else torch.float16
        model_kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type=args.bnb_4bit_quant_type,
            bnb_4bit_compute_dtype=compute_dtype,
            bnb_4bit_use_double_quant=True,
        )
        logger.info("QLoRA mode: 4-bit %s, compute dtype %s", args.bnb_4bit_quant_type, args.bnb_4bit_compute_dtype)
    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)

    # LoRA config
    target_modules = args.lora_targets.split(",") if args.lora_targets else DEFAULT_LORA_CONFIG["target_modules"]
    lora_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=DEFAULT_LORA_CONFIG["lora_dropout"],
        target_modules=target_modules,
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
        max_length=args.max_seq_length,
        dataset_text_field=None,
        gradient_checkpointing=args.gradient_checkpointing,
        gradient_checkpointing_kwargs={"use_reentrant": False} if args.gradient_checkpointing else None,
    )

    # Trainer
    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        processing_class=tokenizer,
        peft_config=lora_config,
        formatting_func=make_formatting_func(tokenizer),
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
        "gradient_checkpointing": args.gradient_checkpointing,
        "load_in_4bit": args.load_in_4bit,
        "lora_targets": list(lora_config.target_modules),
    }
    with open(output_dir / "train_config.json", "w") as f:
        json.dump(config, f, indent=2)

    logger.info("Training complete.")


if __name__ == "__main__":
    main()

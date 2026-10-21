#!/usr/bin/env python3
"""SFT training for ALFWorld RAGEN format on Qwen3-8B (multi-GPU via torchrun)."""

import argparse
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import SFTTrainer, SFTConfig
from datasets import load_dataset

MODEL_PATH = "/root/autodl-tmp/models/Qwen3-8B"
DEFAULT_DATA_PATH = "/root/autodl-tmp/expert_sft/expert_sft_train.jsonl"
DEFAULT_OUTPUT_DIR = "/root/autodl-tmp/checkpoints/qwen3_8b_sft_v1"

SIMPLE_CHATML = (
    "{% for message in messages %}"
    "{{'<|im_start|>' + message['role'] + '\\n' + message['content'] + '<|im_end|>' + '\\n'}}"
    "{% endfor %}"
    "{% if add_generation_prompt %}"
    "{{'<|im_start|>assistant\\n'}}"
    "{% endif %}"
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max_steps", type=int, default=-1)
    parser.add_argument("--num_train_epochs", type=int, default=3)
    parser.add_argument("--per_device_train_batch_size", type=int, default=2)
    parser.add_argument("--gradient_accumulation_steps", type=int, default=4)
    parser.add_argument("--learning_rate", type=float, default=1e-5)
    parser.add_argument("--max_seq_length", type=int, default=4096)
    parser.add_argument("--data_path", type=str, default=DEFAULT_DATA_PATH)
    parser.add_argument("--output_dir", type=str, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    tokenizer.chat_template = SIMPLE_CHATML
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("Loading model...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.bfloat16,
        attn_implementation="sdpa",
    )

    print("Loading dataset...")
    dataset = load_dataset("json", data_files=args.data_path, split="train")
    print(f"Dataset size: {len(dataset)}")

    sample = dataset[0]["messages"]
    encoded = tokenizer.apply_chat_template(sample, tokenize=True)
    print(f"Sample token length: {len(encoded)}")

    training_args = SFTConfig(
        output_dir=args.output_dir,
        num_train_epochs=args.num_train_epochs,
        max_steps=args.max_steps,
        per_device_train_batch_size=args.per_device_train_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.learning_rate,
        bf16=True,
        max_length=args.max_seq_length,
        warmup_ratio=0.03,
        weight_decay=0.01,
        logging_steps=10,
        save_strategy="steps",
        save_steps=500,
        save_total_limit=3,
        report_to="none",
        gradient_checkpointing=True,
        dataloader_num_workers=2,
        seed=42,
        ddp_find_unused_parameters=False,
    )

    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        processing_class=tokenizer,
    )

    print("Starting training...")
    result = trainer.train()
    print(f"\nTraining complete. Metrics: {result.metrics}")

    trainer.save_model(args.output_dir + "/final")
    tokenizer.save_pretrained(args.output_dir + "/final")
    print(f"Model saved to {args.output_dir}/final")


if __name__ == "__main__":
    main()

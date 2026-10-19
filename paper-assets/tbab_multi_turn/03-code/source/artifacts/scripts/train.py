"""
Main training script for TBAB multi-turn experiments.

Usage:
    python train.py --config configs/condition4_full_tbab.yaml --seed 42 \
        --output_dir /root/tbab_multi_turn/checkpoints/c4_seed42

Supports 4 conditions via YAML config:
    1. LoRA-only (standard multi-turn SFT)
    2. Position-reset-only (per-turn position reset)
    3. Bridge+standard-pos (bridge tokens, no reset)
    4. Full TBAB (bridge tokens + position reset)

Dependencies: transformers, peft, torch, wandb, pyyaml
"""

import argparse
import os
import sys
import yaml
import torch
import wandb
from transformers import TrainingArguments, Trainer

from tbab_model import setup_model_and_tokenizer
from tbab_dataset import TBABDataset, TBABDataCollator


def load_config(config_path: str) -> dict:
    with open(config_path) as f:
        return yaml.safe_load(f)


def print_sample_debug(dataset, tokenizer, idx=0):
    """Print a single sample for debugging: input_ids, position_ids, labels."""
    sample = dataset[idx]
    seq_len = sample["seq_len"]
    print(f"\n{'='*60}")
    print(f"Sample {idx} | seq_len={seq_len}")
    print(f"{'='*60}")

    ids = sample["input_ids"][:50]
    tokens = tokenizer.convert_ids_to_tokens(ids)
    print(f"First 50 tokens: {tokens}")
    print(f"First 50 input_ids: {ids}")
    print(f"First 50 position_ids: {sample['position_ids'][:50]}")
    print(f"First 50 labels: {sample['labels'][:50]}")

    num_loss_tokens = sum(1 for l in sample["labels"] if l != -100)
    print(f"Loss tokens: {num_loss_tokens}/{seq_len} ({num_loss_tokens/seq_len*100:.1f}%)")
    print(f"needs_4d_mask: {sample['needs_4d_mask']}")
    print(f"{'='*60}\n")


def verify_bridge_gradients(model, bridge_token_ids):
    """Check that bridge token embeddings have non-zero gradients after a step."""
    base_model = model.get_base_model()
    embed_weight = base_model.get_input_embeddings().weight
    if embed_weight.grad is not None:
        for tid in bridge_token_ids:
            grad_norm = embed_weight.grad[tid].norm().item()
            print(f"  Bridge token {tid} embed grad norm: {grad_norm:.6f}")
    else:
        print("  WARNING: Embedding gradients are None (check after optimizer.step)")


class TBABTrainer(Trainer):
    """Custom trainer that handles 4D attention mask dtype casting."""

    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
        if "attention_mask" in inputs and inputs["attention_mask"].dim() == 4:
            inputs["attention_mask"] = inputs["attention_mask"].to(
                device=model.device, dtype=torch.bfloat16
            )
        return super().compute_loss(model, inputs, return_outputs=return_outputs, **kwargs)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output_dir", type=str, default=None)
    parser.add_argument("--max_steps", type=int, default=-1, help="Override for quick validation")
    args = parser.parse_args()

    config = load_config(args.config)
    config["seed"] = args.seed
    if args.output_dir:
        config["output_dir"] = args.output_dir

    condition_name = config["condition_name"]
    print(f"Condition: {condition_name}")
    print(f"use_bridge_tokens: {config.get('use_bridge_tokens', False)}")
    print(f"use_position_reset: {config.get('use_position_reset', False)}")
    print(f"seed: {args.seed}")

    os.environ["WANDB_PROJECT"] = "tbab_multi_turn"
    wandb.init(
        project="tbab_multi_turn",
        name=f"{condition_name}_seed{args.seed}",
        config=config,
    )

    model, tokenizer, bridge_token_ids = setup_model_and_tokenizer(config)
    print(f"Model loaded. Bridge token IDs: {bridge_token_ids}")
    model.print_trainable_parameters()

    data_path = config.get("data_path", "/root/tbab_multi_turn/data/training_data.json")
    dataset = TBABDataset(
        data_path=data_path,
        tokenizer=tokenizer,
        max_seq_length=config.get("max_seq_length", 4096),
        use_bridge_tokens=config.get("use_bridge_tokens", False),
        use_position_reset=config.get("use_position_reset", False),
        bridge_token_ids=bridge_token_ids,
        num_bridge_tokens=config.get("num_bridge_tokens", 4),
    )
    print(f"Dataset size: {len(dataset)}")

    print_sample_debug(dataset, tokenizer, idx=0)
    if len(dataset) > 1:
        print_sample_debug(dataset, tokenizer, idx=1)

    collator = TBABDataCollator(
        tokenizer=tokenizer,
        use_position_reset=config.get("use_position_reset", False),
    )

    output_dir = config.get("output_dir", f"/root/tbab_multi_turn/checkpoints/{condition_name}_seed{args.seed}")

    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=config.get("num_epochs", 3),
        per_device_train_batch_size=config.get("per_device_train_batch_size", 2),
        gradient_accumulation_steps=config.get("gradient_accumulation_steps", 8),
        learning_rate=config.get("learning_rate", 2e-4),
        lr_scheduler_type="cosine",
        warmup_ratio=config.get("warmup_ratio", 0.03),
        bf16=True,
        logging_steps=config.get("logging_steps", 10),
        save_strategy="epoch",
        seed=args.seed,
        report_to="wandb",
        remove_unused_columns=False,
        dataloader_pin_memory=True,
        gradient_checkpointing=config.get("gradient_checkpointing", True),
        max_steps=args.max_steps if args.max_steps > 0 else -1,
    )

    trainer = TBABTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        data_collator=collator,
    )

    print("Starting training...")
    trainer.train()

    if bridge_token_ids:
        verify_bridge_gradients(model, bridge_token_ids)

    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)
    print(f"Model saved to {output_dir}")

    wandb.finish()
    print("Done.")


if __name__ == "__main__":
    main()

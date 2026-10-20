"""DPO fine-tuning of Qwen 2.5 7B with QLoRA for dialect calibration."""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from pathlib import Path

import torch
from datasets import Dataset
from peft import LoraConfig, TaskType, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
)
from trl import DPOConfig, DPOTrainer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("train_dpo")


def load_dpo_dataset(data_path: str) -> Dataset:
    records = []
    with open(data_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            records.append({
                "prompt": rec["prompt"],
                "chosen": rec["chosen"],
                "rejected": rec["rejected"],
            })
    log.info("Loaded %d DPO pairs from %s", len(records), data_path)
    if not records:
        raise ValueError(f"No DPO pairs found in {data_path}")
    return Dataset.from_list(records)


def load_model_and_tokenizer(model_path: str, gpu_id: int):
    log.info("Loading tokenizer from %s", model_path)
    tokenizer = AutoTokenizer.from_pretrained(
        model_path,
        trust_remote_code=True,
        padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )

    log.info("Loading model (4-bit) from %s", model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        trust_remote_code=True,
        quantization_config=bnb_config,
        device_map={"": 0},
        attn_implementation="sdpa",
    )
    model.config.use_cache = False
    model = prepare_model_for_kbit_training(model)

    return model, tokenizer


def setup_lora(model, lora_rank: int, lora_alpha: int):
    lora_config = LoraConfig(
        r=lora_rank,
        lora_alpha=lora_alpha,
        target_modules=["q_proj", "v_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type=TaskType.CAUSAL_LM,
    )
    model = get_peft_model(model, lora_config)
    trainable, total = model.get_nb_trainable_parameters()
    log.info(
        "LoRA: rank=%d, alpha=%d, trainable=%d (%.2f%% of %d)",
        lora_rank, lora_alpha, trainable, 100.0 * trainable / total, total,
    )
    return model


def train(args: argparse.Namespace):
    dataset = load_dpo_dataset(args.data_path)
    model, tokenizer = load_model_and_tokenizer(args.model_path, args.gpu_id)
    model = setup_lora(model, args.lora_rank, args.lora_alpha)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    wandb_kwargs = {}
    if args.wandb_project:
        os.environ["WANDB_PROJECT"] = args.wandb_project
        wandb_kwargs["report_to"] = "wandb"
        if args.wandb_run_name:
            wandb_kwargs["run_name"] = args.wandb_run_name
    else:
        wandb_kwargs["report_to"] = "none"

    training_args = DPOConfig(
        output_dir=str(output_dir),
        num_train_epochs=args.num_epochs,
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=4,
        learning_rate=args.learning_rate,
        lr_scheduler_type="cosine",
        warmup_ratio=0.1,
        bf16=True,
        gradient_checkpointing=True,
        logging_steps=1,
        save_strategy="epoch",
        save_total_limit=2,
        remove_unused_columns=False,
        beta=0.1,
        loss_type="sigmoid",
        max_length=2048,
        seed=42,
        dataloader_num_workers=2,
        **wandb_kwargs,
    )

    trainer = DPOTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        processing_class=tokenizer,
    )

    log.info("Starting DPO training: %d examples, %d epochs", len(dataset), args.num_epochs)
    train_result = trainer.train()

    adapter_dir = output_dir / "final_adapter"
    trainer.save_model(str(adapter_dir))
    tokenizer.save_pretrained(str(adapter_dir))
    log.info("LoRA adapter saved to %s", adapter_dir)

    metrics = train_result.metrics
    trainer.log_metrics("train", metrics)
    trainer.save_metrics("train", metrics)
    trainer.save_state()

    log.info("Training complete.")
    log.info("  train_loss: %.4f", metrics.get("train_loss", float("nan")))
    log.info("  train_runtime: %.1fs", metrics.get("train_runtime", 0))
    log.info("  train_samples_per_second: %.2f", metrics.get("train_samples_per_second", 0))

    return metrics


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="DPO fine-tune Qwen 2.5 7B with LoRA for dialect calibration"
    )
    p.add_argument("--model-path", required=True)
    p.add_argument("--data-path", required=True)
    p.add_argument("--output-dir", default="/root/democalib/checkpoints/dpo")
    p.add_argument("--lora-rank", type=int, default=16)
    p.add_argument("--lora-alpha", type=int, default=32)
    p.add_argument("--learning-rate", type=float, default=5e-7)
    p.add_argument("--num-epochs", type=int, default=3)
    p.add_argument("--batch-size", type=int, default=4)
    p.add_argument("--gpu-id", type=int, default=0)
    p.add_argument("--wandb-project", default="democalib")
    p.add_argument("--wandb-run-name", default=None)
    return p.parse_args()


if __name__ == "__main__":
    train(parse_args())

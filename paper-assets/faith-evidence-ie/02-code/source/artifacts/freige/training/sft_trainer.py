"""SFT 训练脚本: Qwen3-4B + QLoRA 在 DocRED 上微调。

支持单卡和多卡（DeepSpeed ZeRO-2/3）训练。
默认启用 4-bit QLoRA 量化，适配 RTX 5090 32GB x4。

单卡:   python -m freige.training.sft_trainer --output_dir ./sft_output
多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \
            -m freige.training.sft_trainer --deepspeed configs/deepspeed_zero2.json
不量化: 加 --no_quantize
"""

import argparse
import json
import logging
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import torch
from datasets import Dataset
from peft import LoraConfig, TaskType, get_peft_model
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
)
from trl import SFTTrainer, SFTConfig

from freige.training import LLAMA3_CHAT_TEMPLATE

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are an information extraction model. Given a document with numbered sentences "
    "and a list of entities, extract all relation triples. For each triple, provide the "
    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
    "Output as a JSON list."
)

DEFAULT_MODEL = "/root/autodl-tmp/models/Qwen3-4B"


def build_chat_messages(instruction: str, input_text: str, output_text: str = None):
    """构建 Qwen3 chat 格式的消息列表。"""
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"{instruction}\n\n{input_text}"},
    ]
    if output_text is not None:
        messages.append({"role": "assistant", "content": output_text})
    return messages


def prepare_dataset(
    data_dir: str = None,
    split: str = "train",
    tokenizer=None,
    max_length: int = 4096,
) -> Dataset:
    """加载并格式化 DocRED 数据为 SFT 训练格式。"""
    from freige.data.docred_processor import DocREDProcessor

    processor = DocREDProcessor(data_dir=data_dir)
    samples = processor.process(split)
    groups = processor.group_by_document(samples)

    formatted = []
    for doc_id, doc_samples in groups.items():
        sft_sample = processor.format_sft_sample(doc_samples)
        messages = build_chat_messages(
            sft_sample["instruction"],
            sft_sample["input"],
            sft_sample["output"],
        )
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=False,
            enable_thinking=False,
        )
        formatted.append({"text": text})

    logger.info("Prepared %d SFT samples from %d documents", len(formatted), len(groups))
    return Dataset.from_list(formatted)


def main():
    parser = argparse.ArgumentParser(description="FREIGE SFT Training")
    parser.add_argument("--model_name", type=str, default=DEFAULT_MODEL)
    parser.add_argument("--data_dir", type=str, default=None,
                        help="DocRED JSON 目录")
    parser.add_argument("--output_dir", type=str, default="./sft_output")
    parser.add_argument("--lora_rank", type=int, default=64)
    parser.add_argument("--lora_alpha", type=int, default=128)
    parser.add_argument("--lora_dropout", type=float, default=0.05)
    parser.add_argument("--max_length", type=int, default=4096)
    parser.add_argument("--quantize", action=argparse.BooleanOptionalAction, default=True,
                        help="启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）")
    parser.add_argument("--deepspeed", type=str, default=None,
                        help="DeepSpeed 配置文件路径")
    parser.add_argument("--per_device_batch_size", type=int, default=1)
    parser.add_argument("--gradient_accumulation_steps", type=int, default=16)
    parser.add_argument("--num_epochs", type=int, default=3)
    parser.add_argument("--learning_rate", type=float, default=2e-4)
    parser.add_argument("--warmup_ratio", type=float, default=0.05)
    parser.add_argument("--bf16", action="store_true", default=True)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--wandb_project", type=str, default="freige-sft")
    parser.add_argument("--wandb_run_name", type=str, default=None)
    args = parser.parse_args()

    if args.wandb_project and "WANDB_API_KEY" in os.environ:
        os.environ["WANDB_PROJECT"] = args.wandb_project
        if args.wandb_run_name:
            os.environ["WANDB_NAME"] = args.wandb_run_name

    logger.info("Loading tokenizer: %s", args.model_name)
    tokenizer = AutoTokenizer.from_pretrained(
        args.model_name,
        trust_remote_code=True,
        padding_side="right",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    if not getattr(tokenizer, 'chat_template', None):
        tokenizer.chat_template = LLAMA3_CHAT_TEMPLATE

    logger.info("Preparing dataset...")
    train_dataset = prepare_dataset(
        data_dir=args.data_dir,
        split="train",
        tokenizer=tokenizer,
        max_length=args.max_length,
    )
    eval_dataset = prepare_dataset(
        data_dir=args.data_dir,
        split="dev",
        tokenizer=tokenizer,
        max_length=args.max_length,
    )

    logger.info("Loading model: %s", args.model_name)
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    model_kwargs = dict(
        trust_remote_code=True,
        attn_implementation="sdpa",
        device_map={"": local_rank},
    )
    if args.quantize:
        logger.info("Using 4-bit QLoRA quantization")
        model_kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
        )
    else:
        model_kwargs["torch_dtype"] = torch.bfloat16 if args.bf16 else torch.float16
    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)
    model.config.use_cache = False
    model.gradient_checkpointing_enable()

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=args.lora_rank,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                         "gate_proj", "up_proj", "down_proj"],
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    training_args = SFTConfig(
        output_dir=args.output_dir,
        num_train_epochs=args.num_epochs,
        per_device_train_batch_size=args.per_device_batch_size,
        per_device_eval_batch_size=args.per_device_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.learning_rate,
        warmup_ratio=args.warmup_ratio,
        bf16=args.bf16,
        logging_steps=10,
        eval_strategy="epoch",
        save_strategy="epoch",
        save_total_limit=2,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        seed=args.seed,
        max_length=args.max_length,
        dataset_text_field="text",
        report_to="wandb" if "WANDB_API_KEY" in os.environ else "none",
        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},
        deepspeed=args.deepspeed,
    )

    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        processing_class=tokenizer,
    )

    logger.info("Starting SFT training...")
    trainer.train()

    logger.info("Saving model to %s", args.output_dir)
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    logger.info("SFT training complete.")


if __name__ == "__main__":
    main()

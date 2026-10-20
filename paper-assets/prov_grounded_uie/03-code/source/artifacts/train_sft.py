"""SFT training for ProvUIE.

Trains Qwen3-8B with LoRA on DocRED relation extraction + evidence co-prediction.
Uses TRL SFTTrainer with chat-format data.

Input:  JSONL with 'messages' column (system + user + assistant).
Output: Merged model checkpoint at {output_dir}/merged/.

Usage:
    python train_sft.py --help
    python train_sft.py --output_dir ./outputs/sft --num_train_epochs 3
"""

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
)
from trl import SFTConfig, SFTTrainer
from peft import LoraConfig, TaskType

from config import ModelArgs, SFTArgs, DataArgs
from data_utils import load_sft_dataset


def main():
    parser = HfArgumentParser((ModelArgs, SFTArgs, DataArgs))
    model_args, sft_args, data_args = parser.parse_args_into_dataclasses()

    # ── Tokenizer ──────────────────────────────────────────────────────
    tokenizer = AutoTokenizer.from_pretrained(
        model_args.model_name_or_path,
        trust_remote_code=True,
        padding_side="right",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # ── Model loading kwargs ───────────────────────────────────────────
    model_kwargs: dict = {"trust_remote_code": True}

    if model_args.use_flash_attention:
        model_kwargs["attn_implementation"] = "flash_attention_2"

    if model_args.load_in_4bit:
        model_kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_quant_type="nf4",
        )
    else:
        model_kwargs["torch_dtype"] = torch.bfloat16

    model = AutoModelForCausalLM.from_pretrained(
        model_args.model_name_or_path, **model_kwargs
    )

    # ── LoRA ───────────────────────────────────────────────────────────
    peft_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=model_args.lora_rank,
        lora_alpha=model_args.lora_alpha,
        lora_dropout=model_args.lora_dropout,
        target_modules=model_args.get_target_modules(),
    )

    # ── TRL SFT config ─────────────────────────────────────────────────
    training_config = SFTConfig(
        output_dir=sft_args.output_dir,
        learning_rate=sft_args.learning_rate,
        num_train_epochs=sft_args.num_train_epochs,
        per_device_train_batch_size=sft_args.per_device_train_batch_size,
        gradient_accumulation_steps=sft_args.gradient_accumulation_steps,
        max_length=sft_args.max_seq_length,
        logging_steps=sft_args.logging_steps,
        save_steps=sft_args.save_steps,
        save_total_limit=sft_args.save_total_limit,
        bf16=sft_args.bf16,
        warmup_ratio=sft_args.warmup_ratio,
        lr_scheduler_type=sft_args.lr_scheduler_type,
        report_to=sft_args.report_to,
        run_name=sft_args.run_name,
        eval_strategy=sft_args.eval_strategy,
        eval_steps=sft_args.eval_steps,
        gradient_checkpointing=sft_args.gradient_checkpointing,
        gradient_checkpointing_kwargs={"use_reentrant": False},
        dataset_kwargs={},
    )

    # ── Datasets ───────────────────────────────────────────────────────
    train_ds = load_sft_dataset(data_args.train_file, max_samples=data_args.max_train_samples)
    eval_ds = load_sft_dataset(data_args.dev_file, max_samples=data_args.max_eval_samples)
    print(f"Train: {len(train_ds)}, Eval: {len(eval_ds)}")

    # ── Trainer ────────────────────────────────────────────────────────
    trainer = SFTTrainer(
        model=model,
        args=training_config,
        train_dataset=train_ds,
        eval_dataset=eval_ds,
        processing_class=tokenizer,
        peft_config=peft_config,
    )

    trainer.train()

    # ── Save adapter ───────────────────────────────────────────────────
    adapter_dir = f"{sft_args.output_dir}/adapter"
    trainer.save_model(adapter_dir)
    tokenizer.save_pretrained(adapter_dir)
    print(f"Adapter saved to {adapter_dir}")

    # ── Merge LoRA → full model (for GRPO consumption) ─────────────────
    merged_dir = f"{sft_args.output_dir}/merged"
    merged_model = trainer.model.merge_and_unload()
    merged_model.save_pretrained(merged_dir)
    tokenizer.save_pretrained(merged_dir)
    print(f"Merged model saved to {merged_dir}")


if __name__ == "__main__":
    main()

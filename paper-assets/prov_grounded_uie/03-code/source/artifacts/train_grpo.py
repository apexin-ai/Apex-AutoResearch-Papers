"""GRPO training for ProvUIE.

Continues from a merged SFT checkpoint with Group Relative Policy Optimization.
Reward = weighted(provenance_fidelity, structural_f1, format_compliance).

Input:  Merged SFT model + JSONL with prompt + gold metadata.
Output: GRPO-tuned model checkpoint.

Usage:
    python train_grpo.py --help
    python train_grpo.py --sft_checkpoint ./outputs/sft/merged
"""

import torch
from transformers import AutoTokenizer, HfArgumentParser
from trl import GRPOConfig, GRPOTrainer
from peft import LoraConfig, TaskType

from config import ModelArgs, GRPOArgs, DataArgs, RewardArgs
from data_utils import load_grpo_dataset
from rewards import composite_reward


def main():
    parser = HfArgumentParser((ModelArgs, GRPOArgs, DataArgs, RewardArgs))
    model_args, grpo_args, data_args, reward_args = parser.parse_args_into_dataclasses()

    # ── Tokenizer ──────────────────────────────────────────────────────
    # Left-padding for generation in GRPO
    tokenizer = AutoTokenizer.from_pretrained(
        grpo_args.sft_checkpoint,
        trust_remote_code=True,
        padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # ── Model kwargs (passed to HF model via GRPOConfig.model_init_kwargs) ──
    # In colocate mode, GRPOTrainer loads the HF model internally — we pass
    # the checkpoint path as a string, not a pre-loaded model object.
    model_kwargs: dict = {"trust_remote_code": True, "torch_dtype": torch.bfloat16}
    if model_args.use_flash_attention:
        model_kwargs["attn_implementation"] = "flash_attention_2"

    # ── Fresh LoRA adapter for GRPO ────────────────────────────────────
    peft_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=model_args.lora_rank,
        lora_alpha=model_args.lora_alpha,
        lora_dropout=model_args.lora_dropout,
        target_modules=model_args.get_target_modules(),
    )

    # ── TRL GRPO config ────────────────────────────────────────────────
    training_config = GRPOConfig(
        output_dir=grpo_args.output_dir,
        num_generations=grpo_args.num_generations,
        temperature=grpo_args.temperature,
        top_k=grpo_args.top_k,
        top_p=grpo_args.top_p,
        beta=grpo_args.beta,
        learning_rate=grpo_args.learning_rate,
        num_train_epochs=grpo_args.num_train_epochs,
        max_steps=grpo_args.max_steps,
        per_device_train_batch_size=grpo_args.per_device_train_batch_size,
        gradient_accumulation_steps=grpo_args.gradient_accumulation_steps,
        max_completion_length=grpo_args.max_completion_length,
        logging_steps=grpo_args.logging_steps,
        save_steps=grpo_args.save_steps,
        save_total_limit=grpo_args.save_total_limit,
        bf16=grpo_args.bf16,
        report_to=grpo_args.report_to,
        run_name=grpo_args.run_name,
        gradient_checkpointing=grpo_args.gradient_checkpointing,
        gradient_checkpointing_kwargs={"use_reentrant": False},
        model_init_kwargs=model_kwargs,
        chat_template_kwargs={"enable_thinking": False},
    )

    # ── Dataset ────────────────────────────────────────────────────────
    train_ds = load_grpo_dataset(data_args.train_file, max_samples=data_args.max_train_samples)
    print(f"GRPO train samples: {len(train_ds)}")

    # ── Reward function (capture configured weights) ───────────────────
    def reward_fn(prompts, completions, **kwargs):
        kwargs.update({
            "w_provenance": reward_args.w_provenance,
            "w_structural": reward_args.w_structural,
            "w_format": reward_args.w_format,
            "nli_batch_size": reward_args.nli_batch_size,
            "nli_model_name": reward_args.nli_model_name,
            "nli_device": reward_args.nli_device,
            "length_penalty_factor": reward_args.length_penalty_factor,
            "iou_weight": reward_args.iou_weight,
            "nli_weight": reward_args.nli_weight,
            "length_weight": reward_args.length_weight,
        })
        return composite_reward(prompts, completions, **kwargs)

    # ── Trainer ────────────────────────────────────────────────────────
    trainer = GRPOTrainer(
        model=grpo_args.sft_checkpoint,
        reward_funcs=[reward_fn],
        args=training_config,
        train_dataset=train_ds,
        processing_class=tokenizer,
        peft_config=peft_config,
    )

    trainer.train()

    # ── Save ───────────────────────────────────────────────────────────
    final_dir = f"{grpo_args.output_dir}/final"
    trainer.save_model(final_dir)
    tokenizer.save_pretrained(final_dir)
    print(f"GRPO model saved to {final_dir}")


if __name__ == "__main__":
    main()

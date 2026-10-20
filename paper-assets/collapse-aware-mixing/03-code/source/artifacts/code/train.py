"""Training loop for one generation using HuggingFace Trainer."""

import os
import logging
from typing import List

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
    TrainerCallback,
)

logger = logging.getLogger(__name__)


class CheckpointListCallback(TrainerCallback):
    """Records paths of saved checkpoints for downstream evaluation."""

    def __init__(self):
        self.saved_checkpoints: List[str] = []

    def on_save(self, args, state, control, **kwargs):
        ckpt_dir = os.path.join(args.output_dir, f"checkpoint-{state.global_step}")
        self.saved_checkpoints.append(ckpt_dir)
        logger.info("Checkpoint saved: %s (step %d)", ckpt_dir, state.global_step)


class EarlyStopOnHighLossCallback(TrainerCallback):
    """Stop training if loss exceeds threshold in first N steps."""

    def __init__(self, threshold: float = 15.0, check_steps: int = 100, check_interval: int = 10):
        self.threshold = threshold
        self.check_steps = check_steps
        self.check_interval = check_interval

    def on_log(self, args, state, control, logs=None, **kwargs):
        if state.global_step > self.check_steps:
            return
        if state.global_step % self.check_interval != 0:
            return
        loss = logs.get("loss") if logs else None
        if loss is not None and loss > self.threshold:
            logger.error(
                "EARLY STOP: loss=%.4f > threshold=%.1f at step %d. Training diverged.",
                loss, self.threshold, state.global_step,
            )
            control.should_training_stop = True


def train_generation(
    gen_idx: int,
    train_dataset,
    config,
    model_name_or_path: str | None = None,
) -> tuple[str, list[str]]:
    """Train one generation, return (final_checkpoint_path, all_checkpoint_paths).

    Args:
        gen_idx: Generation index (0, 1, 2).
        train_dataset: PackedDataset for this generation.
        config: PilotConfig.
        model_name_or_path: Override model init (default: config.model_name).

    Returns:
        (final_model_dir, checkpoint_paths) where final_model_dir is the
        directory containing the fully trained model.
    """
    model_name = model_name_or_path or config.model_name
    output_dir = os.path.join(config.gen_dir(gen_idx), "training")
    final_dir = os.path.join(config.gen_dir(gen_idx), "final_model")

    logger.info("=== Generation %d: training from %s ===", gen_idx, model_name)
    logger.info("  Train sequences: %d | Max steps: %d | Save every %d steps",
                len(train_dataset), config.max_steps, config.save_steps)

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
        attn_implementation="sdpa",
    )
    if config.gradient_checkpointing:
        model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})

    ckpt_cb = CheckpointListCallback()

    run_name = f"{config.wandb_run_prefix}_G{gen_idx}"
    training_args = TrainingArguments(
        output_dir=output_dir,
        max_steps=config.max_steps,
        per_device_train_batch_size=config.per_device_batch_size,
        gradient_accumulation_steps=config.gradient_accumulation_steps,
        learning_rate=config.learning_rate,
        warmup_ratio=config.warmup_ratio,
        weight_decay=config.weight_decay,
        bf16=config.bf16,
        logging_steps=50,
        save_steps=config.save_steps,
        save_total_limit=None,
        seed=config.seed,
        max_grad_norm=1.0,
        report_to="wandb" if config.use_wandb else "none",
        run_name=run_name,
        dataloader_num_workers=2,
        dataloader_pin_memory=True,
        remove_unused_columns=False,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        callbacks=[ckpt_cb, EarlyStopOnHighLossCallback()],
    )

    trainer.train()

    # save final model (separate from checkpoints)
    os.makedirs(final_dir, exist_ok=True)
    trainer.save_model(final_dir)
    tokenizer.save_pretrained(final_dir)
    logger.info("Final model saved to %s", final_dir)

    return final_dir, ckpt_cb.saved_checkpoints

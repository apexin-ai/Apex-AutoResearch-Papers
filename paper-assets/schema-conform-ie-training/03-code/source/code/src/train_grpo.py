# GRPO training for Schema-Conformance IE.
# Usage: python src/train_grpo.py --config configs/grpo_conformance.yaml --data_dir /path/to/scierc
# Requires: torch, transformers, trl, peft, accelerate, wandb, pyyaml.

import argparse
import json
import logging
import os
import sys
from collections import defaultdict

import torch
import yaml
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainerCallback
from trl import GRPOConfig, GRPOTrainer

from src.data_utils import (
    load_ace2005_dygiepp, load_ace2005_json, load_scierc_dygiepp,
    IEDataset, ACE2005_SCHEMA, SCIERC_SCHEMA, DATASET_SCHEMAS,
)
from src.rewards import compute_all_rewards, gdpo_from_precomputed, REWARD_NAMES

logger = logging.getLogger(__name__)

CONFORMANCE_KEYS = [
    "structural_validity", "type_conformance",
    "relational_constraint", "structural_completeness",
]


class RewardTracker:
    """Accumulates per-component reward values for hacking detection."""

    def __init__(self, warmup_samples: int = 200):
        self.components: dict[str, list[float]] = defaultdict(list)
        self.baseline_f1: float | None = None
        self.warmup_samples = warmup_samples

    def record(self, rewards_dict: dict[str, float]) -> None:
        for k, v in rewards_dict.items():
            self.components[k].append(v)

    def try_set_baseline(self) -> None:
        """Set baseline F1 from the first warmup_samples entries (once)."""
        if self.baseline_f1 is not None:
            return
        f1_vals = self.components.get("f1_correctness", [])
        if len(f1_vals) >= self.warmup_samples:
            self.baseline_f1 = sum(f1_vals[: self.warmup_samples]) / self.warmup_samples

    def recent_means(self, window: int = 200) -> dict[str, float]:
        means = {}
        for k, vals in self.components.items():
            recent = vals[-window:] if len(vals) > window else vals
            means[k] = sum(recent) / len(recent) if recent else 0.0
        return means


class RewardHackingCallback(TrainerCallback):
    """Checks for reward hacking at each checkpoint save.

    Condition: mean conformance rewards > 0.95 AND mean F1 < baseline_f1 * 0.8.
    Logs WARNING and records the step — the checkpoint is already saved by the trainer.
    """

    def __init__(self, tracker: RewardTracker, output_dir: str):
        self.tracker = tracker
        self.output_dir = output_dir
        self.flagged_steps: list[int] = []

    def on_save(self, args, state, control, **kwargs):
        self.tracker.try_set_baseline()
        if self.tracker.baseline_f1 is None:
            return

        means = self.tracker.recent_means()
        conformance_mean = (
            sum(means.get(k, 0) for k in CONFORMANCE_KEYS) / len(CONFORMANCE_KEYS)
        )
        f1_mean = means.get("f1_correctness", 0)

        if conformance_mean > 0.95 and f1_mean < self.tracker.baseline_f1 * 0.8:
            step = state.global_step
            logger.warning(
                "[REWARD HACKING DETECTED] step=%d conformance_mean=%.4f "
                "f1_mean=%.4f baseline_f1=%.4f",
                step, conformance_mean, f1_mean, self.tracker.baseline_f1,
            )
            self.flagged_steps.append(step)
            flag_path = os.path.join(self.output_dir, "reward_hacking_flags.json")
            with open(flag_path, "w") as f:
                json.dump({"flagged_steps": self.flagged_steps, "baseline_f1": self.tracker.baseline_f1}, f, indent=2)


def load_config(config_path: str) -> dict:
    """Load YAML config file."""
    with open(config_path) as f:
        return yaml.safe_load(f)


def build_reward_fn(
    weights: dict[str, float],
    use_gdpo: bool,
    tracker: RewardTracker | None = None,
):
    """Build reward function compatible with GRPOTrainer.

    Computes per-component rewards, records them in tracker (for hacking
    detection), then returns combined scores (weighted sum or GDPO).
    """

    def reward_fn(completions: list[str], **kwargs) -> list[float]:
        schemas_raw = kwargs.get("schema", [])
        golds_raw = kwargs.get("gold", [])

        schemas = [json.loads(s) if isinstance(s, str) else s for s in schemas_raw]
        golds = [json.loads(g) if isinstance(g, str) else g for g in golds_raw]

        all_component_rewards = [
            compute_all_rewards(comp, schema, gold)
            for comp, schema, gold in zip(completions, schemas, golds)
        ]

        if tracker:
            for r in all_component_rewards:
                tracker.record(r)

        if use_gdpo:
            return gdpo_from_precomputed(all_component_rewards, weights)

        return [
            sum(weights.get(k, 0.0) * v for k, v in r.items())
            for r in all_component_rewards
        ]

    return reward_fn


def main():
    parser = argparse.ArgumentParser(description="GRPO training for Schema-Conformance IE")
    parser.add_argument("--config", required=True, help="Path to YAML config")
    parser.add_argument("--data_dir", default=None, help="Data dir (DyGIE++ format)")
    parser.add_argument("--data_path", default=None, help="Pre-converted JSON data path")
    parser.add_argument("--dataset", default="scierc", choices=["scierc", "ace2005"], help="Training dataset")
    parser.add_argument("--output_dir", default=None, help="Override output directory")
    parser.add_argument("--max_steps", type=int, default=None, help="Override max training steps (e.g. 5 for dry-run)")
    parser.add_argument("--dry_run", action="store_true", help="Run 5 steps to verify setup")
    args = parser.parse_args()

    config = load_config(args.config)
    output_dir = args.output_dir or config.get("output_dir", "./output")
    os.makedirs(output_dir, exist_ok=True)

    # ---- Data ----
    schema = DATASET_SCHEMAS.get(args.dataset, SCIERC_SCHEMA)
    if args.data_path:
        samples = load_ace2005_json(args.data_path)
    elif args.data_dir:
        if args.dataset == "scierc":
            samples = load_scierc_dygiepp(args.data_dir, split="train")
        else:
            samples = load_ace2005_dygiepp(args.data_dir, split="train")
    else:
        raise ValueError("Provide --data_dir (DyGIE++ format) or --data_path (pre-converted JSON)")

    dataset = IEDataset(samples, schema)
    train_dataset = dataset.to_grpo_dataset()
    print(f"Loaded {len(train_dataset)} training samples")

    # ---- Model ----
    model_name = config["model_name"]
    print(f"Loading model: {model_name}")

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Disable thinking mode for Qwen3/3.5 — thinking consumes all completion tokens
    if tokenizer.chat_template and "enable_thinking" in tokenizer.chat_template:
        tokenizer.chat_template = (
            "{%- set enable_thinking = false -%}" + tokenizer.chat_template
        )

    model_kwargs = {
        "torch_dtype": torch.bfloat16 if config.get("bf16", True) else torch.float32,
        "trust_remote_code": True,
    }
    try:
        model_kwargs["attn_implementation"] = "flash_attention_2"
        model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
    except (ImportError, ValueError):
        model_kwargs.pop("attn_implementation", None)
        model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)

    # ---- LoRA ----
    if config.get("use_lora", False):
        from peft import LoraConfig, get_peft_model

        lora_config = LoraConfig(
            r=config.get("lora_r", 16),
            lora_alpha=config.get("lora_alpha", 32),
            lora_dropout=config.get("lora_dropout", 0.05),
            target_modules=config.get("lora_target_modules", ["q_proj", "k_proj", "v_proj", "o_proj"]),
            task_type="CAUSAL_LM",
        )
        model = get_peft_model(model, lora_config)
        model.print_trainable_parameters()

    # ---- Reward + hacking detection ----
    weights = config.get("reward_weights", {"f1_correctness": 1.0})
    use_gdpo = config.get("use_gdpo", False)
    tracker = RewardTracker(warmup_samples=config.get("hacking_warmup_samples", 200))
    reward_fn = build_reward_fn(weights, use_gdpo, tracker=tracker)
    hacking_callback = RewardHackingCallback(tracker, output_dir)

    # ---- Trainer ----
    max_steps = args.max_steps if args.max_steps else config.get("max_steps", -1 if not args.dry_run else 5)

    training_args = GRPOConfig(
        output_dir=output_dir,
        num_generations=config.get("num_generations", 8),
        max_completion_length=config.get("max_new_tokens", 512),
        per_device_train_batch_size=config.get("per_device_train_batch_size", 1),
        gradient_accumulation_steps=config.get("gradient_accumulation_steps", 8),
        num_train_epochs=config.get("num_train_epochs", 3),
        max_steps=max_steps,
        learning_rate=config.get("learning_rate", 1e-6),
        warmup_ratio=config.get("warmup_ratio", 0.1),
        bf16=config.get("bf16", True),
        gradient_checkpointing=config.get("gradient_checkpointing", False),
        logging_steps=1 if args.dry_run else config.get("logging_steps", 10),
        save_steps=config.get("save_steps", 100),
        report_to="none" if args.dry_run else config.get("report_to", "wandb"),
        run_name=config.get("run_name", "grpo-ie"),
        seed=config.get("seed", 42),
        log_completions=True,
    )

    if config.get("wandb_project"):
        os.environ["WANDB_PROJECT"] = config["wandb_project"]

    trainer = GRPOTrainer(
        model=model,
        reward_funcs=reward_fn,
        args=training_args,
        train_dataset=train_dataset,
        processing_class=tokenizer,
        callbacks=[hacking_callback],
    )

    # ---- Train ----
    if args.dry_run:
        print(f"[DRY RUN] Running {max_steps} steps to verify setup...")
    print("Starting GRPO training...")
    trainer.train()

    # ---- Save ----
    print(f"Saving to {output_dir}")
    if config.get("use_lora", False):
        merged = trainer.model.merge_and_unload()
        merged_dir = os.path.join(output_dir, "merged")
        merged.save_pretrained(merged_dir)
        tokenizer.save_pretrained(merged_dir)
        print(f"Merged LoRA model saved to {merged_dir}")
    else:
        trainer.save_model(output_dir)
        tokenizer.save_pretrained(output_dir)

    with open(os.path.join(output_dir, "training_config.yaml"), "w") as f:
        yaml.dump(config, f)

    print("Training complete.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""exp-002v3: DC-GRPO with scaled cosine R1.

Parent: exp-002v2 (cosine R1, but R1 signal too weak vs R3)
Key change: r1_scale_factor=5.0 amplifies cosine R1 from ~[-0.2, +0.2] to ~[-1, +1],
making it commensurate with R3 (NLI, [0,1]). Weights rebalanced to 0.5/0.5.
"""

# MONITORING: step 0-50 异常阈值
# - grad_norm > 1.0 → 立即汇报
# - entropy < 0.1 → 立即汇报
# FALLBACK: 如果不稳定，准备 scale=5 + weight=0.3 配置

import json
import logging
import os
import sys
from pathlib import Path

import torch
from datasets import Dataset
from peft import LoraConfig
from transformers import AutoTokenizer

sys.path.insert(0, "/root/mvp_v2_1_expanded/training")
from dcgrpo_trainer import DCGRPOConfig, DCGRPOTrainer

OUTPUT_DIR = "/root/contrastive_entrain_calib/checkpoints/exp002v3_dcgrpo_scaled_cosine"
os.makedirs(OUTPUT_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(os.path.join(OUTPUT_DIR, "train.log")),
    ],
)
logger = logging.getLogger("exp002v3")

MODEL_PATH = "/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B"
DATA_PATH = "/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl"
DIRECTION_PATH = "/root/contrastive_entrain_calib/results/exp001/directions.pt"

R1_WEIGHT = 0.4
R2_WEIGHT = 0.0
R3_WEIGHT = 0.6
R1_SCALE_FACTOR = 5.0
REWARD_LAYERS = [19, 20, 24, 27, 32, 33, 35]
SEED = 42


class _StrengthAwareReward:
    __name__ = "dc_grpo_reward"

    def __init__(self, trainer, inner):
        self.trainer = trainer
        self._inner = inner

    def __call__(self, prompts, completions, **kwargs):
        self.trainer._current_strengths = kwargs.get(
            "evidence_strength", ["unknown"] * len(completions)
        )
        return self._inner(prompts, completions, **kwargs)


class Exp002v3Trainer(DCGRPOTrainer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._current_strengths = []
        self._log_step = 0
        self.reward_funcs = [_StrengthAwareReward(self, self.reward_funcs[0])]
        if hasattr(self, "reward_func_names"):
            self.reward_func_names = ["dc_grpo_reward"]

    def compute_rewards(self, completions, conditions, pair_ids, batch_activations, r1_ema=None, ema_alpha=0.3):
        rewards, components = super().compute_rewards(
            completions, conditions, pair_ids, batch_activations, r1_ema, ema_alpha
        )

        self._log_step += 1
        log_this = (self._log_step <= 50) or (self._log_step % 10 == 0)
        if log_this:
            import statistics
            r1_vals = list(components.get("r1", []))
            r3_vals = list(components.get("r3", []))
            combined = [float(r) for r in rewards]
            if r1_vals:
                r1_m = sum(r1_vals) / len(r1_vals)
                r1_s = statistics.stdev(r1_vals) if len(r1_vals) > 1 else 0.0
                logger.info("step=%d R1 mean=%.4f std=%.4f", self._log_step, r1_m, r1_s)
            if r3_vals:
                r3_m = sum(r3_vals) / len(r3_vals)
                r3_s = statistics.stdev(r3_vals) if len(r3_vals) > 1 else 0.0
                logger.info("step=%d R3 mean=%.4f std=%.4f", self._log_step, r3_m, r3_s)
            if combined:
                c_s = statistics.stdev(combined) if len(combined) > 1 else 0.0
                logger.info("step=%d combined_reward std=%.4f", self._log_step, c_s)
            strengths = self._current_strengths or []
            for strength in ["weak", "medium", "strong"]:
                indices = [i for i, s in enumerate(strengths) if s == strength]
                if indices:
                    sv = [r1_vals[i] for i in indices if i < len(r1_vals)]
                    if sv:
                        logger.info("step=%d reward/r1_%s_mean=%.4f n=%d", self._log_step, strength, sum(sv) / len(sv), len(sv))

        return rewards, components


def load_dataset(tokenizer):
    records = []
    with open(DATA_PATH) as f:
        for line in f:
            rec = json.loads(line)
            msgs = [{"role": t["role"], "content": t["content"]} for t in rec["turns"]]
            try:
                prompt = tokenizer.apply_chat_template(
                    msgs, tokenize=False, add_generation_prompt=True, enable_thinking=False
                )
            except TypeError:
                prompt = tokenizer.apply_chat_template(
                    msgs, tokenize=False, add_generation_prompt=True
                )
            records.append({
                "prompt": prompt,
                "condition": rec["condition"],
                "pair_id": str(rec["pair_id"]),
                "evidence_strength": rec.get("evidence_strength", "unknown"),
            })
    logger.info("Loaded %d records from %s", len(records), DATA_PATH)
    return Dataset.from_list(records)


def main():
    torch.manual_seed(SEED)

    logger.info("=== exp-002v3: DC-GRPO Scaled Cosine R1 ===")
    logger.info("Weights: R1=%.2f, R2=%.2f, R3=%.2f | R1 scale_factor=%.1f", R1_WEIGHT, R2_WEIGHT, R3_WEIGHT, R1_SCALE_FACTOR)
    logger.info("Reward layers: %s", REWARD_LAYERS)

    model_path = MODEL_PATH if Path(MODEL_PATH).exists() else "Qwen/Qwen3-8B"

    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id

    dataset = load_dataset(tokenizer)

    config = DCGRPOConfig(
        output_dir=OUTPUT_DIR,
        direction_path=DIRECTION_PATH,
        reward_layers=REWARD_LAYERS,
        reward_position="asst_first",
        r1_weight=R1_WEIGHT,
        r2_weight=R2_WEIGHT,
        r3_weight=R3_WEIGHT,
        r1_scale_factor=R1_SCALE_FACTOR,
        r3_model_name="cross-encoder/nli-deberta-v3-base",
        recalibration_interval=500,
        calibration_data_path=DATA_PATH,
        num_train_epochs=10,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=16,
        gradient_checkpointing=True,
        learning_rate=5e-5,
        warmup_steps=200,
        logging_steps=10,
        save_steps=500,
        max_steps=8000,
        bf16=True,
        seed=SEED,
        max_completion_length=256,
        num_generations=2,
    )

    peft_config = LoraConfig(
        r=64,
        lora_alpha=64,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
        bias="none",
        task_type="CAUSAL_LM",
    )

    trainer = Exp002v3Trainer(
        model=model_path,
        args=config,
        train_dataset=dataset,
        processing_class=tokenizer,
        peft_config=peft_config,
    )

    logger.info("Starting training...")
    trainer.train()
    trainer.save_model(os.path.join(OUTPUT_DIR, "final"))
    trainer.cleanup()
    logger.info("Training complete. Checkpoint: %s/final", OUTPUT_DIR)


if __name__ == "__main__":
    main()

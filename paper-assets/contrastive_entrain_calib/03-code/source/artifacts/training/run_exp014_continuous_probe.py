#!/usr/bin/env python3
"""exp-014: Continuous probe baseline for DC-GRPO comparison.

Replaces R1 (direction projection) with a logistic regression probe trained
on exp-001 calibration activations. R1 = 1.0 - P(sycophantic), where P(syc)
is the probe's output probability. All other settings follow exp-002.

This baseline tests whether DC-GRPO's continuous direction signal outperforms
a binary-trained probe signal for sycophancy calibration.
"""
import json
import logging
import os
import sys
from pathlib import Path

import torch
from datasets import Dataset
from peft import LoraConfig
from transformers import AutoTokenizer

if "HF_ENDPOINT" not in os.environ:
    os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

sys.path.insert(0, "/root/mvp_v2_1_expanded/training")
from dcgrpo_trainer import DCGRPOConfig, DCGRPOTrainer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_module import load_probe, save_probe, train_probe

OUTPUT_DIR = "/root/contrastive_entrain_calib/checkpoints/exp014_probe_baseline"
os.makedirs(OUTPUT_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(os.path.join(OUTPUT_DIR, "train.log")),
    ],
)
logger = logging.getLogger("exp014")

MODEL_PATH = "/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B"
DATA_PATH = "/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl"
DIRECTION_PATH = "/root/contrastive_entrain_calib/results/exp001/directions.pt"
ACTIVATIONS_PATH = "/root/contrastive_entrain_calib/results/exp001/activations.pt"

R1_WEIGHT = 0.25
R2_WEIGHT = 0.0
R3_WEIGHT = 0.75
REWARD_LAYERS = [19, 20, 24, 27, 32, 33, 35]
SEED = 42

PROBE_PATH = os.path.join(OUTPUT_DIR, "probe.pt")


class ProbeTrainer(DCGRPOTrainer):
    """DCGRPOTrainer with probe-based R1 replacing direction projection.

    The frozen logistic regression probe predicts P(sycophantic) from mean
    hidden states across reward layers. R1 = 1.0 - P(syc) for all conditions.
    """

    def __init__(self, *args, probe=None, **kwargs):
        self._probe = probe
        self._probe_device = torch.device("cpu")
        super().__init__(*args, **kwargs)
        if self._probe is not None:
            self._probe_device = next(self._probe.parameters()).device
            logger.info("Probe R1 active, device=%s", self._probe_device)

    def compute_r1(self, activations, condition):
        """R1 = 1.0 - P(sycophantic) via frozen logistic probe.

        Input: mean hidden state across reward layers at asst_first position.
        No condition-based sign flip needed since the probe directly outputs
        sycophancy probability (high P(syc) = bad for both conditions).
        """
        if self._probe is None:
            return 0.0

        vecs = []
        for layer_idx in self._reward_layers:
            h = activations.get(layer_idx)
            if h is not None:
                vecs.append(h)
        if not vecs:
            return 0.0

        mean_h = torch.stack(vecs).mean(dim=0)
        with torch.no_grad():
            p_syc = self._probe(mean_h.unsqueeze(0).to(self._probe_device)).item()
        return 1.0 - p_syc


def load_dataset(tokenizer):
    records = []
    with open(DATA_PATH) as f:
        for line in f:
            rec = json.loads(line)
            msgs = [{"role": t["role"], "content": t["content"]} for t in rec["turns"]]
            try:
                prompt = tokenizer.apply_chat_template(
                    msgs,
                    tokenize=False,
                    add_generation_prompt=True,
                    enable_thinking=False,
                )
            except TypeError:
                prompt = tokenizer.apply_chat_template(
                    msgs, tokenize=False, add_generation_prompt=True
                )
            records.append(
                {
                    "prompt": prompt,
                    "condition": rec["condition"],
                    "pair_id": str(rec["pair_id"]),
                    "evidence_strength": rec.get("evidence_strength", "unknown"),
                }
            )
    logger.info("Loaded %d records from %s", len(records), DATA_PATH)
    return Dataset.from_list(records)


def main():
    torch.manual_seed(SEED)

    logger.info("=== exp-014: Continuous Probe Baseline ===")
    logger.info("Weights: R1=%.2f (probe), R2=%.2f, R3=%.2f", R1_WEIGHT, R2_WEIGHT, R3_WEIGHT)
    logger.info("Reward layers: %s", REWARD_LAYERS)

    # --- Step 1: Train or load probe ---
    if Path(PROBE_PATH).exists():
        logger.info("Loading existing probe from %s", PROBE_PATH)
        probe = load_probe(PROBE_PATH)
    else:
        logger.info("Training probe on exp-001 activations: %s", ACTIVATIONS_PATH)
        probe, acc, auroc = train_probe(
            ACTIVATIONS_PATH,
            layers=REWARD_LAYERS,
            position_idx=1,
            seed=SEED,
        )
        save_probe(probe, PROBE_PATH)
        logger.info("Probe trained: accuracy=%.4f, AUROC=%.4f (exp-001 ref: 0.827), saved to %s", acc, auroc, PROBE_PATH)
        logger.info("Probe vs exp-001 direction: AUROC delta = %.4f", auroc - 0.827)

    probe.eval()
    for p in probe.parameters():
        p.requires_grad_(False)

    # --- Step 2: GRPO training setup ---
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
        r3_model_name="cross-encoder/nli-deberta-v3-base",
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

    trainer = ProbeTrainer(
        model=model_path,
        args=config,
        train_dataset=dataset,
        processing_class=tokenizer,
        peft_config=peft_config,
        probe=probe,
    )

    # Move probe to model device after trainer init
    model_device = next(trainer.model.parameters()).device
    probe.to(model_device)
    trainer._probe_device = model_device
    logger.info("Probe moved to model device: %s", model_device)

    # --- Step 3: Train ---
    logger.info("Starting GRPO training with probe-based R1...")
    trainer.train()
    trainer.save_model(os.path.join(OUTPUT_DIR, "final"))
    trainer.cleanup()
    logger.info("Training complete. Checkpoint: %s/final", OUTPUT_DIR)


if __name__ == "__main__":
    main()

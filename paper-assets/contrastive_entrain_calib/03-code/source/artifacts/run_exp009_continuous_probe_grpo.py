#!/usr/bin/env python3
"""exp-009: Continuous Probe Probability GRPO -- ablation cascade member.

Ablation cascade:
  exp-003: R3-only (no R1)
  exp-008 v3: Binary Probe R1 (threshold at 0.5)
  exp-009: Continuous Probe R1 (this script)
  exp-002: Directional Projection R1 (full DC-GRPO)

Difference from exp-008v3:
  exp-008v3: R1 = 1.0 if P(syc) <= 0.5 else 0.0  (binary)
  exp-009:   R1 = 1.0 - P(sycophantic|h)           (continuous [0,1])

The probe is a frozen logistic regression trained on exp-001 activations.
Probe is retrained every 500 steps (same as exp-008v3) to track drift.
All other config (model, data, GRPO params, LoRA, DeepSpeed) identical to exp-008v3.

Input:  calibration_v2_1_expanded.jsonl (362 pairs)
Output: LoRA checkpoints in /root/autodl-tmp/checkpoints/exp009_continuous_probe_grpo/
"""
import json
import logging
import os
import random
import sys
from pathlib import Path

import torch
import torch.nn as nn
from datasets import Dataset
from peft import LoraConfig
from transformers import AutoTokenizer

if "HF_ENDPOINT" not in os.environ:
    os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

sys.path.insert(0, "/root/mvp_v2_1_expanded/training")
from dcgrpo_trainer import DCGRPOConfig, DCGRPOTrainer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_module import LinearProbe, load_probe, save_probe, train_probe

OUTPUT_DIR = "/root/autodl-tmp/checkpoints/exp009_continuous_probe_grpo"
os.makedirs(OUTPUT_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(os.path.join(OUTPUT_DIR, "train.log")),
    ],
)
logger = logging.getLogger("exp009")

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
RETRAIN_INTERVAL = 500
RETRAIN_SAMPLES = 362


class ContinuousProbeTrainer(DCGRPOTrainer):
    """DCGRPOTrainer with continuous probe-based R1.

    R1 = 1.0 - P(sycophantic|h), where P(sycophantic|h) is the sigmoid
    output of a frozen logistic regression probe. Continuous value in [0,1].
    Probe is retrained every RETRAIN_INTERVAL steps on current activations.
    """

    def __init__(self, *args, probe=None, retrain_interval=RETRAIN_INTERVAL, **kwargs):
        self._probe = probe
        self._probe_device = torch.device("cpu")
        self._retrain_interval = retrain_interval
        self._last_retrain_step = 0
        super().__init__(*args, **kwargs)
        if self._probe is not None:
            self._probe_device = next(self._probe.parameters()).device
            logger.info("Continuous probe R1 active, device=%s", self._probe_device)

    def compute_r1(self, activations, condition):
        """R1 = 1.0 - P(sycophantic|h) via continuous probe output."""
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

    def training_step(self, model, inputs, num_items_in_batch=None, **kwargs):
        result = super().training_step(model, inputs, num_items_in_batch=num_items_in_batch, **kwargs)
        step = self.state.global_step
        if (step > 0
                and step % self._retrain_interval == 0
                and step != self._last_retrain_step):
            self._last_retrain_step = step
            self._retrain_probe(step)
        return result

    def _retrain_probe(self, step: int):
        """Retrain probe on current model's activations."""
        logger.info("[Step %d] Retraining probe on current model activations...", step)

        unwrapped = self.accelerator.unwrap_model(self.model)
        unwrapped.eval()

        rng = random.Random(step)
        n_samples = len(self.train_dataset)
        indices = list(range(n_samples))

        device = next(unwrapped.parameters()).device
        features = []
        labels = []

        for idx in indices:
            example = self.train_dataset[idx]
            condition = example["condition"]

            tok_out = self.processing_class(
                example["prompt"],
                return_tensors="pt",
                truncation=True,
                max_length=512,
            )
            input_ids = tok_out["input_ids"].to(device)
            attention_mask = tok_out["attention_mask"].to(device)

            with torch.no_grad():
                outputs = unwrapped(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    output_hidden_states=True,
                )

            vecs = []
            for layer_idx in self._reward_layers:
                h = outputs.hidden_states[layer_idx + 1]
                vecs.append(h[0, -1].float().cpu())

            mean_h = torch.stack(vecs).mean(dim=0)
            features.append(mean_h)
            labels.append(1.0 if condition == "invalid_pressure" else 0.0)

        if len(features) < 10:
            logger.warning(
                "[Step %d] Too few samples (%d), skipping retrain",
                step, len(features),
            )
            unwrapped.train()
            return

        X = torch.stack(features)
        y = torch.tensor(labels)

        new_probe = LinearProbe(X.shape[1])
        new_probe.feat_mean.copy_(X.mean(dim=0))
        new_probe.feat_std.copy_(X.std(dim=0))

        optimizer = torch.optim.Adam(
            new_probe.parameters(), lr=1e-2, weight_decay=1e-4,
        )
        criterion = nn.BCELoss()

        new_probe.train()
        for epoch in range(200):
            preds = new_probe(X)
            loss = criterion(preds, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        new_probe.eval()
        with torch.no_grad():
            final_preds = new_probe(X)
            acc = ((final_preds > 0.5).float() == y).float().mean().item()

        for p in new_probe.parameters():
            p.requires_grad_(False)
        new_probe.to(self._probe_device)
        self._probe = new_probe

        save_probe(new_probe, os.path.join(OUTPUT_DIR, f"probe_step{step}.pt"))

        unwrapped.train()
        logger.info(
            "[Step %d] Probe retrained, accuracy=%.4f on %d samples",
            step, acc, len(features),
        )


def load_dataset(tokenizer):
    records = []
    with open(DATA_PATH) as f:
        for line in f:
            rec = json.loads(line)
            msgs = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": rec["turn1"]},
                {"role": "assistant", "content": rec["turn2"]},
                {"role": "user", "content": rec["turn3"]},
            ]
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

    logger.info("=== exp-009: Continuous Probe Probability GRPO ===")
    logger.info(
        "Ablation cascade: R3-only < Binary Probe < Continuous Probe < Directional (DC-GRPO)"
    )
    logger.info(
        "Weights: R1=%.2f (continuous probe), R2=%.2f, R3=%.2f",
        R1_WEIGHT, R2_WEIGHT, R3_WEIGHT,
    )
    logger.info("Reward layers: %s", REWARD_LAYERS)
    logger.info("Probe retrain interval: %d steps", RETRAIN_INTERVAL)

    # --- Step 1: Train or load initial probe ---
    if Path(PROBE_PATH).exists():
        logger.info("Loading existing probe from %s", PROBE_PATH)
        probe = load_probe(PROBE_PATH)
    else:
        logger.info("Training initial probe on exp-001 activations: %s", ACTIVATIONS_PATH)
        probe, acc, auroc = train_probe(
            ACTIVATIONS_PATH,
            layers=REWARD_LAYERS,
            position_idx=1,
            seed=SEED,
        )
        save_probe(probe, PROBE_PATH)
        logger.info(
            "Probe trained: accuracy=%.4f, AUROC=%.4f, saved to %s",
            acc, auroc, PROBE_PATH,
        )

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
        report_to="none",
        deepspeed="/root/contrastive_entrain_calib/training/ds_config_zero2.json",
    )

    peft_config = LoraConfig(
        r=64,
        lora_alpha=64,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
        bias="none",
        task_type="CAUSAL_LM",
    )

    trainer = ContinuousProbeTrainer(
        model=model_path,
        args=config,
        train_dataset=dataset,
        processing_class=tokenizer,
        peft_config=peft_config,
        probe=probe,
    )

    model_device = next(trainer.model.parameters()).device
    probe.to(model_device)
    trainer._probe_device = model_device
    logger.info("Probe moved to model device: %s", model_device)

    # --- Step 3: Train ---
    logger.info("Starting GRPO training with continuous probe R1...")
    trainer.train()
    trainer.save_model(os.path.join(OUTPUT_DIR, "final"))
    trainer.cleanup()
    logger.info("Training complete. Checkpoint: %s/final", OUTPUT_DIR)


if __name__ == "__main__":
    main()

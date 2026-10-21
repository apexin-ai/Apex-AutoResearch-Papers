#!/usr/bin/env python3
"""exp-008 v3: Binary Probe GRPO -- ablation cascade member.

Ablation cascade:
  exp-003: R3-only (no R1)
  exp-008 v3: Binary Probe R1 (this script)
  exp-014: Continuous Probe R1
  exp-002: Directional Projection R1 (full DC-GRPO)

Replaces R1 (direction projection) with a binary logistic regression probe.
R1 = 1.0 if P(sycophantic) <= 0.5, else 0.0. The probe is retrained every
500 steps on the current model's activations to track representation drift.
"""
import argparse
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

parser = argparse.ArgumentParser(description="exp-008v3 Binary Probe GRPO")
parser.add_argument("--seed", type=int, default=42)
parser.add_argument("--max_steps", type=int, default=2000)
parser.add_argument("--output_dir", type=str, default=None)
_args = parser.parse_args()

if "HF_ENDPOINT" not in os.environ:
    os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

sys.path.insert(0, "/root/mvp_v2_1_expanded/training")
from dcgrpo_trainer import DCGRPOConfig, DCGRPOTrainer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_module import LinearProbe, load_probe, save_probe, train_probe

OUTPUT_DIR = _args.output_dir or f"/root/autodl-tmp/checkpoints/exp008v3_seed{_args.seed}"
os.makedirs(OUTPUT_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(os.path.join(OUTPUT_DIR, "train.log")),
    ],
)
logger = logging.getLogger("exp008v3")

MODEL_PATH = "/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B"
DATA_PATH = "/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl"
DIRECTION_PATH = "/root/contrastive_entrain_calib/results/exp001/directions.pt"
ACTIVATIONS_PATH = "/root/contrastive_entrain_calib/results/exp001/activations.pt"

R1_WEIGHT = 0.25
R2_WEIGHT = 0.0
R3_WEIGHT = 0.75
REWARD_LAYERS = [19, 20, 24, 27, 32, 33, 35]
SEED = _args.seed
MAX_STEPS = _args.max_steps

PROBE_PATH = os.path.join(OUTPUT_DIR, "probe.pt")
RETRAIN_INTERVAL = 500
RETRAIN_SAMPLES = 362


class BinaryProbeTrainer(DCGRPOTrainer):
    """DCGRPOTrainer with binary probe-based R1.

    R1 = 1.0 if P(sycophantic) <= 0.5, else 0.0. Probe is retrained every
    RETRAIN_INTERVAL steps on the current model's activations.
    """

    def __init__(self, *args, probe=None, retrain_interval=RETRAIN_INTERVAL, **kwargs):
        self._probe = probe
        self._probe_device = torch.device("cpu")
        self._retrain_interval = retrain_interval
        self._last_retrain_step = 0
        super().__init__(*args, **kwargs)
        if self._probe is not None:
            self._probe_device = next(self._probe.parameters()).device
            logger.info("Binary probe R1 active, device=%s", self._probe_device)

    def compute_r1(self, activations, condition):
        """R1 = 1.0 if P(sycophantic) <= 0.5, else 0.0 via binary probe."""
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
        return 1.0 if p_syc <= 0.5 else 0.0

    def training_step(self, model, inputs, **kwargs):
        result = super().training_step(model, inputs, **kwargs)
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

    logger.info("=== exp-008 v3: Binary Probe GRPO ===")
    logger.info(
        "Ablation cascade: R3-only < Binary Probe < Continuous Probe < Directional (DC-GRPO)"
    )
    logger.info(
        "Weights: R1=%.2f (binary probe), R2=%.2f, R3=%.2f",
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
        max_steps=MAX_STEPS,
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

    trainer = BinaryProbeTrainer(
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
    logger.info("Starting GRPO training with binary probe R1...")
    trainer.train()
    trainer.save_model(os.path.join(OUTPUT_DIR, "final"))
    trainer.cleanup()
    logger.info("Training complete. Checkpoint: %s/final", OUTPUT_DIR)


if __name__ == "__main__":
    main()

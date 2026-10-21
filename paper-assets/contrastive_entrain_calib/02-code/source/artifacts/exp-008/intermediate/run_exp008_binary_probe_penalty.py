#!/usr/bin/env python3
"""exp-008: Binary Probe Penalty baseline for sycophancy calibration.

SFT-style LoRA training on Qwen3-8B with a frozen binary probe penalty.
Designed to run on a single RTX 5090 (32 GB) without GRPO's memory overhead.

Loss:
    L = L_sft - lambda_reward * (R3 - lambda_probe * S(t))
      = L_sft + lambda_reward * lambda_probe * S(t) - lambda_reward * R3

    L_sft:  cross-entropy on last-assistant-turn tokens (standard SFT)
    S(t):   frozen logistic probe sycophancy score, differentiable through hidden states
    R3:     NLI behavioral reward, precomputed on training data (constant, for monitoring)

Input:
    Model:       /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B
    Data:        calibration_data.jsonl (4-turn conversations with target responses)
    Activations: results/exp001/activations.pt (for probe pretraining)

Output:
    LoRA checkpoints every 500 steps + final in output_dir

Dependencies: torch, transformers, peft
"""
import argparse
import json
import logging
import os
import re
import sys
from dataclasses import dataclass, field
from functools import partial
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torch.utils.data import Dataset as TorchDataset

from peft import LoraConfig, get_peft_model
from transformers import (
    AutoModelForCausalLM,
    AutoModelForSequenceClassification,
    AutoTokenizer,
    get_cosine_schedule_with_warmup,
)

CONDITION_MAP = {
    "warranted_revision": "valid_correction",
    "sycophantic_capitulation": "invalid_pressure",
    "valid_correction": "valid_correction",
    "invalid_pressure": "invalid_pressure",
}


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
@dataclass
class TrainConfig:
    model_path: str = "/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B"
    data_path: str = "/root/contrastive_entrain_calib/calibration_data.jsonl"
    activations_path: str = (
        "/root/contrastive_entrain_calib/results/exp001/activations.pt"
    )
    output_dir: str = (
        "/root/contrastive_entrain_calib/checkpoints/exp008_binary_probe_penalty"
    )

    # LoRA
    lora_rank: int = 16
    lora_alpha: int = 32
    lora_targets: list[str] = field(
        default_factory=lambda: ["q_proj", "v_proj", "k_proj", "o_proj"]
    )

    # Training
    lr: float = 5e-6
    warmup_steps: int = 100
    max_steps: int = 8000
    batch_size: int = 1
    grad_accum: int = 16
    max_seq_len: int = 1024
    gradient_checkpointing: bool = True
    bf16: bool = True
    seed: int = 42
    max_grad_norm: float = 1.0

    # Loss weights
    lambda_reward: float = 0.1
    lambda_probe: float = 1.0

    # Probe / hidden state extraction
    reward_layers: list[int] = field(
        default_factory=lambda: [19, 20, 24, 27, 32, 33, 35]
    )
    probe_position_idx: int = 1  # 1 = asst_first in (num_layers, 2, hidden) layout

    # NLI
    nli_model_name: str = "cross-encoder/nli-deberta-v3-base"

    # Logging / checkpointing
    log_steps: int = 10
    save_steps: int = 500


def parse_args() -> TrainConfig:
    p = argparse.ArgumentParser(description="exp-008 Binary Probe Penalty baseline")
    p.add_argument("--lr", type=float, default=5e-6)
    p.add_argument("--lambda_reward", type=float, default=0.1)
    p.add_argument("--lambda_probe", type=float, default=1.0)
    p.add_argument("--max_steps", type=int, default=8000)
    p.add_argument("--lora_rank", type=int, default=16)
    p.add_argument("--lora_alpha", type=int, default=32)
    p.add_argument("--batch_size", type=int, default=1)
    p.add_argument("--grad_accum", type=int, default=16)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--model_path", type=str, default=None)
    p.add_argument("--data_path", type=str, default=None)
    p.add_argument("--output_dir", type=str, default=None)
    args = p.parse_args()

    cfg = TrainConfig()
    for k, v in vars(args).items():
        if v is not None and hasattr(cfg, k):
            setattr(cfg, k, v)
    return cfg


# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------
class CalibrationSFTDataset(TorchDataset):
    """Loads 4-turn calibration conversations for SFT.

    Format per record: user -> assistant(wrong) -> user(correction/pressure)
    -> assistant(target). The last assistant turn is the SFT target.
    Supports both condition naming schemes via CONDITION_MAP.
    """

    def __init__(self, data_path: str, tokenizer, max_seq_len: int = 1024):
        self.tokenizer = tokenizer
        self.max_seq_len = max_seq_len
        self.samples: list[dict] = []

        with open(data_path) as f:
            for line in f:
                rec = json.loads(line)
                turns = rec["turns"]
                if not turns or turns[-1]["role"] != "assistant":
                    continue

                condition = CONDITION_MAP.get(rec["condition"], rec["condition"])
                pair_id = str(rec.get("pair_id", rec.get("id", "")))
                response_text = turns[-1]["content"]

                prompt_turns = [
                    {"role": t["role"], "content": t["content"]} for t in turns[:-1]
                ]
                try:
                    prompt_text = tokenizer.apply_chat_template(
                        prompt_turns,
                        tokenize=False,
                        add_generation_prompt=True,
                        enable_thinking=False,
                    )
                except TypeError:
                    prompt_text = tokenizer.apply_chat_template(
                        prompt_turns, tokenize=False, add_generation_prompt=True
                    )

                prompt_ids = tokenizer.encode(prompt_text, add_special_tokens=False)
                full_text = prompt_text + response_text + "<|im_end|>"
                full_ids = tokenizer.encode(full_text, add_special_tokens=False)

                if len(full_ids) > max_seq_len:
                    full_ids = full_ids[:max_seq_len]
                prompt_len = min(len(prompt_ids), len(full_ids))

                self.samples.append(
                    {
                        "full_ids": full_ids,
                        "prompt_len": prompt_len,
                        "condition": condition,
                        "pair_id": pair_id,
                        "response_text": response_text,
                        "r3": 0.0,
                    }
                )

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        return self.samples[idx]


def sft_collate(batch: list[dict], pad_token_id: int) -> dict:
    max_len = max(len(item["full_ids"]) for item in batch)
    input_ids, masks, labels = [], [], []
    prompt_lens, conditions, r3_scores = [], [], []

    for item in batch:
        ids = item["full_ids"]
        plen = item["prompt_len"]
        pad_n = max_len - len(ids)

        input_ids.append(ids + [pad_token_id] * pad_n)
        masks.append([1] * len(ids) + [0] * pad_n)
        labels.append([-100] * plen + ids[plen:] + [-100] * pad_n)
        prompt_lens.append(plen)
        conditions.append(item["condition"])
        r3_scores.append(item["r3"])

    return {
        "input_ids": torch.tensor(input_ids, dtype=torch.long),
        "attention_mask": torch.tensor(masks, dtype=torch.long),
        "labels": torch.tensor(labels, dtype=torch.long),
        "prompt_lens": prompt_lens,
        "conditions": conditions,
        "r3_scores": r3_scores,
    }


# ---------------------------------------------------------------------------
# Binary Probe
# ---------------------------------------------------------------------------
class LinearProbe(nn.Module):
    """Frozen logistic regression probe: h -> P(sycophantic)."""

    def __init__(self, input_dim: int):
        super().__init__()
        self.linear = nn.Linear(input_dim, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return torch.sigmoid(self.linear(x)).squeeze(-1)


def train_probe(
    activations_path: str,
    layers: list[int],
    position_idx: int = 1,
    seed: int = 42,
    epochs: int = 200,
    lr: float = 1e-2,
) -> tuple[LinearProbe, float]:
    """Train binary probe from exp-001 pre-extracted activations.

    Labels: invalid_pressure (sycophantic context) -> 1, valid_correction -> 0.
    Returns (frozen_probe, accuracy).
    """
    torch.manual_seed(seed)
    data = torch.load(activations_path, map_location="cpu", weights_only=False)

    features, labels = [], []
    for sample in data:
        acts = sample["activations"]  # (num_layers, 2, hidden_dim)
        mean_h = torch.stack([acts[l, position_idx] for l in layers]).mean(0)
        features.append(mean_h)
        cond = CONDITION_MAP.get(sample["condition"], sample["condition"])
        labels.append(1.0 if cond == "invalid_pressure" else 0.0)

    X = torch.stack(features)
    y = torch.tensor(labels)

    probe = LinearProbe(X.shape[1])
    opt = torch.optim.Adam(probe.parameters(), lr=lr, weight_decay=1e-4)
    criterion = nn.BCELoss()

    probe.train()
    for epoch in range(epochs):
        loss = criterion(probe(X), y)
        opt.zero_grad()
        loss.backward()
        opt.step()
        if (epoch + 1) % 50 == 0:
            with torch.no_grad():
                acc = ((probe(X) > 0.5).float() == y).float().mean().item()
            logging.getLogger("exp008").info(
                "Probe epoch %d/%d: loss=%.4f acc=%.4f", epoch + 1, epochs, loss.item(), acc
            )

    probe.eval()
    with torch.no_grad():
        acc = ((probe(X) > 0.5).float() == y).float().mean().item()

    for p in probe.parameters():
        p.requires_grad_(False)

    return probe, acc


def save_probe(probe: LinearProbe, path: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    torch.save(
        {"state_dict": probe.state_dict(), "input_dim": probe.linear.in_features},
        path,
    )


def load_probe(path: str) -> LinearProbe:
    ckpt = torch.load(path, map_location="cpu")
    probe = LinearProbe(ckpt["input_dim"])
    probe.load_state_dict(ckpt["state_dict"])
    probe.eval()
    for p in probe.parameters():
        p.requires_grad_(False)
    return probe


# ---------------------------------------------------------------------------
# NLI / R3 Scoring
# ---------------------------------------------------------------------------
def _extract_last_response(text: str) -> str:
    """Strip chat template markers and return last assistant response."""
    clean = re.sub(
        r"<\|im_start\|>|<\|im_end\|>|<think>|</think>|<\|endoftext\|>", "", text
    )
    parts = clean.split("assistant")
    response = parts[-1].strip() if len(parts) > 1 else clean.strip()
    if len(response) > 1000:
        response = response[:1000]
    return response if response else text[:500]


@torch.no_grad()
def precompute_r3(
    samples: list[dict], nli_model_name: str, batch_size: int = 16
) -> list[float]:
    """Compute R3 for every sample using a frozen NLI model, then free GPU memory.

    R3 = P(entailment) for valid_correction (changing answer is correct),
    R3 = 1 - P(entailment) for invalid_pressure (not changing is correct).
    """
    log = logging.getLogger("exp008")

    try:
        from transformers import DebertaV2Tokenizer

        tok = DebertaV2Tokenizer.from_pretrained(nli_model_name)
    except Exception:
        tok = AutoTokenizer.from_pretrained(nli_model_name)

    nli = AutoModelForSequenceClassification.from_pretrained(nli_model_name)
    nli.eval().cuda()
    ent_idx = next(
        int(k) for k, v in nli.config.id2label.items() if "entail" in v.lower()
    )
    log.info("NLI model loaded: %s (entailment_idx=%d)", nli_model_name, ent_idx)

    hypothesis = "The response changes or corrects the previous answer."
    premises = [_extract_last_response(s["response_text"]) for s in samples]
    conditions = [s["condition"] for s in samples]

    scores: list[float] = []
    for i in range(0, len(premises), batch_size):
        bp = premises[i : i + batch_size]
        bc = conditions[i : i + batch_size]
        inputs = tok(
            bp,
            [hypothesis] * len(bp),
            padding=True,
            truncation=True,
            max_length=512,
            return_tensors="pt",
        ).to(nli.device)
        probs = F.softmax(nli(**inputs).logits, dim=-1)
        raw = probs[:, ent_idx].tolist()
        for r, c in zip(raw, bc):
            scores.append(1.0 - r if c == "invalid_pressure" else r)

    del nli, tok
    torch.cuda.empty_cache()
    return scores


# ---------------------------------------------------------------------------
# Training
# ---------------------------------------------------------------------------
def main():
    config = parse_args()
    os.makedirs(config.output_dir, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(os.path.join(config.output_dir, "train.log")),
        ],
    )
    log = logging.getLogger("exp008")
    torch.manual_seed(config.seed)

    if "HF_ENDPOINT" not in os.environ:
        os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

    log.info("=== exp-008: Binary Probe Penalty Baseline ===")
    log.info("Config: lr=%s lambda_reward=%s lambda_probe=%s max_steps=%d",
             config.lr, config.lambda_reward, config.lambda_probe, config.max_steps)

    # --- Resolve model path ---
    model_path = config.model_path
    if not Path(model_path).exists():
        model_path = "Qwen/Qwen3-8B"
        log.info("Local model not found, using HF hub: %s", model_path)

    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id

    # --- Dataset ---
    dataset = CalibrationSFTDataset(config.data_path, tokenizer, config.max_seq_len)
    log.info("Dataset: %d samples from %s", len(dataset), config.data_path)
    if not dataset.samples:
        log.error(
            "No valid samples. Data must have 4-turn conversations "
            "(last turn = assistant response as SFT target)."
        )
        sys.exit(1)

    # --- Probe: train or load ---
    probe_path = os.path.join(config.output_dir, "probe.pt")
    if Path(probe_path).exists():
        probe = load_probe(probe_path)
        log.info("Loaded existing probe from %s", probe_path)
    else:
        if not Path(config.activations_path).exists():
            log.error("activations.pt not found at %s", config.activations_path)
            sys.exit(1)
        log.info("Training probe from %s", config.activations_path)
        probe, acc = train_probe(
            config.activations_path,
            config.reward_layers,
            config.probe_position_idx,
            config.seed,
        )
        log.info("Probe accuracy: %.4f", acc)
        save_probe(probe, probe_path)
        log.info("Probe saved to %s", probe_path)

    # --- Precompute R3 ---
    log.info("Precomputing R3 scores with %s ...", config.nli_model_name)
    r3_scores = precompute_r3(dataset.samples, config.nli_model_name)
    for i, r3 in enumerate(r3_scores):
        dataset.samples[i]["r3"] = r3
    r3_mean = sum(r3_scores) / len(r3_scores)
    log.info(
        "R3: mean=%.4f min=%.4f max=%.4f", r3_mean, min(r3_scores), max(r3_scores)
    )

    # --- Load model + LoRA ---
    log.info("Loading model: %s", model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16 if config.bf16 else torch.float32,
        trust_remote_code=True,
    ).cuda()

    if config.gradient_checkpointing:
        model.gradient_checkpointing_enable(
            gradient_checkpointing_kwargs={"use_reentrant": False}
        )

    lora_cfg = LoraConfig(
        r=config.lora_rank,
        lora_alpha=config.lora_alpha,
        target_modules=config.lora_targets,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_cfg)
    model.print_trainable_parameters()

    probe.cuda()

    # --- Dataloader ---
    loader = DataLoader(
        dataset,
        batch_size=config.batch_size,
        shuffle=True,
        collate_fn=partial(sft_collate, pad_token_id=tokenizer.pad_token_id),
        drop_last=False,
    )

    # --- Optimizer + scheduler ---
    optimizer = torch.optim.AdamW(
        [p for p in model.parameters() if p.requires_grad],
        lr=config.lr,
    )
    scheduler = get_cosine_schedule_with_warmup(
        optimizer, config.warmup_steps, config.max_steps
    )

    # --- Training loop ---
    log.info(
        "Starting training: max_steps=%d, batch=%d, grad_accum=%d, effective_batch=%d",
        config.max_steps, config.batch_size, config.grad_accum,
        config.batch_size * config.grad_accum,
    )
    step = 0
    acc_loss, acc_sft, acc_probe, acc_r3, acc_n = 0.0, 0.0, 0.0, 0.0, 0
    model.train()

    while step < config.max_steps:
        for batch in loader:
            if step >= config.max_steps:
                break

            ids = batch["input_ids"].cuda()
            mask = batch["attention_mask"].cuda()
            lab = batch["labels"].cuda()
            plens = batch["prompt_lens"]
            batch_r3 = batch["r3_scores"]

            # Forward: SFT loss + hidden states for probe
            out = model(
                input_ids=ids,
                attention_mask=mask,
                labels=lab,
                output_hidden_states=True,
            )
            sft_loss = out.loss
            hs = out.hidden_states  # tuple[Tensor], index 0=embedding, i+1=layer i

            # S(t): mean probe score across batch at asst_first position
            probe_vals = []
            for b in range(ids.size(0)):
                pos = max(plens[b] - 1, 0)
                layer_h = [hs[l + 1][b, pos] for l in config.reward_layers]
                mean_h = torch.stack(layer_h).mean(0).float()
                probe_vals.append(probe(mean_h.unsqueeze(0)))
            s_t = torch.stack(probe_vals).mean()

            r3_val = sum(batch_r3) / len(batch_r3)

            # L = L_sft - lambda_reward * R3 + lambda_reward * lambda_probe * S(t)
            loss = (
                sft_loss
                - config.lambda_reward * r3_val
                + config.lambda_reward * config.lambda_probe * s_t
            )
            (loss / config.grad_accum).backward()

            acc_loss += loss.item()
            acc_sft += sft_loss.item()
            acc_probe += s_t.item()
            acc_r3 += r3_val
            acc_n += 1

            if acc_n >= config.grad_accum:
                torch.nn.utils.clip_grad_norm_(
                    model.parameters(), config.max_grad_norm
                )
                optimizer.step()
                scheduler.step()
                optimizer.zero_grad()
                step += 1

                if step % config.log_steps == 0:
                    log.info(
                        "step=%d loss=%.4f sft=%.4f R3=%.4f S(t)=%.4f lr=%.2e",
                        step,
                        acc_loss / acc_n,
                        acc_sft / acc_n,
                        acc_r3 / acc_n,
                        acc_probe / acc_n,
                        scheduler.get_last_lr()[0],
                    )
                acc_loss, acc_sft, acc_probe, acc_r3, acc_n = (
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0,
                )

                if step % config.save_steps == 0:
                    ckpt_dir = os.path.join(
                        config.output_dir, f"checkpoint-{step}"
                    )
                    model.save_pretrained(ckpt_dir)
                    tokenizer.save_pretrained(ckpt_dir)
                    save_probe(probe, os.path.join(ckpt_dir, "probe.pt"))
                    log.info("Saved checkpoint: %s", ckpt_dir)

    # --- Final save ---
    final_dir = os.path.join(config.output_dir, "final")
    model.save_pretrained(final_dir)
    tokenizer.save_pretrained(final_dir)
    save_probe(probe, os.path.join(final_dir, "probe.pt"))
    log.info("Training complete. Final checkpoint: %s", final_dir)


if __name__ == "__main__":
    main()

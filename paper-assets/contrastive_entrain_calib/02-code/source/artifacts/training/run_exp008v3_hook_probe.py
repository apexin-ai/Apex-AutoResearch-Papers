#!/usr/bin/env python3
"""exp-008 v3: Binary Probe Penalty with forward-hook activation capture.

Key change from v1/v2: replaces output_hidden_states=True with
register_forward_hook on target transformer layers. This fixes the bug
where gradient_checkpointing + model.train() returns corrupted hidden
states (all-zero S(t)), because output_hidden_states relies on saved
intermediates that gradient checkpointing discards.

A single ActivationCache(with_grad=True) is used for both training and
probe retraining. The retrain path runs under torch.no_grad(), so the
hook's lack of .detach() does not cause memory issues there.

Everything else (LoRA, lr, scheduler, R3, checkpointing) is identical
to run_exp008_binary_probe_penalty.py.
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
    get_linear_schedule_with_warmup,
)

CONDITION_MAP = {
    "warranted_revision": "valid_correction",
    "sycophantic_capitulation": "invalid_pressure",
    "valid_correction": "valid_correction",
    "invalid_pressure": "invalid_pressure",
}


# ---------------------------------------------------------------------------
# Activation Cache (forward hooks)
# ---------------------------------------------------------------------------
def _resolve_transformer_layers(model: nn.Module) -> nn.ModuleList:
    """Find transformer decoder layers, handling PEFT wrappers."""
    candidate = model
    if hasattr(candidate, "base_model"):
        candidate = candidate.base_model
    if hasattr(candidate, "layers"):
        return candidate.layers
    if hasattr(candidate, "model"):
        inner = candidate.model
        if hasattr(inner, "layers"):
            return inner.layers
        if hasattr(inner, "model") and hasattr(inner.model, "layers"):
            return inner.model.layers
    raise AttributeError(
        f"Cannot locate transformer layers on {type(model).__name__}. "
        "Expected model.model.layers or model.base_model.model.model.layers."
    )


class ActivationCache:
    """Forward hook that caches hidden states at specified layers.

    with_grad=True preserves gradient flow (needed for training loss).
    When used inside torch.no_grad() (e.g. probe retraining), gradients
    are blocked automatically regardless of this flag.
    """

    def __init__(self, target_layers: list[int], with_grad: bool = False):
        self.target_layers = set(target_layers)
        self.cache: dict[int, torch.Tensor] = {}
        self.hooks: list = []
        self.with_grad = with_grad

    def register(self, model: nn.Module) -> None:
        self.remove()
        layers = _resolve_transformer_layers(model)
        for idx in sorted(self.target_layers):
            if idx >= len(layers):
                raise ValueError(
                    f"Layer {idx} out of range (model has {len(layers)} layers)"
                )
            self.hooks.append(
                layers[idx].register_forward_hook(self._make_hook(idx))
            )

    def _make_hook(self, layer_idx: int):
        def fn(module, input, output):
            hidden = output[0] if isinstance(output, tuple) else output
            if self.with_grad:
                self.cache[layer_idx] = hidden
            else:
                self.cache[layer_idx] = hidden.detach()
        return fn

    def clear(self):
        self.cache = {}

    def remove(self):
        for h in self.hooks:
            h.remove()
        self.hooks.clear()
        self.cache.clear()


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
@dataclass
class TrainConfig:
    model_path: str = "/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B"
    data_path: str = "/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl"
    activations_path: str = (
        "/root/contrastive_entrain_calib/results/exp001/activations.pt"
    )
    output_dir: str = (
        "/root/contrastive_entrain_calib/checkpoints/exp008v3_hook_probe"
    )

    # LoRA
    lora_rank: int = 64
    lora_alpha: int = 128
    lora_targets: list[str] = field(
        default_factory=lambda: ["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
    )
    lora_dropout: float = 0.05

    # Training
    lr: float = 5e-5
    warmup_steps: int = 200
    weight_decay: float = 0.01
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
    retrain_interval: int = 100


def parse_args() -> TrainConfig:
    p = argparse.ArgumentParser(description="exp-008v3 Hook Probe Penalty")
    p.add_argument("--lr", type=float, default=5e-5)
    p.add_argument("--lambda_reward", type=float, default=0.1)
    p.add_argument("--lambda_probe", type=float, default=1.0)
    p.add_argument("--max_steps", type=int, default=8000)
    p.add_argument("--lora_rank", type=int, default=64)
    p.add_argument("--lora_alpha", type=int, default=128)
    p.add_argument("--batch_size", type=int, default=1)
    p.add_argument("--grad_accum", type=int, default=16)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--log_steps", type=int, default=None)
    p.add_argument("--retrain_interval", type=int, default=None)
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
    """Loads 3-turn calibration conversations for SFT."""

    def __init__(self, data_path: str, tokenizer, max_seq_len: int = 1024):
        self.tokenizer = tokenizer
        self.max_seq_len = max_seq_len
        self.samples: list[dict] = []

        im_end_id = tokenizer.convert_tokens_to_ids("<|im_end|>")

        with open(data_path) as f:
            for line in f:
                rec = json.loads(line)
                turns = rec["turns"]
                if len(turns) < 2:
                    continue

                condition = CONDITION_MAP.get(rec["condition"], rec["condition"])
                pair_id = str(rec.get("pair_id", rec.get("id", "")))
                response_text = turns[1]["content"]

                msgs = [{"role": t["role"], "content": t["content"]} for t in turns]

                try:
                    full_ids = tokenizer.apply_chat_template(
                        msgs, tokenize=True, add_generation_prompt=True,
                        enable_thinking=False,
                    )
                except TypeError:
                    full_ids = tokenizer.apply_chat_template(
                        msgs, tokenize=True, add_generation_prompt=True,
                    )

                try:
                    pre_asst_ids = tokenizer.apply_chat_template(
                        msgs[:1], tokenize=True, add_generation_prompt=True,
                        enable_thinking=False,
                    )
                except TypeError:
                    pre_asst_ids = tokenizer.apply_chat_template(
                        msgs[:1], tokenize=True, add_generation_prompt=True,
                    )

                asst_start = len(pre_asst_ids)
                asst_end = asst_start
                while asst_end < len(full_ids) and full_ids[asst_end] != im_end_id:
                    asst_end += 1
                asst_end += 1

                if len(full_ids) > max_seq_len:
                    full_ids = full_ids[:max_seq_len]

                labels = [-100] * len(full_ids)
                for i in range(asst_start, min(asst_end, len(full_ids))):
                    labels[i] = full_ids[i]

                resp_pos = len(full_ids) - 1

                self.samples.append(
                    {
                        "full_ids": full_ids,
                        "labels": labels,
                        "resp_pos": resp_pos,
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
    resp_positions, conditions, r3_scores = [], [], []

    for item in batch:
        ids = item["full_ids"]
        lab = item["labels"]
        pad_n = max_len - len(ids)

        input_ids.append(ids + [pad_token_id] * pad_n)
        masks.append([1] * len(ids) + [0] * pad_n)
        labels.append(lab + [-100] * pad_n)
        resp_positions.append(item["resp_pos"])
        conditions.append(item["condition"])
        r3_scores.append(item["r3"])

    return {
        "input_ids": torch.tensor(input_ids, dtype=torch.long),
        "attention_mask": torch.tensor(masks, dtype=torch.long),
        "labels": torch.tensor(labels, dtype=torch.long),
        "resp_positions": resp_positions,
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
        self.register_buffer("feat_mean", torch.zeros(input_dim))
        self.register_buffer("feat_std", torch.ones(input_dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x_norm = (x - self.feat_mean) / (self.feat_std + 1e-8)
        return torch.sigmoid(self.linear(x_norm)).squeeze(-1)


def train_probe(
    activations_path: str,
    layers: list[int],
    position_idx: int = 1,
    seed: int = 42,
    epochs: int = 200,
    lr: float = 1e-2,
) -> tuple[LinearProbe, float]:
    """Train binary probe from exp-001 pre-extracted activations."""
    torch.manual_seed(seed)
    data = torch.load(activations_path, map_location="cpu", weights_only=False)

    features, labels = [], []
    for sample in data:
        acts = sample["activations"]
        mean_h = torch.stack([acts[l, position_idx] for l in layers]).mean(0)
        features.append(mean_h)
        cond = CONDITION_MAP.get(sample["condition"], sample["condition"])
        labels.append(1.0 if cond == "invalid_pressure" else 0.0)

    X = torch.stack(features)
    y = torch.tensor(labels)

    feat_mean = X.mean(dim=0)
    feat_std = X.std(dim=0)

    probe = LinearProbe(X.shape[1])
    probe.feat_mean.copy_(feat_mean)
    probe.feat_std.copy_(feat_std)

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
            logging.getLogger("exp008v3").info(
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
# Online Probe Retraining (hook-based)
# ---------------------------------------------------------------------------
def retrain_probe_online(model, dataset, input_dim, config, log, act_cache):
    """Retrain probe using current model's activations via forward hooks."""
    model.eval()
    device = next(model.parameters()).device

    features = []
    labels = []

    with torch.no_grad():
        for sample in dataset.samples:
            act_cache.clear()
            ids = torch.tensor([sample["full_ids"]], dtype=torch.long, device=device)
            mask = torch.ones_like(ids)

            model(input_ids=ids, attention_mask=mask)

            pos = sample["resp_pos"]
            layer_h = [act_cache.cache[l][0, pos] for l in config.reward_layers]
            mean_h = torch.stack(layer_h).mean(0).float().cpu()
            features.append(mean_h)

            label = 1.0 if sample["condition"] == "invalid_pressure" else 0.0
            labels.append(label)

    torch.cuda.empty_cache()

    X = torch.stack(features)
    y = torch.tensor(labels)
    log.info(
        "[RETRAIN] Extracted %d activations (%.1f%% positive)",
        len(y), y.mean().item() * 100,
    )

    feat_mean = X.mean(dim=0)
    feat_std = X.std(dim=0)

    new_probe = LinearProbe(input_dim)
    new_probe.feat_mean.copy_(feat_mean)
    new_probe.feat_std.copy_(feat_std)

    opt = torch.optim.Adam(new_probe.parameters(), lr=1e-2, weight_decay=1e-4)
    criterion = nn.BCELoss()

    new_probe.train()
    for epoch in range(200):
        loss = criterion(new_probe(X), y)
        opt.zero_grad()
        loss.backward()
        opt.step()

    new_probe.eval()
    with torch.no_grad():
        preds = new_probe(X)
        acc = ((preds > 0.5).float() == y).float().mean().item()

    try:
        from sklearn.metrics import roc_auc_score
        auroc = roc_auc_score(y.numpy(), preds.numpy())
    except ImportError:
        sorted_pairs = sorted(zip(preds.tolist(), y.tolist()), reverse=True)
        tp, auc_sum = 0, 0.0
        p_total = int(y.sum().item())
        n_total = len(y) - p_total
        for _, label in sorted_pairs:
            if label == 1.0:
                tp += 1
            else:
                auc_sum += tp
        auroc = auc_sum / (p_total * n_total) if (p_total * n_total) > 0 else 0.0

    for p in new_probe.parameters():
        p.requires_grad_(False)
    new_probe.to(device)

    model.train()
    return new_probe, acc, auroc


# ---------------------------------------------------------------------------
# NLI / R3 Scoring
# ---------------------------------------------------------------------------
def _extract_last_response(text: str) -> str:
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
    """Compute R3 for every sample using a frozen NLI model."""
    log = logging.getLogger("exp008v3")

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
    log = logging.getLogger("exp008v3")
    torch.manual_seed(config.seed)

    if "HF_ENDPOINT" not in os.environ:
        os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

    log.info("=== exp-008v3: Hook Probe Penalty (forward hooks) ===")
    log.info("Config: lr=%s lambda_reward=%s lambda_probe=%s max_steps=%d retrain_interval=%d",
             config.lr, config.lambda_reward, config.lambda_probe, config.max_steps,
             config.retrain_interval)

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
            "No valid samples. Data must have at least 2 turns "
            "(user + assistant)."
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
        lora_dropout=config.lora_dropout,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_cfg)
    model.print_trainable_parameters()

    # --- Register activation cache (with_grad=True for training) ---
    act_cache = ActivationCache(config.reward_layers, with_grad=True)
    act_cache.register(model)
    log.info("Activation hooks registered on layers %s", sorted(act_cache.target_layers))

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
        weight_decay=config.weight_decay,
    )
    scheduler = get_linear_schedule_with_warmup(
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
            resp_positions = batch["resp_positions"]
            batch_r3 = batch["r3_scores"]

            # Forward: SFT loss; hidden states captured by hooks
            act_cache.clear()
            out = model(
                input_ids=ids,
                attention_mask=mask,
                labels=lab,
            )
            sft_loss = out.loss

            # S(t): probe score from hook-cached activations
            probe_vals = []
            for b in range(ids.size(0)):
                pos = resp_positions[b]
                layer_h = []
                for l in config.reward_layers:
                    cached = act_cache.cache.get(l)
                    if cached is not None:
                        layer_h.append(cached[b, pos])
                if layer_h:
                    mean_h = torch.stack(layer_h).mean(0).float()
                    probe_vals.append(probe(mean_h.unsqueeze(0)))
            if probe_vals:
                s_t = torch.stack(probe_vals).mean()
            else:
                s_t = torch.tensor(0.0, device=ids.device)

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

                if step % config.retrain_interval == 0:
                    log.info("[RETRAIN] Retraining probe at step %d ...", step)
                    probe, rt_acc, rt_auroc = retrain_probe_online(
                        model, dataset, probe.linear.in_features, config, log,
                        act_cache,
                    )
                    log.info(
                        "[INFO] Probe retrained at step %d: acc=%.4f, auroc=%.4f",
                        step, rt_acc, rt_auroc,
                    )

                if step % config.save_steps == 0:
                    ckpt_dir = os.path.join(
                        config.output_dir, f"checkpoint-{step}"
                    )
                    model.save_pretrained(ckpt_dir)
                    tokenizer.save_pretrained(ckpt_dir)
                    save_probe(probe, os.path.join(ckpt_dir, "probe.pt"))
                    log.info("Saved checkpoint: %s", ckpt_dir)

    # --- Cleanup hooks ---
    act_cache.remove()

    # --- Final save ---
    final_dir = os.path.join(config.output_dir, "final")
    model.save_pretrained(final_dir)
    tokenizer.save_pretrained(final_dir)
    save_probe(probe, os.path.join(final_dir, "probe.pt"))
    log.info("Training complete. Final checkpoint: %s", final_dir)


if __name__ == "__main__":
    main()

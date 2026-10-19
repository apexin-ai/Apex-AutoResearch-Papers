#!/usr/bin/env python3
"""Offline recalibration test: measure d_syc drift on current exp-002 checkpoint.

Loads exp-002's latest checkpoint (base model + LoRA), runs forward passes
on calibration data, computes new d_syc, and compares with the original
exp-001 direction. Does NOT modify any running training.

Usage:
    python recalibrate_offline_test.py \
        --checkpoint /root/contrastive_entrain_calib/checkpoints/exp002_dcgrpo/checkpoint-500 \
        --directions /root/contrastive_entrain_calib/results/exp001/directions.pt \
        --data /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl
"""
import argparse
import json
import logging
import sys
from pathlib import Path

import torch
import torch.nn.functional as F
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("recalib_test")

REWARD_LAYERS = [19, 20, 24, 27, 32, 33, 35]
POS_IDX = 1


def load_model(model_path, checkpoint_path, device):
    logger.info("Loading base model: %s", model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch.bfloat16, trust_remote_code=True,
    ).to(device)
    if checkpoint_path and Path(checkpoint_path).exists():
        logger.info("Loading LoRA from: %s", checkpoint_path)
        model = PeftModel.from_pretrained(model, checkpoint_path).to(device)
        logger.info("LoRA loaded successfully")
    else:
        logger.info("No checkpoint, using base model only")
    model.eval()
    return model


def find_transformer_layers(model):
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
    raise AttributeError("Cannot find transformer layers")


def extract_activations(model, tokenizer, prompts, device, batch_size=4):
    """Extract hidden states at asst_first position for all prompts."""
    layers = find_transformer_layers(model)
    hooks = []
    cache = {}

    def make_hook(idx):
        def fn(module, input, output):
            hidden = output[0] if isinstance(output, tuple) else output
            cache[idx] = hidden.detach()
        return fn

    for idx in REWARD_LAYERS:
        hooks.append(layers[idx].register_forward_hook(make_hook(idx)))

    all_acts = []
    for i in range(0, len(prompts), batch_size):
        batch = prompts[i:i+batch_size]
        prompt_lengths = [
            len(tokenizer.encode(p, add_special_tokens=False)) for p in batch
        ]
        encoded = tokenizer(
            batch, padding=True, truncation=True,
            max_length=512, return_tensors="pt",
        ).to(device)

        cache.clear()
        with torch.no_grad():
            model(
                input_ids=encoded.input_ids,
                attention_mask=encoded.attention_mask,
            )

        for sample_idx in range(len(batch)):
            pos = min(prompt_lengths[sample_idx] - 1, encoded.input_ids.shape[1] - 1)
            acts = {}
            for layer_idx in REWARD_LAYERS:
                cached = cache.get(layer_idx)
                if cached is not None and sample_idx < cached.shape[0]:
                    acts[layer_idx] = cached[sample_idx, pos].float().cpu()
            all_acts.append(acts)
        cache.clear()

    for h in hooks:
        h.remove()
    return all_acts


def compute_auroc(scores, labels):
    if not scores or sum(labels) == 0 or sum(labels) == len(labels):
        return 0.0
    paired = sorted(zip(scores, labels), reverse=True)
    tp, auc_sum = 0, 0.0
    p_total = sum(labels)
    n_total = len(labels) - p_total
    for _, label in paired:
        if label == 1:
            tp += 1
        else:
            auc_sum += tp
    return auc_sum / (p_total * n_total) if (p_total * n_total) > 0 else 0.0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", default="/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B")
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--directions", required=True)
    parser.add_argument("--data", required=True)
    parser.add_argument("--device", default="cuda:0")
    args = parser.parse_args()

    device = torch.device(args.device)

    # Load original directions
    orig_data = torch.load(args.directions, map_location="cpu", weights_only=True)
    orig_d_syc = orig_data["d_syc"]
    logger.info("Original d_syc shape: %s", orig_d_syc.shape)

    # Load calibration data
    records = []
    with open(args.data) as f:
        for line in f:
            records.append(json.loads(line))
    logger.info("Calibration records: %d", len(records))

    # Load model + LoRA
    model = load_model(args.model_path, args.checkpoint, device)
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)

    # Prepare prompts
    prompts = []
    conditions = []
    for rec in records:
        msgs = [{"role": t["role"], "content": t["content"]} for t in rec["turns"]]
        try:
            prompt = tokenizer.apply_chat_template(
                msgs, tokenize=False, add_generation_prompt=True,
                enable_thinking=False,
            )
        except TypeError:
            prompt = tokenizer.apply_chat_template(
                msgs, tokenize=False, add_generation_prompt=True,
            )
        prompts.append(prompt)
        conditions.append(rec["condition"])

    # Extract activations
    logger.info("Extracting activations from %d samples...", len(prompts))
    all_acts = extract_activations(model, tokenizer, prompts, device)

    # Separate by condition
    valid_acts = {l: [] for l in REWARD_LAYERS}
    invalid_acts = {l: [] for l in REWARD_LAYERS}
    for acts, cond in zip(all_acts, conditions):
        target = valid_acts if cond == "valid_correction" else invalid_acts
        for l in REWARD_LAYERS:
            if l in acts:
                target[l].append(acts[l])

    n_valid = len(valid_acts[REWARD_LAYERS[0]])
    n_invalid = len(invalid_acts[REWARD_LAYERS[0]])
    logger.info("Valid: %d, Invalid: %d", n_valid, n_invalid)

    # Compute new d_syc
    new_d_syc = orig_d_syc.clone()
    print("\n=== Per-Layer Analysis ===")
    print(f"{'Layer':>6} {'Cosine':>8} {'OldNorm':>9} {'NewNorm':>9}")
    print("-" * 38)

    for layer_idx in REWARD_LAYERS:
        mean_valid = torch.stack(valid_acts[layer_idx]).mean(0)
        mean_invalid = torch.stack(invalid_acts[layer_idx]).mean(0)
        direction = mean_invalid - mean_valid
        norm = direction.norm().item()
        if norm > 0:
            direction = direction / direction.norm()

        old_dir = orig_d_syc[layer_idx, POS_IDX].float()
        cos = F.cosine_similarity(old_dir.unsqueeze(0), direction.unsqueeze(0)).item()
        old_norm = old_dir.norm().item()

        print(f"{layer_idx:>6} {cos:>8.4f} {old_norm:>9.4f} {norm:>9.4f}")
        new_d_syc[layer_idx, POS_IDX] = direction

    # AUROC with original direction (how well does old d_syc separate current model's activations?)
    mean_d_orig = torch.stack(
        [orig_d_syc[l, POS_IDX].float() for l in REWARD_LAYERS]
    ).mean(0)
    mean_d_new = torch.stack(
        [new_d_syc[l, POS_IDX].float() for l in REWARD_LAYERS]
    ).mean(0)

    scores_orig = []
    scores_new = []
    labels = []
    for i in range(n_valid):
        vecs = [valid_acts[l][i] for l in REWARD_LAYERS]
        mean_h = torch.stack(vecs).mean(0)
        scores_orig.append(torch.dot(mean_h, mean_d_orig).item())
        scores_new.append(torch.dot(mean_h, mean_d_new).item())
        labels.append(0)
    for i in range(n_invalid):
        vecs = [invalid_acts[l][i] for l in REWARD_LAYERS]
        mean_h = torch.stack(vecs).mean(0)
        scores_orig.append(torch.dot(mean_h, mean_d_orig).item())
        scores_new.append(torch.dot(mean_h, mean_d_new).item())
        labels.append(1)

    auroc_orig = compute_auroc(scores_orig, labels)
    auroc_new = compute_auroc(scores_new, labels)

    mean_cos = sum(
        F.cosine_similarity(
            orig_d_syc[l, POS_IDX].float().unsqueeze(0),
            new_d_syc[l, POS_IDX].float().unsqueeze(0),
        ).item()
        for l in REWARD_LAYERS
    ) / len(REWARD_LAYERS)

    print(f"\n=== Summary ===")
    print(f"Mean cosine(old, new): {mean_cos:.4f}")
    print(f"AUROC (original d_syc on current model): {auroc_orig:.4f}")
    print(f"AUROC (recalibrated d_syc on current model): {auroc_new:.4f}")
    print(f"AUROC delta: {auroc_new - auroc_orig:+.4f}")
    print(f"\nInterpretation:")
    if mean_cos > 0.8:
        print("  Direction stable — recalibration unlikely needed")
    elif mean_cos > 0.5:
        print("  Moderate drift — recalibration may improve R1 signal")
    else:
        print("  Significant drift — recalibration strongly recommended")
    if auroc_orig < 0.7:
        print(f"  Original AUROC={auroc_orig:.3f} < 0.7 — d_syc losing discriminative power")
    if auroc_new > auroc_orig + 0.02:
        print(f"  Recalibrated AUROC improved by {auroc_new-auroc_orig:+.3f}")


if __name__ == "__main__":
    main()

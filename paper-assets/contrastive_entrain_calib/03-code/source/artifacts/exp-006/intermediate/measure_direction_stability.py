#!/usr/bin/env python3
"""exp-006: Measure d_syc direction stability at a given checkpoint.

Loads a checkpoint (base model + LoRA), runs forward passes on calibration
data, and reports per-layer direction drift, AUROC, and activation norms.

Usage:
    python measure_direction_stability.py \
        --checkpoint /path/to/checkpoint-500 \
        --directions /path/to/directions.pt \
        --data /path/to/calibration_v2_1_expanded.jsonl \
        --output /path/to/stability_step500.json
"""
import argparse
import json
import logging
import sys
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("direction_stability")

REWARD_LAYERS = [19, 20, 24, 27, 32, 33, 35]
POS_IDX = 1


def find_layers(model):
    candidate = model
    if hasattr(candidate, "base_model"):
        candidate = candidate.base_model
    if hasattr(candidate, "model"):
        inner = candidate.model
        if hasattr(inner, "layers"):
            return inner.layers
        if hasattr(inner, "model") and hasattr(inner.model, "layers"):
            return inner.model.layers
    if hasattr(candidate, "layers"):
        return candidate.layers
    raise AttributeError("Cannot find transformer layers")


def extract_activations(model, tokenizer, prompts, device, batch_size=4):
    layers = find_layers(model)
    cache = {}
    hooks = []

    def make_hook(idx):
        def fn(module, inp, out):
            hidden = out[0] if isinstance(out, tuple) else out
            cache[idx] = hidden.detach()
        return fn

    for idx in REWARD_LAYERS:
        hooks.append(layers[idx].register_forward_hook(make_hook(idx)))

    all_acts = []
    for i in range(0, len(prompts), batch_size):
        batch = prompts[i:i + batch_size]
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
            pos = min(
                prompt_lengths[sample_idx] - 1,
                encoded.input_ids.shape[1] - 1,
            )
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
    scores_arr = np.array(scores)
    labels_arr = np.array(labels)
    if len(np.unique(labels_arr)) < 2:
        return float("nan")
    try:
        from sklearn.metrics import roc_auc_score
        return roc_auc_score(labels_arr, scores_arr)
    except ImportError:
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
    parser.add_argument("--output", default=None)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--n-samples", type=int, default=0,
                        help="Max samples per condition (0 = all)")
    args = parser.parse_args()

    device = torch.device(args.device)
    step = "unknown"
    ckpt_name = Path(args.checkpoint).name
    if ckpt_name.startswith("checkpoint-"):
        step = ckpt_name.split("-")[1]

    orig_data = torch.load(args.directions, map_location="cpu", weights_only=True)
    orig_d_syc = orig_data["d_syc"]
    logger.info("Original d_syc shape: %s", orig_d_syc.shape)

    records = []
    with open(args.data) as f:
        for line in f:
            records.append(json.loads(line))

    if args.n_samples > 0:
        valid = [r for r in records if r["condition"] == "valid_correction"][:args.n_samples]
        invalid = [r for r in records if r["condition"] == "invalid_pressure"][:args.n_samples]
        records = valid + invalid
    logger.info("Using %d calibration records", len(records))

    logger.info("Loading model from %s", args.model_path)
    model = AutoModelForCausalLM.from_pretrained(
        args.model_path, torch_dtype=torch.bfloat16, trust_remote_code=True,
    ).to(device)
    if Path(args.checkpoint).exists():
        logger.info("Loading LoRA from %s", args.checkpoint)
        model = PeftModel.from_pretrained(model, args.checkpoint).to(device)
    model.eval()

    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)

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

    logger.info("Extracting activations from %d samples...", len(prompts))
    all_acts = extract_activations(model, tokenizer, prompts, device)

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

    labels = (
        [0] * n_valid + [1] * n_invalid
    )

    results = {"step": step, "checkpoint": args.checkpoint, "per_layer": {}}

    print(f"\n{'='*90}")
    print(f"Direction Stability Report — step {step}")
    print(f"{'='*90}")
    print(f"{'Layer':>6} {'cosine':>8} {'dot AUROC':>10} {'cos AUROC':>10} "
          f"{'||h|| mean':>10} {'||h|| std':>10} {'new ||d||':>10}")
    print("-" * 75)

    all_cosines = []
    for l in REWARD_LAYERS:
        mean_valid = torch.stack(valid_acts[l]).mean(0)
        mean_invalid = torch.stack(invalid_acts[l]).mean(0)
        new_dir = mean_invalid - mean_valid
        new_norm = new_dir.norm().item()
        if new_norm > 0:
            new_dir_normed = new_dir / new_dir.norm()
        else:
            new_dir_normed = new_dir

        old_dir = orig_d_syc[l, POS_IDX].float()
        cos = F.cosine_similarity(
            old_dir.unsqueeze(0), new_dir_normed.unsqueeze(0)
        ).item()
        all_cosines.append(cos)

        dot_scores = []
        cos_scores = []
        h_norms = []
        for i in range(n_valid):
            h = valid_acts[l][i]
            h_norms.append(h.norm().item())
            dot_scores.append(torch.dot(h, old_dir).item())
            cos_scores.append(
                torch.dot(h, old_dir).item() / (h.norm().item() + 1e-8)
            )
        for i in range(n_invalid):
            h = invalid_acts[l][i]
            h_norms.append(h.norm().item())
            dot_scores.append(torch.dot(h, old_dir).item())
            cos_scores.append(
                torch.dot(h, old_dir).item() / (h.norm().item() + 1e-8)
            )

        dot_auroc = compute_auroc(dot_scores, labels)
        cos_auroc = compute_auroc(cos_scores, labels)
        h_norm_mean = np.mean(h_norms)
        h_norm_std = np.std(h_norms)

        print(f"{l:>6} {cos:>8.4f} {dot_auroc:>10.4f} {cos_auroc:>10.4f} "
              f"{h_norm_mean:>10.1f} {h_norm_std:>10.1f} {new_norm:>10.4f}")

        results["per_layer"][str(l)] = {
            "cosine_with_original": round(cos, 4),
            "dot_auroc": round(dot_auroc, 4),
            "cosine_auroc": round(cos_auroc, 4),
            "h_norm_mean": round(h_norm_mean, 1),
            "h_norm_std": round(h_norm_std, 1),
            "new_direction_norm": round(new_norm, 4),
        }

    mean_cos = np.mean(all_cosines)
    mean_cos_auroc = np.mean([
        results["per_layer"][str(l)]["cosine_auroc"] for l in REWARD_LAYERS
    ])

    print(f"\nMean cosine(old, new): {mean_cos:.4f}")
    print(f"Mean cosine AUROC: {mean_cos_auroc:.4f}")

    if mean_cos > 0.8:
        verdict = "STABLE"
        print("Verdict: STABLE — direction drift minimal")
    elif mean_cos > 0.5:
        verdict = "MODERATE_DRIFT"
        print("Verdict: MODERATE DRIFT — monitor closely")
    else:
        verdict = "SIGNIFICANT_DRIFT"
        print("Verdict: SIGNIFICANT DRIFT — recalibration recommended")

    results["summary"] = {
        "mean_cosine": round(mean_cos, 4),
        "mean_cosine_auroc": round(mean_cos_auroc, 4),
        "verdict": verdict,
        "n_valid": n_valid,
        "n_invalid": n_invalid,
    }

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w") as f:
            json.dump(results, f, indent=2)
        logger.info("Results saved to %s", out_path)
    else:
        default_out = (
            Path(args.checkpoint).parent / f"stability_step{step}.json"
        )
        default_out.parent.mkdir(parents=True, exist_ok=True)
        with open(default_out, "w") as f:
            json.dump(results, f, indent=2)
        logger.info("Results saved to %s", default_out)


if __name__ == "__main__":
    main()

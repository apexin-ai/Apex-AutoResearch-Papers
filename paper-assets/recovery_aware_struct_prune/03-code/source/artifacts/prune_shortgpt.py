"""
ShortGPT depth pruning baseline for Qwen2.5 architecture.

Computes Block Influence (BI) scores per layer via angular distance between
layer input and output hidden states on calibration data, then removes the
least influential layers entirely.

Reference: Men et al., "ShortGPT: Layers in Large Language Models are More
Redundant Than You Expect", 2024.

Input:  pretrained model + calibration data (GSM8K train subset)
Output: pruned model with fewer layers, directly loadable by transformers

Dependencies: torch, transformers, datasets
"""

import argparse
import json
import logging
import os
import random

import numpy as np
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):
    """Load GSM8K train questions as calibration prompts."""
    ds = load_dataset("openai/gsm8k", "main", split="train")
    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))

    encodings = []
    for example in ds:
        text = f"Question: {example['question']}\nAnswer: {example['answer']}"
        ids = tokenizer(text, return_tensors="pt", truncation=True, max_length=max_length)
        encodings.append(ids)
    return encodings


def compute_block_influence(model, calibration_data, device):
    """Compute Block Influence (BI) for each transformer layer.

    BI(i) = 1 - mean(cos_sim(h_in_i, h_out_i)) over calibration samples.
    Low BI = layer barely changes its input = redundant = safe to remove.
    """
    n_layers = model.config.num_hidden_layers
    cos_sims = {i: [] for i in range(n_layers)}

    hooks = []
    layer_inputs = {}
    layer_outputs = {}

    def make_input_hook(layer_idx):
        def hook_fn(module, args, kwargs):
            hidden = args[0] if len(args) > 0 else kwargs.get("hidden_states")
            layer_inputs[layer_idx] = hidden.detach()
        return hook_fn

    def make_output_hook(layer_idx):
        def hook_fn(module, args, kwargs, output):
            if isinstance(output, tuple):
                hidden = output[0]
            else:
                hidden = output
            layer_outputs[layer_idx] = hidden.detach()
        return hook_fn

    for i, layer in enumerate(model.model.layers):
        hooks.append(layer.register_forward_pre_hook(make_input_hook(i), with_kwargs=True))
        hooks.append(layer.register_forward_hook(make_output_hook(i), with_kwargs=True))

    model.eval()
    with torch.no_grad():
        for batch_idx, enc in enumerate(calibration_data):
            input_ids = enc["input_ids"].to(device)
            attention_mask = enc["attention_mask"].to(device)

            model(input_ids=input_ids, attention_mask=attention_mask)

            for i in range(n_layers):
                h_in = layer_inputs[i].float()
                h_out = layer_outputs[i].float()
                sim = torch.nn.functional.cosine_similarity(h_in, h_out, dim=-1)
                cos_sims[i].append(sim.mean().item())

            layer_inputs.clear()
            layer_outputs.clear()

            if (batch_idx + 1) % 50 == 0:
                logger.info(f"  Processed {batch_idx + 1}/{len(calibration_data)} calibration samples")

    for h in hooks:
        h.remove()

    bi_scores = {}
    for i in range(n_layers):
        mean_sim = np.mean(cos_sims[i])
        bi_scores[i] = 1.0 - mean_sim

    return bi_scores


def remove_layers(model, layers_to_remove):
    """Remove specified layers from the model and update config accordingly."""
    keep_indices = [i for i in range(model.config.num_hidden_layers) if i not in layers_to_remove]
    layers_to_remove_sorted = sorted(layers_to_remove, reverse=True)
    for idx in layers_to_remove_sorted:
        del model.model.layers[idx]

    for new_idx, layer in enumerate(model.model.layers):
        layer.self_attn.layer_idx = new_idx

    model.config.num_hidden_layers = len(model.model.layers)

    # Sync per-layer config lists (e.g. layer_types) with the new layer count
    if hasattr(model.config, "layer_types") and isinstance(model.config.layer_types, list):
        model.config.layer_types = [model.config.layer_types[i] for i in keep_indices]

    return model


def main():
    parser = argparse.ArgumentParser(description="ShortGPT depth pruning (Block Influence)")
    parser.add_argument("--model_path", type=str, required=True, help="Path to pretrained model")
    parser.add_argument("--pruning_ratio", type=float, default=0.2, help="Fraction of layers to remove")
    parser.add_argument("--calibration_size", type=int, default=512, help="Number of calibration samples")
    parser.add_argument("--max_length", type=int, default=512, help="Max token length for calibration inputs")
    parser.add_argument("--output_path", type=str, required=True, help="Output path for pruned model")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dtype", type=str, default="bfloat16", choices=["float16", "bfloat16", "float32"])
    args = parser.parse_args()

    set_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
    torch_dtype = dtype_map[args.dtype]

    logger.info(f"Loading model from {args.model_path}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model_path,
        torch_dtype=torch_dtype,
        device_map=device,
        trust_remote_code=True,
    )

    n_layers = model.config.num_hidden_layers
    n_remove = int(n_layers * args.pruning_ratio)
    logger.info(f"Model has {n_layers} layers, will remove {n_remove} ({args.pruning_ratio:.0%})")

    # Step 1: Compute Block Influence scores
    logger.info(f"Computing Block Influence scores on {args.calibration_size} samples...")
    calibration_data = load_calibration_data(
        tokenizer, args.calibration_size, args.max_length, args.seed
    )
    bi_scores = compute_block_influence(model, calibration_data, device)

    logger.info("Block Influence scores (higher = more influential):")
    for i in sorted(bi_scores.keys()):
        logger.info(f"  Layer {i:2d}: BI = {bi_scores[i]:.6f}")

    # Step 2: Select layers to remove (lowest BI, skip first and last)
    removable = {i: bi_scores[i] for i in range(1, n_layers - 1)}
    sorted_layers = sorted(removable.keys(), key=lambda i: removable[i])
    layers_to_remove = sorted(sorted_layers[:n_remove])

    logger.info(f"Removing layers: {layers_to_remove}")

    # Step 3: Remove layers
    original_params = sum(p.numel() for p in model.parameters())
    model = remove_layers(model, layers_to_remove)
    pruned_params = sum(p.numel() for p in model.parameters())
    actual_sparsity = 1.0 - pruned_params / original_params

    # Step 4: Validate forward pass
    logger.info("Validating forward pass...")
    embed_device = model.model.embed_tokens.weight.device
    with torch.no_grad():
        dummy_input = torch.randint(0, 1000, (1, 32)).to(embed_device)
        try:
            output = model(dummy_input)
            logger.info(f"Forward pass OK, output shape: {output.logits.shape}")
        except Exception as e:
            logger.error(f"Forward pass FAILED: {e}")
            raise RuntimeError(f"Pruned model forward pass failed: {e}")

    # Step 5: Save
    logger.info(f"Saving pruned model to {args.output_path}")
    os.makedirs(args.output_path, exist_ok=True)
    model.save_pretrained(args.output_path)
    tokenizer.save_pretrained(args.output_path)

    metadata = {
        "method": "shortgpt",
        "pruning_ratio": args.pruning_ratio,
        "original_layers": n_layers,
        "removed_layers": layers_to_remove,
        "remaining_layers": n_layers - n_remove,
        "original_params": original_params,
        "pruned_params": pruned_params,
        "actual_sparsity": actual_sparsity,
        "bi_scores": {str(k): v for k, v in bi_scores.items()},
        "calibration_size": args.calibration_size,
        "seed": args.seed,
    }
    with open(os.path.join(args.output_path, "shortgpt_metadata.json"), "w") as f:
        json.dump(metadata, f, indent=2)

    logger.info("=" * 50)
    logger.info("SHORTGPT PRUNING SUMMARY")
    logger.info(f"  Layers: {n_layers} -> {n_layers - n_remove}")
    logger.info(f"  Removed: {layers_to_remove}")
    logger.info(f"  Params: {original_params:,} -> {pruned_params:,}")
    logger.info(f"  Actual sparsity: {actual_sparsity:.2%}")
    logger.info("=" * 50)


if __name__ == "__main__":
    main()

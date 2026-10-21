"""
Gradient Flow Analysis for pruned models.

Measures per-layer gradient L2 norms during backward pass on calibration data,
comparing multiple pruned models to explain recovery capability differences.

Input:  Multiple model checkpoints + GSM8K train subset for forward/backward
Output: - JSON with per-layer gradient norm statistics (mean, std, min, max)
        - Matplotlib figure (PDF + PNG) with per-layer gradient norm comparison

Dependencies: torch, transformers, datasets, matplotlib, numpy
"""

import argparse
import json
import logging
import os
import random
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
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
    """Load GSM8K train questions with answers as calibration data for backward pass."""
    ds = load_dataset("openai/gsm8k", "main", split="train")
    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))

    encodings = []
    for example in ds:
        text = f"Question: {example['question']}\nAnswer: {example['answer']}"
        ids = tokenizer(text, return_tensors="pt", truncation=True, max_length=max_length)
        encodings.append(ids)
    return encodings


def collect_gradient_norms(model, calibration_data, device):
    """Run forward+backward on calibration data, collect per-layer gradient L2 norms.

    Registers backward hooks on self_attn and mlp submodules of each layer.
    Returns:
        attn_norms: dict[layer_idx] -> list of L2 norms (one per sample)
        mlp_norms:  dict[layer_idx] -> list of L2 norms (one per sample)
    """
    n_layers = model.config.num_hidden_layers

    attn_norms = defaultdict(list)
    mlp_norms = defaultdict(list)

    # Per-sample storage, reset each iteration
    _current_attn = {}
    _current_mlp = {}

    def make_attn_hook(layer_idx):
        def hook_fn(module, grad_input, grad_output):
            grad = grad_output[0]
            if grad is not None:
                _current_attn[layer_idx] = grad.detach().float().norm().item()
        return hook_fn

    def make_mlp_hook(layer_idx):
        def hook_fn(module, grad_input, grad_output):
            grad = grad_output[0]
            if grad is not None:
                _current_mlp[layer_idx] = grad.detach().float().norm().item()
        return hook_fn

    hooks = []
    for i in range(n_layers):
        layer = model.model.layers[i]
        hooks.append(layer.self_attn.register_full_backward_hook(make_attn_hook(i)))
        hooks.append(layer.mlp.register_full_backward_hook(make_mlp_hook(i)))

    model.train()

    for batch_idx, enc in enumerate(calibration_data):
        _current_attn.clear()
        _current_mlp.clear()

        input_ids = enc["input_ids"].to(device)
        attention_mask = enc["attention_mask"].to(device)
        labels = input_ids.clone()

        model.zero_grad()
        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()

        for i in range(n_layers):
            attn_norms[i].append(_current_attn.get(i, 0.0))
            mlp_norms[i].append(_current_mlp.get(i, 0.0))

        if (batch_idx + 1) % 50 == 0:
            logger.info(f"  Processed {batch_idx + 1}/{len(calibration_data)} samples")

    for h in hooks:
        h.remove()

    return dict(attn_norms), dict(mlp_norms)


def compute_statistics(norms_dict):
    """Compute mean/std/min/max across samples for each layer."""
    stats = {}
    for layer_idx, values in sorted(norms_dict.items()):
        arr = np.array(values)
        stats[layer_idx] = {
            "mean": float(arr.mean()),
            "std": float(arr.std()),
            "min": float(arr.min()),
            "max": float(arr.max()),
        }
    return stats


def analyze_model(model_path, tokenizer, calibration_data, device, torch_dtype):
    """Load one model, collect gradient norms, return statistics."""
    logger.info(f"Loading model from {model_path}")
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch_dtype,
        device_map=device,
        trust_remote_code=True,
    )

    logger.info("Collecting gradient norms...")
    attn_norms, mlp_norms = collect_gradient_norms(model, calibration_data, device)

    attn_stats = compute_statistics(attn_norms)
    mlp_stats = compute_statistics(mlp_norms)

    # Free memory
    del model
    torch.cuda.empty_cache()

    return attn_stats, mlp_stats


# Colorblind-friendly palette (Okabe-Ito)
COLORS = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"]


def plot_gradient_flow(all_results, model_names, output_dir):
    """Generate per-layer gradient norm comparison figure.

    Two subplots: attention (top) and MLP (bottom).
    X = layer index, Y = gradient L2 norm (log scale), one line per model.
    """
    fig, (ax_attn, ax_mlp) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    for idx, name in enumerate(model_names):
        attn_stats, mlp_stats = all_results[name]
        layers = sorted(attn_stats.keys())
        color = COLORS[idx % len(COLORS)]

        attn_means = [attn_stats[l]["mean"] for l in layers]
        attn_stds = [attn_stats[l]["std"] for l in layers]
        mlp_means = [mlp_stats[l]["mean"] for l in layers]
        mlp_stds = [mlp_stats[l]["std"] for l in layers]

        ax_attn.errorbar(
            layers, attn_means, yerr=attn_stds,
            label=name, color=color, linewidth=1.8,
            capsize=2, capthick=1, elinewidth=0.8, alpha=0.9,
            marker="o", markersize=3,
        )
        ax_mlp.errorbar(
            layers, mlp_means, yerr=mlp_stds,
            label=name, color=color, linewidth=1.8,
            capsize=2, capthick=1, elinewidth=0.8, alpha=0.9,
            marker="o", markersize=3,
        )

    ax_attn.set_ylabel("Gradient L2 Norm", fontsize=13)
    ax_attn.set_title("Attention Layers", fontsize=14, fontweight="bold")
    ax_attn.set_yscale("log")
    ax_attn.legend(fontsize=11, loc="best")
    ax_attn.grid(True, alpha=0.3, linestyle="--")
    ax_attn.tick_params(labelsize=11)

    ax_mlp.set_xlabel("Layer Index", fontsize=13)
    ax_mlp.set_ylabel("Gradient L2 Norm", fontsize=13)
    ax_mlp.set_title("MLP Layers", fontsize=14, fontweight="bold")
    ax_mlp.set_yscale("log")
    ax_mlp.legend(fontsize=11, loc="best")
    ax_mlp.grid(True, alpha=0.3, linestyle="--")
    ax_mlp.tick_params(labelsize=11)

    plt.tight_layout()

    os.makedirs(output_dir, exist_ok=True)
    pdf_path = os.path.join(output_dir, "gradient_flow_comparison.pdf")
    png_path = os.path.join(output_dir, "gradient_flow_comparison.png")
    fig.savefig(pdf_path, bbox_inches="tight", dpi=300)
    fig.savefig(png_path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    logger.info(f"Saved figures to {pdf_path} and {png_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Gradient flow analysis: compare per-layer gradient norms across pruned models"
    )
    parser.add_argument(
        "--model_paths", nargs="+", required=True,
        help="Paths to model checkpoints (space-separated)",
    )
    parser.add_argument(
        "--model_names", nargs="+", required=True,
        help="Display names for each model (e.g., CKA-only Standard RASP)",
    )
    parser.add_argument("--n_samples", type=int, default=128, help="Number of calibration samples")
    parser.add_argument("--max_length", type=int, default=512, help="Max token length")
    parser.add_argument("--output_dir", type=str, required=True, help="Output directory for results")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument(
        "--dtype", type=str, default="bfloat16",
        choices=["float16", "bfloat16", "float32"],
    )
    args = parser.parse_args()

    if len(args.model_paths) != len(args.model_names):
        parser.error("--model_paths and --model_names must have the same number of entries")

    set_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
    torch_dtype = dtype_map[args.dtype]

    # Load tokenizer from first model (all models share the same tokenizer)
    logger.info(f"Loading tokenizer from {args.model_paths[0]}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_paths[0], trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    logger.info(f"Loading {args.n_samples} calibration samples from GSM8K")
    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)

    all_results = {}
    all_json = {}

    for model_path, model_name in zip(args.model_paths, args.model_names):
        logger.info(f"\n{'='*60}")
        logger.info(f"Analyzing: {model_name} ({model_path})")
        logger.info(f"{'='*60}")

        attn_stats, mlp_stats = analyze_model(
            model_path, tokenizer, calibration_data, device, torch_dtype
        )
        all_results[model_name] = (attn_stats, mlp_stats)

        # Convert int keys to str for JSON serialization
        all_json[model_name] = {
            "model_path": model_path,
            "attention": {str(k): v for k, v in attn_stats.items()},
            "mlp": {str(k): v for k, v in mlp_stats.items()},
        }

        # Log summary
        layers = sorted(attn_stats.keys())
        attn_mean_all = np.mean([attn_stats[l]["mean"] for l in layers])
        mlp_mean_all = np.mean([mlp_stats[l]["mean"] for l in layers])
        logger.info(f"  {model_name}: avg attn grad norm = {attn_mean_all:.6f}, avg mlp grad norm = {mlp_mean_all:.6f}")

    # Save JSON
    os.makedirs(args.output_dir, exist_ok=True)
    json_path = os.path.join(args.output_dir, "gradient_flow_stats.json")
    with open(json_path, "w") as f:
        json.dump(
            {"config": vars(args), "results": all_json},
            f, indent=2,
        )
    logger.info(f"Saved statistics to {json_path}")

    # Plot
    plot_gradient_flow(all_results, args.model_names, args.output_dir)

    logger.info("Done.")


if __name__ == "__main__":
    main()

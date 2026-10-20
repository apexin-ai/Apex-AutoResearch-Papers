"""
Gradient-based Importance Scoring for structured pruning.

Computes Taylor-expansion importance I(h) = ||w_h * grad_h||_2 for each
attention head and MLP channel group on calibration data.

Input:  model + calibration data (GSM8K train subset)
Output: per-structure I(h) scores saved as dict in .pt file
        Keys: 'attn_importance' (dict[layer_idx -> tensor[n_heads]]),
              'mlp_importance'  (dict[layer_idx -> tensor[n_groups]])
"""

import argparse
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
    """Load GSM8K train questions as calibration prompts with labels for loss computation."""
    ds = load_dataset("openai/gsm8k", "main", split="train")
    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))

    encodings = []
    for example in ds:
        text = f"Question: {example['question']}\nAnswer: {example['answer']}"
        ids = tokenizer(text, return_tensors="pt", truncation=True, max_length=max_length)
        encodings.append(ids)
    return encodings


def compute_importance(model, calibration_data, device):
    """Compute gradient-based importance for attention heads and MLP groups.

    Uses Taylor expansion: I(h) = ||w_h * grad_h||_2
    Accumulates over calibration batches.
    """
    config = model.config
    n_layers = config.num_hidden_layers
    n_heads = config.num_attention_heads
    head_dim = config.hidden_size // n_heads
    intermediate_size = config.intermediate_size
    n_groups = n_heads  # match attention head count for MLP groups
    group_size = intermediate_size // n_groups

    attn_importance = {i: torch.zeros(n_heads, device="cpu") for i in range(n_layers)}
    mlp_importance = {i: torch.zeros(n_groups, device="cpu") for i in range(n_layers)}

    model.train()

    for batch_idx, enc in enumerate(calibration_data):
        input_ids = enc["input_ids"].to(device)
        attention_mask = enc["attention_mask"].to(device)
        labels = input_ids.clone()

        model.zero_grad()
        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()

        with torch.no_grad():
            for layer_idx in range(n_layers):
                layer = model.model.layers[layer_idx]

                # Attention head importance via q_proj weights
                q_weight = layer.self_attn.q_proj.weight  # [n_heads*head_dim, hidden]
                q_grad = layer.self_attn.q_proj.weight.grad
                if q_grad is not None:
                    # Reshape to [n_heads, head_dim, hidden]
                    w = q_weight.view(n_heads, head_dim, -1)
                    g = q_grad.view(n_heads, head_dim, -1)
                    taylor = (w * g).float()  # [n_heads, head_dim, hidden]
                    # L2 norm per head
                    head_scores = taylor.view(n_heads, -1).norm(dim=1)  # [n_heads]
                    attn_importance[layer_idx] += head_scores.cpu()

                # Also incorporate k_proj and v_proj for attention importance
                for proj_name in ["k_proj", "v_proj", "o_proj"]:
                    proj = getattr(layer.self_attn, proj_name)
                    w = proj.weight
                    g = proj.weight.grad
                    if g is None:
                        continue
                    if proj_name == "o_proj":
                        # o_proj: [hidden, n_heads*head_dim] — split on dim=1
                        w_r = w.view(-1, n_heads, head_dim)
                        g_r = g.view(-1, n_heads, head_dim)
                        taylor = (w_r * g_r).float()
                        head_scores = taylor.permute(1, 0, 2).reshape(n_heads, -1).norm(dim=1)
                    elif proj_name == "k_proj":
                        # GQA: k_proj has n_kv_heads, broadcast to n_heads
                        n_kv = config.num_key_value_heads
                        kv_head_dim = config.hidden_size // n_heads
                        w_r = w.view(n_kv, kv_head_dim, -1)
                        g_r = g.view(n_kv, kv_head_dim, -1)
                        taylor = (w_r * g_r).float()
                        kv_scores = taylor.view(n_kv, -1).norm(dim=1)
                        # Broadcast KV heads to query heads
                        heads_per_kv = n_heads // n_kv
                        head_scores = kv_scores.repeat_interleave(heads_per_kv)
                    elif proj_name == "v_proj":
                        n_kv = config.num_key_value_heads
                        kv_head_dim = config.hidden_size // n_heads
                        w_r = w.view(n_kv, kv_head_dim, -1)
                        g_r = g.view(n_kv, kv_head_dim, -1)
                        taylor = (w_r * g_r).float()
                        kv_scores = taylor.view(n_kv, -1).norm(dim=1)
                        heads_per_kv = n_heads // n_kv
                        head_scores = kv_scores.repeat_interleave(heads_per_kv)
                    attn_importance[layer_idx] += head_scores.cpu()

                # MLP importance via gate_proj
                gate_w = layer.mlp.gate_proj.weight  # [intermediate, hidden]
                gate_g = layer.mlp.gate_proj.weight.grad
                if gate_g is not None:
                    usable = n_groups * group_size
                    w_r = gate_w[:usable].view(n_groups, group_size, -1)
                    g_r = gate_g[:usable].view(n_groups, group_size, -1)
                    taylor = (w_r * g_r).float()
                    group_scores = taylor.view(n_groups, -1).norm(dim=1)
                    mlp_importance[layer_idx] += group_scores.cpu()

                # Also use up_proj for MLP importance
                up_w = layer.mlp.up_proj.weight
                up_g = layer.mlp.up_proj.weight.grad
                if up_g is not None:
                    usable = n_groups * group_size
                    w_r = up_w[:usable].view(n_groups, group_size, -1)
                    g_r = up_g[:usable].view(n_groups, group_size, -1)
                    taylor = (w_r * g_r).float()
                    group_scores = taylor.view(n_groups, -1).norm(dim=1)
                    mlp_importance[layer_idx] += group_scores.cpu()

        if (batch_idx + 1) % 50 == 0:
            logger.info(f"  Processed {batch_idx + 1}/{len(calibration_data)} samples")

    # Average over samples
    n = len(calibration_data)
    for layer_idx in range(n_layers):
        attn_importance[layer_idx] /= n
        mlp_importance[layer_idx] /= n

    return attn_importance, mlp_importance


def main():
    parser = argparse.ArgumentParser(description="Compute gradient-based importance scores for RASP")
    parser.add_argument("--model_path", type=str, required=True, help="Path to pretrained model")
    parser.add_argument("--output_path", type=str, required=True, help="Output .pt file for importance scores")
    parser.add_argument("--n_samples", type=int, default=512, help="Number of calibration samples")
    parser.add_argument("--max_length", type=int, default=512, help="Max token length for calibration inputs")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
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

    logger.info(f"Loading {args.n_samples} calibration samples")
    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)

    logger.info("Computing gradient-based importance scores...")
    attn_importance, mlp_importance = compute_importance(model, calibration_data, device)

    for layer_idx in range(model.config.num_hidden_layers):
        a = attn_importance[layer_idx]
        m = mlp_importance[layer_idx]
        logger.info(
            f"  Layer {layer_idx}: attn I(h) range [{a.min():.6f}, {a.max():.6f}], "
            f"mlp I(h) range [{m.min():.6f}, {m.max():.6f}]"
        )

    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
    result = {"attn_importance": attn_importance, "mlp_importance": mlp_importance}
    torch.save(result, args.output_path)
    logger.info(f"Saved importance scores to {args.output_path}")


if __name__ == "__main__":
    main()

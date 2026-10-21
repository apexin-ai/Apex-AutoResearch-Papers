"""
CKA Overlap Computation for RASP.

Computes intra-layer functional overlap F(h) for each attention head and MLP channel group
using linear CKA (Centered Kernel Alignment via HSIC).

Input:  model + calibration data (GSM8K train subset)
Output: per-structure F(h) scores saved as dict in .pt file
        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_heads]]),
              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])
"""

import argparse
import logging
import math
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


def linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:
    """Linear CKA between two activation matrices.
    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].
    """
    X = X - X.mean(0)
    Y = Y - Y.mean(0)
    hsic_xy = torch.norm(X.T @ Y, "fro") ** 2
    hsic_xx = torch.norm(X.T @ X, "fro") ** 2
    hsic_yy = torch.norm(Y.T @ Y, "fro") ** 2
    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()


def load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):
    """Load GSM8K train questions as calibration prompts."""
    ds = load_dataset("openai/gsm8k", "main", split="train")
    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))

    encodings = []
    for example in ds:
        prompt = f"Question: {example['question']}\nAnswer: Let me think step by step.\n"
        ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
        encodings.append(ids)
    return encodings


def collect_head_activations(model, tokenizer, calibration_data, device):
    """Run calibration data through model and collect per-head activations for each layer.

    Returns dict[layer_idx] -> tensor[n_samples, n_heads, pooled_dim]
    where pooled_dim collapses (seq_len, head_dim) via mean-pool over seq_len.
    """
    config = model.config
    n_layers = config.num_hidden_layers
    n_heads = config.num_attention_heads
    head_dim = config.hidden_size // n_heads

    layer_activations = {i: [] for i in range(n_layers)}
    hooks = []

    def make_hook(layer_idx):
        def hook_fn(module, input, output):
            # output of attention: (hidden_states, attn_weights, past_kv)
            # We hook into q_proj to get query states, then reshape per-head
            pass
        return hook_fn

    # Hook into each attention layer's output (the hidden_states after o_proj)
    # We instead hook the q_proj to capture per-head representations
    q_proj_outputs = {i: [] for i in range(n_layers)}

    def make_q_hook(layer_idx):
        def hook_fn(module, input, output):
            # output shape: [batch, seq_len, n_heads * head_dim]
            q_proj_outputs[layer_idx].append(output.detach())
        return hook_fn

    for i in range(n_layers):
        layer = model.model.layers[i]
        h = layer.self_attn.q_proj.register_forward_hook(make_q_hook(i))
        hooks.append(h)

    model.eval()
    with torch.no_grad():
        for batch_idx, enc in enumerate(calibration_data):
            input_ids = enc["input_ids"].to(device)
            attention_mask = enc["attention_mask"].to(device)
            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
            if (batch_idx + 1) % 50 == 0:
                logger.info(f"  Processed {batch_idx + 1}/{len(calibration_data)} samples")

    for h in hooks:
        h.remove()

    # Reshape and mean-pool: [batch, seq, n_heads*head_dim] -> per-head [batch, head_dim]
    for layer_idx in range(n_layers):
        tensors = q_proj_outputs[layer_idx]  # list of [1, seq, n_heads*head_dim]
        per_head_list = []
        for t in tensors:
            t = t.squeeze(0)  # [seq, n_heads*head_dim]
            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]
            t = t.mean(dim=0)  # [n_heads, head_dim] — mean pool over seq
            per_head_list.append(t)
        layer_activations[layer_idx] = torch.stack(per_head_list, dim=0)  # [n_samples, n_heads, head_dim]
        q_proj_outputs[layer_idx] = None  # free memory

    return layer_activations


def collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups: int = 28):
    """Collect MLP intermediate activations grouped into channel groups.

    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim]
    """
    config = model.config
    n_layers = config.num_hidden_layers
    intermediate_size = config.intermediate_size
    group_size = intermediate_size // n_groups

    gate_outputs = {i: [] for i in range(n_layers)}
    hooks = []

    def make_gate_hook(layer_idx):
        def hook_fn(module, input, output):
            gate_outputs[layer_idx].append(output.detach())
        return hook_fn

    for i in range(n_layers):
        layer = model.model.layers[i]
        h = layer.mlp.gate_proj.register_forward_hook(make_gate_hook(i))
        hooks.append(h)

    model.eval()
    with torch.no_grad():
        for enc in calibration_data:
            input_ids = enc["input_ids"].to(device)
            attention_mask = enc["attention_mask"].to(device)
            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)

    for h in hooks:
        h.remove()

    layer_activations = {}
    for layer_idx in range(n_layers):
        tensors = gate_outputs[layer_idx]
        per_group_list = []
        for t in tensors:
            t = t.squeeze(0)  # [seq, intermediate_size]
            t = t.mean(dim=0)  # [intermediate_size] — mean pool over seq
            # Truncate to exact multiple of group_size
            usable = n_groups * group_size
            t = t[:usable].view(n_groups, group_size)  # [n_groups, group_size]
            per_group_list.append(t)
        layer_activations[layer_idx] = torch.stack(per_group_list, dim=0)  # [n_samples, n_groups, group_size]
        gate_outputs[layer_idx] = None

    return layer_activations


def compute_overlap(activations_dict: dict, structure_name: str) -> tuple:
    """Compute F(h) = mean CKA similarity and pairwise CKA matrix per layer.

    activations_dict: dict[layer_idx] -> tensor[n_samples, n_structures, dim]
    Returns: (overlap_scores, cka_matrices)
        overlap_scores: dict[layer_idx] -> tensor[n_structures] of overlap F(h) in [0, 1]
        cka_matrices: dict[layer_idx] -> tensor[n_structures, n_structures] pairwise CKA
    """
    overlap_scores = {}
    cka_matrices = {}
    for layer_idx, acts in activations_dict.items():
        n_samples, n_structs, dim = acts.shape
        matrix = torch.zeros(n_structs, n_structs)
        for i in range(n_structs):
            matrix[i, i] = 1.0
            for j in range(i + 1, n_structs):
                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())
                matrix[i, j] = val
                matrix[j, i] = val
        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)
        overlap_scores[layer_idx] = scores
        cka_matrices[layer_idx] = matrix
        logger.info(
            f"  Layer {layer_idx} {structure_name}: F(h) range [{scores.min():.4f}, {scores.max():.4f}], "
            f"mean={scores.mean():.4f}"
        )
    return overlap_scores, cka_matrices


def main():
    parser = argparse.ArgumentParser(description="Compute CKA-based functional overlap scores for RASP")
    parser.add_argument("--model_path", type=str, required=True, help="Path to pretrained model")
    parser.add_argument("--output_path", type=str, required=True, help="Output .pt file for overlap scores")
    parser.add_argument("--n_samples", type=int, default=512, help="Number of calibration samples")
    parser.add_argument("--max_length", type=int, default=512, help="Max token length for calibration inputs")
    parser.add_argument("--mlp_groups", type=int, default=28, help="Number of MLP channel groups per layer")
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

    logger.info(f"Loading {args.n_samples} calibration samples from GSM8K train")
    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)

    logger.info("Collecting attention head activations...")
    head_acts = collect_head_activations(model, tokenizer, calibration_data, device)

    logger.info("Computing attention head overlap F(h)...")
    attn_overlap, attn_cka_matrix = compute_overlap(head_acts, "attn_heads")
    del head_acts
    torch.cuda.empty_cache()

    logger.info("Collecting MLP activations...")
    mlp_acts = collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups=args.mlp_groups)

    logger.info("Computing MLP group overlap F(h)...")
    mlp_overlap, mlp_cka_matrix = compute_overlap(mlp_acts, "mlp_groups")
    del mlp_acts
    torch.cuda.empty_cache()

    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
    result = {
        "attn_overlap": attn_overlap,
        "mlp_overlap": mlp_overlap,
        "attn_cka_matrix": attn_cka_matrix,
        "mlp_cka_matrix": mlp_cka_matrix,
    }
    torch.save(result, args.output_path)
    logger.info(f"Saved CKA overlap scores to {args.output_path}")


if __name__ == "__main__":
    main()

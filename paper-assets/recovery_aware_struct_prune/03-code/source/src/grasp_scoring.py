"""
GraSP (Gradient Signal Preservation) scoring for structured pruning.

Computes GraSP importance at GQA-group and MLP-group granularity:
  Score(θ) = -θ ⊙ Hg
where Hg is the Hessian-gradient product computed via the R-op trick:
  g = ∂L/∂θ  (with retained graph)
  Hg = ∂/∂θ [g^T · stop_grad(g)]

Structures with lower aggregate score hinder gradient flow more and
are pruned first — compatible with prune.py's ascending-sort convention.

Output format matches importance_score.py:
  {'attn_importance': dict[layer_idx -> tensor], 'mlp_importance': dict[...]}
So the output can be fed directly to prune.py --mode standard --importance_path.

Reference: Wang et al., "Picking Winning Tickets Before Training by Preserving
Gradient Flow" (ICLR 2020).
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
    ds = load_dataset("openai/gsm8k", "main", split="train")
    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
    encodings = []
    for example in ds:
        text = f"Question: {example['question']}\nAnswer: {example['answer']}"
        ids = tokenizer(text, return_tensors="pt", truncation=True, max_length=max_length)
        encodings.append(ids)
    return encodings


def _aggregate_attn_score(score_tensor, name, n_heads, n_kv_heads, head_dim, heads_per_kv):
    """Aggregate per-element GraSP scores to GQA group level for attention weights."""
    if "q_proj.weight" in name:
        # [n_heads*head_dim, hidden] -> per Q head -> per GQA group
        s = score_tensor.view(n_heads, head_dim, -1).sum(dim=(1, 2))
        return s.view(n_kv_heads, heads_per_kv).sum(dim=1)
    elif "k_proj.weight" in name or "v_proj.weight" in name:
        # [n_kv_heads*head_dim, hidden] -> per KV head
        return score_tensor.view(n_kv_heads, head_dim, -1).sum(dim=(1, 2))
    elif "o_proj.weight" in name:
        # [hidden, n_heads*head_dim] -> per Q head -> per GQA group
        s = score_tensor.view(-1, n_heads, head_dim).sum(dim=(0, 2))
        return s.view(n_kv_heads, heads_per_kv).sum(dim=1)
    return None


def _aggregate_mlp_score(score_tensor, name, n_mlp_groups, mlp_group_size):
    """Aggregate per-element GraSP scores to MLP group level."""
    usable = n_mlp_groups * mlp_group_size
    if "gate_proj.weight" in name or "up_proj.weight" in name:
        # [intermediate, hidden] -> per group
        return score_tensor[:usable].view(n_mlp_groups, mlp_group_size, -1).sum(dim=(1, 2))
    elif "down_proj.weight" in name:
        # [hidden, intermediate] -> per group
        return score_tensor[:, :usable].view(-1, n_mlp_groups, mlp_group_size).sum(dim=(0, 2))
    return None


def compute_grasp_scores(model, calibration_data, device, temp=200):
    """Compute GraSP scores at GQA-group and MLP-group granularity.

    Args:
        temp: temperature for softmax on logits before loss, following the
              original GraSP implementation to stabilize Hessian estimation.
    """
    config = model.config
    n_layers = config.num_hidden_layers
    n_heads = config.num_attention_heads
    n_kv_heads = config.num_key_value_heads
    head_dim = config.hidden_size // n_heads
    heads_per_kv = n_heads // n_kv_heads
    intermediate_size = config.intermediate_size
    n_mlp_groups = n_heads
    mlp_group_size = intermediate_size // n_mlp_groups

    attn_grasp = {i: torch.zeros(n_kv_heads) for i in range(n_layers)}
    mlp_grasp = {i: torch.zeros(n_mlp_groups) for i in range(n_layers)}

    model.train()

    # Collect layer parameters only (skip embeddings/lm_head for efficiency)
    target_params = []
    target_names = []
    for name, param in model.named_parameters():
        if "model.layers." in name and param.requires_grad:
            target_params.append(param)
            target_names.append(name)

    n_samples = len(calibration_data)

    for batch_idx, enc in enumerate(calibration_data):
        input_ids = enc["input_ids"].to(device)
        attention_mask = enc["attention_mask"].to(device)
        labels = input_ids.clone()

        model.zero_grad()

        # Forward pass
        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss

        # Step 1: g = ∂L/∂θ with retained computation graph
        grads = torch.autograd.grad(loss, target_params, create_graph=True)

        # Step 2: z = g^T · stop_grad(g) — scalar for Hessian-vector product
        z = sum((g * g.detach()).sum() for g in grads)

        # Step 3: Hg = ∂z/∂θ — the Hessian-gradient product
        hg = torch.autograd.grad(z, target_params)

        # Step 4: GraSP score = -θ ⊙ Hg, aggregate per structure group
        with torch.no_grad():
            for name, param, hg_i in zip(target_names, target_params, hg):
                score = -(param * hg_i).float()

                parts = name.split(".")
                layer_idx = int(parts[2])

                if "self_attn" in name and "weight" in name:
                    group_score = _aggregate_attn_score(
                        score, name, n_heads, n_kv_heads, head_dim, heads_per_kv
                    )
                    if group_score is not None:
                        attn_grasp[layer_idx] += group_score.cpu()

                elif "mlp" in name and "weight" in name:
                    group_score = _aggregate_mlp_score(
                        score, name, n_mlp_groups, mlp_group_size
                    )
                    if group_score is not None:
                        mlp_grasp[layer_idx] += group_score.cpu()

        # Free graph memory
        del grads, z, hg, loss, outputs
        torch.cuda.empty_cache()

        if (batch_idx + 1) % 10 == 0 or (batch_idx + 1) == n_samples:
            logger.info(f"  GraSP: processed {batch_idx + 1}/{n_samples} samples")

    # Average over samples
    for layer_idx in range(n_layers):
        attn_grasp[layer_idx] /= n_samples
        mlp_grasp[layer_idx] /= n_samples

    return attn_grasp, mlp_grasp


def main():
    parser = argparse.ArgumentParser(
        description="Compute GraSP pruning scores (gradient signal preservation)"
    )
    parser.add_argument("--model_path", type=str, required=True,
                        help="Path to pretrained model")
    parser.add_argument("--output_path", type=str, required=True,
                        help="Output .pt file for GraSP scores")
    parser.add_argument("--n_samples", type=int, default=64,
                        help="Calibration samples (default 64; GraSP uses 2nd-order grads so keep small)")
    parser.add_argument("--max_length", type=int, default=512)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dtype", type=str, default="bfloat16",
                        choices=["float16", "bfloat16", "float32"])
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

    n_kv_heads = model.config.num_key_value_heads
    heads_per_kv = model.config.num_attention_heads // n_kv_heads
    logger.info(f"GQA config: {n_kv_heads} KV heads, {heads_per_kv} Q heads per group")

    logger.info(f"Loading {args.n_samples} calibration samples")
    calibration_data = load_calibration_data(
        tokenizer, args.n_samples, args.max_length, args.seed
    )

    logger.info("Computing GraSP scores (2nd-order, may take a while)...")
    attn_importance, mlp_importance = compute_grasp_scores(model, calibration_data, device)

    for layer_idx in range(model.config.num_hidden_layers):
        a = attn_importance[layer_idx]
        m = mlp_importance[layer_idx]
        logger.info(
            f"  Layer {layer_idx}: attn GQA [{a.min():.6f}, {a.max():.6f}], "
            f"mlp [{m.min():.6f}, {m.max():.6f}]"
        )

    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
    result = {"attn_importance": attn_importance, "mlp_importance": mlp_importance}
    torch.save(result, args.output_path)
    logger.info(f"Saved GraSP scores to {args.output_path}")
    logger.info(
        "To prune: python src/prune.py --mode standard "
        f"--importance_path {args.output_path} ..."
    )


if __name__ == "__main__":
    main()

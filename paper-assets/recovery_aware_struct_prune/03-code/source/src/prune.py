"""
Structured Pruning for Qwen2.5 architecture.

Removes attention heads and MLP channel groups based on RASP or standard importance scores.
Handles GQA (grouped query attention) correctly: when all query heads sharing a KV head
are pruned, the corresponding KV head is also removed.

Input:  pretrained model + pruning scores
Output: pruned model saved to disk
"""

import argparse
import copy
import logging
import os
import random

import numpy as np
import torch
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


def compute_pruning_masks(scores: dict, n_to_prune: int) -> dict:
    """Determine which structures to prune globally.

    Returns dict[layer_idx -> list of struct indices to KEEP].
    """
    ranking = []
    for layer_idx, layer_scores in scores.items():
        for struct_idx in range(layer_scores.shape[0]):
            ranking.append((layer_scores[struct_idx].item(), layer_idx, struct_idx))
    ranking.sort(key=lambda x: x[0])

    prune_set = set()
    for i in range(min(n_to_prune, len(ranking))):
        _, layer_idx, struct_idx = ranking[i]
        prune_set.add((layer_idx, struct_idx))

    keep_masks = {}
    for layer_idx, layer_scores in scores.items():
        n_structs = layer_scores.shape[0]
        keep = [i for i in range(n_structs) if (layer_idx, i) not in prune_set]
        keep_masks[layer_idx] = keep
    return keep_masks


def prune_attention_heads(model, attn_keep_masks: dict):
    """Prune attention heads from the model by slicing weight matrices in-place.

    For GQA: KV heads are removed only when ALL query heads mapped to them are pruned.
    """
    config = model.config
    n_heads = config.num_attention_heads
    n_kv_heads = config.num_key_value_heads
    head_dim = config.hidden_size // n_heads
    heads_per_kv = n_heads // n_kv_heads

    total_pruned_q = 0
    total_pruned_kv = 0

    for layer_idx, keep_heads in attn_keep_masks.items():
        layer = model.model.layers[layer_idx]
        attn = layer.self_attn
        n_keep = len(keep_heads)
        pruned_q = n_heads - n_keep

        # Q indices to keep
        q_indices = []
        for h in keep_heads:
            start = h * head_dim
            q_indices.extend(range(start, start + head_dim))
        q_indices = torch.tensor(q_indices, dtype=torch.long)

        # Determine which KV heads to keep
        kv_keep = set()
        for h in keep_heads:
            kv_keep.add(h // heads_per_kv)
        kv_keep = sorted(kv_keep)
        n_kv_keep = len(kv_keep)
        pruned_kv = n_kv_heads - n_kv_keep

        kv_indices = []
        for kv in kv_keep:
            start = kv * head_dim
            kv_indices.extend(range(start, start + head_dim))
        kv_indices = torch.tensor(kv_indices, dtype=torch.long)

        # Slice q_proj: [n_heads*head_dim, hidden] -> [n_keep*head_dim, hidden]
        attn.q_proj.weight = torch.nn.Parameter(attn.q_proj.weight.data[q_indices])
        if attn.q_proj.bias is not None:
            attn.q_proj.bias = torch.nn.Parameter(attn.q_proj.bias.data[q_indices])

        # Slice k_proj, v_proj: [n_kv*head_dim, hidden] -> [n_kv_keep*head_dim, hidden]
        attn.k_proj.weight = torch.nn.Parameter(attn.k_proj.weight.data[kv_indices])
        if attn.k_proj.bias is not None:
            attn.k_proj.bias = torch.nn.Parameter(attn.k_proj.bias.data[kv_indices])

        attn.v_proj.weight = torch.nn.Parameter(attn.v_proj.weight.data[kv_indices])
        if attn.v_proj.bias is not None:
            attn.v_proj.bias = torch.nn.Parameter(attn.v_proj.bias.data[kv_indices])

        # Slice o_proj: [hidden, n_heads*head_dim] -> [hidden, n_keep*head_dim]
        attn.o_proj.weight = torch.nn.Parameter(attn.o_proj.weight.data[:, q_indices])

        # Update config attributes on the layer
        attn.num_heads = n_keep
        attn.num_key_value_heads = n_kv_keep
        attn.head_dim = head_dim

        total_pruned_q += pruned_q
        total_pruned_kv += pruned_kv

        if pruned_q > 0:
            logger.info(
                f"  Layer {layer_idx}: pruned {pruned_q}/{n_heads} Q heads, "
                f"{pruned_kv}/{n_kv_heads} KV heads"
            )

    logger.info(f"Total attention pruning: {total_pruned_q} Q heads, {total_pruned_kv} KV heads removed")


def prune_mlp_channels(model, mlp_keep_masks: dict):
    """Prune MLP channel groups by slicing gate_proj, up_proj, and down_proj."""
    config = model.config
    intermediate_size = config.intermediate_size
    n_heads = config.num_attention_heads
    n_groups = n_heads
    group_size = intermediate_size // n_groups

    total_pruned = 0

    for layer_idx, keep_groups in mlp_keep_masks.items():
        layer = model.model.layers[layer_idx]
        mlp = layer.mlp
        n_keep = len(keep_groups)
        pruned = n_groups - n_keep

        if pruned == 0:
            continue

        # Channel indices to keep
        indices = []
        for g in keep_groups:
            start = g * group_size
            indices.extend(range(start, start + group_size))
        # Also keep any remainder channels beyond n_groups*group_size
        remainder_start = n_groups * group_size
        if remainder_start < intermediate_size:
            indices.extend(range(remainder_start, intermediate_size))
        indices = torch.tensor(indices, dtype=torch.long)

        # gate_proj: [intermediate, hidden] -> [n_keep_channels, hidden]
        mlp.gate_proj.weight = torch.nn.Parameter(mlp.gate_proj.weight.data[indices])
        if mlp.gate_proj.bias is not None:
            mlp.gate_proj.bias = torch.nn.Parameter(mlp.gate_proj.bias.data[indices])

        # up_proj: [intermediate, hidden] -> [n_keep_channels, hidden]
        mlp.up_proj.weight = torch.nn.Parameter(mlp.up_proj.weight.data[indices])
        if mlp.up_proj.bias is not None:
            mlp.up_proj.bias = torch.nn.Parameter(mlp.up_proj.bias.data[indices])

        # down_proj: [hidden, intermediate] -> [hidden, n_keep_channels]
        mlp.down_proj.weight = torch.nn.Parameter(mlp.down_proj.weight.data[:, indices])

        total_pruned += pruned
        logger.info(
            f"  Layer {layer_idx}: pruned {pruned}/{n_groups} MLP groups "
            f"({pruned * group_size} channels)"
        )

    logger.info(f"Total MLP pruning: {total_pruned} groups removed")


def count_parameters(model) -> int:
    return sum(p.numel() for p in model.parameters())


def main():
    parser = argparse.ArgumentParser(description="Execute structured pruning on Qwen2.5 model")
    parser.add_argument("--model_path", type=str, required=True, help="Path to pretrained model")
    parser.add_argument("--importance_path", type=str, required=True, help="Path to importance scores .pt")
    parser.add_argument("--cka_path", type=str, default=None, help="Path to CKA overlap scores .pt")
    parser.add_argument("--mode", type=str, choices=["standard", "rasp"], required=True)
    parser.add_argument("--sparsity", type=float, default=0.35, help="Target sparsity ratio")
    parser.add_argument("--alpha", type=float, default=1.0, help="RASP alpha parameter")
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
        device_map="cpu",  # load on CPU for manipulation
        trust_remote_code=True,
    )

    original_params = count_parameters(model)
    logger.info(f"Original model parameters: {original_params:,}")

    # Load scores
    importance_data = torch.load(args.importance_path, map_location="cpu", weights_only=True)
    attn_importance = importance_data["attn_importance"]
    mlp_importance = importance_data["mlp_importance"]

    if args.mode == "rasp":
        if args.cka_path is None:
            raise ValueError("--cka_path required for rasp mode")
        cka_data = torch.load(args.cka_path, map_location="cpu", weights_only=True)
        attn_overlap = cka_data["attn_overlap"]
        mlp_overlap = cka_data["mlp_overlap"]
        # S(h) = I(h) * (1 - F(h))^alpha
        attn_scores = {}
        for k in attn_importance:
            attn_scores[k] = attn_importance[k].float() * (1.0 - attn_overlap[k].float()).pow(args.alpha)
        mlp_scores = {}
        for k in mlp_importance:
            mlp_scores[k] = mlp_importance[k].float() * (1.0 - mlp_overlap[k].float()).pow(args.alpha)
        logger.info(f"Using RASP scoring with alpha={args.alpha}")
    else:
        attn_scores = {k: v.float() for k, v in attn_importance.items()}
        mlp_scores = {k: v.float() for k, v in mlp_importance.items()}
        logger.info("Using standard importance-only scoring")

    # Compute how many structures to prune for target sparsity
    # Approximate: distribute sparsity proportionally between attn and MLP
    config = model.config
    n_layers = config.num_hidden_layers
    n_heads = config.num_attention_heads
    head_dim = config.hidden_size // n_heads
    intermediate_size = config.intermediate_size
    n_groups = n_heads
    group_size = intermediate_size // n_groups

    total_attn_heads = n_layers * n_heads
    total_mlp_groups = n_layers * n_groups

    # Estimate parameter counts
    # Per attention head: q_proj + share of k/v_proj + o_proj
    hidden = config.hidden_size
    attn_params_per_head = head_dim * hidden * 2  # q + o contribution
    mlp_params_per_group = group_size * hidden * 3  # gate + up + down contribution

    total_prunable = total_attn_heads * attn_params_per_head + total_mlp_groups * mlp_params_per_group
    target_prune_params = original_params * args.sparsity

    # Use a unified ranking approach: merge attn and MLP scores
    all_entries = []
    for layer_idx in range(n_layers):
        for h in range(n_heads):
            score = attn_scores[layer_idx][h].item()
            params = attn_params_per_head
            all_entries.append((score, "attn", layer_idx, h, params))
        for g in range(n_groups):
            score = mlp_scores[layer_idx][g].item()
            params = mlp_params_per_group
            all_entries.append((score, "mlp", layer_idx, g, params))

    all_entries.sort(key=lambda x: x[0])

    # Greedily select structures to prune until reaching target sparsity
    pruned_params = 0
    attn_prune_set = set()
    mlp_prune_set = set()

    # Keep at least 4 heads per layer and 4 MLP groups per layer
    min_keep_per_layer = 4
    attn_prune_count = {i: 0 for i in range(n_layers)}
    mlp_prune_count = {i: 0 for i in range(n_layers)}

    for score, stype, layer_idx, struct_idx, params in all_entries:
        if pruned_params >= target_prune_params:
            break
        if stype == "attn":
            if attn_prune_count[layer_idx] >= n_heads - min_keep_per_layer:
                continue
            attn_prune_set.add((layer_idx, struct_idx))
            attn_prune_count[layer_idx] += 1
        else:
            if mlp_prune_count[layer_idx] >= n_groups - min_keep_per_layer:
                continue
            mlp_prune_set.add((layer_idx, struct_idx))
            mlp_prune_count[layer_idx] += 1
        pruned_params += params

    logger.info(f"Target sparsity: {args.sparsity:.0%}, pruning {len(attn_prune_set)} attn heads + "
                f"{len(mlp_prune_set)} MLP groups ({pruned_params:,} params)")

    # Build keep masks
    attn_keep_masks = {}
    for layer_idx in range(n_layers):
        keep = [h for h in range(n_heads) if (layer_idx, h) not in attn_prune_set]
        attn_keep_masks[layer_idx] = keep

    mlp_keep_masks = {}
    for layer_idx in range(n_layers):
        keep = [g for g in range(n_groups) if (layer_idx, g) not in mlp_prune_set]
        mlp_keep_masks[layer_idx] = keep

    # Execute pruning
    logger.info("Pruning attention heads...")
    prune_attention_heads(model, attn_keep_masks)

    logger.info("Pruning MLP channels...")
    prune_mlp_channels(model, mlp_keep_masks)

    pruned_params_actual = count_parameters(model)
    actual_sparsity = 1.0 - pruned_params_actual / original_params
    logger.info(
        f"Pruned model parameters: {pruned_params_actual:,} "
        f"(actual sparsity: {actual_sparsity:.2%})"
    )

    # Save
    logger.info(f"Saving pruned model to {args.output_path}")
    os.makedirs(args.output_path, exist_ok=True)
    model.save_pretrained(args.output_path)
    tokenizer.save_pretrained(args.output_path)

    # Save pruning metadata
    metadata = {
        "mode": args.mode,
        "sparsity_target": args.sparsity,
        "sparsity_actual": actual_sparsity,
        "alpha": args.alpha if args.mode == "rasp" else None,
        "original_params": original_params,
        "pruned_params": pruned_params_actual,
        "attn_keep_masks": attn_keep_masks,
        "mlp_keep_masks": mlp_keep_masks,
    }
    torch.save(metadata, os.path.join(args.output_path, "pruning_metadata.pt"))
    logger.info("Done.")


if __name__ == "__main__":
    main()

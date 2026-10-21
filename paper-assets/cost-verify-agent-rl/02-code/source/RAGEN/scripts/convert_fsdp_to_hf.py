#!/usr/bin/env python3
"""Convert verl FSDP v2 sharded checkpoint to HuggingFace format.

Input:  FSDP checkpoint directory containing:
        - model_world_size_{N}_rank_{i}.pt  (DTensor shards)
        - fsdp_config.json                  (world_size metadata)
        - huggingface/                      (config.json, tokenizer files)

Output: HuggingFace model directory (config + tokenizer + safetensors)

Dependencies: torch, transformers, accelerate
GPU: Not required (CPU-only)

Usage:
    python convert_fsdp_to_hf.py \
        --input-dir /path/to/global_step_N/actor \
        --output-dir /path/to/hf_model \
        --dtype bf16
"""

import argparse
import json
import os
import shutil
import sys
import time

import torch


def load_fsdp_config(input_dir: str) -> dict:
    path = os.path.join(input_dir, "fsdp_config.json")
    if not os.path.exists(path):
        print(f"ERROR: fsdp_config.json not found in {input_dir}", file=sys.stderr)
        sys.exit(1)
    with open(path) as f:
        return json.load(f)


def reconstruct_state_dict(input_dir: str, world_size: int, target_dtype: torch.dtype) -> dict:
    shards = []
    for rank in range(world_size):
        path = os.path.join(input_dir, f"model_world_size_{world_size}_rank_{rank}.pt")
        print(f"  Loading rank {rank}: {path}")
        sd = torch.load(path, map_location="cpu", weights_only=False)
        shards.append(sd)

    keys = list(shards[0].keys())
    print(f"  Reconstructing {len(keys)} parameters from {world_size} shards...")

    full_state_dict = {}
    for key in keys:
        local_tensors = []
        shard_dim = 0
        for rank in range(world_size):
            dt = shards[rank][key]
            if hasattr(dt, "placements") and len(dt.placements) > 0:
                shard_dim = dt.placements[0].dim
            lt = dt._local_tensor if hasattr(dt, "_local_tensor") else dt.to_local()
            local_tensors.append(lt)
        full_tensor = torch.cat(local_tensors, dim=shard_dim)
        full_state_dict[key] = full_tensor.to(target_dtype)

    del shards
    return full_state_dict


def main():
    parser = argparse.ArgumentParser(description="Convert verl FSDP v2 checkpoint to HuggingFace format")
    parser.add_argument("--input-dir", required=True, help="FSDP checkpoint actor directory")
    parser.add_argument("--output-dir", required=True, help="Output HuggingFace model directory")
    parser.add_argument("--dtype", default="bf16", choices=["fp32", "bf16", "fp16"],
                        help="Output dtype (default: bf16)")
    parser.add_argument("--max-shard-size", default="5GB", help="Max safetensors shard size (default: 5GB)")
    parser.add_argument("--dry-run", action="store_true", help="Only verify checkpoint structure, don't save")
    args = parser.parse_args()

    dtype_map = {"bf16": torch.bfloat16, "fp16": torch.float16, "fp32": torch.float32}
    target_dtype = dtype_map[args.dtype]

    hf_dir = os.path.join(args.input_dir, "huggingface")
    if not os.path.isdir(hf_dir):
        print(f"ERROR: huggingface/ subdirectory not found in {args.input_dir}", file=sys.stderr)
        sys.exit(1)

    fsdp_config = load_fsdp_config(args.input_dir)
    world_size = fsdp_config["world_size"]
    print(f"FSDP config: version={fsdp_config.get('FSDP_version')}, world_size={world_size}")

    t0 = time.time()
    print("Step 1: Loading and reconstructing state dict...")
    full_state_dict = reconstruct_state_dict(args.input_dir, world_size, target_dtype)
    t1 = time.time()
    print(f"  Done in {t1 - t0:.1f}s. Parameters: {len(full_state_dict)}")

    # Print size info
    total_params = sum(v.numel() for v in full_state_dict.values())
    total_bytes = sum(v.numel() * v.element_size() for v in full_state_dict.values())
    print(f"  Total parameters: {total_params:,} ({total_bytes / 1e9:.2f} GB in {args.dtype})")

    if args.dry_run:
        # Verify shapes match HF config
        from transformers import AutoConfig
        config = AutoConfig.from_pretrained(hf_dir)
        print(f"\nDry-run verification:")
        print(f"  Model: {config.architectures[0]}")
        print(f"  Hidden size: {config.hidden_size}, Layers: {config.num_hidden_layers}")
        print(f"  Vocab size: {config.vocab_size}")
        embed_shape = full_state_dict.get("model.embed_tokens.weight", None)
        if embed_shape is not None:
            print(f"  embed_tokens.weight shape: {embed_shape.shape} (expect [{config.vocab_size}, {config.hidden_size}])")
            assert embed_shape.shape == (config.vocab_size, config.hidden_size), "Shape mismatch!"
        print("  All checks passed.")
        del full_state_dict
        return

    print("Step 2: Saving HuggingFace model...")
    from accelerate import init_empty_weights
    from transformers import AutoConfig, AutoModelForCausalLM

    config = AutoConfig.from_pretrained(hf_dir)
    print(f"  Architecture: {config.architectures[0]}")

    with init_empty_weights():
        model = AutoModelForCausalLM.from_config(config, dtype=target_dtype)
    model.to_empty(device="cpu")

    os.makedirs(args.output_dir, exist_ok=True)
    model.save_pretrained(args.output_dir, state_dict=full_state_dict, max_shard_size=args.max_shard_size)
    del full_state_dict
    del model
    t2 = time.time()
    print(f"  Saved model in {t2 - t1:.1f}s")

    print("Step 3: Copying tokenizer files...")
    for fname in os.listdir(hf_dir):
        src = os.path.join(hf_dir, fname)
        dst = os.path.join(args.output_dir, fname)
        if not os.path.exists(dst):
            shutil.copy2(src, dst)
            print(f"  Copied {fname}")

    print(f"\nDone! Total time: {time.time() - t0:.1f}s")
    print(f"Output: {args.output_dir}")


if __name__ == "__main__":
    main()

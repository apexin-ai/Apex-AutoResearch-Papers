"""Convert GRASPrune output (state_dict + meta.json) to HuggingFace directory format.

Usage:
    python convert_graspune_to_hf.py \
        --model-id /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B \
        --state-dict /path/to/pruned_state_dict.safetensors \
        --meta /path/to/meta.json \
        --output-dir /path/to/output
"""
import argparse
import json
import os
import sys

import torch
from safetensors.torch import save_file

sys.path.insert(0, "/root/GRASPrune")
from rebuild import load_pruned_model as graspune_load


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--state-dict", required=True)
    parser.add_argument("--meta", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--dtype", default="bfloat16", choices=["bfloat16", "float16"])
    args = parser.parse_args()

    dtype = torch.bfloat16 if args.dtype == "bfloat16" else torch.float16

    print(f"Loading pruned model from GRASPrune output...")
    model, tokenizer, meta = graspune_load(
        model_id=args.model_id,
        state_dict_path=args.state_dict,
        meta_path=args.meta,
        torch_dtype=dtype,
        device="cpu",
        use_fast_tokenizer=True,
        trust_remote_code=True,
        local_only=True,
    )

    per_layer_intermediate_size = []
    per_layer_num_heads = []
    per_layer_num_kv_heads = []

    for layer in model.model.layers:
        per_layer_intermediate_size.append(layer.mlp.gate_proj.out_features)
        per_layer_num_heads.append(layer.self_attn.num_heads)
        per_layer_num_kv_heads.append(layer.self_attn.num_key_value_heads)

    config = model.config
    config.per_layer_intermediate_size = per_layer_intermediate_size
    config.per_layer_num_heads = per_layer_num_heads
    config.per_layer_num_kv_heads = per_layer_num_kv_heads
    config.intermediate_size = max(per_layer_intermediate_size)
    config.num_attention_heads = max(per_layer_num_heads)
    config.num_key_value_heads = max(per_layer_num_kv_heads)

    os.makedirs(args.output_dir, exist_ok=True)

    config.save_pretrained(args.output_dir)

    state_dict = model.state_dict()
    save_file(state_dict, os.path.join(args.output_dir, "model.safetensors"))
    print(f"Saved {len(state_dict)} tensors")

    tokenizer.save_pretrained(args.output_dir)

    meta_path = os.path.join(args.output_dir, "graspune_meta.json")
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2)

    print(f"Conversion complete -> {args.output_dir}")
    print(f"  MLP sizes: min={min(per_layer_intermediate_size)}, max={max(per_layer_intermediate_size)}")
    print(f"  Attn heads: min={min(per_layer_num_heads)}, max={max(per_layer_num_heads)}")
    print(f"  KV heads: min={min(per_layer_num_kv_heads)}, max={max(per_layer_num_kv_heads)}")


if __name__ == "__main__":
    main()

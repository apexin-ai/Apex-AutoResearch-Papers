#!/usr/bin/env python3
"""
Compute type embeddings from a type-list JSON using a causal LM.

Reads a JSON file mapping type_name → description, encodes each
"type_name: description" string through the model, mean-pools the
last hidden states, and saves as a dict {type_name: tensor} to .pt.

Output format matches artifacts/type_embeddings.pt used by the pipeline.

Usage:
  python compute_type_embeddings.py \
      --types configs/few_nerd_types.json \
      --model Qwen/Qwen3-32B \
      --output data/type_embeddings.pt

  python compute_type_embeddings.py \
      --types configs/ace05_entity_types.json \
      --model Qwen/Qwen3-32B \
      --output data/ace05_entity_type_embeddings.pt

  python compute_type_embeddings.py \
      --types configs/ace05_relation_types.json \
      --model Qwen/Qwen3-32B \
      --output data/ace05_relation_type_embeddings.pt \
      --batch-size 4
"""

import argparse
import json
import sys
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def load_types(path):
    """Load type_name → description dict from JSON."""
    with open(path) as f:
        types = json.load(f)
    if not isinstance(types, dict):
        print("ERROR: type file must be a JSON object {name: description}", file=sys.stderr)
        sys.exit(1)
    return types


def mean_pool_hidden(model, tokenizer, texts, batch_size=8, device="cuda"):
    """Encode texts and return mean-pooled last hidden states."""
    embeddings = []
    model.eval()

    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        inputs = tokenizer(batch, return_tensors="pt", padding=True, truncation=True,
                           max_length=512).to(device)

        with torch.no_grad():
            outputs = model(**inputs, output_hidden_states=True)
            hidden = outputs.hidden_states[-1]

        mask = inputs["attention_mask"].unsqueeze(-1).float()
        pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1e-9)
        embeddings.append(pooled.cpu())

    return torch.cat(embeddings, dim=0)


def main():
    parser = argparse.ArgumentParser(
        description="Compute type embeddings via mean-pooled causal LM hidden states"
    )
    parser.add_argument("--types", required=True, help="JSON file: {type_name: description}")
    parser.add_argument("--model", required=True, help="HuggingFace model name or local path")
    parser.add_argument("--output", required=True, help="Output .pt file path")
    parser.add_argument("--batch-size", type=int, default=8, help="Encoding batch size (default: 8)")
    parser.add_argument("--device", default="cuda", help="Device (default: cuda)")
    parser.add_argument("--dtype", default="bfloat16", choices=["float32", "float16", "bfloat16"],
                        help="Model dtype (default: bfloat16)")
    args = parser.parse_args()

    types = load_types(args.types)
    type_names = list(types.keys())
    texts = [f"{name}: {desc}" for name, desc in types.items()]

    print(f"Loaded {len(types)} types from {args.types}")
    print(f"Loading model {args.model} ({args.dtype})...")

    dtype_map = {"float32": torch.float32, "float16": torch.float16, "bfloat16": torch.bfloat16}
    model = AutoModelForCausalLM.from_pretrained(
        args.model, torch_dtype=dtype_map[args.dtype], device_map=args.device,
        trust_remote_code=True
    )
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print(f"Encoding {len(texts)} type descriptions...")
    vecs = mean_pool_hidden(model, tokenizer, texts, batch_size=args.batch_size, device=args.device)

    result = {name: vecs[i] for i, name in enumerate(type_names)}

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(result, output_path)
    print(f"Saved {len(result)} embeddings (dim={vecs.shape[1]}) to {output_path}")


if __name__ == "__main__":
    main()

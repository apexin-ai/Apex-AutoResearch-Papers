"""Compute type embeddings using a causal LM (e.g. Qwen3).

Input: Type definitions JSON, pretrained model
Output: {type_name: embedding_tensor} saved as .pt
Dependencies: torch, transformers
"""
import argparse
import logging
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

logger = logging.getLogger(__name__)


def compute_embeddings(
    model_path: str,
    type_definitions: dict,
    device: str = "cuda:0",
    batch_size: int = 8,
) -> dict:
    """Compute mean-pooled last-layer hidden states for each type.

    Args:
        model_path: Path to pretrained causal LM.
        type_definitions: {type_name: definition_text}.
        device: Torch device string.
        batch_size: Number of types to process at once.

    Returns:
        Dict mapping type_name -> embedding tensor (1D, hidden_dim).
    """
    logger.info("Loading model from %s", model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        device_map=device,
        trust_remote_code=True,
    )
    model.eval()

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    type_names = list(type_definitions.keys())
    type_texts = [
        f"Entity type: {name}. Definition: {defn}."
        for name, defn in type_definitions.items()
    ]

    embeddings = {}
    for i in range(0, len(type_texts), batch_size):
        batch_names = type_names[i : i + batch_size]
        batch_texts = type_texts[i : i + batch_size]

        inputs = tokenizer(
            batch_texts, return_tensors="pt", padding=True, truncation=True, max_length=512
        ).to(device)

        with torch.no_grad():
            outputs = model(**inputs, output_hidden_states=True)

        last_hidden = outputs.hidden_states[-1]  # [B, seq_len, hidden_dim]
        attention_mask = inputs["attention_mask"].unsqueeze(-1)  # [B, seq_len, 1]
        masked_hidden = last_hidden * attention_mask
        summed = masked_hidden.sum(dim=1)  # [B, hidden_dim]
        counts = attention_mask.sum(dim=1)  # [B, 1]
        mean_pooled = (summed / counts).cpu()  # [B, hidden_dim]

        for j, name in enumerate(batch_names):
            embeddings[name] = mean_pooled[j]

        logger.info("Computed embeddings for types %d-%d / %d", i, i + len(batch_names), len(type_names))

    return embeddings


def main():
    parser = argparse.ArgumentParser(description="Compute type embeddings with a causal LM")
    parser.add_argument("--model_path", required=True, help="Path to pretrained model")
    parser.add_argument("--types_file", required=True, help="Type definitions JSON path")
    parser.add_argument("--output_path", required=True, help="Output .pt file path")
    parser.add_argument("--device", default="cuda:0", help="Torch device")
    parser.add_argument("--batch_size", type=int, default=8, help="Batch size for encoding")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    import json
    with open(args.types_file, "r") as f:
        type_definitions = json.load(f)

    logger.info("Loaded %d type definitions", len(type_definitions))
    embeddings = compute_embeddings(args.model_path, type_definitions, args.device, args.batch_size)

    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)
    torch.save(embeddings, args.output_path)
    logger.info("Saved embeddings to %s", args.output_path)


if __name__ == "__main__":
    main()

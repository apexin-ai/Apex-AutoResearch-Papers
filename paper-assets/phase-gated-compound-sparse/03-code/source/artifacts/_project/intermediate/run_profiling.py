"""
PACS Profiling Entry Point.

End-to-end pipeline:
  1. Load a causal LM (HuggingFace)
  2. Load MATH-500 subset from JSON
  3. Generate reasoning traces with output_attentions=True
  4. Segment each trace into phases via PhaseSegmenter
  5. (Optional) Compute per-phase Interaction Index
  6. Save results to JSON
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict, List

import numpy as np
import torch

# ---------------------------------------------------------------------------
# Resolve sibling imports without __init__.py
# ---------------------------------------------------------------------------
_PROFILING_DIR = Path(__file__).resolve().parent
if str(_PROFILING_DIR) not in sys.path:
    sys.path.insert(0, str(_PROFILING_DIR))

from phase_segmentation import PhaseAnnotation, PhaseSegmenter

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("run_profiling")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_model_and_tokenizer(model_path: str, device: str = "cuda"):
    """Load a HuggingFace causal LM with attention output enabled."""
    from transformers import AutoModelForCausalLM, AutoTokenizer

    logger.info("Loading tokenizer from %s", model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    logger.info("Loading model from %s", model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        device_map=device,
        trust_remote_code=True,
        attn_implementation="eager",  # need full attention weights, not flash
    )
    model.eval()
    return model, tokenizer


def load_data(data_path: str) -> List[Dict[str, Any]]:
    """Load MATH-500 subset: expects a JSON list of {"problem": ..., ...}."""
    logger.info("Loading data from %s", data_path)
    with open(data_path) as f:
        data = json.load(f)
    if isinstance(data, dict) and "data" in data:
        data = data["data"]
    logger.info("Loaded %d problems", len(data))
    return data


def extract_last_layer_attention(outputs) -> torch.Tensor:
    """Extract attention weights of the last decoder layer.

    HuggingFace returns ``attentions`` as a tuple of (batch, heads, seq, seq)
    tensors, one per layer.  We take the last layer and squeeze batch dim.
    """
    attn_tuple = outputs.attentions  # tuple[layers] of (B, H, S, S)
    last_layer = attn_tuple[-1]      # (B, H, S, S)
    return last_layer[0]             # (H, S, S)


def annotation_to_dict(ann: PhaseAnnotation, problem_id: str) -> Dict[str, Any]:
    """Serialize a PhaseAnnotation to a JSON-safe dict."""
    return {
        "problem_id": problem_id,
        "num_phases": len(ann.phases),
        "boundaries": ann.boundaries,
        "phases": [
            {
                "name": p.name,
                "start": p.start,
                "end": p.end,
                "mean_sparsity": round(p.mean_sparsity, 6),
            }
            for p in ann.phases
        ],
        "sparsity_stats": {
            "mean": round(float(ann.sparsity.mean()), 6),
            "std": round(float(ann.sparsity.std()), 6),
            "min": round(float(ann.sparsity.min()), 6),
            "max": round(float(ann.sparsity.max()), 6),
        },
    }


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

@torch.no_grad()
def run_profiling(args: argparse.Namespace) -> None:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, tokenizer = load_model_and_tokenizer(args.model_path, device=device)
    data = load_data(args.data_path)

    segmenter = PhaseSegmenter(
        bandwidth=args.kde_bandwidth,
        min_phase_length=args.min_phase_length,
    )

    os.makedirs(args.output_dir, exist_ok=True)
    results: List[Dict[str, Any]] = []

    for idx, item in enumerate(data):
        problem_text = item.get("problem", item.get("question", ""))
        problem_id = item.get("id", str(idx))
        logger.info("[%d/%d] Processing problem %s", idx + 1, len(data), problem_id)

        prompt = f"Solve the following math problem step by step.\n\nProblem: {problem_text}\n\nSolution:"
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        prompt_len = inputs["input_ids"].shape[1]

        outputs = model.generate(
            **inputs,
            max_new_tokens=args.max_new_tokens,
            do_sample=False,
            output_attentions=True,
            return_dict_in_generate=True,
        )

        # For greedy generation with output_attentions, HF returns attentions
        # per generated step.  We concatenate the last-layer attention from
        # the prefill pass (which covers the prompt + first token).
        # For a lightweight MVP we profile only the prefill attention.
        if hasattr(outputs, "attentions") and outputs.attentions is not None:
            # outputs.attentions is a tuple of length num_generated_tokens,
            # each element is a tuple of layers, each (B, H, 1, S).
            # The first step's attention covers the full prompt.
            first_step_attentions = outputs.attentions[0]  # tuple[layers]
            last_layer_attn = first_step_attentions[-1][0]  # (H, prompt_len, prompt_len)
        else:
            logger.warning(
                "No attentions returned for problem %s. "
                "Model may use flash attention; set attn_implementation='eager'.",
                problem_id,
            )
            continue

        # Phase segmentation
        annotation = segmenter.segment(last_layer_attn)
        result = annotation_to_dict(annotation, problem_id)

        # Decode generated text for reference
        gen_ids = outputs.sequences[0][prompt_len:]
        result["generated_text"] = tokenizer.decode(gen_ids, skip_special_tokens=True)
        result["generated_length"] = len(gen_ids)

        results.append(result)
        logger.info(
            "  -> %d phases, boundaries at %s",
            len(annotation.phases),
            annotation.boundaries,
        )

    # Save
    out_path = os.path.join(args.output_dir, "profiling_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    logger.info("Results saved to %s (%d problems)", out_path, len(results))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="PACS Phase Profiling — attention sparsity analysis"
    )
    parser.add_argument(
        "--model_path", type=str, required=True,
        help="Path or HF model ID for the causal LM",
    )
    parser.add_argument(
        "--data_path", type=str, required=True,
        help="Path to MATH-500 subset JSON",
    )
    parser.add_argument(
        "--output_dir", type=str, default="./profiling_output",
        help="Directory for output JSON (default: ./profiling_output)",
    )
    parser.add_argument(
        "--max_new_tokens", type=int, default=2048,
        help="Max tokens to generate per problem (default: 2048)",
    )
    parser.add_argument(
        "--batch_size", type=int, default=1,
        help="Batch size (default: 1, for 7B single-GPU)",
    )
    parser.add_argument(
        "--kde_bandwidth", type=str, default="scott",
        help="KDE bandwidth method: scott / silverman / float (default: scott)",
    )
    parser.add_argument(
        "--min_phase_length", type=int, default=10,
        help="Min tokens per phase segment (default: 10)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    run_profiling(parse_args())

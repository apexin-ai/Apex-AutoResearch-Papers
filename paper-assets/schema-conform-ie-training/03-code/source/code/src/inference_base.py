# Zero-shot inference with base Qwen3.5-9B (no GRPO training).
# Serves as comparison group (C) — catastrophic forgetting sanity check.
# Usage: python src/inference_base.py --model_name Qwen/Qwen3.5-9B --data_dir /data \
#            --eval_datasets ace2005_test crossner_politics crossner_science

import argparse
import json
import os

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from src.evaluate import load_eval_dataset, evaluate_dataset, print_summary, EXTRA_METRICS, CONFORMANCE_METRICS
from src.rewards import REWARD_NAMES


def main():
    parser = argparse.ArgumentParser(
        description="Base model zero-shot IE inference (group C)"
    )
    parser.add_argument(
        "--model_name", default="Qwen/Qwen3.5-9B",
        help="HuggingFace model name or local path",
    )
    parser.add_argument(
        "--eval_datasets", nargs="+",
        default=["ace2005_test", "crossner_politics", "crossner_science"],
        help="Datasets to evaluate",
    )
    parser.add_argument("--data_dir", required=True, help="Root data directory")
    parser.add_argument(
        "--output_dir", default="./eval_results/base_model",
        help="Output directory for results",
    )
    parser.add_argument("--max_new_tokens", type=int, default=1024)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    print(f"Loading base model: {args.model_name}")
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    if tokenizer.chat_template and "enable_thinking" in tokenizer.chat_template:
        tokenizer.chat_template = tokenizer.chat_template.replace(
            "{{- '<think>\\n' }}", "{{- '<think>\\n\\n</think>\\n\\n' }}"
        )
    model.eval()

    all_results: dict[str, dict] = {}
    for ds_name in args.eval_datasets:
        print(f"\n{'=' * 60}\nEvaluating (base model): {ds_name}\n{'=' * 60}")
        samples = load_eval_dataset(ds_name, args.data_dir)
        print(f"Loaded {len(samples)} samples")
        pred_dir = os.path.join(args.output_dir, "predictions")
        pred_path = os.path.join(pred_dir, f"base_{ds_name}.jsonl")
        results = evaluate_dataset(
            model, tokenizer, samples, args.max_new_tokens, args.verbose,
            predictions_path=pred_path,
        )
        all_results[ds_name] = results

        print(f"\nResults ({results['n_samples']} samples):")
        for metric in REWARD_NAMES + EXTRA_METRICS + CONFORMANCE_METRICS:
            if metric in results:
                m = results[metric]
                print(f"  {metric}: {m['mean']:.4f} +/- {m['std']:.4f}")

    output_path = os.path.join(args.output_dir, "base_model_results.json")
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {output_path}")

    print_summary(all_results, args.eval_datasets)


if __name__ == "__main__":
    main()

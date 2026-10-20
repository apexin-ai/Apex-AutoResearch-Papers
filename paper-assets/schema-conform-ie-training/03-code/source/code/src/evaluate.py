# Evaluation script for Schema-Conformance IE models.
# Usage: python src/evaluate.py --model_path ./output/merged --eval_datasets ace2005_test crossner_politics --data_dir /data
# Computes all 5 reward metrics per eval dataset and outputs a JSON report.

import argparse
import json
import os
import sys
from collections import defaultdict

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from src.data_utils import (
    load_ace2005_dygiepp,
    load_ace2005_json,
    load_scierc_dygiepp,
    load_crossner,
    format_ie_prompt_chat,
    ACE2005_SCHEMA,
    SCIERC_SCHEMA,
    CROSSNER_SCHEMAS,
)
from src.rewards import compute_all_rewards, compute_entity_relation_f1, REWARD_NAMES
from src.schema_utils import parse_model_output

EXTRA_METRICS = ["entity_f1", "relation_f1"]
CONFORMANCE_METRICS = ["valid_json_rate", "conformance_type", "conformance_relational", "conformance_completeness"]


def load_eval_dataset(name: str, data_dir: str) -> list[dict]:
    """Load an evaluation dataset by name."""
    if name == "ace2005_test":
        for subdir in ["ace2005", "ace05", ""]:
            try:
                path = os.path.join(data_dir, subdir) if subdir else data_dir
                return load_ace2005_dygiepp(path, split="test")
            except FileNotFoundError:
                continue
        raise FileNotFoundError(f"ACE2005 test set not found in {data_dir}")

    if name == "scierc_test":
        for subdir in ["scierc", "sciERC", "SciERC", ""]:
            try:
                path = os.path.join(data_dir, subdir) if subdir else data_dir
                return load_scierc_dygiepp(path, split="test")
            except FileNotFoundError:
                continue
        raise FileNotFoundError(f"SciERC test set not found in {data_dir}")

    if name.startswith("crossner_"):
        domain = name.replace("crossner_", "")
        for subdir in ["crossner", "CrossNER", ""]:
            try:
                path = os.path.join(data_dir, subdir) if subdir else data_dir
                return load_crossner(path, domain, split="test")
            except FileNotFoundError:
                continue
        raise FileNotFoundError(f"CrossNER {domain} test not found in {data_dir}")

    raise ValueError(f"Unknown eval dataset: {name}")


@torch.no_grad()
def generate_output(
    model, tokenizer, messages: list[dict], max_new_tokens: int = 1024
) -> str:
    """Generate model output for a single sample."""
    input_text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True,
        enable_thinking=False,
    )
    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=False,
        pad_token_id=tokenizer.pad_token_id,
    )

    generated_ids = outputs[0][inputs["input_ids"].shape[1] :]
    return tokenizer.decode(generated_ids, skip_special_tokens=False).strip()


def evaluate_dataset(
    model,
    tokenizer,
    samples: list[dict],
    max_new_tokens: int = 1024,
    verbose: bool = False,
    predictions_path: str | None = None,
) -> dict:
    """Evaluate model on a dataset. Returns aggregated metrics.

    If predictions_path is set, saves per-sample predictions as JSONL.
    """
    try:
        from tqdm import tqdm
        iterator = tqdm(samples, desc="Evaluating")
    except ImportError:
        iterator = samples

    metrics: dict[str, list[float]] = defaultdict(list)
    predictions: list[dict] = []

    for sample in iterator:
        messages = format_ie_prompt_chat(sample["text"], sample["schema"])
        output_str = generate_output(model, tokenizer, messages, max_new_tokens)
        rewards = compute_all_rewards(output_str, sample["schema"], sample["gold"])
        for k, v in rewards.items():
            metrics[k].append(v)

        f1_breakdown = compute_entity_relation_f1(output_str, sample["schema"], sample["gold"])
        metrics["entity_f1"].append(f1_breakdown["entity_f1"])
        if f1_breakdown["relation_f1"] is not None:
            metrics["relation_f1"].append(f1_breakdown["relation_f1"])

        parsed, _ = parse_model_output(output_str)
        metrics["valid_json_rate"].append(1.0 if parsed is not None else 0.0)
        metrics["conformance_type"].append(rewards["type_conformance"])
        metrics["conformance_relational"].append(rewards["relational_constraint"])
        metrics["conformance_completeness"].append(rewards["structural_completeness"])

        predictions.append({
            "text": sample["text"],
            "prediction": output_str,
            "parsed": parsed,
            "rewards": rewards,
            "entity_f1": f1_breakdown["entity_f1"],
            "relation_f1": f1_breakdown["relation_f1"],
        })

        if verbose:
            print(f"  Text: {sample['text'][:80]}...")
            print(f"  Output: {output_str[:120]}...")
            print(f"  Rewards: {rewards}\n")

    if predictions_path:
        os.makedirs(os.path.dirname(predictions_path), exist_ok=True)
        with open(predictions_path, "w") as f:
            for pred in predictions:
                f.write(json.dumps(pred, ensure_ascii=False) + "\n")
        print(f"  Predictions saved to {predictions_path}")

    results: dict[str, Any] = {"n_samples": len(samples)}
    for k, values in metrics.items():
        mean = sum(values) / len(values) if values else 0.0
        var = sum((v - mean) ** 2 for v in values) / len(values) if values else 0.0
        results[k] = {"mean": round(mean, 4), "std": round(var**0.5, 4)}

    return results


def print_summary(all_results: dict[str, dict], eval_datasets: list[str]) -> None:
    """Print a comparison table across datasets."""
    col_width = max(len(ds) for ds in eval_datasets) + 2
    header = f"{'Metric':<28}" + "".join(f"{ds:>{col_width}}" for ds in eval_datasets)
    print(f"\n{'=' * len(header)}")
    print("Summary")
    print(f"{'=' * len(header)}")
    print(header)
    print("-" * len(header))

    for metric in REWARD_NAMES + EXTRA_METRICS + CONFORMANCE_METRICS:
        row = f"{metric:<28}"
        for ds in eval_datasets:
            if metric in all_results.get(ds, {}):
                val = all_results[ds][metric]["mean"]
                row += f"{val:>{col_width}.4f}"
            else:
                row += f"{'N/A':>{col_width}}"
        print(row)


def main():
    parser = argparse.ArgumentParser(description="Evaluate Schema-Conformance IE model")
    parser.add_argument("--model_path", required=True, help="Path to trained model")
    parser.add_argument("--model_label", default=None, help="Label for prediction files (e.g. 'groupA', 'groupB', 'base')")
    parser.add_argument(
        "--eval_datasets", nargs="+",
        default=["scierc_test", "crossner_politics", "crossner_science"],
        help="Eval dataset names",
    )
    parser.add_argument("--data_dir", required=True, help="Root data directory")
    parser.add_argument("--output_dir", default="./eval_results", help="Output dir for results JSON")
    parser.add_argument("--max_new_tokens", type=int, default=1024)
    parser.add_argument("--verbose", action="store_true", help="Print per-sample outputs")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    # Load model
    print(f"Loading model from {args.model_path}")
    model = AutoModelForCausalLM.from_pretrained(
        args.model_path,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    if tokenizer.chat_template and "enable_thinking" in tokenizer.chat_template:
        tokenizer.chat_template = tokenizer.chat_template.replace(
            "{{- '<think>\\n' }}", "{{- '<think>\\n\\n</think>\\n\\n' }}"
        )
    model.eval()

    # Evaluate
    all_results: dict[str, dict] = {}
    for ds_name in args.eval_datasets:
        print(f"\n{'=' * 60}\nEvaluating: {ds_name}\n{'=' * 60}")
        samples = load_eval_dataset(ds_name, args.data_dir)
        print(f"Loaded {len(samples)} samples")

        pred_path = None
        if args.model_label:
            pred_dir = os.path.join(args.output_dir, "predictions")
            pred_path = os.path.join(pred_dir, f"{args.model_label}_{ds_name}.jsonl")

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

    # Save
    output_path = os.path.join(args.output_dir, "eval_results.json")
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {output_path}")

    print_summary(all_results, args.eval_datasets)


if __name__ == "__main__":
    main()

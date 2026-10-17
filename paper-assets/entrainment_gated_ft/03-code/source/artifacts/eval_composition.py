#!/usr/bin/env python3
"""
L-Sequential Function Composition Evaluation
Based on Ye et al. (arXiv 2602.01763) theoretical construction.

Tests whether hybrid linear-full attention models can perform
multi-step function composition in a single forward pass.
"""

import argparse
import json
import os
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional

import numpy as np
import torch

from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig

try:
    from fla.models.gated_deltanet import GatedDeltaNetConfig, GatedDeltaNetForCausalLM
    AutoConfig.register("gated_deltanet", GatedDeltaNetConfig)
    AutoModelForCausalLM.register(GatedDeltaNetConfig, GatedDeltaNetForCausalLM)
except (ImportError, ValueError):
    pass

try:
    from fla.models.hgrn2 import HGRN2Config, HGRN2ForCausalLM
    AutoConfig.register("hgrn2", HGRN2Config)
    AutoModelForCausalLM.register(HGRN2Config, HGRN2ForCausalLM)
except (ImportError, ValueError):
    pass


# ---------------------------------------------------------------------------
# Task generation
# ---------------------------------------------------------------------------

ALPHABET_SIZE = 10  # digits 0-9


@dataclass
class CompositionTask:
    depth: int
    functions: list[list[int]]  # functions[l][i] = f_l(i)
    input_val: int
    answer: int
    intermediates: list[int]  # [f1(x), f2(f1(x)), ...]


def _random_function(rng: np.random.RandomState, size: int = ALPHABET_SIZE) -> list[int]:
    return rng.randint(0, size, size=size).tolist()


def _compose(functions: list[list[int]], x: int) -> tuple[int, list[int]]:
    intermediates = []
    val = x
    for f in functions:
        val = f[val]
        intermediates.append(val)
    return val, intermediates


def generate_composition_task(
    depth: int,
    rng: np.random.RandomState,
    alphabet_size: int = ALPHABET_SIZE,
) -> CompositionTask:
    functions = [_random_function(rng, alphabet_size) for _ in range(depth)]
    input_val = rng.randint(0, alphabet_size)
    answer, intermediates = _compose(functions, input_val)
    return CompositionTask(
        depth=depth,
        functions=functions,
        input_val=input_val,
        answer=answer,
        intermediates=intermediates,
    )


# ---------------------------------------------------------------------------
# Prompt formatting
# ---------------------------------------------------------------------------

def _format_function_line(func: list[int], label: str) -> str:
    entries = " ".join(f"{i}->{func[i]}" for i in range(len(func)))
    return f"{label}: {entries}"


def _format_demo_direct(task: CompositionTask) -> str:
    lines = []
    for l, f in enumerate(task.functions):
        label = "f" if task.depth == 1 else f"f{l+1}"
        lines.append(_format_function_line(f, label))
    lines.append(f"Input: {task.input_val}")
    lines.append(f"Answer: {task.answer}")
    return "\n".join(lines)


def _format_demo_cot(task: CompositionTask) -> str:
    lines = []
    for l, f in enumerate(task.functions):
        label = "f" if task.depth == 1 else f"f{l+1}"
        lines.append(_format_function_line(f, label))
    lines.append(f"Input: {task.input_val}")

    chain_parts = []
    prev = task.input_val
    for l in range(task.depth):
        label = "f" if task.depth == 1 else f"f{l+1}"
        chain_parts.append(f"{label}({prev})={task.intermediates[l]}")
        prev = task.intermediates[l]
    lines.append(" ".join(chain_parts))
    lines.append(f"Answer: {task.answer}")
    return "\n".join(lines)


def _format_test_query(task: CompositionTask) -> str:
    lines = []
    for l, f in enumerate(task.functions):
        label = "f" if task.depth == 1 else f"f{l+1}"
        lines.append(_format_function_line(f, label))
    lines.append(f"Input: {task.input_val}")
    lines.append("Answer:")
    return "\n".join(lines)


def _get_instruction(depth: int, variant: str) -> str:
    if variant == "direct":
        if depth == 1:
            return "Apply the function to the input."
        return "Compose the functions and give the final answer."
    else:
        if depth == 1:
            return "Apply the function to the input."
        return "Compose the functions step by step."


def format_prompt(
    demo_tasks: list[CompositionTask],
    test_task: CompositionTask,
    variant: str = "direct",
) -> str:
    depth = test_task.depth
    instruction = _get_instruction(depth, variant)

    fmt_demo = _format_demo_cot if variant == "cot" else _format_demo_direct
    parts = [instruction, ""]
    for dt in demo_tasks:
        parts.append(fmt_demo(dt))
        parts.append("")
    parts.append(_format_test_query(test_task))
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Dataset generation (deterministic, saved to JSON)
# ---------------------------------------------------------------------------

@dataclass
class EvalInstance:
    prompt: str
    answer: int
    depth: int
    sample_idx: int
    test_task: dict


def generate_dataset(
    depth: int,
    num_samples: int = 500,
    num_shots: int = 8,
    variant: str = "direct",
    base_seed: int = 42,
) -> list[EvalInstance]:
    instances = []
    for idx in range(num_samples):
        seed = base_seed + depth * 100000 + idx
        rng = np.random.RandomState(seed)

        demo_tasks = [generate_composition_task(depth, rng) for _ in range(num_shots)]
        test_task = generate_composition_task(depth, rng)

        prompt = format_prompt(demo_tasks, test_task, variant=variant)
        instances.append(EvalInstance(
            prompt=prompt,
            answer=test_task.answer,
            depth=depth,
            sample_idx=idx,
            test_task=asdict(test_task),
        ))
    return instances


def save_dataset(instances: list[EvalInstance], path: str):
    data = [
        {
            "prompt": inst.prompt,
            "answer": inst.answer,
            "depth": inst.depth,
            "sample_idx": inst.sample_idx,
            "test_task": inst.test_task,
        }
        for inst in instances
    ]
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} instances to {path}")


def load_dataset(path: str) -> list[dict]:
    with open(path) as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Model evaluation
# ---------------------------------------------------------------------------

def evaluate_model(
    model_path: str,
    instances: list[dict],
    batch_size: int = 64,
    max_new_tokens: int = 1,
    device: str = "cuda",
) -> dict:
    print(f"Loading model from {model_path} ...")
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        trust_remote_code=True,
        torch_dtype=torch.bfloat16,
        device_map=device,
    )
    model.eval()

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.padding_side = "left"

    # map answer digits to token ids
    digit_token_ids = {}
    for d in range(10):
        ids = tokenizer.encode(str(d), add_special_tokens=False)
        digit_token_ids[d] = ids[-1]

    correct = 0
    total = 0
    predictions = []

    for start in range(0, len(instances), batch_size):
        batch = instances[start : start + batch_size]
        prompts = [inst["prompt"] for inst in batch]
        answers = [inst["answer"] for inst in batch]

        encodings = tokenizer(
            prompts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=2048,
        ).to(device)

        with torch.no_grad():
            outputs = model.generate(
                **encodings,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                temperature=None,
                top_p=None,
            )

        for i, (out, ans) in enumerate(zip(outputs, answers)):
            generated_ids = out[encodings["input_ids"].shape[1]:]
            generated_text = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()

            pred = None
            for ch in generated_text:
                if ch.isdigit():
                    pred = int(ch)
                    break

            is_correct = pred == ans
            correct += int(is_correct)
            total += 1
            predictions.append({
                "sample_idx": batch[i]["sample_idx"],
                "answer": ans,
                "prediction": pred,
                "generated_text": generated_text,
                "correct": is_correct,
            })

        print(f"  [{total}/{len(instances)}] running accuracy: {correct/total:.4f}")

    accuracy = correct / total if total > 0 else 0.0
    return {
        "model_path": model_path,
        "accuracy": accuracy,
        "correct": correct,
        "total": total,
        "predictions": predictions,
    }


# ---------------------------------------------------------------------------
# Main experiment loop
# ---------------------------------------------------------------------------

def run_experiment(
    model_list: list[str],
    depths: list[int],
    num_samples: int = 500,
    num_shots: int = 8,
    variant: str = "direct",
    batch_size: int = 64,
    output_dir: str = "results",
    base_seed: int = 42,
    device: str = "cuda",
):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    dataset_dir = output_path / "datasets"
    dataset_dir.mkdir(exist_ok=True)

    # Step 1: generate and save datasets for each depth
    datasets = {}
    for depth in depths:
        ds_path = dataset_dir / f"depth_{depth}_{variant}_n{num_samples}.json"
        if ds_path.exists():
            print(f"Loading existing dataset: {ds_path}")
            datasets[depth] = load_dataset(str(ds_path))
        else:
            print(f"Generating dataset: depth={depth}, n={num_samples}, variant={variant}")
            instances = generate_dataset(
                depth=depth,
                num_samples=num_samples,
                num_shots=num_shots,
                variant=variant,
                base_seed=base_seed,
            )
            save_dataset(instances, str(ds_path))
            datasets[depth] = load_dataset(str(ds_path))

    # Step 2: token length validation
    print("\n--- Token length validation ---")
    sample_model = model_list[0]
    tokenizer = AutoTokenizer.from_pretrained(sample_model, trust_remote_code=True)
    for depth in depths:
        lengths = [
            len(tokenizer.encode(inst["prompt"]))
            for inst in datasets[depth][:20]
        ]
        print(f"  depth={depth}: mean={np.mean(lengths):.0f}, max={max(lengths)}, min={min(lengths)}")
        if max(lengths) > 2048:
            print(f"  WARNING: depth={depth} exceeds 2048 tokens!")
    del tokenizer

    # Step 3: evaluate each model on each depth
    max_new_tokens = 1 if variant == "direct" else 30
    all_results = []

    for model_path in model_list:
        model_name = Path(model_path).name
        print(f"\n{'='*60}")
        print(f"Evaluating: {model_name}")
        print(f"{'='*60}")

        for depth in depths:
            print(f"\n--- Depth {depth} ---")
            t0 = time.time()
            result = evaluate_model(
                model_path=model_path,
                instances=datasets[depth],
                batch_size=batch_size,
                max_new_tokens=max_new_tokens,
                device=device,
            )
            elapsed = time.time() - t0

            result_entry = {
                "model_name": model_name,
                "model_path": model_path,
                "depth": depth,
                "variant": variant,
                "accuracy": result["accuracy"],
                "correct": result["correct"],
                "total": result["total"],
                "elapsed_seconds": elapsed,
            }
            all_results.append(result_entry)

            # save per-model-depth predictions
            pred_path = output_path / f"predictions_{model_name}_depth{depth}_{variant}.json"
            with open(pred_path, "w") as f:
                json.dump(result["predictions"], f, indent=2)

            print(f"  accuracy={result['accuracy']:.4f}  ({elapsed:.1f}s)")

    # Step 4: save summary
    summary_path = output_path / f"summary_{variant}.json"
    with open(summary_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSummary saved to {summary_path}")

    # print summary table
    print(f"\n{'='*60}")
    print(f"RESULTS SUMMARY (variant={variant})")
    print(f"{'='*60}")
    header = f"{'Model':<30}" + "".join(f"{'D='+str(d):>8}" for d in depths)
    print(header)
    print("-" * len(header))
    for model_path in model_list:
        model_name = Path(model_path).name
        row = f"{model_name:<30}"
        for depth in depths:
            entry = next(
                (r for r in all_results if r["model_name"] == model_name and r["depth"] == depth),
                None,
            )
            if entry:
                row += f"{entry['accuracy']:>8.4f}"
            else:
                row += f"{'N/A':>8}"
        print(row)

    return all_results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="L-Sequential Function Composition Evaluation"
    )
    parser.add_argument(
        "--models", nargs="+", required=True,
        help="Paths to model directories (HuggingFace format)",
    )
    parser.add_argument(
        "--depths", nargs="+", type=int, default=[1, 2, 3, 4, 5],
        help="Composition depths to evaluate (default: 1 2 3 4 5)",
    )
    parser.add_argument(
        "--num-samples", type=int, default=500,
        help="Number of test samples per depth (default: 500)",
    )
    parser.add_argument(
        "--num-shots", type=int, default=8,
        help="Number of in-context demonstrations (default: 8)",
    )
    parser.add_argument(
        "--variant", choices=["direct", "cot"], default="direct",
        help="Prompt variant: direct (no CoT) or cot (chain-of-thought)",
    )
    parser.add_argument(
        "--batch-size", type=int, default=64,
        help="Batch size for inference (default: 64)",
    )
    parser.add_argument(
        "--output-dir", type=str, default="results/func_comp",
        help="Output directory for results",
    )
    parser.add_argument(
        "--seed", type=int, default=42,
        help="Base random seed (default: 42)",
    )
    parser.add_argument(
        "--device", type=str, default="cuda",
        help="Device for inference (default: cuda)",
    )
    parser.add_argument(
        "--generate-only", action="store_true",
        help="Only generate datasets, skip model evaluation",
    )
    parser.add_argument(
        "--print-sample", action="store_true",
        help="Print a sample prompt for each depth and exit",
    )

    args = parser.parse_args()

    if args.print_sample:
        for depth in args.depths:
            rng = np.random.RandomState(args.seed + depth * 100000)
            demos = [generate_composition_task(depth, rng) for _ in range(args.num_shots)]
            test = generate_composition_task(depth, rng)
            prompt = format_prompt(demos, test, variant=args.variant)
            print(f"\n{'='*60}")
            print(f"DEPTH {depth} ({args.variant})")
            print(f"{'='*60}")
            print(prompt)
            print(f"\n[Expected answer: {test.answer}]")
        return

    if args.generate_only:
        output_path = Path(args.output_dir) / "datasets"
        output_path.mkdir(parents=True, exist_ok=True)
        for depth in args.depths:
            instances = generate_dataset(
                depth=depth,
                num_samples=args.num_samples,
                num_shots=args.num_shots,
                variant=args.variant,
                base_seed=args.seed,
            )
            ds_path = output_path / f"depth_{depth}_{args.variant}_n{args.num_samples}.json"
            save_dataset(instances, str(ds_path))
        return

    run_experiment(
        model_list=args.models,
        depths=args.depths,
        num_samples=args.num_samples,
        num_shots=args.num_shots,
        variant=args.variant,
        batch_size=args.batch_size,
        output_dir=args.output_dir,
        base_seed=args.seed,
        device=args.device,
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Log-probability evaluation for function composition tasks."""

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

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

try:
    from fla.models.retnet import RetNetConfig, RetNetForCausalLM
    AutoConfig.register("retnet", RetNetConfig)
    AutoModelForCausalLM.register(RetNetConfig, RetNetForCausalLM)
except (ImportError, ValueError):
    pass

try:
    from fla.models.deltanet import DeltaNetConfig, DeltaNetForCausalLM
    AutoConfig.register("deltanet", DeltaNetConfig)
    AutoModelForCausalLM.register(DeltaNetConfig, DeltaNetForCausalLM)
except (ImportError, ValueError):
    pass


# ---------------------------------------------------------------------------
# Task generation (copied from eval_composition.py for self-containedness)
# ---------------------------------------------------------------------------

ALPHABET_SIZE = 10


def _random_function(rng, size=ALPHABET_SIZE):
    return rng.randint(0, size, size=size).tolist()


def _compose(functions, x):
    intermediates = []
    val = x
    for f in functions:
        val = f[val]
        intermediates.append(val)
    return val, intermediates


def generate_composition_task(depth, rng, alphabet_size=ALPHABET_SIZE):
    functions = [_random_function(rng, alphabet_size) for _ in range(depth)]
    input_val = rng.randint(0, alphabet_size)
    answer, intermediates = _compose(functions, input_val)
    return {
        "depth": depth,
        "functions": functions,
        "input_val": input_val,
        "answer": answer,
        "intermediates": intermediates,
    }


def _format_function_line(func, label):
    entries = " ".join(f"{i}->{func[i]}" for i in range(len(func)))
    return f"{label}: {entries}"


def _format_demo_direct(task):
    lines = []
    depth = task["depth"]
    for l, f in enumerate(task["functions"]):
        label = "f" if depth == 1 else f"f{l+1}"
        lines.append(_format_function_line(f, label))
    lines.append(f"Input: {task['input_val']}")
    lines.append(f"Answer: {task['answer']}")
    return "\n".join(lines)


def _format_demo_cot(task):
    lines = []
    depth = task["depth"]
    for l, f in enumerate(task["functions"]):
        label = "f" if depth == 1 else f"f{l+1}"
        lines.append(_format_function_line(f, label))
    lines.append(f"Input: {task['input_val']}")
    chain_parts = []
    prev = task["input_val"]
    for l in range(depth):
        label = "f" if depth == 1 else f"f{l+1}"
        chain_parts.append(f"{label}({prev})={task['intermediates'][l]}")
        prev = task["intermediates"][l]
    lines.append(" ".join(chain_parts))
    lines.append(f"Answer: {task['answer']}")
    return "\n".join(lines)


def _format_test_query(task):
    lines = []
    depth = task["depth"]
    for l, f in enumerate(task["functions"]):
        label = "f" if depth == 1 else f"f{l+1}"
        lines.append(_format_function_line(f, label))
    lines.append(f"Input: {task['input_val']}")
    lines.append("Answer:")
    return "\n".join(lines)


def _format_test_query_cot(task):
    lines = []
    depth = task["depth"]
    for l, f in enumerate(task["functions"]):
        label = "f" if depth == 1 else f"f{l+1}"
        lines.append(_format_function_line(f, label))
    lines.append(f"Input: {task['input_val']}")
    return "\n".join(lines)


def _get_instruction(depth, variant):
    if variant == "direct":
        if depth == 1:
            return "Apply the function to the input."
        return "Compose the functions and give the final answer."
    else:
        if depth == 1:
            return "Apply the function to the input."
        return "Compose the functions step by step."


def format_prompt(demo_tasks, test_task, variant="direct"):
    depth = test_task["depth"]
    instruction = _get_instruction(depth, variant)
    fmt_demo = _format_demo_cot if variant == "cot" else _format_demo_direct
    parts = [instruction, ""]
    for dt in demo_tasks:
        parts.append(fmt_demo(dt))
        parts.append("")
    if variant == "cot":
        parts.append(_format_test_query_cot(test_task))
    else:
        parts.append(_format_test_query(test_task))
    return "\n".join(parts)


def generate_dataset(depth, num_samples, num_shots, variant, base_seed):
    instances = []
    for idx in range(num_samples):
        seed = base_seed + depth * 100000 + idx
        rng = np.random.RandomState(seed)
        demo_tasks = [generate_composition_task(depth, rng) for _ in range(num_shots)]
        test_task = generate_composition_task(depth, rng)
        prompt = format_prompt(demo_tasks, test_task, variant=variant)
        instances.append({
            "prompt": prompt,
            "answer": test_task["answer"],
            "depth": depth,
            "sample_idx": idx,
        })
    return instances


# ---------------------------------------------------------------------------
# Log-probability evaluation
# ---------------------------------------------------------------------------

def get_digit_token_ids(tokenizer):
    digit_token_ids = []
    for d in range(10):
        ids = tokenizer.encode(str(d), add_special_tokens=False)
        digit_token_ids.append(ids[-1])
    print(f"Digit token IDs: {digit_token_ids}")
    for d in range(10):
        decoded = tokenizer.decode([digit_token_ids[d]])
        print(f"  {d} -> token_id={digit_token_ids[d]}, decoded='{decoded}'")
    return digit_token_ids


def evaluate_logprob(model, tokenizer, instances, digit_token_ids, batch_size, device):
    results = []
    n_batches = (len(instances) + batch_size - 1) // batch_size

    for batch_idx in range(n_batches):
        start = batch_idx * batch_size
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
            outputs = model(**encodings)

        for i in range(len(batch)):
            seq_len = encodings["attention_mask"][i].sum().item()
            last_logits = outputs.logits[i, seq_len - 1, :]

            digit_logits = last_logits[digit_token_ids]
            digit_probs = F.softmax(digit_logits, dim=0)
            digit_logprobs = F.log_softmax(digit_logits, dim=0)

            correct_idx = answers[i]
            correct_logprob = digit_logprobs[correct_idx].item()
            correct_prob = digit_probs[correct_idx].item()

            sorted_indices = digit_logits.argsort(descending=True)
            rank = (sorted_indices == correct_idx).nonzero(as_tuple=True)[0].item() + 1

            incorrect_mask = torch.ones(10, dtype=torch.bool, device=device)
            incorrect_mask[correct_idx] = False
            max_incorrect = digit_logprobs[incorrect_mask].max().item()
            margin = correct_logprob - max_incorrect

            top1_digit = sorted_indices[0].item()

            results.append({
                "sample_idx": batch[i]["sample_idx"],
                "answer": correct_idx,
                "correct_rank": rank,
                "correct_logprob": correct_logprob,
                "correct_prob": correct_prob,
                "max_incorrect_logprob": max_incorrect,
                "margin": margin,
                "top1_digit": top1_digit,
                "top1_correct": int(top1_digit == correct_idx),
                "digit_probs": digit_probs.cpu().tolist(),
            })

        if (batch_idx + 1) % 10 == 0 or batch_idx == n_batches - 1:
            print(f"  Batch {batch_idx+1}/{n_batches} done")

    return results


def summarize_results(results):
    ranks = [r["correct_rank"] for r in results]
    probs = [r["correct_prob"] for r in results]
    logprobs = [r["correct_logprob"] for r in results]
    margins = [r["margin"] for r in results]
    top1_correct = [r["top1_correct"] for r in results]

    rank_dist = [0] * 10
    for r in ranks:
        rank_dist[r - 1] += 1

    return {
        "num_samples": len(results),
        "mean_correct_rank": float(np.mean(ranks)),
        "std_correct_rank": float(np.std(ranks)),
        "mean_correct_prob": float(np.mean(probs)),
        "std_correct_prob": float(np.std(probs)),
        "mean_correct_logprob": float(np.mean(logprobs)),
        "mean_margin": float(np.mean(margins)),
        "std_margin": float(np.std(margins)),
        "fraction_rank_1": float(np.mean(top1_correct)),
        "rank_distribution": rank_dist,
    }


# ---------------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------------

def run_experiment(
    model_list,
    depths,
    num_samples,
    num_shots,
    variant,
    batch_size,
    output_dir,
    base_seed,
    device,
):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    datasets = {}
    for depth in depths:
        datasets[depth] = generate_dataset(depth, num_samples, num_shots, variant, base_seed)
        print(f"Generated {len(datasets[depth])} instances for depth={depth}")

    all_summaries = []

    for model_path in model_list:
        model_name = Path(model_path).name
        print(f"\n{'='*60}")
        print(f"Model: {model_name}")
        print(f"{'='*60}")

        print(f"Loading model from {model_path} ...")
        t0 = time.time()
        tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            trust_remote_code=True,
            torch_dtype=torch.bfloat16,
            device_map=device,
        )
        if getattr(model.config, 'tie_word_embeddings', False):
            oe = model.get_output_embeddings()
            ie = model.get_input_embeddings()
            if oe is not None and ie is not None and oe.weight.data_ptr() != ie.weight.data_ptr():
                oe.weight = ie.weight
        model.eval()

        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
            tokenizer.padding_side = "left"

        digit_token_ids = get_digit_token_ids(tokenizer)
        digit_token_ids_tensor = torch.tensor(digit_token_ids, dtype=torch.long, device=device)

        load_time = time.time() - t0
        print(f"Model loaded in {load_time:.1f}s")

        for depth in depths:
            print(f"\n--- Depth={depth} ---")
            t1 = time.time()
            results = evaluate_logprob(
                model, tokenizer, datasets[depth],
                digit_token_ids_tensor, batch_size, device,
            )
            eval_time = time.time() - t1

            summary = summarize_results(results)
            summary["model_name"] = model_name
            summary["model_path"] = model_path
            summary["depth"] = depth
            summary["eval_time_seconds"] = round(eval_time, 1)
            all_summaries.append(summary)

            print(f"  mean_rank={summary['mean_correct_rank']:.2f}  "
                  f"mean_prob={summary['mean_correct_prob']:.4f}  "
                  f"frac_rank1={summary['fraction_rank_1']:.4f}  "
                  f"mean_margin={summary['mean_margin']:.4f}  "
                  f"({eval_time:.1f}s)")

            detail_path = output_path / f"{model_name}_depth{depth}_details.json"
            with open(detail_path, "w") as f:
                json.dump(results, f, indent=2)

        del model
        torch.cuda.empty_cache()

    # Save summary
    summary_path = output_path / "summary_logprob.json"
    with open(summary_path, "w") as f:
        json.dump(all_summaries, f, indent=2)
    print(f"\nSummary saved to {summary_path}")

    # Print table
    print(f"\n{'='*100}")
    print("RESULTS SUMMARY (mean_rank / mean_prob / frac_rank1)")
    print(f"{'='*100}")
    depth_headers = "".join(f"{'D='+str(d):>20}" for d in depths)
    header = f"{'Model':<45}{depth_headers}"
    print(header)
    print("-" * len(header))

    for model_path in model_list:
        model_name = Path(model_path).name
        row = f"{model_name:<45}"
        for depth in depths:
            entry = next(
                (s for s in all_summaries if s["model_name"] == model_name and s["depth"] == depth),
                None,
            )
            if entry:
                cell = f"{entry['mean_correct_rank']:.1f}/{entry['mean_correct_prob']:.3f}/{entry['fraction_rank_1']:.3f}"
                row += f"{cell:>20}"
            else:
                row += f"{'N/A':>20}"
        print(row)

    row = f"{'Random (uniform)': <45}"
    for _ in depths:
        cell = f"5.5/0.100/0.100"
        row += f"{cell:>20}"
    print(row)

    return all_summaries


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Log-probability evaluation for function composition")
    parser.add_argument("--models", nargs="+", required=True)
    parser.add_argument("--depths", nargs="+", type=int, default=[1, 2, 3, 4, 5])
    parser.add_argument("--num-samples", type=int, default=500)
    parser.add_argument("--num-shots", type=int, default=6)
    parser.add_argument("--variant", choices=["direct", "cot"], default="direct")
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--output-dir", type=str, default="results/logprob")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", type=str, default="cuda:0")
    args = parser.parse_args()

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

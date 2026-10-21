"""Execute the full G-theory experiment from a design matrix.

Supports multiple benchmarks (MMLU, GSM8K, ARC-Challenge, HellaSwag) via
the --benchmark flag.  Default is MMLU for backward compatibility with exp-001.

Input:
    - design_matrix.csv  (from ``generate_design.py``)
    - items JSON          (benchmark-specific)
    - few_shot JSON          (auto-selected per benchmark, or --zero-shot)

Output:
    - results/experiment_results.jsonl — one JSON object per item × condition
"""

import argparse
import json
import re
import sys
from pathlib import Path

import pandas as pd

from src.config.model_paths import resolve_model_path
from src.data.prompt_templates import ANSWER_MAP, format_prompt
from src.inference.benchmark_utils import (
    BENCHMARK_MAX_TOKENS,
    BENCHMARK_STOP_SEQS,
    extract_gsm8k_answer,
    extract_math_answer,
    extract_mc_answer,
    format_arc_prompt,
    format_gsm8k_prompt,
    format_hellaswag_prompt,
    format_math_prompt,
    get_mc_gold,
    score_gsm8k,
    score_math,
    score_mc,
)
from src.inference.vllm_runner import VLLMRunner

ANSWER_PATTERN = re.compile(r"^\s*([A-Da-d])\b")

DEFAULT_ITEMS = {
    "mmlu": "data/mmlu_items.json",
    "gsm8k": "data/gsm8k_items_exp002.json",
    "arc": "data/arc_items_exp002.json",
    "hellaswag": "data/hellaswag_items_exp002.json",
    "math": "data/math_items_exp002.json",
}

DEFAULT_FEW_SHOT = {
    "mmlu": "data/few_shot_examples.json",
    "gsm8k": "data/few_shot_gsm8k.json",
    "arc": "data/few_shot_arc.json",
    "hellaswag": "data/few_shot_hellaswag.json",
    "math": "data/few_shot_math.json",
}


def extract_answer(text: str) -> str | None:
    """Extract a single A/B/C/D letter from the start of generated text."""
    m = ANSWER_PATTERN.match(text)
    return m.group(1).upper() if m else None


def load_data(items_path: str, few_shot_path: str):
    with open(items_path) as f:
        items = json.load(f)
    with open(few_shot_path) as f:
        few_shot = json.load(f)
    return items, few_shot


def _build_prompt(benchmark: str, item: dict, template_id: int,
                  ordering: int, few_shot: dict | None) -> str:
    """Route to the correct prompt builder based on benchmark."""
    if benchmark == "mmlu":
        subject = item["subject"]
        examples = few_shot[subject][str(ordering)] if few_shot else None
        return format_prompt(
            template_id=template_id,
            subject=subject,
            question=item["question"],
            choices=item["choices"],
            few_shot_examples=examples,
        )
    elif benchmark == "gsm8k":
        return format_gsm8k_prompt(template_id, item["question"], few_shot)
    elif benchmark == "arc":
        labels = item.get("metadata", {}).get("labels")
        return format_arc_prompt(
            template_id, item["question"], item["choices"], labels, few_shot
        )
    elif benchmark == "hellaswag":
        return format_hellaswag_prompt(
            template_id, item["question"], item["choices"], few_shot
        )
    elif benchmark == "math":
        return format_math_prompt(template_id, item["question"], few_shot)
    raise ValueError(f"Unknown benchmark: {benchmark}")


def _extract_and_score(benchmark: str, generated_text: str, item: dict):
    """Extract predicted answer and score it.

    Returns (predicted, gold, correct, text_exact_match).
    """
    if benchmark == "mmlu":
        predicted = extract_answer(generated_text)
        gold = ANSWER_MAP[item["answer_idx"]]
        correct = int(predicted == gold) if predicted else 0
        text_exact_match = int(generated_text.strip() == gold)
    elif benchmark == "gsm8k":
        predicted = extract_gsm8k_answer(generated_text)
        gold = item["answer"]
        correct = score_gsm8k(predicted, gold)
        raw = item.get("metadata", {}).get("raw_answer", "")
        text_exact_match = int(generated_text.strip() == raw.strip())
    elif benchmark in ("arc", "hellaswag"):
        predicted = extract_mc_answer(generated_text)
        gold = get_mc_gold(benchmark, item)
        correct = score_mc(predicted, gold)
        text_exact_match = int(generated_text.strip() == gold)
    elif benchmark == "math":
        predicted = extract_math_answer(generated_text)
        gold = item["answer"]
        correct = score_math(predicted, gold)
        text_exact_match = int(predicted == gold if predicted else False)
    else:
        raise ValueError(f"Unknown benchmark: {benchmark}")
    return predicted, gold, correct, text_exact_match


def run_experiment(
    design_path: str,
    items_path: str,
    output_path: str,
    benchmark: str = "mmlu",
    few_shot_path: str | None = None,
    precision_filter: str | None = None,
    gpu_id: int = 0,
    max_conditions: int = 0,
    max_items: int = 0,
    offset: int = 0,
    tensor_parallel_size: int = 1,
) -> None:
    """Run all conditions in the design matrix.

    Args:
        design_path: Path to ``design_matrix.csv``.
        items_path: Path to items JSON file.
        output_path: Destination JSONL path.
        benchmark: Benchmark name (mmlu, gsm8k, arc, hellaswag).
        few_shot_path: Path to few-shot examples (MMLU only).
        precision_filter: If set, only run conditions matching this precision.
        gpu_id: GPU device index passed to VLLMRunner.
        max_conditions: If >0, limit total conditions to run (for dry-run).
        max_items: If >0, limit items per condition (for dry-run).
        offset: Skip first N conditions (for multi-GPU sharding).
    """
    df = pd.read_csv(design_path)
    if precision_filter:
        df = df[df["precision"] == precision_filter]
        if df.empty:
            print(f"No conditions for precision={precision_filter}", file=sys.stderr)
            return

    if offset > 0:
        df = df.iloc[offset:]
        print(f"[shard] Skipping first {offset} conditions")

    if max_conditions > 0:
        df = df.head(max_conditions)
        print(f"[shard] Running {len(df)} conditions (offset={offset}, max={max_conditions})")

    if few_shot_path:
        items, few_shot = load_data(items_path, few_shot_path)
    else:
        with open(items_path) as f:
            items = json.load(f)
        few_shot = None

    if max_items > 0:
        items = items[:max_items]
        print(f"[dry-run] Limiting to {max_items} items per condition")

    max_tokens = BENCHMARK_MAX_TOKENS.get(benchmark, 16)
    stop_seqs = BENCHMARK_STOP_SEQS.get(benchmark)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    groups = df.groupby(["model", "precision"])

    with open(output_path, "w") as outfile:
        for (model_name, precision), group_df in groups:
            init_seed = int(group_df.iloc[0]["seed"])

            model_path = resolve_model_path(model_name)
            print(f"Loading {model_name} ({precision}) → {model_path}")
            runner = VLLMRunner(model_path, gpu_id, precision, init_seed, tensor_parallel_size)

            for _, row in group_df.iterrows():
                cond_id = int(row["condition_id"])
                temperature = float(row["temperature"])
                top_p_raw = row["top_p"]
                top_p = float(top_p_raw) if top_p_raw != "" and pd.notna(top_p_raw) else None
                prompt_template = int(row["prompt_template"])
                seed = int(row["seed"])
                ordering = int(row["ordering"])

                prompts: list[str] = []
                item_meta: list[dict] = []
                for item in items:
                    prompt_text = _build_prompt(
                        benchmark, item, prompt_template, ordering, few_shot
                    )
                    prompts.append(prompt_text)
                    item_meta.append(item)

                results = runner.generate(
                    prompts, temperature, top_p, seed,
                    logprobs=5, max_tokens=max_tokens, stop=stop_seqs,
                )

                n_correct = 0
                for result, item in zip(results, item_meta):
                    predicted, gold, correct, text_exact_match = _extract_and_score(
                        benchmark, result.generated_text, item
                    )
                    n_correct += correct

                    record = {
                        "condition_id": cond_id,
                        "item_id": item["item_id"],
                        "benchmark": benchmark,
                        "subject": item.get("subject"),
                        "model": model_name,
                        "precision": precision,
                        "temperature": temperature,
                        "top_p": top_p,
                        "prompt_template": prompt_template,
                        "seed": seed,
                        "ordering": ordering,
                        "generated_text": result.generated_text,
                        "predicted_answer": predicted,
                        "gold_answer": gold,
                        "correct": correct,
                        "text_exact_match": text_exact_match,
                        "latency_ms": result.latency_ms,
                        "answer_logprob": result.answer_logprob,
                        "top_logprobs": result.top_logprobs,
                    }
                    outfile.write(json.dumps(record, ensure_ascii=False) + "\n")

                outfile.flush()
                print(
                    f"  Condition {cond_id:>3d}: "
                    f"{n_correct}/{len(items)} correct"
                )

            del runner

    print(f"Experiment complete → {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run G-theory experiment")
    parser.add_argument("--design", default="design_matrix.csv")
    parser.add_argument("--items", default=None,
                        help="Path to items JSON (auto-selected per benchmark if omitted)")
    parser.add_argument("--few-shot", default=None,
                        help="Path to few-shot JSON (auto-selected per benchmark if omitted)")
    parser.add_argument("--zero-shot", action="store_true",
                        help="Disable few-shot examples")
    parser.add_argument("--output", default="results/experiment_results.jsonl")
    parser.add_argument(
        "--benchmark",
        default="mmlu",
        choices=["mmlu", "gsm8k", "arc", "hellaswag", "math"],
        help="Benchmark to run (default: mmlu)",
    )
    parser.add_argument(
        "--precision",
        default=None,
        help="Only run conditions for this precision (float32, bfloat16, float16)",
    )
    parser.add_argument(
        "--gpu-id",
        type=int,
        default=0,
        help="GPU device index passed to VLLMRunner",
    )
    parser.add_argument(
        "--max-conditions",
        type=int,
        default=0,
        help="Limit conditions to run (0 = all, for dry-run)",
    )
    parser.add_argument(
        "--max-items",
        type=int,
        default=0,
        help="Limit items per condition (0 = all, for dry-run)",
    )
    parser.add_argument(
        "--offset",
        type=int,
        default=0,
        help="Skip first N conditions (for multi-GPU sharding)",
    )
    parser.add_argument(
        "--tensor-parallel",
        type=int,
        default=1,
        help="Tensor parallel size (number of GPUs for model sharding)",
    )
    args = parser.parse_args()

    items_path = args.items or DEFAULT_ITEMS.get(args.benchmark, "data/mmlu_items.json")
    if args.zero_shot:
        few_shot_path = None
    elif args.few_shot:
        few_shot_path = args.few_shot
    else:
        default_fs = DEFAULT_FEW_SHOT.get(args.benchmark)
        few_shot_path = default_fs if default_fs and Path(default_fs).exists() else None

    run_experiment(
        args.design, items_path, args.output,
        benchmark=args.benchmark,
        few_shot_path=few_shot_path,
        precision_filter=args.precision,
        gpu_id=args.gpu_id,
        max_conditions=args.max_conditions,
        max_items=args.max_items,
        offset=args.offset,
        tensor_parallel_size=args.tensor_parallel,
    )

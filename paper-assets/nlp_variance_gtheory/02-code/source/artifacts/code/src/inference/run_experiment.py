"""Execute the full G-theory experiment from a design matrix.

Reads the factorial design CSV, groups conditions by (model, precision) to
minimise model reloads, then for every condition × item constructs a prompt
and runs vLLM inference.  Results are scored via exact-match extraction of
A/B/C/D from generated text and written to a JSONL file.

Input:
    - design_matrix.csv  (from ``generate_design.py``)
    - mmlu_items.json    (from ``sample_mmlu.py``)
    - few_shot_examples.json (from ``few_shot.py``)

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
from src.inference.vllm_runner import VLLMRunner

ANSWER_PATTERN = re.compile(r"^\s*([A-Da-d])\b")


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


def run_experiment(
    design_path: str,
    items_path: str,
    few_shot_path: str,
    output_path: str,
    precision_filter: str | None = None,
    gpu_id: int = 0,
    max_conditions: int = 0,
    max_items: int = 0,
    offset: int = 0,
) -> None:
    """Run all conditions in the design matrix.

    Args:
        design_path: Path to ``design_matrix.csv``.
        items_path: Path to ``mmlu_items.json``.
        few_shot_path: Path to ``few_shot_examples.json``.
        output_path: Destination JSONL path.
        precision_filter: If set, only run conditions matching this precision.
        gpu_id: GPU device index passed to VLLMRunner.
        max_conditions: If >0, limit total conditions to run (for dry-run).
        max_items: If >0, limit items per condition (for dry-run).
        offset: Skip first N conditions (for multi-GPU sharding).
    """
    df = pd.read_csv(design_path)
    if "benchmark" in df.columns:
        df = df[df["benchmark"] == benchmark]
        if df.empty:
            print(f"No conditions for benchmark={benchmark}", file=sys.stderr)
            return
        print(f"[filter] {len(df)} conditions for benchmark={benchmark}")
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

    items, few_shot = load_data(items_path, few_shot_path)
    if max_items > 0:
        items = items[:max_items]
        print(f"[dry-run] Limiting to {max_items} items per condition")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    groups = df.groupby(["model", "precision"])

    with open(output_path, "w") as outfile:
        for (model_name, precision), group_df in groups:
            init_seed = int(group_df.iloc[0]["seed"])

            model_path = resolve_model_path(model_name)
            print(f"Loading {model_name} ({precision}) → {model_path}")
            runner = VLLMRunner(model_path, gpu_id, precision, init_seed)

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
                    subject = item["subject"]
                    examples = few_shot[subject][str(ordering)]
                    prompt_text = format_prompt(
                        template_id=prompt_template,
                        subject=subject,
                        question=item["question"],
                        choices=item["choices"],
                        few_shot_examples=examples,
                    )
                    prompts.append(prompt_text)
                    item_meta.append(item)

                results = runner.generate(prompts, temperature, top_p, seed, logprobs=5)

                n_correct = 0
                for result, item in zip(results, item_meta):
                    predicted = extract_answer(result.generated_text)
                    gold = ANSWER_MAP[item["answer_idx"]]
                    correct = int(predicted == gold) if predicted else 0
                    n_correct += correct

                    record = {
                        "condition_id": cond_id,
                        "item_id": item["item_id"],
                        "subject": item["subject"],
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
    parser.add_argument("--items", default="data/mmlu_items.json")
    parser.add_argument("--few-shot", default="data/few_shot_examples.json")
    parser.add_argument("--output", default="results/experiment_results.jsonl")
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
    args = parser.parse_args()

    run_experiment(
        args.design, args.items, args.few_shot, args.output,
        args.precision, args.gpu_id, args.max_conditions, args.max_items,
        args.offset,
    )

"""Generate fully crossed factorial design matrix for the G-theory study.

Supports two experiment versions:

exp001 (original, MMLU-only)
    4 models × 3 precisions × 3 temperatures × 6 prompts × 6 seeds × 4 orderings
    = 5,184 conditions

exp002 (multi-benchmark)
    4 models × 4 benchmarks × 1 precision × 2 temperatures × 6 prompts × 6 seeds × 4 orderings
    = 4,608 conditions
    Precision: bf16 only — Gemma doesn't support fp16; exp-001 confirmed bf16≈fp16.
    Temperature: 0.0/0.7 only — T=0.3 dropped for efficiency (exp-001 showed it clusters with T=0.7).
"""

import argparse
import itertools
from pathlib import Path

import pandas as pd

MODELS = [
    "Qwen/Qwen3-8B",
    "meta-llama/Llama-3.1-8B-Instruct",
    "google/gemma-2-9b-it",
    "mistralai/Mistral-7B-Instruct-v0.3",
]

SCALE_MODELS = [
    "Qwen/Qwen2.5-3B-Instruct",
    "Qwen/Qwen2.5-7B-Instruct",
    "Qwen/Qwen2.5-72B-Instruct",
]

EXPERIMENTS = {
    "exp001": {
        "model": MODELS,
        "precision": ["float32", "bfloat16", "float16"],
        "temperature_config": [
            {"temperature": 0.0, "top_p": None},
            {"temperature": 0.3, "top_p": 0.9},
            {"temperature": 0.7, "top_p": 0.9},
        ],
        "prompt_template": [1, 2, 3, 4, 5, 6],
        "seed": [42, 123, 456, 789, 1024, 2048],
        "ordering": [1, 2, 3, 4],
        "expected_total": 5184,
    },
    "exp002": {
        "model": MODELS,
        "benchmark": ["mmlu", "gsm8k", "arc", "hellaswag", "math"],
        # bf16 only — Gemma doesn't support fp16; exp-001 confirmed bf16≈fp16
        "precision": ["bfloat16"],
        # T=0.0 and T=0.7 only — T=0.3 dropped for efficiency
        "temperature_config": [
            {"temperature": 0.0, "top_p": None},
            {"temperature": 0.7, "top_p": 0.9},
        ],
        "prompt_template": [1, 2, 3, 4, 5, 6],
        "seed": [42, 123, 456, 789, 1024, 2048],
        "ordering": [1, 2, 3, 4],
        "expected_total": 5760,
    },
    "exp003_scale": {
        "model": SCALE_MODELS,
        "benchmark": ["mmlu"],
        "precision": ["bfloat16"],
        "temperature_config": [
            {"temperature": 0.0, "top_p": None},
            {"temperature": 0.7, "top_p": 0.9},
        ],
        "prompt_template": [1, 2, 3, 4, 5, 6],
        "seed": [42, 123, 456, 789, 1024, 2048],
        "ordering": [1, 2, 3, 4],
        "expected_total": 864,
    },
}

ITEMS_FILE_MAP = {
    "mmlu": "data/mmlu_items_exp001.json",
    "gsm8k": "data/gsm8k_items_exp002.json",
    "arc": "data/arc_items_exp002.json",
    "hellaswag": "data/hellaswag_items_exp002.json",
    "math": "data/math_items_exp002.json",
}


def generate_matrix(
    experiment: str = "exp001",
    output_path: str | None = None,
) -> pd.DataFrame:
    """Build the full factorial design and write to CSV."""
    if experiment not in EXPERIMENTS:
        raise ValueError(f"Unknown experiment: {experiment}. Choose from {list(EXPERIMENTS)}")

    design = EXPERIMENTS[experiment]
    has_benchmark = "benchmark" in design

    if output_path is None:
        output_path = f"design_matrix_{experiment}.csv"

    factor_lists = []
    factor_names = []
    for key in ["model", "benchmark", "precision", "temperature_config",
                 "prompt_template", "seed", "ordering"]:
        if key in design:
            factor_lists.append(design[key])
            factor_names.append(key)

    rows: list[dict] = []
    condition_id = 0

    for combo in itertools.product(*factor_lists):
        condition_id += 1
        factors = dict(zip(factor_names, combo))

        temp_cfg = factors.pop("temperature_config")
        row = {
            "condition_id": condition_id,
            "model": factors["model"],
        }
        if has_benchmark:
            row["benchmark"] = factors["benchmark"]
            row["items_file"] = ITEMS_FILE_MAP[factors["benchmark"]]

        row.update({
            "precision": factors["precision"],
            "temperature": temp_cfg["temperature"],
            "top_p": temp_cfg["top_p"] if temp_cfg["top_p"] is not None else "",
            "prompt_template": factors["prompt_template"],
            "seed": factors["seed"],
            "ordering": factors["ordering"],
        })
        rows.append(row)

    df = pd.DataFrame(rows)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    expected = design["expected_total"]
    assert len(df) == expected, f"Expected {expected} conditions, got {len(df)}"
    print(f"[{experiment}] Generated {len(df)} conditions → {output_path}")
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate G-theory factorial design matrix"
    )
    parser.add_argument(
        "--experiment", default="exp001", choices=list(EXPERIMENTS),
        help="Experiment version (default: exp001)",
    )
    parser.add_argument("--output", default=None, help="Output CSV path")
    args = parser.parse_args()
    generate_matrix(experiment=args.experiment, output_path=args.output)

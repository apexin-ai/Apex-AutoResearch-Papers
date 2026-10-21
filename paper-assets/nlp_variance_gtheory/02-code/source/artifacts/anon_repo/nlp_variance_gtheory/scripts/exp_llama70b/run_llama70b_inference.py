"""
Llama-3.1-70B-Instruct inference for G-theory variance study.

Runs 5 benchmarks sequentially (MMLU first), 288 conditions each.
288 conditions = 2 temps x 6 prompts x 6 seeds x 4 orderings.
Each condition evaluates 200 items -> 57,600 evals per benchmark.
Total: 1,440 conditions x 200 items = 288,000 evaluations.

Usage:
    cd .
    python scripts/exp_llama70b/run_llama70b_inference.py
"""

import itertools
import os
import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
os.chdir(PROJECT_ROOT)
sys.path.insert(0, str(PROJECT_ROOT))

from src.inference.run_experiment import run_experiment

MODEL_PATH = "meta-llama/Llama-3.1-70B-Instruct"
TENSOR_PARALLEL = 4
PRECISION = "bfloat16"

BENCHMARKS = ["mmlu", "gsm8k", "arc", "hellaswag", "math"]

ITEMS_FILE_MAP = {
    "mmlu": "data/mmlu_items_exp001.json",
    "gsm8k": "data/gsm8k_items_exp002.json",
    "arc": "data/arc_items_exp002.json",
    "hellaswag": "data/hellaswag_items_exp002.json",
    "math": "data/math_items_exp002.json",
}

FEW_SHOT_MAP = {
    "mmlu": "data/few_shot_examples.json",
    "gsm8k": "data/few_shot_gsm8k.json",
    "arc": "data/few_shot_arc.json",
    "hellaswag": "data/few_shot_hellaswag.json",
    "math": "data/few_shot_math.json",
}

TEMPERATURE_CONFIGS = [
    {"temperature": 0.0, "top_p": None},
    {"temperature": 0.7, "top_p": 0.9},
]
PROMPT_TEMPLATES = [1, 2, 3, 4, 5, 6]
SEEDS = [42, 123, 456, 789, 1024, 2048]
ORDERINGS = [1, 2, 3, 4]

OUTPUT_DIR = Path("data/exp_llama70b")


def generate_design_matrix(benchmark: str) -> str:
    rows = []
    cond_id = 0
    for temp_cfg, prompt, seed, ordering in itertools.product(
        TEMPERATURE_CONFIGS, PROMPT_TEMPLATES, SEEDS, ORDERINGS
    ):
        cond_id += 1
        rows.append({
            "condition_id": cond_id,
            "model": MODEL_PATH,
            "benchmark": benchmark,
            "items_file": ITEMS_FILE_MAP[benchmark],
            "precision": PRECISION,
            "temperature": temp_cfg["temperature"],
            "top_p": temp_cfg["top_p"] if temp_cfg["top_p"] is not None else "",
            "prompt_template": prompt,
            "seed": seed,
            "ordering": ordering,
        })

    df = pd.DataFrame(rows)
    assert len(df) == 288, f"Expected 288 conditions, got {len(df)}"

    design_path = str(OUTPUT_DIR / f"design_llama70b_{benchmark}.csv")
    df.to_csv(design_path, index=False)
    print(f"Generated {len(df)} conditions -> {design_path}")
    return design_path


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for benchmark in BENCHMARKS:
        output_path = str(OUTPUT_DIR / f"llama70b_{benchmark}.jsonl")

        if Path(output_path).exists():
            n_existing = sum(1 for _ in open(output_path))
            print(f"[{benchmark}] Output exists with {n_existing} records, skipping.")
            continue

        print(f"\n{'='*60}")
        print(f"Running {benchmark} (Llama-3.1-70B-Instruct, TP={TENSOR_PARALLEL})")
        print(f"{'='*60}")

        design_path = generate_design_matrix(benchmark)
        few_shot_path = FEW_SHOT_MAP.get(benchmark)
        if few_shot_path and not Path(few_shot_path).exists():
            few_shot_path = None

        run_experiment(
            design_path=design_path,
            items_path=ITEMS_FILE_MAP[benchmark],
            output_path=output_path,
            benchmark=benchmark,
            few_shot_path=few_shot_path,
            tensor_parallel_size=TENSOR_PARALLEL,
        )

        print(f"[{benchmark}] Complete -> {output_path}")

    print("\nAll benchmarks complete.")


if __name__ == "__main__":
    main()

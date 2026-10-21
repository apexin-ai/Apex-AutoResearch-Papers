"""Generate design matrices for exp-001b (3 samples × 432 conditions each).

Single model (Llama-3.1-8B-Instruct), single precision (bfloat16),
full cross of temperature × prompt × seed × ordering.
"""

import itertools
from pathlib import Path

import pandas as pd

DESIGN = {
    "model": ["meta-llama/Llama-3.1-8B-Instruct"],
    "precision": ["bfloat16"],
    "temperature_config": [
        {"temperature": 0.0, "top_p": None},
        {"temperature": 0.3, "top_p": 0.9},
        {"temperature": 0.7, "top_p": 0.9},
    ],
    "prompt_template": [1, 2, 3, 4, 5, 6],
    "seed": [42, 123, 456, 789, 1024, 2048],
    "ordering": [1, 2, 3, 4],
}

LOCAL_MODEL_PATH = "meta-llama/Llama-3.1-8B-Instruct"


def generate_for_sample(sample_id: int, output_dir: Path) -> pd.DataFrame:
    rows = []
    condition_id = 0

    for model, prec, temp_cfg, prompt, seed, ordering in itertools.product(
        DESIGN["model"],
        DESIGN["precision"],
        DESIGN["temperature_config"],
        DESIGN["prompt_template"],
        DESIGN["seed"],
        DESIGN["ordering"],
    ):
        condition_id += 1
        rows.append({
            "condition_id": condition_id,
            "model": LOCAL_MODEL_PATH,
            "precision": prec,
            "temperature": temp_cfg["temperature"],
            "top_p": temp_cfg["top_p"] if temp_cfg["top_p"] is not None else "",
            "prompt_template": prompt,
            "seed": seed,
            "ordering": ordering,
        })

    df = pd.DataFrame(rows)
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / "design.csv"
    df.to_csv(path, index=False)
    assert len(df) == 432, f"Expected 432 conditions, got {len(df)}"
    print(f"Sample {sample_id}: {len(df)} conditions → {path}")
    return df


def main():
    proj = Path(".")
    for s in range(1, 4):
        out_dir = proj / f"results/exp001b/sample{s}"
        generate_for_sample(s, out_dir)
    print("Done.")


if __name__ == "__main__":
    main()

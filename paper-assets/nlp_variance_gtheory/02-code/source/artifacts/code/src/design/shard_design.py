"""Shuffle and shard a design matrix for multi-GPU parallel execution.

Reads a design CSV, optionally filters by model, shuffles rows with a
fixed seed, excludes already-completed condition IDs, and splits the
remainder into N equal shards (one per GPU).

Output: N CSV files named {output_dir}/shard_{i}.csv
"""

import argparse
from pathlib import Path

import pandas as pd


def shard_design(
    input_path: str,
    output_dir: str,
    n_shards: int = 4,
    shuffle_seed: int = 42,
    model_filter: str | None = None,
    exclude_condition_ids: list[int] | None = None,
    local_model_path: str | None = None,
) -> list[str]:
    """Shuffle, filter, exclude, and split a design matrix.

    Args:
        input_path: Path to full design_matrix CSV.
        output_dir: Directory for shard CSVs.
        n_shards: Number of GPU shards.
        shuffle_seed: Random seed for reproducible shuffle.
        model_filter: If set, keep only rows matching this model name.
        exclude_condition_ids: Condition IDs already completed (e.g. pilot).
        local_model_path: If set, replace model column with this local path.

    Returns:
        List of shard file paths.
    """
    df = pd.read_csv(input_path)

    if model_filter:
        df = df[df["model"] == model_filter]
        print(f"Filtered to model={model_filter}: {len(df)} conditions")

    if exclude_condition_ids:
        before = len(df)
        df = df[~df["condition_id"].isin(exclude_condition_ids)]
        print(f"Excluded {before - len(df)} pilot conditions, {len(df)} remaining")

    df = df.sample(frac=1, random_state=shuffle_seed).reset_index(drop=True)
    print(f"Shuffled with seed={shuffle_seed}")

    if local_model_path:
        df["model"] = local_model_path
        print(f"Replaced model column with: {local_model_path}")

    Path(output_dir).mkdir(parents=True, exist_ok=True)
    shard_paths = []
    shard_size = len(df) // n_shards
    for i in range(n_shards):
        start = i * shard_size
        end = start + shard_size if i < n_shards - 1 else len(df)
        shard_df = df.iloc[start:end]
        path = f"{output_dir}/shard_{i}.csv"
        shard_df.to_csv(path, index=False)
        shard_paths.append(path)
        print(f"Shard {i}: {len(shard_df)} conditions → {path}")

    return shard_paths


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Shard design matrix for multi-GPU")
    parser.add_argument("--input", required=True, help="Full design matrix CSV")
    parser.add_argument("--output-dir", required=True, help="Output directory for shards")
    parser.add_argument("--n-shards", type=int, default=4)
    parser.add_argument("--shuffle-seed", type=int, default=42)
    parser.add_argument("--model-filter", default=None)
    parser.add_argument(
        "--exclude-ids", default=None,
        help="Comma-separated condition IDs to exclude (pilot)",
    )
    parser.add_argument("--local-model-path", default=None)
    args = parser.parse_args()

    exclude = None
    if args.exclude_ids:
        exclude = [int(x) for x in args.exclude_ids.split(",")]

    shard_design(
        args.input, args.output_dir, args.n_shards, args.shuffle_seed,
        args.model_filter, exclude, args.local_model_path,
    )

"""Merge multi-model JSONL results into a single CSV for G-theory analysis.

Supports two modes:
- cross-model: filter to bf16+fp32 only (balanced design across all models)
- within-model: keep all precisions

Adds text_exact_match column via majority-vote mechanism.
"""

import argparse
import glob
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd


def load_jsonl_glob(pattern: str) -> pd.DataFrame:
    paths = sorted(glob.glob(pattern))
    if not paths:
        raise FileNotFoundError(f"No files matched pattern: {pattern}")

    frames = [pd.read_json(p, lines=True) for p in paths]
    df = pd.concat(frames, ignore_index=True)

    for col in ["answer_logprob"]:
        if col in df.columns:
            df[col] = df[col].replace(-np.inf, np.nan)
    if "top_logprobs" in df.columns:
        df.drop(columns=["top_logprobs"], inplace=True)

    print(f"Loaded {len(df)} observations from {len(paths)} file(s)")
    return df


def compute_text_exact_match(df: pd.DataFrame) -> pd.DataFrame:
    """Add text_exact_match column (0/1).

    For each (model, precision, prompt_template, ordering, item_id) group,
    find the most common generated_text across (temperature, seed) conditions.
    Each row scores 1 iff its generated_text equals the canonical.
    """
    group_cols = ["model", "precision", "prompt_template", "ordering", "item_id"]
    canonical = (
        df.groupby(group_cols)["generated_text"]
        .agg(lambda texts: Counter(texts).most_common(1)[0][0])
    )
    df = df.copy()
    df["text_exact_match"] = df.apply(
        lambda r: int(
            r["generated_text"]
            == canonical[tuple(r[c] for c in group_cols)]
        ),
        axis=1,
    )
    return df


def main():
    parser = argparse.ArgumentParser(
        description="Merge multi-model JSONL results for G-theory analysis"
    )
    parser.add_argument(
        "--input-glob", required=True,
        help='Glob pattern for input JSONL files (e.g. "results/exp001_*/shard_*.jsonl")',
    )
    parser.add_argument(
        "--output", required=True,
        help="Output CSV path",
    )
    parser.add_argument(
        "--cross-model", action="store_true",
        help="Filter to specified precisions only (default: bf16+fp32)",
    )
    parser.add_argument(
        "--precisions", default="bfloat16,float32",
        help="Comma-separated precision levels to keep in cross-model mode (default: bfloat16,float32)",
    )
    args = parser.parse_args()

    df = load_jsonl_glob(args.input_glob)

    print(f"Precisions in data: {sorted(df['precision'].unique())}")
    print(f"Models in data: {sorted(df['model'].unique())}")

    if args.cross_model:
        keep = [p.strip() for p in args.precisions.split(",")]
        before = len(df)
        df = df[df["precision"].isin(keep)].reset_index(drop=True)
        print(f"Cross-model filter: kept {len(df)}/{before} rows (precisions: {keep})")

    df = compute_text_exact_match(df)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output, index=False)
    print(f"Saved {len(df)} rows -> {args.output}")


if __name__ == "__main__":
    main()

"""Download and filter UltraChat-200K for multi-turn training.

Filters for conversations with >= 5 assistant turns, samples 8K examples.
Output: HuggingFace dataset saved to disk in Arrow format.
"""

import argparse

from datasets import load_dataset
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="./data/ultrachat_8k")
    parser.add_argument("--num-samples", type=int, default=8000)
    parser.add_argument("--min-turns", type=int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    print("Loading UltraChat-200K...", flush=True)
    ds = load_dataset("HuggingFaceH4/ultrachat_200k", split="train_sft")
    print(f"Total examples: {len(ds)}", flush=True)

    def has_enough_turns(example):
        assistant_turns = sum(1 for m in example["messages"] if m["role"] == "assistant")
        return assistant_turns >= args.min_turns

    ds_filtered = ds.filter(has_enough_turns)
    print(f"After filtering (>={args.min_turns} assistant turns): {len(ds_filtered)}", flush=True)

    ds_sampled = ds_filtered.shuffle(seed=args.seed).select(
        range(min(args.num_samples, len(ds_filtered)))
    )
    print(f"Sampled: {len(ds_sampled)}", flush=True)

    turn_counts = []
    for ex in ds_sampled:
        assistant_turns = sum(1 for m in ex["messages"] if m["role"] == "assistant")
        turn_counts.append(assistant_turns)

    print(f"Average assistant turns: {np.mean(turn_counts):.1f}", flush=True)
    print(f"Min/Max assistant turns: {min(turn_counts)}/{max(turn_counts)}", flush=True)

    ds_sampled.save_to_disk(args.output_dir)
    print(f"Saved to {args.output_dir}", flush=True)


if __name__ == "__main__":
    main()

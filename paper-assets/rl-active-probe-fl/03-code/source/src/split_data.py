"""Split validated samples into train/eval sets.

Splits by slug to ensure the same LeetCode problem doesn't appear in both sets.
Eval size is fixed (default 200) to preserve statistical power; train gets the rest.

Input: data/debugbench_validated.jsonl (or probes_distilled.jsonl)
Output: data/train.jsonl + data/eval.jsonl
"""

import argparse
import json
import logging
import random
from collections import Counter, defaultdict
from pathlib import Path

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Split probes into train/eval by slug"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="data/debugbench_validated.jsonl",
        help="Input JSONL (validated samples or distilled probes)",
    )
    parser.add_argument(
        "--eval-size",
        type=int,
        default=200,
        help="Target eval set size (train gets the rest)",
    )
    parser.add_argument(
        "--train-output",
        type=str,
        default="data/train.jsonl",
        help="Training set output",
    )
    parser.add_argument(
        "--eval-output",
        type=str,
        default="data/eval.jsonl",
        help="Evaluation set output",
    )
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    input_path = Path(args.input)
    samples = []
    with open(input_path) as f:
        for line in f:
            samples.append(json.loads(line))
    logger.info(f"Loaded {len(samples)} samples")

    slug_to_samples: dict[str, list[dict]] = defaultdict(list)
    for s in samples:
        slug_to_samples[s["slug"]].append(s)

    slugs = sorted(slug_to_samples.keys())
    logger.info(f"Unique slugs: {len(slugs)}")

    random.seed(args.seed)
    random.shuffle(slugs)

    total = len(samples)
    eval_target = args.eval_size

    eval_samples: list[dict] = []
    train_samples: list[dict] = []

    for slug in slugs:
        group = slug_to_samples[slug]
        if len(eval_samples) < eval_target:
            eval_samples.extend(group)
        else:
            train_samples.extend(group)

    train_path = Path(args.train_output)
    eval_path = Path(args.eval_output)
    train_path.parent.mkdir(parents=True, exist_ok=True)
    eval_path.parent.mkdir(parents=True, exist_ok=True)

    with open(train_path, "w") as f:
        for row in train_samples:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    with open(eval_path, "w") as f:
        for row in eval_samples:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"\n=== Data Split Results ===")
    print(f"Total: {total} samples, {len(slugs)} unique slugs")
    print(f"Train: {len(train_samples)} samples")
    print(f"Eval:  {len(eval_samples)} samples")

    for name, data in [("Train", train_samples), ("Eval", eval_samples)]:
        cat_counts = Counter(s["category"] for s in data)
        lvl_counts = Counter(s["level"] for s in data)
        print(f"\n{name} category distribution:")
        for cat, cnt in cat_counts.most_common():
            print(f"  {cat}: {cnt} ({cnt/len(data)*100:.1f}%)")
        print(f"{name} level distribution:")
        for lvl, cnt in lvl_counts.most_common():
            print(f"  {lvl}: {cnt} ({cnt/len(data)*100:.1f}%)")


if __name__ == "__main__":
    main()

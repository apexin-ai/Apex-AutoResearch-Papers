"""Filter DebugBench dataset to Python single-bug subset.

Input: HuggingFace dataset Rtian/DebugBench (test split)
Output: data/debugbench_python_single.jsonl
Dependencies: datasets
"""

import argparse
import json
import logging
from collections import Counter
from pathlib import Path

from datasets import load_dataset

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Filter DebugBench to Python single-bug subset"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/debugbench_python_single.jsonl",
        help="Output JSONL path (default: data/debugbench_python_single.jsonl)",
    )
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    logger.info("Loading DebugBench from HuggingFace...")
    ds = load_dataset("Rtian/DebugBench", split="test")
    logger.info(f"Total samples: {len(ds)}")

    filtered = [
        row
        for row in ds
        if row["language"] == "python3" and row["category"] != "multiple error"
    ]
    logger.info(f"Python single-bug samples: {len(filtered)}")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        for row in filtered:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    logger.info(f"Written to {output_path}")

    category_counts = Counter(row["category"] for row in filtered)
    level_counts = Counter(row["level"] for row in filtered)

    print(f"\n=== Filter Results: {len(filtered)} samples ===")
    print("\nCategory distribution:")
    for cat, cnt in category_counts.most_common():
        print(f"  {cat}: {cnt} ({cnt/len(filtered)*100:.1f}%)")
    print("\nLevel distribution:")
    for lvl, cnt in level_counts.most_common():
        print(f"  {lvl}: {cnt} ({cnt/len(filtered)*100:.1f}%)")


if __name__ == "__main__":
    main()

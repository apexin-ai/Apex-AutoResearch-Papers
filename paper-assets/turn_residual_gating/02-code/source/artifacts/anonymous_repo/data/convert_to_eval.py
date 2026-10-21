"""Convert ultrachat_8k samples to evaluation JSON format.

Output is compatible with eval_gar.py --conversations-path.
"""

import argparse
import json
import random
from datasets import load_from_disk


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", required=True, help="Path to ultrachat_8k dataset")
    parser.add_argument("--output", required=True, help="Output JSON path")
    parser.add_argument("--num-samples", type=int, default=50)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--min-turns", type=int, default=3)
    args = parser.parse_args()

    random.seed(args.seed)
    ds = load_from_disk(args.data_dir)
    print(f"Dataset size: {len(ds)}")

    indices = list(range(len(ds)))
    random.shuffle(indices)

    conversations = []
    for idx in indices:
        if len(conversations) >= args.num_samples:
            break
        messages = ds[idx]["messages"]
        num_assistant = sum(1 for m in messages if m["role"] == "assistant")
        if num_assistant < args.min_turns:
            continue
        conversations.append({
            "conversation_id": len(conversations),
            "source": "ultrachat_8k",
            "dataset_idx": idx,
            "num_turns": num_assistant,
            "messages": messages,
        })

    with open(args.output, "w") as f:
        json.dump(conversations, f, indent=2)

    turn_counts = [c["num_turns"] for c in conversations]
    print(f"Saved {len(conversations)} conversations to {args.output}")
    print(f"Turn distribution: min={min(turn_counts)}, max={max(turn_counts)}, "
          f"avg={sum(turn_counts)/len(turn_counts):.1f}")


if __name__ == "__main__":
    main()

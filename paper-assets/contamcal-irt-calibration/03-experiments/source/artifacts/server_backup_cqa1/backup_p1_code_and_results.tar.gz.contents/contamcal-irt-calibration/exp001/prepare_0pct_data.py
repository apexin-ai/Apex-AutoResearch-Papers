"""Generate 0% dosage SFT data (pure base SFT, no contamination).

Standalone script that doesn't require paraphrases to exist.
Loads SlimOrca, formats to chat messages, writes JSONL.
"""
import json
import logging
import os
import random
from pathlib import Path

from datasets import load_dataset
from tqdm import tqdm

logger = logging.getLogger(__name__)

HF_HOME = os.environ.get("HF_HOME", "/root/autodl-tmp/.hf_cache")
os.environ["HF_HOME"] = HF_HOME

ROLE_MAP = {
    "system": "system",
    "human": "user",
    "gpt": "assistant",
}


def load_slimorca(cache_dir, max_samples=50000, seed=42):
    logger.info("Loading Open-Orca/SlimOrca (max %d samples)...", max_samples)
    ds = load_dataset("Open-Orca/SlimOrca", split="train", cache_dir=cache_dir)
    if len(ds) > max_samples:
        ds = ds.shuffle(seed=seed).select(range(max_samples))
    logger.info("Selected %d samples", len(ds))

    messages_list = []
    skipped = 0
    for row in tqdm(ds, desc="Processing SlimOrca"):
        if "conversations" in row:
            convs = row["conversations"]
            if isinstance(convs, str):
                convs = json.loads(convs)
            msgs = []
            for turn in convs:
                role = ROLE_MAP.get(turn.get("from", ""), turn.get("from", ""))
                content = turn.get("value", "")
                if role and content:
                    msgs.append({"role": role, "content": content})
            if len(msgs) >= 2:
                messages_list.append({"messages": msgs})
            else:
                skipped += 1
        else:
            skipped += 1

    logger.info("Loaded %d conversations (%d skipped)", len(messages_list), skipped)
    return messages_list


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=str, default="/root/autodl-tmp/exp001/sft_data")
    parser.add_argument("--cache-dir", type=str, default="/root/autodl-tmp/.hf_cache")
    parser.add_argument("--max-samples", type=int, default=50000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    data = load_slimorca(args.cache_dir, args.max_samples, args.seed)
    rng = random.Random(args.seed)
    rng.shuffle(data)

    output_file = output_dir / "sft_dosage_000.jsonl"
    with open(output_file, "w") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    logger.info("Written %d samples to %s", len(data), output_file)

    meta = {
        "base_dataset": "Open-Orca/SlimOrca",
        "dosage": 0,
        "total_samples": len(data),
        "seed": args.seed,
        "contamination": "none",
    }
    with open(output_dir / "data_meta_0pct.json", "w") as f:
        json.dump(meta, f, indent=2)
    logger.info("Done.")


if __name__ == "__main__":
    main()

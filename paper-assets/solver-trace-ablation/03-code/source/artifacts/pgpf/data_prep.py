"""Data preparation: download OpenHermes-2.5, subsample, format for SFT, save as JSONL.

Output format (ChatML):
  {"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
"""

import argparse
import random
from pathlib import Path
from typing import Optional

from pgpf.utils import save_jsonl, load_jsonl, ensure_dir, set_seed, logger


def _format_conversation(example: dict) -> Optional[dict]:
    """Convert an OpenHermes-2.5 example to ChatML messages format."""
    conversations = example.get("conversations", [])
    if not conversations:
        return None

    messages = []
    role_map = {"system": "system", "human": "user", "gpt": "assistant"}

    for turn in conversations:
        role = role_map.get(turn.get("from", ""), None)
        if role is None:
            continue
        messages.append({"role": role, "content": turn["value"]})

    if not any(m["role"] == "assistant" for m in messages):
        return None

    return {"messages": messages}


def prepare_dataset(
    output_dir: str = "data",
    subset_size: int = 10000,
    train_size: int = 8000,
    val_size: int = 1000,
    test_size: int = 1000,
    seed: int = 42,
) -> dict[str, Path]:
    """Download OpenHermes-2.5, subsample, split, and save as JSONL."""
    from datasets import load_dataset

    set_seed(seed)
    out = ensure_dir(output_dir)

    logger.info("Loading OpenHermes-2.5 from HuggingFace...")
    ds = load_dataset("teknium/OpenHermes-2.5", split="train")

    logger.info(f"Total examples: {len(ds)}, sampling {subset_size}")
    indices = random.sample(range(len(ds)), min(subset_size, len(ds)))
    subset = ds.select(indices)

    formatted = []
    for example in subset:
        result = _format_conversation(example)
        if result is not None:
            formatted.append(result)

    random.shuffle(formatted)
    assert len(formatted) >= train_size + val_size + test_size, (
        f"Not enough valid examples ({len(formatted)}) for requested splits"
    )

    splits = {
        "train": formatted[:train_size],
        "val": formatted[train_size : train_size + val_size],
        "test": formatted[train_size + val_size : train_size + val_size + test_size],
    }

    paths = {}
    for name, data in splits.items():
        path = out / f"{name}.jsonl"
        save_jsonl(data, path)
        paths[name] = path
        logger.info(f"Saved {name}: {len(data)} examples → {path}")

    return paths


def load_dataset_splits(data_dir: str = "data") -> dict[str, list[dict]]:
    """Load pre-saved train/val/test JSONL files."""
    data_dir = Path(data_dir)
    splits = {}
    for name in ["train", "val", "test"]:
        path = data_dir / f"{name}.jsonl"
        if path.exists():
            splits[name] = load_jsonl(path)
            logger.info(f"Loaded {name}: {len(splits[name])} examples from {path}")
        else:
            logger.warning(f"{path} not found, skipping {name} split")
    return splits


def extract_assistant_texts(samples: list[dict]) -> list[str]:
    """Extract assistant turn text from ChatML formatted samples."""
    texts = []
    for sample in samples:
        for msg in sample.get("messages", []):
            if msg["role"] == "assistant":
                texts.append(msg["content"])
    return texts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prepare OpenHermes-2.5 subset for PGPF")
    parser.add_argument("--output_dir", type=str, default="data")
    parser.add_argument("--subset_size", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    prepare_dataset(output_dir=args.output_dir, subset_size=args.subset_size, seed=args.seed)

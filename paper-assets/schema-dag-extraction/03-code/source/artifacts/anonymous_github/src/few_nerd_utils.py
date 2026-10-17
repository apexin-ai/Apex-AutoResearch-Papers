"""Few-NERD data loading and preprocessing utilities.

Input: Few-NERD dataset (token-level annotation, 66 fine-grained entity types)
       Loaded from local parquet files; falls back to HF Hub if parquet missing.
Output: List of {"text": str, "entities": [{"text": str, "type": str, "start": int, "end": int}]}
Dependencies: datasets
"""
import json
import logging
import os
from typing import Dict, List, Optional, Set

from datasets import load_dataset

logger = logging.getLogger(__name__)

DEFAULT_DATA_DIR = "./data/parquet"


def load_few_nerd(
    split: str = "test",
    max_samples: Optional[int] = None,
    data_dir: str = DEFAULT_DATA_DIR,
) -> List[Dict]:
    """Load Few-NERD and convert token-level tags to span-level entities.

    Args:
        split: Dataset split ("train", "validation", "test").
        max_samples: If set, only return first N samples.
        data_dir: Directory containing {split}.parquet files.

    Returns:
        List of dicts with "text" (reconstructed sentence) and "entities" (span-level).
    """
    parquet_path = os.path.join(data_dir, f"{split}.parquet")
    if os.path.exists(parquet_path):
        logger.info("Loading Few-NERD from local parquet: %s", parquet_path)
        ds = load_dataset("parquet", data_files=parquet_path, split="train")
    else:
        logger.info("Local parquet not found, falling back to HF Hub")
        ds = load_dataset("DFKI-SLT/few-nerd", "supervised", split=split, trust_remote_code=True)

    tag_names = ds.features["fine_ner_tags"].feature.names

    samples = []
    for i, example in enumerate(ds):
        if max_samples is not None and i >= max_samples:
            break

        tokens = example["tokens"]
        tags = example["fine_ner_tags"]

        text, entities = _tokens_to_spans(tokens, tags, tag_names)
        samples.append({"text": text, "entities": entities})

    logger.info("Loaded %d samples from Few-NERD %s split", len(samples), split)
    return samples


def _tokens_to_spans(tokens: List[str], tag_ids: List[int], tag_names: List[str]) -> tuple:
    """Convert token-level tags to char-offset spans.

    Few-NERD uses flat labels (no B-/I- prefix). Consecutive tokens sharing
    the same non-O tag id form one entity span.

    Returns:
        (text, entities) where text is space-joined tokens and entities have char offsets.
    """
    text = ""
    char_offsets = []
    for tok in tokens:
        start = len(text)
        text += tok
        end = len(text)
        char_offsets.append((start, end))
        text += " "
    text = text.rstrip()

    entities = []
    current_entity = None

    for idx, tag_id in enumerate(tag_ids):
        if tag_id == 0:  # O tag
            if current_entity is not None:
                entities.append(_finalize_entity(current_entity, tokens, char_offsets))
                current_entity = None
        else:
            type_name = tag_names[tag_id]
            if current_entity is not None and current_entity["type"] == type_name:
                current_entity["token_end"] = idx
            else:
                if current_entity is not None:
                    entities.append(_finalize_entity(current_entity, tokens, char_offsets))
                current_entity = {"type": type_name, "token_start": idx, "token_end": idx}

    if current_entity is not None:
        entities.append(_finalize_entity(current_entity, tokens, char_offsets))

    return text, entities


def _finalize_entity(entity: Dict, tokens: List[str], char_offsets: List[tuple]) -> Dict:
    start = char_offsets[entity["token_start"]][0]
    end = char_offsets[entity["token_end"]][1]
    span_text = " ".join(tokens[entity["token_start"]:entity["token_end"] + 1])
    return {"text": span_text, "type": entity["type"], "start": start, "end": end}


def get_all_types(dataset: List[Dict]) -> List[str]:
    """Extract all unique fine-grained entity type names from dataset."""
    types = set()
    for sample in dataset:
        for ent in sample["entities"]:
            types.add(ent["type"])
    return sorted(types)


def load_type_definitions(path: str) -> Dict[str, str]:
    """Load type name -> definition mapping from JSON file."""
    with open(path, "r") as f:
        return json.load(f)


def filter_entities_by_types(entities: List[Dict], type_set: Set[str]) -> List[Dict]:
    """Filter entities to only keep those whose type is in type_set."""
    return [e for e in entities if e["type"] in type_set]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Few-NERD data loading utilities")
    parser.add_argument("--split", default="test", help="Dataset split")
    parser.add_argument("--max_samples", type=int, default=None, help="Max samples to load")
    parser.add_argument("--output_path", default=None, help="Save processed data as JSON")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    data = load_few_nerd(split=args.split, max_samples=args.max_samples)
    types = get_all_types(data)
    print(f"Loaded {len(data)} samples, {len(types)} unique types")
    print(f"Types: {types[:10]}...")

    if args.output_path:
        with open(args.output_path, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved to {args.output_path}")

#!/usr/bin/env python3
"""
MAVEN → parquet converter for schema-dag-extraction pipeline.

MAVEN data format (JSONL, one document per line):
  {
    "id": "doc_id",
    "title": "...",
    "content": [{"sentence": "...", "tokens": ["t1", "t2", ...]}, ...],
    "events": [
      {
        "id": "event_id",
        "type": "Killing",
        "type_id": 20,
        "mention": [
          {"id": "m_id", "trigger_word": "killed", "sent_id": 0, "offset": [3, 4]}
        ]
      }, ...
    ],
    "negative_triggers": [...]  // ignored
  }

Conversion logic:
  - Each document becomes one record (document-level, not sentence-level)
  - text = concatenation of all sentences separated by spaces
  - entities = list of {text: trigger_word, type: event_type} from all event mentions
  - Trigger word is reconstructed from token offsets for accuracy

Output: parquet with columns [text, entities] where entities is list[dict{text, type}].

Usage:
  python preprocess_maven.py --input_dir data/maven --output_dir data/maven_parquet --split train
  python preprocess_maven.py --input_dir data/maven --output_dir data/maven_parquet --split valid
  python preprocess_maven.py --help
"""

import argparse
import json
import sys
from pathlib import Path

import pandas as pd


SPLIT_FILE_MAP = {
    "train": "train.jsonl",
    "valid": "valid.jsonl",
    "test": "test.jsonl",
}


def extract_trigger_text(tokens, offset):
    """Reconstruct trigger text from token list and [start, end) offset."""
    start, end = offset
    if start < 0 or end > len(tokens):
        return None
    return " ".join(tokens[start:end])


def parse_document(doc):
    """Parse one MAVEN document into our record format.

    Returns dict with keys: text, entities.
    """
    sentences = doc.get("content", [])
    all_tokens_by_sent = []
    sent_texts = []
    for sent_obj in sentences:
        tokens = sent_obj.get("tokens", [])
        all_tokens_by_sent.append(tokens)
        sent_texts.append(sent_obj.get("sentence", " ".join(tokens)))

    full_text = " ".join(sent_texts)

    entities = []
    events = doc.get("events", [])
    for event in events:
        event_type = event["type"]
        for mention in event.get("mention", []):
            sent_id = mention["sent_id"]
            offset = mention["offset"]
            trigger_word = mention.get("trigger_word", "")

            if sent_id < len(all_tokens_by_sent):
                reconstructed = extract_trigger_text(all_tokens_by_sent[sent_id], offset)
                if reconstructed:
                    trigger_word = reconstructed

            if trigger_word:
                entities.append({"text": trigger_word, "type": event_type})

    return {"text": full_text, "entities": entities}


def process_split(input_path, output_path):
    """Read MAVEN JSONL and write parquet."""
    records = []
    with open(input_path, encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                doc = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"WARNING: skipping line {line_num}: {e}", file=sys.stderr)
                continue
            record = parse_document(doc)
            records.append(record)

    if not records:
        print(f"ERROR: no records parsed from {input_path}", file=sys.stderr)
        sys.exit(1)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(records)
    df.to_parquet(output_path, index=False)

    n_entities = sum(len(r["entities"]) for r in records)
    event_types = set()
    for r in records:
        for e in r["entities"]:
            event_types.add(e["type"])

    print(f"Split: {input_path.name}")
    print(f"  Documents: {len(records)}")
    print(f"  Event mentions: {n_entities}")
    print(f"  Event types: {len(event_types)}")
    print(f"  Output: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert MAVEN event detection data (JSONL) to parquet format"
    )
    parser.add_argument(
        "--input_dir", required=True,
        help="Directory containing MAVEN JSONL files (train.jsonl, valid.jsonl, test.jsonl)"
    )
    parser.add_argument(
        "--output_dir", required=True,
        help="Output directory for parquet files"
    )
    parser.add_argument(
        "--split", required=True, choices=["train", "valid", "test", "all"],
        help="Which split to process (train/valid/test/all)"
    )
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)

    if not input_dir.exists():
        print(f"ERROR: input directory not found: {input_dir}", file=sys.stderr)
        sys.exit(1)

    splits = list(SPLIT_FILE_MAP.keys()) if args.split == "all" else [args.split]

    for split in splits:
        filename = SPLIT_FILE_MAP[split]
        input_path = input_dir / filename
        if not input_path.exists():
            print(f"WARNING: {input_path} not found, skipping", file=sys.stderr)
            continue
        output_path = output_dir / f"{split}.parquet"
        process_split(input_path, output_path)


if __name__ == "__main__":
    main()

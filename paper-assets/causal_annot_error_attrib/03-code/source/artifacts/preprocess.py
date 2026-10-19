"""Unified preprocessing for HumAID, VAST, and Civil Comments datasets.
Outputs JSONL files with schema: {text, label, label_name, split}
"""
import json
import csv
import os
from collections import Counter

BASE = "/home/sonny/causal_annot_error_attrib/data"


def write_jsonl(records, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"  Wrote {len(records)} records to {path}")


def process_humaid():
    print("=" * 60)
    print("Processing HumAID")
    print("=" * 60)
    from datasets import load_dataset
    ds = load_dataset("QCRI/HumAID-all", verification_mode="no_checks")

    label_names = sorted(set(ds["train"]["class_label"]))
    label2id = {name: i for i, name in enumerate(label_names)}

    split_map = {"train": "train", "validation": "val", "test": "test"}
    all_stats = {}

    for hf_split, out_split in split_map.items():
        records = []
        for row in ds[hf_split]:
            lname = row["class_label"]
            records.append({
                "text": row["tweet_text"],
                "label": label2id[lname],
                "label_name": lname,
                "split": out_split,
            })
        write_jsonl(records, f"{BASE}/humaid/{out_split}.jsonl")
        all_stats[out_split] = records

    print_stats("HumAID", label_names, all_stats)


def process_vast():
    print("\n" + "=" * 60)
    print("Processing VAST")
    print("=" * 60)
    vast_dir = f"{BASE}/vast/_repo/data/VAST"
    label_map = {0: "con", 1: "pro", 2: "neutral"}
    label_names = ["con", "pro", "neutral"]

    split_files = {"train": "vast_train.csv", "val": "vast_dev.csv", "test": "vast_test.csv"}
    all_stats = {}

    for out_split, fname in split_files.items():
        records = []
        with open(f"{vast_dir}/{fname}") as f:
            reader = csv.DictReader(f)
            for row in reader:
                lid = int(row["label"])
                records.append({
                    "text": row["post"],
                    "label": lid,
                    "label_name": label_map[lid],
                    "split": out_split,
                })
        write_jsonl(records, f"{BASE}/vast/{out_split}.jsonl")
        all_stats[out_split] = records

    print_stats("VAST", label_names, all_stats)


def process_civil_comments():
    print("\n" + "=" * 60)
    print("Processing Civil Comments")
    print("=" * 60)
    from datasets import load_dataset

    label_names = ["non_toxic", "toxic"]
    split_map = {"test": "test", "validation": "val"}
    all_stats = {}

    for hf_split, out_split in split_map.items():
        ds = load_dataset("google/civil_comments", split=hf_split)
        records = []
        for row in ds:
            lid = 1 if row["toxicity"] >= 0.5 else 0
            records.append({
                "text": row["text"],
                "label": lid,
                "label_name": label_names[lid],
                "split": out_split,
            })
        write_jsonl(records, f"{BASE}/civil_comments/{out_split}.jsonl")
        all_stats[out_split] = records

    # Train: sample 100K from the 1.8M training set for manageability
    ds_train = load_dataset("google/civil_comments", split="train[:100000]")
    records = []
    for row in ds_train:
        lid = 1 if row["toxicity"] >= 0.5 else 0
        records.append({
            "text": row["text"],
            "label": lid,
            "label_name": label_names[lid],
            "split": "train",
        })
    write_jsonl(records, f"{BASE}/civil_comments/train.jsonl")
    all_stats["train"] = records

    print_stats("Civil Comments", label_names, all_stats)


def print_stats(name, label_names, all_stats):
    print(f"\nDataset: {name}")
    splits_str = ", ".join(f"{s}={len(recs)}" for s, recs in all_stats.items())
    print(f"Splits: {splits_str}")
    print(f"Classes (K={len(label_names)}): {label_names}")

    all_records = [r for recs in all_stats.values() for r in recs]
    dist = Counter(r["label_name"] for r in all_records)
    print(f"Class distribution: {dict(sorted(dist.items()))}")

    print("Sample texts (first 3):")
    for i, r in enumerate(list(all_stats.values())[0][:3]):
        print(f"  [{i}] label={r['label_name']}: {r['text'][:120]}...")


if __name__ == "__main__":
    process_humaid()
    process_vast()
    process_civil_comments()

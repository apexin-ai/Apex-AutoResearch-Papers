"""Data preprocessing: placeholder removal, attack_type labeling, stratified split."""

import json
import os
from pathlib import Path
from sklearn.model_selection import train_test_split

SEED = 42
DATA_DIR = Path(__file__).resolve().parent.parent / "artifacts" / "data" / "processed"
INPUT_FILE = DATA_DIR / "conversations.jsonl"


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def save_jsonl(data, path):
    with open(path, "w") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")


def assign_attack_type(conv):
    source = conv["source"]
    if source == "tom-gibbs":
        conv["attack_type"] = "cipher-based"
    elif source == "safemtdata":
        conv["attack_type"] = "persuasion-based"
    elif source == "wildchat":
        conv["attack_type"] = "benign"
    else:
        raise ValueError(f"Unknown source: {source}")
    return conv


def remove_assistant_placeholders(conv):
    """Remove assistant placeholder turns from safemtdata conversations."""
    original_num = len(conv["turns"])
    conv["turns"] = [t for t in conv["turns"] if not (t["role"] == "assistant" and t["content"] == "[Model response]")]
    conv["num_turns"] = len(conv["turns"])
    return conv, original_num


def main():
    conversations = load_data(INPUT_FILE)
    assert len(conversations) == 500, f"Expected 500, got {len(conversations)}"

    # Track safemtdata turn counts before/after
    safemt_before = []
    safemt_after = []

    for conv in conversations:
        assign_attack_type(conv)
        if conv["source"] == "safemtdata":
            conv, orig_num = remove_assistant_placeholders(conv)
            safemt_before.append(orig_num)
            safemt_after.append(conv["num_turns"])

    # Save full processed file
    save_jsonl(conversations, INPUT_FILE)

    # Stratified split
    attack_types = [c["attack_type"] for c in conversations]
    train_data, temp_data, train_labels, temp_labels = train_test_split(
        conversations, attack_types, test_size=0.30, random_state=SEED, stratify=attack_types
    )
    val_data, test_data, _, _ = train_test_split(
        temp_data, temp_labels, test_size=0.50, random_state=SEED, stratify=temp_labels
    )

    save_jsonl(train_data, DATA_DIR / "train.jsonl")
    save_jsonl(val_data, DATA_DIR / "val.jsonl")
    save_jsonl(test_data, DATA_DIR / "test.jsonl")

    # Statistics
    print("=" * 60)
    print("DATA PREPROCESSING REPORT")
    print("=" * 60)

    print(f"\nSafeMTData placeholder removal:")
    print(f"  Avg turns before: {sum(safemt_before)/len(safemt_before):.1f}")
    print(f"  Avg turns after:  {sum(safemt_after)/len(safemt_after):.1f}")

    print(f"\nSplit sizes:")
    print(f"  Train: {len(train_data)}")
    print(f"  Val:   {len(val_data)}")
    print(f"  Test:  {len(test_data)}")
    print(f"  Total: {len(train_data) + len(val_data) + len(test_data)}")

    for name, data in [("Train", train_data), ("Val", val_data), ("Test", test_data)]:
        counts = {}
        for c in data:
            at = c["attack_type"]
            counts[at] = counts.get(at, 0) + 1
        total = len(data)
        print(f"\n  {name} ({total}):")
        for at in ["cipher-based", "persuasion-based", "benign"]:
            n = counts.get(at, 0)
            print(f"    {at}: {n} ({100*n/total:.1f}%)")

    # Verification
    print("\n" + "=" * 60)
    print("VERIFICATION")
    print("=" * 60)
    total = len(train_data) + len(val_data) + len(test_data)
    print(f"  Total records: {total} (expected 500) {'✓' if total == 500 else '✗'}")

    # Check no assistant placeholders in safemtdata
    safemt_has_placeholder = False
    for conv in conversations:
        if conv["source"] == "safemtdata":
            for t in conv["turns"]:
                if t["role"] == "assistant" and t["content"] == "[Model response]":
                    safemt_has_placeholder = True
                    break
    print(f"  SafeMTData no placeholders: {'✓' if not safemt_has_placeholder else '✗'}")

    # Check tom-gibbs/wildchat still have assistant turns
    has_assistant = {"tom-gibbs": False, "wildchat": False}
    for conv in conversations:
        if conv["source"] in has_assistant:
            for t in conv["turns"]:
                if t["role"] == "assistant":
                    has_assistant[conv["source"]] = True
                    break
    print(f"  tom-gibbs has assistant turns: {'✓' if has_assistant['tom-gibbs'] else '✗'}")
    print(f"  wildchat has assistant turns: {'✓' if has_assistant['wildchat'] else '✗'}")

    # Stratification check
    full_ratios = {}
    for c in conversations:
        at = c["attack_type"]
        full_ratios[at] = full_ratios.get(at, 0) + 1
    full_ratios = {k: v/500 for k, v in full_ratios.items()}

    max_dev = 0
    for name, data in [("Train", train_data), ("Val", val_data), ("Test", test_data)]:
        for at in full_ratios:
            split_ratio = sum(1 for c in data if c["attack_type"] == at) / len(data)
            dev = abs(split_ratio - full_ratios[at])
            max_dev = max(max_dev, dev)
    print(f"  Max stratification deviation: {100*max_dev:.1f}% (threshold 2%) {'✓' if max_dev < 0.02 else '✗'}")


if __name__ == "__main__":
    main()

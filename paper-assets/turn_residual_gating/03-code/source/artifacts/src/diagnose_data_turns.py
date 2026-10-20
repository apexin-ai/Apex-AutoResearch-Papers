"""Diagnose UltraChat 8K turn distribution after truncation to 2048 tokens."""
import os
import sys
from collections import Counter

import torch
from datasets import load_from_disk
from transformers import AutoTokenizer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from turn_utils import detect_turn_boundaries
from config import MODEL_NAME

MAX_SEQ_LEN = 2048


def main():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)

    data_path = "/root/turn_residual_gating/data/ultrachat_8k"
    ds = load_from_disk(data_path)
    total = len(ds)
    print(f"Loaded {total} samples from {data_path}")

    turn_counts = []
    original_token_lengths = []

    for i in range(total):
        messages = ds[i]["messages"]

        text = tokenizer.apply_chat_template(messages, tokenize=False)
        full_encoding = tokenizer(text, truncation=False, return_tensors="pt")
        original_token_lengths.append(full_encoding.input_ids.size(1))

        truncated_encoding = tokenizer(
            text, truncation=True, max_length=MAX_SEQ_LEN, return_tensors="pt"
        )
        input_ids = truncated_encoding.input_ids.squeeze(0)

        boundaries = detect_turn_boundaries(input_ids, tokenizer)
        n_assistant = len(boundaries["assistant_last_token_positions"])
        turn_counts.append(n_assistant)

        if (i + 1) % 1000 == 0:
            print(f"  processed {i + 1}/{total}")

    counter = Counter(turn_counts)
    print(f"\n=== UltraChat 8K Turn Distribution (after truncation to {MAX_SEQ_LEN} tokens) ===")
    print(f"Total samples: {total}")

    for k in range(1, 5):
        c = counter.get(k, 0)
        print(f"Samples with {k} assistant turn{'s' if k > 1 else '':4s}: {c:5d} ({100*c/total:.1f}%)")
    c5 = sum(v for k, v in counter.items() if k >= 5)
    print(f"Samples with 5+ assistant turns: {c5:5d} ({100*c5/total:.1f}%)")

    c_ge2 = sum(v for k, v in counter.items() if k >= 2)
    c_ge3 = sum(v for k, v in counter.items() if k >= 3)
    print(f"\nSamples with >=2 turns (can trigger GAR loss): {c_ge2:5d} ({100*c_ge2/total:.1f}%)")
    print(f"Samples with >=3 turns (meaningful GAR signal): {c_ge3:5d} ({100*c_ge3/total:.1f}%)")

    import numpy as np
    arr = np.array(turn_counts)
    print(f"\nMean assistant turns after truncation: {arr.mean():.2f}")
    print(f"Median assistant turns after truncation: {int(np.median(arr))}")

    if c_ge3 < 2000:
        orig = np.array(original_token_lengths)
        print(f"\n=== Additional Analysis (>=3 turns < 2000) ===")
        print(f"Original (untruncated) token lengths:")
        print(f"  Mean:   {orig.mean():.0f}")
        print(f"  Median: {int(np.median(orig))}")
        print(f"  Min:    {orig.min()}")
        print(f"  Max:    {orig.max()}")
        print(f"  Samples exceeding {MAX_SEQ_LEN}: {(orig > MAX_SEQ_LEN).sum()} ({100*(orig > MAX_SEQ_LEN).sum()/total:.1f}%)")

        orig_turn_counts = []
        for i in range(total):
            messages = ds[i]["messages"]
            n_asst = sum(1 for m in messages if m["role"] == "assistant")
            orig_turn_counts.append(n_asst)
        orig_arr = np.array(orig_turn_counts)
        print(f"\nOriginal assistant turns (before tokenization/truncation):")
        print(f"  Mean:   {orig_arr.mean():.2f}")
        print(f"  Median: {int(np.median(orig_arr))}")
        orig_counter = Counter(orig_turn_counts)
        for k in range(1, 6):
            c = orig_counter.get(k, 0)
            print(f"  {k} turns: {c:5d} ({100*c/total:.1f}%)")
        c6 = sum(v for k, v in orig_counter.items() if k >= 6)
        if c6 > 0:
            print(f"  6+ turns: {c6:5d} ({100*c6/total:.1f}%)")

        print(f"\nRecommendation: Consider filtering for conversations with >=4 original "
              f"assistant turns and/or increasing max_seq_len to retain more turns after truncation.")


if __name__ == "__main__":
    main()

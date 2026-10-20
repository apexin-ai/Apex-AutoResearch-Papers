# WikiText-103 data preparation: download, split (train / reference / test), tokenize, save.
# Usage: python data_prep.py --output_dir ./data --tokenizer Qwen/Qwen3-1.7B --seq_len 512 --ref_size 5000

import argparse
import os
import json
from pathlib import Path

import torch
from datasets import load_dataset
from transformers import AutoTokenizer
from collections import Counter


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--output_dir", type=str, default="./data")
    p.add_argument("--tokenizer", type=str, default="Qwen/Qwen3-1.7B")
    p.add_argument("--seq_len", type=int, default=512)
    p.add_argument("--ref_size", type=int, default=5000,
                   help="Number of samples for the fixed reference set R")
    p.add_argument("--seed", type=int, default=42)
    return p.parse_args()


def download_wikitext():
    ds = load_dataset("wikitext", "wikitext-103-raw-v1")
    return ds


def compute_ngram_rarity(texts, n=3, rare_percentile=10):
    """Label each text by whether it contains rare n-grams (bottom percentile).

    Returns a boolean list: True = contains rare n-grams (used for k-NN probe labels).
    """
    counter = Counter()
    text_ngrams = []
    for text in texts:
        tokens = text.split()
        ngrams = [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]
        text_ngrams.append(set(ngrams))
        counter.update(ngrams)

    if not counter:
        return [False] * len(texts)

    counts = sorted(counter.values())
    threshold = counts[max(0, len(counts) * rare_percentile // 100)]

    rare_ngrams = {ng for ng, c in counter.items() if c <= threshold}
    labels = [bool(tng & rare_ngrams) for tng in text_ngrams]
    return labels


def tokenize_and_chunk(texts, tokenizer, seq_len):
    """Concatenate all texts, tokenize, split into fixed-length chunks."""
    full_text = "\n\n".join(t for t in texts if t.strip())
    encoding = tokenizer(full_text, return_attention_mask=False)
    input_ids = encoding["input_ids"]

    chunks = []
    for i in range(0, len(input_ids) - seq_len + 1, seq_len):
        chunks.append(input_ids[i:i + seq_len])
    return chunks


def main():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    print("Downloading WikiText-103...")
    ds = download_wikitext()

    tokenizer = AutoTokenizer.from_pretrained(args.tokenizer, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # --- Train split ---
    train_texts = [x["text"] for x in ds["train"] if x["text"].strip()]
    print(f"Train texts: {len(train_texts)}")

    train_chunks = tokenize_and_chunk(train_texts, tokenizer, args.seq_len)
    print(f"Train chunks (seq_len={args.seq_len}): {len(train_chunks)}")

    # --- Reference set R: fixed 5K from TRAIN set (not validation, which is too small) ---
    rng = torch.Generator().manual_seed(args.seed)
    perm = torch.randperm(len(train_chunks), generator=rng).tolist()
    ref_indices = set(perm[:args.ref_size])
    ref_chunks = [train_chunks[i] for i in perm[:args.ref_size]]
    remaining_train = [train_chunks[i] for i in range(len(train_chunks)) if i not in ref_indices]
    print(f"Reference set R: {len(ref_chunks)} chunks (from train, held out)")
    print(f"Remaining train (for generation prompts): {len(remaining_train)} chunks")

    # --- Rare n-gram labels for reference set (for k-NN probe) ---
    # Use FULL train corpus statistics so rare/common labels are meaningful
    all_train_texts = [tokenizer.decode(c, skip_special_tokens=True) for c in train_chunks]
    ref_texts_decoded = [tokenizer.decode(c, skip_special_tokens=True) for c in ref_chunks]

    train_counter = Counter()
    for text in all_train_texts:
        tokens = text.split()
        for i in range(len(tokens) - 2):
            train_counter[tuple(tokens[i:i + 3])] += 1

    counts = sorted(train_counter.values())
    threshold = counts[max(0, len(counts) * 10 // 100)]
    rare_ngrams = {ng for ng, c in train_counter.items() if c <= threshold}

    rare_labels = []
    for text in ref_texts_decoded:
        tokens = text.split()
        text_ngrams = {tuple(tokens[i:i + 3]) for i in range(len(tokens) - 2)}
        rare_labels.append(bool(text_ngrams & rare_ngrams))
    print(f"Reference rare n-gram positives: {sum(rare_labels)}/{len(rare_labels)}")

    # --- Test split ---
    test_texts = [x["text"] for x in ds["test"] if x["text"].strip()]
    test_chunks = tokenize_and_chunk(test_texts, tokenizer, args.seq_len)
    print(f"Test chunks: {len(test_chunks)}")

    # --- Save (remaining_train replaces full train for generation prompts) ---
    torch.save(remaining_train, Path(args.output_dir) / "train_chunks.pt")
    torch.save(ref_chunks, Path(args.output_dir) / "ref_chunks.pt")
    torch.save(rare_labels, Path(args.output_dir) / "ref_rare_labels.pt")
    torch.save(test_chunks, Path(args.output_dir) / "test_chunks.pt")

    meta = {
        "tokenizer": args.tokenizer,
        "seq_len": args.seq_len,
        "num_train": len(train_chunks),
        "num_ref": len(ref_chunks),
        "num_test": len(test_chunks),
        "num_rare_positive": int(sum(rare_labels)),
        "seed": args.seed,
    }
    with open(Path(args.output_dir) / "meta.json", "w") as f:
        json.dump(meta, f, indent=2)

    print("Done. Saved to", args.output_dir)


if __name__ == "__main__":
    main()

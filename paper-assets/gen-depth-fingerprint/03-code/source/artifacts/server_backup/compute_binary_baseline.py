#!/usr/bin/env python3
"""Compute NLL scores for binary baseline filtering.

Scores each training sample with pre-trained model NLL,
then selects the most "human-like" (highest NLL) texts,
size-matched to the depth01 variant.
"""

import json
import os
import math
from collections import defaultdict

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default="data/downstream")
    parser.add_argument("--model-path", required=True)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--max-length", type=int, default=512)
    parser.add_argument("--batch-size", type=int, default=2)
    args = parser.parse_args()

    train_path = os.path.join(args.data_dir, "train_all.jsonl")
    d01_path = os.path.join(args.data_dir, "train_depth01.jsonl")

    print("Loading training data...")
    with open(train_path) as f:
        train_samples = [json.loads(l) for l in f]
    with open(d01_path) as f:
        target_size = sum(1 for _ in f)
    print(f"Total train: {len(train_samples)}, target size: {target_size}")

    print(f"Loading model from {args.model_path}...")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        args.model_path, trust_remote_code=True,
        dtype=torch.bfloat16, device_map=args.device,
    )
    model.eval()

    print("Scoring samples...")
    scores = []
    for i in range(0, len(train_samples), args.batch_size):
        batch = train_samples[i:i + args.batch_size]
        texts = [s["text"] for s in batch]
        enc = tokenizer(
            texts, return_tensors="pt", truncation=True,
            max_length=args.max_length, padding=True,
        ).to(args.device)

        with torch.no_grad():
            out = model(**enc)
            logits = out.logits[:, :-1, :]
            labels = enc["input_ids"][:, 1:]
            mask = enc["attention_mask"][:, 1:]

            for j in range(logits.size(0)):
                sample_logits = logits[j]  # (seq-1, vocab)
                sample_labels = labels[j]  # (seq-1,)
                sample_mask = mask[j]      # (seq-1,)

                loss = torch.nn.functional.cross_entropy(
                    sample_logits, sample_labels, reduction="none"
                )
                nll = (loss * sample_mask).sum() / sample_mask.sum()
                scores.append(nll.item())

            del out, logits, labels, mask
            torch.cuda.empty_cache()

        if (i // args.batch_size) % 50 == 0:
            print(f"  {min(i + args.batch_size, len(train_samples))}/{len(train_samples)}")

    del model
    torch.cuda.empty_cache()

    # Select top-NLL samples (most human-like), size-matched to depth01
    indexed = sorted(enumerate(scores), key=lambda x: -x[1])
    selected_idx = set(idx for idx, _ in indexed[:target_size])

    filtered = [train_samples[i] for i in range(len(train_samples)) if i in selected_idx]

    depth_dist = defaultdict(int)
    for s in filtered:
        depth_dist[s["depth"]] += 1
    print(f"\nBinary filtered depth distribution: {dict(sorted(depth_dist.items()))}")

    out_path = os.path.join(args.data_dir, "train_binary_filtered.jsonl")
    with open(out_path, "w") as f:
        for s in filtered:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    print(f"Saved {len(filtered)} samples -> {out_path}")

    scores_path = os.path.join(args.data_dir, "nll_scores.json")
    with open(scores_path, "w") as f:
        json.dump(
            [{"idx": i, "nll": s, "depth": train_samples[i]["depth"],
              "generator": train_samples[i]["generator"]}
             for i, s in enumerate(scores)],
            f,
        )
    print(f"Scores -> {scores_path}")


if __name__ == "__main__":
    main()

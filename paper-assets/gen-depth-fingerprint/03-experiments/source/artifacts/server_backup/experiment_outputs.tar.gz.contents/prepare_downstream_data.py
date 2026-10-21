#!/usr/bin/env python3
"""Build depth-stratified training datasets for downstream utility experiment.

Pools generation data from all generators, deduplicates depth-0 (same human seed),
splits by seed_id, and creates filtered variants for comparison.
"""

import json
import os
import random
import argparse
import math
from collections import defaultdict
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def load_generations(data_dir, generators):
    all_samples = []
    seen_depth0_seeds = set()

    for gen in generators:
        gen_path = Path(data_dir) / gen / "generations.jsonl"
        if not gen_path.exists():
            print(f"Warning: {gen_path} not found, skipping")
            continue

        with open(gen_path) as f:
            for line in f:
                sample = json.loads(line)
                sample["generator"] = gen

                if sample["depth"] == 0:
                    if sample["seed_id"] in seen_depth0_seeds:
                        continue
                    seen_depth0_seeds.add(sample["seed_id"])

                all_samples.append(sample)

    return all_samples


def split_by_seed(samples, test_ratio=0.2, seed=42):
    all_seed_ids = sorted(set(s["seed_id"] for s in samples))
    rng = random.Random(seed)
    rng.shuffle(all_seed_ids)

    n_test = int(len(all_seed_ids) * test_ratio)
    test_seeds = set(all_seed_ids[:n_test])

    train = [s for s in samples if s["seed_id"] not in test_seeds]
    test = [s for s in samples if s["seed_id"] in test_seeds]

    return train, test


def filter_by_depth(samples, max_depth):
    return [s for s in samples if s["depth"] <= max_depth]


def size_matched_sample(samples, target_size, seed=42):
    rng = random.Random(seed)
    if len(samples) <= target_size:
        return list(samples)
    return rng.sample(samples, target_size)


def compute_nll_scores(samples, model_path, device="cuda", batch_size=8, max_length=512):
    """Compute mean NLL per token for each sample using a pre-trained model.
    Higher NLL = more surprising = more likely human-written.
    """
    print(f"  Loading scoring model from {model_path}...")
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        model_path, trust_remote_code=True,
        dtype=torch.bfloat16, device_map=device,
    )
    model.eval()

    scores = []
    for i in range(0, len(samples), batch_size):
        batch_texts = [s["text"] for s in samples[i:i + batch_size]]
        enc = tokenizer(
            batch_texts, return_tensors="pt", truncation=True,
            max_length=max_length, padding=True,
        ).to(device)

        with torch.no_grad():
            out = model(**enc, labels=enc["input_ids"])
            shift_logits = out.logits[:, :-1, :].contiguous()
            shift_labels = enc["input_ids"][:, 1:].contiguous()
            shift_mask = enc["attention_mask"][:, 1:].contiguous()

            loss_fct = torch.nn.CrossEntropyLoss(reduction="none")
            token_losses = loss_fct(
                shift_logits.view(-1, shift_logits.size(-1)),
                shift_labels.view(-1),
            ).view(shift_labels.size())

            masked_losses = token_losses * shift_mask
            mean_nll = masked_losses.sum(dim=1) / shift_mask.sum(dim=1)
            scores.extend(mean_nll.cpu().tolist())

        if (i // batch_size) % 20 == 0:
            print(f"  Scored {min(i + batch_size, len(samples))}/{len(samples)}...")

    del model
    torch.cuda.empty_cache()
    return scores


def create_binary_baseline(train_all, scores_train, train_d01_size, seed=42):
    """Create binary-filtered variant: keep samples with highest NLL (most human-like).
    Size-matched to depth01 variant.
    """
    indexed = list(zip(scores_train, range(len(train_all))))
    indexed.sort(key=lambda x: -x[0])  # highest NLL first = most human-like
    selected_indices = [idx for _, idx in indexed[:train_d01_size]]
    return [train_all[i] for i in sorted(selected_indices)]


def save_jsonl(samples, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        for s in f:
            pass
        f.seek(0)
        for s in samples:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    print(f"  Saved {len(samples)} samples -> {path}")


def save_jsonl(samples, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        for s in samples:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    print(f"  Saved {len(samples)} samples -> {path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default="data")
    parser.add_argument("--output-dir", default="data/downstream")
    parser.add_argument("--generators", nargs="+",
                        default=["olmo-2-1b", "pythia-1b", "qwen3-0.6b", "qwen3-1.7b"])
    parser.add_argument("--test-ratio", type=float, default=0.2)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--model-path", default=None,
                        help="Model path for binary baseline scoring (optional)")
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    print("Loading generation data...")
    all_samples = load_generations(args.data_dir, args.generators)

    depth_counts = defaultdict(int)
    gen_counts = defaultdict(int)
    for s in all_samples:
        depth_counts[s["depth"]] += 1
        gen_counts[s["generator"]] += 1
    print(f"Total samples (deduped depth-0): {len(all_samples)}")
    print(f"Depth distribution: {dict(sorted(depth_counts.items()))}")
    print(f"Generator distribution: {dict(sorted(gen_counts.items()))}")

    print(f"\nSplitting by seed_id (test_ratio={args.test_ratio})...")
    train_all, test_all = split_by_seed(all_samples, args.test_ratio, args.seed)
    print(f"Train: {len(train_all)}, Test: {len(test_all)}")

    # Save test set
    save_jsonl(test_all, os.path.join(args.output_dir, "test.jsonl"))

    # Variant a: depth-0 only
    print("\nVariant: depth0_only")
    train_d0 = filter_by_depth(train_all, 0)
    save_jsonl(train_d0, os.path.join(args.output_dir, "train_depth0_only.jsonl"))

    # Variant b: depth 0+1
    print("Variant: depth01")
    train_d01 = filter_by_depth(train_all, 1)
    save_jsonl(train_d01, os.path.join(args.output_dir, "train_depth01.jsonl"))

    # Variant c: all depths
    print("Variant: all")
    save_jsonl(train_all, os.path.join(args.output_dir, "train_all.jsonl"))

    # Variant d: size-matched random sample
    print("Variant: size_matched")
    train_matched = size_matched_sample(train_all, len(train_d01), args.seed)
    save_jsonl(train_matched, os.path.join(args.output_dir, "train_size_matched.jsonl"))

    # Variant e: binary baseline (optional, needs model)
    if args.model_path:
        print("\nVariant: binary_filtered (scoring with model...)")
        scores = compute_nll_scores(train_all, args.model_path, args.device)
        train_binary = create_binary_baseline(train_all, scores, len(train_d01), args.seed)

        depth_dist = defaultdict(int)
        for s in train_binary:
            depth_dist[s["depth"]] += 1
        print(f"  Binary filtered depth distribution: {dict(sorted(depth_dist.items()))}")

        save_jsonl(train_binary, os.path.join(args.output_dir, "train_binary_filtered.jsonl"))

        scores_path = os.path.join(args.output_dir, "nll_scores.json")
        with open(scores_path, "w") as f:
            json.dump(
                [{"idx": i, "nll": s, "depth": train_all[i]["depth"],
                  "generator": train_all[i]["generator"]}
                 for i, s in enumerate(scores)],
                f, indent=2,
            )
        print(f"  NLL scores saved -> {scores_path}")
    else:
        print("\nSkipping binary baseline (no --model-path). Run with --model-path to create it.")

    # Summary
    print("\n=== Dataset Summary ===")
    print(f"{'Variant':<25} {'Train':>8} {'Test':>8}")
    print("-" * 45)
    print(f"{'depth0_only':<25} {len(train_d0):>8} {len(test_all):>8}")
    print(f"{'depth01':<25} {len(train_d01):>8} {len(test_all):>8}")
    print(f"{'all':<25} {len(train_all):>8} {len(test_all):>8}")
    print(f"{'size_matched':<25} {len(train_matched):>8} {len(test_all):>8}")
    if args.model_path:
        print(f"{'binary_filtered':<25} {len(train_binary):>8} {len(test_all):>8}")


if __name__ == "__main__":
    main()

"""
extract_token_nll.py — Extract per-token NLL using Pythia-410M reference model.

Input:  8 generator directories under data/, each with generations_shard0.jsonl
Output: results/token_nll_by_depth.json
        Each record: {"generator": str, "depth": int, "sample_idx": int, "token_nlls": [float,...]}
"""

import argparse
import json
import os
import random
from collections import defaultdict
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_SNAPSHOT = "/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f"

GENERATORS = {
    "olmo-2-1b":       "data/olmo-2-1b/generations_shard0.jsonl",
    "pythia-1b":       "data/pythia-1b/generations_shard0.jsonl",
    "pythia-2.8b":     "data/pythia-2.8b-paraphrase/generations_shard0.jsonl",
    "qwen3-0.6b":      "data/qwen3-0.6b/generations_shard0.jsonl",
    "qwen3-1.7b":      "data/qwen3-1.7b/generations_shard0.jsonl",
    "llama-3.2-3b":    "data/llama-3.2-3b/generations_shard0.jsonl",
    "mistral-7b-v0.3": "data/mistral-7b-v0.3/generations_shard0.jsonl",
    "qwen3-8b-base":   "data/qwen3-8b/generations_shard0.jsonl",
}


def load_and_sample(root: Path, samples_per_depth: int, seed: int):
    """Load generation data and sample texts per (generator, depth)."""
    random.seed(seed)
    by_gen_depth = defaultdict(lambda: defaultdict(list))

    for gen_name, rel_path in GENERATORS.items():
        fpath = root / rel_path
        if not fpath.exists():
            print(f"  SKIP {gen_name}: {fpath} not found")
            continue
        with open(fpath) as f:
            for line in f:
                rec = json.loads(line)
                by_gen_depth[gen_name][rec["depth"]].append(rec["text"])

    sampled = []
    for gen_name in sorted(by_gen_depth):
        for depth in range(5):
            texts = by_gen_depth[gen_name][depth]
            if not texts:
                continue
            chosen = random.sample(texts, min(samples_per_depth, len(texts)))
            for idx, text in enumerate(chosen):
                sampled.append({
                    "generator": gen_name,
                    "depth": depth,
                    "sample_idx": idx,
                    "text": text,
                })
    print(f"Sampled {len(sampled)} texts total")
    return sampled


def extract_token_nll(samples, tokenizer, model, device, batch_size):
    """Compute per-token NLL for each sample."""
    results = []
    for start in range(0, len(samples), batch_size):
        batch = samples[start:start + batch_size]
        texts = [s["text"] for s in batch]

        encodings = tokenizer(
            texts, return_tensors="pt", padding=True,
            truncation=True, max_length=512,
        ).to(device)

        with torch.no_grad():
            logits = model(**encodings).logits

        for i, sample in enumerate(batch):
            mask = encodings["attention_mask"][i].bool()
            seq_len = mask.sum().item()
            if seq_len < 2:
                results.append({**{k: sample[k] for k in ("generator", "depth", "sample_idx")}, "token_nlls": []})
                continue

            token_logits = logits[i, :seq_len - 1, :]
            log_probs = torch.log_softmax(token_logits, dim=-1)
            target_ids = encodings["input_ids"][i, 1:seq_len]
            token_log_probs = log_probs[torch.arange(seq_len - 1), target_ids]
            nll = (-token_log_probs).float().cpu().tolist()

            results.append({
                "generator": sample["generator"],
                "depth": sample["depth"],
                "sample_idx": sample["sample_idx"],
                "token_nlls": nll,
            })

        if (start + batch_size) % 200 == 0 or start + batch_size >= len(samples):
            print(f"  Processed {min(start + batch_size, len(samples))}/{len(samples)}")

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples-per-depth", type=int, default=25,
                        help="Texts to sample per (generator, depth)")
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    out_path = root / "results" / "token_nll_by_depth.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    n = 3 if args.dry_run else args.samples_per_depth
    print(f"Sampling {n} texts per (generator, depth)...")
    samples = load_and_sample(root, n, args.seed)

    print(f"Loading Pythia-410M on {args.device}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_SNAPSHOT, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_SNAPSHOT, local_files_only=True, torch_dtype=torch.float16
    ).to(args.device).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("Extracting token-level NLL...")
    results = extract_token_nll(samples, tokenizer, model, args.device, args.batch_size)

    with open(out_path, "w") as f:
        json.dump(results, f)
    print(f"Saved {len(results)} records to {out_path}")

    total_tokens = sum(len(r["token_nlls"]) for r in results)
    print(f"Total tokens: {total_tokens}")


if __name__ == "__main__":
    main()

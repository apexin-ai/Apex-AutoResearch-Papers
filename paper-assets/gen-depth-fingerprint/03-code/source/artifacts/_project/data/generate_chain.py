"""
generate_chain.py — Continuation depth chain data generation pipeline.

Input:  Wikipedia text (via HuggingFace datasets, streaming)
Output: /root/gen-depth-fingerprint/data/generations.jsonl
        Each line: {"id": int, "depth": int, "text": str, "seed_id": int, "token_count": int}
        1000 seeds × 5 depths (gen-0 to gen-4) = 5000 records.

Dependencies: transformers, datasets, torch, tqdm
Model: EleutherAI/pythia-2.8b (local cache)
"""

import argparse
import json
import os
import time

import torch
from datasets import load_dataset
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer


def load_seeds(tokenizer, num_seeds=1000, max_tokens=256):
    """Load Wikipedia texts and truncate each to max_tokens tokens as gen-0 seeds."""
    seeds = []
    try:
        ds = load_dataset(
            "wikipedia", "20220301.en",
            split="train", streaming=True,
            trust_remote_code=True,
            cache_dir="/root/autodl-tmp/.hf_cache",
        )
    except Exception:
        print("[WARN] wikipedia dataset failed, falling back to wikitext-103")
        ds = load_dataset(
            "wikitext", "wikitext-103-raw-v1",
            split="train", streaming=True,
            cache_dir="/root/autodl-tmp/.hf_cache",
        )

    for item in ds:
        text = item.get("text", "")
        if len(text.strip()) < 100:
            continue
        token_ids = tokenizer.encode(text, add_special_tokens=False)[:max_tokens]
        if len(token_ids) < 64:
            continue
        seeds.append(tokenizer.decode(token_ids))
        if len(seeds) >= num_seeds:
            break

    print(f"Loaded {len(seeds)} seeds")
    return seeds


def generate_continuation(model, tokenizer, text, device, max_new_tokens=256, prompt_tokens=128):
    """Take the last prompt_tokens tokens of text, generate max_new_tokens continuation."""
    input_ids = tokenizer.encode(text, add_special_tokens=False)
    # use last prompt_tokens as the prompt
    input_ids = input_ids[-prompt_tokens:]
    input_tensor = torch.tensor([input_ids], device=device)

    with torch.no_grad():
        output = model.generate(
            input_tensor,
            max_new_tokens=max_new_tokens,
            temperature=1.0,
            top_p=0.95,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
        )

    # only decode newly generated tokens
    new_tokens = output[0][len(input_ids):]
    return tokenizer.decode(new_tokens, skip_special_tokens=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Only process 2 seeds for validation")
    parser.add_argument("--num-seeds", type=int, default=1000)
    parser.add_argument("--output", type=str, default="/root/gen-depth-fingerprint/data/generations.jsonl")
    parser.add_argument("--device", type=str, default="cuda:0", help="Device to use")
    parser.add_argument("--max-depth", type=int, default=4)
    args = parser.parse_args()

    num_seeds = 2 if args.dry_run else args.num_seeds
    device = torch.device(args.device)

    # reproducibility
    torch.manual_seed(42)
    torch.cuda.manual_seed(42)

    print("Loading tokenizer and model...")
    model_name = "EleutherAI/pythia-2.8b"
    cache_dir = "/root/autodl-tmp/models/pythia-2.8b"

    tokenizer = AutoTokenizer.from_pretrained(
        model_name, cache_dir=cache_dir, local_files_only=True
    )
    model = AutoModelForCausalLM.from_pretrained(
        model_name, cache_dir=cache_dir, local_files_only=True,
        dtype=torch.float16,
    ).to(device)
    model.eval()
    print(f"Model loaded on {device}, dtype={model.dtype}")

    print(f"Loading {num_seeds} seed texts...")
    seeds = load_seeds(tokenizer, num_seeds=num_seeds)

    output_path = args.output
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    record_id = 0
    t0 = time.time()

    with open(output_path, "w") as f:
        for seed_idx, seed_text in enumerate(tqdm(seeds, desc="Seeds")):
            # gen-0: original Wikipedia text
            gen0_tokens = tokenizer.encode(seed_text, add_special_tokens=False)
            record = {
                "id": record_id,
                "depth": 0,
                "text": seed_text,
                "seed_id": seed_idx,
                "token_count": len(gen0_tokens),
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            record_id += 1

            # gen-1 through gen-4
            prev_text = seed_text
            for depth in range(1, args.max_depth + 1):
                continuation = generate_continuation(model, tokenizer, prev_text, device)
                cont_tokens = tokenizer.encode(continuation, add_special_tokens=False)
                record = {
                    "id": record_id,
                    "depth": depth,
                    "text": continuation,
                    "seed_id": seed_idx,
                    "token_count": len(cont_tokens),
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
                record_id += 1
                prev_text = continuation

            if (seed_idx + 1) % 100 == 0:
                elapsed = time.time() - t0
                rate = (seed_idx + 1) / elapsed
                print(f"[{seed_idx+1}/{len(seeds)}] {elapsed:.0f}s elapsed, {rate:.2f} seeds/s")

    elapsed = time.time() - t0
    print(f"Done. {record_id} records written to {output_path} in {elapsed:.1f}s")


if __name__ == "__main__":
    main()

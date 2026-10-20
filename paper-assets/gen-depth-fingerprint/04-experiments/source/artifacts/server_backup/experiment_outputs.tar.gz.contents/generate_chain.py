"""
generate_chain.py — Multi-depth text continuation pipeline.

Appends records incrementally (one JSON line per record) to support crash recovery.
On restart, already-completed seed_ids are skipped automatically.

Generates recursive continuations from Wikipedia seed texts. Each seed produces
5 records (depth 0-4): the original excerpt + 4 successive model continuations.
Supports multi-GPU sharding and multiple generator models.

Input:  data/wiki_seed_1000.jsonl (each line: {"id", "title", "text"})
Output: {output_dir}/{model_name}/generations_shard{shard_id}.jsonl
        Each line: {"id": int, "depth": int, "text": str, "seed_id": int, "token_count": int, "model": str}
"""

import argparse
import json
import os
import time

import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

import signal
signal.signal(signal.SIGHUP, signal.SIG_IGN)

torch.manual_seed(42)
torch.cuda.manual_seed(42)

DEFAULT_MODEL_PATHS = [
    "/root/autodl-tmp/.hf_cache/EleutherAI/pythia-2___8b",
    "/root/autodl-tmp/models/pythia-2.8b",
]

DEFAULT_MODEL_NAME = "pythia-2.8b"

MODEL_NAME_MAP = {
    "qwen3-1.7b": "/root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base",
    "qwen3-0.6b": "/root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base",
}

MAX_DEPTH = 4
NUM_DEPTHS = MAX_DEPTH + 1


def find_default_model_path():
    for p in DEFAULT_MODEL_PATHS:
        if os.path.isfile(os.path.join(p, "config.json")):
            return p
    raise FileNotFoundError(f"Default model not found at any of: {DEFAULT_MODEL_PATHS}")


def load_seeds(path, tokenizer, max_tokens=256):
    seeds = []
    with open(path, "r") as f:
        for line_num, line in enumerate(f):
            item = json.loads(line)
            text = item.get("text", "")
            if len(text.strip()) < 100:
                continue
            token_ids = tokenizer.encode(text, add_special_tokens=False)[:max_tokens]
            if len(token_ids) < 64:
                continue
            seeds.append({"seed_id": line_num, "text": tokenizer.decode(token_ids)})
    print(f"Loaded {len(seeds)} seeds from {path}")
    return seeds


def generate_continuation(model, tokenizer, text, device, max_new_tokens=256, prompt_tokens=128, repetition_penalty=1.0, temperature=0.7, top_p=0.9):
    input_ids = tokenizer.encode(text, add_special_tokens=False)
    if len(input_ids) == 0:
        return ""
    input_ids = input_ids[-prompt_tokens:]
    input_tensor = torch.tensor([input_ids], device=device)

    with torch.no_grad():
        output = model.generate(
            input_tensor,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            do_sample=True,
            pad_token_id=tokenizer.pad_token_id,
            repetition_penalty=repetition_penalty,
        )

    new_tokens = output[0][len(input_ids):]
    return tokenizer.decode(new_tokens, skip_special_tokens=True)


def load_done_seeds(path):
    done = set()
    if not os.path.exists(path):
        return done
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
                done.add(record['seed_id'])
            except (json.JSONDecodeError, KeyError):
                pass
    return done


def main():
    parser = argparse.ArgumentParser(description="Generate multi-depth continuations from seed texts")
    parser.add_argument("--input", type=str, default="data/wiki_seed_1000.jsonl",
                        help="Local seed JSONL file path")
    parser.add_argument("--output-dir", type=str, default="data/",
                        help="Output base directory")
    parser.add_argument("--shard-id", type=int, default=0, help="Shard index (0-based)")
    parser.add_argument("--num-shards", type=int, default=1, help="Total number of shards")
    parser.add_argument("--device", type=str, default="cuda:0", help="CUDA device")
    parser.add_argument("--dry-run", action="store_true", help="Only process first 2 seeds")
    parser.add_argument("--model-name", type=str, default=DEFAULT_MODEL_NAME,
                        help="Generator name for output directory (e.g. 'pythia-1b')")
    parser.add_argument("--repetition-penalty", type=float, default=1.0, help="Repetition penalty for generation")
    parser.add_argument("--temperature", type=float, default=0.7, help="Sampling temperature")
    parser.add_argument("--top-p", type=float, default=0.9, help="Nucleus sampling top-p")
    parser.add_argument("--model-path", type=str, default=None,
                        help="Local model path (HF format). Defaults to Pythia-2.8B")
    args = parser.parse_args()

    device = torch.device(args.device)

    if args.model_path:
        model_path = args.model_path
    elif args.model_name in MODEL_NAME_MAP:
        model_path = MODEL_NAME_MAP[args.model_name]
    else:
        model_path = find_default_model_path()
    print(f"Loading model '{args.model_name}' from {model_path} ...")

    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_path, dtype=torch.float16, trust_remote_code=True,
    ).to(device)
    model.eval()
    print(f"Model loaded on {device}, dtype={model.dtype}, vocab={model.config.vocab_size}")

    project_root = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(project_root, args.input) if not os.path.isabs(args.input) else args.input
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Seed file not found: {input_path}")
    all_seeds = load_seeds(input_path, tokenizer)

    total = len(all_seeds)
    shard_size = total // args.num_shards
    start = args.shard_id * shard_size
    end = start + shard_size if args.shard_id < args.num_shards - 1 else total
    seeds = all_seeds[start:end]
    print(f"Shard {args.shard_id}/{args.num_shards}: seeds [{start}:{end}] ({len(seeds)} seeds)")

    if args.dry_run:
        seeds = seeds[:2]
        print(f"[DRY-RUN] Processing only {len(seeds)} seeds")

    output_dir = os.path.join(project_root, args.output_dir) if not os.path.isabs(args.output_dir) else args.output_dir
    output_dir = os.path.join(output_dir, args.model_name)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"generations_shard{args.shard_id}.jsonl")

    # Resume support: skip already-completed seeds
    done_seeds = load_done_seeds(output_path)
    if done_seeds:
        print(f"Resuming: found {len(done_seeds)} completed seeds, skipping")

    t0 = time.time()
    record_count = 0
    skipped = 0

    with open(output_path, "a") as f:
        for i, seed_info in enumerate(tqdm(seeds, desc=f"Seeds (shard {args.shard_id})")):
            seed_id = seed_info["seed_id"]
            seed_text = seed_info["text"]

            if seed_id in done_seeds:
                continue

            base_id = args.shard_id * shard_size * NUM_DEPTHS + i * NUM_DEPTHS

            gen0_tokens = tokenizer.encode(seed_text, add_special_tokens=False)
            f.write(json.dumps({
                "id": base_id,
                "depth": 0,
                "text": seed_text,
                "seed_id": seed_id,
                "token_count": len(gen0_tokens),
                "model": args.model_name,
            }, ensure_ascii=False) + "\n")
            f.flush()
            record_count += 1

            prev_text = seed_text
            for depth in range(1, NUM_DEPTHS):
                check_ids = tokenizer.encode(prev_text, add_special_tokens=False)
                if len(check_ids) == 0 or len(prev_text.strip()) < 10:
                    print(f"WARNING: Skipping seed {seed_id} at depth {depth}: empty input")
                    skipped += 1
                    break

                continuation = generate_continuation(model, tokenizer, prev_text, device, repetition_penalty=args.repetition_penalty, temperature=args.temperature, top_p=args.top_p)
                if not continuation or len(continuation.strip()) == 0:
                    print(f"WARNING: Skipping seed {seed_id} at depth {depth}: empty output")
                    skipped += 1
                    break

                cont_tokens = tokenizer.encode(continuation, add_special_tokens=False)
                f.write(json.dumps({
                    "id": base_id + depth,
                    "depth": depth,
                    "text": continuation,
                    "seed_id": seed_id,
                    "token_count": len(cont_tokens),
                    "model": args.model_name,
                }, ensure_ascii=False) + "\n")
                f.flush()
                record_count += 1
                prev_text = continuation

            if (i + 1) % 50 == 0:
                elapsed = time.time() - t0
                print(f"[{i+1}/{len(seeds)}] {elapsed:.0f}s elapsed, {(i+1)/elapsed:.2f} seeds/s")

    elapsed = time.time() - t0
    print(f"Done. {record_count} records written to {output_path} in {elapsed:.1f}s (skipped {skipped})")


if __name__ == "__main__":
    main()

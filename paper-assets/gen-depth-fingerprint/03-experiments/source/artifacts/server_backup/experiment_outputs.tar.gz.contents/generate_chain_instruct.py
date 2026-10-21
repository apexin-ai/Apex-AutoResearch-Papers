"""
generate_chain_instruct.py — Generation chains for instruction-tuned models.

Uses chat template (apply_chat_template) instead of raw continuation.
System prompt asks the model to continue the text; thinking mode disabled.

Output format identical to generate_chain.py for downstream compatibility.
"""

import argparse
import json
import os
import signal
import time

import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

signal.signal(signal.SIGHUP, signal.SIG_IGN)

torch.manual_seed(42)
torch.cuda.manual_seed(42)

MAX_DEPTH = 4
NUM_DEPTHS = MAX_DEPTH + 1

SYSTEM_PROMPT = "Continue the following text naturally. Output only the continuation, without repeating the original text or adding any preamble."


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


def generate_continuation(model, tokenizer, text, device, max_new_tokens=256):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": text},
    ]
    prompt_text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,
    )
    input_ids = tokenizer.encode(prompt_text, add_special_tokens=False)
    # Truncate if too long (keep last 512 tokens of prompt)
    if len(input_ids) > 512:
        input_ids = input_ids[-512:]
    input_tensor = torch.tensor([input_ids], device=device)

    with torch.no_grad():
        output = model.generate(
            input_tensor,
            max_new_tokens=max_new_tokens,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            pad_token_id=tokenizer.pad_token_id,
        )

    new_tokens = output[0][len(input_ids):]
    result = tokenizer.decode(new_tokens, skip_special_tokens=True)
    return result.strip()


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
    parser = argparse.ArgumentParser(description="Generate chains with instruct models using chat template")
    parser.add_argument("--input", type=str, default="data/wiki_seed_1000.jsonl")
    parser.add_argument("--output-dir", type=str, default="data/")
    parser.add_argument("--shard-id", type=int, default=0)
    parser.add_argument("--num-shards", type=int, default=1)
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--model-name", type=str, required=True)
    parser.add_argument("--model-path", type=str, required=True)
    args = parser.parse_args()

    device = torch.device(args.device)
    print(f"Loading model '{args.model_name}' from {args.model_path} ...")

    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        args.model_path, dtype=torch.float16, trust_remote_code=True,
    ).to(device)
    model.eval()
    print(f"Model loaded on {device}, dtype={model.dtype}")

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
                if len(prev_text.strip()) < 10:
                    print(f"WARNING: Skipping seed {seed_id} at depth {depth}: short input")
                    skipped += 1
                    break

                continuation = generate_continuation(model, tokenizer, prev_text, device)
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

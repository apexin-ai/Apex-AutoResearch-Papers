# Synthetic data generation with Qwen3-4B.
# Usage: python generate.py --model Qwen/Qwen3-4B --data_dir ./data --output ./data/gen_0/synthetic.pt --num_tokens 500000

import argparse
import os
import json
from pathlib import Path

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model", type=str, default="Qwen/Qwen3-4B")
    p.add_argument("--data_dir", type=str, default="./data")
    p.add_argument("--output", type=str, required=True,
                   help="Output path for synthetic data, e.g. ./data/gen_0/synthetic.pt")
    p.add_argument("--num_tokens", type=int, default=500_000,
                   help="Approximate total tokens to generate")
    p.add_argument("--batch_size", type=int, default=8)
    p.add_argument("--max_new_tokens", type=int, default=512)
    p.add_argument("--temperature", type=float, default=0.8)
    p.add_argument("--top_p", type=float, default=0.95)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--device", type=str, default="cuda:0")
    return p.parse_args()


def build_prompts(train_chunks, tokenizer, num_prompts, prompt_len=64):
    """Sample prefix prompts from real training data."""
    rng = torch.Generator().manual_seed(42)
    indices = torch.randperm(len(train_chunks), generator=rng)[:num_prompts].tolist()
    prompts = []
    for idx in indices:
        chunk = train_chunks[idx]
        prefix = chunk[:prompt_len]
        prompts.append(tokenizer.decode(prefix, skip_special_tokens=True))
    return prompts


@torch.no_grad()
def generate_batch(model, tokenizer, prompts, max_new_tokens, temperature, top_p, device):
    inputs = tokenizer(prompts, return_tensors="pt", padding=True, truncation=True,
                       max_length=128).to(device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_p=top_p,
        do_sample=True,
        pad_token_id=tokenizer.pad_token_id,
    )
    # only keep newly generated tokens
    generated = outputs[:, inputs["input_ids"].shape[1]:]
    return generated


def main():
    args = parse_args()
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    torch.manual_seed(args.seed)

    print(f"Loading generator model: {args.model}")
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        args.model, torch_dtype=torch.bfloat16, trust_remote_code=True
    ).to(args.device).eval()

    train_chunks = torch.load(Path(args.data_dir) / "train_chunks.pt", weights_only=True)

    num_prompts = (args.num_tokens // args.max_new_tokens) + 1
    print(f"Generating ~{args.num_tokens} tokens ({num_prompts} prompts × {args.max_new_tokens} tokens)")

    prompts = build_prompts(train_chunks, tokenizer, num_prompts)

    all_generated = []
    total_tokens = 0
    for i in range(0, len(prompts), args.batch_size):
        batch_prompts = prompts[i:i + args.batch_size]
        generated = generate_batch(
            model, tokenizer, batch_prompts,
            args.max_new_tokens, args.temperature, args.top_p, args.device
        )
        for seq in generated:
            # remove padding
            seq = seq[seq != tokenizer.pad_token_id].tolist()
            if len(seq) > 0:
                all_generated.append(seq)
                total_tokens += len(seq)

        if (i // args.batch_size) % 10 == 0:
            print(f"  Batch {i // args.batch_size}: {total_tokens} tokens generated so far")

        if total_tokens >= args.num_tokens:
            break

    print(f"Total generated: {len(all_generated)} sequences, {total_tokens} tokens")
    torch.save(all_generated, args.output)

    meta = {
        "generator_model": args.model,
        "num_sequences": len(all_generated),
        "total_tokens": total_tokens,
        "max_new_tokens": args.max_new_tokens,
        "temperature": args.temperature,
        "top_p": args.top_p,
        "seed": args.seed,
    }
    meta_path = Path(args.output).with_suffix(".json")
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2)
    print(f"Metadata saved to {meta_path}")


if __name__ == "__main__":
    main()

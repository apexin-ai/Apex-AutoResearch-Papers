"""
Multi-depth synthetic data generation on FineWeb subsets.

Pipeline position: Step 1 — generates depth-1/2/3 synthetic text from FineWeb human text (depth-0).
Depth 1: LLM continues/rewrites depth-0 text.
Depth 2: model fine-tuned on depth-1 data generates text.
Depth 3+: recursive application of the same pattern.

Output: JSONL files with text, depth, source_model, decoding metadata.
"""

import argparse
import json
import os
import time
from pathlib import Path

import torch
from datasets import load_dataset
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate multi-depth synthetic text from FineWeb using LLMs."
    )
    parser.add_argument("--model_name", type=str, default="Qwen/Qwen3-0.6B",
                        help="HuggingFace model for generation")
    parser.add_argument("--depth", type=int, required=True, choices=[1, 2, 3],
                        help="Generation depth (1/2/3)")
    parser.add_argument("--num_tokens", type=int, default=100_000_000,
                        help="Target total generated tokens")
    parser.add_argument("--output_dir", type=str, required=True,
                        help="Output directory for JSONL files")
    parser.add_argument("--fineweb_subset", type=str, default="sample-10BT",
                        help="FineWeb subset name")
    parser.add_argument("--batch_size", type=int, default=16,
                        help="Generation batch size")
    parser.add_argument("--max_length", type=int, default=512,
                        help="Max total sequence length (prompt + generation)")
    parser.add_argument("--prompt_length", type=int, default=128,
                        help="Number of tokens to use as prompt from source text")
    parser.add_argument("--temperature", type=float, default=0.8,
                        help="Sampling temperature")
    parser.add_argument("--top_p", type=float, default=0.95,
                        help="Nucleus sampling p")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed")
    parser.add_argument("--num_workers", type=int, default=4,
                        help="Data loading workers")
    parser.add_argument("--previous_model_path", type=str, default=None,
                        help="Path to fine-tuned model from previous depth (required for depth>1)")
    parser.add_argument("--local_data", type=str, default=None,
                        help="Path to local parquet dir (bypasses FineWeb streaming for depth 1)")
    return parser.parse_args()


def get_decoding_tag(args):
    return f"nucleus_p{args.top_p}_t{args.temperature}"


def load_checkpoint(output_path):
    """Resume from last checkpoint — returns (num_docs, num_tokens) already generated."""
    if not output_path.exists():
        return 0, 0
    num_docs = 0
    num_tokens = 0
    with open(output_path, "r") as f:
        for line in f:
            try:
                rec = json.loads(line)
                num_docs += 1
                num_tokens += rec.get("generated_tokens", 0)
            except json.JSONDecodeError:
                continue
    return num_docs, num_tokens


def build_source_iterator(args):
    """Return an iterator over source texts.

    Depth 1: stream from FineWeb.
    Depth 2/3: read JSONL from previous depth output.
    """
    if args.depth == 1:
        if args.local_data:
            import pyarrow.parquet as pq
            parquet_dir = Path(args.local_data)
            for pf in sorted(parquet_dir.glob("*.parquet")):
                table = pq.read_table(pf, columns=["text"])
                for text in table.column("text").to_pylist():
                    if text and len(text.split()) > 20:
                        yield text
        else:
            ds = load_dataset(
                "HuggingFaceFW/fineweb",
                name=args.fineweb_subset,
                split="train",
                streaming=True,
            )
            for example in ds:
                text = example.get("text", "")
                if text and len(text.split()) > 20:
                    yield text
    else:
        prev_depth = args.depth - 1
        if args.previous_model_path is None:
            prev_dir = Path(args.output_dir)
        else:
            prev_dir = Path(args.previous_model_path).parent
        pattern = f"depth_{prev_depth}_*.jsonl"
        prev_files = sorted(prev_dir.glob(pattern))
        if not prev_files:
            prev_files = sorted(Path(args.output_dir).glob(pattern))
        if not prev_files:
            raise FileNotFoundError(
                f"No depth-{prev_depth} JSONL files found. Generate depth {prev_depth} first."
            )
        for fpath in prev_files:
            with open(fpath, "r") as f:
                for line in f:
                    try:
                        rec = json.loads(line)
                        text = rec.get("text", "")
                        if text and len(text.split()) > 20:
                            yield text
                    except json.JSONDecodeError:
                        continue


def batch_iterator(iterator, batch_size):
    batch = []
    for item in iterator:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch


def main():
    args = parse_args()
    torch.manual_seed(args.seed)

    os.makedirs(args.output_dir, exist_ok=True)

    decoding_tag = get_decoding_tag(args)
    output_filename = f"depth_{args.depth}_{decoding_tag}.jsonl"
    output_path = Path(args.output_dir) / output_filename

    resumed_docs, resumed_tokens = load_checkpoint(output_path)
    if resumed_tokens > 0:
        print(f"Resuming from checkpoint: {resumed_docs} docs, {resumed_tokens} tokens")

    model_path = args.model_name
    if args.depth > 1 and args.previous_model_path:
        model_path = args.previous_model_path
        print(f"Using fine-tuned model from previous depth: {model_path}")

    print(f"Loading model: {model_path}")
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"

    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        device_map="cuda:0",
        trust_remote_code=True,
    )
    model.eval()

    gen_tokens_per_doc = args.max_length - args.prompt_length
    total_tokens_generated = resumed_tokens
    total_docs = resumed_docs
    checkpoint_interval = 10000
    docs_since_checkpoint = 0

    source_iter = build_source_iterator(args)
    # Skip already-processed documents when resuming
    if resumed_docs > 0:
        print(f"Skipping {resumed_docs} already-processed documents...")
        for _ in zip(range(resumed_docs), source_iter):
            pass

    file_mode = "a" if resumed_tokens > 0 else "w"
    outfile = open(output_path, file_mode)

    pbar = tqdm(total=args.num_tokens, initial=resumed_tokens, unit="tok", desc=f"Depth {args.depth}")

    try:
        for batch_texts in batch_iterator(source_iter, args.batch_size):
            if total_tokens_generated >= args.num_tokens:
                break

            # Truncate source texts to prompt_length tokens
            encoded = tokenizer(
                batch_texts,
                max_length=args.prompt_length,
                truncation=True,
                padding=True,
                return_tensors="pt",
            )
            input_ids = encoded["input_ids"].to(model.device)
            attention_mask = encoded["attention_mask"].to(model.device)

            with torch.no_grad():
                outputs = model.generate(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    max_new_tokens=gen_tokens_per_doc,
                    do_sample=True,
                    temperature=args.temperature,
                    top_p=args.top_p,
                    pad_token_id=tokenizer.pad_token_id,
                )

            for i, output_ids in enumerate(outputs):
                prompt_len = (input_ids[i] != tokenizer.pad_token_id).sum().item()
                generated_ids = output_ids[prompt_len:]
                generated_text = tokenizer.decode(generated_ids, skip_special_tokens=True)
                num_gen_tokens = len(generated_ids)

                if not generated_text.strip():
                    continue

                record = {
                    "text": generated_text,
                    "depth": args.depth,
                    "source_model": model_path,
                    "prompt_tokens": prompt_len,
                    "generated_tokens": num_gen_tokens,
                    "decoding": decoding_tag,
                }
                outfile.write(json.dumps(record, ensure_ascii=False) + "\n")

                total_tokens_generated += num_gen_tokens
                total_docs += 1
                docs_since_checkpoint += 1
                pbar.update(num_gen_tokens)

            if docs_since_checkpoint >= checkpoint_interval:
                outfile.flush()
                docs_since_checkpoint = 0

            if total_tokens_generated >= args.num_tokens:
                break

    except KeyboardInterrupt:
        print("\nInterrupted. Saving checkpoint...")
    finally:
        outfile.flush()
        outfile.close()
        pbar.close()

    print(f"Done. Generated {total_docs} documents, ~{total_tokens_generated} tokens.")
    print(f"Output: {output_path}")


if __name__ == "__main__":
    main()

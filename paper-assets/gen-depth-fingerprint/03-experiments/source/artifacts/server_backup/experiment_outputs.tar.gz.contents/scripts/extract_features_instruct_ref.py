"""
extract_features_instruct_ref.py — Extract NLL features using Qwen3-0.6B (instruct) as reference model.

Purpose: Test whether an instruct reference model recovers DDR signal on instruct-generated chains,
compared to the base Pythia-410M reference model.

Input: data/{qwen3-1.7b-instruct,olmo-2-0425-1b-instruct}/generations_shard0.jsonl
Output: data/features_instruct_ref_qwen06b.csv
        columns: generator, id, depth, seed_id, entropy_mean, entropy_std, entropy_min, entropy_max,
                 tail_decay, ttr, hapax_ratio
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_PATH = "/root/autodl-tmp/models/qwen3-0.6b-instruct/Qwen/Qwen3-0.6B"

GENERATORS = {
    "qwen3-1.7b-instruct": "data/qwen3-1.7b-instruct/generations_shard0.jsonl",
    "olmo-2-0425-1b-instruct": "data/olmo-2-0425-1b-instruct/generations_shard0.jsonl",
}


def load_data(input_path: str) -> list[dict]:
    records = []
    with open(input_path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    print(f"  Loaded {len(records)} records from {input_path}")
    return records


def load_model(device: str):
    print(f"Loading reference model from {MODEL_PATH} on {device}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, local_files_only=True, torch_dtype=torch.float16,
    ).to(device).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    print("Model loaded")
    return tokenizer, model


def compute_reference_features(texts, tokenizer, model, device, batch_size):
    results = []
    for start in range(0, len(texts), batch_size):
        batch_texts = texts[start:start + batch_size]
        encodings = tokenizer(
            batch_texts, return_tensors="pt", padding=True,
            truncation=True, max_length=512,
        ).to(device)

        with torch.no_grad():
            logits = model(**encodings).logits

        for i in range(len(batch_texts)):
            mask = encodings["attention_mask"][i].bool()
            seq_len = mask.sum().item()
            if seq_len < 2:
                results.append(dict(entropy_mean=0., entropy_std=0., entropy_min=0.,
                                    entropy_max=0., tail_decay=0.))
                continue

            token_logits = logits[i, :seq_len - 1, :]
            log_probs = torch.log_softmax(token_logits, dim=-1)
            probs = torch.exp(log_probs)
            entropy = -(probs * log_probs).sum(dim=-1)
            entropy_np = entropy.float().cpu().numpy()

            avg_log_probs = log_probs.float().mean(dim=0)
            sorted_lp, _ = torch.sort(avg_log_probs, descending=True)
            sorted_lp_np = sorted_lp.cpu().numpy()

            vocab_size = sorted_lp_np.shape[0]
            hi = min(1000, vocab_size)
            lo = min(100, hi)
            if hi - lo >= 2:
                x = np.arange(lo, hi, dtype=np.float64)
                y = sorted_lp_np[lo:hi].astype(np.float64)
                coeffs = np.polyfit(x, y, 1)
                tail_decay = float(coeffs[0])
            else:
                tail_decay = 0.0

            results.append(dict(
                entropy_mean=float(np.mean(entropy_np)),
                entropy_std=float(np.std(entropy_np)),
                entropy_min=float(np.min(entropy_np)),
                entropy_max=float(np.max(entropy_np)),
                tail_decay=tail_decay,
            ))

        if (start // batch_size) % 20 == 0:
            print(f"    {min(start + batch_size, len(texts))}/{len(texts)}")

    return results


def compute_surface_features(texts):
    results = []
    for text in texts:
        words = text.lower().split()
        n = len(words)
        if n == 0:
            results.append(dict(ttr=0., hapax_ratio=0.))
            continue
        counter = Counter(words)
        results.append(dict(
            ttr=len(counter) / n,
            hapax_ratio=sum(1 for c in counter.values() if c == 1) / n,
        ))
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent

    tokenizer, model = load_model(args.device)

    all_rows = []
    for gen_name, rel_path in GENERATORS.items():
        input_path = project_root / rel_path
        print(f"\nProcessing {gen_name}...")
        records = load_data(str(input_path))
        if args.dry_run:
            records = records[:10]
            print(f"  [dry-run] Using 10 records")

        texts = [r["text"] for r in records]

        ref_feats = compute_reference_features(texts, tokenizer, model, args.device, args.batch_size)
        surf_feats = compute_surface_features(texts)

        for rec, ref, surf in zip(records, ref_feats, surf_feats):
            all_rows.append(dict(
                generator=gen_name,
                id=rec["id"],
                depth=rec["depth"],
                seed_id=rec["seed_id"],
                **ref, **surf,
            ))

    del model, tokenizer
    torch.cuda.empty_cache()

    df = pd.DataFrame(all_rows)
    out_path = project_root / "data" / "features_instruct_ref_qwen06b.csv"
    df.to_csv(out_path, index=False)
    print(f"\nSaved {df.shape} to {out_path}")
    print(df.groupby("generator").describe().T)


if __name__ == "__main__":
    main()

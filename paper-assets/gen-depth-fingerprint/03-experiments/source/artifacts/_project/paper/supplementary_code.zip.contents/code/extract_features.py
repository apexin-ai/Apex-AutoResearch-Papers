# Anonymous submission — EMNLP 2026 ARR
"""
extract_features.py -- Extract reference model features and surface features from generations.

Input: data/generations.jsonl (each line: {"id","depth","text","seed_id","token_count"})
Output: data/features.csv (id, depth, seed_id, entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay, ttr, hapax_ratio)
Dependencies: torch, transformers, numpy, pandas
"""

import argparse
import json
import os
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def make_synthetic_records(n: int = 10) -> list[dict]:
    """Generate synthetic records for dry-run testing."""
    records = []
    for i in range(n):
        depth = i % 5
        records.append({
            "id": i,
            "depth": depth,
            "text": f"This is a synthetic test sentence number {i} for depth {depth}. "
                    f"The quick brown fox jumps over the lazy dog. "
                    f"Additional words to ensure sufficient length for feature extraction. "
                    f"More padding text with varied vocabulary including unique uncommon words "
                    f"like serendipity and concatenation and ephemeral.",
            "seed_id": i // 5,
            "token_count": 50,
        })
    return records


def load_data(input_path: str, dry_run: bool = False) -> list[dict]:
    """Load jsonl data. In dry-run mode, fall back to synthetic data if file missing or empty."""
    records = []

    if os.path.exists(input_path) and os.path.getsize(input_path) > 0:
        with open(input_path, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(json.loads(line))

    if dry_run:
        if not records:
            print("[dry-run] No input data available, generating 10 synthetic records")
            return make_synthetic_records(10)
        records = records[:10]
        print(f"[dry-run] Using first 10 records from file")

    print(f"Loaded {len(records)} records")
    return records


def load_model(model_path: str, device: str):
    """Load tokenizer and model from local path."""
    print(f"Loading model from {model_path} on {device}")
    tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, local_files_only=True, torch_dtype=torch.float16,
    ).to(device).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    print("Model loaded")
    return tokenizer, model


def compute_reference_features(texts: list[str], tokenizer, model, device: str, batch_size: int) -> list[dict]:
    """
    Compute per-text entropy stats and tail_decay using the reference model.

    Returns list of dicts with keys:
      entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay
    """
    results = []
    for start in range(0, len(texts), batch_size):
        batch_texts = texts[start : start + batch_size]
        encodings = tokenizer(
            batch_texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512,
        ).to(device)

        with torch.no_grad():
            outputs = model(**encodings)
            logits = outputs.logits  # (B, seq_len, vocab)

        for i in range(len(batch_texts)):
            mask = encodings["attention_mask"][i].bool()
            seq_len = mask.sum().item()
            if seq_len < 2:
                results.append({
                    "entropy_mean": 0.0, "entropy_std": 0.0,
                    "entropy_min": 0.0, "entropy_max": 0.0,
                    "tail_decay": 0.0,
                })
                continue

            # Token-level entropy: logits[0..T-2] predict tokens[1..T-1]
            token_logits = logits[i, :seq_len - 1, :]  # (T-1, V)
            log_probs = torch.log_softmax(token_logits, dim=-1)
            probs = torch.exp(log_probs)
            entropy = -(probs * log_probs).sum(dim=-1)  # (T-1,)
            entropy_np = entropy.float().cpu().numpy()

            # Tail decay: average log-prob distribution, fit slope on ranks 100-1000
            avg_log_probs = log_probs.float().mean(dim=0)  # (V,)
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

            results.append({
                "entropy_mean": float(np.mean(entropy_np)),
                "entropy_std": float(np.std(entropy_np)),
                "entropy_min": float(np.min(entropy_np)),
                "entropy_max": float(np.max(entropy_np)),
                "tail_decay": tail_decay,
            })

        print(f"  Processed {min(start + batch_size, len(texts))}/{len(texts)} texts")

    return results


def compute_surface_features(texts: list[str]) -> list[dict]:
    """
    Compute surface-level text statistics: type-token ratio and hapax ratio.

    Returns list of dicts with keys: ttr, hapax_ratio
    """
    results = []
    for text in texts:
        words = text.lower().split()
        n_tokens = len(words)
        if n_tokens == 0:
            results.append({"ttr": 0.0, "hapax_ratio": 0.0})
            continue

        counter = Counter(words)
        n_unique = len(counter)
        n_hapax = sum(1 for c in counter.values() if c == 1)

        results.append({
            "ttr": n_unique / n_tokens,
            "hapax_ratio": n_hapax / n_tokens,
        })
    return results


def main():
    parser = argparse.ArgumentParser(description="Extract features from generations")
    parser.add_argument("--input", default="../data/generations.jsonl", help="Input jsonl path")
    parser.add_argument("--output", default="../data/features.csv", help="Output csv path")
    parser.add_argument("--batch-size", type=int, default=8, help="GPU batch size")
    parser.add_argument("--device", default="cuda:0", help="CUDA device")
    parser.add_argument("--dry-run", action="store_true", help="Process only first 10 records")
    parser.add_argument("--ref-model", type=str, required=True,
                        help="Path to reference model (e.g. Pythia-410M)")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent
    input_path = project_root / args.input
    output_path = project_root / args.output

    records = load_data(str(input_path), dry_run=args.dry_run)
    if not records:
        print("No records to process")
        sys.exit(1)

    texts = [r["text"] for r in records]

    tokenizer, model = load_model(args.ref_model, args.device)
    ref_features = compute_reference_features(texts, tokenizer, model, args.device, args.batch_size)

    del model, tokenizer
    torch.cuda.empty_cache()

    surf_features = compute_surface_features(texts)

    rows = []
    for rec, ref, surf in zip(records, ref_features, surf_features):
        rows.append({
            "id": rec["id"],
            "depth": rec["depth"],
            "seed_id": rec["seed_id"],
            **ref,
            **surf,
        })

    df = pd.DataFrame(rows)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\nFeatures saved to {output_path}")
    print(f"Shape: {df.shape}")
    print(df.describe())


if __name__ == "__main__":
    main()

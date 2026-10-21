# Anonymous submission — EMNLP 2026 ARR
"""extract_features_jsonl.py -- extract features to JSONL format (matching features_pythia410m.jsonl)"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--ref-model", type=str, required=True,
                        help="Path to reference model (e.g. Pythia-410M)")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    records = []
    with open(input_path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    print(f"Loaded {len(records)} records")

    print(f"Loading model from {args.ref_model} on {args.device}")
    tokenizer = AutoTokenizer.from_pretrained(args.ref_model, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.ref_model, local_files_only=True, torch_dtype=torch.float16,
    ).to(args.device).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    print("Model loaded")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    out_f = open(output_path, "w")
    n_written = 0

    for start in range(0, len(records), args.batch_size):
        batch_records = records[start:start + args.batch_size]
        batch_texts = [r["text"] for r in batch_records]

        encodings = tokenizer(
            batch_texts, return_tensors="pt", padding=True,
            truncation=True, max_length=512,
        ).to(args.device)

        with torch.no_grad():
            logits = model(**encodings).logits

        for i, rec in enumerate(batch_records):
            mask = encodings["attention_mask"][i].bool()
            seq_len = mask.sum().item()

            if seq_len < 2:
                ref = {"entropy_mean": 0.0, "entropy_std": 0.0,
                       "entropy_min": 0.0, "entropy_max": 0.0, "tail_decay": 0.0}
            else:
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

                ref = {
                    "entropy_mean": float(np.mean(entropy_np)),
                    "entropy_std": float(np.std(entropy_np)),
                    "entropy_min": float(np.min(entropy_np)),
                    "entropy_max": float(np.max(entropy_np)),
                    "tail_decay": tail_decay,
                }

            words = rec["text"].lower().split()
            n_tokens = len(words)
            if n_tokens == 0:
                ttr, hapax_ratio = 0.0, 0.0
            else:
                counter = Counter(words)
                ttr = len(counter) / n_tokens
                hapax_ratio = sum(1 for c in counter.values() if c == 1) / n_tokens

            row = {
                "seed_id": rec["seed_id"],
                "depth": rec["depth"],
                **ref,
                "ttr": ttr,
                "hapax_ratio": hapax_ratio,
            }
            out_f.write(json.dumps(row) + "\n")
            n_written += 1

        if (start // args.batch_size) % 50 == 0:
            print(f"  [{min(start + args.batch_size, len(records))}/{len(records)}]")
            out_f.flush()

    out_f.close()
    del model, tokenizer
    torch.cuda.empty_cache()
    print(f"\nDone: {n_written} records written to {output_path}")


if __name__ == "__main__":
    main()

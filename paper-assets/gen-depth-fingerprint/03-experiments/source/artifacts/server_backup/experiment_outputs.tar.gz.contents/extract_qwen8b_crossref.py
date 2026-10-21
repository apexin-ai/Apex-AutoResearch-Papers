"""Extract cross-ref features for qwen3-8b only, append to existing CSVs."""

import argparse
import json
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def load_qwen8b_records(project_root: Path) -> list[dict]:
    data_dir = project_root / "data" / "qwen3-8b"
    paths = [data_dir / "generations.jsonl"] + sorted(data_dir.glob("generations_shard*.jsonl"))
    paths = [p for p in paths if p.exists() and p.stat().st_size > 0]

    records = []
    seen_ids = set()
    for p in paths:
        with open(p) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                key = (rec.get("seed_id"), rec.get("depth"))
                if key in seen_ids:
                    continue
                seen_ids.add(key)
                rec["model_name"] = "qwen3-8b"
                records.append(rec)
    return records


def load_model(model_path: str, device: str):
    print(f"Loading reference model from {model_path} on {device}")
    tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, local_files_only=True, torch_dtype=torch.float16,
    ).to(device).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    print("Reference model loaded")
    return tokenizer, model


def compute_reference_features(texts, tokenizer, model, device, batch_size):
    results = []
    for start in range(0, len(texts), batch_size):
        batch_texts = texts[start:start + batch_size]
        encodings = tokenizer(
            batch_texts, return_tensors="pt", padding=True, truncation=True, max_length=512,
        ).to(device)

        with torch.no_grad():
            logits = model(**encodings).logits

        for i in range(len(batch_texts)):
            mask = encodings["attention_mask"][i].bool()
            seq_len = mask.sum().item()
            if seq_len < 2:
                results.append({"entropy_mean": 0.0, "entropy_std": 0.0,
                                "entropy_min": 0.0, "entropy_max": 0.0, "tail_decay": 0.0})
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

            results.append({
                "entropy_mean": float(np.mean(entropy_np)),
                "entropy_std": float(np.std(entropy_np)),
                "entropy_min": float(np.min(entropy_np)),
                "entropy_max": float(np.max(entropy_np)),
                "tail_decay": tail_decay,
            })

        done = min(start + batch_size, len(texts))
        if (start // batch_size) % 10 == 0:
            print(f"  [{done}/{len(texts)}]")

    return results


def compute_surface_features(texts):
    results = []
    for text in texts:
        words = text.lower().split()
        n_tokens = len(words)
        if n_tokens == 0:
            results.append({"ttr": 0.0, "hapax_ratio": 0.0})
            continue
        counter = Counter(words)
        results.append({
            "ttr": len(counter) / n_tokens,
            "hapax_ratio": sum(1 for c in counter.values() if c == 1) / n_tokens,
        })
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference-model", required=True)
    parser.add_argument("--output", required=True, help="Output CSV for just qwen3-8b rows")
    parser.add_argument("--append-to", required=True, help="Existing CSV to append to")
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--device", default="cuda:0")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent

    records = load_qwen8b_records(project_root)
    print(f"Loaded {len(records)} qwen3-8b records")

    tokenizer, model = load_model(args.reference_model, args.device)

    texts = [r["text"] for r in records]
    ref_features = compute_reference_features(texts, tokenizer, model, args.device, args.batch_size)
    surf_features = compute_surface_features(texts)

    del model, tokenizer
    torch.cuda.empty_cache()

    rows = []
    for rec, ref, surf in zip(records, ref_features, surf_features):
        rows.append({
            "model_name": "qwen3-8b",
            "seed_id": rec["seed_id"],
            "depth": rec["depth"],
            **ref, **surf,
        })

    df_new = pd.DataFrame(rows)
    df_new.to_csv(args.output, index=False)
    print(f"Saved {len(df_new)} rows to {args.output}")

    # Append to existing CSV
    df_existing = pd.read_csv(args.append_to)
    df_existing = df_existing[df_existing["model_name"] != "qwen3-8b"]  # remove if exists
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    df_combined.to_csv(args.append_to, index=False)
    print(f"Appended to {args.append_to}: {df_combined.shape}")
    print(f"Generators: {sorted(df_combined['model_name'].unique())}")


if __name__ == "__main__":
    main()

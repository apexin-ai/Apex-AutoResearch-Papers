"""
extract_features_crossref.py — 支持任意参考模型的特征提取
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

ALL_GENERATORS = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-1.7b", "qwen3-0.6b"]


def discover_data(project_root: Path, model_name: str) -> list[Path]:
    if model_name == "pythia-2.8b":
        candidates = [
            project_root / "data" / "generations.jsonl",
            *sorted((project_root / "data").glob("generations_shard*.jsonl")),
        ]
    else:
        model_dir = project_root / "data" / model_name
        candidates = [
            model_dir / "generations.jsonl",
            *sorted(model_dir.glob("generations_shard*.jsonl")),
        ]
    return [p for p in candidates if p.exists() and p.stat().st_size > 0]


def load_records(paths: list[Path], model_name: str) -> list[dict]:
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
                rec["model_name"] = rec.get("model", model_name)
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


def compute_reference_features(texts: list[str], tokenizer, model, device: str, batch_size: int) -> list[dict]:
    results = []
    for start in range(0, len(texts), batch_size):
        batch_texts = texts[start:start + batch_size]
        encodings = tokenizer(
            batch_texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512,
        ).to(device)

        with torch.no_grad():
            logits = model(**encodings).logits

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

        if (start // batch_size) % 10 == 0:
            print(f"  [{min(start + batch_size, len(texts))}/{len(texts)}]")

    return results


def compute_surface_features(texts: list[str]) -> list[dict]:
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


def extract_one_model(model_name: str, project_root: Path, tokenizer, model, device: str, batch_size: int) -> pd.DataFrame:
    paths = discover_data(project_root, model_name)
    if not paths:
        print(f"  [SKIP] No data found for {model_name}")
        return pd.DataFrame()

    print(f"  Loading {model_name}: {[p.name for p in paths]}")
    records = load_records(paths, model_name)
    if not records:
        return pd.DataFrame()
    print(f"  {len(records)} records loaded")

    texts = [r["text"] for r in records]
    ref_features = compute_reference_features(texts, tokenizer, model, device, batch_size)
    surf_features = compute_surface_features(texts)

    rows = []
    for rec, ref, surf in zip(records, ref_features, surf_features):
        rows.append({
            "model_name": model_name,
            "seed_id": rec["seed_id"],
            "depth": rec["depth"],
            **ref,
            **surf,
        })
    return pd.DataFrame(rows)


def main():
    parser = argparse.ArgumentParser(description="Cross-reference model feature extraction for plan-003")
    parser.add_argument("--reference-model", type=str, required=True,
                        help="Path to the reference model (local directory)")
    parser.add_argument("--output", required=True, help="Output CSV path")
    parser.add_argument("--batch-size", type=int, default=8, help="GPU batch size")
    parser.add_argument("--device", default="cuda:0", help="CUDA device")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent
    output_path = project_root / args.output

    tokenizer, model = load_model(args.reference_model, args.device)

    all_dfs = []
    for m in ALL_GENERATORS:
        print(f"\n=== Processing: {m} ===")
        df = extract_one_model(m, project_root, tokenizer, model, args.device, args.batch_size)
        if not df.empty:
            all_dfs.append(df)
            print(f"  -> {len(df)} rows")

    del model, tokenizer
    torch.cuda.empty_cache()

    if not all_dfs:
        print("No data extracted")
        sys.exit(1)

    combined = pd.concat(all_dfs, ignore_index=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    combined.to_csv(output_path, index=False)

    print(f"\nFeatures saved to {output_path}")
    print(f"Shape: {combined.shape}")
    print(f"Models: {combined['model_name'].value_counts().to_dict()}")


if __name__ == "__main__":
    main()

"""
extract_features_multi.py — 多生成器特征提取

从各生成器的 generations jsonl 文件中提取参考模型特征和表面特征。
支持增量模式（--model-name 单独提取某个生成器）。

输入: data/{model_name}/generations*.jsonl 或 data/generations.jsonl (MVP pythia-2.8b)
输出: data/features_all.csv (model_name, seed_id, depth, [features...])
依赖: torch, transformers, numpy, pandas
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

MODEL_SNAPSHOT = "/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f"

# plan-002 生成器列表
ALL_GENERATORS = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-1.7b", "qwen3-0.6b", "qwen3-8b"]


def discover_data(project_root: Path, model_name: str) -> list[Path]:
    """找到指定生成器的所有 jsonl 数据文件。"""
    if model_name == "pythia-2.8b":
        # MVP 数据在根 data/ 目录
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

    found = [p for p in candidates if p.exists() and p.stat().st_size > 0]
    return found


def load_records(paths: list[Path], model_name: str) -> list[dict]:
    """从多个 jsonl 文件加载记录，统一添加 model_name 字段。"""
    records = []
    seen_ids = set()
    for p in paths:
        with open(p) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                # 去重（shard 间可能有 merged 文件）
                key = (rec.get("seed_id"), rec.get("depth"))
                if key in seen_ids:
                    continue
                seen_ids.add(key)
                rec["model_name"] = rec.get("model", model_name)
                records.append(rec)
    return records


def load_model(device: str):
    """加载 Pythia-410M 参考模型。"""
    print(f"Loading reference model from {MODEL_SNAPSHOT} on {device}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_SNAPSHOT, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_SNAPSHOT, local_files_only=True, torch_dtype=torch.float16,
    ).to(device).eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    print("Reference model loaded")
    return tokenizer, model


def compute_reference_features(texts: list[str], tokenizer, model, device: str, batch_size: int) -> list[dict]:
    """计算参考模型特征：entropy stats + tail_decay。"""
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

            # tail decay: avg log-prob 在 rank 100-1000 的斜率
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
    """计算表面特征：type-token ratio, hapax ratio。"""
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
    """提取单个生成器的全部特征，返回 DataFrame。"""
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
    parser = argparse.ArgumentParser(description="Multi-generator feature extraction for plan-002")
    parser.add_argument("--model-name", type=str, default=None,
                        help="Extract features for a single generator (incremental mode)")
    parser.add_argument("--output", default="data/features_all.csv", help="Output CSV path")
    parser.add_argument("--batch-size", type=int, default=8, help="GPU batch size")
    parser.add_argument("--device", default="cuda:0", help="CUDA device")
    parser.add_argument("--dry-run", action="store_true", help="Process only 2 seeds per model")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent
    output_path = project_root / args.output

    models_to_process = [args.model_name] if args.model_name else ALL_GENERATORS

    tokenizer, model = load_model(args.device)

    all_dfs = []
    for m in models_to_process:
        print(f"\n=== Processing: {m} ===")
        df = extract_one_model(m, project_root, tokenizer, model, args.device, args.batch_size)
        if not df.empty:
            if args.dry_run:
                # 只保留前 2 个 seed
                df = df[df["seed_id"] < 2]
            all_dfs.append(df)
            print(f"  -> {len(df)} rows")

    del model, tokenizer
    torch.cuda.empty_cache()

    if not all_dfs:
        print("No data extracted")
        sys.exit(1)

    new_df = pd.concat(all_dfs, ignore_index=True)

    # 增量模式：合并已有数据
    if args.model_name and output_path.exists():
        existing = pd.read_csv(output_path)
        # 去掉旧的同名模型数据
        existing = existing[existing["model_name"] != args.model_name]
        combined = pd.concat([existing, new_df], ignore_index=True)
    else:
        combined = new_df

    output_path.parent.mkdir(parents=True, exist_ok=True)
    combined.to_csv(output_path, index=False)

    print(f"\nFeatures saved to {output_path}")
    print(f"Shape: {combined.shape}")
    print(f"Models: {combined['model_name'].value_counts().to_dict()}")


if __name__ == "__main__":
    main()

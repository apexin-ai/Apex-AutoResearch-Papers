"""
Signal 1: Embedding-based near-duplicate retrieval.

Encodes benchmark items and SFT training data with sentence-transformers,
builds a FAISS index, and computes max cosine similarity between each
benchmark item and the top-K nearest training segments.

Input:  Benchmark dataset, SFT training data (JSONL from exp-001)
Output: JSON with per-item max cosine similarity scores
"""

import argparse
import json
import logging
import os
from pathlib import Path

import gc

import numpy as np
import torch
from tqdm import tqdm

logger = logging.getLogger(__name__)

HF_HOME = os.environ.get("HF_HOME", "/root/autodl-tmp/.hf_cache")
os.environ["HF_HOME"] = HF_HOME

DEFAULT_ENCODER = "sentence-transformers/all-mpnet-base-v2"
DEFAULT_TOP_K = 10


def load_sft_texts(data_path: str) -> list[str]:
    """Extract text content from SFT JSONL training data."""
    texts = []
    with open(data_path) as f:
        for line in f:
            row = json.loads(line)
            messages = row.get("messages", [])
            if isinstance(messages, str):
                messages = json.loads(messages)
            parts = []
            for msg in messages:
                if msg.get("role") in ("user", "assistant"):
                    parts.append(msg["content"])
            if parts:
                texts.append(" ".join(parts))
    return texts


def load_benchmark_texts(benchmark: str, cache_dir: str) -> list[dict]:
    """Load benchmark items as text strings with item metadata."""
    from datasets import load_dataset

    items = []
    if benchmark == "mmlu":
        ds = load_dataset("cais/mmlu", "all", split="test", cache_dir=cache_dir)
        for i, row in enumerate(ds):
            choices = " ".join(f"({chr(65+j)}) {c}" for j, c in enumerate(row["choices"]))
            text = f"{row['question']} {choices}"
            items.append({"index": i, "text": text, "benchmark": benchmark})
    elif benchmark == "gsm8k":
        ds = load_dataset("openai/gsm8k", "main", split="test", cache_dir=cache_dir)
        for i, row in enumerate(ds):
            items.append({"index": i, "text": row["question"], "benchmark": benchmark})
    elif benchmark == "arc_challenge":
        ds = load_dataset("allenai/ai2_arc", "ARC-Challenge", split="test", cache_dir=cache_dir)
        for i, row in enumerate(ds):
            choices = " ".join(f"({l}) {t}" for l, t in zip(row["choices"]["label"], row["choices"]["text"]))
            text = f"{row['question']} {choices}"
            items.append({"index": i, "text": text, "benchmark": benchmark})
    elif benchmark == "humaneval":
        ds = load_dataset("openai/openai_humaneval", "openai_humaneval", split="test", cache_dir=cache_dir)
        for i, row in enumerate(ds):
            items.append({"index": i, "text": row["prompt"], "benchmark": benchmark})
    else:
        raise ValueError(f"Unknown benchmark: {benchmark}")
    return items


def encode_texts(texts: list[str], encoder_name: str, cache_dir: str,
                 batch_size: int = 64, device: str = "cuda") -> np.ndarray:
    """Encode texts into normalized embeddings."""
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(encoder_name, cache_folder=cache_dir, device=device)
    embeddings = model.encode(
        texts, batch_size=batch_size, show_progress_bar=True,
        normalize_embeddings=True, convert_to_numpy=True,
    )
    return embeddings


def build_faiss_index(embeddings: np.ndarray, use_gpu: bool = True):
    """Build a FAISS index for cosine similarity search (on normalized vectors, IP = cosine)."""
    import faiss

    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    if use_gpu and faiss.get_num_gpus() > 0:
        res = faiss.StandardGpuResources()
        index = faiss.index_cpu_to_gpu(res, 0, index)
    index.add(embeddings.astype(np.float32))
    return index


def compute_embedding_signal(
    benchmark: str,
    sft_data_path: str,
    cache_dir: str,
    encoder_name: str = DEFAULT_ENCODER,
    top_k: int = DEFAULT_TOP_K,
    batch_size: int = 64,
    device: str = "cuda",
) -> list[dict]:
    """Compute per-item max cosine similarity with training data."""
    logger.info("Loading SFT training data from %s", sft_data_path)
    train_texts = load_sft_texts(sft_data_path)
    logger.info("Training segments: %d", len(train_texts))

    logger.info("Loading benchmark items: %s", benchmark)
    bench_items = load_benchmark_texts(benchmark, cache_dir)
    logger.info("Benchmark items: %d", len(bench_items))

    logger.info("Encoding training data with %s", encoder_name)
    train_embeddings = encode_texts(train_texts, encoder_name, cache_dir, batch_size, device)

    logger.info("Encoding benchmark items")
    bench_texts = [item["text"] for item in bench_items]
    bench_embeddings = encode_texts(bench_texts, encoder_name, cache_dir, batch_size, device)

    logger.info("Building FAISS index (%d vectors, dim=%d)", len(train_embeddings), train_embeddings.shape[1])
    try:
        index = build_faiss_index(train_embeddings, use_gpu=True)
    except Exception:
        logger.warning("FAISS GPU failed, falling back to CPU")
        index = build_faiss_index(train_embeddings, use_gpu=False)

    logger.info("Searching top-%d nearest neighbors", top_k)
    scores, indices = index.search(bench_embeddings.astype(np.float32), top_k)

    del index, train_embeddings, bench_embeddings
    gc.collect()
    torch.cuda.empty_cache()
    logger.info("Freed embedding model and FAISS index GPU memory")

    results = []
    for i, item in enumerate(bench_items):
        max_sim = float(scores[i, 0])  # already sorted descending
        mean_sim = float(np.mean(scores[i]))
        results.append({
            "index": item["index"],
            "benchmark": item["benchmark"],
            "s1_embedding": max_sim,
            "s1_embedding_mean_topk": mean_sim,
            "s1_top_k_sims": [float(s) for s in scores[i]],
        })

    return results


def main():
    parser = argparse.ArgumentParser(description="Signal 1: Embedding near-duplicate retrieval")
    parser.add_argument("--benchmark", type=str, required=True,
                        choices=["mmlu", "gsm8k", "arc_challenge", "humaneval"])
    parser.add_argument("--sft-data-path", type=str, required=True,
                        help="Path to SFT training JSONL (from exp-001 prepare_sft_data.py)")
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--encoder", type=str, default=DEFAULT_ENCODER,
                        help="Sentence-transformers model name")
    parser.add_argument("--top-k", type=int, default=DEFAULT_TOP_K)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--gpu", type=str, default=None,
                        help="GPU device ID (e.g., '0')")
    parser.add_argument("--cache-dir", type=str, default="/root/autodl-tmp/.hf_cache")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    if args.gpu:
        os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu

    device = "cuda" if torch.cuda.is_available() else "cpu"
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    results = compute_embedding_signal(
        benchmark=args.benchmark,
        sft_data_path=args.sft_data_path,
        cache_dir=args.cache_dir,
        encoder_name=args.encoder,
        top_k=args.top_k,
        batch_size=args.batch_size,
        device=device,
    )

    out_file = output_dir / f"signal_embedding_{args.benchmark}.json"
    with open(out_file, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Saved %d items to %s", len(results), out_file)


if __name__ == "__main__":
    main()

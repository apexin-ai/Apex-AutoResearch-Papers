import logging
import os

import numpy as np
import torch

logger = logging.getLogger(__name__)

DEFAULT_ENCODER = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_SFT_DATA_DIR = "/root/autodl-tmp/exp001/sft_data"
DEFAULT_TOP_K = 10


def _encode_texts(texts: list[str], encoder_name: str, cache_dir: str,
                  batch_size: int = 64, device: str = "cuda") -> np.ndarray:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(encoder_name, cache_folder=cache_dir, device=device)
    embeddings = model.encode(
        texts, batch_size=batch_size, show_progress_bar=True,
        normalize_embeddings=True, convert_to_numpy=True,
    )
    return embeddings


def _build_faiss_index(embeddings: np.ndarray, use_gpu: bool = True):
    import faiss
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    if use_gpu and faiss.get_num_gpus() > 0:
        res = faiss.StandardGpuResources()
        index = faiss.index_cpu_to_gpu(res, 0, index)
    index.add(embeddings.astype(np.float32))
    return index


def compute(
    benchmark: str,
    model_path: str = None,
    adapter_path: str = None,
    output_dir: str = None,
    cache_dir: str = None,
    batch_size: int = 64,
    sft_data_dir: str = None,
    **kwargs,
) -> list[dict]:
    from utils import (
        load_benchmark_dataset, format_question_text,
        make_item_id, load_sft_texts, infer_dosage_from_path,
    )

    sft_data_dir = sft_data_dir or DEFAULT_SFT_DATA_DIR
    cache_dir = cache_dir or "/root/autodl-tmp/.hf_cache"

    dosage = infer_dosage_from_path(adapter_path) if adapter_path else "000"
    sft_data_path = os.path.join(sft_data_dir, f"sft_dosage_{dosage}.jsonl")
    if not os.path.exists(sft_data_path):
        sft_data_path = os.path.join(sft_data_dir, "sft_dosage_000.jsonl")
    logger.info("Loading SFT training data from %s", sft_data_path)
    train_texts = load_sft_texts(sft_data_path)
    logger.info("Training segments: %d", len(train_texts))

    logger.info("Loading benchmark items: %s", benchmark)
    ds = load_benchmark_dataset(benchmark, cache_dir)
    bench_texts = [format_question_text(row, benchmark) for row in ds]
    logger.info("Benchmark items: %d", len(bench_texts))

    device = "cuda" if torch.cuda.is_available() else "cpu"

    logger.info("Encoding training data with %s", DEFAULT_ENCODER)
    train_embeddings = _encode_texts(train_texts, DEFAULT_ENCODER, cache_dir, batch_size, device)

    logger.info("Encoding benchmark items")
    bench_embeddings = _encode_texts(bench_texts, DEFAULT_ENCODER, cache_dir, batch_size, device)

    logger.info("Building FAISS index (%d vectors, dim=%d)", len(train_embeddings), train_embeddings.shape[1])
    try:
        index = _build_faiss_index(train_embeddings, use_gpu=True)
    except Exception:
        logger.warning("FAISS GPU failed, falling back to CPU")
        index = _build_faiss_index(train_embeddings, use_gpu=False)

    logger.info("Searching top-%d nearest neighbors", DEFAULT_TOP_K)
    scores, indices = index.search(bench_embeddings.astype(np.float32), DEFAULT_TOP_K)

    results = []
    for i in range(len(ds)):
        max_sim = float(scores[i, 0])
        mean_sim = float(np.mean(scores[i]))
        results.append({
            "item_id": make_item_id(benchmark, i),
            "signal": "s1_embedding",
            "score": max_sim,
            "metadata": {
                "mean_topk_sim": mean_sim,
                "top_k_sims": [float(s) for s in scores[i]],
                "sft_data_path": sft_data_path,
            },
        })

    return results

"""
exp-008: Compute 4 contamination detection signals on any model.

Wraps exp-002 signal modules (embedding, minkpp, selfcritique) to compute
signals on arbitrary models (base pretrained, SFT adapters, Instruct/RL models).
ConStat (S3) is skipped for models without eval results — it requires
pre-computed per-item correctness from original vs paraphrased benchmarks.

Usage:
  # Compute on Instruct model
  python compute_signals_on_model.py \
    --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct \
    --ref-model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B \
    --sft-data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl \
    --benchmarks mmlu gsm8k arc_challenge \
    --output-dir /root/autodl-tmp/exp008/signals/rl_aligned \
    --gpu 0

  # Compute on base pretrained
  python compute_signals_on_model.py \
    --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B \
    --ref-model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B \
    --sft-data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl \
    --benchmarks mmlu gsm8k arc_challenge \
    --output-dir /root/autodl-tmp/exp008/signals/base \
    --gpu 0

Dependencies: torch, transformers, peft, sentence-transformers, datasets, faiss-cpu, numpy, tqdm
"""

import argparse
import json
import logging
import os
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

EXP002_DIR = str(Path(__file__).resolve().parent.parent / "exp002")
HF_HOME = os.environ.get("HF_HOME", "/root/autodl-tmp/.hf_cache")
os.environ["HF_HOME"] = HF_HOME

SIGNALS = ["embedding", "minkpp", "selfcritique"]


def setup_exp002_imports():
    """Add exp-002 directory to sys.path for signal module imports."""
    if EXP002_DIR not in sys.path:
        sys.path.insert(0, EXP002_DIR)


def compute_all_signals(
    model_path: str,
    ref_model_path: str,
    sft_data_path: str,
    benchmark: str,
    output_dir: Path,
    signals: list[str],
    device: str = "cuda",
    batch_size: int = 64,
    k_percent: int = 20,
    cache_dir: str = HF_HOME,
):
    """Compute requested signals for one benchmark and save results."""
    setup_exp002_imports()
    output_dir.mkdir(parents=True, exist_ok=True)

    results = {}

    # S1: Embedding near-duplicate retrieval
    if "embedding" in signals:
        cached = _load_cached(output_dir, "embedding", benchmark)
        if cached is not None:
            results["embedding"] = cached
        else:
            logger.info("=== S1: Embedding retrieval [%s] ===", benchmark)
            from signal_embedding import compute_embedding_signal
            results["embedding"] = compute_embedding_signal(
                benchmark=benchmark,
                sft_data_path=sft_data_path,
                cache_dir=cache_dir,
                batch_size=batch_size,
                device=device,
            )
            _save_signal(results["embedding"], output_dir, "embedding", benchmark)

    # S2: Min-K%++
    if "minkpp" in signals:
        cached = _load_cached(output_dir, "minkpp", benchmark)
        if cached is not None:
            results["minkpp"] = cached
        else:
            logger.info("=== S2: Min-K%%++ [%s] ===", benchmark)
            from signal_minkpp import compute_minkpp_signal
            results["minkpp"] = compute_minkpp_signal(
                benchmark=benchmark,
                target_model_path=model_path,
                ref_model_path=ref_model_path,
                cache_dir=cache_dir,
                k_percent=k_percent,
            )
            _save_signal(results["minkpp"], output_dir, "minkpp", benchmark)

    # S4: Self-Critique entropy
    if "selfcritique" in signals:
        cached = _load_cached(output_dir, "selfcritique", benchmark)
        if cached is not None:
            results["selfcritique"] = cached
        else:
            logger.info("=== S4: Self-Critique entropy [%s] ===", benchmark)
            from signal_selfcritique import compute_selfcritique_signal
            results["selfcritique"] = compute_selfcritique_signal(
                benchmark=benchmark,
                model_path=model_path,
                cache_dir=cache_dir,
            )
            _save_signal(results["selfcritique"], output_dir, "selfcritique", benchmark)

    # Merge
    if len(results) >= 2:
        logger.info("Merging %d signals for %s", len(results), benchmark)
        merged = _merge_signals(results, benchmark)
        merged_path = output_dir / f"signals_merged_{benchmark}.json"
        with open(merged_path, "w") as f:
            json.dump(merged, f, indent=2)
        logger.info("Merged %d items -> %s", len(merged), merged_path)

    return results


def _merge_signals(results: dict, benchmark: str) -> list[dict]:
    """Merge multiple signal outputs into per-item records."""
    sig_key_map = {
        "embedding": "s1_embedding",
        "minkpp": "s2_minkpp",
        "constat": "s3_constat",
        "selfcritique": "s4_selfcritique",
    }

    by_index: dict[int, dict] = {}
    for sig_name, records in results.items():
        out_key = sig_key_map.get(sig_name, sig_name)
        for r in records:
            idx = r["index"]
            if idx not in by_index:
                by_index[idx] = {"index": idx, "benchmark": benchmark}
            by_index[idx][out_key] = r.get(out_key) or r.get(f"s{list(sig_key_map.keys()).index(sig_name)+1}_{sig_name}")

    # Fill missing signals with None
    all_keys = {sig_key_map[k] for k in results}
    for idx_data in by_index.values():
        for k in ["s1_embedding", "s2_minkpp", "s3_constat", "s4_selfcritique"]:
            if k not in idx_data:
                idx_data[k] = None

    return sorted(by_index.values(), key=lambda r: r["index"])


def _load_cached(output_dir: Path, signal_name: str, benchmark: str):
    path = output_dir / f"signal_{signal_name}_{benchmark}.json"
    if path.exists():
        with open(path) as f:
            data = json.load(f)
        logger.info("Loaded cached %s from %s (%d items)", signal_name, path, len(data))
        return data
    return None


def _save_signal(results: list[dict], output_dir: Path, signal_name: str, benchmark: str):
    path = output_dir / f"signal_{signal_name}_{benchmark}.json"
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Saved %d items -> %s", len(results), path)


def main():
    parser = argparse.ArgumentParser(
        description="exp-008: Compute contamination detection signals on any model"
    )
    parser.add_argument("--model-path", type=str, required=True,
                        help="Target model path (HF ID or local path, supports LoRA adapters)")
    parser.add_argument("--ref-model-path", type=str, required=True,
                        help="Reference model for Min-K%++ normalization")
    parser.add_argument("--sft-data-path", type=str, required=True,
                        help="SFT training data JSONL for embedding signal")
    parser.add_argument("--benchmarks", type=str, nargs="+",
                        default=["mmlu", "gsm8k", "arc_challenge"],
                        choices=["mmlu", "gsm8k", "arc_challenge", "humaneval"])
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--signals", type=str, nargs="+", default=SIGNALS,
                        choices=SIGNALS)
    parser.add_argument("--gpu", type=str, default=None)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--k-percent", type=int, default=20)
    parser.add_argument("--cache-dir", type=str, default=HF_HOME)
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    if args.gpu is not None:
        os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu
        device = "cuda"
    else:
        import torch
        device = "cuda" if torch.cuda.is_available() else "cpu"

    output_base = Path(args.output_dir)

    logger.info("Model: %s", args.model_path)
    logger.info("Ref model: %s", args.ref_model_path)
    logger.info("Benchmarks: %s", args.benchmarks)
    logger.info("Signals: %s", args.signals)
    logger.info("Output: %s", output_base)

    for benchmark in args.benchmarks:
        bench_output = output_base / benchmark
        logger.info("--- %s ---", benchmark)
        compute_all_signals(
            model_path=args.model_path,
            ref_model_path=args.ref_model_path,
            sft_data_path=args.sft_data_path,
            benchmark=benchmark,
            output_dir=bench_output,
            signals=args.signals,
            device=device,
            batch_size=args.batch_size,
            k_percent=args.k_percent,
            cache_dir=args.cache_dir,
        )

    logger.info("All signals computed. Output: %s", output_base)


if __name__ == "__main__":
    main()

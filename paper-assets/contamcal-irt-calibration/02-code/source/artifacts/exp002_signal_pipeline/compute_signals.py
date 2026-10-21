"""
exp-002 Stage 1 Signal Pipeline — main entry point.

Computes 4 contamination detection signals for each model-item pair:
  S1: Embedding near-duplicate retrieval (max cosine sim with training data)
  S2: Min-K%++ membership inference (z-scored against reference model)
  S3: ConStat performance gap (original vs paraphrased accuracy)
  S4: Self-Critique entropy collapse (YES/NO confidence on own answer)

Input:  Model checkpoint, benchmark data, paraphrased items, SFT training data
Output: JSON per model with item_id, s1_embedding, s2_minkpp, s3_constat, s4_selfcritique
"""

import argparse
import json
import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)


def merge_signals(
    embedding_results: list[dict],
    minkpp_results: list[dict],
    constat_results: list[dict],
    selfcritique_results: list[dict],
    benchmark: str,
) -> list[dict]:
    """Merge 4 signal outputs into a single per-item record."""
    # Index by item index
    emb_map = {r["index"]: r for r in embedding_results}
    mkpp_map = {r["index"]: r for r in minkpp_results}
    con_map = {r["index"]: r for r in constat_results}
    sc_map = {r["index"]: r for r in selfcritique_results}

    all_indices = sorted(set(emb_map) | set(mkpp_map) | set(con_map) | set(sc_map))

    merged = []
    for idx in all_indices:
        record = {
            "index": idx,
            "benchmark": benchmark,
            "s1_embedding": emb_map.get(idx, {}).get("s1_embedding"),
            "s2_minkpp": mkpp_map.get(idx, {}).get("s2_minkpp"),
            "s3_constat": con_map.get(idx, {}).get("s3_constat"),
            "s4_selfcritique": sc_map.get(idx, {}).get("s4_selfcritique"),
        }
        merged.append(record)

    return merged


def run_signal(signal_name: str, args_dict: dict):
    """Run a signal computation module."""
    if signal_name == "embedding":
        from signal_embedding import compute_embedding_signal
        return compute_embedding_signal(**args_dict)
    elif signal_name == "minkpp":
        from signal_minkpp import compute_minkpp_signal
        return compute_minkpp_signal(**args_dict)
    elif signal_name == "constat":
        from signal_constat import compute_constat_signal
        return compute_constat_signal(**args_dict)
    elif signal_name == "selfcritique":
        from signal_selfcritique import compute_selfcritique_signal
        return compute_selfcritique_signal(**args_dict)
    else:
        raise ValueError(f"Unknown signal: {signal_name}")


def main():
    parser = argparse.ArgumentParser(
        description="Compute all 4 contamination detection signals for a model-benchmark pair"
    )
    parser.add_argument("--model-path", type=str, required=True,
                        help="Path to target (potentially contaminated) model checkpoint")
    parser.add_argument("--benchmark", type=str, required=True,
                        choices=["mmlu", "gsm8k", "arc_challenge", "humaneval"])
    parser.add_argument("--ref-model-path", type=str, required=True,
                        help="Reference (clean) model for Min-K%%++ (e.g., 0%%%% dosage)")
    parser.add_argument("--sft-data-path", type=str, required=True,
                        help="SFT training JSONL for embedding retrieval")
    parser.add_argument("--original-eval-paths", type=str, nargs="+", default=None,
                        help="eval_results.json paths for original items (one per seed)")
    parser.add_argument("--paraphrase-eval-paths", type=str, nargs="+", default=None,
                        help="eval_results.json paths for paraphrased items (one per seed)")
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--gpu", type=str, default=None)
    parser.add_argument("--batch-size", type=int, default=64,
                        help="Batch size for embedding encoding")
    parser.add_argument("--k-percent", type=int, default=20,
                        help="K%%%% for Min-K%%%% selection")
    parser.add_argument("--signals", type=str, nargs="+",
                        default=["embedding", "minkpp", "constat", "selfcritique"],
                        choices=["embedding", "minkpp", "constat", "selfcritique"],
                        help="Which signals to compute")
    parser.add_argument("--cache-dir", type=str, default="/root/autodl-tmp/.hf_cache")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    if args.gpu:
        os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu

    import torch
    device = "cuda" if torch.cuda.is_available() else "cpu"

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    signal_results = {}

    # Signal 1: Embedding
    if "embedding" in args.signals:
        logger.info("=== Signal 1: Embedding near-duplicate retrieval ===")
        signal_results["embedding"] = run_signal("embedding", {
            "benchmark": args.benchmark,
            "sft_data_path": args.sft_data_path,
            "cache_dir": args.cache_dir,
            "batch_size": args.batch_size,
            "device": device,
        })
        _save_signal(signal_results["embedding"], output_dir, "embedding", args.benchmark)

    # Signal 2: Min-K%++
    if "minkpp" in args.signals:
        logger.info("=== Signal 2: Min-K%%++ membership inference ===")
        signal_results["minkpp"] = run_signal("minkpp", {
            "benchmark": args.benchmark,
            "target_model_path": args.model_path,
            "ref_model_path": args.ref_model_path,
            "cache_dir": args.cache_dir,
            "k_percent": args.k_percent,
        })
        _save_signal(signal_results["minkpp"], output_dir, "minkpp", args.benchmark)

    # Signal 3: ConStat
    if "constat" in args.signals:
        if args.original_eval_paths and args.paraphrase_eval_paths:
            logger.info("=== Signal 3: ConStat performance gap ===")
            signal_results["constat"] = run_signal("constat", {
                "benchmark": args.benchmark,
                "original_eval_paths": args.original_eval_paths,
                "paraphrase_eval_paths": args.paraphrase_eval_paths,
            })
            _save_signal(signal_results["constat"], output_dir, "constat", args.benchmark)
        else:
            logger.warning("Skipping ConStat: --original-eval-paths and --paraphrase-eval-paths required")

    # Signal 4: Self-Critique
    if "selfcritique" in args.signals:
        logger.info("=== Signal 4: Self-Critique entropy collapse ===")
        signal_results["selfcritique"] = run_signal("selfcritique", {
            "benchmark": args.benchmark,
            "model_path": args.model_path,
            "cache_dir": args.cache_dir,
        })
        _save_signal(signal_results["selfcritique"], output_dir, "selfcritique", args.benchmark)

    # Merge all computed signals (graceful: merge whenever ≥2 signals available)
    if len(signal_results) >= 2:
        logger.info("=== Merging all signals ===")
        merged = merge_signals(
            signal_results.get("embedding", []),
            signal_results.get("minkpp", []),
            signal_results.get("constat", []),
            signal_results.get("selfcritique", []),
            args.benchmark,
        )
        merged_file = output_dir / f"signals_merged_{args.benchmark}.json"
        with open(merged_file, "w") as f:
            json.dump(merged, f, indent=2)
        logger.info("Merged signals saved to %s (%d items)", merged_file, len(merged))
    else:
        logger.info("Computed %d/4 signals. Need at least 2 for merged output.", len(signal_results))

    (output_dir / ".done").touch()
    logger.info("Sentinel .done written to %s", output_dir)


def _save_signal(results: list[dict], output_dir: Path, signal_name: str, benchmark: str):
    out_file = output_dir / f"signal_{signal_name}_{benchmark}.json"
    with open(out_file, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Saved %d items to %s", len(results), out_file)


if __name__ == "__main__":
    main()

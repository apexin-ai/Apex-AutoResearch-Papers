import argparse
import gc
import json
import logging
import os
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

sys.path.insert(0, str(Path(__file__).resolve().parent))


def main():
    parser = argparse.ArgumentParser(
        description="Compute contamination detection signals for model-benchmark pairs"
    )
    parser.add_argument("--model-path", type=str, required=True,
                        help="Base model path (e.g., /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B)")
    parser.add_argument("--adapter-path", type=str, default=None,
                        help="LoRA adapter path (optional, for SFT models)")
    parser.add_argument("--benchmark", type=str, required=True,
                        choices=["mmlu", "gsm8k", "arc_challenge", "humaneval"])
    parser.add_argument("--signal", type=str, required=True,
                        choices=["s1", "s2", "s3", "s4", "all"],
                        help="Which signal to compute (s1/s2/s3/s4/all)")
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--cache-dir", type=str, default="/root/autodl-tmp/.hf_cache")
    parser.add_argument("--batch-size", type=int, default=8)

    parser.add_argument("--sft-data-dir", type=str, default="/root/autodl-tmp/exp001/sft_data",
                        help="SFT training data directory (for S1)")
    parser.add_argument("--ref-model-path", type=str, default=None,
                        help="Reference model path for S2 Min-K%%++ (auto-inferred if not set)")
    parser.add_argument("--k-percent", type=int, default=20,
                        help="K%% for Min-K%% selection (S2, default: 20)")
    parser.add_argument("--original-eval-paths", type=str, nargs="+", default=None,
                        help="eval_results.json paths for original items (S3, one per seed)")
    parser.add_argument("--paraphrase-eval-paths", type=str, nargs="+", default=None,
                        help="eval_results.json paths for paraphrased items (S3, one per seed)")

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    os.environ["HF_HOME"] = args.cache_dir

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    signals_to_run = ["s1", "s2", "s3", "s4"] if args.signal == "all" else [args.signal]

    common_kwargs = {
        "benchmark": args.benchmark,
        "model_path": args.model_path,
        "adapter_path": args.adapter_path,
        "output_dir": args.output_dir,
        "cache_dir": args.cache_dir,
        "batch_size": args.batch_size,
    }

    from signals import SIGNAL_MAP

    all_results = {}
    for sig in signals_to_run:
        logger.info("=== Computing signal: %s ===", sig)

        sig_kwargs = dict(common_kwargs)
        if sig == "s1":
            sig_kwargs["sft_data_dir"] = args.sft_data_dir
        elif sig == "s2":
            sig_kwargs["ref_model_path"] = args.ref_model_path
            sig_kwargs["k_percent"] = args.k_percent
        elif sig == "s3":
            sig_kwargs["original_eval_paths"] = args.original_eval_paths
            sig_kwargs["paraphrase_eval_paths"] = args.paraphrase_eval_paths

        compute_fn = SIGNAL_MAP[sig]
        results = compute_fn(**sig_kwargs)

        if results:
            from utils import save_signal_results
            sig_name = {
                "s1": "s1_embedding",
                "s2": "s2_minkpp",
                "s3": "s3_constat",
                "s4": "s4_selfcritique",
            }[sig]
            save_signal_results(results, args.output_dir, sig_name, args.benchmark)
            all_results[sig] = results
            logger.info("Signal %s: %d items computed", sig, len(results))
        else:
            logger.warning("Signal %s: no results (check required inputs)", sig)

        gc.collect()
        try:
            import torch
            torch.cuda.empty_cache()
            logger.info("Memory cleaned after signal: %s", sig)
        except ImportError:
            pass

    if len(all_results) >= 2:
        merged = _merge_signals(all_results, args.benchmark)
        merged_file = output_dir / f"signals_merged_{args.benchmark}.json"
        with open(merged_file, "w") as f:
            json.dump(merged, f, indent=2)
        logger.info("Merged %d signals -> %s (%d items)", len(all_results), merged_file, len(merged))

    logger.info("Done. Results in %s", output_dir)


def _merge_signals(all_results: dict, benchmark: str) -> list[dict]:
    by_item = {}
    for sig, results in all_results.items():
        for r in results:
            item_id = r["item_id"]
            if item_id not in by_item:
                by_item[item_id] = {"item_id": item_id, "benchmark": benchmark}
            by_item[item_id][r["signal"]] = r["score"]

    return sorted(by_item.values(), key=lambda x: x["item_id"])


if __name__ == "__main__":
    main()

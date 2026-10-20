"""Phase 1: 3-generation filtered comparison across 5 conditions.

Usage:
  python run_phase1.py --condition no_filter --gpu 0 --output_dir outputs/phase1
  python run_phase1.py --condition all --gpu 0 --output_dir outputs/phase1  # run all sequentially
  python run_phase1.py --condition pgpf_s --gpu 0 &  # parallel: GPU 0
  python run_phase1.py --condition random --gpu 1 &   # parallel: GPU 1

GPU parallelism notes:
  - Training + generation: 1 GPU sufficient for 1.5B model (~3GB bf16)
  - Scoring: needs ft model + base model on same GPU; 96GB RTX PRO 6000 can hold both
  - Two conditions can run in parallel on different GPUs (--gpu 0 / --gpu 1)
  - Each condition occupies 1 GPU exclusively via CUDA_VISIBLE_DEVICES
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

from pgpf.config import PGPFConfig
from pgpf.recursive_loop import RecursiveTrainingLoop
from pgpf.utils import save_json, logger


CONDITIONS = {
    "no_filter":    {"filter_method": "no_filter",     "retention_rate": 1.0, "seed": 42},
    "random":       {"filter_method": "random",        "retention_rate": 0.5, "seed": 43},
    "confidence":   {"filter_method": "confidence",    "retention_rate": 0.5, "seed": 44},
    "pgpf_s":       {"filter_method": "pgpf_static",   "retention_rate": 0.5, "seed": 45},
    "lexical_only": {"filter_method": "lexical_only",  "retention_rate": 0.5, "seed": 46},
}


def make_config(condition_name: str, output_dir: str, data_dir: str) -> PGPFConfig:
    params = CONDITIONS[condition_name]
    return PGPFConfig(
        filter_method=params["filter_method"],
        retention_rate=params["retention_rate"],
        seed=params["seed"],
        num_generations=3,
        real_data_mix_ratio=0.5,
        output_dir=str(Path(output_dir) / condition_name),
        data_dir=data_dir,
    )


def collect_summary(output_dir: str, condition_name: str) -> dict:
    """Read per-generation metrics and produce a condition summary."""
    cond_dir = Path(output_dir) / condition_name
    summary = {"condition": condition_name, "generations": []}

    for gen in range(3):
        metrics_path = cond_dir / f"gen_{gen}" / "metrics.json"
        if metrics_path.exists():
            with open(metrics_path) as f:
                m = json.load(f)
            summary["generations"].append({
                "generation": gen,
                "held_out_ppl": m.get("held_out_ppl"),
                "self_bleu": m.get("self_bleu"),
                "vocab_coverage": m.get("vocab_coverage"),
                "embedding_diversity": m.get("embedding_diversity"),
                "num_filtered": m.get("num_filtered"),
                "elapsed_seconds": m.get("elapsed_seconds"),
            })

    # degradation = ppl_gen2 / ppl_gen0 - 1 (gen indices 0,1,2 = 3 generations)
    ppls = [g["held_out_ppl"] for g in summary["generations"] if g.get("held_out_ppl") is not None]
    if len(ppls) >= 2:
        summary["degradation"] = ppls[-1] / ppls[0] - 1.0

    return summary


def build_comparison(output_dir: str, conditions: list[str]) -> dict:
    """Cross-condition comparison."""
    comparison = {"conditions": {}}
    for cond in conditions:
        summary_path = Path(output_dir) / cond / "summary.json"
        if summary_path.exists():
            with open(summary_path) as f:
                s = json.load(f)
            comparison["conditions"][cond] = {
                "degradation": s.get("degradation"),
                "final_ppl": s["generations"][-1]["held_out_ppl"] if s.get("generations") else None,
                "final_self_bleu": s["generations"][-1]["self_bleu"] if s.get("generations") else None,
                "final_vocab_coverage": s["generations"][-1]["vocab_coverage"] if s.get("generations") else None,
                "final_embedding_diversity": s["generations"][-1]["embedding_diversity"] if s.get("generations") else None,
            }
    return comparison


def run_condition(condition_name: str, gpu: int, output_dir: str, data_dir: str) -> None:
    os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu)
    logger.info(f"=== Running condition: {condition_name} on GPU {gpu} ===")

    config = make_config(condition_name, output_dir, data_dir)
    start = time.time()
    loop = RecursiveTrainingLoop(config)
    loop.run()
    elapsed = time.time() - start

    summary = collect_summary(output_dir, condition_name)
    summary["total_elapsed_seconds"] = elapsed
    summary_path = Path(output_dir) / condition_name / "summary.json"
    save_json(summary, summary_path)
    logger.info(f"Condition {condition_name} done in {elapsed:.0f}s, degradation={summary.get('degradation', 'N/A')}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--condition", type=str, required=True,
                        choices=list(CONDITIONS.keys()) + ["all"],
                        help="Which condition to run, or 'all' for sequential execution")
    parser.add_argument("--gpu", type=int, default=0, help="GPU index (sets CUDA_VISIBLE_DEVICES)")
    parser.add_argument("--output_dir", type=str, default="outputs/phase1")
    parser.add_argument("--data_dir", type=str, default="data")
    args = parser.parse_args()

    if args.condition == "all":
        conditions_to_run = list(CONDITIONS.keys())
    else:
        conditions_to_run = [args.condition]

    for cond in conditions_to_run:
        run_condition(cond, args.gpu, args.output_dir, args.data_dir)

    # Generate cross-condition comparison if all 5 completed
    completed = [c for c in CONDITIONS if (Path(args.output_dir) / c / "summary.json").exists()]
    if len(completed) > 1:
        comparison = build_comparison(args.output_dir, completed)
        comp_path = Path(args.output_dir) / "comparison.json"
        save_json(comparison, comp_path)
        logger.info(f"Comparison saved to {comp_path}")


if __name__ == "__main__":
    main()

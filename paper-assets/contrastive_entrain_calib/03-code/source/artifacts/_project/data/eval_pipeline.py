#!/usr/bin/env python3
"""Unified evaluation pipeline for contrastive entrainment calibration.

Supports 4 benchmarks: SYCONBench, SycophancyEval, MTBench, MMLU.
Each benchmark is independently runnable; the pipeline orchestrates them.

Usage:
  python eval_pipeline.py --model-path <path> --benchmarks sycon,mmlu --output-dir results/
  python eval_pipeline.py --model-path <path> --dry-run
"""

import argparse
import json
import logging
import sys
import time
from abc import ABC, abstractmethod
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import torch
except ImportError:
    torch = None

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Base class
# ---------------------------------------------------------------------------

class BenchmarkBase(ABC):
    """Abstract base for all benchmark evaluators."""

    name: str = "base"

    def __init__(self, device: str = "cuda", **kwargs):
        self.device = device
        self.kwargs = kwargs

    @abstractmethod
    def load_data(self) -> list[dict]:
        ...

    @abstractmethod
    def run_inference(
        self, model: Any, tokenizer: Any, data: list[dict]
    ) -> list[dict]:
        ...

    @abstractmethod
    def compute_metrics(self, predictions: list[dict]) -> dict:
        ...

    def evaluate(self, model: Any, tokenizer: Any) -> dict:
        t0 = time.time()
        data = self.load_data()
        logger.info("[%s] Loaded %d samples", self.name, len(data))
        predictions = self.run_inference(model, tokenizer, data)
        metrics = self.compute_metrics(predictions)
        metrics["_meta"] = {
            "n_samples": len(data),
            "elapsed_sec": round(time.time() - t0, 2),
        }
        return metrics

    def dry_run(self) -> dict:
        data = self.load_data()
        logger.info("[%s] Dry-run OK — %d samples loaded", self.name, len(data))
        return {"n_samples": len(data), "status": "dry_run_ok"}


# ---------------------------------------------------------------------------
# Benchmark: SYCONBench (multi-turn sycophancy)
# ---------------------------------------------------------------------------

class SYCONBench(BenchmarkBase):
    """Multi-turn sycophancy benchmark measuring Turn-of-Flip and Number-of-Flip."""

    name = "sycon_bench"

    def __init__(self, max_turns: int = 10, **kwargs):
        super().__init__(**kwargs)
        self.max_turns = max_turns

    def load_data(self) -> list[dict]:
        # TODO: Load or generate SYCON test set.
        #   Expected format per sample:
        #   {
        #       "id": str,
        #       "topic": str,
        #       "initial_question": str,
        #       "correct_answer": str,
        #       "pressure_prompts": list[str],   # follow-up turns that push model to flip
        #       "difficulty": str,                # easy / medium / hard
        #   }
        raise NotImplementedError("SYCONBench.load_data not yet implemented")

    def run_inference(
        self, model: Any, tokenizer: Any, data: list[dict]
    ) -> list[dict]:
        # TODO: Multi-turn conversation loop.
        #   For each sample:
        #     1. Send initial_question, record model stance.
        #     2. For each pressure_prompt (up to max_turns):
        #        - Append user turn, generate model reply.
        #        - Detect whether model flipped stance.
        #        - Record turn index of first flip (ToF) and count total flips (NoF).
        #   Return list of:
        #   {
        #       "id": str,
        #       "tof": int | None,   # turn of first flip (None if never flipped)
        #       "nof": int,          # number of flips
        #       "difficulty": str,
        #       "turns": list[dict], # full conversation for debugging
        #   }
        raise NotImplementedError("SYCONBench.run_inference not yet implemented")

    def compute_metrics(self, predictions: list[dict]) -> dict:
        # TODO: Aggregate per-sample ToF/NoF into summary statistics.
        #   - tof_mean, tof_median (excluding samples that never flipped)
        #   - nof_mean
        #   - flip_rate (fraction of samples where at least one flip occurred)
        #   - by_difficulty: {easy: {...}, medium: {...}, hard: {...}}
        raise NotImplementedError("SYCONBench.compute_metrics not yet implemented")


# ---------------------------------------------------------------------------
# Benchmark: SycophancyEval (single-turn sycophancy)
# ---------------------------------------------------------------------------

class SycophancyEval(BenchmarkBase):
    """Single-turn sycophancy evaluation: does the model agree with wrong premises?"""

    name = "sycophancy_eval"

    def load_data(self) -> list[dict]:
        # TODO: Load from HuggingFace or local JSON.
        #   Expected format per sample:
        #   {
        #       "id": str,
        #       "question": str,
        #       "user_claim": str,        # incorrect claim by user
        #       "correct_answer": str,
        #       "category": str,           # e.g. math, facts, opinions
        #   }
        raise NotImplementedError("SycophancyEval.load_data not yet implemented")

    def run_inference(
        self, model: Any, tokenizer: Any, data: list[dict]
    ) -> list[dict]:
        # TODO: Single-turn generation.
        #   For each sample:
        #     1. Format prompt with user_claim embedded.
        #     2. Generate model response.
        #     3. Classify: did model agree with incorrect claim (sycophantic)
        #        or maintain correct answer (non-sycophantic)?
        #   Return list of:
        #   {
        #       "id": str,
        #       "sycophantic": bool,
        #       "model_response": str,
        #       "category": str,
        #   }
        raise NotImplementedError("SycophancyEval.run_inference not yet implemented")

    def compute_metrics(self, predictions: list[dict]) -> dict:
        # TODO: Compute:
        #   - sycophancy_rate: fraction of sycophantic responses
        #   - accuracy: fraction of correct (non-sycophantic) responses
        #   - by_category: {category: {sycophancy_rate, accuracy, n}}
        raise NotImplementedError("SycophancyEval.compute_metrics not yet implemented")


# ---------------------------------------------------------------------------
# Benchmark: MTBench (multi-turn dialogue quality)
# ---------------------------------------------------------------------------

class MTBench(BenchmarkBase):
    """MT-Bench: 80 two-turn questions scored by an LLM judge."""

    name = "mt_bench"

    def __init__(self, judge_model: str = "gpt-4", **kwargs):
        super().__init__(**kwargs)
        self.judge_model = judge_model

    def load_data(self) -> list[dict]:
        # TODO: Load MT-Bench question set (80 questions, 8 categories x 10).
        #   Expected format per sample:
        #   {
        #       "question_id": int,
        #       "category": str,
        #       "turns": [str, str],   # turn-1 and turn-2 prompts
        #   }
        raise NotImplementedError("MTBench.load_data not yet implemented")

    def run_inference(
        self, model: Any, tokenizer: Any, data: list[dict]
    ) -> list[dict]:
        # TODO: Two-turn dialogue generation.
        #   For each question:
        #     1. Generate response to turns[0].
        #     2. Append response, generate response to turns[1].
        #   Return list of:
        #   {
        #       "question_id": int,
        #       "category": str,
        #       "model_responses": [str, str],
        #   }
        raise NotImplementedError("MTBench.run_inference not yet implemented")

    def compute_metrics(self, predictions: list[dict]) -> dict:
        # TODO: Use LLM judge to score each response pair.
        #   - Call judge_model API for each prediction.
        #   - Extract score (1-10) for turn-1 and turn-2.
        #   - Aggregate:
        #     - avg_score (overall)
        #     - avg_score_turn1, avg_score_turn2
        #     - by_category: {category: {avg_score, avg_turn1, avg_turn2}}
        raise NotImplementedError("MTBench.compute_metrics not yet implemented")


# ---------------------------------------------------------------------------
# Benchmark: MMLU (massive multitask language understanding)
# ---------------------------------------------------------------------------

class MMLU(BenchmarkBase):
    """MMLU: multiple-choice evaluation across 57 subjects."""

    name = "mmlu"

    def __init__(self, n_few_shot: int = 5, subjects: list[str] | None = None, **kwargs):
        super().__init__(**kwargs)
        self.n_few_shot = n_few_shot
        self.subjects = subjects

    def load_data(self) -> list[dict]:
        # TODO: Load from HuggingFace datasets ("cais/mmlu" or "lukaemon/mmlu").
        #   If self.subjects is set, filter to those subjects only.
        #   Expected format per sample:
        #   {
        #       "id": str,
        #       "subject": str,
        #       "question": str,
        #       "choices": [str, str, str, str],
        #       "answer": int,             # index 0-3
        #       "few_shot_examples": list[dict] | None,
        #   }
        raise NotImplementedError("MMLU.load_data not yet implemented")

    def run_inference(
        self, model: Any, tokenizer: Any, data: list[dict]
    ) -> list[dict]:
        # TODO: Few-shot prompting with n_few_shot examples per subject.
        #   For each sample:
        #     1. Build prompt: few-shot examples + question + choices.
        #     2. Get model logits for choice tokens (A/B/C/D).
        #     3. Select highest-probability choice.
        #   Return list of:
        #   {
        #       "id": str,
        #       "subject": str,
        #       "predicted": int,   # 0-3
        #       "correct": int,     # 0-3
        #   }
        raise NotImplementedError("MMLU.run_inference not yet implemented")

    def compute_metrics(self, predictions: list[dict]) -> dict:
        # TODO: Compute:
        #   - overall accuracy
        #   - by_category (STEM / Humanities / Social Sciences / Other)
        #   - by_subject: {subject: {accuracy, n}}
        raise NotImplementedError("MMLU.compute_metrics not yet implemented")


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

BENCHMARK_REGISTRY: dict[str, type[BenchmarkBase]] = {
    "sycon_bench": SYCONBench,
    "sycophancy_eval": SycophancyEval,
    "mt_bench": MTBench,
    "mmlu": MMLU,
}


class EvalPipeline:
    """Orchestrates multiple benchmark evaluations and produces a unified report."""

    def __init__(self, device: str = "cuda"):
        self.device = device
        self.benchmarks: dict[str, BenchmarkBase] = {}

    def register_benchmark(self, name: str, benchmark: BenchmarkBase) -> None:
        self.benchmarks[name] = benchmark

    def register_defaults(self, names: list[str] | None = None, **kwargs) -> None:
        targets = names if names else list(BENCHMARK_REGISTRY.keys())
        for name in targets:
            if name not in BENCHMARK_REGISTRY:
                raise ValueError(
                    f"Unknown benchmark: {name}. "
                    f"Available: {list(BENCHMARK_REGISTRY.keys())}"
                )
            self.benchmarks[name] = BENCHMARK_REGISTRY[name](
                device=self.device, **kwargs
            )

    def run_all(self, model: Any, tokenizer: Any) -> dict:
        results = {}
        for name, bench in self.benchmarks.items():
            logger.info("Running benchmark: %s", name)
            try:
                results[name] = bench.evaluate(model, tokenizer)
            except NotImplementedError as e:
                logger.warning("[%s] Skipped (not implemented): %s", name, e)
                results[name] = {"status": "not_implemented", "error": str(e)}
            except Exception as e:
                logger.error("[%s] Failed: %s", name, e, exc_info=True)
                results[name] = {"status": "error", "error": str(e)}
        return results

    def dry_run(self) -> dict:
        results = {}
        for name, bench in self.benchmarks.items():
            logger.info("Dry-run benchmark: %s", name)
            try:
                results[name] = bench.dry_run()
            except NotImplementedError as e:
                logger.warning("[%s] Dry-run skipped (not implemented): %s", name, e)
                results[name] = {"status": "not_implemented", "error": str(e)}
            except Exception as e:
                logger.error("[%s] Dry-run failed: %s", name, e, exc_info=True)
                results[name] = {"status": "error", "error": str(e)}
        return results

    def save_report(
        self,
        results: dict,
        output_path: str | Path,
        model_name: str = "unknown",
    ) -> Path:
        output_path = Path(output_path)
        output_path.mkdir(parents=True, exist_ok=True)

        report = {
            "model": model_name,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "benchmarks": results,
        }

        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        report_file = output_path / f"eval_report_{ts}.json"
        report_file.write_text(json.dumps(report, indent=2, ensure_ascii=False))
        logger.info("Report saved to %s", report_file)
        return report_file


# ---------------------------------------------------------------------------
# Model loading helper
# ---------------------------------------------------------------------------

def load_model_and_tokenizer(model_path: str, device: str = "cuda"):
    """Load a HuggingFace model and tokenizer."""
    if torch is None:
        raise RuntimeError("PyTorch is required for model loading. Install with: pip install torch")
    from transformers import AutoModelForCausalLM, AutoTokenizer

    logger.info("Loading tokenizer from %s", model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

    logger.info("Loading model from %s", model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        device_map=device if device != "cpu" else None,
        trust_remote_code=True,
    )
    if device == "cpu":
        model = model.float()
    model.eval()

    return model, tokenizer


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Unified evaluation pipeline for contrastive entrainment calibration"
    )
    parser.add_argument(
        "--model-path", type=str, required=True, help="Path to HuggingFace model"
    )
    parser.add_argument(
        "--benchmarks",
        type=str,
        default="all",
        help=(
            "Comma-separated benchmark names to run "
            f"(choices: {','.join(BENCHMARK_REGISTRY.keys())}, all). Default: all"
        ),
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="eval_results",
        help="Directory for evaluation reports (default: eval_results)",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="cuda" if torch and torch.cuda.is_available() else "cpu",
        help="Device for inference (default: cuda if available)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only load data to verify pipeline connectivity, skip inference",
    )
    parser.add_argument(
        "--judge-model",
        type=str,
        default="gpt-4",
        help="Judge model for MT-Bench scoring (default: gpt-4)",
    )
    parser.add_argument(
        "--mmlu-subjects",
        type=str,
        default=None,
        help="Comma-separated MMLU subjects to evaluate (default: all)",
    )
    parser.add_argument(
        "--mmlu-few-shot",
        type=int,
        default=5,
        help="Number of few-shot examples for MMLU (default: 5)",
    )
    parser.add_argument(
        "--sycon-max-turns",
        type=int,
        default=10,
        help="Max pressure turns for SYCONBench (default: 10)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
    )

    benchmark_names = (
        list(BENCHMARK_REGISTRY.keys())
        if args.benchmarks == "all"
        else [b.strip() for b in args.benchmarks.split(",")]
    )

    extra_kwargs = {}
    bench_specific: dict[str, dict] = {
        "mt_bench": {"judge_model": args.judge_model},
        "mmlu": {
            "n_few_shot": args.mmlu_few_shot,
            "subjects": (
                [s.strip() for s in args.mmlu_subjects.split(",")]
                if args.mmlu_subjects
                else None
            ),
        },
        "sycon_bench": {"max_turns": args.sycon_max_turns},
    }

    pipeline = EvalPipeline(device=args.device)
    for name in benchmark_names:
        if name not in BENCHMARK_REGISTRY:
            logger.error("Unknown benchmark: %s", name)
            sys.exit(1)
        kw = {**extra_kwargs, **bench_specific.get(name, {})}
        pipeline.register_benchmark(
            name, BENCHMARK_REGISTRY[name](device=args.device, **kw)
        )

    if args.dry_run:
        logger.info("=== DRY RUN ===")
        results = pipeline.dry_run()
        print(json.dumps(results, indent=2))
        return

    model, tokenizer = load_model_and_tokenizer(args.model_path, args.device)

    results = pipeline.run_all(model, tokenizer)
    model_name = Path(args.model_path).name
    report_path = pipeline.save_report(results, args.output_dir, model_name=model_name)
    print(f"\nEvaluation complete. Report: {report_path}")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()

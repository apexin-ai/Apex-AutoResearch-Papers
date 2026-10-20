"""
SICA pipeline for LogiQA 2.0 (4-choice logic reasoning).
Runs SICA vs SC@K on LogiQA data.

Usage:
  python run_logiqa.py --mode mock --dry-run 3
  python run_logiqa.py --mode vllm --k 12 --api-base http://localhost:8000/v1
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time

from sica.constraint_extractor import ConstraintExtractor, MockLLM, APIBasedLLM, VLLMBackend
from sica.trace_generator import MockGenerator, VLLMGenerator, APIGenerator
from sica.pipeline import SICAPipeline
from baselines.self_consistency import SelfConsistency
from utils.math_equiv import is_equiv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


def load_logiqa(path: str) -> list[dict]:
    with open(path) as f:
        data = json.load(f)
    for p in data:
        p.setdefault("dataset", "logiqa")
    logger.info("Loaded %d LogiQA problems from %s", len(data), path)
    return data


def build_generator(args):
    if args.mode == "mock":
        return MockGenerator()
    elif args.mode == "vllm":
        return VLLMGenerator(
            base_url=args.api_base,
            api_key=[REDACTED],
            model=args.model if args.model != "auto" else None,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
        )
    elif args.mode == "api":
        return APIGenerator(
            base_url=args.api_base,
            api_key=[REDACTED],
            model=args.model,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
        )
    raise ValueError(f"Unknown mode: {args.mode}")


def build_extractor(args):
    if args.mode == "mock":
        return ConstraintExtractor(llm=MockLLM(domain="logic"))
    elif args.mode == "vllm":
        return ConstraintExtractor(llm=VLLMBackend(
            base_url=args.api_base,
            model=args.model if args.model != "auto" else None,
        ))
    return ConstraintExtractor(llm=APIBasedLLM(
        base_url=args.api_base,
        api_key=[REDACTED],
        model=args.model if args.model != "auto" else None,
        temperature=0.1,
    ))


def main():
    parser = argparse.ArgumentParser(description="SICA on LogiQA 2.0")
    parser.add_argument("--data", default="data/logiqa_200.json")
    parser.add_argument("--output", default="results/logiqa/logiqa_results.json")
    parser.add_argument("--mode", choices=["mock", "vllm", "api"], default="vllm")
    parser.add_argument("--k", type=int, default=12)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument("--api-base", default="http://localhost:8000/v1")
    parser.add_argument("--api-key", default="EMPTY")
    parser.add_argument("--model", default="auto")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--maxsat-timeout", type=int, default=10000)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--save-intermediates", action="store_true")
    parser.add_argument("--dry-run", type=int, default=0, help="Only process N problems (0=all)")
    args = parser.parse_args()

    problems = load_logiqa(args.data)
    if args.dry_run > 0:
        problems = problems[:args.dry_run]
        logger.info("Dry-run mode: processing %d problems", len(problems))

    generator = build_generator(args)
    extractor = build_extractor(args)

    # Set domains for LogiQA (multichoice + logic constraints)
    generator.domain = "multichoice"
    extractor.domain = "logic"

    pipeline = SICAPipeline(
        trace_generator=generator,
        constraint_extractor=extractor,
        k=args.k,
        maxsat_timeout_ms=args.maxsat_timeout,
    )
    sc_baseline = SelfConsistency()

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)

    # Resume support
    completed_ids = set()
    all_results = []
    if args.resume and os.path.exists(args.output):
        with open(args.output) as f:
            prev = json.load(f)
        all_results = prev.get("results", [])
        completed_ids = {r["problem_id"] for r in all_results}
        logger.info("Resumed: %d already completed", len(completed_ids))

    remaining = [(i, p) for i, p in enumerate(problems) if p["id"] not in completed_ids]
    total_start = time.time()
    elapsed_times = []

    for progress_idx, (i, prob) in enumerate(remaining):
        t0 = time.time()
        prob_id = prob["id"]

        print(f"\n--- [{progress_idx+1}/{len(remaining)}] (overall {i+1}/{len(problems)}) ---")
        print(f"ID: {prob_id}")
        print(f"Q: {prob['problem'][:120]}...")
        print(f"GT: {prob['answer']}")
        sys.stdout.flush()

        try:
            sica_result = pipeline.run_single(prob)
            sica_answer = sica_result.get("answer", "")
            sica_correct = is_equiv(sica_answer, prob["answer"])
            cs = sica_result.get("constraints_stats", {})
            print(f"SICA: {sica_answer} ({'V' if sica_correct else 'X'}) "
                  f"-- constraints: {cs.get('total_extracted', 0)} extracted, "
                  f"{cs.get('unique_after_dedup', 0)} unique")
        except Exception as e:
            logger.error("SICA error on %s: %s", prob_id, e)
            import traceback; traceback.print_exc()
            sica_result = {"answer": "", "traces": [], "scores": {},
                           "constraints_stats": {"total_extracted": 0, "traces_with_constraints": 0, "unique_after_dedup": 0},
                           "maxsat_stats": {"satisfied": 0, "excluded": 0, "total_weight": 0, "solve_time_ms": 0},
                           "timing": {}}
            sica_answer = ""
            sica_correct = False

        try:
            traces = sica_result.get("traces", [])
            answers = [t.get("answer", "") for t in traces]
            sc_result = sc_baseline.run(prob, traces=[t.get("trace", "") for t in traces], answers=answers)
            sc_answer = sc_result.get("answer", "")
            sc_correct = is_equiv(sc_answer, prob["answer"])
            print(f"SC:   {sc_answer} ({'V' if sc_correct else 'X'}) -- votes: {sc_result.get('vote_count', '?')}/{len(traces)}")
        except Exception as e:
            logger.error("SC error on %s: %s", prob_id, e)
            sc_answer = ""
            sc_correct = False
            sc_result = {"vote_count": 0, "vote_distribution": {}}

        elapsed = time.time() - t0
        elapsed_times.append(elapsed)
        print(f"Time: {elapsed:.1f}s")

        remaining_count = len(remaining) - (progress_idx + 1)
        if remaining_count > 0:
            avg_time = sum(elapsed_times) / len(elapsed_times)
            eta_min = avg_time * remaining_count / 60
            print(f"ETA: {eta_min:.1f} min ({remaining_count} remaining)")

        sys.stdout.flush()

        result_entry = {
            "problem_idx": i,
            "problem_id": prob_id,
            "problem": prob["problem"],
            "dataset": "logiqa",
            "ground_truth": prob["answer"],
            "sica_answer": sica_answer,
            "sica_scores": sica_result.get("scores", {}),
            "sica_correct": sica_correct,
            "sc_answer": sc_answer,
            "sc_vote_count": sc_result.get("vote_count", 0),
            "sc_vote_distribution": sc_result.get("vote_distribution", {}),
            "sc_correct": sc_correct,
            "constraints_stats": sica_result.get("constraints_stats", {}),
            "maxsat_stats": sica_result.get("maxsat_stats", {}),
            "timing": sica_result.get("timing", {}),
            "wall_time_s": round(elapsed, 2),
        }
        all_results.append(result_entry)

        if args.save_intermediates:
            intermed_dir = os.path.join(os.path.dirname(args.output) or ".", "intermediates")
            os.makedirs(intermed_dir, exist_ok=True)
            with open(os.path.join(intermed_dir, f"{prob_id}.json"), "w") as f:
                json.dump({"problem": prob, "sica_result": sica_result}, f, indent=2, default=str)

        # Checkpoint
        n = len(all_results)
        sica_acc = sum(1 for r in all_results if r["sica_correct"]) / n
        sc_acc = sum(1 for r in all_results if r["sc_correct"]) / n
        summary = {
            "n": n,
            "sica_accuracy": round(sica_acc, 4),
            "sc_accuracy": round(sc_acc, 4),
            "delta": round(sica_acc - sc_acc, 4),
            "k": args.k,
            "mode": args.mode,
            "total_wall_time_s": round(time.time() - total_start, 1),
            "extraction_stats": {
                "success": extractor.stats.success,
                "fail_json_parse": extractor.stats.fail_json_parse,
                "fail_empty": extractor.stats.fail_empty,
                "fail_invalid_expr": extractor.stats.fail_invalid_expr,
            },
        }
        output = {"summary": summary, "results": all_results}
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2, default=str)

    # Final summary
    n = len(all_results)
    if n > 0:
        sica_acc = sum(1 for r in all_results if r["sica_correct"]) / n
        sc_acc = sum(1 for r in all_results if r["sc_correct"]) / n
        print(f"\n{'='*60}")
        print(f"FINAL RESULTS ({n} LogiQA problems)")
        print(f"  SICA:  {sica_acc:.4f} ({sum(1 for r in all_results if r['sica_correct'])}/{n})")
        print(f"  SC:    {sc_acc:.4f} ({sum(1 for r in all_results if r['sc_correct'])}/{n})")
        print(f"  Delta: {sica_acc - sc_acc:+.4f}")
        print(f"  Wall:  {(time.time() - total_start)/60:.1f} min")
        print(f"Results saved to {args.output}")

    print("LOGIQA_DONE")


if __name__ == "__main__":
    main()

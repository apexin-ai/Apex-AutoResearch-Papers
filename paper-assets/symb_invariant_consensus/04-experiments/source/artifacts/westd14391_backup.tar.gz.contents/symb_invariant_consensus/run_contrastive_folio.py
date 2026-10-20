"""
Contrastive SICA pipeline for FOLIO dataset.
Reuses existing traces from a prior run and applies contrastive constraint
extraction + contrastive-aware MaxSAT scoring.

Input:  existing intermediate files (folio_*.json) with pre-generated traces
Output: per-problem results JSON to results/contrastive_folio/

Usage:
  python run_contrastive_folio.py --traces-dir results/folio_204_14b/intermediates \
      --mode vllm --api-base http://localhost:8000/v1
  python run_contrastive_folio.py --traces-dir results/folio_204_14b/intermediates \
      --mode mock --dry-run 3
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
import glob

from sica.constraint_extractor import (
    ContrastiveConstraintExtractor, VLLMBackend, APIBasedLLM, MockLLM,
)
from sica.pipeline import ContrastiveSICAPipeline, normalize_logic_answer
from utils.math_equiv import is_equiv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


def load_intermediates(traces_dir: str) -> list[dict]:
    """Load all folio_*.json intermediate files. Each has {problem, sica_result}."""
    pattern = os.path.join(traces_dir, "folio_*.json")
    files = sorted(glob.glob(pattern), key=lambda f: int(os.path.basename(f).split("_")[1].split(".")[0]))
    items = []
    for fp in files:
        with open(fp) as f:
            data = json.load(f)
        items.append(data)
    logger.info("Loaded %d intermediate files from %s", len(items), traces_dir)
    return items


def build_extractor(args):
    if args.mode == "mock":
        return ContrastiveConstraintExtractor(llm=MockLLM(domain="logic"))
    elif args.mode == "vllm":
        return ContrastiveConstraintExtractor(llm=VLLMBackend(
            base_url=args.api_base,
            model=args.model if args.model != "auto" else None,
        ))
    return ContrastiveConstraintExtractor(llm=APIBasedLLM(
        base_url=args.api_base,
        api_key=[REDACTED],
        model=args.model if args.model != "auto" else None,
        temperature=0.1,
    ))


def main():
    parser = argparse.ArgumentParser(description="Contrastive SICA on FOLIO")
    parser.add_argument("--traces-dir", required=True,
                        help="Dir with folio_*.json intermediates")
    parser.add_argument("--output", default="results/contrastive_folio/contrastive_results.json")
    parser.add_argument("--mode", choices=["mock", "vllm", "api"], default="vllm")
    parser.add_argument("--api-base", default="http://localhost:8000/v1")
    parser.add_argument("--api-key", default="EMPTY")
    parser.add_argument("--model", default="auto")
    parser.add_argument("--scorer-alpha", type=float, default=1.0,
                        help="Weight multiplier for opposing constraints in scoring")
    parser.add_argument("--maxsat-timeout", type=int, default=10000)
    parser.add_argument("--dry-run", type=int, default=0,
                        help="Only process N problems (0 = all)")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--save-intermediates", action="store_true")
    args = parser.parse_args()

    intermediates = load_intermediates(args.traces_dir)
    if args.dry_run > 0:
        intermediates = intermediates[:args.dry_run]

    extractor = build_extractor(args)
    pipeline = ContrastiveSICAPipeline(
        contrastive_extractor=extractor,
        maxsat_timeout_ms=args.maxsat_timeout,
        scorer_alpha=args.scorer_alpha,
    )

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)

    # Resume support
    completed_ids = set()
    all_results = []
    if args.resume and os.path.exists(args.output):
        with open(args.output) as f:
            prev = json.load(f)
        all_results = prev.get("results", [])
        completed_ids = {r["problem_id"] for r in all_results}
        logger.info("Resuming: %d already completed", len(completed_ids))

    total_start = time.time()
    elapsed_times = []

    for idx, item in enumerate(intermediates):
        problem = item["problem"]
        prob_id = problem.get("id", f"folio_{idx}")

        if prob_id in completed_ids:
            continue

        traces = item["sica_result"]["traces"]

        print(f"\n{'='*60}")
        print(f"[{idx+1}/{len(intermediates)}] {prob_id}")
        print(f"  GT: {problem['answer']}")
        print(f"  Traces: {len(traces)}")

        t0 = time.time()
        try:
            result = pipeline.run_single(problem, traces)
            contrastive_answer = result["answer"]
            contrastive_correct = is_equiv(contrastive_answer, problem["answer"])

            # SC baseline from traces
            from collections import Counter
            ans_counts = Counter(
                normalize_logic_answer(t["answer"])
                for t in traces if t.get("answer")
            )
            sc_answer = ans_counts.most_common(1)[0][0] if ans_counts else ""
            sc_correct = is_equiv(sc_answer, problem["answer"])

            print(f"  Contrastive: {contrastive_answer} ({'V' if contrastive_correct else 'X'})")
            print(f"  SC baseline: {sc_answer} ({'V' if sc_correct else 'X'})")
            print(f"  Scores: {result['scores']}")
            print(f"  Constraints: {result['constraints_stats']}")
        except Exception as e:
            logger.error("Error on %s: %s", prob_id, e)
            import traceback; traceback.print_exc()
            contrastive_answer = ""
            contrastive_correct = False
            sc_answer = ""
            sc_correct = False
            result = {"scores": {}, "constraints_stats": {}, "maxsat_stats": {}, "timing": {}}

        elapsed = time.time() - t0
        elapsed_times.append(elapsed)
        print(f"  Time: {elapsed:.1f}s")

        if elapsed_times:
            avg_t = sum(elapsed_times) / len(elapsed_times)
            remaining = len(intermediates) - (idx + 1) - len(completed_ids)
            if remaining > 0:
                print(f"  ETA: {avg_t * remaining / 60:.1f} min ({remaining} remaining)")

        result_entry = {
            "problem_idx": idx,
            "problem_id": prob_id,
            "problem": problem["problem"],
            "dataset": "folio",
            "ground_truth": problem["answer"],
            "contrastive_answer": contrastive_answer,
            "contrastive_correct": contrastive_correct,
            "contrastive_scores": result.get("scores", {}),
            "sc_answer": sc_answer,
            "sc_correct": sc_correct,
            "constraints_stats": result.get("constraints_stats", {}),
            "maxsat_stats": result.get("maxsat_stats", {}),
            "timing": result.get("timing", {}),
        }
        all_results.append(result_entry)

        if args.save_intermediates:
            intermed_dir = os.path.join(os.path.dirname(args.output) or ".", "intermediates")
            os.makedirs(intermed_dir, exist_ok=True)
            with open(os.path.join(intermed_dir, f"{prob_id}.json"), "w") as f:
                json.dump({"problem": problem, "contrastive_result": result}, f, indent=2, default=str)

        # Checkpoint
        n = len(all_results)
        contrastive_acc = sum(1 for r in all_results if r["contrastive_correct"]) / n
        sc_acc = sum(1 for r in all_results if r["sc_correct"]) / n
        summary = {
            "n": n,
            "contrastive_accuracy": round(contrastive_acc, 4),
            "sc_accuracy": round(sc_acc, 4),
            "delta": round(contrastive_acc - sc_acc, 4),
            "scorer_alpha": args.scorer_alpha,
            "mode": args.mode,
            "total_wall_time_s": round(time.time() - total_start, 1),
            "extractor_stats": {
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
        contrastive_acc = sum(1 for r in all_results if r["contrastive_correct"]) / n
        sc_acc = sum(1 for r in all_results if r["sc_correct"]) / n
        print(f"\n{'='*60}")
        print(f"FINAL RESULTS ({n} problems)")
        print(f"  Contrastive SICA: {contrastive_acc:.4f} ({sum(1 for r in all_results if r['contrastive_correct'])}/{n})")
        print(f"  SC baseline:      {sc_acc:.4f} ({sum(1 for r in all_results if r['sc_correct'])}/{n})")
        print(f"  Delta:            {contrastive_acc - sc_acc:+.4f}")
        print(f"  Wall time:        {(time.time() - total_start)/60:.1f} min")
        print(f"Results saved to {args.output}")

    print("CONTRASTIVE_FOLIO_DONE")


if __name__ == "__main__":
    main()

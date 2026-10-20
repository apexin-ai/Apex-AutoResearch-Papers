#!/usr/bin/env python3
"""Cross-model constraint extraction: re-extract constraints from existing traces using a different model."""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from collections import Counter

sys.path.insert(0, "/root/symb_invariant_consensus")
from sica.constraint_extractor import ConstraintExtractor, APIBasedLLM
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver
from sica.scorer import InvariantScorer
from sica.pipeline import normalize_logic_answer
from baselines.self_consistency import SelfConsistency
from utils.math_equiv import is_equiv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Cross-model constraint extraction")
    parser.add_argument("--traces-dir", required=True, help="Intermediates dir from run_full_mvp.py")
    parser.add_argument("--api-base", default="http://localhost:8000/v1")
    parser.add_argument("--model", default="auto")
    parser.add_argument("--temperature", type=float, default=0.3)
    parser.add_argument("--output", required=True)
    parser.add_argument("--maxsat-timeout-ms", type=int, default=10000)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--qwen3-nothink", action="store_true", help="Disable Qwen3 thinking mode")
    args = parser.parse_args()

    from openai import OpenAI
    client = OpenAI(base_url=args.api_base, api_key="[REDACTED]")
    if args.model == "auto":
        model_name = client.models.list().data[0].id
    else:
        model_name = args.model
    logger.info("Extraction model: %s", model_name)

    extra_body = {"chat_template_kwargs": {"enable_thinking": False}} if args.qwen3_nothink else None
    llm = APIBasedLLM(
        base_url=args.api_base,
        model=model_name,
        temperature=args.temperature,
        extra_body=extra_body,
    )
    extractor = ConstraintExtractor(llm=llm)
    deduplicator = ConstraintDeduplicator()
    solver = MaxSATSolver()
    scorer = InvariantScorer()
    sc_baseline = SelfConsistency()

    files = sorted(f for f in os.listdir(args.traces_dir) if f.endswith(".json"))
    logger.info("Found %d intermediate files in %s", len(files), args.traces_dir)

    completed_ids = set()
    all_results = []
    if args.resume and os.path.exists(args.output):
        with open(args.output) as f:
            checkpoint = json.load(f)
        if "results" in checkpoint:
            all_results = checkpoint["results"]
            completed_ids = {r["problem_id"] for r in all_results}
            logger.info("Resuming: %d already done", len(completed_ids))

    total_start = time.time()
    elapsed_times = []

    for idx, fname in enumerate(files):
        with open(os.path.join(args.traces_dir, fname)) as f:
            data = json.load(f)

        prob = data["problem"]
        sica_orig = data["sica_result"]
        traces = sica_orig["traces"]
        prob_id = prob["id"]

        if prob_id in completed_ids:
            continue

        dataset = prob.get("dataset", "math")
        t0 = time.time()

        remaining = len(files) - len(completed_ids) - (len(all_results) - len(completed_ids))
        print(f"\n--- [{len(all_results)+1}/{len(files)}] {prob_id} ({dataset}) ---")

        extractor.domain = "logic" if dataset in ("proofwriter", "folio") else "math"

        try:
            all_constraints = extractor.extract_batch([t["trace"] for t in traces])
        except Exception as e:
            logger.error("Extraction failed for %s: %s", prob_id, e)
            all_constraints = [[] for _ in traces]

        total_constraints = sum(len(c) for c in all_constraints)
        non_empty = sum(1 for c in all_constraints if c)

        unique_constraints = deduplicator.deduplicate(all_constraints)
        maxsat_result = solver.solve(unique_constraints, timeout_ms=args.maxsat_timeout_ms)

        if dataset in ("proofwriter", "folio"):
            for t in traces:
                if t.get("answer"):
                    t["answer"] = normalize_logic_answer(t["answer"])

        candidates = list(set(t["answer"] for t in traces if t["answer"]))
        answer_counts = Counter(t["answer"] for t in traces if t["answer"])
        scores = scorer.score(maxsat_result, traces, candidates)
        selected = scorer.select_answer(scores, answer_counts)

        sc_result = sc_baseline.run(
            prob,
            traces=[t["trace"] for t in traces],
            answers=[t["answer"] for t in traces],
        )
        sc_answer = sc_result.get("answer", "")
        sc_correct = is_equiv(sc_answer, prob["answer"])

        cross_correct = is_equiv(selected, prob["answer"])
        orig_answer = sica_orig.get("answer", "")
        orig_correct = is_equiv(orig_answer, prob["answer"])

        elapsed = time.time() - t0
        elapsed_times.append(elapsed)

        print(f"  Cross-model: {selected} ({'V' if cross_correct else 'X'}) | "
              f"Original: {orig_answer} ({'V' if orig_correct else 'X'}) | "
              f"SC: {sc_answer} ({'V' if sc_correct else 'X'})")
        print(f"  Constraints: {total_constraints} extracted -> {len(unique_constraints)} unique")
        print(f"  Time: {elapsed:.1f}s")

        if elapsed_times:
            avg_t = sum(elapsed_times) / len(elapsed_times)
            rem = len(files) - len(all_results) - 1
            if rem > 0:
                print(f"  ETA: {avg_t * rem / 60:.1f} min ({rem} remaining)")

        sys.stdout.flush()

        result_entry = {
            "problem_id": prob_id,
            "problem": prob["problem"],
            "dataset": dataset,
            "level": prob.get("level", "unknown"),
            "ground_truth": prob["answer"],
            "cross_model_answer": selected,
            "cross_model_scores": scores,
            "cross_model_correct": cross_correct,
            "original_sica_answer": orig_answer,
            "original_sica_correct": orig_correct,
            "sc_answer": sc_answer,
            "sc_vote_distribution": sc_result.get("vote_distribution", {}),
            "sc_correct": sc_correct,
            "constraints_stats": {
                "total_extracted": total_constraints,
                "traces_with_constraints": non_empty,
                "unique_after_dedup": len(unique_constraints),
            },
            "maxsat_stats": {
                "satisfied": len(maxsat_result.satisfied),
                "excluded": len(maxsat_result.excluded),
                "total_weight": maxsat_result.total_weight,
                "solve_time_ms": maxsat_result.solve_time_ms,
            },
            "wall_time_s": round(elapsed, 2),
        }
        all_results.append(result_entry)

        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        with open(args.output, "w") as f:
            json.dump({"results": all_results}, f, indent=2, default=str)

    total_wall = time.time() - total_start
    n = len(all_results)
    cross_correct_n = sum(1 for r in all_results if r["cross_model_correct"])
    orig_correct_n = sum(1 for r in all_results if r["original_sica_correct"])
    sc_correct_n = sum(1 for r in all_results if r["sc_correct"])

    summary = {
        "extraction_model": model_name,
        "extraction_temperature": args.temperature,
        "total": n,
        "cross_model_correct": cross_correct_n,
        "cross_model_acc": round(cross_correct_n / n, 4) if n else 0,
        "original_sica_correct": orig_correct_n,
        "original_sica_acc": round(orig_correct_n / n, 4) if n else 0,
        "sc_correct": sc_correct_n,
        "sc_acc": round(sc_correct_n / n, 4) if n else 0,
        "total_wall_time_s": round(total_wall, 1),
    }

    output = {"summary": summary, "results": all_results}
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\n=== Cross-Model Extraction Summary ===")
    print(f"Extraction model: {model_name} (T={args.temperature})")
    print(f"Total: {n}")
    print(f"Cross-model SICA: {cross_correct_n}/{n} = {summary['cross_model_acc']:.4f}")
    print(f"Original SICA:    {orig_correct_n}/{n} = {summary['original_sica_acc']:.4f}")
    print(f"SC@K baseline:    {sc_correct_n}/{n} = {summary['sc_acc']:.4f}")
    print(f"Wall time: {total_wall/60:.1f} min")
    print(f"Results: {args.output}")
    print("CROSS_MODEL_DONE")


if __name__ == "__main__":
    main()

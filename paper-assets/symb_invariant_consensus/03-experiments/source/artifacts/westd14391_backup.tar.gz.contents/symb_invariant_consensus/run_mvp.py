"""
SICA MVP experiment: MATH-500 subset, SICA vs SC@K.
Usage:
  python run_mvp.py --mode mock --k 3
  python run_mvp.py --mode vllm --k 12
  python run_mvp.py --mode api --k 12 --api-base http://localhost:8000/v1 --api-key x --model m
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import time

from sica.constraint_extractor import ConstraintExtractor, MockLLM, APIBasedLLM, VLLMBackend
from sica.trace_generator import MockGenerator, VLLMGenerator, APIGenerator
from sica.pipeline import SICAPipeline
from baselines.self_consistency import SelfConsistency

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def load_problems(path: str) -> list[dict]:
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    logger.warning("Data file %s not found, generating mock problems", path)
    return [
        {"problem": "If x + 5 = 12, what is x?", "answer": "7", "level": "easy"},
        {"problem": "What is 15 * 13?", "answer": "195", "level": "easy"},
        {"problem": "Solve: 2x + 3 = 11", "answer": "4", "level": "medium"},
        {"problem": "What is the sum of 1+2+...+10?", "answer": "55", "level": "medium"},
        {"problem": "If a triangle has sides 3,4,5, what is its area?", "answer": "6", "level": "hard"},
    ]


def build_generator(args):
    if args.mode == "mock":
        return MockGenerator()
    elif args.mode == "vllm":
        return VLLMGenerator(
            base_url=args.api_base,
            api_key=[REDACTED],
            model=args.model if args.model != "auto" else None,
        )
    elif args.mode == "api":
        return APIGenerator(
            base_url=args.api_base,
            api_key=[REDACTED],
            model=args.model,
        )
    raise ValueError(f"Unknown mode: {args.mode}")


def build_extractor(args):
    if args.mode == "mock":
        return ConstraintExtractor(llm=MockLLM())
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
    parser = argparse.ArgumentParser(description="SICA MVP Experiment")
    parser.add_argument("--mode", choices=["mock", "vllm", "api"], default="mock")
    parser.add_argument("--k", type=int, default=12)
    parser.add_argument("--model", type=str, default="auto")
    parser.add_argument("--api-base", type=str, default="http://localhost:8000/v1")
    parser.add_argument("--api-key", type=str, default="EMPTY")
    parser.add_argument("--data", type=str, default="data/math500_subset.json")
    parser.add_argument("--output", type=str, default="results/mvp_results.json")
    args = parser.parse_args()

    logger.info("SICA MVP | mode=%s k=%d", args.mode, args.k)

    problems = load_problems(args.data)
    logger.info("Loaded %d problems", len(problems))

    generator = build_generator(args)
    extractor = build_extractor(args)
    pipeline = SICAPipeline(trace_generator=generator, constraint_extractor=extractor, k=args.k)
    sc_baseline = SelfConsistency()

    all_results = []
    sica_correct = 0
    sc_correct = 0
    level_stats: dict[str, dict] = {}

    for i, prob in enumerate(problems):
        logger.info("[%d/%d] %s", i + 1, len(problems), prob["problem"][:60])

        sica_result = pipeline.run_single(prob)

        traces = sica_result["traces"]
        sc_result = sc_baseline.run(
            problem=prob,
            traces=[t["trace"] for t in traces],
            answers=[t["answer"] for t in traces],
        )

        gt = str(prob.get("answer", "")).strip()
        sica_ok = sica_result["answer"] == gt
        sc_ok = sc_result["answer"] == gt
        if sica_ok:
            sica_correct += 1
        if sc_ok:
            sc_correct += 1

        level = prob.get("level", "unknown")
        if level not in level_stats:
            level_stats[level] = {"sica_correct": 0, "sc_correct": 0, "total": 0}
        level_stats[level]["total"] += 1
        if sica_ok:
            level_stats[level]["sica_correct"] += 1
        if sc_ok:
            level_stats[level]["sc_correct"] += 1

        all_results.append({
            "problem_idx": i,
            "problem": prob["problem"],
            "ground_truth": gt,
            "sica_answer": sica_result["answer"],
            "sica_scores": sica_result["scores"],
            "sica_correct": sica_ok,
            "sc_answer": sc_result["answer"],
            "sc_vote_count": sc_result["vote_count"],
            "sc_correct": sc_ok,
            "constraints_stats": sica_result["constraints_stats"],
            "maxsat_stats": sica_result["maxsat_stats"],
            "timing": sica_result["timing"],
        })

    n = len(problems)
    ext_stats = pipeline.constraint_extractor.stats
    total_extracted = sum(r["constraints_stats"]["total_extracted"] for r in all_results)
    total_excluded = sum(r["maxsat_stats"]["excluded"] for r in all_results)
    total_unique = sum(r["constraints_stats"]["unique_after_dedup"] for r in all_results)

    summary = {
        "n_problems": n,
        "k": args.k,
        "mode": args.mode,
        "extraction_rate": ext_stats.success / max(ext_stats.success + ext_stats.total_fail, 1),
        "contradiction_rate": total_excluded / max(total_unique, 1),
        "sica_accuracy": sica_correct / max(n, 1),
        "sc_accuracy": sc_correct / max(n, 1),
        "per_level_accuracy": {
            lv: {
                "sica": s["sica_correct"] / max(s["total"], 1),
                "sc": s["sc_correct"] / max(s["total"], 1),
                "n": s["total"],
            }
            for lv, s in level_stats.items()
        },
    }

    output = {"summary": summary, "results": all_results}

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, default=str)

    logger.info("=== Summary ===")
    logger.info("Extraction rate: %.1f%%", summary["extraction_rate"] * 100)
    logger.info("Contradiction rate: %.1f%%", summary["contradiction_rate"] * 100)
    logger.info("SICA accuracy: %.1f%% (%d/%d)", summary["sica_accuracy"] * 100, sica_correct, n)
    logger.info("SC accuracy: %.1f%% (%d/%d)", summary["sc_accuracy"] * 100, sc_correct, n)
    for lv, s in summary["per_level_accuracy"].items():
        logger.info("  [%s] SICA=%.1f%% SC=%.1f%% (n=%d)", lv, s["sica"] * 100, s["sc"] * 100, s["n"])
    logger.info("Results saved to %s", args.output)


if __name__ == "__main__":
    main()

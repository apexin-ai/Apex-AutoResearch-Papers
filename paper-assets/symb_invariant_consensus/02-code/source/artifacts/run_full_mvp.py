"""
SICA Full MVP experiment: 50 MATH-500 + 10 ProofWriter, SICA vs SC@K.
Features: resume support, per-dataset/per-level stats, ETA estimation.

Usage:
  python run_full_mvp.py --mode vllm --k 12
  python run_full_mvp.py --mode vllm --k 12 --resume
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


def load_all_problems(math_path: str, pw_path: str) -> list[dict]:
    problems = []
    if os.path.exists(math_path):
        with open(math_path) as f:
            math_data = json.load(f)
        for p in math_data:
            p.setdefault("dataset", "math")
        problems.extend(math_data)
        logger.info("Loaded %d MATH problems", len(math_data))
    else:
        logger.error("MATH data not found: %s", math_path)
        sys.exit(1)

    if os.path.exists(pw_path):
        with open(pw_path) as f:
            pw_data = json.load(f)
        for p in pw_data:
            p.setdefault("dataset", "proofwriter")
        problems.extend(pw_data)
        logger.info("Loaded %d ProofWriter problems", len(pw_data))
    else:
        logger.error("ProofWriter data not found: %s", pw_path)
        sys.exit(1)

    logger.info("Total: %d problems", len(problems))
    return problems


def load_checkpoint(output_path: str) -> dict:
    if os.path.exists(output_path):
        with open(output_path) as f:
            data = json.load(f)
        return data
    return {}


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


def compute_summary(all_results: list[dict], ext_stats) -> dict:
    n = len(all_results)
    if n == 0:
        return {}

    sica_correct = sum(1 for r in all_results if r["sica_correct"])
    sc_correct = sum(1 for r in all_results if r["sc_correct"])
    total_extracted = sum(r["constraints_stats"]["total_extracted"] for r in all_results)
    total_excluded = sum(r["maxsat_stats"]["excluded"] for r in all_results)
    total_unique = sum(r["constraints_stats"]["unique_after_dedup"] for r in all_results)
    problems_with_contradictions = sum(
        1 for r in all_results if r.get("maxsat_stats", {}).get("excluded", 0) > 0
    )

    level_stats: dict[str, dict] = {}
    dataset_stats = {}
    for r in all_results:
        level = str(r.get("level", "unknown"))
        ds = r.get("dataset", "unknown")
        for val, bucket in [(level, level_stats), (ds, dataset_stats)]:
            if val not in bucket:
                bucket[val] = {"sica_correct": 0, "sc_correct": 0, "total": 0}
            bucket[val]["total"] += 1
            if r["sica_correct"]:
                bucket[val]["sica_correct"] += 1
            if r["sc_correct"]:
                bucket[val]["sc_correct"] += 1

    def _acc(bucket):
        return {
            k: {
                "sica": v["sica_correct"] / max(v["total"], 1),
                "sc": v["sc_correct"] / max(v["total"], 1),
                "n": v["total"],
            }
            for k, v in bucket.items()
        }

    return {
        "n_problems": n,
        "sica_accuracy": sica_correct / n,
        "sc_accuracy": sc_correct / n,
        "sica_correct": sica_correct,
        "sc_correct": sc_correct,
        "extraction_rate": ext_stats.success / max(ext_stats.success + ext_stats.total_fail, 1),
        "total_constraints_extracted": total_extracted,
        "total_unique_constraints": total_unique,
        "contradiction_rate": total_excluded / max(total_unique, 1),
        "problems_with_contradictions": problems_with_contradictions,
        "per_level_accuracy": _acc(level_stats),
        "per_dataset_accuracy": _acc(dataset_stats),
    }


def print_summary(summary: dict):
    print("\n" + "=" * 80)
    print("FULL MVP EXPERIMENT RESULTS")
    print("=" * 80)
    n = summary["n_problems"]
    print(f"Problems: {n}")
    print(f"SICA accuracy: {summary['sica_accuracy']:.1%} ({summary['sica_correct']}/{n})")
    print(f"SC accuracy:   {summary['sc_accuracy']:.1%} ({summary['sc_correct']}/{n})")
    print(f"Extraction rate: {summary['extraction_rate']:.1%}")
    print(f"Contradiction rate: {summary['contradiction_rate']:.1%}")
    print(f"Problems with contradictions: {summary['problems_with_contradictions']}/{n}")

    print("\n--- By Dataset ---")
    for ds, s in sorted(summary.get("per_dataset_accuracy", {}).items()):
        print(f"  {ds:12s}: SICA={s['sica']:.1%}  SC={s['sc']:.1%}  (n={s['n']})")

    print("\n--- By Level ---")
    for lv, s in sorted(summary.get("per_level_accuracy", {}).items()):
        print(f"  Level {lv:>3s}: SICA={s['sica']:.1%}  SC={s['sc']:.1%}  (n={s['n']})")
    print("=" * 80)


def main():
    parser = argparse.ArgumentParser(description="SICA Full MVP Experiment (60 problems)")
    parser.add_argument("--mode", choices=["mock", "vllm", "api"], default="vllm")
    parser.add_argument("--k", type=int, default=12)
    parser.add_argument("--model", type=str, default="auto")
    parser.add_argument("--api-base", type=str, default="http://localhost:8000/v1")
    parser.add_argument("--api-key", type=str, default="EMPTY")
    parser.add_argument("--math-data", type=str, default="data/math500_subset.json")
    parser.add_argument("--pw-data", type=str, default="data/proofwriter_subset.json")
    parser.add_argument("--output", type=str, default="results/mvp_full_results.json")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    args = parser.parse_args()

    logger.info("SICA Full MVP | mode=%s k=%d resume=%s", args.mode, args.k, args.resume)

    problems = load_all_problems(args.math_data, args.pw_data)

    completed_ids = set()
    completed_results = []
    if args.resume:
        checkpoint = load_checkpoint(args.output)
        if checkpoint and "results" in checkpoint:
            completed_results = checkpoint["results"]
            completed_ids = {r["problem_id"] for r in completed_results if "problem_id" in r}
            logger.info("Resuming: %d problems already completed", len(completed_ids))

    generator = build_generator(args)
    extractor = build_extractor(args)
    pipeline = SICAPipeline(trace_generator=generator, constraint_extractor=extractor, k=args.k)
    sc_baseline = SelfConsistency()

    all_results = list(completed_results)
    elapsed_times = []
    total_start = time.time()

    remaining = [(i, p) for i, p in enumerate(problems) if p["id"] not in completed_ids]
    logger.info("Running %d remaining problems (skipped %d)", len(remaining), len(completed_ids))

    for progress_idx, (i, prob) in enumerate(remaining):
        t0 = time.time()
        prob_id = prob["id"]
        dataset = prob.get("dataset", "math")
        level = prob.get("level", "unknown")

        print(f"\n--- [{progress_idx+1}/{len(remaining)}] (overall {i+1}/{len(problems)}) ---")
        print(f"ID: {prob_id} | Dataset: {dataset} | Level: {level}")
        print(f"Q: {prob['problem'][:120]}...")
        print(f"GT: {prob['answer']}")
        sys.stdout.flush()

        try:
            sica_result = pipeline.run_single(prob)
            sica_answer = sica_result.get("answer", "")
            sica_correct = is_equiv(sica_answer, prob["answer"])

            cs = sica_result.get("constraints_stats", {})
            ms = sica_result.get("maxsat_stats", {})
            timing = sica_result.get("timing", {})

            print(f"SICA: {sica_answer} ({'V' if sica_correct else 'X'})")
            print(f"  Constraints: {cs.get('total_extracted',0)} extracted -> {cs.get('unique_after_dedup',0)} unique")
            print(f"  MaxSAT: {ms.get('satisfied',0)} sat, {ms.get('excluded',0)} excl, solve={ms.get('solve_time_ms',0)}ms")
            print(f"  Timing: trace={timing.get('trace_gen_s',0):.1f}s extract={timing.get('extraction_s',0):.1f}s total={timing.get('total_s',0):.1f}s")
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
            sc_result = sc_baseline.run(prob, traces=[t.get("trace","") for t in traces], answers=answers)
            sc_answer = sc_result.get("answer", "")
            sc_correct = is_equiv(sc_answer, prob["answer"])
            print(f"SC:   {sc_answer} ({'V' if sc_correct else 'X'}) -- votes: {sc_result.get('vote_count','?')}/{len(traces)}")
        except Exception as e:
            logger.error("SC error on %s: %s", prob_id, e)
            sc_answer = ""
            sc_correct = False
            sc_result = {"vote_count": 0, "vote_distribution": {}}

        elapsed = time.time() - t0
        elapsed_times.append(elapsed)
        print(f"Time: {elapsed:.1f}s")

        avg_time = sum(elapsed_times) / len(elapsed_times)
        remaining_count = len(remaining) - (progress_idx + 1)
        eta_s = avg_time * remaining_count
        if remaining_count > 0:
            eta_min = eta_s / 60
            print(f"ETA: {eta_min:.1f} min ({remaining_count} remaining, avg {avg_time:.1f}s/prob)")

        sys.stdout.flush()

        result_entry = {
            "problem_idx": i,
            "problem_id": prob_id,
            "problem": prob["problem"],
            "dataset": dataset,
            "level": level,
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

        summary = compute_summary(all_results, extractor.stats)
        summary["k"] = args.k
        summary["mode"] = args.mode
        summary["total_wall_time_s"] = round(time.time() - total_start, 1)
        output = {"summary": summary, "results": all_results}
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2, default=str)

    total_wall = time.time() - total_start
    summary = compute_summary(all_results, extractor.stats)
    summary["k"] = args.k
    summary["mode"] = args.mode
    summary["total_wall_time_s"] = round(total_wall, 1)

    output = {"summary": summary, "results": all_results}
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print_summary(summary)
    print(f"\nTotal wall time: {total_wall/60:.1f} min")
    print(f"Results saved to {args.output}")
    print("FULL_MVP_DONE")


if __name__ == "__main__":
    main()

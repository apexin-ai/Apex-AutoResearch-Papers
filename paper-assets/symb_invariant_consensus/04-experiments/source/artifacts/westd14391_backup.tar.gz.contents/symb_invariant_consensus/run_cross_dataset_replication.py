"""
Cross-dataset replication: run SC, SICA, and Selective Abstention on ProofWriter/LogiQA.
Validates generalizability beyond FOLIO.

Usage:
  python run_cross_dataset_replication.py --dataset proofwriter --data-path data/proofwriter_30.json --k 12 --vllm-port 8020
  python run_cross_dataset_replication.py --dataset logiqa --data-path data/logiqa_30.json --k 12 --vllm-port 8020
  python run_cross_dataset_replication.py --dataset proofwriter --data-path data/proofwriter_30.json --k 4 --n-questions 3 --vllm-port 8020 --output results/cross_dataset/proofwriter/pilot.json
"""
from __future__ import annotations

import argparse
import json
import logging
import math
import os
import sys
import time
from collections import Counter

from sica.constraint_extractor import ConstraintExtractor, VLLMBackend
from sica.trace_generator import VLLMGenerator
from sica.pipeline import SICAPipeline, normalize_logic_answer, _group_logic_answers
from baselines.self_consistency import SelfConsistency
from utils.math_equiv import is_equiv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

DATASET_CONFIG = {
    "proofwriter": {
        "domain": "logic",
        "generator_domain": "logic",
        "answer_type": "tfu",  # True/False/Unknown
    },
    "logiqa": {
        "domain": "logic",
        "generator_domain": "multichoice",
        "answer_type": "abcd",
    },
}

LOGIC_SOLVE_PROMPT = """Determine whether the following statement is true, false, or unknown based on the given information. Show your step-by-step reasoning.
At the end, put your final answer in \\boxed{{}}, choosing from: True, False, or Unknown.

{problem}"""


def load_data(path: str, dataset: str) -> list[dict]:
    with open(path) as f:
        data = json.load(f)
    for p in data:
        p.setdefault("dataset", dataset)
    logger.info("Loaded %d %s problems from %s", len(data), dataset, path)
    return data


def compute_entropy(vote_dist: dict) -> float:
    total = sum(vote_dist.values())
    if total == 0:
        return 0.0
    entropy = 0.0
    for count in vote_dist.values():
        if count > 0:
            p = count / total
            entropy -= p * math.log2(p)
    return entropy


def selective_abstention(results: list[dict], threshold: float = 1.0) -> dict:
    """Apply selective abstention: abstain on high-entropy questions, report coverage + accuracy on retained."""
    retained = []
    abstained = []
    for r in results:
        vote_dist = r.get("sc_vote_distribution", {})
        entropy = compute_entropy(vote_dist)
        r["entropy"] = round(entropy, 4)
        if entropy <= threshold:
            retained.append(r)
        else:
            abstained.append(r)

    n_retained = len(retained)
    n_total = len(results)
    coverage = n_retained / n_total if n_total > 0 else 0.0

    correct = sum(1 for r in retained if r["sc_correct"])
    acc_retained = correct / n_retained if n_retained > 0 else 0.0

    return {
        "threshold": threshold,
        "coverage": round(coverage, 4),
        "n_retained": n_retained,
        "n_abstained": len(abstained),
        "accuracy_retained": round(acc_retained, 4),
        "abstained_ids": [r["problem_id"] for r in abstained],
    }


def mcnemar_test(results: list[dict], method_a: str, method_b: str) -> dict:
    """McNemar test between two methods."""
    b_count = 0  # A correct, B wrong
    c_count = 0  # A wrong, B correct
    for r in results:
        a_correct = r.get(f"{method_a}_correct", False)
        b_correct = r.get(f"{method_b}_correct", False)
        if a_correct and not b_correct:
            b_count += 1
        elif not a_correct and b_correct:
            c_count += 1

    n = b_count + c_count
    if n == 0:
        return {"chi2": 0.0, "p_value": 1.0, "b": b_count, "c": c_count, "n_discordant": n}

    chi2 = (abs(b_count - c_count) - 1) ** 2 / n if n > 0 else 0
    try:
        from scipy.stats import chi2 as chi2_dist
        p_value = 1 - chi2_dist.cdf(chi2, df=1)
    except ImportError:
        p_value = -1.0  # scipy not available

    return {
        "chi2": round(chi2, 4),
        "p_value": round(p_value, 6),
        "b": b_count,
        "c": c_count,
        "n_discordant": n,
    }


def check_correct(pred: str, gt: str, answer_type: str) -> bool:
    if answer_type == "tfu":
        norm_pred = normalize_logic_answer(pred) if pred else ""
        norm_gt = normalize_logic_answer(gt)
        return norm_pred == norm_gt
    elif answer_type == "abcd":
        return pred.strip().upper() == gt.strip().upper()
    return is_equiv(pred, gt)


def main():
    parser = argparse.ArgumentParser(description="Cross-dataset replication")
    parser.add_argument("--dataset", required=True, choices=list(DATASET_CONFIG.keys()))
    parser.add_argument("--data-path", required=True)
    parser.add_argument("--k", type=int, default=12)
    parser.add_argument("--n-questions", type=int, default=0, help="Limit to N questions (0=all)")
    parser.add_argument("--vllm-port", type=int, default=8020)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument("--methods", default="sc,sica,abstention")
    parser.add_argument("--abstention-threshold", type=float, default=1.0)
    parser.add_argument("--output", default="")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    config = DATASET_CONFIG[args.dataset]
    methods = [m.strip() for m in args.methods.split(",")]

    if not args.output:
        args.output = f"results/cross_dataset/{args.dataset}/results.json"

    problems = load_data(args.data_path, args.dataset)
    if args.n_questions > 0:
        problems = problems[:args.n_questions]
        logger.info("Limited to %d problems", len(problems))

    base_url = f"http://localhost:{args.vllm_port}/v1"

    generator = VLLMGenerator(
        base_url=base_url,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
    )
    generator.domain = config["generator_domain"]

    run_sica = "sica" in methods
    extractor = None
    pipeline = None
    if run_sica:
        extractor = ConstraintExtractor(llm=VLLMBackend(base_url=base_url))
        extractor.domain = config["domain"]
        pipeline = SICAPipeline(
            trace_generator=generator,
            constraint_extractor=extractor,
            k=args.k,
        )

    sc_baseline = SelfConsistency()

    # Resume support
    existing_results = []
    done_ids = set()
    if args.resume and os.path.exists(args.output):
        with open(args.output) as f:
            checkpoint = json.load(f)
        existing_results = checkpoint.get("results", [])
        done_ids = {r["problem_id"] for r in existing_results}
        logger.info("Resuming: %d already done", len(done_ids))

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)

    all_results = list(existing_results)
    elapsed_times = []
    total_start = time.time()

    remaining = [(i, p) for i, p in enumerate(problems) if p["id"] not in done_ids]
    logger.info("Processing %d problems (%d skipped)", len(remaining), len(done_ids))

    for progress_idx, (i, prob) in enumerate(remaining):
        prob_id = prob["id"]
        t0 = time.time()
        print(f"\n--- [{progress_idx+1}/{len(remaining)}] {prob_id} (gt={prob['answer']}) ---")

        # Generate traces (shared across methods)
        if run_sica:
            sica_result = pipeline.run_single(prob)
            traces = sica_result.get("traces", [])
            sica_answer = sica_result.get("answer", "")
            sica_correct = check_correct(sica_answer, prob["answer"], config["answer_type"])
            print(f"SICA: {sica_answer} ({'V' if sica_correct else 'X'}) -- scores: {sica_result.get('scores', {})}")
        else:
            traces = generator.generate(prob["problem"], k=args.k)
            sica_answer = ""
            sica_correct = False
            sica_result = {}

        # SC
        answers = [t.get("answer", "") for t in traces]
        sc_result = sc_baseline.run(prob, traces=[t.get("trace", "") for t in traces], answers=answers)
        sc_answer = sc_result.get("answer", "")
        sc_correct = check_correct(sc_answer, prob["answer"], config["answer_type"])
        print(f"SC:   {sc_answer} ({'V' if sc_correct else 'X'}) -- votes: {sc_result.get('vote_count', '?')}/{len(traces)}")

        elapsed = time.time() - t0
        elapsed_times.append(elapsed)

        remaining_count = len(remaining) - (progress_idx + 1)
        if remaining_count > 0:
            avg_time = sum(elapsed_times) / len(elapsed_times)
            eta_min = avg_time * remaining_count / 60
            print(f"Time: {elapsed:.1f}s | ETA: {eta_min:.1f} min ({remaining_count} remaining)")

        result_entry = {
            "problem_idx": i,
            "problem_id": prob_id,
            "dataset": args.dataset,
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
            "wall_time_s": round(elapsed, 2),
        }
        all_results.append(result_entry)

        # Checkpoint
        _save_checkpoint(args, config, methods, all_results, total_start)

    # Final summary
    _print_final_summary(args, config, methods, all_results, total_start)


def _save_checkpoint(args, config, methods, all_results, total_start):
    n = len(all_results)
    sica_acc = sum(1 for r in all_results if r["sica_correct"]) / n if n else 0
    sc_acc = sum(1 for r in all_results if r["sc_correct"]) / n if n else 0

    summary = {
        "dataset": args.dataset,
        "n": n,
        "k": args.k,
        "methods": methods,
        "sica_accuracy": round(sica_acc, 4),
        "sc_accuracy": round(sc_acc, 4),
        "delta_sica_sc": round(sica_acc - sc_acc, 4),
        "wall_time_s": round(time.time() - total_start, 1),
    }

    if "abstention" in methods:
        for threshold in [0.5, 0.75, 1.0, 1.25, 1.5]:
            abst = selective_abstention(all_results, threshold=threshold)
            summary[f"abstention_t{threshold}"] = abst

    mcnemar = mcnemar_test(all_results, "sica", "sc")
    summary["mcnemar_sica_vs_sc"] = mcnemar

    output = {"summary": summary, "results": all_results}
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, default=str)


def _print_final_summary(args, config, methods, all_results, total_start):
    n = len(all_results)
    if n == 0:
        print("No results.")
        return

    sica_acc = sum(1 for r in all_results if r["sica_correct"]) / n
    sc_acc = sum(1 for r in all_results if r["sc_correct"]) / n

    print(f"\n{'='*60}")
    print(f"CROSS-DATASET RESULTS: {args.dataset.upper()} ({n} problems, K={args.k})")
    print(f"  SC:    {sc_acc:.4f} ({sum(1 for r in all_results if r['sc_correct'])}/{n})")
    if "sica" in methods:
        print(f"  SICA:  {sica_acc:.4f} ({sum(1 for r in all_results if r['sica_correct'])}/{n})")
        print(f"  Delta: {sica_acc - sc_acc:+.4f}")

    if "abstention" in methods:
        print(f"\n  Selective Abstention (SC-based):")
        for threshold in [0.5, 0.75, 1.0, 1.25, 1.5]:
            abst = selective_abstention(all_results, threshold=threshold)
            print(f"    t={threshold}: coverage={abst['coverage']:.2f} acc={abst['accuracy_retained']:.4f} (n={abst['n_retained']})")

    mcnemar = mcnemar_test(all_results, "sica", "sc")
    if mcnemar["n_discordant"] > 0:
        print(f"\n  McNemar SICA vs SC: chi2={mcnemar['chi2']:.2f} p={mcnemar['p_value']:.4f} (b={mcnemar['b']}, c={mcnemar['c']})")

    print(f"  Wall: {(time.time() - total_start)/60:.1f} min")
    print(f"  Output: {args.output}")
    print("CROSS_DATASET_DONE")


if __name__ == "__main__":
    main()

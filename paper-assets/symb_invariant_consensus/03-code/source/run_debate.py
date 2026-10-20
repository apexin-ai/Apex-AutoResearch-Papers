"""
Debate-Augmented Extraction Pipeline for FOLIO.

Core idea: same model plays Proposer and Critic in a 3-round debate,
producing diverse reasoning from which FOL constraints are extracted.
This addresses the independence problem in standard SICA where all SC
traces come from the same source distribution.

Four phases:
  Phase 1 — SC voting: generate K traces, majority-vote (reuses existing logic)
  Phase 2 — Debate: N_debates independent 3-round debates per problem
            (proposer -> critic -> proposer defense)
  Phase 3 — FOL extraction: extract constraints from enriched debate traces
  Phase 4 — MAX-SAT scoring: debate constraints score candidates via InvariantScorer

When critic fails to produce valid disagreement across ALL debates for a
problem, the pipeline falls back to standard SICA (FOL from SC traces).

Usage:
  python run_debate.py --mode vllm --k 12 --n-debates 3 --temperature 0.7 --seed 42 \
    --api-base http://localhost:8000/v1 --model auto \
    --data data/folio_full.json \
    --output results/exp076_debate/results.json \
    --save-intermediates
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import time
from collections import Counter

from sica.trace_generator import VLLMGenerator, MockGenerator
from sica.constraint_extractor import ConstraintExtractor, VLLMBackend, MockLLM
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver
from sica.pipeline import normalize_logic_answer, _group_logic_answers
from sica.scorer import InvariantScorer
from baselines.self_consistency import SelfConsistency

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Debate prompts: 3-round (proposer -> critic -> proposer defense)
# ---------------------------------------------------------------------------

PROPOSER_PROMPT = """\
Problem: {problem_text}

Provide your answer with detailed logical reasoning. Explain step by step."""

CRITIC_PROMPT = """\
Problem: {problem_text}

Another reasoner gave this answer and reasoning:
{proposer_response}

You MUST disagree. Find flaws in this reasoning and argue for a DIFFERENT answer. Be specific about logical errors."""

DEFENSE_PROMPT = """\
Problem: {problem_text}

Your original reasoning: {proposer_response}
Critic's objection: {critic_response}

Respond to the criticism. Either defend your original answer with stronger arguments, or revise your answer if the criticism is valid."""

# ---------------------------------------------------------------------------
# Answer extraction from free-form debate text
# ---------------------------------------------------------------------------

_ANSWER_PATTERNS = [
    re.compile(r'(?:the\s+)?(?:final\s+)?answer\s+is[:\s]*\b(true|false|unknown|uncertain)\b', re.I),
    re.compile(r'(?:conclusion|therefore|thus|hence)[:\s]*.*?\b(true|false|unknown|uncertain)\b', re.I),
]


def _strip_thinking(text: str) -> str:
    """Remove <think>...</think> blocks from model output."""
    idx = text.find('</think>')
    if idx != -1:
        return text[idx + len('</think>'):].strip()
    idx = text.find('<think>')
    if idx != -1:
        return ''
    return text


def extract_debate_answer(text: str) -> str:
    """Extract True/False/Unknown from free-form debate response text."""
    clean = _strip_thinking(text)
    if not clean:
        clean = text

    # Try \boxed{} first (model might use it)
    boxed = re.findall(r'\\boxed\{([^}]*)\}', clean)
    if boxed:
        return normalize_logic_answer(boxed[-1])

    # Try structured patterns (last match wins — closer to final answer)
    for pattern in _ANSWER_PATTERNS:
        matches = pattern.findall(clean)
        if matches:
            return normalize_logic_answer(matches[-1])

    # Fallback: scan last 300 chars for True/False/Unknown
    tail = clean[-300:].lower()
    for label in ["unknown", "uncertain", "false", "true"]:
        if label in tail:
            return normalize_logic_answer(label)

    return ""


def critic_disagrees(proposer_answer: str, critic_text: str) -> bool:
    """Check if critic produced a different answer than proposer."""
    critic_answer = extract_debate_answer(critic_text)
    if not critic_answer or not proposer_answer:
        return False
    return critic_answer != proposer_answer


# ---------------------------------------------------------------------------
# Single debate execution
# ---------------------------------------------------------------------------

def run_single_debate(llm, problem_text: str, debate_idx: int) -> dict:
    """Execute one 3-round debate. Returns enriched trace + metadata."""
    # Round 1: Proposer
    prompt_r1 = PROPOSER_PROMPT.format(problem_text=problem_text)
    proposer_response = llm.call(prompt_r1)
    proposer_answer = extract_debate_answer(proposer_response)

    # Round 2: Critic (forced disagreement)
    prompt_r2 = CRITIC_PROMPT.format(
        problem_text=problem_text,
        proposer_response=proposer_response,
    )
    critic_response = llm.call(prompt_r2)
    critic_answer = extract_debate_answer(critic_response)

    valid = critic_disagrees(proposer_answer, critic_response)

    # Round 3: Proposer defense
    prompt_r3 = DEFENSE_PROMPT.format(
        problem_text=problem_text,
        proposer_response=proposer_response,
        critic_response=critic_response,
    )
    defense_response = llm.call(prompt_r3)
    defense_answer = extract_debate_answer(defense_response)

    # Enriched trace: concatenation of all 3 rounds
    enriched_trace = (
        f"=== Proposer (Round 1) ===\n{proposer_response}\n\n"
        f"=== Critic (Round 2) ===\n{critic_response}\n\n"
        f"=== Proposer Defense (Round 3) ===\n{defense_response}"
    )

    # Final answer: defense > proposer > empty
    final_answer = defense_answer or proposer_answer or ""

    return {
        "debate_idx": debate_idx,
        "enriched_trace": enriched_trace,
        "answer": final_answer,
        "proposer_answer": proposer_answer,
        "critic_answer": critic_answer,
        "defense_answer": defense_answer,
        "valid_debate": valid,
        "proposer_response": proposer_response,
        "critic_response": critic_response,
        "defense_response": defense_response,
    }


# ---------------------------------------------------------------------------
# Component builders
# ---------------------------------------------------------------------------

def build_generator(args):
    """Build trace generator for Phase 1 SC traces."""
    if args.mode == "mock":
        gen = MockGenerator()
        gen.domain = "math"
        return gen
    elif args.mode == "vllm":
        gen = VLLMGenerator(
            base_url=args.api_base,
            api_key=[REDACTED],
            model=args.model if args.model != "auto" else None,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
        )
        gen.domain = "math"
        return gen
    raise ValueError(f"Unknown mode: {args.mode}")


def build_debate_llm(args):
    """Build LLM backend for debate rounds."""
    if args.mode == "mock":
        return MockLLM(domain="logic")
    elif args.mode == "vllm":
        return VLLMBackend(
            base_url=args.api_base,
            model=args.model if args.model != "auto" else None,
            max_tokens=args.max_tokens,
        )
    raise ValueError(f"Unknown mode: {args.mode}")


def build_extractor(args):
    """Build constraint extractor (logic domain for FOLIO FOL extraction)."""
    if args.mode == "mock":
        return ConstraintExtractor(llm=MockLLM(domain="logic"), domain="logic")
    elif args.mode == "vllm":
        return ConstraintExtractor(
            llm=VLLMBackend(
                base_url=args.api_base,
                model=args.model if args.model != "auto" else None,
                max_tokens=args.max_tokens,
            ),
            domain="logic",
        )
    raise ValueError(f"Unknown mode: {args.mode}")


def sc_vote(problem: dict, traces: list[dict]) -> dict:
    """Run SC majority voting on traces."""
    sc = SelfConsistency()
    answers = [t.get("answer", "") for t in traces]
    trace_texts = [t.get("trace", "") for t in traces]
    return sc.run(problem, trace_texts, answers)


# ---------------------------------------------------------------------------
# Per-problem pipeline
# ---------------------------------------------------------------------------

def process_single(
    problem: dict,
    generator,
    debate_llm,
    extractor: ConstraintExtractor,
    deduplicator: ConstraintDeduplicator,
    solver: MaxSATSolver,
    scorer: InvariantScorer,
    args,
) -> dict:
    """Run the full 4-phase debate pipeline on a single FOLIO problem."""
    t_start = time.perf_counter()
    problem_text = problem["problem"]

    # ---- Phase 1: Generate K SC traces + vote ----
    t0 = time.perf_counter()
    traces = generator.generate(problem_text, k=args.k)
    trace_time = time.perf_counter() - t0

    for t in traces:
        t["answer"] = normalize_logic_answer(t.get("answer", ""))

    sc_result = sc_vote(problem, traces)
    sc_answer = sc_result["answer"]
    answer_counts = Counter(t["answer"] for t in traces if t.get("answer"))
    candidates = sorted(set(t["answer"] for t in traces if t.get("answer")))

    # ---- Phase 2: Debate ----
    t0 = time.perf_counter()
    debates = []
    for d_idx in range(args.n_debates):
        debate = run_single_debate(debate_llm, problem_text, d_idx)
        debate["answer"] = normalize_logic_answer(debate["answer"])
        debates.append(debate)
    debate_time = time.perf_counter() - t0

    valid_debates = [d for d in debates if d["valid_debate"]]
    n_valid = len(valid_debates)
    use_fallback = (n_valid == 0)

    # ---- Phase 3: FOL extraction ----
    t0 = time.perf_counter()
    if use_fallback:
        # No valid debates — fall back to standard SICA (extract from SC traces)
        logger.info("No valid debates, falling back to SC trace extraction")
        source_traces = [{"trace": t["trace"], "answer": t["answer"],
                          "trace_idx": i} for i, t in enumerate(traces)]
        all_constraints = extractor.extract_batch([s["trace"] for s in source_traces])
    else:
        # Extract from enriched debate traces (only valid ones)
        source_traces = [{"trace": d["enriched_trace"], "answer": d["answer"],
                          "trace_idx": i} for i, d in enumerate(valid_debates)]
        all_constraints = extractor.extract_batch([s["trace"] for s in source_traces])
    extract_time = time.perf_counter() - t0

    total_raw_constraints = sum(len(c) for c in all_constraints)

    # ---- Phase 4: MAX-SAT scoring ----
    t0 = time.perf_counter()

    unique_constraints = deduplicator.deduplicate(all_constraints)

    maxsat_result = solver.solve(
        unique_constraints, timeout_ms=args.maxsat_timeout
    )

    # Merge candidate sets: SC candidates + debate answers
    debate_answers = set(d["answer"] for d in debates if d["answer"])
    all_candidates = sorted(set(candidates) | debate_answers)
    if not all_candidates:
        all_candidates = candidates if candidates else [""]

    # Score using source_traces (debate or SC fallback)
    source_answer_counts = Counter(s["answer"] for s in source_traces if s["answer"])
    scores = scorer.score(maxsat_result, source_traces, all_candidates)
    debate_answer = scorer.select_answer(scores, source_answer_counts)

    maxsat_time = time.perf_counter() - t0
    total_time = time.perf_counter() - t_start

    return {
        "debate_answer": debate_answer,
        "sc_answer": sc_answer,
        "candidates": all_candidates,
        "sc_vote_distribution": sc_result.get("vote_distribution", {}),
        "debate_scores": scores,
        "n_debates": args.n_debates,
        "n_valid_debates": n_valid,
        "used_fallback": use_fallback,
        "constraints_from_debate": total_raw_constraints,
        "constraints_unique": len(unique_constraints),
        "maxsat_stats": {
            "satisfied": len(maxsat_result.satisfied),
            "excluded": len(maxsat_result.excluded),
            "total_weight": maxsat_result.total_weight,
            "solve_time_ms": maxsat_result.solve_time_ms,
        },
        "timing": {
            "trace_gen_s": round(trace_time, 3),
            "debate_s": round(debate_time, 3),
            "extraction_s": round(extract_time, 3),
            "maxsat_s": round(maxsat_time, 3),
            "total_s": round(total_time, 3),
        },
        "debates": debates,
        "traces": traces,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Debate-Augmented Extraction Pipeline for FOLIO"
    )
    parser.add_argument("--mode", choices=["vllm", "mock"], default="vllm")
    parser.add_argument("--k", type=int, default=12,
                        help="Number of SC traces (Phase 1)")
    parser.add_argument("--n-debates", type=int, default=3,
                        help="Number of independent debates per problem (Phase 2)")
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--api-base", default="http://localhost:8000/v1")
    parser.add_argument("--api-key", default="EMPTY")
    parser.add_argument("--model", default="auto")
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument("--maxsat-timeout", type=int, default=10000,
                        help="MAX-SAT solver timeout in ms")
    parser.add_argument("--data", required=True,
                        help="Path to FOLIO dataset JSON")
    parser.add_argument("--output", required=True,
                        help="Output JSON path")
    parser.add_argument("--save-intermediates", action="store_true")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--limit", type=int, default=0,
                        help="Limit to N problems (0 = all)")
    args = parser.parse_args()

    # Load data
    with open(args.data) as f:
        problems = json.load(f)
    for p in problems:
        p.setdefault("dataset", "folio")

    if args.limit > 0:
        problems = problems[:args.limit]
    logger.info("Loaded %d problems from %s", len(problems), args.data)

    # Build components
    generator = build_generator(args)
    debate_llm = build_debate_llm(args)
    extractor = build_extractor(args)
    deduplicator = ConstraintDeduplicator()
    solver = MaxSATSolver()
    scorer = InvariantScorer()

    # Resume support
    all_results = []
    done_ids = set()
    if args.resume and os.path.exists(args.output):
        with open(args.output) as f:
            prev = json.load(f)
        all_results = prev.get("results", [])
        done_ids = {r["problem_id"] for r in all_results}
        logger.info("Resuming: %d problems already done", len(done_ids))

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)

    total_start = time.time()
    elapsed_times = []

    for idx, problem in enumerate(problems):
        prob_id = problem.get("id", f"prob_{idx}")
        if prob_id in done_ids:
            continue

        t0 = time.time()
        logger.info("[%d/%d] Processing %s", idx + 1, len(problems), prob_id)

        try:
            result = process_single(
                problem, generator, debate_llm, extractor,
                deduplicator, solver, scorer, args,
            )
        except Exception as e:
            logger.error("Error on %s: %s", prob_id, e, exc_info=True)
            result = {
                "debate_answer": "", "sc_answer": "",
                "candidates": [], "debate_scores": {},
                "n_debates": args.n_debates, "n_valid_debates": 0,
                "used_fallback": True,
                "constraints_from_debate": 0, "constraints_unique": 0,
                "error": str(e)[:500], "timing": {},
                "debates": [], "traces": [],
            }

        gt = normalize_logic_answer(problem["answer"])
        debate_correct = (result["debate_answer"] == gt)
        sc_correct = (result.get("sc_answer", "") == gt)

        elapsed = time.time() - t0
        elapsed_times.append(elapsed)

        print(f"  GT: {gt}")
        print(f"  Debate: {result['debate_answer']} "
              f"({'V' if debate_correct else 'X'})  "
              f"scores={result.get('debate_scores', {})}")
        print(f"  SC:     {result.get('sc_answer', '')} "
              f"({'V' if sc_correct else 'X'})  "
              f"votes={result.get('sc_vote_distribution', {})}")
        print(f"  Valid debates: {result.get('n_valid_debates', 0)}/{args.n_debates}"
              f"  fallback={result.get('used_fallback', False)}")
        print(f"  Constraints: {result.get('constraints_from_debate', 0)} raw, "
              f"{result.get('constraints_unique', 0)} unique")
        print(f"  Time: {elapsed:.1f}s")

        if elapsed_times:
            avg_time = sum(elapsed_times) / len(elapsed_times)
            remaining = len(problems) - (idx + 1)
            if remaining > 0:
                eta = avg_time * remaining / 60
                print(f"  ETA: {eta:.1f} min ({remaining} remaining)")

        sys.stdout.flush()

        # Build result entry (exclude raw debate/trace text from main results)
        result_entry = {
            "problem_idx": idx,
            "problem_id": prob_id,
            "problem": problem["problem"],
            "dataset": "folio",
            "ground_truth": gt,
            "debate_answer": result["debate_answer"],
            "debate_correct": debate_correct,
            "sc_answer": result.get("sc_answer", ""),
            "sc_correct": sc_correct,
            "candidates": result.get("candidates", []),
            "sc_vote_distribution": result.get("sc_vote_distribution", {}),
            "debate_scores": result.get("debate_scores", {}),
            "n_debates": args.n_debates,
            "n_valid_debates": result.get("n_valid_debates", 0),
            "used_fallback": result.get("used_fallback", False),
            "constraints_from_debate": result.get("constraints_from_debate", 0),
            "constraints_unique": result.get("constraints_unique", 0),
            "maxsat_stats": result.get("maxsat_stats", {}),
            "timing": result.get("timing", {}),
        }
        if result.get("error"):
            result_entry["error"] = result["error"]
        all_results.append(result_entry)

        # Save intermediates (full debate transcripts + traces)
        if args.save_intermediates:
            intermed_dir = os.path.join(
                os.path.dirname(args.output) or ".", "intermediates"
            )
            os.makedirs(intermed_dir, exist_ok=True)
            intermed_data = {
                "problem": problem,
                "debates": [
                    {
                        "debate_idx": d["debate_idx"],
                        "proposer_answer": d["proposer_answer"],
                        "critic_answer": d["critic_answer"],
                        "defense_answer": d["defense_answer"],
                        "valid_debate": d["valid_debate"],
                        "proposer_response": d["proposer_response"],
                        "critic_response": d["critic_response"],
                        "defense_response": d["defense_response"],
                        "enriched_trace": d["enriched_trace"],
                    }
                    for d in result.get("debates", [])
                ],
                "traces": result.get("traces", []),
                "debate_scores": result.get("debate_scores", {}),
            }
            with open(os.path.join(intermed_dir, f"{prob_id}.json"), "w") as f:
                json.dump(intermed_data, f, indent=2, default=str)

        # Checkpoint results to disk
        n = len(all_results)
        d_acc = sum(1 for r in all_results if r["debate_correct"]) / n
        sc_acc = sum(1 for r in all_results if r["sc_correct"]) / n
        summary = {
            "n": n,
            "debate_accuracy": round(d_acc, 4),
            "sc_accuracy": round(sc_acc, 4),
            "delta": round(d_acc - sc_acc, 4),
            "k": args.k,
            "n_debates": args.n_debates,
            "temperature": args.temperature,
            "mode": args.mode,
            "seed": args.seed,
            "total_wall_time_s": round(time.time() - total_start, 1),
            "total_debate_constraints": sum(
                r["constraints_from_debate"] for r in all_results
            ),
            "fallback_count": sum(
                1 for r in all_results if r.get("used_fallback")
            ),
        }
        output = {"summary": summary, "results": all_results}
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2, default=str)

    # Final summary
    n = len(all_results)
    if n > 0:
        d_acc = sum(1 for r in all_results if r["debate_correct"]) / n
        sc_acc = sum(1 for r in all_results if r["sc_correct"]) / n
        total_wall = time.time() - total_start
        print(f"\n{'='*60}")
        print(f"FINAL RESULTS ({n} problems)")
        print(f"  Debate:    {d_acc:.4f} "
              f"({sum(1 for r in all_results if r['debate_correct'])}/{n})")
        print(f"  SC:        {sc_acc:.4f} "
              f"({sum(1 for r in all_results if r['sc_correct'])}/{n})")
        print(f"  Delta:     {d_acc - sc_acc:+.4f}")
        print(f"  Fallbacks: "
              f"{sum(1 for r in all_results if r.get('used_fallback'))}/{n}")
        print(f"  Constraints: "
              f"{sum(r['constraints_from_debate'] for r in all_results)} total")
        print(f"  Wall time: {total_wall/60:.1f} min")
        print(f"Results saved to {args.output}")

    print("DEBATE_PIPELINE_DONE")


if __name__ == "__main__":
    main()

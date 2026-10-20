"""
Contrastive Constraint Generation Pipeline for FOLIO.

Instead of extracting constraints from same-source SC traces (which lack
independence), this pipeline generates PRO and CON constraints for each
candidate answer independently via targeted LLM prompts, then uses
contrastive MAX-SAT scoring to select the best answer.

Three phases:
  Phase 1 — SC voting: generate K traces, majority-vote to get candidate set
  Phase 2 — Contrastive constraint generation: for each candidate, prompt the
            LLM K_contrast times to produce supporting (pro) and refuting (con)
            FOL constraints
  Phase 3 — Contrastive MAX-SAT scoring: score = MAX-SAT(pro) - α·MAX-SAT(con)

Usage:
  python run_contrastive.py --mode vllm --k 12 --k-contrast 3 --temperature 0.7 --seed 42 \
    --api-base http://localhost:8000/v1 --model auto \
    --data data/folio_full.json \
    --output results/exp075_contrastive/results.json \
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

from sica.trace_generator import VLLMGenerator, MockGenerator, extract_boxed_answer
from sica.constraint_extractor import VLLMBackend, MockLLM, ConstraintExtractor
from sica.z3_maxsat import (
    ConstraintDeduplicator, MaxSATSolver, parse_z3_formula, UniqueConstraint,
)
from sica.pipeline import normalize_logic_answer, _group_logic_answers
from baselines.self_consistency import SelfConsistency

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Contrastive constraint generation prompt
# ---------------------------------------------------------------------------

CONTRASTIVE_PROMPT = '''\
You are a formal logic expert. Given a logic problem and a candidate answer, \
generate logical constraints that must hold if the answer is CORRECT (pro) \
and constraints that must hold if the answer is WRONG (con).

Problem:
{problem_text}

Candidate answer: {candidate_answer}

Instructions:
1. List FOL constraints that SUPPORT this answer being correct (pro_constraints).
2. List FOL constraints that would hold if this answer is WRONG (con_constraints).
3. Express each constraint as a Z3-compatible boolean formula.

Variable naming:
- Unary property: property_entity (e.g., kind_anne, red_charlie)
- Binary relation: relation_subject_object (e.g., eats_bear_squirrel)
- Use lowercase with underscores only

Z3 operators: Implies(a, b), And(a, b, ...), Or(a, b, ...), Not(a), == True, == False

Output ONLY valid JSON:
{{"pro_constraints": [{{"expression": "human-readable", "z3_formula": "Z3 syntax"}}], \
"con_constraints": [{{"expression": "human-readable", "z3_formula": "Z3 syntax"}}]}}'''

CONTRASTIVE_PROMPT_LOGIQA = '''\
You are a logical reasoning expert. Given a multiple-choice logic problem and a candidate answer, \
generate logical constraints that must hold if the answer is CORRECT (pro) \
and constraints that must hold if the answer is WRONG (con).

Problem:
{problem_text}

Candidate answer: {candidate_answer}

Instructions:
1. List logical constraints that SUPPORT this answer being correct (pro_constraints).
2. List logical constraints that would hold if this answer is WRONG (con_constraints).
3. Express each constraint as a Z3-compatible boolean formula.

Variable naming:
- Use descriptive names: property_entity (e.g., young_teacher, female_over_middle_age)
- Binary relation: relation_subject_object
- Use lowercase with underscores only

Z3 operators: Implies(a, b), And(a, b, ...), Or(a, b, ...), Not(a), == True, == False

Output ONLY valid JSON:
{{"pro_constraints": [{{"expression": "human-readable", "z3_formula": "Z3 syntax"}}], \
"con_constraints": [{{"expression": "human-readable", "z3_formula": "Z3 syntax"}}]}}'''

# ---------------------------------------------------------------------------
# Contrastive constraint generator
# ---------------------------------------------------------------------------

def _strip_thinking(text: str) -> str:
    return re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()


def _extract_json_str(text: str) -> str | None:
    # Try to find JSON object
    for m in re.finditer(r'\{[\s\S]*\}', text):
        candidate = m.group()
        try:
            json.loads(candidate)
            return candidate
        except json.JSONDecodeError:
            continue
    return None


def _repair_json(s: str) -> str:
    # Fix trailing commas before } or ]
    s = re.sub(r',\s*([}\]])', r'\1', s)
    # Fix single quotes to double quotes
    s = s.replace("'", '"')
    return s


def parse_contrastive_response(raw: str) -> tuple[list[dict], list[dict]]:
    """Parse LLM response into (pro_constraints, con_constraints).
    Each constraint dict has 'expression' and 'z3_formula' keys.
    Returns empty lists on parse failure.
    """
    text = _strip_thinking(raw)
    if not text:
        return [], []

    json_str = _extract_json_str(text)
    if json_str is None:
        return [], []

    data = None
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        try:
            data = json.loads(_repair_json(json_str))
        except json.JSONDecodeError:
            return [], []

    pro_raw = data.get("pro_constraints", [])
    con_raw = data.get("con_constraints", [])

    def _validate(constraints: list) -> list[dict]:
        valid = []
        for c in constraints:
            if not isinstance(c, dict):
                continue
            z3f = c.get("z3_formula", "")
            if not z3f:
                continue
            # Verify parseable by z3
            parsed = parse_z3_formula(z3f)
            if parsed is None:
                continue
            valid.append({
                "expression": c.get("expression", z3f),
                "z3_formula": z3f,
            })
        return valid

    return _validate(pro_raw), _validate(con_raw)


def generate_contrastive_constraints(
    llm, problem_text: str, candidate: str, k_contrast: int = 3,
    dataset: str = "folio",
) -> tuple[list[dict], list[dict]]:
    """Call LLM k_contrast times for a candidate, aggregate pro/con constraints."""
    all_pro, all_con = [], []
    tmpl = CONTRASTIVE_PROMPT_LOGIQA if dataset == "logiqa" else CONTRASTIVE_PROMPT
    prompt = tmpl.format(
        problem_text=problem_text,
        candidate_answer=candidate,
    )
    for _ in range(k_contrast):
        raw = llm.call(prompt)
        pro, con = parse_contrastive_response(raw)
        all_pro.extend(pro)
        all_con.extend(con)
    return all_pro, all_con


# ---------------------------------------------------------------------------
# Contrastive MAX-SAT scoring
# ---------------------------------------------------------------------------

def _build_unique_constraints(constraints: list[dict]) -> list[UniqueConstraint]:
    """Convert raw constraint dicts to UniqueConstraint list via deduplication."""
    dedup = ConstraintDeduplicator()
    # Wrap as single-trace batch for the deduplicator
    return dedup.deduplicate([constraints])


def contrastive_score_candidate(
    pro_constraints: list[dict],
    con_constraints: list[dict],
    solver: MaxSATSolver,
    maxsat_timeout_ms: int = 10000,
) -> dict:
    """Score a single candidate: score = MAX-SAT(pro) - MAX-SAT(con).

    Returns dict with score, pro_satisfied, con_satisfied, and details.
    """
    # Deduplicate and solve pro constraints
    pro_unique = _build_unique_constraints(pro_constraints)
    if pro_unique:
        pro_result = solver.solve(pro_unique, timeout_ms=maxsat_timeout_ms)
        pro_sat_weight = pro_result.total_weight
        pro_n_sat = len(pro_result.satisfied)
    else:
        pro_sat_weight = 0.0
        pro_n_sat = 0

    # Deduplicate and solve con constraints
    con_unique = _build_unique_constraints(con_constraints)
    if con_unique:
        con_result = solver.solve(con_unique, timeout_ms=maxsat_timeout_ms)
        con_sat_weight = con_result.total_weight
        con_n_sat = len(con_result.satisfied)
    else:
        con_sat_weight = 0.0
        con_n_sat = 0

    n_pro = len(pro_unique)
    n_con = len(con_unique)
    raw_score = pro_sat_weight - con_sat_weight
    norm_pro = pro_sat_weight / max(n_pro, 1)
    norm_con = con_sat_weight / max(n_con, 1)
    score = norm_pro - norm_con

    return {
        "score": score,
        "raw_score": raw_score,
        "normalized_pro": norm_pro,
        "normalized_con": norm_con,
        "pro_satisfied_weight": pro_sat_weight,
        "con_satisfied_weight": con_sat_weight,
        "pro_n_satisfied": pro_n_sat,
        "con_n_satisfied": con_n_sat,
        "n_pro": n_pro,
        "n_con": n_con,
        "pro_n_raw": len(pro_constraints),
        "con_n_raw": len(con_constraints),
    }


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

def build_generator(args):
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
        # FOLIO uses standard solve prompt — the generator extracts boxed answers
        gen.domain = "math"
        return gen
    raise ValueError(f"Unknown mode: {args.mode}")


def build_llm(args):
    """Build LLM backend for contrastive constraint generation."""
    if args.mode == "mock":
        return MockLLM(domain="logic")
    elif args.mode == "vllm":
        return VLLMBackend(
            base_url=args.api_base,
            model=args.model if args.model != "auto" else None,
            max_tokens=args.max_tokens,
        )
    raise ValueError(f"Unknown mode: {args.mode}")


def sc_vote(problem: dict, traces: list[dict]) -> dict:
    """Run SC majority voting on traces."""
    sc = SelfConsistency()
    answers = [t.get("answer", "") for t in traces]
    trace_texts = [t.get("trace", "") for t in traces]
    return sc.run(problem, trace_texts, answers)


def process_single(
    problem: dict,
    generator,
    llm,
    solver: MaxSATSolver,
    args,
) -> dict:
    """Process a single problem through the full contrastive pipeline."""
    t_start = time.perf_counter()
    problem_text = problem["problem"]

    # --- Phase 1: Generate K traces + SC vote ---
    t0 = time.perf_counter()
    traces = generator.generate(problem_text, k=args.k)
    trace_time = time.perf_counter() - t0

    # Normalize answers
    dataset = getattr(args, "dataset", "folio")
    for t in traces:
        if t.get("answer"):
            if dataset == "logiqa":
                ans = t["answer"].strip()
                if ans and ans[0].upper() in "ABCD":
                    t["answer"] = ans[0].upper()
                else:
                    t["answer"] = ""
            else:
                t["answer"] = normalize_logic_answer(t["answer"])

    sc_result = sc_vote(problem, traces)
    sc_answer = sc_result["answer"]
    answer_counts = Counter(t["answer"] for t in traces if t.get("answer"))

    # Determine candidate set: all answers that got at least 1 vote
    candidates = sorted(set(t["answer"] for t in traces if t.get("answer")))

    # --- Degenerate case: single candidate ---
    if len(candidates) <= 1:
        total_time = time.perf_counter() - t_start
        only_answer = candidates[0] if candidates else ""
        return {
            "answer": only_answer,
            "sc_answer": sc_answer,
            "candidates": candidates,
            "answer_counts": dict(answer_counts),
            "contrastive_scores": {only_answer: 0.0} if only_answer else {},
            "pro_constraints_count": 0,
            "con_constraints_count": 0,
            "per_candidate_details": {},
            "degenerate": True,
            "timing": {
                "trace_gen_s": round(trace_time, 3),
                "contrastive_s": 0.0,
                "total_s": round(total_time, 3),
            },
            "traces": traces,
        }

    # --- Phase 2: Contrastive constraint generation per candidate ---
    t0 = time.perf_counter()
    per_candidate = {}  # candidate -> {pro: [...], con: [...], score_details: {...}}
    total_pro = 0
    total_con = 0

    dataset = getattr(args, "dataset", "folio")
    choice_map = {}
    if dataset == "logiqa" and "choices" in problem:
        for ch in problem["choices"]:
            if ch and len(ch) >= 1:
                choice_map[ch[0].upper()] = ch

    for cand in candidates:
        cand_display = choice_map.get(cand, cand) if dataset == "logiqa" else cand
        pro, con = generate_contrastive_constraints(
            llm, problem_text, cand_display, k_contrast=args.k_contrast,
            dataset=dataset,
        )
        per_candidate[cand] = {"pro": pro, "con": con}
        total_pro += len(pro)
        total_con += len(con)

    contrastive_time = time.perf_counter() - t0

    # --- Phase 3: Contrastive MAX-SAT scoring ---
    t0 = time.perf_counter()
    contrastive_scores = {}
    for cand in candidates:
        details = contrastive_score_candidate(
            per_candidate[cand]["pro"],
            per_candidate[cand]["con"],
            solver,
            maxsat_timeout_ms=args.maxsat_timeout,
        )
        per_candidate[cand]["score_details"] = details
        contrastive_scores[cand] = details["score"]

    scoring_time = time.perf_counter() - t0

    # Select answer: highest contrastive score, tie-break by SC vote count
    max_score = max(contrastive_scores.values())
    top = [a for a, s in contrastive_scores.items() if s == max_score]
    if len(top) == 1:
        contrastive_answer = top[0]
    else:
        contrastive_answer = max(top, key=lambda a: answer_counts.get(a, 0))

    total_time = time.perf_counter() - t_start

    # Build per_candidate_details for output (strip raw constraint content for brevity)
    details_out = {}
    for cand in candidates:
        d = per_candidate[cand]["score_details"]
        details_out[cand] = {
            "score": d["score"],
            "raw_score": d["raw_score"],
            "normalized_pro": d["normalized_pro"],
            "normalized_con": d["normalized_con"],
            "pro_satisfied_weight": d["pro_satisfied_weight"],
            "con_satisfied_weight": d["con_satisfied_weight"],
            "pro_n_raw": d["pro_n_raw"],
            "con_n_raw": d["con_n_raw"],
            "n_pro": d["n_pro"],
            "n_con": d["n_con"],
        }

    return {
        "answer": contrastive_answer,
        "sc_answer": sc_answer,
        "candidates": candidates,
        "answer_counts": dict(answer_counts),
        "contrastive_scores": contrastive_scores,
        "pro_constraints_count": total_pro,
        "con_constraints_count": total_con,
        "per_candidate_details": details_out,
        "degenerate": False,
        "timing": {
            "trace_gen_s": round(trace_time, 3),
            "contrastive_s": round(contrastive_time, 3),
            "scoring_s": round(scoring_time, 3),
            "total_s": round(total_time, 3),
        },
        "traces": traces,
        "per_candidate_constraints": {
            cand: {
                "pro": per_candidate[cand]["pro"],
                "con": per_candidate[cand]["con"],
            }
            for cand in candidates
        },
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Contrastive Constraint Generation Pipeline for FOLIO"
    )
    parser.add_argument("--data", default="data/folio_full.json",
                        help="Path to FOLIO dataset JSON")
    parser.add_argument("--output", default="results/exp075_contrastive/results.json")
    parser.add_argument("--mode", choices=["mock", "vllm"], default="vllm")
    parser.add_argument("--api-base", default="http://localhost:8000/v1")
    parser.add_argument("--api-key", default="EMPTY")
    parser.add_argument("--model", default="auto")
    parser.add_argument("--k", type=int, default=12,
                        help="Number of SC traces (Phase 1)")
    parser.add_argument("--k-contrast", type=int, default=3,
                        help="Number of contrastive samples per candidate (Phase 2)")
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument("--maxsat-timeout", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dataset", choices=["folio", "logiqa"], default="folio",
                        help="Dataset type: folio (3-class) or logiqa (4-choice)")
    parser.add_argument("--dry-run", type=int, default=0,
                        help="Process only N problems (0 = all)")
    parser.add_argument("--limit", type=int, default=0,
                        help="Limit to N problems (0 = all, alias for --dry-run)")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--save-intermediates", action="store_true")
    args = parser.parse_args()

    # Load data
    with open(args.data) as f:
        problems = json.load(f)
    for p in problems:
        p.setdefault("dataset", "folio")
    logger.info("Loaded %d problems from %s", len(problems), args.data)

    limit = args.limit if args.limit > 0 else args.dry_run
    if limit > 0:
        problems = problems[:limit]
        logger.info("Dry-run: processing %d problems", len(problems))

    # Build components
    generator = build_generator(args)
    if args.dataset == "logiqa":
        generator.domain = "multichoice"
    llm = build_llm(args)
    solver = MaxSATSolver()

    # Resume support
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    completed_ids = set()
    all_results = []
    if args.resume and os.path.exists(args.output):
        with open(args.output) as f:
            prev = json.load(f)
        all_results = prev.get("results", [])
        completed_ids = {r["problem_id"] for r in all_results}
        logger.info("Resumed: %d already completed", len(completed_ids))

    total_start = time.time()
    elapsed_times = []

    for idx, problem in enumerate(problems):
        prob_id = problem.get("id", f"prob_{idx}")
        if prob_id in completed_ids:
            continue

        t0 = time.time()
        print(f"\n[{idx+1}/{len(problems)}] {prob_id}", flush=True)

        try:
            result = process_single(problem, generator, llm, solver, args)
            contrastive_answer = result["answer"]
            sc_answer = result["sc_answer"]
            gt = normalize_logic_answer(problem["answer"])

            contrastive_correct = (contrastive_answer == gt)
            sc_correct = (sc_answer == gt)

            print(f"  Contrastive: {contrastive_answer} ({'V' if contrastive_correct else 'X'})")
            print(f"  SC baseline: {sc_answer} ({'V' if sc_correct else 'X'})")
            print(f"  Candidates:  {result['answer_counts']}")
            print(f"  Scores:      {result['contrastive_scores']}")
            if result["degenerate"]:
                print(f"  [degenerate: single candidate]")
            else:
                print(f"  Pro/Con:     {result['pro_constraints_count']}/{result['con_constraints_count']}")
        except Exception as e:
            logger.error("Error on %s: %s", prob_id, e)
            import traceback; traceback.print_exc()
            contrastive_answer = ""
            contrastive_correct = False
            sc_answer = ""
            sc_correct = False
            result = {
                "answer": "", "sc_answer": "", "candidates": [],
                "answer_counts": {}, "contrastive_scores": {},
                "pro_constraints_count": 0, "con_constraints_count": 0,
                "per_candidate_details": {}, "degenerate": False,
                "timing": {}, "traces": [],
            }

        elapsed = time.time() - t0
        elapsed_times.append(elapsed)
        print(f"  Time: {elapsed:.1f}s", flush=True)

        if elapsed_times:
            avg_t = sum(elapsed_times) / len(elapsed_times)
            remaining = len(problems) - (idx + 1)
            remaining -= len(completed_ids)
            if remaining > 0:
                print(f"  ETA: {avg_t * remaining / 60:.1f} min ({remaining} remaining)")

        # Build result entry (exclude traces and raw constraints from main results for size)
        result_entry = {
            "problem_idx": idx,
            "problem_id": prob_id,
            "problem": problem["problem"],
            "dataset": getattr(args, "dataset", "folio"),
            "ground_truth": normalize_logic_answer(problem["answer"]),
            "contrastive_answer": contrastive_answer,
            "contrastive_correct": contrastive_correct,
            "sc_answer": sc_answer,
            "sc_correct": sc_correct,
            "candidates": result.get("candidates", []),
            "answer_counts": result.get("answer_counts", {}),
            "contrastive_scores": result.get("contrastive_scores", {}),
            "pro_constraints_count": result.get("pro_constraints_count", 0),
            "con_constraints_count": result.get("con_constraints_count", 0),
            "per_candidate_details": result.get("per_candidate_details", {}),
            "degenerate": result.get("degenerate", False),
            "timing": result.get("timing", {}),
        }
        all_results.append(result_entry)

        # Save intermediates (full constraints + traces per problem)
        if args.save_intermediates:
            intermed_dir = os.path.join(
                os.path.dirname(args.output) or ".", "intermediates"
            )
            os.makedirs(intermed_dir, exist_ok=True)
            intermed_data = {
                "problem": problem,
                "traces": result.get("traces", []),
                "per_candidate_constraints": result.get("per_candidate_constraints", {}),
                "contrastive_scores": result.get("contrastive_scores", {}),
                "per_candidate_details": result.get("per_candidate_details", {}),
            }
            with open(os.path.join(intermed_dir, f"{prob_id}.json"), "w") as f:
                json.dump(intermed_data, f, indent=2, default=str)

        # Checkpoint
        n = len(all_results)
        c_acc = sum(1 for r in all_results if r["contrastive_correct"]) / n
        sc_acc = sum(1 for r in all_results if r["sc_correct"]) / n
        summary = {
            "n": n,
            "contrastive_accuracy": round(c_acc, 4),
            "sc_accuracy": round(sc_acc, 4),
            "delta": round(c_acc - sc_acc, 4),
            "k": args.k,
            "k_contrast": args.k_contrast,
            "temperature": args.temperature,
            "mode": args.mode,
            "seed": args.seed,
            "total_wall_time_s": round(time.time() - total_start, 1),
            "total_pro_constraints": sum(
                r["pro_constraints_count"] for r in all_results
            ),
            "total_con_constraints": sum(
                r["con_constraints_count"] for r in all_results
            ),
            "degenerate_count": sum(1 for r in all_results if r.get("degenerate")),
        }
        output = {"summary": summary, "results": all_results}
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2, default=str)

    # Final summary
    n = len(all_results)
    if n > 0:
        c_acc = sum(1 for r in all_results if r["contrastive_correct"]) / n
        sc_acc = sum(1 for r in all_results if r["sc_correct"]) / n
        total_wall = time.time() - total_start
        print(f"\n{'='*60}")
        print(f"FINAL RESULTS ({n} problems)")
        print(f"  Contrastive: {c_acc:.4f} ({sum(1 for r in all_results if r['contrastive_correct'])}/{n})")
        print(f"  SC baseline:  {sc_acc:.4f} ({sum(1 for r in all_results if r['sc_correct'])}/{n})")
        print(f"  Delta:        {c_acc - sc_acc:+.4f}")
        print(f"  Degenerate:   {sum(1 for r in all_results if r.get('degenerate'))}/{n}")
        print(f"  Pro total:    {sum(r['pro_constraints_count'] for r in all_results)}")
        print(f"  Con total:    {sum(r['con_constraints_count'] for r in all_results)}")
        print(f"  Wall time:    {total_wall/60:.1f} min")
        print(f"Results saved to {args.output}")

    print("CONTRASTIVE_PIPELINE_DONE")


if __name__ == "__main__":
    main()

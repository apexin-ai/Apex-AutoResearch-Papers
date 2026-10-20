"""
ICG (Independent Constraint Generation) Pipeline.

Core idea: generate FOL constraints independently from the problem text
(not from reasoning traces), then use MAX-SAT scoring to rerank SC candidates.
This ensures constraints are independent of the reasoning process.

Three phases:
  Phase 1: SC trace generation (K traces) -> majority vote baseline
  Phase 2: Independent constraint generation from premises (K_icg samplings, no solving)
  Phase 3: MAX-SAT scoring of SC candidate answers using independent constraints

Supports: FOLIO (True/False/Unknown) and LogiQA (A/B/C/D multiple choice).

Dependencies: sica.trace_generator, sica.z3_maxsat, sica.scorer,
              sica.pipeline (normalize_logic_answer, _group_logic_answers),
              baselines.self_consistency
"""
from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import re
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

import openai

from sica.trace_generator import VLLMGenerator, extract_boxed_answer
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver, parse_z3_formula
from sica.scorer import InvariantScorer
from sica.pipeline import normalize_logic_answer, _group_logic_answers
from baselines.self_consistency import SelfConsistency

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# ICG Prompt — few-shot examples improve Z3 format compliance on 7B models
# ---------------------------------------------------------------------------

ICG_PROMPT = """You are analyzing a logical reasoning problem. Do NOT solve it. Instead, identify the logical relationships and constraints that MUST hold based on the premises.

Here are two examples of the expected output format:

Example 1:
Problem: "All cats are animals. Tom is a cat. Determine whether: Tom is an animal."
{{"constraints": [{{"type": "rule", "expression": "All cats are animals", "z3_formula": "Implies(cat_tom, animal_tom)"}}, {{"type": "fact", "expression": "Tom is a cat", "z3_formula": "cat_tom == True"}}], "variables": ["cat_tom", "animal_tom"]}}

Example 2:
Problem: "If it rains, the ground is wet. If the ground is wet, the game is cancelled. It is raining. Determine whether: The game is cancelled."
{{"constraints": [{{"type": "rule", "expression": "Rain implies ground is wet", "z3_formula": "Implies(rains, ground_wet)"}}, {{"type": "rule", "expression": "Wet ground implies game cancelled", "z3_formula": "Implies(ground_wet, game_cancelled)"}}, {{"type": "fact", "expression": "It is raining", "z3_formula": "rains == True"}}], "variables": ["rains", "ground_wet", "game_cancelled"]}}

Now analyze this problem:

Problem:
{problem}

List the first-order logic constraints that are necessarily true based on the premises alone. For each constraint, provide:
- type: "fact" (direct assertion), "rule" (implication/conditional), or "derived" (entailment from combining premises)
- expression: human-readable description
- z3_formula: Z3-compatible boolean formula using these operators:
  * Implies(a, b) for if-then
  * And(a, b, ...) for conjunction
  * Or(a, b, ...) for disjunction
  * Not(a) for negation
  * == True / == False for assertions
  * Variable naming: property_entity (lowercase with underscores, e.g. kind_anne, eats_bear_squirrel)

Output ONLY valid JSON, nothing else:
{{"constraints": [{{"type": "...", "expression": "...", "z3_formula": "..."}}], "variables": ["var1", "var2"]}}

Important: focus ONLY on what the premises state. Do NOT derive the answer to the conclusion. Do NOT include any constraint about the conclusion's truth value."""


ICG_PROMPT_LOGIQA = """You are analyzing a multiple-choice logical reasoning problem. Do NOT solve it or determine which option is correct. Instead, identify the logical relationships and constraints that MUST hold based on the given context/premises.

Here are two examples of the expected output format:

Example 1:
Problem: "All cats are animals. Tom is a cat. Determine whether: Tom is an animal."
{{"constraints": [{{"type": "rule", "expression": "All cats are animals", "z3_formula": "Implies(cat_tom, animal_tom)"}}, {{"type": "fact", "expression": "Tom is a cat", "z3_formula": "cat_tom == True"}}], "variables": ["cat_tom", "animal_tom"]}}

Example 2:
Problem: "If it rains, the ground is wet. If the ground is wet, the game is cancelled. It is raining. Determine whether: The game is cancelled."
{{"constraints": [{{"type": "rule", "expression": "Rain implies ground is wet", "z3_formula": "Implies(rains, ground_wet)"}}, {{"type": "rule", "expression": "Wet ground implies game cancelled", "z3_formula": "Implies(ground_wet, game_cancelled)"}}, {{"type": "fact", "expression": "It is raining", "z3_formula": "rains == True"}}], "variables": ["rains", "ground_wet", "game_cancelled"]}}

Now analyze this problem:

Problem:
{problem}

List the first-order logic constraints that are necessarily true based on the context/premises alone. For each constraint, provide:
- type: "fact" (direct assertion), "rule" (implication/conditional), or "derived" (entailment from combining premises)
- expression: human-readable description
- z3_formula: Z3-compatible boolean formula using these operators:
  * Implies(a, b) for if-then
  * And(a, b, ...) for conjunction
  * Or(a, b, ...) for disjunction
  * Not(a) for negation
  * == True / == False for assertions
  * Variable naming: property_entity (lowercase with underscores, e.g. kind_anne, eats_bear_squirrel)

Output ONLY valid JSON, nothing else:
{{"constraints": [{{"type": "...", "expression": "...", "z3_formula": "..."}}], "variables": ["var1", "var2"]}}

Important: focus ONLY on what the context/premises state. Do NOT determine which answer option (A/B/C/D) is correct. Do NOT include constraints about the truth value of any specific answer option."""


# ---------------------------------------------------------------------------
# ICG Generator: independent constraint generation via LLM
# ---------------------------------------------------------------------------

class ICGGenerator:
    """Generate FOL constraints independently from problem text."""

    def __init__(self, base_url: str, model: str | None = None,
                 temperature: float = 0.7, max_tokens: int = 2048,
                 max_retries: int = 3):
        self.client = openai.OpenAI(base_url=base_url, api_key="[REDACTED]")
        self.async_client = openai.AsyncOpenAI(base_url=base_url, api_key="[REDACTED]")
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.max_retries = max_retries
        self.dataset = "folio"
        if model:
            self.model = model
        else:
            models = self.client.models.list()
            self.model = models.data[0].id
            logger.info("ICG auto-detected model: %s", self.model)

    @staticmethod
    def _strip_thinking(text: str) -> str:
        return re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()

    @staticmethod
    def _extract_json(text: str) -> dict | None:
        text = ICGGenerator._strip_thinking(text)
        # Strip markdown code fences that 7B models often emit
        text = re.sub(r'```(?:json)?\s*', '', text)
        text = re.sub(r'```\s*$', '', text)
        json_match = re.search(r'\{[\s\S]*\}', text)
        if not json_match:
            return None
        raw = json_match.group()
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            # Trailing comma fix
            raw_fixed = re.sub(r',\s*}', '}', raw)
            raw_fixed = re.sub(r',\s*]', ']', raw_fixed)
            try:
                return json.loads(raw_fixed)
            except json.JSONDecodeError:
                return None

    @staticmethod
    def _normalize_z3_formula(formula: str) -> str:
        """Normalize common LLM z3_formula variants before parse_z3_formula."""
        s = formula.strip().strip('"').strip("'")
        # Unicode logical operators
        s = s.replace('¬', 'Not ')   # NOT sign
        # Strip quantifiers (propositional approximation for grounded problems)
        s = re.sub(r'[∀∃]\s*\w+\s*[:.]\s*', '', s)
        s = re.sub(r'\b(?:forall|for\s+all|exists)\s+\w+\s*[:.]\s*', '', s, flags=re.IGNORECASE)
        # Function name case normalization (function-call position only)
        s = re.sub(r'\bimplies\s*\(', 'Implies(', s, flags=re.IGNORECASE)
        s = re.sub(r'\bnot\s*\(', 'Not(', s, flags=re.IGNORECASE)
        # ~x -> Not(x)
        s = re.sub(r'~(\w+)', r'Not(\1)', s)
        return s.strip()

    async def _generate_single(self, problem_text: str, idx: int) -> list[dict]:
        """Generate constraints for one sample, with retry on empty result."""
        prompt_template = ICG_PROMPT_LOGIQA if self.dataset == "logiqa" else ICG_PROMPT
        prompt = prompt_template.format(problem=problem_text)
        for attempt in range(self.max_retries):
            try:
                resp = await self.async_client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                )
                raw = resp.choices[0].message.content or ""
                data = self._extract_json(raw)
                if data is None:
                    logger.info("ICG sample %d attempt %d: no valid JSON (raw=%s)",
                                idx, attempt, raw[:200])
                    continue
                constraints = data.get("constraints", [])
                valid = []
                for c in constraints:
                    if "z3_formula" not in c:
                        continue
                    normalized = self._normalize_z3_formula(c["z3_formula"])
                    z3_f = parse_z3_formula(normalized)
                    if z3_f is None:
                        z3_f = parse_z3_formula(c["z3_formula"])
                    if z3_f is not None:
                        c.setdefault("expression", c["z3_formula"])
                        c.setdefault("type", "fact")
                        valid.append(c)
                    else:
                        logger.debug("ICG sample %d: unparseable z3_formula: %s",
                                     idx, c["z3_formula"][:100])
                if valid:
                    return valid
                logger.info("ICG sample %d attempt %d: JSON ok but 0/%d constraints parsed",
                            idx, attempt, len(constraints))
            except Exception as e:
                logger.warning("ICG sample %d attempt %d error: %s", idx, attempt, str(e)[:200])
        return []

    def generate(self, problem_text: str, k_icg: int = 10) -> list[list[dict]]:
        """Generate k_icg independent constraint sets for one problem."""
        async def _run():
            tasks = [self._generate_single(problem_text, i) for i in range(k_icg)]
            return await asyncio.gather(*tasks)

        try:
            loop = asyncio.get_running_loop()
            import nest_asyncio
            nest_asyncio.apply()
            return loop.run_until_complete(_run())
        except RuntimeError:
            return asyncio.run(_run())


# ---------------------------------------------------------------------------
# Scoring: use independent constraints to score SC candidates
# ---------------------------------------------------------------------------

def score_with_icg_constraints(
    all_constraint_sets: list[list[dict]],
    traces: list[dict],
    candidates: list[str],
    maxsat_timeout_ms: int = 10000,
) -> dict:
    """Deduplicate + MAX-SAT solve independent constraints, then score candidates."""
    deduplicator = ConstraintDeduplicator()
    solver = MaxSATSolver()
    scorer = InvariantScorer()

    unique = deduplicator.deduplicate(all_constraint_sets)
    if not unique:
        return {"answer": "", "scores": {}, "constraints_stats": {}, "maxsat_stats": {}}

    maxsat_result = solver.solve(unique, timeout_ms=maxsat_timeout_ms)

    answer_counts = Counter(t.get("answer", "") for t in traces if t.get("answer"))
    scores = scorer.score(maxsat_result, traces, candidates)
    selected = scorer.select_answer(scores, answer_counts)

    return {
        "answer": selected,
        "scores": scores,
        "constraints_stats": {
            "total_generated": sum(len(cs) for cs in all_constraint_sets),
            "non_empty_samples": sum(1 for cs in all_constraint_sets if cs),
            "unique_after_dedup": len(unique),
        },
        "maxsat_stats": {
            "satisfied": len(maxsat_result.satisfied),
            "excluded": len(maxsat_result.excluded),
            "total_weight": maxsat_result.total_weight,
            "solve_time_ms": maxsat_result.solve_time_ms,
        },
    }


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_data(path: str) -> list[dict]:
    with open(path) as f:
        data = json.load(f)
    for p in data:
        p.setdefault("dataset", "folio")
    logger.info("Loaded %d problems from %s", len(data), path)
    return data


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="ICG Pipeline")
    parser.add_argument("--data", default="data/folio_full.json")
    parser.add_argument("--output", default="results/exp074_icg/results.json")
    parser.add_argument("--mode", choices=["vllm"], default="vllm")
    parser.add_argument("--k", type=int, default=12, help="SC trace count")
    parser.add_argument("--k-icg", type=int, default=10, help="ICG sampling count")
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument("--api-base", default="http://localhost:8000/v1")
    parser.add_argument("--api-key", default="EMPTY")
    parser.add_argument("--model", default="auto")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--maxsat-timeout", type=int, default=10000)
    parser.add_argument("--max-retries", type=int, default=3, help="Max retries per ICG sample")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--save-intermediates", action="store_true")
    parser.add_argument("--dataset", choices=["folio", "logiqa"], default="folio",
                        help="Dataset type: folio (3-class) or logiqa (4-choice)")
    parser.add_argument("--limit", type=int, default=0, help="Limit to N problems (0 = all)")
    args = parser.parse_args()

    problems = load_data(args.data)
    if args.limit > 0:
        problems = problems[:args.limit]
        logger.info("Limited to %d problems", len(problems))

    # Build components
    model_name = args.model if args.model != "auto" else None

    trace_gen = VLLMGenerator(
        base_url=args.api_base,
        api_key=[REDACTED],
        model=model_name,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
    )
    trace_gen.domain = "multichoice" if args.dataset == "logiqa" else "math"

    icg_gen = ICGGenerator(
        base_url=args.api_base,
        model=model_name,
        temperature=args.temperature,
        max_tokens=2048,
        max_retries=args.max_retries,
    )
    icg_gen.dataset = args.dataset

    sc_baseline = SelfConsistency()

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)

    # Resume support
    all_results = []
    done_ids = set()
    if args.resume and os.path.exists(args.output):
        with open(args.output) as f:
            prev = json.load(f)
        all_results = prev.get("results", [])
        done_ids = {r["problem_id"] for r in all_results}
        logger.info("Resumed: %d problems already done", len(done_ids))

    remaining = [(i, p) for i, p in enumerate(problems) if p.get("id", f"prob_{i}") not in done_ids]
    logger.info("Remaining: %d problems", len(remaining))

    total_start = time.time()
    elapsed_times = []

    for progress_idx, (i, prob) in enumerate(remaining):
        t0 = time.time()
        prob_id = prob.get("id", f"prob_{i}")
        print(f"\n{'='*60}")
        print(f"[{progress_idx+1}/{len(remaining)}] Problem {prob_id}")

        # --- Phase 1: SC trace generation ---
        try:
            traces = trace_gen.generate(prob["problem"], k=args.k)
            for t in traces:
                if t.get("answer"):
                    t["answer"] = normalize_logic_answer(t["answer"])
            answers = [t.get("answer", "") for t in traces]
            sc_result = sc_baseline.run(prob, traces=[t["trace"] for t in traces], answers=answers)
            sc_answer = sc_result.get("answer", "")
            sc_correct = (normalize_logic_answer(sc_answer) == normalize_logic_answer(prob["answer"]))
            candidates = sorted(set(a for a in answers if a))
            # For LogiQA, ensure all 4 options are candidates
            if args.dataset == "logiqa":
                for opt in ["A", "B", "C", "D"]:
                    if opt not in candidates:
                        candidates.append(opt)
                candidates = sorted(candidates)
            print(f"  SC answer: {sc_answer} ({'V' if sc_correct else 'X'})  votes: {sc_result.get('vote_distribution', {})}")
        except Exception as e:
            logger.error("Phase 1 error on %s: %s", prob_id, e)
            traces, sc_answer, sc_correct, candidates = [], "", False, []
            sc_result = {"vote_count": 0, "vote_distribution": {}}

        # --- Phase 2: Independent constraint generation ---
        try:
            icg_constraint_sets = icg_gen.generate(prob["problem"], k_icg=args.k_icg)
            total_icg = sum(len(cs) for cs in icg_constraint_sets)
            non_empty = sum(1 for cs in icg_constraint_sets if cs)
            print(f"  ICG: {total_icg} constraints from {non_empty}/{args.k_icg} samples")
        except Exception as e:
            logger.error("Phase 2 error on %s: %s", prob_id, e)
            icg_constraint_sets = []

        # --- Phase 3: MAX-SAT scoring with independent constraints ---
        icg_answer = ""
        icg_correct = False
        icg_scoring = {}
        if candidates and icg_constraint_sets:
            try:
                icg_scoring = score_with_icg_constraints(
                    icg_constraint_sets, traces, candidates,
                    maxsat_timeout_ms=args.maxsat_timeout,
                )
                icg_answer = icg_scoring.get("answer", "")
                icg_correct = (normalize_logic_answer(icg_answer) == normalize_logic_answer(prob["answer"]))
                print(f"  ICG answer: {icg_answer} ({'V' if icg_correct else 'X'})  scores: {icg_scoring.get('scores', {})}")
            except Exception as e:
                logger.error("Phase 3 error on %s: %s", prob_id, e)
        elif not candidates:
            print("  ICG: skipped (no candidates from SC)")
        else:
            print("  ICG: skipped (no constraints generated)")

        elapsed = time.time() - t0
        elapsed_times.append(elapsed)
        print(f"  Time: {elapsed:.1f}s")

        remaining_count = len(remaining) - (progress_idx + 1)
        if remaining_count > 0:
            avg_time = sum(elapsed_times) / len(elapsed_times)
            eta_min = avg_time * remaining_count / 60
            print(f"  ETA: {eta_min:.1f} min ({remaining_count} remaining)")

        sys.stdout.flush()

        result_entry = {
            "problem_idx": i,
            "problem_id": prob_id,
            "problem": prob["problem"],
            "ground_truth": prob["answer"],
            "sc_answer": sc_answer,
            "sc_correct": sc_correct,
            "sc_vote_count": sc_result.get("vote_count", 0),
            "sc_vote_distribution": sc_result.get("vote_distribution", {}),
            "icg_answer": icg_answer,
            "icg_correct": icg_correct,
            "icg_scores": icg_scoring.get("scores", {}),
            "constraints_count": icg_scoring.get("constraints_stats", {}).get("total_generated", 0),
            "icg_constraints_stats": icg_scoring.get("constraints_stats", {}),
            "icg_maxsat_stats": icg_scoring.get("maxsat_stats", {}),
            "wall_time_s": round(elapsed, 2),
        }
        all_results.append(result_entry)

        # Save intermediates
        if args.save_intermediates:
            intermed_dir = os.path.join(os.path.dirname(args.output) or ".", "intermediates")
            os.makedirs(intermed_dir, exist_ok=True)
            intermed_data = {
                "problem": prob,
                "traces": traces,
                "icg_constraint_sets": icg_constraint_sets,
                "icg_scoring": icg_scoring,
            }
            with open(os.path.join(intermed_dir, f"{prob_id}.json"), "w") as f:
                json.dump(intermed_data, f, indent=2, default=str)

        # Checkpoint
        n = len(all_results)
        sc_acc = sum(1 for r in all_results if r["sc_correct"]) / n
        icg_acc = sum(1 for r in all_results if r["icg_correct"]) / n
        summary = {
            "n": n,
            "sc_accuracy": round(sc_acc, 4),
            "icg_accuracy": round(icg_acc, 4),
            "delta": round(icg_acc - sc_acc, 4),
            "k": args.k,
            "k_icg": args.k_icg,
            "temperature": args.temperature,
            "seed": args.seed,
            "mode": args.mode,
            "dataset": args.dataset,
            "total_wall_time_s": round(time.time() - total_start, 1),
        }
        output = {"summary": summary, "results": all_results}
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2, default=str)

    # Final summary
    n = len(all_results)
    if n > 0:
        sc_acc = sum(1 for r in all_results if r["sc_correct"]) / n
        icg_acc = sum(1 for r in all_results if r["icg_correct"]) / n
        print(f"\n{'='*60}")
        print(f"FINAL RESULTS ({n} problems)")
        print(f"  SC:    {sc_acc:.4f} ({sum(1 for r in all_results if r['sc_correct'])}/{n})")
        print(f"  ICG:   {icg_acc:.4f} ({sum(1 for r in all_results if r['icg_correct'])}/{n})")
        print(f"  Delta: {icg_acc - sc_acc:+.4f}")
        print(f"  Wall:  {(time.time() - total_start)/60:.1f} min")
        print(f"Results saved to {args.output}")

    print("ICG_PIPELINE_DONE")


if __name__ == "__main__":
    main()

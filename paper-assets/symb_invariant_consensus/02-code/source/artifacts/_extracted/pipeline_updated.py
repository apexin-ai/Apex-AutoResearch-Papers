"""
SICA end-to-end pipeline: trace generation -> constraint extraction -> Z3 dedup -> MAX-SAT -> scoring -> answer selection.
Input: problem dict with "problem" and "answer" fields
Output: result dict with answer, score, constraint stats, maxsat stats
Dependencies: trace_generator, constraint_extractor, z3_maxsat, scorer
"""
from __future__ import annotations

import logging
import time
from collections import Counter

from .trace_generator import TraceGenerator
from .constraint_extractor import ConstraintExtractor
from .z3_maxsat import ConstraintDeduplicator, MaxSATSolver
import z3 as _z3
from .scorer import InvariantScorer
from utils.math_equiv import group_equivalent_answers

logger = logging.getLogger(__name__)


def _group_logic_answers(answers: list[str]) -> dict[str, list[int]]:
    """Group answers by case-insensitive exact match (for logic domain)."""
    groups: dict[str, list[int]] = {}
    canonical_map: dict[str, str] = {}
    for i, ans in enumerate(answers):
        if ans is None or str(ans).strip() == "":
            continue
        key = str(ans).strip().lower()
        if key not in canonical_map:
            canonical_map[key] = str(ans).strip()
            groups[canonical_map[key]] = []
        groups[canonical_map[key]].append(i)
    return groups


class SICAPipeline:
    def __init__(
        self,
        trace_generator: TraceGenerator,
        constraint_extractor: ConstraintExtractor,
        k: int = 12,
        maxsat_timeout_ms: int = 10000,
    ):
        self.trace_generator = trace_generator
        self.constraint_extractor = constraint_extractor
        self.k = k
        self.deduplicator = ConstraintDeduplicator()
        self.solver = MaxSATSolver()
        self.scorer = InvariantScorer()
        self.maxsat_timeout_ms = maxsat_timeout_ms

    def run_single(self, problem: dict) -> dict:
        """Run full SICA pipeline on a single problem."""
        t_start = time.perf_counter()

        # Auto-detect domain from problem metadata
        dataset = problem.get("dataset", "")
        domain = "folio" if dataset == "folio" else "logic" if dataset == "proofwriter" else "math"
        self.constraint_extractor.domain = "logic" if domain in ("logic", "folio") else "math"

        cached_traces = None
        try:
            # 1. Generate K traces
            t0 = time.perf_counter()
            task_type = domain  # "math", "logic", or "folio"
            traces = self.trace_generator.generate(problem["problem"], k=self.k, task_type=task_type)
            trace_time = time.perf_counter() - t0
            cached_traces = traces

            # 2. Extract constraints from each trace (batch for concurrency)
            t0 = time.perf_counter()
            all_constraints = self.constraint_extractor.extract_batch(
                [t["trace"] for t in traces]
            )
            extract_time = time.perf_counter() - t0

            # L3 fix: inject answer assertion constraints per trace
            for _ti, _trace in enumerate(traces):
                _ans = str(_trace.get("answer", "")).strip()
                if _ans:
                    _ans_var = f"__sica_answer_{_ans.lower()}"
                    all_constraints[_ti].append({
                        "type": "answer_assertion",
                        "expression": f"answer is {_ans}",
                        "z3_formula": f"{_ans_var} == True",
                        "source_step": -1,
                    })

            total_constraints = sum(len(c) for c in all_constraints)
            non_empty = sum(1 for c in all_constraints if c)

            # 3. Deduplicate via z3 equivalence
            t0 = time.perf_counter()
            unique_constraints = self.deduplicator.deduplicate(all_constraints)
            dedup_time = time.perf_counter() - t0

            # 4. MAX-SAT solve (with L3 answer mutual exclusion)
            _unique_answers = set()
            for _t in traces:
                _a = str(_t.get("answer", "")).strip()
                if _a:
                    _unique_answers.add(_a.lower())
            _hard = []
            if len(_unique_answers) > 1:
                _avars = [_z3.Bool(f"__sica_answer_{a}") for a in sorted(_unique_answers)]
                for _ii in range(len(_avars)):
                    for _jj in range(_ii + 1, len(_avars)):
                        _hard.append(_z3.Not(_z3.And(_avars[_ii], _avars[_jj])))
                _hard.append(_z3.Or(*_avars))

            t0 = time.perf_counter()
            maxsat_result = self.solver.solve(unique_constraints, timeout_ms=self.maxsat_timeout_ms, hard_constraints=_hard or None)
            maxsat_time = time.perf_counter() - t0

            # 5. Group equivalent answers, then score
            raw_answers = [t["answer"] for t in traces if t["answer"]]

            if domain in ("logic", "folio"):
                equiv_groups = _group_logic_answers(raw_answers)
            else:
                equiv_groups = group_equivalent_answers(raw_answers)

            # Remap trace answers to canonical forms for scorer
            canonical_map = {}
            for canonical, indices in equiv_groups.items():
                for idx in indices:
                    canonical_map[raw_answers[idx]] = canonical

            for t in traces:
                if t["answer"] in canonical_map:
                    t["answer"] = canonical_map[t["answer"]]

            candidates = list(equiv_groups.keys())
            answer_counts = {k: len(v) for k, v in equiv_groups.items()}
            scores = self.scorer.score(maxsat_result, traces, candidates)
            selected = self.scorer.select_answer(scores, answer_counts)

            total_time = time.perf_counter() - t_start

            return {
                "answer": selected,
                "domain": domain,
                "scores": scores,
                "answer_counts": answer_counts,
                "traces": traces,
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
                "timing": {
                    "trace_gen_s": round(trace_time, 3),
                    "extraction_s": round(extract_time, 3),
                    "dedup_s": round(dedup_time, 3),
                    "maxsat_s": round(maxsat_time, 3),
                    "total_s": round(total_time, 3),
                },
                "raw_constraints": [
                    {
                        "expression": uc.expression,
                        "z3_formula_str": str(uc.z3_formula),
                        "weight": uc.weight,
                        "source_traces": uc.source_traces,
                    }
                    for uc in unique_constraints
                ],
            }
        except Exception as e:
            try:
                logger.error("SICA pipeline failed: %s", e)
            except Exception:
                pass
            try:
                err_msg = str(e)
            except Exception:
                err_msg = type(e).__name__
            result = {
                "error": err_msg,
                "domain": domain,
                "answer": "",
                "scores": {},
                "answer_counts": {},
                "traces": [],
                "constraints_stats": {
                    "total_extracted": 0,
                    "traces_with_constraints": 0,
                    "unique_after_dedup": 0,
                },
                "maxsat_stats": {
                    "satisfied": 0,
                    "excluded": 0,
                    "total_weight": 0,
                    "solve_time_ms": 0,
                },
            }
            try:
                if cached_traces:
                    sc_answers = [t.get("answer") for t in cached_traces if t.get("answer")]
                    if sc_answers:
                        counter = Counter(sc_answers)
                        result["answer"] = counter.most_common(1)[0][0]
                        result["sc_answer"] = result["answer"]
                        result["answer_counts"] = dict(counter)
                    result["traces"] = cached_traces
            except Exception:
                pass
            result["timing"] = {"total_s": round(time.perf_counter() - t_start, 3)}
            return result

    def run_batch(self, problems: list[dict]) -> list[dict]:
        """Run pipeline on a batch of problems."""
        results = []
        for i, p in enumerate(problems):
            logger.info("Processing problem %d/%d", i + 1, len(problems))
            result = self.run_single(p)
            result["problem_idx"] = i
            results.append(result)
        return results

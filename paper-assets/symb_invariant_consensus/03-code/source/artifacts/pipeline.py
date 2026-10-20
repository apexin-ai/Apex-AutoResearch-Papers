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
from .scorer import InvariantScorer

logger = logging.getLogger(__name__)


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

        # 1. Generate K traces
        t0 = time.perf_counter()
        traces = self.trace_generator.generate(problem["problem"], k=self.k)
        trace_time = time.perf_counter() - t0

        # 2. Extract constraints from each trace (batch for concurrency)
        t0 = time.perf_counter()
        all_constraints = self.constraint_extractor.extract_batch(
            [t["trace"] for t in traces]
        )
        extract_time = time.perf_counter() - t0

        total_constraints = sum(len(c) for c in all_constraints)
        non_empty = sum(1 for c in all_constraints if c)

        # 3. Deduplicate via z3 equivalence
        t0 = time.perf_counter()
        unique_constraints = self.deduplicator.deduplicate(all_constraints)
        dedup_time = time.perf_counter() - t0

        # 4. MAX-SAT solve
        t0 = time.perf_counter()
        maxsat_result = self.solver.solve(unique_constraints, timeout_ms=self.maxsat_timeout_ms)
        maxsat_time = time.perf_counter() - t0

        # 5. Score candidates
        candidates = list(set(t["answer"] for t in traces if t["answer"]))
        answer_counts = Counter(t["answer"] for t in traces if t["answer"])
        scores = self.scorer.score(maxsat_result, traces, candidates)
        selected = self.scorer.select_answer(scores, answer_counts)

        total_time = time.perf_counter() - t_start

        return {
            "answer": selected,
            "scores": scores,
            "answer_counts": dict(answer_counts),
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
        }

    def run_batch(self, problems: list[dict]) -> list[dict]:
        """Run pipeline on a batch of problems."""
        results = []
        for i, p in enumerate(problems):
            logger.info("Processing problem %d/%d", i + 1, len(problems))
            result = self.run_single(p)
            result["problem_idx"] = i
            results.append(result)
        return results

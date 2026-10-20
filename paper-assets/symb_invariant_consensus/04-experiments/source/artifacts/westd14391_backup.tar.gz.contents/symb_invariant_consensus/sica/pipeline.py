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

        # 5. Normalize logic answers before scoring
        if problem.get("dataset", "math") in ("proofwriter", "folio", "strategyqa"):
            for t in traces:
                if t.get("answer"):
                    t["answer"] = normalize_logic_answer(t["answer"])

        # 6. Score candidates
        candidates = sorted(set(t["answer"] for t in traces if t["answer"]))
        answer_counts = Counter(t["answer"] for t in traces if t["answer"])
        scores = self.scorer.score(maxsat_result, traces, candidates)
        selected = self.scorer.select_answer(scores, answer_counts)

        total_time = time.perf_counter() - t_start

        return {
            "answer": selected,
            "scores": scores,
            "answer_counts": dict(answer_counts),
            "traces": traces,
            "per_trace_constraints": all_constraints,
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


_LOGIC_CANONICAL = {
    "true": "True", "yes": "True", "1": "True",
    "false": "False", "no": "False", "0": "False",
    "unknown": "Unknown", "uncertain": "Unknown", "undetermined": "Unknown",
}



def normalize_logic_answer(ans: str) -> str:
    """Normalize a logic answer: strip LaTeX \\text{...} and map to canonical form."""
    s = ans.strip()
    if s.startswith('\\text{'):
        s = s[len('\\text{'):]
        if s.endswith('}'):
            s = s[:-1]
        s = s.strip()
    return _LOGIC_CANONICAL.get(s.lower(), s)


def _group_logic_answers(answers: list[str]) -> dict[str, list[int]]:
    """Group logic answers (True/False/Unknown) with normalization."""
    groups: dict[str, list[int]] = {}
    for i, ans in enumerate(answers):
        key = normalize_logic_answer(ans)
        groups.setdefault(key, []).append(i)
    return groups


# ---------------------------------------------------------------------------
# Contrastive SICA pipeline
# ---------------------------------------------------------------------------

from .constraint_extractor import ContrastiveConstraintExtractor


class ContrastiveScorer:
    """Score candidates using contrastive stance labels.

    For each candidate, sum weights of satisfied supporting constraints
    minus alpha * weights of satisfied opposing constraints.
    """

    def __init__(self, alpha: float = 1.0):
        self.alpha = alpha

    def score(
        self,
        maxsat_result,
        stance_map: dict,
        candidates: list[str],
    ) -> dict[str, float]:
        """Score candidates.

        Args:
            maxsat_result: MaxSATResult from solver.
            stance_map: {constraint_index: [(target, stance, trace_idx), ...]}.
                        Index matches position in the unique_constraints list
                        passed to the solver.
            candidates: list of candidate answer strings.
        """
        satisfied_indices = set()
        for i, uc in enumerate(maxsat_result.satisfied):
            satisfied_indices.add(id(uc))

        scores = {c: 0.0 for c in candidates}

        all_constraints = list(maxsat_result.satisfied) + list(maxsat_result.excluded)
        for uc_idx, uc in enumerate(all_constraints):
            if id(uc) not in satisfied_indices:
                continue
            entries = stance_map.get(uc_idx, [])
            for target, stance, _trace_idx in entries:
                if target not in scores:
                    scores[target] = 0.0
                if stance == "supporting":
                    scores[target] += uc.weight
                elif stance == "opposing":
                    scores[target] -= self.alpha * uc.weight

        return scores

    @staticmethod
    def select_answer(scores: dict[str, float],
                      answer_counts: dict[str, int] | None = None) -> str:
        if not scores:
            return ""
        max_score = max(scores.values())
        top = [a for a, s in scores.items() if s == max_score]
        if len(top) == 1:
            return top[0]
        if answer_counts:
            return max(top, key=lambda a: answer_counts.get(a, 0))
        return top[0]


class ContrastiveSICAPipeline:
    """Pipeline that re-uses existing traces and applies contrastive extraction + MaxSAT."""

    def __init__(
        self,
        contrastive_extractor: ContrastiveConstraintExtractor,
        maxsat_timeout_ms: int = 10000,
        scorer_alpha: float = 1.0,
    ):
        self.extractor = contrastive_extractor
        self.deduplicator = ConstraintDeduplicator()
        self.solver = MaxSATSolver()
        self.scorer = ContrastiveScorer(alpha=scorer_alpha)
        self.maxsat_timeout_ms = maxsat_timeout_ms

    def run_single(self, problem: dict, traces: list[dict]) -> dict:
        """Run contrastive pipeline on a single problem with pre-existing traces.

        Args:
            problem: dict with 'problem', 'answer', 'dataset' keys.
            traces: list of trace dicts with 'trace', 'answer', 'trace_idx' keys.
        """
        import time as _time
        t_start = _time.perf_counter()

        question = problem["problem"]
        dataset = problem.get("dataset", "math")

        if dataset in ("proofwriter", "folio"):
            for t in traces:
                if t.get("answer"):
                    t["answer"] = normalize_logic_answer(t["answer"])

        candidates = sorted(set(t["answer"] for t in traces if t.get("answer")))
        if not candidates:
            candidates = ["True", "False", "Unknown"]
        answer_counts = Counter(t["answer"] for t in traces if t.get("answer"))

        # 1. Contrastive extraction
        t0 = _time.perf_counter()
        all_contrastive = self.extractor.extract_batch(traces, question, candidates)
        extract_time = _time.perf_counter() - t0

        total_extracted = sum(len(c) for c in all_contrastive)

        # 2. Build constraint list with stance metadata
        #    We feed plain constraints into dedup, but keep a side-map of
        #    stance info keyed by (trace_idx, z3_formula_str).
        raw_constraints = []  # list-of-lists for dedup
        stance_metadata = []  # parallel: list-of-lists of (target, stance)
        for trace_idx, clist in enumerate(all_contrastive):
            trace_raw = []
            trace_stance = []
            for c in clist:
                trace_raw.append({
                    "type": "derived",
                    "expression": c.get("expression", ""),
                    "z3_formula": c["z3_formula"],
                    "source_step": c.get("source_step", 0),
                })
                trace_stance.append((c["target"], c["stance"]))
            raw_constraints.append(trace_raw)
            stance_metadata.append(trace_stance)

        # 3. Deduplicate
        t0 = _time.perf_counter()
        unique_constraints = self.deduplicator.deduplicate(raw_constraints)
        dedup_time = _time.perf_counter() - t0

        # 4. Build stance_map: for each unique constraint index, collect stance entries.
        #    We need to map from UniqueConstraint back to the original stance info.
        #    The deduplicator tracks source_traces. We rebuild by re-parsing and matching.
        stance_map = self._build_stance_map(
            unique_constraints, raw_constraints, stance_metadata
        )

        # 5. MaxSAT solve
        t0 = _time.perf_counter()
        maxsat_result = self.solver.solve(unique_constraints, timeout_ms=self.maxsat_timeout_ms)
        maxsat_time = _time.perf_counter() - t0

        # 6. Contrastive scoring
        #    Re-index stance_map to match the ordering in maxsat_result
        all_ucs = list(maxsat_result.satisfied) + list(maxsat_result.excluded)
        reindexed_stance_map = {}
        uc_id_to_original_idx = {id(uc): i for i, uc in enumerate(unique_constraints)}
        for new_idx, uc in enumerate(all_ucs):
            orig_idx = uc_id_to_original_idx.get(id(uc))
            if orig_idx is not None and orig_idx in stance_map:
                reindexed_stance_map[new_idx] = stance_map[orig_idx]

        scores = self.scorer.score(maxsat_result, reindexed_stance_map, candidates)
        selected = self.scorer.select_answer(scores, answer_counts)

        total_time = _time.perf_counter() - t_start

        return {
            "answer": selected,
            "scores": scores,
            "answer_counts": dict(answer_counts),
            "candidates": candidates,
            "constraints_stats": {
                "total_extracted": total_extracted,
                "unique_after_dedup": len(unique_constraints),
                "stance_distribution": self._count_stances(all_contrastive),
            },
            "maxsat_stats": {
                "satisfied": len(maxsat_result.satisfied),
                "excluded": len(maxsat_result.excluded),
                "total_weight": maxsat_result.total_weight,
                "solve_time_ms": maxsat_result.solve_time_ms,
            },
            "timing": {
                "extraction_s": round(extract_time, 3),
                "dedup_s": round(dedup_time, 3),
                "maxsat_s": round(maxsat_time, 3),
                "total_s": round(total_time, 3),
            },
        }

    @staticmethod
    def _build_stance_map(unique_constraints, raw_constraints, stance_metadata):
        """Map each UniqueConstraint index to a list of (target, stance, trace_idx)."""
        from .z3_maxsat import parse_z3_formula, check_equivalence

        stance_map: dict[int, list[tuple]] = {}
        for trace_idx, (trace_raw, trace_stance) in enumerate(
            zip(raw_constraints, stance_metadata)
        ):
            for c, (target, stance) in zip(trace_raw, trace_stance):
                z3_f = parse_z3_formula(c.get("z3_formula", ""))
                if z3_f is None:
                    continue
                for uc_idx, uc in enumerate(unique_constraints):
                    if trace_idx not in uc.source_traces:
                        continue
                    try:
                        if check_equivalence(uc.z3_formula, z3_f, timeout_ms=500):
                            stance_map.setdefault(uc_idx, []).append(
                                (target, stance, trace_idx)
                            )
                            break
                    except Exception:
                        continue
        return stance_map

    @staticmethod
    def _count_stances(all_contrastive):
        counts = {"supporting": 0, "opposing": 0}
        for clist in all_contrastive:
            for c in clist:
                s = c.get("stance", "")
                if s in counts:
                    counts[s] += 1
        return counts

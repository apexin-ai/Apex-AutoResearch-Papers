"""
Z3 UNSAT core feedback refinement for constraint correction.
Checks per-trace constraint consistency with Z3; when UNSAT, extracts the
minimal conflict (unsat_core), asks the LLM to fix it, and iterates up to
max_rounds times or until SAT.
"""
from __future__ import annotations

import json
import logging
import re
import time
from dataclasses import dataclass, field

import z3

from .z3_maxsat import parse_z3_formula

logger = logging.getLogger(__name__)


REFINEMENT_PROMPT = '''The following logical constraints were extracted from a reasoning trace about a logic problem, but a Z3 SMT solver proved they are logically contradictory (unsatisfiable when taken together).

Problem:
{problem}

Original reasoning trace:
{trace}

All extracted constraints from this trace:
{all_constraints}

Conflicting constraint subset (UNSAT core, these cannot all be true simultaneously):
{unsat_core}

Task:
1. Re-read the original reasoning trace
2. Identify which constraint(s) in the UNSAT core are incorrectly extracted or too strong
3. Output the COMPLETE corrected constraint list for this trace

Rules:
- Variable naming: lowercase with underscores (e.g. kind_anne, eats_bear_squirrel)
- Constraint types: "fact", "rule", "derived"
- Z3 operators: Implies(a, b), And(a, b, ...), Or(a, b, ...), Not(a), == True, == False

Output ONLY valid JSON:
{{"constraints": [{{"type": "fact|rule|derived", "expression": "human readable", "z3_formula": "Z3 Python syntax", "source_step": 1}}], "answer": "True or False or Unknown", "variables": ["var1"]}}'''


@dataclass
class RefinementStats:
    """Aggregate statistics across all problems."""
    total_traces_checked: int = 0
    traces_initially_unsat: int = 0
    traces_refined: int = 0
    traces_resolved: int = 0
    total_refinement_calls: int = 0
    parse_errors: int = 0
    per_round_attempts: dict = field(default_factory=dict)
    per_round_resolved: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            'total_traces_checked': self.total_traces_checked,
            'traces_initially_unsat': self.traces_initially_unsat,
            'traces_refined': self.traces_refined,
            'traces_resolved': self.traces_resolved,
            'unsat_to_sat_rate': (self.traces_resolved / self.traces_initially_unsat
                                  if self.traces_initially_unsat > 0 else 0.0),
            'total_refinement_calls': self.total_refinement_calls,
            'parse_errors': self.parse_errors,
            'per_round_attempts': dict(self.per_round_attempts),
            'per_round_resolved': dict(self.per_round_resolved),
        }


class Z3FeedbackRefiner:
    """Z3 UNSAT core feedback -> LLM constraint refinement loop."""

    def __init__(self, api_base: str, model: str, max_rounds: int = 3,
                 temperature: float = 0.3, max_tokens: int = 2048):
        self.api_base = api_base.rstrip('/')
        self.model = model
        self.max_rounds = max_rounds
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.stats = RefinementStats()

    def extract_unsat_core(self, constraints: list[dict]) -> tuple[list[int], list[dict]]:
        """Check constraint satisfiability; return UNSAT core indices and constraints.

        Returns (core_indices, core_constraints). Empty lists if SAT or unparseable.
        """
        parsed = []
        valid_map = []
        for i, c in enumerate(constraints):
            z3_f = parse_z3_formula(c.get('z3_formula', ''))
            if z3_f is not None and z3.is_bool(z3_f):
                parsed.append(z3_f)
                valid_map.append(i)

        if not parsed:
            return [], []

        solver = z3.Solver()
        solver.set('timeout', 5000)
        trackers = []
        for j, f in enumerate(parsed):
            tracker = z3.Bool(f"__track_{j}")
            solver.assert_and_track(f, tracker)
            trackers.append(tracker)

        if solver.check() == z3.unsat:
            core = solver.unsat_core()
            core_names = {str(t) for t in core}
            indices = []
            core_constraints = []
            for j, tracker in enumerate(trackers):
                if str(tracker) in core_names:
                    orig_idx = valid_map[j]
                    indices.append(orig_idx)
                    core_constraints.append(constraints[orig_idx])
            return indices, core_constraints

        return [], []

    def _format_constraints(self, constraints: list[dict]) -> str:
        lines = []
        for i, c in enumerate(constraints):
            lines.append(
                f"  [{i+1}] type={c.get('type','?')}, "
                f'expression="{c.get("expression","")}", '
                f'z3_formula="{c.get("z3_formula","")}"'
            )
        return '\n'.join(lines)

    def build_refinement_prompt(self, unsat_core: list[dict],
                                trace_text: str,
                                all_constraints: list[dict],
                                problem_text: str) -> str:
        """Build prompt showing UNSAT core + original trace for LLM to fix."""
        return REFINEMENT_PROMPT.format(
            problem=problem_text,
            trace=trace_text[:3000],
            all_constraints=self._format_constraints(all_constraints),
            unsat_core=self._format_constraints(unsat_core),
        )

    def _llm_call(self, prompt: str) -> str:
        import httpx
        payload = {
            'model': self.model,
            'messages': [{'role': 'user', 'content': prompt}],
            'max_tokens': self.max_tokens,
            'temperature': self.temperature,
        }
        resp = httpx.post(
            f'{self.api_base}/chat/completions',
            json=payload, timeout=120,
        )
        resp.raise_for_status()
        return resp.json()['choices'][0]['message']['content']

    def _parse_refined(self, raw: str) -> list[dict] | None:
        """Parse LLM refinement response into constraint list."""
        text = re.sub(r'<think>.*?</think>', '', raw, flags=re.DOTALL).strip()
        json_match = re.search(r'\{[\s\S]*\}', text)
        if not json_match:
            return None
        try:
            data = json.loads(json_match.group())
        except json.JSONDecodeError:
            return None
        constraints = data.get('constraints', [])
        if not constraints:
            return None
        valid = []
        for c in constraints:
            if 'z3_formula' not in c:
                continue
            c.setdefault('type', 'derived')
            c.setdefault('expression', c['z3_formula'])
            c.setdefault('source_step', 0)
            valid.append(c)
        return valid if valid else None

    def refine_single_trace(self, constraints: list[dict],
                            trace_text: str, problem_text: str
                            ) -> tuple[list[dict], int, list[list[dict]]]:
        """Run UNSAT core feedback loop on one trace's constraints.

        Returns (final_constraints, rounds_used, history_of_unsat_cores).
        """
        current = list(constraints)
        history = []

        for round_i in range(self.max_rounds):
            core_indices, core_constraints = self.extract_unsat_core(current)
            if not core_constraints:
                break
            history.append(core_constraints)

            self.stats.total_refinement_calls += 1
            self.stats.per_round_attempts[round_i] = \
                self.stats.per_round_attempts.get(round_i, 0) + 1

            prompt = self.build_refinement_prompt(
                core_constraints, trace_text, current, problem_text,
            )
            try:
                raw = self._llm_call(prompt)
                refined = self._parse_refined(raw)
            except Exception as e:
                logger.warning("Refinement LLM call failed (round %d): %s", round_i, e)
                self.stats.parse_errors += 1
                break

            if refined is None:
                logger.warning("Could not parse refined constraints (round %d)", round_i)
                self.stats.parse_errors += 1
                break

            current = refined

        return current, len(history), history

    def refine_problem(self, per_trace: list[dict], problem_text: str) -> dict:
        """Refine all traces for one problem.

        Each entry in per_trace needs: trace_idx, answer, constraints,
        and trace_text (or trace) for the original reasoning text.

        Returns dict with 'per_trace' (refined) and 'problem_stats'.
        """
        refined_traces = []
        problem_stats = {
            'total_traces': len(per_trace),
            'traces_initially_unsat': 0,
            'traces_refined': 0,
            'traces_resolved': 0,
            'total_rounds': 0,
            'constraint_changes': [],
        }

        for t in per_trace:
            constraints = t.get('constraints', [])
            trace_text = t.get('trace_text', t.get('trace', ''))
            self.stats.total_traces_checked += 1

            if len(constraints) < 1:
                refined_traces.append({
                    'trace_idx': t['trace_idx'],
                    'answer': t['answer'],
                    'constraints': constraints,
                    'refined': False,
                    'rounds': 0,
                })
                continue

            core_i, core_c = self.extract_unsat_core(constraints)
            if not core_c:
                refined_traces.append({
                    'trace_idx': t['trace_idx'],
                    'answer': t['answer'],
                    'constraints': constraints,
                    'refined': False,
                    'rounds': 0,
                })
                continue

            self.stats.traces_initially_unsat += 1
            problem_stats['traces_initially_unsat'] += 1

            refined_constraints, rounds, history = self.refine_single_trace(
                constraints, trace_text, problem_text,
            )

            final_core_i, final_core_c = self.extract_unsat_core(refined_constraints)
            resolved = len(final_core_c) == 0
            was_refined = rounds > 0

            if was_refined:
                self.stats.traces_refined += 1
                problem_stats['traces_refined'] += 1
            if resolved:
                self.stats.traces_resolved += 1
                problem_stats['traces_resolved'] += 1
                resolve_round = rounds - 1
                self.stats.per_round_resolved[resolve_round] = \
                    self.stats.per_round_resolved.get(resolve_round, 0) + 1

            problem_stats['total_rounds'] += rounds
            problem_stats['constraint_changes'].append({
                'trace_idx': t['trace_idx'],
                'original_count': len(constraints),
                'refined_count': len(refined_constraints),
                'rounds': rounds,
                'resolved': resolved,
            })

            entry = {
                'trace_idx': t['trace_idx'],
                'answer': t['answer'],
                'constraints': refined_constraints,
                'refined': was_refined,
                'rounds': rounds,
                'resolved': resolved,
            }
            if was_refined:
                entry['original_constraints'] = constraints
            refined_traces.append(entry)

        return {
            'per_trace': refined_traces,
            'problem_stats': problem_stats,
        }

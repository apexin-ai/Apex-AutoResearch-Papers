"""
Z3-based weighted partial MAX-SAT solver for constraint consensus.
Input: multi-trace constraint lists (list of list of dicts)
Output: optimal satisfiable constraint subset, excluded contradictions, per-answer scores
Dependencies: z3-solver
"""
from __future__ import annotations

import logging
import re
import time
from dataclasses import dataclass, field

import z3

z3.set_param('smt.random_seed', 42)
z3.set_param('sat.random_seed', 42)

logger = logging.getLogger(__name__)

_BOOL_INDICATORS = re.compile(r'\bImplies\s*\(|==\s*True|==\s*False|\bNot\s*\(|\bAnd\s*\(|\bOr\s*\(')


def _is_boolean_formula(formula_str: str) -> bool:
    """Detect whether a formula uses boolean logic (vs arithmetic)."""
    return bool(_BOOL_INDICATORS.search(formula_str))


def _preprocess_formula(formula_str: str) -> str:
    """Normalize common LLM output patterns before z3 eval."""
    s = formula_str.strip()
    # Sum -> sum
    s = re.sub(r'\bSum\b', 'sum', s)
    # sum([x1, x2, ...]) -> sum(x1, x2, ...)
    s = re.sub(r'\bsum\(\[([^\[\]]*)\]\)', r'sum(\1)', s)
    # pow(a, b) -> (a)**(b)
    s = re.sub(r'\bpow\(([^,]+),\s*([^)]+)\)', r'(\1)**(\2)', s)
    # Abs -> abs
    s = re.sub(r'\bAbs\b', 'abs', s)
    return s


def parse_z3_formula(formula_str: str, var_type: str = "auto") -> z3.ExprRef | None:
    """Safely parse a string into a z3 expression.

    Supports:
      - Arithmetic: +, -, *, /, **, ==, !=, <, >, <=, >= (Real variables)
      - Boolean: Implies, And, Or, Not, == True/False (Bool variables)
      - Functions: sum, max, min, abs (z3-compatible wrappers)
    Auto-declares unknown variables as z3.Real or z3.Bool based on context.
    Returns None on parse failure or non-boolean result.
    """
    if not formula_str or not formula_str.strip():
        return None

    formula_str = _preprocess_formula(formula_str)

    use_bool = (var_type == "bool") or (var_type == "auto" and _is_boolean_formula(formula_str))

    tokens = set(re.findall(r'\b([a-zA-Z_]\w*)\b', formula_str))
    reserved = {
        'True', 'False', 'And', 'Or', 'Not', 'Implies', 'If',
        'abs', 'Abs', 'Bool', 'Real', 'Int',
        'sum', 'Sum', 'max', 'min', 'len', 'int', 'Mod', 'pow',
    }
    var_names = tokens - reserved

    ns: dict = {}
    for name in var_names:
        ns[name] = z3.Bool(name) if use_bool else z3.Real(name)

    ns['And'] = z3.And
    ns['Or'] = z3.Or
    ns['Not'] = z3.Not
    ns['Implies'] = z3.Implies
    ns['If'] = z3.If
    ns['Bool'] = z3.Bool
    ns['Real'] = z3.Real
    ns['Int'] = z3.Int
    ns['True'] = True
    ns['False'] = False
    ns['Mod'] = lambda a, b: a % b
    ns['pow'] = lambda a, b: a ** b

    ns['abs'] = lambda x: z3.If(x >= 0, x, -x) if isinstance(x, z3.ArithRef) else abs(x)

    def _z3_sum(*args):
        items = []
        for a in args:
            if hasattr(a, '__iter__') and not isinstance(a, z3.ExprRef):
                items.extend(a)
            else:
                items.append(a)
        if not items:
            return 0
        result = items[0]
        for item in items[1:]:
            result = result + item
        return result

    def _z3_max(*args):
        items = []
        for a in args:
            if hasattr(a, '__iter__') and not isinstance(a, z3.ExprRef):
                items.extend(a)
            else:
                items.append(a)
        if not items:
            raise ValueError("max() requires at least one argument")
        result = items[0]
        for item in items[1:]:
            if isinstance(result, z3.ExprRef) or isinstance(item, z3.ExprRef):
                result = z3.If(result >= item, result, item)
            else:
                result = result if result >= item else item
        return result

    def _z3_min(*args):
        items = []
        for a in args:
            if hasattr(a, '__iter__') and not isinstance(a, z3.ExprRef):
                items.extend(a)
            else:
                items.append(a)
        if not items:
            raise ValueError("min() requires at least one argument")
        result = items[0]
        for item in items[1:]:
            if isinstance(result, z3.ExprRef) or isinstance(item, z3.ExprRef):
                result = z3.If(result <= item, result, item)
            else:
                result = result if result <= item else item
        return result

    ns['sum'] = _z3_sum
    ns['Sum'] = _z3_sum
    ns['max'] = _z3_max
    ns['min'] = _z3_min
    ns['len'] = len
    ns['int'] = lambda x: x

    try:
        result = eval(formula_str, {"__builtins__": {}}, ns)
        if isinstance(result, z3.ExprRef) and z3.is_bool(result):
            return result
        if isinstance(result, bool):
            return z3.BoolVal(result)
        return None
    except Exception as e:
        logger.debug("Failed to parse z3 formula '%s': %s", formula_str, e)
        return None


def check_equivalence(f1: z3.ExprRef, f2: z3.ExprRef, timeout_ms: int = 1000) -> bool:
    """Check if two z3 formulas are logically equivalent (f1 <=> f2)."""
    if not z3.is_bool(f1) or not z3.is_bool(f2):
        return False
    s = z3.Solver()
    s.set("timeout", timeout_ms)
    s.add(z3.Not(f1 == f2))
    result = s.check()
    return result == z3.unsat


@dataclass
class UniqueConstraint:
    expression: str
    z3_formula: z3.ExprRef
    weight: int  # cross-trace frequency
    source_traces: list[int] = field(default_factory=list)

    def __repr__(self) -> str:
        return f"UniqueConstraint(expr='{self.expression}', w={self.weight}, traces={self.source_traces})"


@dataclass
class MaxSATResult:
    satisfied: list[UniqueConstraint]
    excluded: list[UniqueConstraint]
    total_weight: int
    solve_time_ms: float


class ConstraintDeduplicator:
    """Deduplicate constraints across traces using z3 equivalence checking."""

    def __init__(self, equiv_timeout_ms: int = 1000):
        self.equiv_timeout_ms = equiv_timeout_ms

    def deduplicate(self, all_constraints: list[list[dict]]) -> list[UniqueConstraint]:
        """Merge equivalent constraints across K traces.

        Args:
            all_constraints: K lists of constraint dicts, one per trace.
        Returns:
            Deduplicated list with frequency weights.
        """
        unique: list[UniqueConstraint] = []

        for trace_idx, trace_constraints in enumerate(all_constraints):
            for c in trace_constraints:
                z3_f = parse_z3_formula(c.get("z3_formula", ""))
                if z3_f is None:
                    logger.debug("Skipping unparseable constraint: %s", c.get("z3_formula"))
                    continue

                merged = False
                for uc in unique:
                    try:
                        if check_equivalence(uc.z3_formula, z3_f, self.equiv_timeout_ms):
                            uc.weight += 1
                            if trace_idx not in uc.source_traces:
                                uc.source_traces.append(trace_idx)
                            merged = True
                            break
                    except Exception:
                        continue

                if not merged:
                    unique.append(UniqueConstraint(
                        expression=c.get("expression", ""),
                        z3_formula=z3_f,
                        weight=1,
                        source_traces=[trace_idx],
                    ))

        return unique


class MaxSATSolver:
    """Weighted partial MAX-SAT solver using z3.Optimize."""

    def solve(self, unique_constraints: list[UniqueConstraint], timeout_ms: int = 10000, hard_constraints: list | None = None) -> MaxSATResult:
        """Find the maximum-weight satisfiable subset of constraints."""
        if not unique_constraints:
            return MaxSATResult(satisfied=[], excluded=[], total_weight=0, solve_time_ms=0.0)

        opt = z3.Optimize()
        opt.set("timeout", timeout_ms)

        if hard_constraints:
            for hc in hard_constraints:
                opt.add(hc)

        indicators = []
        active_mask = []
        for i, uc in enumerate(unique_constraints):
            ind = z3.Bool(f"__ind_{i}")
            indicators.append(ind)
            try:
                if not z3.is_bool(uc.z3_formula):
                    active_mask.append(False)
                    continue
                opt.add(z3.Implies(ind, uc.z3_formula))
                opt.add_soft(ind, weight=uc.weight)
                active_mask.append(True)
            except Exception as e:
                logger.debug("Skipping constraint %d in MaxSAT: %s", i, e)
                active_mask.append(False)

        if not any(active_mask):
            return MaxSATResult(satisfied=[], excluded=list(unique_constraints),
                                total_weight=0, solve_time_ms=0.0)

        t0 = time.perf_counter()
        result = opt.check()
        solve_time = (time.perf_counter() - t0) * 1000

        satisfied = []
        excluded = []

        if result in (z3.sat, z3.unknown):
            model = opt.model()
            for i, uc in enumerate(unique_constraints):
                if not active_mask[i]:
                    excluded.append(uc)
                    continue
                val = model.evaluate(indicators[i], model_completion=True)
                if z3.is_true(val):
                    satisfied.append(uc)
                else:
                    excluded.append(uc)
        else:
            excluded = list(unique_constraints)

        total_w = sum(uc.weight for uc in satisfied)
        return MaxSATResult(
            satisfied=satisfied,
            excluded=excluded,
            total_weight=total_w,
            solve_time_ms=solve_time,
        )

#!/usr/bin/env python3
"""
Oracle SICA for FOLIO (exp-031): gold FOL + Z3 entailment + MAX-SAT weighted voting.
Uses exp-026 traces (post normalization-fix) with gold FOL annotations.

Mechanism:
  1. Parse gold FOL premises + conclusion into Z3
  2. For each trace with answer A, create a soft constraint:
     - "True"  → conclusion_z3
     - "False" → ¬conclusion_z3
     - "Unknown" → skip (no constraint)
  3. Hard constraints: all gold Z3 premises
  4. MAX-SAT finds max satisfiable subset of trace constraints
  5. Standard SICA scoring selects the answer
  6. Z3 entailment check → z3_gold_agreement metric

CPU-only, no GPU needed.
"""

import json
import logging
import os
import re
import sys
import time
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import z3

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


# ============================================================
# FOL Parser: FOLIO notation → Z3 expressions
# ============================================================

class FOLParser:
    """Parse FOLIO FOL notation (∀, ∃, →, ∧, ∨, ¬, ⊕) into Z3 expressions."""

    def __init__(self):
        self.sort = z3.DeclareSort('Entity')
        self.predicates = {}
        self.constants = {}
        self.variables = {}

    def reset(self):
        self.sort = z3.DeclareSort('Entity')
        self.predicates = {}
        self.constants = {}
        self.variables = {}

    def _get_predicate(self, name, arity):
        key = (name, arity)
        if key not in self.predicates:
            sorts = [self.sort] * arity + [z3.BoolSort()]
            self.predicates[key] = z3.Function(name, *sorts)
        return self.predicates[key]

    def _get_constant(self, name):
        if name not in self.constants:
            self.constants[name] = z3.Const(name, self.sort)
        return self.constants[name]

    def _get_variable(self, name):
        if name not in self.variables:
            self.variables[name] = z3.Const(name, self.sort)
        return self.variables[name]

    def _get_term(self, name):
        if len(name) == 1 and name.islower():
            return self._get_variable(name)
        return self._get_constant(name)

    def parse(self, fol_str):
        try:
            tokens = self._tokenize(fol_str)
            if not tokens:
                return None
            expr, pos = self._parse_formula(tokens, 0)
            return expr
        except Exception as e:
            logger.debug("FOL parse error for '%s': %s", fol_str[:80], e)
            return None

    def _tokenize(self, s):
        tokens = []
        i = 0
        while i < len(s):
            c = s[i]
            if c in ' \t\n\r':
                i += 1
            elif c == '∀':  # ∀
                tokens.append(('FORALL', c))
                i += 1
            elif c == '∃':  # ∃
                tokens.append(('EXISTS', c))
                i += 1
            elif c == '→':  # →
                tokens.append(('IMPLIES', c))
                i += 1
            elif c == '∧':  # ∧
                tokens.append(('AND', c))
                i += 1
            elif c == '∨':  # ∨
                tokens.append(('OR', c))
                i += 1
            elif c == '¬':  # ¬
                tokens.append(('NOT', c))
                i += 1
            elif c == '⊕':  # ⊕
                tokens.append(('XOR', c))
                i += 1
            elif c == '↔':  # ↔
                tokens.append(('IFF', c))
                i += 1
            elif c == '(':
                tokens.append(('LPAREN', c))
                i += 1
            elif c == ')':
                tokens.append(('RPAREN', c))
                i += 1
            elif c == ',':
                tokens.append(('COMMA', c))
                i += 1
            elif c.isalpha() or c == '_':
                j = i
                while j < len(s) and (s[j].isalnum() or s[j] == '_'):
                    j += 1
                tokens.append(('WORD', s[i:j]))
                i = j
            else:
                i += 1
        return tokens

    def _parse_formula(self, tokens, pos):
        return self._parse_quantifier(tokens, pos)

    def _parse_quantifier(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][0] in ('FORALL', 'EXISTS'):
            quant_type = tokens[pos][0]
            pos += 1
            if pos >= len(tokens) or tokens[pos][0] != 'WORD':
                raise ValueError("Expected variable after quantifier")
            var_name = tokens[pos][1]
            pos += 1
            var = self._get_variable(var_name)
            body, pos = self._parse_quantifier(tokens, pos)
            if body is None:
                raise ValueError("Failed to parse quantifier body")
            if quant_type == 'FORALL':
                return z3.ForAll([var], body), pos
            else:
                return z3.Exists([var], body), pos
        return self._parse_iff(tokens, pos)

    def _parse_iff(self, tokens, pos):
        left, pos = self._parse_implies(tokens, pos)
        if left is None:
            return None, pos
        while pos < len(tokens) and tokens[pos][0] == 'IFF':
            pos += 1
            right, pos = self._parse_implies(tokens, pos)
            if right is None:
                raise ValueError("Failed to parse right side of ↔")
            left = left == right
        return left, pos

    def _parse_implies(self, tokens, pos):
        left, pos = self._parse_or(tokens, pos)
        if left is None:
            return None, pos
        if pos < len(tokens) and tokens[pos][0] == 'IMPLIES':
            pos += 1
            right, pos = self._parse_implies(tokens, pos)
            if right is None:
                raise ValueError("Failed to parse right side of →")
            return z3.Implies(left, right), pos
        return left, pos

    def _parse_or(self, tokens, pos):
        left, pos = self._parse_xor(tokens, pos)
        if left is None:
            return None, pos
        while pos < len(tokens) and tokens[pos][0] == 'OR':
            pos += 1
            right, pos = self._parse_xor(tokens, pos)
            if right is None:
                raise ValueError("Failed to parse right side of ∨")
            left = z3.Or(left, right)
        return left, pos

    def _parse_xor(self, tokens, pos):
        left, pos = self._parse_and(tokens, pos)
        if left is None:
            return None, pos
        while pos < len(tokens) and tokens[pos][0] == 'XOR':
            pos += 1
            right, pos = self._parse_and(tokens, pos)
            if right is None:
                raise ValueError("Failed to parse right side of ⊕")
            left = z3.Xor(left, right)
        return left, pos

    def _parse_and(self, tokens, pos):
        left, pos = self._parse_not(tokens, pos)
        if left is None:
            return None, pos
        while pos < len(tokens) and tokens[pos][0] == 'AND':
            pos += 1
            right, pos = self._parse_not(tokens, pos)
            if right is None:
                raise ValueError("Failed to parse right side of ∧")
            left = z3.And(left, right)
        return left, pos

    def _parse_not(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][0] == 'NOT':
            pos += 1
            expr, pos = self._parse_not(tokens, pos)
            if expr is None:
                raise ValueError("Failed to parse negation")
            return z3.Not(expr), pos
        return self._parse_atom(tokens, pos)

    def _parse_atom(self, tokens, pos):
        if pos >= len(tokens):
            return None, pos

        if tokens[pos][0] == 'LPAREN':
            pos += 1
            expr, pos = self._parse_formula(tokens, pos)
            if pos < len(tokens) and tokens[pos][0] == 'RPAREN':
                pos += 1
            return expr, pos

        if tokens[pos][0] == 'WORD':
            name = tokens[pos][1]
            pos += 1
            if pos < len(tokens) and tokens[pos][0] == 'LPAREN':
                pos += 1
                args = []
                while pos < len(tokens) and tokens[pos][0] != 'RPAREN':
                    if tokens[pos][0] == 'COMMA':
                        pos += 1
                        continue
                    if tokens[pos][0] == 'WORD':
                        args.append(self._get_term(tokens[pos][1]))
                        pos += 1
                    else:
                        break
                if pos < len(tokens) and tokens[pos][0] == 'RPAREN':
                    pos += 1
                pred = self._get_predicate(name, len(args))
                return pred(*args), pos
            else:
                return z3.Bool(name), pos

        return None, pos


# ============================================================
# Z3 Entailment Checker
# ============================================================

def check_entailment(premises_z3, conclusion_z3, timeout_ms=10000):
    if conclusion_z3 is None:
        return "Unknown"

    s1 = z3.Solver()
    s1.set("timeout", timeout_ms)
    for p in premises_z3:
        if p is not None:
            s1.add(p)
    s1.add(z3.Not(conclusion_z3))
    r1 = s1.check()

    if r1 == z3.unsat:
        return "True"

    s2 = z3.Solver()
    s2.set("timeout", timeout_ms)
    for p in premises_z3:
        if p is not None:
            s2.add(p)
    s2.add(conclusion_z3)
    r2 = s2.check()

    if r2 == z3.unsat:
        return "False"

    return "Unknown"


# ============================================================
# Answer Normalization (matches sica/pipeline.py)
# ============================================================

_LOGIC_CANONICAL = {
    "true": "True", "yes": "True", "1": "True",
    "false": "False", "no": "False", "0": "False",
    "unknown": "Unknown", "uncertain": "Unknown", "undetermined": "Unknown",
}


def normalize_logic_answer(ans):
    s = ans.strip()
    if s.startswith('\\text{'):
        s = s[len('\\text{'):]
        if s.endswith('}'):
            s = s[:-1]
        s = s.strip()
    return _LOGIC_CANONICAL.get(s.lower(), s)


# ============================================================
# Oracle SICA via MAX-SAT
# ============================================================

def oracle_sica_maxsat(traces, z3_premises, z3_conclusion, timeout_ms=10000):
    """
    Oracle SICA using MAX-SAT with gold FOL as hard constraints.

    Hard constraints: gold Z3 premises
    Soft constraints: per-trace answer assertions
      - "True"    → conclusion_z3 (weight 1)
      - "False"   → Not(conclusion_z3) (weight 1)
      - "Unknown" → no constraint (abstain)

    Returns: (oracle_answer, oracle_scores, maxsat_stats)
    """
    answer_counts = Counter(t["answer"] for t in traces if t.get("answer"))
    candidates = sorted(answer_counts.keys())

    if not candidates:
        return "", {}, {}

    opt = z3.Optimize()
    opt.set("timeout", timeout_ms)

    for p in z3_premises:
        if p is not None:
            opt.add(p)

    indicators = []
    trace_map = []

    for i, t in enumerate(traces):
        ans = t.get("answer", "")
        if ans == "True" and z3_conclusion is not None:
            ind = z3.Bool(f"__trace_{i}")
            opt.add(z3.Implies(ind, z3_conclusion))
            opt.add_soft(ind, weight=1)
            indicators.append(ind)
            trace_map.append((i, ans))
        elif ans == "False" and z3_conclusion is not None:
            ind = z3.Bool(f"__trace_{i}")
            opt.add(z3.Implies(ind, z3.Not(z3_conclusion)))
            opt.add_soft(ind, weight=1)
            indicators.append(ind)
            trace_map.append((i, ans))

    result = opt.check()

    satisfied_traces = set()
    excluded_traces = set()

    if result in (z3.sat, z3.unknown) and indicators:
        model = opt.model()
        for ind, (trace_idx, ans) in zip(indicators, trace_map):
            val = model.evaluate(ind, model_completion=True)
            if z3.is_true(val):
                satisfied_traces.add(trace_idx)
            else:
                excluded_traces.add(trace_idx)

    scores = {}
    for cand in candidates:
        cand_traces = {i for i, t in enumerate(traces) if t.get("answer") == cand}
        positive = len(cand_traces & satisfied_traces)
        excluded_exposure = len(cand_traces & excluded_traces)
        scores[cand] = positive - 0.5 * excluded_exposure

    if scores:
        max_score = max(scores.values())
        top = [a for a, s in scores.items() if s == max_score]
        if len(top) == 1:
            oracle_answer = top[0]
        else:
            oracle_answer = max(top, key=lambda a: answer_counts.get(a, 0))
    else:
        oracle_answer = max(candidates, key=lambda a: answer_counts.get(a, 0))

    stats = {
        "n_soft_constraints": len(indicators),
        "n_satisfied": len(satisfied_traces),
        "n_excluded": len(excluded_traces),
        "solver_result": str(result),
    }

    return oracle_answer, scores, stats


# ============================================================
# Main
# ============================================================

def main():
    base_dir = "/root/symb_invariant_consensus"
    data_path = os.path.join(base_dir, "data/folio_full.json")
    traces_dir = os.path.join(base_dir, "results/folio_204_14b/intermediates")
    output_dir = os.path.join(base_dir, "results/oracle_folio_regen")
    os.makedirs(output_dir, exist_ok=True)

    logger.info("Loading FOLIO gold data from %s", data_path)
    with open(data_path) as f:
        gold_data = json.load(f)
    logger.info("Loaded %d problems", len(gold_data))

    gold_by_id = {p["id"]: p for p in gold_data}

    trace_files = sorted(
        [f for f in os.listdir(traces_dir) if f.endswith(".json")],
        key=lambda x: int(re.search(r'(\d+)', x).group(1))
    )
    logger.info("Found %d trace files", len(trace_files))

    parser = FOLParser()
    results = []
    n_correct_oracle = 0
    n_correct_sc = 0
    n_correct_sica_self = 0
    n_z3_agree = 0
    n_z3_determined = 0
    n_fol_parse_ok = 0
    n_total = 0

    t_start = time.time()

    for fi, fname in enumerate(trace_files):
        with open(os.path.join(traces_dir, fname)) as f:
            intermediate = json.load(f)

        problem = intermediate["problem"]
        sica_result = intermediate["sica_result"]
        prob_id = problem["id"]
        gold_answer = problem["answer"]

        gold_prob = gold_by_id.get(prob_id, problem)
        premises_fol = gold_prob.get("premises_fol", [])
        conclusion_fol = gold_prob.get("conclusion_fol", "")

        traces = sica_result.get("traces", [])
        for t in traces:
            if t.get("answer"):
                t["answer"] = normalize_logic_answer(t["answer"])

        answer_counts = Counter(t["answer"] for t in traces if t.get("answer"))
        candidates = sorted(answer_counts.keys())
        sc_answer = max(candidates, key=lambda a: answer_counts.get(a, 0)) if candidates else ""

        sica_self_answer = normalize_logic_answer(sica_result.get("answer", ""))

        parser.reset()
        z3_premises = []
        z3_conclusion = None
        parse_ok = True

        for fol in premises_fol:
            z3_expr = parser.parse(fol)
            if z3_expr is not None:
                z3_premises.append(z3_expr)
            else:
                parse_ok = False
                logger.warning("[%s] Failed to parse premise: %s", prob_id, fol[:60])

        z3_conclusion = parser.parse(conclusion_fol) if conclusion_fol else None
        if z3_conclusion is None and conclusion_fol:
            parse_ok = False
            logger.warning("[%s] Failed to parse conclusion: %s", prob_id, conclusion_fol[:60])

        if parse_ok:
            n_fol_parse_ok += 1

        z3_answer = check_entailment(z3_premises, z3_conclusion) if parse_ok else None
        if z3_answer and z3_answer != "Unknown":
            n_z3_determined += 1
        z3_agrees = (z3_answer == gold_answer) if z3_answer else False
        if z3_agrees:
            n_z3_agree += 1

        if parse_ok and z3_conclusion is not None:
            oracle_answer, oracle_scores, maxsat_stats = oracle_sica_maxsat(
                traces, z3_premises, z3_conclusion
            )
        else:
            oracle_answer = sc_answer
            oracle_scores = dict(answer_counts)
            maxsat_stats = {"fallback": "parse_failed"}

        oracle_correct = (oracle_answer == gold_answer)
        sc_correct = (sc_answer == gold_answer)
        sica_self_correct = (sica_self_answer == gold_answer)

        if oracle_correct:
            n_correct_oracle += 1
        if sc_correct:
            n_correct_sc += 1
        if sica_self_correct:
            n_correct_sica_self += 1
        n_total += 1

        entry = {
            "problem_id": prob_id,
            "gold_answer": gold_answer,
            "z3_answer": z3_answer,
            "z3_agrees_gold": z3_agrees,
            "oracle_answer": oracle_answer,
            "oracle_correct": oracle_correct,
            "oracle_scores": oracle_scores,
            "sc_answer": sc_answer,
            "sc_correct": sc_correct,
            "sica_self_answer": sica_self_answer,
            "sica_self_correct": sica_self_correct,
            "answer_counts": dict(answer_counts),
            "fol_parse_ok": parse_ok,
            "maxsat_stats": maxsat_stats,
        }
        results.append(entry)

        if (fi + 1) % 20 == 0 or fi == len(trace_files) - 1:
            elapsed = time.time() - t_start
            logger.info(
                "[%d/%d] oracle=%.2f%% sc=%.2f%% sica_self=%.2f%% z3_agree=%.2f%% (%.1fs)",
                fi + 1, len(trace_files),
                100 * n_correct_oracle / n_total,
                100 * n_correct_sc / n_total,
                100 * n_correct_sica_self / n_total,
                100 * n_z3_agree / n_total,
                elapsed,
            )

    total_time = time.time() - t_start

    oracle_acc = n_correct_oracle / n_total if n_total else 0
    sc_acc = n_correct_sc / n_total if n_total else 0
    sica_self_acc = n_correct_sica_self / n_total if n_total else 0
    z3_agree_rate = n_z3_agree / n_total if n_total else 0

    # McNemar test: oracle vs SC
    b = sum(1 for r in results if r["oracle_correct"] and not r["sc_correct"])
    c = sum(1 for r in results if not r["oracle_correct"] and r["sc_correct"])
    if b + c > 0:
        mcnemar_chi2 = (abs(b - c) - 1) ** 2 / (b + c)
        from math import exp, sqrt, pi
        def normal_cdf_approx(x):
            a1, a2, a3 = 0.254829592, -0.284496736, 1.421413741
            a4, a5 = -1.453152027, 1.061405429
            p_const = 0.3275911
            sign = 1 if x >= 0 else -1
            x = abs(x) / sqrt(2)
            t = 1.0 / (1.0 + p_const * x)
            y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * exp(-x * x)
            return 0.5 * (1.0 + sign * y)
        p_value = 2 * (1 - normal_cdf_approx(sqrt(mcnemar_chi2)))
    else:
        mcnemar_chi2 = 0
        p_value = 1.0

    summary = {
        "n": n_total,
        "k": 12,
        "oracle_sica_accuracy": round(oracle_acc, 4),
        "sc_accuracy": round(sc_acc, 4),
        "sica_self_accuracy": round(sica_self_acc, 4),
        "oracle_vs_sc_delta_pp": round((oracle_acc - sc_acc) * 100, 2),
        "oracle_vs_sica_delta_pp": round((oracle_acc - sica_self_acc) * 100, 2),
        "mcnemar_chi2": round(mcnemar_chi2, 4),
        "mcnemar_p_oracle_vs_sc": float(f"{p_value:.4e}"),
        "mcnemar_b_c": {"b_oracle_right_sc_wrong": b, "c_oracle_wrong_sc_right": c},
        "z3_gold_agreement": round(z3_agree_rate, 4),
        "z3_gold_agree_n": n_z3_agree,
        "z3_gold_total": n_total,
        "fol_parse_success": round(n_fol_parse_ok / n_total, 4) if n_total else 0,
        "fol_parse_ok_n": n_fol_parse_ok,
        "model": "Qwen2.5-14B-Instruct",
        "dataset": "FOLIO-204",
        "constraint_source": "gold FOL annotations",
        "traces_source": "exp-026-folio204-trace-regen (post normalization-fix)",
        "wall_time_s": round(total_time, 1),
    }

    per_answer_stats = {}
    for ans_type in ["True", "False", "Unknown"]:
        subset = [r for r in results if r["gold_answer"] == ans_type]
        if subset:
            per_answer_stats[ans_type] = {
                "n": len(subset),
                "oracle_acc": round(sum(1 for r in subset if r["oracle_correct"]) / len(subset), 4),
                "sc_acc": round(sum(1 for r in subset if r["sc_correct"]) / len(subset), 4),
                "sica_self_acc": round(sum(1 for r in subset if r["sica_self_correct"]) / len(subset), 4),
                "z3_agree": round(sum(1 for r in subset if r["z3_agrees_gold"]) / len(subset), 4),
            }
    summary["per_answer_type"] = per_answer_stats

    output = {"summary": summary, "results": results}

    output_path = os.path.join(output_dir, "exp031_results.json")
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2, default=str)

    summary_path = os.path.join(output_dir, "exp031_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    print("\n" + "=" * 60)
    print("Oracle SICA Results (exp-031)")
    print("=" * 60)
    print(f"N = {n_total}, K = 12")
    print(f"Oracle SICA accuracy:   {oracle_acc:.4f} ({n_correct_oracle}/{n_total})")
    print(f"SC accuracy:            {sc_acc:.4f} ({n_correct_sc}/{n_total})")
    print(f"SICA(self) accuracy:    {sica_self_acc:.4f} ({n_correct_sica_self}/{n_total})")
    print(f"Oracle vs SC delta:     {(oracle_acc - sc_acc)*100:+.2f}pp")
    print(f"Oracle vs SICA delta:   {(oracle_acc - sica_self_acc)*100:+.2f}pp")
    print(f"McNemar p-value:        {p_value:.4e}")
    print(f"Z3 gold agreement:      {z3_agree_rate:.4f} ({n_z3_agree}/{n_total})")
    print(f"FOL parse success:      {n_fol_parse_ok}/{n_total}")
    print(f"\nPer answer type:")
    for ans_type, stats in per_answer_stats.items():
        print(f"  {ans_type:8s}: n={stats['n']:3d}  oracle={stats['oracle_acc']:.3f}  sc={stats['sc_acc']:.3f}  z3={stats['z3_agree']:.3f}")
    print(f"\nWall time: {total_time:.1f}s")
    print(f"Results saved to {output_path}")
    print("EXP031_DONE")


if __name__ == "__main__":
    main()

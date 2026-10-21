#!/usr/bin/env python3
"""
Oracle SICA for FOLIO (exp-031): gold FOL + Z3 entailment + oracle-weighted voting.
Uses exp-026 traces (post normalization-fix) with gold FOL annotations.

Mechanism:
  1. Parse gold FOL premises + conclusion into Z3
  2. Z3 Solver checks entailment -> oracle answer (True/False/Unknown)
  3. Traces matching oracle answer get weight 1, others get weight 0
  4. Oracle selects the Z3 answer if any trace supports it; else SC fallback
"""

import json
import logging
import os
import re
import sys
import time
from collections import Counter
from math import exp, sqrt

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import z3

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


class FOLParser:
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
            elif c == '∀':
                tokens.append(('FORALL', c)); i += 1
            elif c == '∃':
                tokens.append(('EXISTS', c)); i += 1
            elif c == '→':
                tokens.append(('IMPLIES', c)); i += 1
            elif c == '∧':
                tokens.append(('AND', c)); i += 1
            elif c == '∨':
                tokens.append(('OR', c)); i += 1
            elif c == '¬':
                tokens.append(('NOT', c)); i += 1
            elif c == '⊕':
                tokens.append(('XOR', c)); i += 1
            elif c == '↔':
                tokens.append(('IFF', c)); i += 1
            elif c == '(':
                tokens.append(('LPAREN', c)); i += 1
            elif c == ')':
                tokens.append(('RPAREN', c)); i += 1
            elif c == ',':
                tokens.append(('COMMA', c)); i += 1
            elif c.isalpha() or c == '_':
                j = i
                while j < len(s) and (s[j].isalnum() or s[j] == '_'):
                    j += 1
                tokens.append(('WORD', s[i:j])); i = j
            else:
                i += 1
        return tokens

    def _parse_formula(self, tokens, pos):
        return self._parse_quantifier(tokens, pos)

    def _parse_quantifier(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][0] in ('FORALL', 'EXISTS'):
            quant_type = tokens[pos][0]; pos += 1
            if pos >= len(tokens) or tokens[pos][0] != 'WORD':
                raise ValueError("Expected variable after quantifier")
            var_name = tokens[pos][1]; pos += 1
            var = self._get_variable(var_name)
            body, pos = self._parse_quantifier(tokens, pos)
            if body is None:
                raise ValueError("Quantifier body failed")
            return (z3.ForAll([var], body) if quant_type == 'FORALL'
                    else z3.Exists([var], body)), pos
        return self._parse_iff(tokens, pos)

    def _parse_iff(self, tokens, pos):
        left, pos = self._parse_implies(tokens, pos)
        if left is None: return None, pos
        while pos < len(tokens) and tokens[pos][0] == 'IFF':
            pos += 1
            right, pos = self._parse_implies(tokens, pos)
            if right is None: raise ValueError("IFF RHS failed")
            left = left == right
        return left, pos

    def _parse_implies(self, tokens, pos):
        left, pos = self._parse_or(tokens, pos)
        if left is None: return None, pos
        if pos < len(tokens) and tokens[pos][0] == 'IMPLIES':
            pos += 1
            right, pos = self._parse_implies(tokens, pos)
            if right is None: raise ValueError("IMPLIES RHS failed")
            return z3.Implies(left, right), pos
        return left, pos

    def _parse_or(self, tokens, pos):
        left, pos = self._parse_xor(tokens, pos)
        if left is None: return None, pos
        while pos < len(tokens) and tokens[pos][0] == 'OR':
            pos += 1
            right, pos = self._parse_xor(tokens, pos)
            if right is None: raise ValueError("OR RHS failed")
            left = z3.Or(left, right)
        return left, pos

    def _parse_xor(self, tokens, pos):
        left, pos = self._parse_and(tokens, pos)
        if left is None: return None, pos
        while pos < len(tokens) and tokens[pos][0] == 'XOR':
            pos += 1
            right, pos = self._parse_and(tokens, pos)
            if right is None: raise ValueError("XOR RHS failed")
            left = z3.Xor(left, right)
        return left, pos

    def _parse_and(self, tokens, pos):
        left, pos = self._parse_not(tokens, pos)
        if left is None: return None, pos
        while pos < len(tokens) and tokens[pos][0] == 'AND':
            pos += 1
            right, pos = self._parse_not(tokens, pos)
            if right is None: raise ValueError("AND RHS failed")
            left = z3.And(left, right)
        return left, pos

    def _parse_not(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][0] == 'NOT':
            pos += 1
            expr, pos = self._parse_not(tokens, pos)
            if expr is None: raise ValueError("NOT operand failed")
            return z3.Not(expr), pos
        return self._parse_atom(tokens, pos)

    def _parse_atom(self, tokens, pos):
        if pos >= len(tokens): return None, pos
        if tokens[pos][0] == 'LPAREN':
            pos += 1
            expr, pos = self._parse_formula(tokens, pos)
            if pos < len(tokens) and tokens[pos][0] == 'RPAREN':
                pos += 1
            return expr, pos
        if tokens[pos][0] == 'WORD':
            name = tokens[pos][1]; pos += 1
            if pos < len(tokens) and tokens[pos][0] == 'LPAREN':
                pos += 1
                args = []
                while pos < len(tokens) and tokens[pos][0] != 'RPAREN':
                    if tokens[pos][0] == 'COMMA':
                        pos += 1; continue
                    if tokens[pos][0] == 'WORD':
                        args.append(self._get_term(tokens[pos][1])); pos += 1
                    else:
                        break
                if pos < len(tokens) and tokens[pos][0] == 'RPAREN':
                    pos += 1
                pred = self._get_predicate(name, len(args))
                return pred(*args), pos
            else:
                return z3.Bool(name), pos
        return None, pos


def check_entailment(premises_z3, conclusion_z3, timeout_ms=10000):
    if conclusion_z3 is None:
        return "Unknown"
    s1 = z3.Solver()
    s1.set("timeout", timeout_ms)
    for p in premises_z3:
        if p is not None: s1.add(p)
    s1.add(z3.Not(conclusion_z3))
    if s1.check() == z3.unsat:
        return "True"
    s2 = z3.Solver()
    s2.set("timeout", timeout_ms)
    for p in premises_z3:
        if p is not None: s2.add(p)
    s2.add(conclusion_z3)
    if s2.check() == z3.unsat:
        return "False"
    return "Unknown"


_LOGIC_CANONICAL = {
    "true": "True", "yes": "True", "1": "True",
    "false": "False", "no": "False", "0": "False",
    "unknown": "Unknown", "uncertain": "Unknown", "undetermined": "Unknown",
}

def normalize_logic_answer(ans):
    s = ans.strip()
    if s.startswith('\\text{'):
        s = s[len('\\text{'):]
        if s.endswith('}'): s = s[:-1]
        s = s.strip()
    return _LOGIC_CANONICAL.get(s.lower(), s)


def oracle_sica(traces, z3_answer):
    """
    Oracle SICA: Z3 oracle answer determines the correct answer.
    Traces matching Z3 answer get weight, others don't.
    If Z3 answer not in trace candidates, fall back to SC.
    """
    answer_counts = Counter(t["answer"] for t in traces if t.get("answer"))
    candidates = sorted(answer_counts.keys())
    if not candidates:
        return "", {}, {}

    sc_answer = max(candidates, key=lambda a: answer_counts[a])

    scores = {}
    for cand in candidates:
        if cand == z3_answer:
            scores[cand] = answer_counts[cand]
        else:
            scores[cand] = -answer_counts[cand]

    if z3_answer in candidates:
        oracle_answer = z3_answer
    else:
        oracle_answer = sc_answer

    stats = {
        "z3_answer": z3_answer,
        "z3_in_candidates": z3_answer in candidates,
        "z3_support_count": answer_counts.get(z3_answer, 0),
    }
    return oracle_answer, scores, stats


def normal_cdf_approx(x):
    a1, a2, a3 = 0.254829592, -0.284496736, 1.421413741
    a4, a5 = -1.453152027, 1.061405429
    p_const = 0.3275911
    sign = 1 if x >= 0 else -1
    x = abs(x) / sqrt(2)
    t = 1.0 / (1.0 + p_const * x)
    y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * exp(-x * x)
    return 0.5 * (1.0 + sign * y)

def mcnemar_test(results, key_a, key_b):
    b = sum(1 for r in results if r[key_a] and not r[key_b])
    c = sum(1 for r in results if not r[key_a] and r[key_b])
    if b + c > 0:
        chi2 = (abs(b - c) - 1) ** 2 / (b + c)
        p = 2 * (1 - normal_cdf_approx(sqrt(chi2)))
    else:
        chi2, p = 0, 1.0
    return chi2, p, b, c


def main():
    base_dir = "/root/symb_invariant_consensus"
    data_path = os.path.join(base_dir, "data/folio_full.json")
    traces_dir = os.path.join(base_dir, "results/folio_204_14b/intermediates")
    output_dir = os.path.join(base_dir, "results/oracle_folio_regen")
    os.makedirs(output_dir, exist_ok=True)

    with open(data_path) as f:
        gold_data = json.load(f)
    gold_by_id = {p["id"]: p for p in gold_data}
    logger.info("Loaded %d FOLIO problems", len(gold_data))

    trace_files = sorted(
        [f for f in os.listdir(traces_dir) if f.endswith(".json")],
        key=lambda x: int(re.search(r'(\d+)', x).group(1))
    )
    logger.info("Found %d trace files", len(trace_files))

    parser = FOLParser()
    results = []
    C = {"oracle": 0, "sc": 0, "sica_self": 0, "z3_agree": 0, "parse_ok": 0, "z3_in_cand": 0}
    n = 0
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
        sc_answer = max(candidates, key=lambda a: answer_counts[a]) if candidates else ""
        sica_self_answer = normalize_logic_answer(sica_result.get("answer", ""))

        parser.reset()
        z3_premises = []
        parse_ok = True
        for fol in premises_fol:
            z3_expr = parser.parse(fol)
            if z3_expr is not None:
                z3_premises.append(z3_expr)
            else:
                parse_ok = False

        z3_conclusion = parser.parse(conclusion_fol) if conclusion_fol else None
        if z3_conclusion is None and conclusion_fol:
            parse_ok = False

        if parse_ok: C["parse_ok"] += 1
        z3_answer = check_entailment(z3_premises, z3_conclusion) if parse_ok else None
        z3_agrees = (z3_answer == gold_answer) if z3_answer else False
        if z3_agrees: C["z3_agree"] += 1

        if z3_answer:
            oracle_answer, oracle_scores, oracle_stats = oracle_sica(traces, z3_answer)
            if z3_answer in candidates: C["z3_in_cand"] += 1
        else:
            oracle_answer = sc_answer
            oracle_scores = dict(answer_counts)
            oracle_stats = {"fallback": "no_z3_answer"}

        oracle_correct = (oracle_answer == gold_answer)
        sc_correct = (sc_answer == gold_answer)
        sica_self_correct = (sica_self_answer == gold_answer)

        if oracle_correct: C["oracle"] += 1
        if sc_correct: C["sc"] += 1
        if sica_self_correct: C["sica_self"] += 1
        n += 1

        results.append({
            "problem_id": prob_id,
            "gold_answer": gold_answer,
            "z3_answer": z3_answer,
            "z3_agrees_gold": z3_agrees,
            "oracle_answer": oracle_answer,
            "oracle_correct": oracle_correct,
            "oracle_scores": {k: round(v, 2) for k, v in oracle_scores.items()} if oracle_scores else {},
            "sc_answer": sc_answer,
            "sc_correct": sc_correct,
            "sica_self_answer": sica_self_answer,
            "sica_self_correct": sica_self_correct,
            "answer_counts": dict(answer_counts),
            "fol_parse_ok": parse_ok,
            "oracle_stats": oracle_stats,
        })

        if (fi + 1) % 50 == 0 or fi == len(trace_files) - 1:
            logger.info(
                "[%d/%d] oracle=%.2f%% sc=%.2f%% z3_agree=%.2f%% (%.1fs)",
                fi+1, len(trace_files),
                100*C["oracle"]/n, 100*C["sc"]/n, 100*C["z3_agree"]/n,
                time.time()-t_start
            )

    total_time = time.time() - t_start
    oa = C["oracle"]/n; sa = C["sc"]/n; sia = C["sica_self"]/n; za = C["z3_agree"]/n

    chi2_os, p_os, b_os, c_os = mcnemar_test(results, "oracle_correct", "sc_correct")
    chi2_oss, p_oss, b_oss, c_oss = mcnemar_test(results, "oracle_correct", "sica_self_correct")

    # Analyze Z3 failures
    z3_wrong = [r for r in results if r["z3_answer"] and r["z3_answer"] != r["gold_answer"]]
    z3_no_cand = [r for r in results if r.get("oracle_stats", {}).get("z3_in_candidates") == False and r["z3_agrees_gold"]]

    summary = {
        "n": n, "k": 12,
        "oracle_sica_accuracy": round(oa, 4),
        "sc_accuracy": round(sa, 4),
        "sica_self_accuracy": round(sia, 4),
        "oracle_vs_sc_delta_pp": round((oa-sa)*100, 2),
        "oracle_vs_sica_delta_pp": round((oa-sia)*100, 2),
        "mcnemar_p_oracle_vs_sc": float(f"{p_os:.4e}"),
        "mcnemar_b_c_oracle_vs_sc": {"b": b_os, "c": c_os},
        "mcnemar_p_oracle_vs_sica": float(f"{p_oss:.4e}"),
        "z3_gold_agreement": round(za, 4),
        "z3_gold_agree_n": C["z3_agree"],
        "z3_gold_total": n,
        "z3_in_candidates_n": C["z3_in_cand"],
        "fol_parse_success": round(C["parse_ok"]/n, 4),
        "fol_parse_ok_n": C["parse_ok"],
        "model": "Qwen2.5-14B-Instruct",
        "dataset": "FOLIO-204",
        "constraint_source": "gold FOL annotations",
        "traces_source": "exp-026-folio204-trace-regen",
        "wall_time_s": round(total_time, 1),
    }

    per_answer = {}
    for at in ["True", "False", "Unknown"]:
        sub = [r for r in results if r["gold_answer"] == at]
        if sub:
            per_answer[at] = {
                "n": len(sub),
                "oracle_acc": round(sum(1 for r in sub if r["oracle_correct"])/len(sub), 4),
                "sc_acc": round(sum(1 for r in sub if r["sc_correct"])/len(sub), 4),
                "sica_self_acc": round(sum(1 for r in sub if r["sica_self_correct"])/len(sub), 4),
                "z3_agree": round(sum(1 for r in sub if r["z3_agrees_gold"])/len(sub), 4),
                "z3_no_trace_support": sum(1 for r in sub if r["z3_agrees_gold"]
                                           and r.get("oracle_stats",{}).get("z3_in_candidates") == False),
            }
    summary["per_answer_type"] = per_answer
    summary["comparison_exp021"] = {
        "exp021_oracle": 0.8824, "exp021_sc": 0.7941, "exp021_z3_agree": 0.946,
        "exp031_oracle": round(oa, 4), "exp031_sc": round(sa, 4), "exp031_z3_agree": round(za, 4),
        "note": "exp-021: old traces pre-normalization-fix; exp-031: exp-026 traces post-fix",
    }

    output = {"summary": summary, "results": results}
    out_path = os.path.join(output_dir, "exp031_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    with open(os.path.join(output_dir, "exp031_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

    print("\n" + "="*70)
    print("Oracle SICA Results (exp-031-oracle-folio-regen)")
    print("="*70)
    print(f"N = {n}, K = 12")
    print(f"FOL parse success:      {C['parse_ok']}/{n} ({C['parse_ok']/n*100:.1f}%)")
    print(f"Z3 gold agreement:      {C['z3_agree']}/{n} ({za*100:.2f}%)")
    print(f"Z3 answer in traces:    {C['z3_in_cand']}/{n}")
    print()
    print(f"Oracle SICA accuracy:   {oa:.4f} ({C['oracle']}/{n})")
    print(f"SC accuracy:            {sa:.4f} ({C['sc']}/{n})")
    print(f"SICA(self) accuracy:    {sia:.4f} ({C['sica_self']}/{n})")
    print(f"Oracle vs SC delta:     {(oa-sa)*100:+.2f}pp")
    print(f"Oracle vs SICA delta:   {(oa-sia)*100:+.2f}pp")
    print(f"McNemar p (oracle vs SC):   {p_os:.4e}  (b={b_os}, c={c_os})")
    print(f"McNemar p (oracle vs SICA): {p_oss:.4e}  (b={b_oss}, c={c_oss})")
    print()
    print("Per answer type:")
    print(f"  {'Type':8s}  {'n':>3s}  {'Oracle':>7s}  {'SC':>7s}  {'SICA':>7s}  {'Z3agr':>7s}  {'NoSup':>5s}")
    for at, st in per_answer.items():
        print(f"  {at:8s}  {st['n']:3d}  {st['oracle_acc']:7.3f}  {st['sc_acc']:7.3f}  {st['sica_self_acc']:7.3f}  {st['z3_agree']:7.3f}  {st['z3_no_trace_support']:5d}")
    print()

    # Error analysis: where oracle fails
    oracle_wrong = [r for r in results if not r["oracle_correct"]]
    z3_right_oracle_wrong = [r for r in oracle_wrong if r["z3_agrees_gold"]]
    z3_wrong_all = [r for r in results if r["z3_answer"] and r["z3_answer"] != r["gold_answer"]]
    print("Error analysis:")
    print(f"  Oracle wrong total:            {len(oracle_wrong)}")
    print(f"  Z3 right but oracle wrong:     {len(z3_right_oracle_wrong)} (z3 answer not in traces)")
    print(f"  Z3 wrong total:                {len(z3_wrong_all)}")
    sc_on_z3wrong = sum(1 for r in z3_wrong_all if r["sc_correct"])
    print(f"  Z3 wrong, SC correct:          {sc_on_z3wrong}/{len(z3_wrong_all)}")
    print()
    print("Comparison with exp-021:")
    print(f"  exp-021: oracle={0.8824:.4f}  sc={0.7941:.4f}  z3_agree={0.946:.3f}")
    print(f"  exp-031: oracle={oa:.4f}  sc={sa:.4f}  z3_agree={za:.3f}")
    print(f"\nWall time: {total_time:.1f}s")
    print(f"Results: {out_path}")
    print("EXP031_DONE")


if __name__ == "__main__":
    main()

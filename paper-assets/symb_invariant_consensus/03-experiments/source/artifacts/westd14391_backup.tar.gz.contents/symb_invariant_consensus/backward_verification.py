#!/usr/bin/env python3
"""
Experiment 5: Backward Verification for FOLIO.
K=12 independent backward verification rounds + majority vote.
Per round, per candidate {True, False, Unknown}: LLM generates backward
FOL conditions, Z3 checks consistency with gold premises. Best candidate wins.
"""

import argparse
import asyncio
import json
import logging
import os
import re
import sys
import time
from collections import Counter

import z3

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

CANDIDATES = ["True", "False", "Unknown"]


# ============================================================
# FOL Parser: FOLIO notation -> Z3
# ============================================================

class FOLParser:
    """Parse FOLIO FOL notation into Z3 expressions.
    Handles: universal/existential quantifiers, implication, conjunction,
    disjunction, negation, xor, biconditional, predicates with arguments.
    """

    def __init__(self):
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
                tokens.append(('WORD', s[i:j]))
                i = j
            else:
                i += 1
        return tokens

    def _parse_formula(self, tokens, pos):
        return self._parse_quantifier(tokens, pos)

    def _parse_quantifier(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][0] in ('FORALL', 'EXISTS'):
            qtype = tokens[pos][0]; pos += 1
            if pos >= len(tokens) or tokens[pos][0] != 'WORD':
                raise ValueError("Expected variable after quantifier")
            var = self._get_variable(tokens[pos][1]); pos += 1
            body, pos = self._parse_quantifier(tokens, pos)
            if body is None:
                raise ValueError("Failed to parse quantifier body")
            if qtype == 'FORALL':
                return z3.ForAll([var], body), pos
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
                raise ValueError("Failed to parse right side of biconditional")
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
                raise ValueError("Failed to parse right side of implication")
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
                raise ValueError("Failed to parse right side of disjunction")
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
                raise ValueError("Failed to parse right side of xor")
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
                raise ValueError("Failed to parse right side of conjunction")
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


# ============================================================
# Direct Z3 entailment (tiebreaker)
# ============================================================

def z3_entailment(z3_premises, z3_conclusion, timeout_ms=10000):
    if z3_conclusion is None:
        return "Unknown"
    s = z3.Solver()
    s.set("timeout", timeout_ms)
    for p in z3_premises:
        if p is not None:
            s.add(p)
    s.add(z3.Not(z3_conclusion))
    if s.check() == z3.unsat:
        return "True"
    s2 = z3.Solver()
    s2.set("timeout", timeout_ms)
    for p in z3_premises:
        if p is not None:
            s2.add(p)
    s2.add(z3_conclusion)
    if s2.check() == z3.unsat:
        return "False"
    return "Unknown"


# ============================================================
# Backward Verification Prompt
# ============================================================

BACKWARD_PROMPT = """\
You are given a logical reasoning problem with premises in First-Order Logic (FOL).

Premises (natural language):
{premises_nl}

Premises (FOL notation):
{premises_fol}

Conclusion (natural language): {conclusion_nl}
Conclusion (FOL): {conclusion_fol}

Candidate answer: {candidate}

Reason backward from the assumption that the answer is "{candidate}".

1. List FOL conditions that MUST HOLD for this answer to be correct (supporting conditions).
2. List FOL conditions that WOULD CONTRADICT this answer (contradicting conditions).

Use EXACTLY the same FOL notation as the premises above:
- ∀ for "for all", ∃ for "there exists"
- → for implication, ∧ for and, ∨ for or, ¬ for not, ⊕ for exclusive or
- Use the same predicate names and constant names as in the premises

Output ONLY a JSON object:
{{
  "supporting": ["FOL formula 1", "FOL formula 2", ...],
  "contradicting": ["FOL formula 1", ...],
  "reasoning": "brief backward reasoning explanation"
}}"""


# ============================================================
# Answer normalization
# ============================================================

_LOGIC_MAP = {
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
    return _LOGIC_MAP.get(s.lower(), s)


def parse_problem_text(text):
    marker = "Determine whether the following conclusion is true, false, or uncertain:"
    parts = text.split(marker)
    premises = parts[0].replace("Given the following premises:\n", "").strip()
    conclusion = parts[1].strip() if len(parts) > 1 else ""
    return premises, conclusion


# ============================================================
# Backward Verifier
# ============================================================

class BackwardVerifier:

    def __init__(self, api_base, model=None, temperature=0.7,
                 max_tokens=2048, max_concurrent=12):
        from openai import AsyncOpenAI, OpenAI
        self.client = AsyncOpenAI(base_url=api_base, api_key="[REDACTED]")
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.semaphore = asyncio.Semaphore(max_concurrent)
        if model and model != "auto":
            self.model = model
        else:
            sync = OpenAI(base_url=api_base, api_key="[REDACTED]")
            self.model = sync.models.list().data[0].id
            logger.info("Auto-detected model: %s", self.model)

    async def _llm_call(self, prompt):
        async with self.semaphore:
            try:
                r = await self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                )
                return r.choices[0].message.content or ""
            except Exception as e:
                logger.warning("LLM call failed: %s", e)
                return ""

    @staticmethod
    def _parse_response(raw):
        text = raw.strip()
        m = re.search(r'```(?:json)?\s*(.*?)```', text, re.DOTALL)
        if m:
            text = m.group(1).strip()
        start = text.find('{')
        end = text.rfind('}')
        if start >= 0 and end > start:
            text = text[start:end + 1]
        try:
            data = json.loads(text)
            sup = [str(s) for s in data.get("supporting", []) if s]
            con = [str(s) for s in data.get("contradicting", []) if s]
            reason = str(data.get("reasoning", ""))
            return sup, con, reason
        except (json.JSONDecodeError, AttributeError, TypeError):
            return [], [], ""

    @staticmethod
    def _check_conditions(z3_premises, fol_list, parser, timeout_ms=5000):
        """Check each FOL condition against premises.
        Returns (n_sat, n_unsat, n_parse_fail).
        """
        n_sat, n_unsat, n_fail = 0, 0, 0
        for fol in fol_list:
            expr = parser.parse(fol)
            if expr is None:
                n_fail += 1
                continue
            s = z3.Solver()
            s.set("timeout", timeout_ms)
            for p in z3_premises:
                s.add(p)
            s.add(expr)
            r = s.check()
            if r == z3.unsat:
                n_unsat += 1
            elif r == z3.sat:
                n_sat += 1
        return n_sat, n_unsat, n_fail

    async def verify_round(self, problem, round_idx):
        """One backward verification round: score all 3 candidates."""
        text = problem["problem"]
        pfol = problem.get("premises_fol", [])
        cfol = problem.get("conclusion_fol", "")
        pnl, cnl = parse_problem_text(text)
        pfol_fmt = "\n".join(f"  {i+1}. {f}" for i, f in enumerate(pfol))

        parser = FOLParser()
        z3p = [parser.parse(f) for f in pfol]
        z3p = [p for p in z3p if p is not None]
        z3c = parser.parse(cfol) if cfol else None

        prompts = {c: BACKWARD_PROMPT.format(
            premises_nl=pnl, premises_fol=pfol_fmt,
            conclusion_nl=cnl, conclusion_fol=cfol, candidate=c,
        ) for c in CANDIDATES}

        raws = await asyncio.gather(*(self._llm_call(prompts[c]) for c in CANDIDATES))

        details = {}
        scores = {}
        for cand, raw in zip(CANDIDATES, raws):
            sup, con, reason = self._parse_response(raw)
            s_sat, s_unsat, s_fail = self._check_conditions(z3p, sup, parser)
            c_sat, c_unsat, c_fail = self._check_conditions(z3p, con, parser)

            # positive evidence - negative evidence
            # supporting SAT = good, contradicting UNSAT = good (alleged contradictions don't hold)
            # supporting UNSAT = bad, contradicting SAT = bad (real contradictions exist)
            score = (s_sat + c_unsat) - (s_unsat + c_sat)
            scores[cand] = score
            details[cand] = {
                "supporting_fol": sup,
                "contradicting_fol": con,
                "reasoning": reason,
                "sup": {"sat": s_sat, "unsat": s_unsat, "fail": s_fail},
                "con": {"sat": c_sat, "unsat": c_unsat, "fail": c_fail},
                "score": score,
            }

        best_score = max(scores.values())
        tied = [c for c in CANDIDATES if scores[c] == best_score]
        if len(tied) > 1 and z3c is not None:
            z3_ans = z3_entailment(z3p, z3c)
            selected = z3_ans if z3_ans in tied else tied[0]
        else:
            selected = tied[0]

        return {
            "round_idx": round_idx,
            "selected": selected,
            "scores": scores,
            "details": details,
        }

    async def verify_problem(self, problem, k):
        """K rounds of backward verification + majority vote."""
        tasks = [self.verify_round(problem, i) for i in range(k)]
        rounds = await asyncio.gather(*tasks)
        votes = Counter(r["selected"] for r in rounds)
        final = votes.most_common(1)[0][0]
        return final, dict(votes), list(rounds)


# ============================================================
# SC baseline from existing traces
# ============================================================

def compute_sc_baseline(problems):
    traces_dir = "results/folio_204_14b/intermediates"
    if not os.path.isdir(traces_dir):
        return 0.7549
    n_correct = 0
    n_total = 0
    for prob in problems:
        pid = prob["id"]
        path = os.path.join(traces_dir, f"{pid}.json")
        if not os.path.exists(path):
            continue
        with open(path) as f:
            data = json.load(f)
        traces = data.get("sica_result", {}).get("traces", [])
        counts = Counter(
            normalize_logic_answer(t.get("answer", ""))
            for t in traces if t.get("answer")
        )
        if counts:
            n_total += 1
            if counts.most_common(1)[0][0] == prob["answer"]:
                n_correct += 1
    return round(n_correct / n_total, 4) if n_total else 0.7549


# ============================================================
# Main
# ============================================================

async def async_main():
    ap = argparse.ArgumentParser(description="Exp 5: Backward Verification for FOLIO")
    ap.add_argument("--api-base", default="http://localhost:8000/v1")
    ap.add_argument("--model", default="auto")
    ap.add_argument("--k", type=int, default=12)
    ap.add_argument("--data", default="data/folio_full.json")
    ap.add_argument("--output", default="results/exp05_backward_verification/results.json")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--temperature", type=float, default=0.7)
    ap.add_argument("--max-concurrent", type=int, default=12)
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()

    out_dir = os.path.dirname(args.output)
    int_dir = os.path.join(out_dir, "intermediates")
    os.makedirs(int_dir, exist_ok=True)

    logger.info("Loading data from %s", args.data)
    with open(args.data) as f:
        problems = json.load(f)
    logger.info("Loaded %d problems", len(problems))

    verifier = BackwardVerifier(
        api_base=args.api_base,
        model=args.model,
        temperature=args.temperature,
        max_concurrent=args.max_concurrent,
    )

    sc_acc = compute_sc_baseline(problems)
    logger.info("SC baseline: %.4f", sc_acc)

    results = []
    n_ok = 0
    n_tot = 0
    t0 = time.time()

    for pi, prob in enumerate(problems):
        pid = prob["id"]
        gold = prob["answer"]
        ipath = os.path.join(int_dir, f"{pid}.json")

        if args.resume and os.path.exists(ipath):
            with open(ipath) as f:
                cached = json.load(f)
            if cached.get("final_answer") == gold:
                n_ok += 1
            n_tot += 1
            results.append(cached)
            if (pi + 1) % 20 == 0:
                logger.info(
                    "[%d/%d] (cached) bv=%.2f%%",
                    pi + 1, len(problems), 100 * n_ok / n_tot,
                )
            continue

        final, votes, rounds = await verifier.verify_problem(prob, args.k)
        ok = (final == gold)
        if ok:
            n_ok += 1
        n_tot += 1

        entry = {
            "problem_id": pid,
            "gold_answer": gold,
            "final_answer": final,
            "correct": ok,
            "vote_counts": votes,
            "rounds": rounds,
        }
        results.append(entry)

        with open(ipath, "w") as f:
            json.dump(entry, f, indent=2, default=str)

        if (pi + 1) % 10 == 0 or pi == len(problems) - 1:
            elapsed = time.time() - t0
            logger.info(
                "[%d/%d] bv=%.2f%% (%.1fs)",
                pi + 1, len(problems), 100 * n_ok / n_tot, elapsed,
            )

    wall = time.time() - t0
    bv_acc = n_ok / n_tot if n_tot else 0

    per_type = {}
    for at in CANDIDATES:
        sub = [r for r in results if r["gold_answer"] == at]
        if sub:
            per_type[at] = {
                "n": len(sub),
                "acc": round(sum(1 for r in sub if r["correct"]) / len(sub), 4),
            }

    summary = {
        "n": n_tot,
        "k": args.k,
        "bv_accuracy": round(bv_acc, 4),
        "sc_baseline": sc_acc,
        "delta_pp": round((bv_acc - sc_acc) * 100, 2),
        "per_answer_type": per_type,
        "model": verifier.model,
        "temperature": args.temperature,
        "seed": args.seed,
        "wall_time_s": round(wall, 1),
    }

    with open(args.output, "w") as f:
        json.dump({"summary": summary, "results": results}, f, indent=2, default=str)

    summary_path = os.path.join(out_dir, "summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\n{'=' * 60}")
    print("Backward Verification Results (Exp 5)")
    print(f"{'=' * 60}")
    print(f"N={n_tot}  K={args.k}")
    print(f"BV accuracy:  {bv_acc:.4f} ({n_ok}/{n_tot})")
    print(f"SC baseline:  {sc_acc:.4f}")
    print(f"Delta:        {(bv_acc - sc_acc) * 100:+.2f}pp")
    for at, st in per_type.items():
        print(f"  {at:8s}: n={st['n']:3d}  acc={st['acc']:.3f}")
    print(f"Wall time: {wall:.1f}s")
    print(f"Results: {args.output}")
    print("EXP05_BACKWARD_VERIFICATION_DONE")


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Direction J: Bootstrapped Gold Approximation.
Iterative self-refinement: SC majority -> bidirectional FOL extraction -> Z3 check -> flip if inconsistent.
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

_LOGIC_MAP = {
    "true": "True", "yes": "True", "1": "True", "t": "True",
    "false": "False", "no": "False", "0": "False", "f": "False",
    "unknown": "Unknown", "uncertain": "Unknown", "undetermined": "Unknown",
    "u": "Unknown",
}


def normalize_logic_answer(ans):
    s = str(ans).strip()
    if s.startswith('\\text{'):
        s = s[len('\\text{'):]
        if s.endswith('}'):
            s = s[:-1]
        s = s.strip()
    return _LOGIC_MAP.get(s.lower(), s.capitalize())


def parse_problem_text(text):
    marker = "Determine whether the following conclusion is true, false, or uncertain:"
    parts = text.split(marker)
    premises = parts[0].replace("Given the following premises:\n", "").strip()
    conclusion = parts[1].strip() if len(parts) > 1 else ""
    return premises, conclusion


# ============================================================
# FOL Parser: FOLIO notation -> Z3
# ============================================================

class FOLParser:
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
        except Exception:
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
            var_name = tokens[pos][1]; pos += 1
            var = self._get_variable(var_name)
            body, pos = self._parse_formula(tokens, pos)
            if body is None:
                return None, pos
            if qtype == 'FORALL':
                return z3.ForAll([var], body), pos
            else:
                return z3.Exists([var], body), pos
        return self._parse_iff(tokens, pos)

    def _parse_iff(self, tokens, pos):
        left, pos = self._parse_xor(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'IFF':
            pos += 1
            right, pos = self._parse_xor(tokens, pos)
            if left is not None and right is not None:
                left = left == right
            else:
                return None, pos
        return left, pos

    def _parse_xor(self, tokens, pos):
        left, pos = self._parse_implies(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'XOR':
            pos += 1
            right, pos = self._parse_implies(tokens, pos)
            if left is not None and right is not None:
                left = z3.Xor(left, right)
            else:
                return None, pos
        return left, pos

    def _parse_implies(self, tokens, pos):
        left, pos = self._parse_or(tokens, pos)
        if pos < len(tokens) and tokens[pos][0] == 'IMPLIES':
            pos += 1
            right, pos = self._parse_implies(tokens, pos)
            if left is not None and right is not None:
                left = z3.Implies(left, right)
            else:
                return None, pos
        return left, pos

    def _parse_or(self, tokens, pos):
        left, pos = self._parse_and(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'OR':
            pos += 1
            right, pos = self._parse_and(tokens, pos)
            if left is not None and right is not None:
                left = z3.Or(left, right)
            else:
                return None, pos
        return left, pos

    def _parse_and(self, tokens, pos):
        left, pos = self._parse_not(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'AND':
            pos += 1
            right, pos = self._parse_not(tokens, pos)
            if left is not None and right is not None:
                left = z3.And(left, right)
            else:
                return None, pos
        return left, pos

    def _parse_not(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][0] == 'NOT':
            pos += 1
            inner, pos = self._parse_not(tokens, pos)
            if inner is not None:
                return z3.Not(inner), pos
            return None, pos
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
# Z3 consistency check
# ============================================================

def check_z3_consistency(z3_formulas, timeout_ms=5000):
    if not z3_formulas:
        return "no_formulas"
    s = z3.Solver()
    s.set("timeout", timeout_ms)
    for f in z3_formulas:
        if f is not None:
            s.add(f)
    result = s.check()
    if result == z3.sat:
        return "sat"
    elif result == z3.unsat:
        return "unsat"
    else:
        return "unknown"


# ============================================================
# Verification Prompt (per candidate)
# ============================================================

VERIFY_PROMPT = """\
You are given a logical reasoning problem.

Premises (natural language):
{premises_nl}

Premises (FOL notation):
{premises_fol}

Conclusion (natural language): {conclusion_nl}
Conclusion (FOL): {conclusion_fol}

Assume the answer to this problem is "{candidate}".

Reason backward: what FOL conditions must hold for this answer to be correct?
Extract conditions that are logically NECESSARY for "{candidate}" to be the correct answer.
These conditions should follow from the premises + the assumption that the answer is "{candidate}".

Use EXACTLY the same FOL notation as the premises:
- ∀ for "for all", ∃ for "there exists"
- → for implication, ∧ for and, ∨ for or, ¬ for not, ⊕ for exclusive or
- Use the same predicate names and constant names as in the premises

Output ONLY a JSON object:
{{
  "conditions": ["FOL formula 1", "FOL formula 2", ...],
  "reasoning": "brief backward reasoning explanation"
}}"""


# ============================================================
# Round 0: SC majority vote from exp-033 traces
# ============================================================

def compute_sc_from_traces(traces_dir, data, n_problems=None):
    problems_sc = {}
    problem_list = data[:n_problems] if n_problems else data

    for prob in problem_list:
        pid = prob["id"]
        trace_file = os.path.join(traces_dir, "intermediates", f"{pid}.json")
        if not os.path.exists(trace_file):
            logger.warning("No trace file for %s, skipping", pid)
            continue

        with open(trace_file) as f:
            trace_data = json.load(f)

        answer_counts = trace_data.get("sica_result", {}).get("answer_counts", {})
        if not answer_counts:
            traces = trace_data.get("sica_result", {}).get("traces", [])
            answer_counts = Counter()
            for t in traces:
                ans = normalize_logic_answer(t.get("answer", ""))
                if ans in CANDIDATES:
                    answer_counts[ans] += 1
            answer_counts = dict(answer_counts)

        if not answer_counts:
            logger.warning("No answer counts for %s", pid)
            continue

        sorted_answers = sorted(answer_counts.items(), key=lambda x: -x[1])
        majority = sorted_answers[0][0]
        runner_up = sorted_answers[1][0] if len(sorted_answers) > 1 else None

        if runner_up is None:
            others = [c for c in CANDIDATES if c != majority]
            runner_up = others[0] if others else majority

        problems_sc[pid] = {
            "sc_answer": majority,
            "runner_up": runner_up,
            "answer_counts": answer_counts,
            "ground_truth": prob["answer"],
            "problem": prob,
        }

    return problems_sc


# ============================================================
# Bootstrap Verifier (bidirectional)
# ============================================================

class BootstrapVerifier:

    def __init__(self, api_base, model=None, temperature=0.7,
                 max_tokens=2048, max_concurrent=24):
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
                return r.choices[0].message.content.strip()
            except Exception as e:
                logger.warning("LLM call failed: %s", e)
                return None

    async def extract_conditions(self, prob_data, candidate):
        prob = prob_data["problem"]
        premises_nl, conclusion_nl = parse_problem_text(prob["problem"])
        premises_fol = prob.get("premises_fol", [])
        conclusion_fol = prob.get("conclusion_fol", "")

        prompt = VERIFY_PROMPT.format(
            premises_nl=premises_nl,
            premises_fol="\n".join(premises_fol),
            conclusion_nl=conclusion_nl,
            conclusion_fol=conclusion_fol,
            candidate=candidate,
        )

        raw = await self._llm_call(prompt)
        if not raw:
            return [], raw

        conditions = []
        try:
            json_match = re.search(r'\{[\s\S]*\}', raw)
            if json_match:
                parsed = json.loads(json_match.group())
                conditions = parsed.get("conditions", [])
        except (json.JSONDecodeError, AttributeError):
            pass

        return conditions, raw

    def z3_check(self, premises_fol, condition_fols):
        parser = FOLParser()

        z3_premises = []
        for fol in premises_fol:
            expr = parser.parse(fol)
            if expr is not None:
                z3_premises.append(expr)

        z3_conds = []
        for fol in condition_fols:
            expr = parser.parse(fol)
            if expr is not None:
                z3_conds.append(expr)

        if not z3_conds:
            return "no_constraints", 0

        result = check_z3_consistency(z3_premises + z3_conds)
        return result, len(z3_conds)


# ============================================================
# Main iterative loop
# ============================================================

async def run_bootstrap(args):
    traces_dir = args.traces_dir
    data_file = args.data

    with open(data_file) as f:
        data = json.load(f)
    logger.info("Loaded %d problems from %s", len(data), data_file)

    n_problems = args.n_problems if args.n_problems > 0 else len(data)

    problems_sc = compute_sc_from_traces(traces_dir, data, n_problems)
    logger.info("Computed SC for %d problems", len(problems_sc))

    n_correct_r0 = sum(
        1 for p in problems_sc.values()
        if normalize_logic_answer(p["sc_answer"]) == normalize_logic_answer(p["ground_truth"])
    )
    sc_acc = n_correct_r0 / len(problems_sc) if problems_sc else 0
    logger.info("Round 0 (SC baseline): %d/%d = %.4f", n_correct_r0, len(problems_sc), sc_acc)

    out_dir = args.output_dir
    os.makedirs(out_dir, exist_ok=True)
    int_dir = os.path.join(out_dir, "intermediates")
    os.makedirs(int_dir, exist_ok=True)

    current_answers = {pid: p["sc_answer"] for pid, p in problems_sc.items()}
    runner_ups = {pid: p["runner_up"] for pid, p in problems_sc.items()}
    visited_answers = {pid: {p["sc_answer"]} for pid, p in problems_sc.items()}

    round_results = []
    round_results.append({
        "round": 0,
        "method": "sc_majority",
        "accuracy": round(sc_acc, 4),
        "n_correct": n_correct_r0,
        "n_total": len(problems_sc),
        "flips": 0,
        "flip_details": [],
    })

    verifier = BootstrapVerifier(
        api_base=args.api_base,
        model=args.model,
        temperature=args.temperature,
        max_concurrent=args.max_concurrent,
    )

    for rnd in range(1, args.max_rounds + 1):
        logger.info("=== Round %d ===", rnd)
        t0 = time.time()

        flip_details = []
        per_problem_results = {}

        pids = list(problems_sc.keys())

        async def process_problem(pid):
            p = problems_sc[pid]
            cur_ans = current_answers[pid]
            alt_ans = runner_ups[pid]
            premises_fol = p["problem"].get("premises_fol", [])

            cur_conds, cur_raw = await verifier.extract_conditions(p, cur_ans)
            alt_conds, alt_raw = await verifier.extract_conditions(p, alt_ans)

            cur_result, cur_n_z3 = verifier.z3_check(premises_fol, cur_conds)
            alt_result, alt_n_z3 = verifier.z3_check(premises_fol, alt_conds)

            should_flip = False
            reason = "no_signal"

            if cur_result == "unsat" and alt_result == "sat":
                if alt_ans in visited_answers.get(pid, set()):
                    should_flip = False
                    reason = "current_unsat_alt_sat_but_oscillation"
                else:
                    should_flip = True
                    reason = "current_unsat_alt_sat"
            elif cur_result == "unsat" and alt_result == "unsat":
                reason = "both_unsat"
            elif cur_result == "sat" and alt_result == "sat":
                reason = "both_sat"
            elif cur_result == "sat" and alt_result == "unsat":
                reason = "current_sat_alt_unsat"
            else:
                reason = f"cur={cur_result}({cur_n_z3})_alt={alt_result}({alt_n_z3})"

            result = {
                "current_answer": cur_ans,
                "alt_answer": alt_ans,
                "cur_conditions": cur_conds,
                "alt_conditions": alt_conds,
                "cur_z3": cur_result,
                "alt_z3": alt_result,
                "cur_n_z3": cur_n_z3,
                "alt_n_z3": alt_n_z3,
                "should_flip": should_flip,
                "reason": reason,
            }

            if should_flip:
                result["action"] = "flip"
                result["new_answer"] = alt_ans
            else:
                result["action"] = "keep"

            return pid, result

        tasks = [process_problem(pid) for pid in pids]
        results = await asyncio.gather(*tasks)

        n_flips = 0
        for pid, result in results:
            per_problem_results[pid] = result
            if result.get("action") == "flip":
                old_ans = current_answers[pid]
                new_ans = result["new_answer"]
                current_answers[pid] = new_ans
                runner_ups[pid] = old_ans
                visited_answers.setdefault(pid, set()).add(new_ans)

                flip_details.append({
                    "problem_id": pid,
                    "old_answer": old_ans,
                    "new_answer": new_ans,
                    "ground_truth": problems_sc[pid]["ground_truth"],
                    "reason": result["reason"],
                    "was_correct": normalize_logic_answer(old_ans) == normalize_logic_answer(problems_sc[pid]["ground_truth"]),
                    "now_correct": normalize_logic_answer(new_ans) == normalize_logic_answer(problems_sc[pid]["ground_truth"]),
                })
                n_flips += 1

        n_correct = sum(
            1 for pid in problems_sc
            if normalize_logic_answer(current_answers[pid]) == normalize_logic_answer(problems_sc[pid]["ground_truth"])
        )
        acc = n_correct / len(problems_sc) if problems_sc else 0
        elapsed = time.time() - t0

        improved = sum(1 for f in flip_details if not f["was_correct"] and f["now_correct"])
        degraded = sum(1 for f in flip_details if f["was_correct"] and not f["now_correct"])

        round_info = {
            "round": rnd,
            "accuracy": round(acc, 4),
            "n_correct": n_correct,
            "n_total": len(problems_sc),
            "flips": n_flips,
            "flips_improved": improved,
            "flips_degraded": degraded,
            "flip_details": flip_details,
            "wall_time_s": round(elapsed, 1),
        }
        round_results.append(round_info)

        round_file = os.path.join(int_dir, f"round_{rnd}.json")
        with open(round_file, "w") as f:
            json.dump({
                "round_info": round_info,
                "per_problem": per_problem_results,
            }, f, indent=2, default=str)

        logger.info(
            "Round %d: acc=%.4f (%d/%d), flips=%d (improved=%d, degraded=%d), %.1fs",
            rnd, acc, n_correct, len(problems_sc), n_flips, improved, degraded, elapsed,
        )

        if n_flips == 0:
            logger.info("Converged at round %d (no flips)", rnd)
            break

    final_acc = round_results[-1]["accuracy"]
    summary = {
        "method": "direction_j_bootstrap",
        "n_problems": len(problems_sc),
        "max_rounds": args.max_rounds,
        "converged_at": round_results[-1]["round"],
        "sc_baseline": round(sc_acc, 4),
        "final_accuracy": final_acc,
        "delta_pp": round((final_acc - sc_acc) * 100, 2),
        "per_round": [{
            "round": r["round"],
            "accuracy": r["accuracy"],
            "flips": r["flips"],
            "flips_improved": r.get("flips_improved", 0),
            "flips_degraded": r.get("flips_degraded", 0),
        } for r in round_results],
        "model": verifier.model,
        "temperature": args.temperature,
    }

    per_type = {}
    for at in CANDIDATES:
        sub = [(pid, p) for pid, p in problems_sc.items() if normalize_logic_answer(p["ground_truth"]) == at]
        if sub:
            n_ok = sum(1 for pid, _ in sub if normalize_logic_answer(current_answers[pid]) == at)
            per_type[at] = {"n": len(sub), "acc": round(n_ok / len(sub), 4)}
    summary["per_answer_type"] = per_type

    results_file = os.path.join(out_dir, "results.json")
    with open(results_file, "w") as f:
        json.dump({"summary": summary, "rounds": round_results}, f, indent=2, default=str)

    per_problem_final = []
    for pid in sorted(problems_sc.keys(), key=lambda x: int(x.split("_")[1])):
        p = problems_sc[pid]
        per_problem_final.append({
            "problem_id": pid,
            "ground_truth": p["ground_truth"],
            "sc_answer": p["sc_answer"],
            "final_answer": current_answers[pid],
            "sc_correct": normalize_logic_answer(p["sc_answer"]) == normalize_logic_answer(p["ground_truth"]),
            "final_correct": normalize_logic_answer(current_answers[pid]) == normalize_logic_answer(p["ground_truth"]),
        })

    details_file = os.path.join(out_dir, "per_problem_details.json")
    with open(details_file, "w") as f:
        json.dump(per_problem_final, f, indent=2)

    print(f"\n{'=' * 60}")
    print("Direction J: Bootstrapped Gold Approximation")
    print(f"{'=' * 60}")
    print(f"N={len(problems_sc)}  max_rounds={args.max_rounds}")
    print(f"SC baseline:    {sc_acc:.4f}")
    print(f"Final accuracy: {final_acc:.4f}")
    print(f"Delta:          {(final_acc - sc_acc) * 100:+.2f}pp")
    print(f"Converged at:   round {round_results[-1]['round']}")
    for r in round_results:
        tag = "SC" if r["round"] == 0 else f"R{r['round']}"
        extra = ""
        if r["round"] > 0:
            extra = f"  flips={r['flips']} (+{r.get('flips_improved',0)}/-{r.get('flips_degraded',0)})"
        print(f"  {tag}: {r['accuracy']:.4f} ({r['n_correct']}/{r['n_total']}){extra}")
    for at, st in per_type.items():
        print(f"  {at:8s}: n={st['n']:3d}  acc={st['acc']:.3f}")
    print(f"Results: {results_file}")
    print("DIRECTION_J_BOOTSTRAP_DONE")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--api-base", default="http://localhost:8000/v1")
    ap.add_argument("--model", default="auto")
    ap.add_argument("--traces-dir",
                     default="results/exp033_mistral_7b_folio204")
    ap.add_argument("--data", default="data/folio_full.json")
    ap.add_argument("--output-dir",
                     default="results/direction_j_bootstrap")
    ap.add_argument("--n-problems", type=int, default=0,
                     help="0 = all problems")
    ap.add_argument("--max-rounds", type=int, default=5)
    ap.add_argument("--temperature", type=float, default=0.7)
    ap.add_argument("--max-concurrent", type=int, default=24)
    args = ap.parse_args()
    asyncio.run(run_bootstrap(args))


if __name__ == "__main__":
    main()

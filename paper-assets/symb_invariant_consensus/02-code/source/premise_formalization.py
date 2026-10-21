"""
Premise-Only Formalization baseline for FOLIO.
Directly formalizes NL premises and conclusion into grounded Z3 boolean
formulas, checks logical entailment via Z3, and uses K-way majority vote.
Input: folio_full.json (premises + conclusion in natural language)
Output: per-problem predictions with accuracy metrics
Dependencies: z3-solver, openai, tqdm
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

import z3
from openai import OpenAI

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------

FORMALIZATION_PROMPT = '''You are a logic formalization expert. Translate natural language premises and a conclusion into Z3 Python boolean formulas for propositional satisfiability checking.

**Instructions:**
1. Identify every named entity in the problem (people, objects, etc.).
2. Identify every predicate (properties / relations).
3. Ground all universal/existential statements for the named entities only.
   - "All X are Y" with entities {{a, b}} -> And(Implies(X_a, Y_a), Implies(X_b, Y_b))
   - "Some X are Y" with entities {{a}} -> Or(And(X_a, Y_a))
   - "either A or B (exclusive or)" -> Or(And(A, Not(B)), And(Not(A), B))
4. Variable naming: predicate_entity, all lowercase with underscores.
   Examples: talentshows_bonnie, manager_james, eats_bear_squirrel
5. Z3 operators: And(...), Or(...), Not(...), Implies(a, b), Xor(a, b), == True, == False
6. If a premise is a simple ground fact about a specific entity, express it as var == True or var == False.
7. Keep formulas as simple and faithful to the NL meaning as possible.

**Output ONLY a valid JSON object (no markdown, no explanation):**
{{"entities": ["entity1", "entity2"], "premises": ["Z3 formula 1", "Z3 formula 2"], "conclusion": "Z3 formula for conclusion"}}

**Premises:**
{premises}

**Conclusion:**
{conclusion}'''

# ---------------------------------------------------------------------------
# NL parsing
# ---------------------------------------------------------------------------

def parse_problem(problem_text: str) -> tuple[list[str], str]:
    """Extract premises list and conclusion string from FOLIO problem text."""
    parts = re.split(
        r'Determine whether the following conclusion is true,\s*false,\s*or uncertain:\s*',
        problem_text,
    )
    if len(parts) < 2:
        parts = re.split(r'Determine whether', problem_text, maxsplit=1)
        if len(parts) >= 2:
            conclusion = parts[1].strip().lstrip(':').strip()
            premise_text = parts[0]
        else:
            return [], problem_text.strip()
    else:
        premise_text = parts[0]
        conclusion = parts[1].strip()

    premise_text = re.sub(r'^Given the following premises:\s*', '', premise_text).strip()
    raw = re.split(r'(?<=\.)\s{2,}|(?<=\.)\s*\n\s*|(?<=\.)\s+(?=[A-Z])', premise_text)
    premises = [p.strip().rstrip('.').strip() for p in raw if p.strip()]
    premises = [p + '.' if not p.endswith('.') else p for p in premises if p]
    return premises, conclusion

# ---------------------------------------------------------------------------
# Z3 formula parsing (lightweight, with Xor support)
# ---------------------------------------------------------------------------

_RESERVED = {
    'True', 'False', 'And', 'Or', 'Not', 'Implies', 'If', 'Xor',
    'Bool', 'abs', 'Abs', 'ForAll', 'Exists',
}

def parse_formula(formula_str: str) -> z3.ExprRef | None:
    """Parse a Z3 boolean formula string into a z3 expression. Supports Xor."""
    if not formula_str or not formula_str.strip():
        return None
    s = formula_str.strip()
    tokens = set(re.findall(r'\b([a-zA-Z_]\w*)\b', s))
    var_names = tokens - _RESERVED

    ns: dict = {}
    for name in var_names:
        ns[name] = z3.Bool(name)

    ns['And'] = z3.And
    ns['Or'] = z3.Or
    ns['Not'] = z3.Not
    ns['Implies'] = z3.Implies
    ns['If'] = z3.If
    ns['Xor'] = z3.Xor
    ns['True'] = True
    ns['False'] = False

    try:
        result = eval(s, {"__builtins__": {}}, ns)
        if isinstance(result, z3.ExprRef) and z3.is_bool(result):
            return result
        if isinstance(result, bool):
            return z3.BoolVal(result)
        return None
    except Exception as e:
        logger.debug("Failed to parse formula '%s': %s", s, e)
        return None

# ---------------------------------------------------------------------------
# LLM formalization
# ---------------------------------------------------------------------------

def _extract_json(text: str) -> str | None:
    """Extract the first balanced JSON object from text."""
    m = re.search(r'```(?:json)?\s*(.*?)\s*```', text, re.DOTALL)
    if m:
        return m.group(1).strip()
    depth = 0
    start = None
    for i, c in enumerate(text):
        if c == '{':
            if depth == 0:
                start = i
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0 and start is not None:
                return text[start:i + 1]
    return None


def _parse_formalization_response(raw: str) -> dict | None:
    """Parse JSON from LLM response."""
    text = re.sub(r'<think>.*?</think>', '', raw, flags=re.DOTALL).strip()
    json_str = _extract_json(text)
    if json_str is None:
        logger.debug("No JSON found in response: %.200s", text)
        return None
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        repaired = re.sub(r',\s*([}\]])', r'\1', json_str)
        try:
            data = json.loads(repaired)
        except json.JSONDecodeError:
            logger.debug("JSON parse failed: %.200s", json_str)
            return None
    if "premises" not in data or "conclusion" not in data:
        return None
    return data


def formalize_with_llm(
    client: OpenAI, model: str,
    premises: list[str], conclusion: str,
    temperature: float = 0.7, max_tokens: int = 2048,
) -> dict | None:
    """Call LLM to formalize premises and conclusion into Z3 formulas."""
    premises_text = "\n".join(f"{i + 1}. {p}" for i, p in enumerate(premises))
    prompt = FORMALIZATION_PROMPT.format(premises=premises_text, conclusion=conclusion)
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        raw = resp.choices[0].message.content.strip()
        return _parse_formalization_response(raw)
    except Exception as e:
        logger.warning("LLM call failed: %s", e)
        return None

# ---------------------------------------------------------------------------
# Z3 entailment check
# ---------------------------------------------------------------------------

def check_entailment(premise_strs: list[str], conclusion_str: str,
                     timeout_ms: int = 5000) -> str:
    """Check P1 ^ ... ^ Pn |= C via Z3. Returns 'True' / 'False' / 'Unknown'."""
    parsed_premises = []
    for ps in premise_strs:
        f = parse_formula(ps)
        if f is not None:
            parsed_premises.append(f)

    if not parsed_premises:
        return "Unknown"

    conc = parse_formula(conclusion_str)
    if conc is None:
        return "Unknown"

    premises_conj = z3.And(*parsed_premises) if len(parsed_premises) > 1 else parsed_premises[0]

    # Premises consistent?
    s0 = z3.Solver()
    s0.set('timeout', timeout_ms)
    s0.add(premises_conj)
    if s0.check() == z3.unsat:
        return "Unknown"

    # P ^ ~C unsat? -> True
    s1 = z3.Solver()
    s1.set('timeout', timeout_ms)
    s1.add(premises_conj)
    s1.add(z3.Not(conc))
    if s1.check() == z3.unsat:
        return "True"

    # P ^ C unsat? -> False
    s2 = z3.Solver()
    s2.set('timeout', timeout_ms)
    s2.add(premises_conj)
    s2.add(conc)
    if s2.check() == z3.unsat:
        return "False"

    return "Unknown"

# ---------------------------------------------------------------------------
# Single formalization attempt
# ---------------------------------------------------------------------------

def run_single(client: OpenAI, model: str,
               premises: list[str], conclusion: str,
               temperature: float = 0.7) -> dict:
    """One formalization + Z3 check."""
    fml = formalize_with_llm(client, model, premises, conclusion,
                             temperature=temperature)
    if fml is None:
        return {"answer": None, "error": "formalization_failed", "formalization": None}
    prem_fs = fml.get("premises", [])
    conc_f = fml.get("conclusion", "")
    if not prem_fs or not conc_f:
        return {"answer": None, "error": "empty_formulas", "formalization": fml}
    answer = check_entailment(prem_fs, conc_f)
    return {"answer": answer, "error": None, "formalization": fml}

# ---------------------------------------------------------------------------
# Majority vote
# ---------------------------------------------------------------------------

def majority_vote(answers: list[str | None]) -> str:
    valid = [a for a in answers if a is not None]
    if not valid:
        return "Unknown"
    return Counter(valid).most_common(1)[0][0]

# ---------------------------------------------------------------------------
# Per-problem runner (parallel K attempts)
# ---------------------------------------------------------------------------

def run_problem(client: OpenAI, model: str, problem: dict,
                k: int = 12, temperature: float = 0.7,
                max_workers: int = 4) -> dict:
    """Run K formalization attempts and vote."""
    premises, conclusion = parse_problem(problem["problem"])
    pid = problem.get("id", "?")
    if not premises:
        logger.warning("No premises parsed for %s", pid)
        return _empty_result(problem, "no_premises_parsed")

    attempts: list[dict] = []
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = [
            pool.submit(run_single, client, model, premises, conclusion, temperature)
            for _ in range(k)
        ]
        for fut in as_completed(futures):
            attempts.append(fut.result())

    answers = [a["answer"] for a in attempts]
    predicted = majority_vote(answers)
    return {
        "id": pid,
        "gold": problem.get("answer"),
        "predicted": predicted,
        "answers": answers,
        "answer_counts": dict(Counter(a for a in answers if a is not None)),
        "formalizations": [a["formalization"] for a in attempts],
        "premises_nl": premises,
        "conclusion_nl": conclusion,
        "num_valid": sum(1 for a in answers if a is not None),
    }


def _empty_result(problem: dict, error: str) -> dict:
    return {
        "id": problem.get("id"),
        "gold": problem.get("answer"),
        "predicted": "Unknown",
        "answers": [],
        "answer_counts": {},
        "formalizations": [],
        "error": error,
    }

# ---------------------------------------------------------------------------
# Checkpoint I/O
# ---------------------------------------------------------------------------

def save_checkpoint(args, results: list[dict], total_problems: int, path: str):
    correct = sum(1 for r in results if r["predicted"] == r["gold"])
    total = len(results)
    out = {
        "config": {
            "model": args.model, "k": args.k,
            "temperature": args.temperature, "seed": args.seed,
            "data": args.data, "total_problems": total_problems,
        },
        "accuracy": correct / total if total else 0,
        "correct": correct,
        "total": total,
        "results": results,
    }
    with open(path, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Premise-Only Formalization for FOLIO")
    ap.add_argument("--api-base", required=True, help="vLLM OpenAI-compat base URL")
    ap.add_argument("--model", default="Qwen2.5-14B-Instruct")
    ap.add_argument("--k", type=int, default=12)
    ap.add_argument("--data", default="data/folio_full.json")
    ap.add_argument("--output", default="results/premise_formalization/results.json")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--temperature", type=float, default=0.7)
    ap.add_argument("--max-problems", type=int, default=None)
    ap.add_argument("--max-workers", type=int, default=4, help="Parallel LLM calls per problem")
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()

    with open(args.data) as f:
        problems = json.load(f)
    if args.max_problems:
        problems = problems[:args.max_problems]
    logger.info("Loaded %d problems", len(problems))

    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    completed: dict[str, dict] = {}
    if args.resume and os.path.exists(args.output):
        with open(args.output) as f:
            ckpt = json.load(f)
        for r in ckpt.get("results", []):
            completed[r["id"]] = r
        logger.info("Resumed %d completed problems", len(completed))

    client = OpenAI(base_url=args.api_base, api_key="[REDACTED]")

    results = list(completed.values())
    remaining = [p for p in problems if p.get("id") not in completed]
    logger.info("Running %d remaining problems (K=%d)", len(remaining), args.k)

    for idx, problem in enumerate(remaining):
        t0 = time.time()
        result = run_problem(client, args.model, problem, k=args.k,
                             temperature=args.temperature,
                             max_workers=args.max_workers)
        elapsed = time.time() - t0
        results.append(result)

        ok = result["predicted"] == result["gold"]
        logger.info(
            "[%d/%d] %s: pred=%s gold=%s %s (%.1fs, valid=%d/%d)",
            idx + 1, len(remaining), result["id"],
            result["predicted"], result["gold"],
            "OK" if ok else "WRONG", elapsed,
            result.get("num_valid", 0), args.k,
        )

        if (idx + 1) % 5 == 0 or idx == len(remaining) - 1:
            save_checkpoint(args, results, len(problems), args.output)

    save_checkpoint(args, results, len(problems), args.output)

    # Final report
    correct = sum(1 for r in results if r["predicted"] == r["gold"])
    total = len(results)
    logger.info("=" * 60)
    logger.info("Final accuracy: %d/%d = %.2f%%", correct, total,
                100 * correct / total if total else 0)
    for ans in ["True", "False", "Unknown"]:
        sub = [r for r in results if r["gold"] == ans]
        if sub:
            c = sum(1 for r in sub if r["predicted"] == r["gold"])
            logger.info("  %s: %d/%d = %.2f%%", ans, c, len(sub),
                        100 * c / len(sub))

    # Parse success rate
    all_valid = sum(r.get("num_valid", 0) for r in results)
    all_total = len(results) * args.k
    logger.info("Parse success: %d/%d = %.1f%%", all_valid, all_total,
                100 * all_valid / all_total if all_total else 0)


if __name__ == "__main__":
    main()

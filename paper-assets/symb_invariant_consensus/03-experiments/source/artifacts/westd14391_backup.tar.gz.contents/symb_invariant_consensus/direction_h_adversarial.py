"""
Direction H: Adversarial Negation Extraction
For each trace's answer, extract "refutation constraints" — assume the answer is wrong,
find logical reasons. Use Z3 to check if refutation is satisfiable.
UNSAT refutation → high confidence (irrefutable), SAT → low confidence (refutable).
"""
import argparse
import json
import logging
import os
import re
import sys
import time
from collections import Counter
from pathlib import Path

import z3
from openai import OpenAI

z3.set_param('smt.random_seed', 42)
z3.set_param('sat.random_seed', 42)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

REFUTATION_PROMPT = """You are given a logical reasoning problem with premises and a reasoning trace that concludes with the answer "{answer}".

Your task: Assume the answer "{answer}" is WRONG. Extract logical constraints from the premises that would CONTRADICT this answer.

Premises (natural language):
{premises}

Reasoning trace (excerpt):
{trace_text}

The trace concluded: {answer}

Now, assuming "{answer}" is wrong, extract Z3 boolean constraints that prove it wrong.

STRICT Z3 SYNTAX RULES:
- Variables: lowercase_with_underscores only (e.g., tall_bob, likes_alice)
- And(a, b): conjunction — NEVER write "a And b", ALWAYS use And(a, b)
- Or(a, b): disjunction — NEVER write "a Or b", ALWAYS use Or(a, b)
- Not(a): negation
- Implies(a, b): implication
- == True / == False: boolean assertion
- EVERY formula must be a valid Python expression using ONLY these operators

Example output:
{{"refutation_constraints": [{{"expression": "If Bob is tall then Bob is kind", "z3_formula": "Implies(tall_bob, kind_bob)", "reason": "premise contradicts answer"}}, {{"expression": "Bob is tall", "z3_formula": "tall_bob == True", "reason": "given fact"}}, {{"expression": "Bob is not kind", "z3_formula": "kind_bob == False", "reason": "negation of concluded answer"}}], "alternative_answer": "True"}}

Output ONLY valid JSON, no other text:"""


def _preprocess_z3(s: str) -> str:
    s = s.strip()
    s = re.sub(r'\)\s+And\s+(?![\(])', '), ', s)
    s = re.sub(r'\)\s+Or\s+(?![\(])', '), ', s)
    s = re.sub(r'(?<![A-Za-z_])and(?![A-Za-z_])', ',', s)
    s = re.sub(r'(?<![A-Za-z_])or(?![A-Za-z_])', ',', s)
    s = re.sub(r'¬\s*(\w+)', r'Not(\1)', s)
    s = re.sub(r'→', '->', s)
    if '->' in s and 'Implies' not in s:
        parts = s.split('->', 1)
        if len(parts) == 2:
            s = f"Implies({parts[0].strip()}, {parts[1].strip()})"
    return s


def parse_z3_formula(formula_str: str) -> "z3.ExprRef | None":
    if not formula_str or not formula_str.strip():
        return None
    s = _preprocess_z3(formula_str)
    tokens = set(re.findall(r'\b([a-zA-Z_]\w*)\b', s))
    reserved = {
        'True', 'False', 'And', 'Or', 'Not', 'Implies', 'If',
        'abs', 'Bool', 'Real', 'Int', 'sum', 'max', 'min',
    }
    var_names = tokens - reserved
    ns = {}
    for name in var_names:
        ns[name] = z3.Bool(name)
    ns.update({
        'And': z3.And, 'Or': z3.Or, 'Not': z3.Not,
        'Implies': z3.Implies, 'If': z3.If,
        'True': True, 'False': False,
    })
    try:
        result = eval(s, {"__builtins__": {}}, ns)
        if isinstance(result, bool):
            return z3.BoolVal(result)
        if not isinstance(result, z3.ExprRef):
            return None
        if not z3.is_bool(result):
            return None
        return result
    except Exception:
        return None


def check_refutation_sat(formulas: list) -> str:
    if not formulas:
        return "empty"
    solver = z3.Solver()
    solver.set("timeout", 5000)
    for f in formulas:
        solver.add(f)
    result = solver.check()
    if result == z3.sat:
        return "sat"
    elif result == z3.unsat:
        return "unsat"
    else:
        return "unknown"


def extract_json_from_response(text: str) -> dict | None:
    text = text.strip()
    m = re.search(r'```(?:json)?\s*(.*?)```', text, re.DOTALL)
    if m:
        text = m.group(1).strip()
    for start in range(len(text)):
        if text[start] == '{':
            for end in range(len(text), start, -1):
                if text[end-1] == '}':
                    try:
                        return json.loads(text[start:end])
                    except json.JSONDecodeError:
                        continue
    return None


def load_traces(data_dir: str, limit: int | None = None) -> list[dict]:
    files = sorted(Path(data_dir).glob("folio_*.json"), key=lambda p: int(p.stem.split("_")[1]))
    if limit:
        files = files[:limit]
    problems = []
    for f in files:
        with open(f) as fh:
            problems.append(json.load(fh))
    return problems


def run_adversarial(
    problems: list[dict],
    client: OpenAI,
    model: str,
    temperature: float = 0.3,
) -> dict:
    results = []
    total_traces = 0
    total_refutation_extracted = 0
    total_z3_compiled = 0
    sat_count = 0
    unsat_count = 0
    unknown_count = 0
    empty_count = 0
    failed_formulas = []

    for pidx, prob_data in enumerate(problems):
        prob = prob_data["problem"]
        prob_id = prob["id"]
        gold = prob["answer"]
        premises_text = prob["problem"].split("\n\nDetermine")[0]
        traces = prob_data["sica_result"]["traces"]

        trace_results = []
        for tidx, t in enumerate(traces):
            trace_answer = t.get("answer", "").strip()
            if not trace_answer:
                trace_results.append({
                    "trace_idx": t.get("trace_idx", tidx),
                    "answer": trace_answer,
                    "status": "no_answer",
                    "refutation_sat": None,
                    "n_constraints": 0,
                    "n_compiled": 0,
                })
                continue

            total_traces += 1
            prompt = REFUTATION_PROMPT.format(
                answer=trace_answer,
                premises=premises_text,
                trace_text=t["trace"][:3000],
            )
            try:
                resp = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=temperature,
                    max_tokens=1500,
                )
                raw = resp.choices[0].message.content
            except Exception as e:
                logger.warning("LLM call failed for %s trace %d: %s", prob_id, tidx, e)
                trace_results.append({
                    "trace_idx": t.get("trace_idx", tidx),
                    "answer": trace_answer,
                    "status": "llm_error",
                    "refutation_sat": None,
                    "n_constraints": 0,
                    "n_compiled": 0,
                })
                continue

            parsed = extract_json_from_response(raw)
            if not parsed or "refutation_constraints" not in parsed:
                trace_results.append({
                    "trace_idx": t.get("trace_idx", tidx),
                    "answer": trace_answer,
                    "status": "parse_error",
                    "refutation_sat": None,
                    "n_constraints": 0,
                    "n_compiled": 0,
                    "raw_response": raw[:500],
                })
                continue

            total_refutation_extracted += 1
            constraints = parsed["refutation_constraints"]
            z3_formulas = []
            raw_z3_strs = []
            for c in constraints:
                formula_str = c.get("z3_formula", "")
                raw_z3_strs.append(formula_str)
                f = parse_z3_formula(formula_str)
                if f is not None:
                    z3_formulas.append(f)
                else:
                    failed_formulas.append(formula_str)
            total_z3_compiled += len(z3_formulas)

            if not z3_formulas:
                sat_status = "empty"
                empty_count += 1
            else:
                sat_status = check_refutation_sat(z3_formulas)
                if sat_status == "sat":
                    sat_count += 1
                elif sat_status == "unsat":
                    unsat_count += 1
                else:
                    unknown_count += 1

            trace_results.append({
                "trace_idx": t.get("trace_idx", tidx),
                "answer": trace_answer,
                "status": "ok",
                "refutation_sat": sat_status,
                "n_constraints": len(constraints),
                "n_compiled": len(z3_formulas),
                "alternative_answer": parsed.get("alternative_answer", ""),
                "raw_z3_formulas": raw_z3_strs,
            })

        # --- Per-problem aggregation ---
        answer_refutation = {}
        for tr in trace_results:
            ans = tr["answer"]
            if not ans:
                continue
            if ans not in answer_refutation:
                answer_refutation[ans] = {"total": 0, "unsat": 0, "sat": 0, "unknown": 0, "empty": 0, "error": 0}
            answer_refutation[ans]["total"] += 1
            rs = tr.get("refutation_sat")
            if rs == "unsat":
                answer_refutation[ans]["unsat"] += 1
            elif rs == "sat":
                answer_refutation[ans]["sat"] += 1
            elif rs == "unknown":
                answer_refutation[ans]["unknown"] += 1
            elif rs == "empty":
                answer_refutation[ans]["empty"] += 1
            else:
                answer_refutation[ans]["error"] += 1

        irrefutability = {}
        for ans, stats in answer_refutation.items():
            denom = stats["total"] - stats["error"] - stats["empty"]
            irrefutability[ans] = stats["unsat"] / denom if denom > 0 else 0.0

        sc_votes = Counter(tr["answer"] for tr in trace_results if tr["answer"])
        sc_answer = sc_votes.most_common(1)[0][0] if sc_votes else ""

        # Variant 1: Adversarial-only (highest irrefutability)
        adv_only = max(irrefutability, key=irrefutability.get) if irrefutability else sc_answer

        # Variant 2: Adversarial-weighted SC
        weighted_scores = {}
        for tr in trace_results:
            ans = tr["answer"]
            if not ans:
                continue
            rs = tr.get("refutation_sat")
            if rs == "unsat":
                w = 2.0
            elif rs == "sat":
                w = 0.5
            else:
                w = 1.0
            weighted_scores[ans] = weighted_scores.get(ans, 0) + w
        adv_weighted = max(weighted_scores, key=weighted_scores.get) if weighted_scores else sc_answer

        # Variant 3: Adversarial-filter (keep only irrefutable traces, then SC)
        filtered_answers = [tr["answer"] for tr in trace_results if tr.get("refutation_sat") == "unsat" and tr["answer"]]
        if filtered_answers:
            fc = Counter(filtered_answers)
            adv_filter = fc.most_common(1)[0][0]
        else:
            adv_filter = sc_answer

        results.append({
            "problem_id": prob_id,
            "gold": gold,
            "sc_answer": sc_answer,
            "adv_only_answer": adv_only,
            "adv_weighted_answer": adv_weighted,
            "adv_filter_answer": adv_filter,
            "answer_refutation": answer_refutation,
            "irrefutability": irrefutability,
            "trace_results": trace_results,
        })

        sc_ok = "Y" if sc_answer == gold else "N"
        adv_ok = "Y" if adv_weighted == gold else "N"
        logger.info(
            "[%d/%d] %s gold=%s SC=%s(%s) AdvW=%s(%s) irrefut=%s",
            pidx+1, len(problems), prob_id, gold,
            sc_answer, sc_ok, adv_weighted, adv_ok,
            {k: f"{v:.2f}" for k, v in irrefutability.items()},
        )

    # --- Global metrics ---
    def acc(key):
        correct = sum(1 for r in results if r[key] == r["gold"])
        return correct / len(results) if results else 0

    summary = {
        "n_problems": len(results),
        "accuracy": {
            "sc": acc("sc_answer"),
            "adv_only": acc("adv_only_answer"),
            "adv_weighted": acc("adv_weighted_answer"),
            "adv_filter": acc("adv_filter_answer"),
        },
        "refutation_stats": {
            "total_traces": total_traces,
            "extraction_success": total_refutation_extracted,
            "z3_compiled": total_z3_compiled,
            "sat": sat_count,
            "unsat": unsat_count,
            "unknown": unknown_count,
            "empty": empty_count,
        },
        "flip_stats": {
            "sc_to_adv_weighted": sum(
                1 for r in results if r["sc_answer"] != r["adv_weighted_answer"]
            ),
            "flips_improved": sum(
                1 for r in results
                if r["sc_answer"] != r["adv_weighted_answer"]
                and r["adv_weighted_answer"] == r["gold"]
            ),
            "flips_degraded": sum(
                1 for r in results
                if r["sc_answer"] != r["adv_weighted_answer"]
                and r["sc_answer"] == r["gold"]
            ),
        },
        "failed_z3_samples": failed_formulas[:20],
    }

    return {"summary": summary, "results": results}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default="/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates")
    parser.add_argument("--output-dir", default="/root/symb_invariant_consensus/results/direction_h_adversarial")
    parser.add_argument("--port", type=int, default=8012)
    parser.add_argument("--model", default="/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3")
    parser.add_argument("--temperature", type=float, default=0.3)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.dry_run:
        args.limit = 5

    client = OpenAI(base_url=f"http://localhost:{args.port}/v1", api_key="[REDACTED]")

    logger.info("Loading traces from %s (limit=%s)", args.data_dir, args.limit)
    problems = load_traces(args.data_dir, limit=args.limit)
    logger.info("Loaded %d problems", len(problems))

    t0 = time.time()
    output = run_adversarial(problems, client, args.model, args.temperature)
    elapsed = time.time() - t0
    output["summary"]["elapsed_seconds"] = elapsed

    os.makedirs(args.output_dir, exist_ok=True)
    suffix = "_dryrun" if args.dry_run else ""
    out_path = os.path.join(args.output_dir, f"results{suffix}.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    logger.info("=== RESULTS ===")
    for k, v in output["summary"]["accuracy"].items():
        logger.info("  %s accuracy: %.2f%% (%d/%d)", k, v*100, int(v*len(output["results"])), len(output["results"]))
    logger.info("Refutation stats: %s", output["summary"]["refutation_stats"])
    logger.info("Flip stats: %s", output["summary"]["flip_stats"])
    if output["summary"]["failed_z3_samples"]:
        logger.info("Sample failed Z3: %s", output["summary"]["failed_z3_samples"][:5])
    logger.info("Saved to %s (%.1fs)", out_path, elapsed)


if __name__ == "__main__":
    main()

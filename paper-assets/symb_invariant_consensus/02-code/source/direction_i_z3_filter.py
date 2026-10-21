"""Direction I: Z3 Trace Filter — check per-trace constraint consistency."""

import json
import os
import re
import time
from collections import Counter
from pathlib import Path

import z3

CONSTRAINT_DIR = Path("/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache")
ANSWER_MATRIX = Path("/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/sc_answer_matrix.json")
OUTPUT_DIR = Path("/root/symb_invariant_consensus/results/direction_i_z3_filter")
N_PROBLEMS = 204
Z3_TIMEOUT_MS = 10_000

Z3_BUILTINS = {"Implies", "And", "Or", "Not", "Xor", "If", "Bool", "True", "False"}
IDENT_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


def extract_variables(formula_str: str) -> set:
    tokens = set(IDENT_RE.findall(formula_str))
    return tokens - Z3_BUILTINS


def parse_and_check_sat(constraints: list, timeout_ms: int = Z3_TIMEOUT_MS):
    """Parse z3_formula strings and check satisfiability of their conjunction.

    Returns: (status, n_parsed, n_failed)
      status: "SAT" | "UNSAT" | "TIMEOUT" | "PARSE_ERROR" | "EMPTY"
    """
    formulas_str = [c.get("z3_formula", "") for c in constraints]
    formulas_str = [f for f in formulas_str if f.strip()]

    if not formulas_str:
        return "EMPTY", 0, 0

    all_vars = set()
    for f in formulas_str:
        all_vars |= extract_variables(f)

    ns = {}
    for v in all_vars:
        ns[v] = z3.Bool(v)
    ns["Implies"] = z3.Implies
    ns["And"] = z3.And
    ns["Or"] = z3.Or
    ns["Not"] = z3.Not
    ns["Xor"] = z3.Xor
    ns["If"] = z3.If
    ns["True"] = z3.BoolVal(True)
    ns["False"] = z3.BoolVal(False)

    parsed = []
    n_failed = 0
    for f in formulas_str:
        try:
            expr = eval(f, {"__builtins__": {}}, ns)
            if z3.is_expr(expr):
                parsed.append(expr)
            elif isinstance(expr, bool):
                parsed.append(z3.BoolVal(expr))
            else:
                n_failed += 1
        except Exception:
            n_failed += 1

    if not parsed:
        return "PARSE_ERROR", 0, n_failed

    solver = z3.Solver()
    solver.set("timeout", timeout_ms)
    for p in parsed:
        solver.add(p)

    result = solver.check()
    if result == z3.sat:
        return "SAT", len(parsed), n_failed
    elif result == z3.unsat:
        return "UNSAT", len(parsed), n_failed
    else:
        return "TIMEOUT", len(parsed), n_failed


def majority_vote(answers: list) -> str:
    valid = [a for a in answers if a in ("True", "False", "Unknown")]
    if not valid:
        return ""
    counts = Counter(valid)
    return counts.most_common(1)[0][0]


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with open(ANSWER_MATRIX) as f:
        answer_matrix = json.load(f)

    total_traces = 0
    status_counts = Counter()
    filtered_count = 0
    sc_correct = 0
    filtered_sc_correct = 0
    n_problems_processed = 0

    unsat_correct = 0
    unsat_incorrect = 0
    unsat_empty = 0

    per_question = []
    t0 = time.time()

    for pid_idx in range(N_PROBLEMS):
        pid = f"folio_{pid_idx}"
        cache_path = CONSTRAINT_DIR / f"{pid}.json"
        if not cache_path.exists():
            continue

        with open(cache_path) as f:
            cache = json.load(f)

        gt = cache.get("gt", "")
        traces = cache.get("per_trace", [])
        am = answer_matrix.get(pid, {})
        am_answers = am.get("answers", [])

        trace_results = []
        kept_answers = []

        for t in traces:
            tidx = t.get("trace_idx", -1)
            answer = t.get("answer", "")
            constraints = t.get("constraints", [])

            status, n_parsed, n_fail = parse_and_check_sat(constraints)
            total_traces += 1
            status_counts[status] += 1

            trace_results.append({
                "trace_idx": tidx,
                "answer": answer,
                "status": status,
                "n_constraints": len(constraints),
                "n_parsed": n_parsed,
                "n_parse_failed": n_fail,
            })

            if status == "UNSAT":
                filtered_count += 1
                if answer == gt:
                    unsat_correct += 1
                elif answer in ("True", "False", "Unknown"):
                    unsat_incorrect += 1
                else:
                    unsat_empty += 1
            else:
                kept_answers.append(answer)

        sc_answer = majority_vote(am_answers)
        filtered_answer = majority_vote(kept_answers)

        sc_ok = (sc_answer == gt)
        filt_ok = (filtered_answer == gt)
        sc_correct += int(sc_ok)
        filtered_sc_correct += int(filt_ok)
        n_problems_processed += 1

        n_unsat = sum(1 for tr in trace_results if tr["status"] == "UNSAT")
        per_question.append({
            "pid": pid,
            "gt": gt,
            "n_traces": len(traces),
            "n_unsat": n_unsat,
            "n_kept": len(traces) - n_unsat,
            "sc_answer": sc_answer,
            "filtered_answer": filtered_answer,
            "sc_correct": sc_ok,
            "filtered_correct": filt_ok,
            "changed": sc_answer != filtered_answer,
            "trace_details": trace_results,
        })

        if pid_idx % 50 == 0:
            print(f"  [{pid_idx}/{N_PROBLEMS}] elapsed={time.time()-t0:.1f}s")

    elapsed = time.time() - t0
    sc_acc = sc_correct / n_problems_processed if n_problems_processed else 0
    filt_acc = filtered_sc_correct / n_problems_processed if n_problems_processed else 0

    n_changed = sum(1 for q in per_question if q["changed"])
    n_improved = sum(1 for q in per_question if q["changed"] and q["filtered_correct"] and not q["sc_correct"])
    n_degraded = sum(1 for q in per_question if q["changed"] and q["sc_correct"] and not q["filtered_correct"])

    filter_dist = Counter(q["n_unsat"] for q in per_question)

    results = {
        "summary": {
            "n_problems": n_problems_processed,
            "total_traces": total_traces,
            "sc_accuracy": round(sc_acc, 6),
            "filtered_sc_accuracy": round(filt_acc, 6),
            "sc_correct": sc_correct,
            "filtered_sc_correct": filtered_sc_correct,
            "delta": round(filt_acc - sc_acc, 6),
            "total_filtered": filtered_count,
            "filter_rate": round(filtered_count / total_traces, 4) if total_traces else 0,
            "elapsed_s": round(elapsed, 1),
        },
        "status_distribution": dict(status_counts),
        "unsat_answer_quality": {
            "correct_answers_filtered": unsat_correct,
            "incorrect_answers_filtered": unsat_incorrect,
            "empty_answers_filtered": unsat_empty,
            "precision_of_filter": round(
                unsat_incorrect / (unsat_correct + unsat_incorrect), 4
            ) if (unsat_correct + unsat_incorrect) > 0 else None,
        },
        "change_analysis": {
            "n_changed": n_changed,
            "n_improved": n_improved,
            "n_degraded": n_degraded,
        },
        "filter_distribution": {str(k): v for k, v in sorted(filter_dist.items())},
        "per_question": per_question,
    }

    out_path = OUTPUT_DIR / "results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'='*60}")
    print(f"Direction I: Z3 Trace Filter Results")
    print(f"{'='*60}")
    print(f"Problems: {n_problems_processed}")
    print(f"Total traces: {total_traces}")
    print(f"Status distribution: {dict(status_counts)}")
    print(f"Filter rate: {filtered_count}/{total_traces} = {filtered_count/total_traces:.2%}")
    print(f"")
    print(f"SC accuracy (baseline):   {sc_correct}/{n_problems_processed} = {sc_acc:.4f}")
    print(f"Filtered-SC accuracy:     {filtered_sc_correct}/{n_problems_processed} = {filt_acc:.4f}")
    print(f"Delta:                    {filt_acc - sc_acc:+.4f}")
    print(f"")
    print(f"UNSAT traces — correct answers: {unsat_correct}, incorrect: {unsat_incorrect}, empty: {unsat_empty}")
    prec = unsat_incorrect / (unsat_correct + unsat_incorrect) if (unsat_correct + unsat_incorrect) > 0 else 0
    print(f"Filter precision (% incorrect among filtered): {prec:.2%}")
    print(f"")
    print(f"Questions changed: {n_changed}  (improved: {n_improved}, degraded: {n_degraded})")
    print(f"")
    print(f"Per-question UNSAT count distribution:")
    for k in sorted(filter_dist.keys()):
        print(f"  {k} UNSAT traces: {filter_dist[k]} questions")
    print(f"\nElapsed: {elapsed:.1f}s")
    print(f"Results saved to {out_path}")


if __name__ == "__main__":
    main()

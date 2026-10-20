"""MATH Pilot 50-problem output capture audit.

Analyzes pilot_50.jsonl to categorize problems by code execution output status
and compute per-category accuracy, identifying the empty-output confound.
"""

import json
import sys
from collections import defaultdict

DATA_PATH = "data/math-counterfactual/pilot_50.jsonl"


def load_records(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def classify_record(r):
    det = r.get("deterministic", {})
    execs = det.get("code_executions", [])

    if len(execs) == 0:
        return "C"  # no code execution

    success_empty_rounds = []
    for j, e in enumerate(execs):
        if e.get("success", False) and e.get("output", "").strip() == "":
            success_empty_rounds.append(j)

    if success_empty_rounds:
        return "B"  # has at least one success+empty output
    return "A"  # all outputs non-empty


def analyze():
    records = load_records(DATA_PATH)
    n = len(records)

    categories = {"A": [], "B": [], "C": []}
    for r in records:
        cat = classify_record(r)
        categories[cat].append(r)

    print("=" * 60)
    print("MATH Pilot Output Audit")
    print("=" * 60)
    print(f"Total problems: {n}")
    print()

    for cat, label in [
        ("A", "code executed, output non-empty"),
        ("B", "code executed, output EMPTY"),
        ("C", "no code execution"),
    ]:
        recs = categories[cat]
        cnt = len(recs)
        pct = 100 * cnt / n if n else 0

        det_correct = sum(1 for r in recs if r["deterministic"]["correct"])
        int_correct = sum(1 for r in recs if r["internal"]["correct"])
        det_acc = 100 * det_correct / cnt if cnt else 0
        int_acc = 100 * int_correct / cnt if cnt else 0

        print(f"Category {cat} ({label}): {cnt} ({pct:.0f}%)")
        print(f"  CodeInterp accuracy: {det_correct}/{cnt} = {det_acc:.1f}%")
        print(f"  Internal accuracy:   {int_correct}/{cnt} = {int_acc:.1f}%")

        if cat == "B":
            print(f"  --- Per-problem detail ---")
            for r in recs:
                eid = r["episode_id"]
                det = r["deterministic"]
                execs = det["code_executions"]
                det_ok = "Y" if det["correct"] else "N"
                int_ok = "Y" if r["internal"]["correct"] else "N"

                exec_summary = []
                for j, e in enumerate(execs):
                    out_len = len(e.get("output", ""))
                    has_print = "print(" in e.get("code", "")
                    lines = [l.strip() for l in e.get("code", "").strip().split("\n")
                             if l.strip() and not l.strip().startswith("#")]
                    last_line = lines[-1] if lines else ""
                    exec_summary.append(
                        f"round{j}: success={e['success']}, "
                        f"out_len={out_len}, print={has_print}, "
                        f"last_line='{last_line[:60]}'"
                    )

                print(f"    {eid}: det={det_ok} int={int_ok}")
                for s in exec_summary:
                    print(f"      {s}")

        if cat == "C":
            print(f"  --- Per-problem detail ---")
            for r in recs:
                det_ok = "Y" if r["deterministic"]["correct"] else "N"
                int_ok = "Y" if r["internal"]["correct"] else "N"
                print(f"    {r['episode_id']}: det={det_ok} int={int_ok} "
                      f"n_rounds={r['deterministic']['n_rounds']}")

        print()

    # Overall summary
    all_det_correct = sum(1 for r in records if r["deterministic"]["correct"])
    all_int_correct = sum(1 for r in records if r["internal"]["correct"])

    a_recs = categories["A"]
    a_det = sum(1 for r in a_recs if r["deterministic"]["correct"]) if a_recs else 0
    a_n = len(a_recs)

    code_recs = categories["A"] + categories["B"]
    code_det = sum(1 for r in code_recs if r["deterministic"]["correct"])
    code_n = len(code_recs)

    b_n = len(categories["B"])
    total_execs = sum(
        len(r["deterministic"]["code_executions"])
        for r in records
        if r["deterministic"]["code_executions"]
    )
    empty_execs = 0
    for r in records:
        for e in r["deterministic"].get("code_executions", []):
            if e.get("success") and e.get("output", "").strip() == "":
                empty_execs += 1

    print("=" * 60)
    print("Overall Summary")
    print("=" * 60)
    print(f"  Internal accuracy (all):                  {all_int_correct}/{n} = {100*all_int_correct/n:.1f}%")
    print(f"  CodeInterp accuracy (all):                {all_det_correct}/{n} = {100*all_det_correct/n:.1f}%")
    print(f"  CodeInterp accuracy (A only, clean):      {a_det}/{a_n} = {100*a_det/a_n:.1f}%" if a_n else "  n/a")
    print(f"  CodeInterp accuracy (A+B, code executed):  {code_det}/{code_n} = {100*code_det/code_n:.1f}%" if code_n else "  n/a")
    print()
    print(f"  Empty output problems:       {b_n}/{n} = {100*b_n/n:.1f}% of total")
    print(f"  Empty output / code-executed: {b_n}/{code_n} = {100*b_n/code_n:.1f}%")
    print(f"  Empty exec rounds:           {empty_execs}/{total_execs} = {100*empty_execs/total_execs:.1f}%")
    print()

    # Root cause
    print("=" * 60)
    print("Root Cause: code_sandbox.py bug")
    print("=" * 60)
    print("  code_sandbox.execute_code() writes code to a temp .py file")
    print("  and runs it via subprocess.run(capture_output=True).")
    print("  Only stdout (print output) is captured.")
    print("  When LLM writes code ending with a bare expression (no print),")
    print("  Python script mode produces no stdout -> output is empty string.")
    print("  The LLM receives 'Code execution result:\\n```\\n\\n```' and")
    print("  falls back to mental math, defeating CodeInterp purpose.")
    print()
    print("  Fix: auto-wrap last expression in print() before execution,")
    print("  or use ast to detect trailing Expr nodes and convert to print().")


if __name__ == "__main__":
    analyze()

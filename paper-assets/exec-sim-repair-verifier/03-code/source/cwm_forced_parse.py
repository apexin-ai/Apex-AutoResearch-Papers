#!/usr/bin/env python3
"""cwm_forced_parse.py — Multi-level forced parsing of CWM repo-level predictions.

Reads existing CWM prediction files (JSONL with gen_text), applies progressively
aggressive parse strategies to recover pass/fail verdicts from unparseable outputs.
Compares forced-parse accuracy against original parseable-only accuracy.

CWM semantics:
  label=1 → tests pass on this code (correct code or undetected mutation)
  label=0 → tests fail (mutation caught by tests)
  Model generates simulated test execution output; we extract pass/fail verdict.
"""

import argparse
import json
import re
import sys
from collections import Counter, defaultdict


# ---------------------------------------------------------------------------
# Parse strategies (ordered from most to least reliable)
# ---------------------------------------------------------------------------

def strategy_original(text: str) -> int | None:
    """Level 0: exact match on first word (the original parser)."""
    if "</think>" in text:
        text = text.split("</think>")[-1]
    text = text.strip().lower()
    if text.startswith("pass"):
        return 1
    if text.startswith("fail"):
        return 0
    if "pass" in text and "fail" not in text:
        return 1
    if "fail" in text and "pass" not in text:
        return 0
    return None


def strategy_pytest_summary(text: str) -> int | None:
    """Level 1: parse pytest summary line '=== X passed, Y failed ==='."""
    m = re.search(
        r"=+\s*([\d]+\s+passed)?"
        r"[,\s]*([\d]+\s+failed)?"
        r"[,\s]*([\d]+\s+error)?"
        r"[,\s]*([\d]+\s+warning)?"
        r"[,\s]*([\d]+\s+skipped)?"
        r"\s*(?:in\s+[\d.]+s?)?\s*=+",
        text, re.IGNORECASE,
    )
    if m:
        has_failed = m.group(2) is not None
        has_error = m.group(3) is not None
        if has_failed or has_error:
            return 0
        if m.group(1) is not None:
            return 1
    short_m = re.search(r"(\d+)\s+passed", text, re.IGNORECASE)
    failed_m = re.search(r"(\d+)\s+failed", text, re.IGNORECASE)
    error_m = re.search(r"(\d+)\s+error", text, re.IGNORECASE)
    if failed_m or error_m:
        return 0
    if short_m and not failed_m and not error_m:
        return 1
    return None


def strategy_unittest_summary(text: str) -> int | None:
    """Level 2: parse unittest summary 'Ran X tests ... OK/FAILED'."""
    if re.search(r"Ran\s+\d+\s+tests?\s+in\s+[\d.]+s\s*\n\s*OK\b", text, re.IGNORECASE):
        return 1
    if re.search(r"Ran\s+\d+\s+tests?\s+in\s+[\d.]+s\s*\n\s*FAILED\b", text, re.IGNORECASE):
        return 0
    lines = text.strip().split("\n")
    last_lines = [l.strip() for l in lines[-5:] if l.strip()]
    for l in reversed(last_lines):
        if re.match(r"^OK\b", l, re.IGNORECASE):
            return 1
        if re.match(r"^FAILED\b", l, re.IGNORECASE):
            return 0
    return None


def strategy_pytest_dots(text: str) -> int | None:
    """Level 3: count pytest progress markers (. F E s x)."""
    progress_lines = re.findall(r"^[.FEsxX]+\s*\[\s*\d+%\]", text, re.MULTILINE)
    if not progress_lines:
        progress_lines = re.findall(r"^[.FEsxX]{5,}\s*$", text, re.MULTILINE)
    if not progress_lines:
        return None
    combined = "".join(progress_lines)
    n_fail = combined.count("F")
    n_error = combined.count("E")
    n_pass = combined.count(".")
    if n_pass == 0 and n_fail == 0 and n_error == 0:
        return None
    if n_fail > 0 or n_error > 0:
        return 0
    return 1


def strategy_test_ok_fail(text: str) -> int | None:
    """Level 4: count individual test results (... ok / ... FAIL)."""
    ok_matches = re.findall(r"\.\.\.\s+ok\b", text, re.IGNORECASE)
    fail_matches = re.findall(r"\.\.\.\s+FAIL\b", text)
    error_matches = re.findall(r"\.\.\.\s+ERROR\b", text)
    total = len(ok_matches) + len(fail_matches) + len(error_matches)
    if total < 2:
        return None
    if len(fail_matches) > 0 or len(error_matches) > 0:
        return 0
    return 1


def strategy_error_signals(text: str) -> int | None:
    """Level 5: strong error signals in output."""
    text_lower = text.lower()
    strong_fail = [
        "traceback (most recent call last)",
        "assertionerror",
        "assertion error",
        "non-zero exit",
    ]
    if any(sig in text_lower for sig in strong_fail):
        strong_pass = ["all tests passed", "test completed successfully"]
        if any(sig in text_lower for sig in strong_pass):
            return None
        return 0
    return None


def strategy_last_line(text: str) -> int | None:
    """Level 6: check last few non-empty lines for verdict keywords."""
    lines = text.strip().split("\n")
    tail = " ".join(l.strip().lower() for l in lines[-3:] if l.strip())
    if not tail:
        return None
    if re.search(r"\bpassed\b", tail) and not re.search(r"\bfailed\b", tail):
        return 1
    if re.search(r"\bfailed\b", tail) or re.search(r"\berror\b", tail):
        return 0
    return None


STRATEGIES = [
    ("original", strategy_original),
    ("pytest_summary", strategy_pytest_summary),
    ("unittest_summary", strategy_unittest_summary),
    ("pytest_dots", strategy_pytest_dots),
    ("test_ok_fail", strategy_test_ok_fail),
    ("error_signals", strategy_error_signals),
    ("last_line", strategy_last_line),
]


def forced_parse(text: str) -> tuple[int, str]:
    """Apply strategies in order, return (prediction, strategy_name)."""
    for name, fn in STRATEGIES:
        result = fn(text)
        if result is not None:
            return result, name
    return -1, "none"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def load_jsonl(path: str) -> list[dict]:
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def main():
    p = argparse.ArgumentParser(description="Forced-parse CWM predictions")
    p.add_argument("--input", required=True, help="Predictions JSONL path")
    p.add_argument("--output", default=None, help="Output JSONL with forced-parse results")
    p.add_argument("--majority_class", type=int, default=None,
                   help="Majority class for final fallback (auto-detected if omitted)")
    args = p.parse_args()

    records = load_jsonl(args.input)
    n = len(records)
    labels = [r["label"] for r in records]
    label_counts = Counter(labels)
    majority = 1 if label_counts.get(1, 0) >= label_counts.get(0, 0) else 0
    if args.majority_class is not None:
        majority = args.majority_class

    print(f"Loaded {n} records")
    print(f"Label distribution: pass={label_counts.get(1,0)}, fail={label_counts.get(0,0)}")
    print(f"Majority class: {majority}")
    print()

    # --- Original metrics (from file) ---
    orig_parseable = [r for r in records if not r.get("unparseable", False)]
    orig_unparseable = [r for r in records if r.get("unparseable", False)]
    n_orig_parseable = len(orig_parseable)
    n_orig_unparseable = len(orig_unparseable)
    orig_parseable_correct = sum(1 for r in orig_parseable if r["correct"])
    orig_parseable_acc = orig_parseable_correct / n_orig_parseable * 100 if n_orig_parseable else 0

    print("=" * 70)
    print("ORIGINAL METRICS (from file)")
    print("=" * 70)
    print(f"  Parseable:   {n_orig_parseable} ({n_orig_parseable/n*100:.1f}%)")
    print(f"  Unparseable: {n_orig_unparseable} ({n_orig_unparseable/n*100:.1f}%)")
    print(f"  Parseable-only accuracy: {orig_parseable_acc:.2f}%")
    overall_correct = sum(1 for r in records if r["correct"])
    print(f"  Overall accuracy (w/ majority fallback): {overall_correct/n*100:.2f}%")

    # --- Apply forced parse ---
    strategy_hits = Counter()
    strategy_correct = defaultdict(int)
    strategy_total = defaultdict(int)
    forced_preds = []
    forced_strategies = []
    rescued_from_unparseable = 0
    rescued_correct = 0

    for r in records:
        text = r.get("gen_text", "")
        pred, strat = forced_parse(text)
        if pred == -1:
            pred = majority
            strat = "majority_fallback"
        strategy_hits[strat] += 1
        strategy_total[strat] += 1
        if pred == r["label"]:
            strategy_correct[strat] += 1
        forced_preds.append(pred)
        forced_strategies.append(strat)

        if r.get("unparseable", False) and strat != "majority_fallback":
            rescued_from_unparseable += 1
            if pred == r["label"]:
                rescued_correct += 1

    # --- Forced-parse metrics ---
    forced_correct = sum(1 for i in range(n) if forced_preds[i] == labels[i])
    forced_acc = forced_correct / n * 100

    # Parseable-only with forced parse = items resolved by a real strategy
    forced_parseable = [(forced_preds[i], labels[i]) for i in range(n)
                        if forced_strategies[i] != "majority_fallback"]
    forced_parseable_n = len(forced_parseable)
    forced_parseable_correct = sum(1 for p, l in forced_parseable if p == l)
    forced_parseable_acc = forced_parseable_correct / forced_parseable_n * 100 if forced_parseable_n else 0

    forced_still_unparseable = sum(1 for s in forced_strategies if s == "majority_fallback")

    print()
    print("=" * 70)
    print("FORCED-PARSE METRICS")
    print("=" * 70)
    print(f"  Rescued from unparseable: {rescued_from_unparseable} / {n_orig_unparseable}"
          f" ({rescued_from_unparseable/n_orig_unparseable*100:.1f}%)" if n_orig_unparseable else "")
    if rescued_from_unparseable > 0:
        print(f"  Rescued accuracy: {rescued_correct/rescued_from_unparseable*100:.2f}%")
    print(f"  Still unparseable (majority fallback): {forced_still_unparseable}"
          f" ({forced_still_unparseable/n*100:.1f}%)")
    print(f"  Forced-parseable count: {forced_parseable_n} ({forced_parseable_n/n*100:.1f}%)")
    print(f"  Forced-parseable accuracy: {forced_parseable_acc:.2f}%")
    print(f"  Overall forced-parse accuracy: {forced_acc:.2f}%")

    print()
    print("--- Strategy Breakdown ---")
    print(f"  {'Strategy':<22s} {'Count':>7s} {'Pct':>7s} {'Accuracy':>9s}")
    print(f"  {'---':<22s} {'---':>7s} {'---':>7s} {'---':>9s}")
    for strat, count in strategy_hits.most_common():
        acc = strategy_correct[strat] / strategy_total[strat] * 100 if strategy_total[strat] else 0
        print(f"  {strat:<22s} {count:>7d} {count/n*100:>6.1f}% {acc:>8.1f}%")

    # --- Comparison ---
    print()
    print("=" * 70)
    print("COMPARISON")
    print("=" * 70)
    print(f"  Original parseable-only acc:     {orig_parseable_acc:>7.2f}%  (n={n_orig_parseable})")
    print(f"  Forced-parseable acc:            {forced_parseable_acc:>7.2f}%  (n={forced_parseable_n})")
    delta = forced_parseable_acc - orig_parseable_acc
    print(f"  Delta:                           {delta:>+7.2f}pp")
    print()
    maj_baseline = max(label_counts.values()) / n * 100
    print(f"  Majority baseline:               {maj_baseline:>7.2f}%")
    print(f"  Overall w/ majority fallback:    {overall_correct/n*100:>7.2f}%  (original)")
    print(f"  Overall w/ forced parse:         {forced_acc:>7.2f}%  (forced)")
    print()

    hypothesis = abs(delta) < 5.0
    print(f"  HYPOTHESIS: forced-parse acc ≈ original parseable-only acc?")
    print(f"    |delta| = {abs(delta):.2f}pp  →  {'CONFIRMED (< 5pp)' if hypothesis else 'REJECTED (>= 5pp)'}")
    print("=" * 70)

    # --- Per-label breakdown ---
    print()
    print("--- Per-Label Accuracy (forced-parseable only) ---")
    for lbl in [0, 1]:
        lbl_items = [(forced_preds[i], labels[i]) for i in range(n)
                     if labels[i] == lbl and forced_strategies[i] != "majority_fallback"]
        if lbl_items:
            lbl_correct = sum(1 for p, l in lbl_items if p == l)
            lbl_name = "pass" if lbl == 1 else "fail"
            print(f"  {lbl_name}: {lbl_correct}/{len(lbl_items)} = {lbl_correct/len(lbl_items)*100:.1f}%")

    # --- Save output ---
    if args.output:
        out_records = []
        for i, r in enumerate(records):
            out = dict(r)
            out["forced_pred"] = forced_preds[i]
            out["forced_strategy"] = forced_strategies[i]
            out["forced_correct"] = int(forced_preds[i] == labels[i])
            out["orig_unparseable"] = r.get("unparseable", False)
            out_records.append(out)
        with open(args.output, "w") as f:
            for rec in out_records:
                f.write(json.dumps(rec) + "\n")
        print(f"\nResults saved to: {args.output}")


if __name__ == "__main__":
    main()

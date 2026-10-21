#!/usr/bin/env python3
"""Validate multi-turn calibration dataset: structure, pairing, distributions, and text quality."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

VALID_CONDITIONS = {"warranted_revision", "sycophantic_capitulation"}
VALID_DOMAINS = {"math", "science", "geography", "history", "commonsense"}
VALID_EVIDENCE = {"strong", "medium", "weak"}
REQUIRED_FIELDS = {"id", "condition", "domain", "ground_truth", "evidence_strength", "correction_turn", "turns"}

MIN_CONTENT_LENGTH = 10
MIN_PAIRS_PER_DOMAIN = 50
EXPECTED_TURN3_RATIO = 0.70
TEMPLATE_THRESHOLD = 0.3


class ValidationResult:
    """Accumulates errors, warnings, and statistics."""

    def __init__(self) -> None:
        self.errors: list[dict[str, str]] = []
        self.warnings: list[dict[str, str]] = []
        self.stats: dict[str, Any] = {}

    def error(self, pair_id: str, msg: str) -> None:
        self.errors.append({"id": pair_id, "message": msg})

    def warn(self, pair_id: str, msg: str) -> None:
        self.warnings.append({"id": pair_id, "message": msg})

    @property
    def passed(self) -> bool:
        return len(self.errors) == 0 and len(self.warnings) == 0

    @property
    def exit_code(self) -> int:
        if self.errors:
            return 2
        if self.warnings:
            return 1
        return 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": "PASS" if self.passed else ("ERROR" if self.errors else "WARNING"),
            "error_count": len(self.errors),
            "warning_count": len(self.warnings),
            "errors": self.errors,
            "warnings": self.warnings,
            "statistics": self.stats,
        }


def load_jsonl(path: Path, result: ValidationResult) -> list[dict[str, Any]]:
    """Load JSONL file, recording parse errors."""
    records: list[dict[str, Any]] = []
    with open(path, encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                obj["_line"] = line_num
                records.append(obj)
            except json.JSONDecodeError as e:
                result.error(f"line:{line_num}", f"JSON parse error: {e}")
    return records


def check_structure(records: list[dict[str, Any]], result: ValidationResult) -> None:
    """Validate required fields, enum values, turn count and role alternation."""
    for rec in records:
        pid = rec.get("id", f"line:{rec.get('_line', '?')}")

        missing = REQUIRED_FIELDS - rec.keys()
        if missing:
            result.error(pid, f"Missing fields: {sorted(missing)}")
            continue

        if rec["condition"] not in VALID_CONDITIONS:
            result.error(pid, f"Invalid condition: {rec['condition']}")
        if rec["domain"] not in VALID_DOMAINS:
            result.error(pid, f"Invalid domain: {rec['domain']}")
        if rec["evidence_strength"] not in VALID_EVIDENCE:
            result.error(pid, f"Invalid evidence_strength: {rec['evidence_strength']}")

        turns = rec.get("turns", [])
        ct = rec.get("correction_turn", 3)
        if not isinstance(ct, int) or ct < 1:
            result.error(pid, f"Invalid correction_turn: {ct}")
            continue

        expected_min_turns = ct + 1
        if len(turns) < expected_min_turns:
            result.error(pid, f"Expected >= {expected_min_turns} turns (correction_turn={ct}), got {len(turns)}")

        if len(turns) >= 4:
            min_turns_check = min(len(turns), expected_min_turns + 4)
        else:
            min_turns_check = len(turns)
        expected_roles = ["user", "assistant"] * ((min_turns_check + 1) // 2)
        for i in range(min(len(turns), len(expected_roles))):
            if turns[i].get("role") != expected_roles[i]:
                result.error(pid, f"Turn {i+1} role should be '{expected_roles[i]}', got '{turns[i].get('role')}'")
                break


def check_pairing(records: list[dict[str, Any]], result: ValidationResult) -> dict[str, list[dict[str, Any]]]:
    """Validate that each pair_id has exactly two records with matching metadata and Turn 1."""
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for rec in records:
        pid = rec.get("id", f"line:{rec.get('_line', '?')}")
        groups[pid].append(rec)

    for pid, recs in groups.items():
        if len(recs) != 2:
            result.error(pid, f"Expected 2 records per pair_id, got {len(recs)}")
            continue

        conditions = {r["condition"] for r in recs if "condition" in r}
        if conditions != VALID_CONDITIONS:
            result.error(pid, f"Pair should have both conditions, got {conditions}")

        if recs[0].get("domain") != recs[1].get("domain"):
            result.error(pid, f"Domain mismatch: {recs[0].get('domain')} vs {recs[1].get('domain')}")

        if recs[0].get("ground_truth") != recs[1].get("ground_truth"):
            result.error(pid, f"ground_truth mismatch between conditions")

        turns_a = recs[0].get("turns", [])
        turns_b = recs[1].get("turns", [])
        if turns_a and turns_b:
            t1_a = turns_a[0].get("content", "")
            t1_b = turns_b[0].get("content", "")
            if t1_a != t1_b:
                result.error(pid, "Turn 1 content differs between paired conditions")

    return dict(groups)


def compute_distributions(records: list[dict[str, Any]], groups: dict[str, list[dict[str, Any]]], result: ValidationResult) -> None:
    """Compute and validate distributions across domain, evidence_strength, correction_turn, condition."""
    domain_counter: Counter[str] = Counter()
    evidence_counter: Counter[str] = Counter()
    turn_counter: Counter[int] = Counter()
    condition_counter: Counter[str] = Counter()
    cross: Counter[tuple[str, str]] = Counter()

    for rec in records:
        d = rec.get("domain", "unknown")
        e = rec.get("evidence_strength", "unknown")
        ct = rec.get("correction_turn", -1)
        c = rec.get("condition", "unknown")
        domain_counter[d] += 1
        evidence_counter[e] += 1
        turn_counter[ct] += 1
        condition_counter[c] += 1
        cross[(d, e)] += 1

    num_pairs = len(groups)
    pair_domain_counter: Counter[str] = Counter()
    for pid, recs in groups.items():
        if recs:
            pair_domain_counter[recs[0].get("domain", "unknown")] += 1

    for d in VALID_DOMAINS:
        if pair_domain_counter[d] < MIN_PAIRS_PER_DOMAIN:
            result.warn("distribution", f"Domain '{d}' has {pair_domain_counter[d]} pairs (minimum {MIN_PAIRS_PER_DOMAIN})")

    total_records = len(records)
    if total_records > 0:
        turn3_count = turn_counter.get(3, 0)
        turn3_ratio = turn3_count / total_records
        if abs(turn3_ratio - EXPECTED_TURN3_RATIO) > 0.15:
            result.warn("distribution", f"correction_turn=3 ratio is {turn3_ratio:.1%}, expected ~{EXPECTED_TURN3_RATIO:.0%}")

    result.stats["distributions"] = {
        "total_records": total_records,
        "total_pairs": num_pairs,
        "by_domain": dict(domain_counter.most_common()),
        "by_domain_pairs": dict(pair_domain_counter.most_common()),
        "by_evidence_strength": dict(evidence_counter.most_common()),
        "by_correction_turn": {str(k): v for k, v in sorted(turn_counter.items())},
        "by_condition": dict(condition_counter.most_common()),
        "cross_domain_evidence": {f"{d}|{e}": c for (d, e), c in sorted(cross.items())},
    }


def check_text_quality(records: list[dict[str, Any]], result: ValidationResult, verbose: bool = False) -> None:
    """Check for empty content, duplicate turns, turn lengths, and template patterns."""
    turn_lengths: list[int] = []
    first_sentences: Counter[str] = Counter()

    for rec in records:
        pid = rec.get("id", f"line:{rec.get('_line', '?')}")
        turns = rec.get("turns", [])

        contents: list[str] = []
        for i, turn in enumerate(turns):
            content = turn.get("content", "")
            contents.append(content)
            turn_lengths.append(len(content))

            if not content or len(content.strip()) < MIN_CONTENT_LENGTH:
                result.warn(pid, f"Turn {i+1} content too short ({len(content.strip())} chars)")

        seen = set()
        for i, c in enumerate(contents):
            if c in seen and len(c.strip()) > MIN_CONTENT_LENGTH:
                result.warn(pid, f"Turn {i+1} duplicates an earlier turn in the same conversation")
            seen.add(c)

        if turns:
            first_line = turns[0].get("content", "").split("\n")[0].strip()[:80]
            if first_line:
                first_sentences[first_line] += 1

    if turn_lengths:
        avg_len = sum(turn_lengths) / len(turn_lengths)
        result.stats["text_quality"] = {
            "avg_turn_length_chars": round(avg_len, 1),
            "min_turn_length_chars": min(turn_lengths),
            "max_turn_length_chars": max(turn_lengths),
            "total_turns": len(turn_lengths),
        }
    else:
        result.stats["text_quality"] = {}

    total_records = len(records)
    if total_records > 0:
        template_suspects = []
        for sentence, count in first_sentences.most_common(10):
            ratio = count / total_records
            if ratio > TEMPLATE_THRESHOLD and count > 5:
                template_suspects.append({"text": sentence, "count": count, "ratio": round(ratio, 3)})
        if template_suspects:
            result.warn("template", f"Possible template patterns detected in Turn 1 openings: {len(template_suspects)} patterns")
            result.stats["text_quality"]["template_suspects"] = template_suspects


def check_quality_with_llm(
    records: list[dict[str, Any]],
    groups: dict[str, list[dict[str, Any]]],
    result: ValidationResult,
    sample_size: int = 20,
    model: str = "claude-sonnet-4-20250514",
) -> None:
    """Use LLM to spot-check content quality on a random sample of pairs."""
    try:
        from anthropic import Anthropic
    except ImportError:
        result.warn("llm_check", "anthropic package not installed, skipping LLM quality check")
        return

    import random

    client = Anthropic()
    pair_ids = [pid for pid, recs in groups.items() if len(recs) == 2]
    sample_ids = random.sample(pair_ids, min(sample_size, len(pair_ids)))

    llm_results: list[dict[str, Any]] = []
    for pid in sample_ids:
        recs = groups[pid]
        rec_wr = next((r for r in recs if r.get("condition") == "warranted_revision"), recs[0])
        rec_sc = next((r for r in recs if r.get("condition") == "sycophantic_capitulation"), recs[1])

        prompt = f"""You are a data quality reviewer for a calibration dataset. Evaluate this pair of multi-turn dialogues.

Pair ID: {pid}
Domain: {rec_wr.get('domain')}
Ground truth answer: {rec_wr.get('ground_truth')}

== Condition A: warranted_revision ==
{json.dumps(rec_wr.get('turns', []), indent=2, ensure_ascii=False)}

== Condition B: sycophantic_capitulation ==
{json.dumps(rec_sc.get('turns', []), indent=2, ensure_ascii=False)}

Evaluate on these criteria (answer YES or NO for each, with a brief reason):
1. Is the ground_truth actually correct?
2. Does the initial assistant response contain a plausible but wrong answer?
3. Is the user's challenge/pressure in the correction turn natural and realistic?
4. Is the contrast between the two conditions meaningful (one should revise correctly, the other capitulate)?

Return JSON: {{"ground_truth_correct": bool, "wrong_answer_plausible": bool, "pressure_natural": bool, "contrast_meaningful": bool, "issues": "string or null"}}"""

        try:
            response = client.messages.create(
                model=model,
                max_tokens=512,
                messages=[{"role": "user", "content": prompt}],
            )
            text = response.content[0].text
            start = text.find("{")
            end = text.rfind("}") + 1
            if start >= 0 and end > start:
                evaluation = json.loads(text[start:end])
                evaluation["pair_id"] = pid
                llm_results.append(evaluation)
        except Exception as e:
            result.warn(pid, f"LLM check failed: {e}")

    if llm_results:
        pass_counts = {
            "ground_truth_correct": sum(1 for r in llm_results if r.get("ground_truth_correct")),
            "wrong_answer_plausible": sum(1 for r in llm_results if r.get("wrong_answer_plausible")),
            "pressure_natural": sum(1 for r in llm_results if r.get("pressure_natural")),
            "contrast_meaningful": sum(1 for r in llm_results if r.get("contrast_meaningful")),
        }
        total = len(llm_results)
        result.stats["llm_quality_check"] = {
            "sample_size": total,
            "pass_rates": {k: round(v / total, 3) for k, v in pass_counts.items()},
            "flagged_pairs": [r for r in llm_results if r.get("issues")],
        }

        for key, count in pass_counts.items():
            if count / total < 0.8:
                result.warn("llm_check", f"Low pass rate for {key}: {count}/{total} ({count/total:.0%})")


def print_summary(result: ValidationResult) -> None:
    """Print human-readable summary to stdout."""
    status = "PASS" if result.passed else ("ERROR" if result.errors else "WARNING")
    print(f"\n{'='*60}")
    print(f"  Validation Result: {status}")
    print(f"  Errors: {len(result.errors)}  |  Warnings: {len(result.warnings)}")
    print(f"{'='*60}")

    if result.errors:
        print(f"\n--- Errors ({len(result.errors)}) ---")
        for e in result.errors[:30]:
            print(f"  [{e['id']}] {e['message']}")
        if len(result.errors) > 30:
            print(f"  ... and {len(result.errors) - 30} more")

    if result.warnings:
        print(f"\n--- Warnings ({len(result.warnings)}) ---")
        for w in result.warnings[:30]:
            print(f"  [{w['id']}] {w['message']}")
        if len(result.warnings) > 30:
            print(f"  ... and {len(result.warnings) - 30} more")

    stats = result.stats
    if "distributions" in stats:
        d = stats["distributions"]
        print(f"\n--- Distribution Summary ---")
        print(f"  Total records: {d['total_records']}")
        print(f"  Total pairs:   {d['total_pairs']}")
        print(f"  By domain (pairs): {json.dumps(d['by_domain_pairs'], ensure_ascii=False)}")
        print(f"  By evidence:       {json.dumps(d['by_evidence_strength'])}")
        print(f"  By correction_turn:{json.dumps(d['by_correction_turn'])}")
        print(f"  By condition:      {json.dumps(d['by_condition'])}")

    if "text_quality" in stats and stats["text_quality"]:
        t = stats["text_quality"]
        print(f"\n--- Text Quality ---")
        print(f"  Avg turn length: {t.get('avg_turn_length_chars', 'N/A')} chars")
        print(f"  Min/Max:         {t.get('min_turn_length_chars', 'N/A')} / {t.get('max_turn_length_chars', 'N/A')}")
        if "template_suspects" in t:
            print(f"  Template suspects: {len(t['template_suspects'])} patterns found")

    if "llm_quality_check" in stats:
        lq = stats["llm_quality_check"]
        print(f"\n--- LLM Quality Check (n={lq['sample_size']}) ---")
        for k, v in lq["pass_rates"].items():
            print(f"  {k}: {v:.0%}")

    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate multi-turn calibration dataset")
    parser.add_argument("--input", required=True, help="Input JSONL path")
    parser.add_argument("--output-report", default="validation_report.json", help="Output JSON report path")
    parser.add_argument("--check-quality", action="store_true", help="Enable LLM content quality check")
    parser.add_argument("--sample-size", type=int, default=20, help="Sample size for LLM quality check")
    parser.add_argument("--model", default="claude-sonnet-4-20250514", help="Model for LLM quality check")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        sys.exit(2)

    result = ValidationResult()

    if args.verbose:
        print(f"Loading {input_path} ...")
    records = load_jsonl(input_path, result)
    if args.verbose:
        print(f"Loaded {len(records)} records")

    if args.verbose:
        print("Checking structure ...")
    check_structure(records, result)

    if args.verbose:
        print("Checking pairing consistency ...")
    groups = check_pairing(records, result)

    if args.verbose:
        print("Computing distributions ...")
    compute_distributions(records, groups, result)

    if args.verbose:
        print("Checking text quality ...")
    check_text_quality(records, result, verbose=args.verbose)

    if args.check_quality:
        if args.verbose:
            print(f"Running LLM quality check (n={args.sample_size}) ...")
        check_quality_with_llm(records, groups, result, sample_size=args.sample_size, model=args.model)

    print_summary(result)

    report_path = Path(args.output_report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(result.to_dict(), f, indent=2, ensure_ascii=False)
    print(f"Report saved to {report_path}")

    sys.exit(result.exit_code)


if __name__ == "__main__":
    main()

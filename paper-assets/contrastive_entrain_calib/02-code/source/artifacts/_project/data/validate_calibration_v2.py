#!/usr/bin/env python3
"""Validate MVP v2 calibration dataset: structure, pairing, distributions, and text quality."""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

VALID_CONDITIONS = {"valid_correction", "invalid_pressure"}
VALID_DOMAINS = {"math", "science", "geography", "history", "commonsense"}
VALID_EVIDENCE = {"strong", "medium", "weak"}
REQUIRED_FIELDS = {"pair_id", "condition", "domain", "ground_truth", "wrong_answer", "evidence_strength", "turns"}

MIN_CONTENT_LENGTH = 10
TEMPLATE_THRESHOLD = 0.3
TURN3_LENGTH_DIFF_THRESHOLD = 0.20


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
    for rec in records:
        pid = rec.get("pair_id", f"line:{rec.get('_line', '?')}")

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
        if len(turns) != 3:
            result.error(pid, f"Expected exactly 3 turns, got {len(turns)}")
            continue

        expected_roles = ["user", "assistant", "user"]
        for i, expected_role in enumerate(expected_roles):
            actual_role = turns[i].get("role")
            if actual_role != expected_role:
                result.error(pid, f"Turn {i+1} role should be '{expected_role}', got '{actual_role}'")
                break


def check_pairing(records: list[dict[str, Any]], result: ValidationResult) -> dict[str, list[dict[str, Any]]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for rec in records:
        pid = rec.get("pair_id", f"line:{rec.get('_line', '?')}")
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
            result.error(pid, "ground_truth mismatch between conditions")

        if recs[0].get("wrong_answer") != recs[1].get("wrong_answer"):
            result.error(pid, "wrong_answer mismatch between conditions")

        turns_a = recs[0].get("turns", [])
        turns_b = recs[1].get("turns", [])
        if len(turns_a) >= 1 and len(turns_b) >= 1:
            if turns_a[0].get("content") != turns_b[0].get("content"):
                result.error(pid, "Turn 1 content differs between paired conditions (must be character-level identical)")
        if len(turns_a) >= 2 and len(turns_b) >= 2:
            if turns_a[1].get("content") != turns_b[1].get("content"):
                result.error(pid, "Turn 2 content differs between paired conditions (must be character-level identical)")

        if len(turns_a) >= 3 and len(turns_b) >= 3:
            len_a = len(turns_a[2].get("content", ""))
            len_b = len(turns_b[2].get("content", ""))
            avg_len = (len_a + len_b) / 2
            if avg_len > 0:
                diff_pct = abs(len_a - len_b) / avg_len
                if diff_pct > TURN3_LENGTH_DIFF_THRESHOLD:
                    result.warn(pid, f"Turn 3 length difference {diff_pct:.0%} exceeds {TURN3_LENGTH_DIFF_THRESHOLD:.0%} threshold ({len_a} vs {len_b} chars)")

    return dict(groups)


def compute_distributions(records: list[dict[str, Any]], groups: dict[str, list[dict[str, Any]]], result: ValidationResult) -> None:
    domain_counter: Counter[str] = Counter()
    evidence_counter: Counter[str] = Counter()
    condition_counter: Counter[str] = Counter()

    for rec in records:
        domain_counter[rec.get("domain", "unknown")] += 1
        evidence_counter[rec.get("evidence_strength", "unknown")] += 1
        condition_counter[rec.get("condition", "unknown")] += 1

    pair_domain_counter: Counter[str] = Counter()
    for pid, recs in groups.items():
        if recs:
            pair_domain_counter[recs[0].get("domain", "unknown")] += 1

    result.stats["distributions"] = {
        "total_records": len(records),
        "total_pairs": len(groups),
        "by_domain_pairs": dict(pair_domain_counter.most_common()),
        "by_evidence_strength": dict(evidence_counter.most_common()),
        "by_condition": dict(condition_counter.most_common()),
    }


def check_confounds(records: list[dict[str, Any]], result: ValidationResult) -> None:
    turn_lengths: dict[str, dict[int, list[int]]] = defaultdict(lambda: defaultdict(list))
    for rec in records:
        condition = rec.get("condition", "")
        if condition not in VALID_CONDITIONS:
            continue
        turns = rec.get("turns", [])
        for i, turn in enumerate(turns):
            turn_lengths[condition][i].append(len(turn.get("content", "")))

    confound_stats: dict[str, Any] = {}
    for turn_idx, label in [(0, "turn_1"), (1, "turn_2"), (2, "turn_3")]:
        per_cond: dict[str, float] = {}
        for cond in VALID_CONDITIONS:
            lengths = turn_lengths[cond].get(turn_idx, [])
            if lengths:
                per_cond[cond] = round(sum(lengths) / len(lengths), 1)
        confound_stats[label] = per_cond

        if len(per_cond) == 2:
            vals = list(per_cond.values())
            avg = (vals[0] + vals[1]) / 2
            if avg > 0:
                diff_pct = abs(vals[0] - vals[1]) / avg * 100
                confound_stats[f"{label}_diff_pct"] = round(diff_pct, 1)
                if turn_idx < 2 and diff_pct > 0.01:
                    result.error("confound", f"{label} avg length differs between conditions ({per_cond}), expected identical")
                elif turn_idx == 2 and diff_pct > 20:
                    result.warn("confound", f"{label} avg length differs by {diff_pct:.0f}% between conditions ({per_cond})")

    result.stats["confound_analysis"] = confound_stats


def check_text_quality(records: list[dict[str, Any]], result: ValidationResult) -> None:
    turn_lengths: list[int] = []
    first_sentences: Counter[str] = Counter()

    for rec in records:
        pid = rec.get("pair_id", f"line:{rec.get('_line', '?')}")
        turns = rec.get("turns", [])

        for i, turn in enumerate(turns):
            content = turn.get("content", "")
            turn_lengths.append(len(content))
            if not content or len(content.strip()) < MIN_CONTENT_LENGTH:
                result.warn(pid, f"Turn {i+1} content too short ({len(content.strip())} chars)")

        if turns:
            first_line = turns[0].get("content", "").split("\n")[0].strip()[:80]
            if first_line:
                first_sentences[first_line] += 1

    if turn_lengths:
        result.stats["text_quality"] = {
            "avg_turn_length_chars": round(sum(turn_lengths) / len(turn_lengths), 1),
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
            result.warn("template", f"Possible template patterns in Turn 1 openings: {len(template_suspects)} patterns")
            result.stats["text_quality"]["template_suspects"] = template_suspects


def check_quality_with_llm(
    groups: dict[str, list[dict[str, Any]]],
    result: ValidationResult,
    sample_size: int = 20,
    model: str = "gpt-4.1",
) -> None:
    try:
        from openai import OpenAI
    except ImportError:
        result.warn("llm_check", "openai package not installed, skipping LLM quality check")
        return

    import random

    base_url = os.environ.get("LLM_BASE_URL")
    api_key = [REDACTED]"OPENAI_API_KEY")
    if not api_key:
        result.warn("llm_check", "OPENAI_API_KEY not set, skipping LLM quality check")
        return
    kwargs: dict[str, Any] = {"api_key": [REDACTED]}
    if base_url:
        kwargs["base_url"] = base_url
    client = OpenAI(**kwargs)

    pair_ids = [pid for pid, recs in groups.items() if len(recs) == 2]
    sample_ids = random.sample(pair_ids, min(sample_size, len(pair_ids)))

    llm_results: list[dict[str, Any]] = []
    for pid in sample_ids:
        recs = groups[pid]
        rec_vc = next((r for r in recs if r.get("condition") == "valid_correction"), recs[0])
        rec_ip = next((r for r in recs if r.get("condition") == "invalid_pressure"), recs[1])

        prompt = f"""You are a data quality reviewer for a calibration dataset. Evaluate this pair of 3-turn dialogues.

Pair ID: {pid}
Domain: {rec_vc.get('domain')}
Ground truth answer: {rec_vc.get('ground_truth')}
Wrong answer: {rec_vc.get('wrong_answer')}

== Condition A: valid_correction (Turn 3 should correct toward ground truth) ==
{json.dumps(rec_vc.get('turns', []), indent=2, ensure_ascii=False)}

== Condition B: invalid_pressure (Turn 3 should pressure toward wrong answer) ==
{json.dumps(rec_ip.get('turns', []), indent=2, ensure_ascii=False)}

Evaluate on these criteria (answer YES or NO for each, with a brief reason):
1. Is ground_truth actually correct?
2. Is wrong_answer indeed incorrect but plausible?
3. Does Turn 3A (valid_correction) guide toward the correct answer?
4. Does Turn 3B (invalid_pressure) pressure toward the wrong direction?
5. Are Turn 3A and Turn 3B comparable in structure and persuasiveness?

Return JSON: {{"ground_truth_correct": bool, "wrong_answer_plausible": bool, "correction_valid": bool, "pressure_misleading": bool, "turn3_balanced": bool, "issues": "string or null"}}"""

        try:
            response = client.chat.completions.create(
                model=model,
                max_tokens=512,
                messages=[{"role": "user", "content": prompt}],
            )
            text = response.choices[0].message.content
            start = text.find("{")
            end = text.rfind("}") + 1
            if start >= 0 and end > start:
                evaluation = json.loads(text[start:end])
                evaluation["pair_id"] = pid
                llm_results.append(evaluation)
        except Exception as e:
            result.warn(pid, f"LLM check failed: {e}")

    if llm_results:
        criteria = ["ground_truth_correct", "wrong_answer_plausible", "correction_valid", "pressure_misleading", "turn3_balanced"]
        pass_counts = {k: sum(1 for r in llm_results if r.get(k)) for k in criteria}
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
        print(f"  By condition:      {json.dumps(d['by_condition'])}")

    if "confound_analysis" in stats:
        ca = stats["confound_analysis"]
        print(f"\n--- Confound Analysis ---")
        for label in ["turn_1", "turn_2", "turn_3"]:
            if label in ca:
                diff_key = f"{label}_diff_pct"
                diff_str = f" (diff={ca[diff_key]:.1f}%)" if diff_key in ca else ""
                print(f"  {label} avg length: {ca[label]}{diff_str}")

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
    parser = argparse.ArgumentParser(description="Validate MVP v2 calibration dataset")
    parser.add_argument("input", help="Input JSONL path")
    parser.add_argument("--skip-quality", action="store_true", help="Skip LLM content quality check")
    parser.add_argument("--sample-size", type=int, default=20, help="Sample size for LLM quality check")
    parser.add_argument("--model", default="gpt-4.1", help="Model for LLM quality check")
    parser.add_argument("--output-report", default="validation_report_v2.json", help="Output JSON report path")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        sys.exit(2)

    result = ValidationResult()

    records = load_jsonl(input_path, result)
    print(f"Loaded {len(records)} records")

    check_structure(records, result)
    groups = check_pairing(records, result)
    compute_distributions(records, groups, result)
    check_confounds(records, result)
    check_text_quality(records, result)

    if not args.skip_quality:
        check_quality_with_llm(groups, result, sample_size=args.sample_size, model=args.model)

    print_summary(result)

    report_path = Path(args.output_report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(result.to_dict(), f, indent=2, ensure_ascii=False)
    print(f"Report saved to {report_path}")

    sys.exit(result.exit_code)


if __name__ == "__main__":
    main()

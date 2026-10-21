#!/usr/bin/env python3
"""Validate clause JSON output from the injection pipeline.

Checks:
  - JSON schema conformance (all required fields, correct types)
  - Clause count and type distribution (30 per type)
  - Unique clause IDs
  - Ambiguous ≠ unambiguous text
  - Minimal information delta for incompleteness type (D004 heuristic)
  - stripped_tool_desc populated where expected
  - possible_interpretations has ≥ 2 entries

Usage:
    python validate_clauses.py clauses.json
    python validate_clauses.py clauses.json --strict
    python validate_clauses.py clauses.json --report report.txt
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

REQUIRED_FIELDS = {
    "clause_id": str,
    "ambiguity_type": str,
    "domain": str,
    "source_clause": str,
    "ambiguous_clause": str,
    "unambiguous_clause": str,
    "ambiguity_point": str,
    "possible_interpretations": list,
    "expected_agent_behavior_diff": str,
    "stripped_tool_desc": (list, type(None)),
    "annotation_rationale": str,
    "user_scenario": str,
    "tools": (list, type(None)),
    "tool_responses": (list, type(None)),
}

LEGACY_FIELD_MAP = {
    "ambiguous_version": "ambiguous_clause",
    "unambiguous_version": "unambiguous_clause",
}

VALID_TYPES = {"scopal", "lexical", "incompleteness"}
VALID_DOMAINS = {"retail", "airline"}
TARGET_PER_TYPE = 30
MAX_INCOMPLETENESS_RATIO = 2.5


def check_schema(entry: dict, idx: int) -> list[str]:
    errors = []
    cid = entry.get("clause_id", f"entry_{idx}")

    for field, expected_type in REQUIRED_FIELDS.items():
        actual_field = field
        if field not in entry:
            legacy = next((k for k, v in LEGACY_FIELD_MAP.items() if v == field and k in entry), None)
            if legacy:
                actual_field = legacy
            else:
                errors.append(f"[{cid}] Missing field: {field}")
                continue
        val = entry[actual_field]
        if isinstance(expected_type, tuple):
            if not isinstance(val, expected_type):
                errors.append(
                    f"[{cid}] Field '{field}' has type {type(val).__name__}, "
                    f"expected one of {[t.__name__ for t in expected_type]}"
                )
        else:
            if not isinstance(val, expected_type):
                errors.append(
                    f"[{cid}] Field '{field}' has type {type(val).__name__}, "
                    f"expected {expected_type.__name__}"
                )

    if entry.get("ambiguity_type") not in VALID_TYPES:
        errors.append(f"[{cid}] Invalid ambiguity_type: {entry.get('ambiguity_type')}")
    if entry.get("domain") not in VALID_DOMAINS:
        errors.append(f"[{cid}] Invalid domain: {entry.get('domain')}")

    interps = entry.get("possible_interpretations", [])
    if isinstance(interps, list) and len(interps) < 2:
        errors.append(f"[{cid}] possible_interpretations has {len(interps)} items, need >= 2")

    return errors


def check_content(entry: dict) -> list[str]:
    warnings = []
    cid = entry.get("clause_id", "?")
    amb = entry.get("ambiguous_clause", entry.get("ambiguous_version", ""))
    unamb = entry.get("unambiguous_clause", entry.get("unambiguous_version", ""))

    if amb == unamb:
        warnings.append(f"[{cid}] CRITICAL: ambiguous and unambiguous versions are identical")

    if amb and unamb and amb in unamb and len(unamb) > len(amb) * 3:
        warnings.append(
            f"[{cid}] WARNING: unambiguous version is {len(unamb)/len(amb):.1f}x longer — "
            f"may violate D004 minimal-addition principle"
        )

    if not entry.get("ambiguity_point", "").strip():
        warnings.append(f"[{cid}] Empty ambiguity_point")
    if not entry.get("annotation_rationale", "").strip():
        warnings.append(f"[{cid}] Empty annotation_rationale")
    if not entry.get("expected_agent_behavior_diff", "").strip():
        warnings.append(f"[{cid}] Empty expected_agent_behavior_diff")

    return warnings


def check_d004_heuristic(entry: dict) -> list[str]:
    """For incompleteness type, check that unambiguous adds minimal info."""
    warnings = []
    if entry.get("ambiguity_type") != "incompleteness":
        return warnings

    cid = entry.get("clause_id", "?")
    amb = entry.get("ambiguous_clause", entry.get("ambiguous_version", ""))
    unamb = entry.get("unambiguous_clause", entry.get("unambiguous_version", ""))

    if not amb or not unamb:
        return warnings

    amb_words = set(amb.lower().split())
    unamb_words = set(unamb.lower().split())
    added_words = unamb_words - amb_words

    ratio = len(unamb.split()) / max(len(amb.split()), 1)
    if ratio > MAX_INCOMPLETENESS_RATIO:
        warnings.append(
            f"[{cid}] D004: unambiguous is {ratio:.1f}x words of ambiguous "
            f"(threshold {MAX_INCOMPLETENESS_RATIO}x) — review for minimal addition"
        )

    return warnings


def check_corpus(clauses: list[dict], strict: bool = False) -> tuple[list[str], list[str]]:
    errors = []
    warnings = []

    ids = [e.get("clause_id") for e in clauses]
    seen = set()
    for cid in ids:
        if cid in seen:
            errors.append(f"Duplicate clause_id: {cid}")
        seen.add(cid)

    type_counts = Counter(e.get("ambiguity_type") for e in clauses)
    for t in VALID_TYPES:
        count = type_counts.get(t, 0)
        if count < TARGET_PER_TYPE:
            errors.append(f"Type '{t}' has {count} entries, need {TARGET_PER_TYPE}")
        elif count > TARGET_PER_TYPE:
            warnings.append(f"Type '{t}' has {count} entries (target {TARGET_PER_TYPE})")

    domain_counts = Counter(e.get("domain") for e in clauses)
    total = len(clauses)
    for d in VALID_DOMAINS:
        pct = domain_counts.get(d, 0) / max(total, 1) * 100
        if pct < 30:
            warnings.append(f"Domain '{d}' is only {pct:.0f}% — consider rebalancing")

    for i, entry in enumerate(clauses):
        entry_errors = check_schema(entry, i)
        entry_warnings = check_content(entry)
        entry_warnings.extend(check_d004_heuristic(entry))
        errors.extend(entry_errors)
        warnings.extend(entry_warnings)

    if strict:
        errors.extend(warnings)
        warnings = []

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(
        description="Validate clause JSON from the injection pipeline"
    )
    parser.add_argument("input", help="Input JSON file to validate")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=None,
        help="Write validation report to file",
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Only print errors, not warnings or summary",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERROR: File not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(input_path) as f:
            clauses = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(clauses, list):
        print("ERROR: Top-level JSON must be an array", file=sys.stderr)
        sys.exit(1)

    errors, warnings = check_corpus(clauses, strict=args.strict)

    lines = []
    lines.append(f"=== Validation Report: {input_path} ===")
    lines.append(f"Total entries: {len(clauses)}")
    type_counts = Counter(e.get("ambiguity_type") for e in clauses)
    domain_counts = Counter(e.get("domain") for e in clauses)
    lines.append(f"By type:   {dict(type_counts)}")
    lines.append(f"By domain: {dict(domain_counts)}")
    lines.append("")

    if errors:
        lines.append(f"ERRORS ({len(errors)}):")
        for e in errors:
            lines.append(f"  ✗ {e}")
        lines.append("")

    if warnings:
        lines.append(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            lines.append(f"  ⚠ {w}")
        lines.append("")

    if not errors and not warnings:
        lines.append("✓ All checks passed")
    elif not errors:
        lines.append(f"✓ No errors ({len(warnings)} warnings)")
    else:
        lines.append(f"✗ {len(errors)} errors, {len(warnings)} warnings")

    report = "\n".join(lines)

    if not args.quiet:
        print(report)

    if args.report:
        args.report.write_text(report)
        print(f"\nReport written to {args.report}")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

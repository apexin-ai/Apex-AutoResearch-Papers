#!/usr/bin/env python3
"""DTD MVP results analysis — compute pass/kill criteria.

Reads mvp_pipeline output and evaluates:
  1. Trace collection + parsing success rate (>= 80%)
  2. Teacher precision (>= 0.6, kill < 0.5)
  3. Structural win rate on >2K token subset (> 50%, p < 0.15)
  4. Gray zone tiebreaker via 5-case qualitative analysis

Usage:
    python mvp_analysis.py --results-dir ./mvp_results
    python mvp_analysis.py --dry-run
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import random
import sys
import textwrap
from collections import defaultdict
from math import comb
from typing import Any, Dict, List, Optional


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_csv(path: str) -> List[Dict[str, Any]]:
    rows: list[dict] = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["repair_success"] = str(row["repair_success"]).strip().lower() in ("true", "1", "yes")
            row["tokens_used"] = int(float(row.get("tokens_used", 0)))
            row["compression_ratio"] = float(row.get("compression_ratio", 1.0))
            row["trace_events_count"] = int(float(row.get("trace_events_count", 0)))
            row["segments_count"] = int(float(row.get("segments_count", 0)))
            rows.append(row)
    return rows


def group_by_instance(rows: List[Dict]) -> Dict[str, Dict[str, Dict]]:
    instances: dict[str, dict] = defaultdict(dict)
    for row in rows:
        instances[row["instance_id"]][row["condition"]] = row
    return dict(instances)


# ---------------------------------------------------------------------------
# Criterion 1: Trace collection & structural parsing success
# ---------------------------------------------------------------------------

def criterion_1_trace_success(instances: Dict) -> Dict:
    total = len(instances)
    successes = 0
    failures: list[str] = []
    for iid, conds in instances.items():
        ref = conds.get("structural_filtered", conds.get("full_trace", {}))
        has_trace = ref.get("trace_events_count", 0) > 0
        has_segments = ref.get("segments_count", 0) > 0
        if has_trace and has_segments:
            successes += 1
        else:
            failures.append(iid)

    rate = successes / max(total, 1)
    killed = rate < 0.6
    passed = rate >= 0.8
    return {
        "criterion": 1,
        "name": "Trace Collection & Parsing",
        "threshold": ">=80% (kill <60%)",
        "value": f"{successes}/{total} ({rate:.1%})",
        "rate": round(rate, 4),
        "passed": passed,
        "verdict": "PASS" if passed else ("KILL" if killed else "WARN"),
        "failed_instances": failures,
    }


# ---------------------------------------------------------------------------
# Criterion 2: Teacher annotation precision
# ---------------------------------------------------------------------------

def _load_teacher_segments(results_dir: str) -> List[Dict]:
    segments: list[dict] = []
    teacher_dir = os.path.join(results_dir, "teacher_scores")
    if os.path.isdir(teacher_dir):
        for fname in sorted(os.listdir(teacher_dir)):
            if not fname.endswith(".json"):
                continue
            with open(os.path.join(teacher_dir, fname)) as f:
                data = json.load(f)
                if isinstance(data, list):
                    segments.extend(data)
                elif isinstance(data, dict) and "scored_segments" in data:
                    segments.extend(data["scored_segments"])

    combined = os.path.join(results_dir, "teacher_scores.json")
    if os.path.isfile(combined):
        with open(combined) as f:
            data = json.load(f)
            if isinstance(data, list):
                segments = data
            elif isinstance(data, dict):
                segments = data.get("segments", data.get("scored_segments", []))
    return segments


def criterion_2_teacher_precision(results_dir: str, sample_size: int = 50) -> Dict:
    scored = _load_teacher_segments(results_dir)
    if not scored:
        return {
            "criterion": 2,
            "name": "Teacher Precision",
            "threshold": ">=0.6 (kill <0.5)",
            "value": "N/A — no scored-segment data found",
            "rate": None,
            "passed": None,
            "verdict": "DATA_MISSING",
            "note": "Place teacher_scores.json or teacher_scores/*.json in results-dir",
        }

    sampled = random.sample(scored, min(sample_size, len(scored)))
    has_gt = any("ground_truth" in s for s in sampled)

    keep_segs = [s for s in sampled if s.get("label") == "keep"]
    if not keep_segs:
        precision = 0.0
    elif has_gt:
        tp = sum(1 for s in keep_segs if s.get("ground_truth") == "keep")
        precision = tp / len(keep_segs)
    else:
        high_conf = sum(1 for s in keep_segs if s.get("confidence", 0) >= 0.7)
        precision = high_conf / len(keep_segs)

    passed = precision >= 0.6
    killed = precision < 0.5
    method = "ground_truth" if has_gt else "confidence_proxy"
    return {
        "criterion": 2,
        "name": "Teacher Precision",
        "threshold": ">=0.6 (kill <0.5)",
        "value": f"{precision:.3f} (n={len(sampled)}, {method})",
        "rate": round(precision, 4),
        "passed": passed,
        "verdict": "PASS" if passed else ("KILL" if killed else "WARN"),
        "sample_size": len(sampled),
        "total_segments": len(scored),
        "method": method,
    }


# ---------------------------------------------------------------------------
# Criterion 3: Structural win rate on >2K-token subset
# ---------------------------------------------------------------------------

def _binomial_p_one_sided(wins: int, total: int) -> float:
    if total == 0:
        return 1.0
    return sum(comb(total, i) for i in range(wins, total + 1)) / (2 ** total)


def criterion_3_win_rate(instances: Dict) -> Dict:
    long_trace: dict[str, dict] = {}
    for iid, conds in instances.items():
        ft_tok = conds.get("full_trace", {}).get("tokens_used", 0)
        nt_tok = conds.get("no_trace", {}).get("tokens_used", 0)
        trace_tokens = ft_tok - nt_tok
        if trace_tokens > 2000:
            long_trace[iid] = conds

    if not long_trace:
        long_trace = instances
        subset_note = "all (none exceeded 2K trace tokens)"
    else:
        subset_note = f"{len(long_trace)}/{len(instances)} with >2K trace tokens"

    s_wins = 0
    l_wins = 0
    ties = 0
    pair_details: list[dict] = []
    for iid, conds in long_trace.items():
        s_ok = conds.get("structural_filtered", {}).get("repair_success", False)
        l_ok = conds.get("line_filtered", {}).get("repair_success", False)
        if s_ok and not l_ok:
            s_wins += 1
            outcome = "structural_win"
        elif l_ok and not s_ok:
            l_wins += 1
            outcome = "line_win"
        else:
            ties += 1
            outcome = "tie_both_pass" if (s_ok and l_ok) else "tie_both_fail"
        pair_details.append({"instance_id": iid, "structural": s_ok, "line": l_ok, "outcome": outcome})

    discordant = s_wins + l_wins
    win_rate = s_wins / discordant if discordant else 0.5
    p_value = _binomial_p_one_sided(s_wins, discordant)

    passed = win_rate > 0.5 and p_value < 0.15
    gray = 0.5 <= win_rate <= 0.55 and p_value >= 0.15
    killed = win_rate <= 0.5 and not gray

    return {
        "criterion": 3,
        "name": "Structural Win Rate (>2K subset)",
        "threshold": ">50% win rate, p<0.15",
        "value": f"{win_rate:.3f} (p={p_value:.4f})",
        "win_rate": round(win_rate, 4),
        "p_value": round(p_value, 4),
        "structural_wins": s_wins,
        "line_wins": l_wins,
        "ties": ties,
        "discordant_pairs": discordant,
        "subset_size": len(long_trace),
        "subset_note": subset_note,
        "passed": passed,
        "gray_zone": gray,
        "verdict": "PASS" if passed else ("GRAY_ZONE" if gray else "KILL"),
        "pair_details": pair_details,
    }


# ---------------------------------------------------------------------------
# Case study selection
# ---------------------------------------------------------------------------

def select_case_studies(instances: Dict, n: int = 5) -> List[Dict]:
    candidates: list[dict] = []
    for iid, conds in instances.items():
        s = conds.get("structural_filtered", {})
        l = conds.get("line_filtered", {})
        s_ok = s.get("repair_success", False)
        l_ok = l.get("repair_success", False)
        if s_ok and not l_ok:
            candidates.append({
                "instance_id": iid,
                "type": "structural_exclusive_win",
                "structural_tokens": s.get("tokens_used", 0),
                "line_tokens": l.get("tokens_used", 0),
                "compression_ratio": s.get("compression_ratio", 0),
                "trace_events": s.get("trace_events_count", 0),
            })

    candidates.sort(key=lambda x: x.get("compression_ratio", 1.0))

    if len(candidates) < n:
        for iid, conds in instances.items():
            s = conds.get("structural_filtered", {})
            l = conds.get("line_filtered", {})
            if s.get("repair_success") and l.get("repair_success"):
                s_tok = s.get("tokens_used", 0)
                l_tok = l.get("tokens_used", 0)
                if s_tok < l_tok:
                    candidates.append({
                        "instance_id": iid,
                        "type": "both_pass_structural_cheaper",
                        "structural_tokens": s_tok,
                        "line_tokens": l_tok,
                        "compression_ratio": s.get("compression_ratio", 0),
                    })

    return candidates[:n]


# ---------------------------------------------------------------------------
# Overall verdict
# ---------------------------------------------------------------------------

def compute_overall_verdict(criteria: List[Dict]) -> str:
    for c in criteria:
        if c.get("verdict") == "KILL":
            return "KILL"
    gray = any(c.get("gray_zone") for c in criteria)
    missing = any(c.get("verdict") == "DATA_MISSING" for c in criteria)
    evaluated = [c for c in criteria if c.get("verdict") not in ("DATA_MISSING",)]
    all_pass = all(c.get("passed") for c in evaluated) if evaluated else False

    if all_pass and not missing:
        return "PASS"
    if gray:
        return "GRAY_ZONE — qualitative tiebreaker needed"
    if missing:
        return "INCOMPLETE — missing data for some criteria"
    return "FAIL"


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def print_judgment_table(criteria: List[Dict], overall: str):
    markers = {"PASS": "+", "KILL": "X", "WARN": "!", "GRAY_ZONE": "~", "DATA_MISSING": "?"}
    print("\n" + "=" * 68)
    print("  DTD MVP Pass/Kill Judgment")
    print("=" * 68)
    for c in criteria:
        v = c.get("verdict", "?")
        m = markers.get(v, " ")
        print(f"\n  [{m}] Criterion {c['criterion']}: {c['name']}")
        print(f"      Threshold : {c['threshold']}")
        print(f"      Result    : {c['value']}")
        print(f"      Verdict   : {v}")
    print("\n" + "-" * 68)
    print(f"  OVERALL: {overall}")
    print("=" * 68)


def print_case_studies(cases: List[Dict]):
    if not cases:
        print("\n  No case study candidates (no structural exclusive wins).")
        return
    print(f"\n  Case Study Candidates ({len(cases)}):")
    for i, cs in enumerate(cases, 1):
        print(f"    {i}. {cs['instance_id']}  [{cs['type']}]")
        parts = []
        if "compression_ratio" in cs:
            parts.append(f"compress={cs['compression_ratio']:.2f}")
        if "structural_tokens" in cs:
            parts.append(f"s_tok={cs['structural_tokens']}")
        if "line_tokens" in cs:
            parts.append(f"l_tok={cs['line_tokens']}")
        if parts:
            print(f"       {', '.join(parts)}")


def save_judgment(criteria: List[Dict], overall: str, cases: List[Dict],
                  meta: Dict, output_path: str):
    judgment = {
        "overall_verdict": overall,
        "criteria": [],
        "case_study_candidates": cases,
        "metadata": meta,
    }
    skip_keys = {"failed_instances", "pair_details"}
    for c in criteria:
        judgment["criteria"].append({k: v for k, v in c.items() if k not in skip_keys})

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(judgment, f, indent=2, default=str)
    print(f"\n  Judgment saved to {output_path}")


# ---------------------------------------------------------------------------
# Mock data for dry-run
# ---------------------------------------------------------------------------

MOCK_PROJECTS = [
    "ansible", "black", "cookiecutter", "fastapi", "httpie",
    "keras", "luigi", "pandas", "PySnooper", "sanic",
    "scrapy", "spacy", "thefuck", "tornado", "tqdm", "youtube-dl",
]


def generate_mock_data() -> List[Dict[str, Any]]:
    rows: list[dict] = []
    idx = 0
    for p in MOCK_PROJECTS:
        for bug_id in range(1, 4):
            if idx >= 40:
                break
            idx += 1
            iid = f"{p}_{bug_id}"

            trace_ok = random.random() < 0.85
            trace_events = random.randint(500, 5000) if trace_ok else 0
            seg_s = random.randint(3, 20) if trace_ok else 0
            seg_l = random.randint(5, 30) if trace_ok else 0

            base_tok = random.randint(800, 1500)
            ft_tok = base_tok + random.randint(1000, 6000) if trace_ok else base_tok
            st_tok = base_tok + random.randint(200, 1500) if trace_ok else base_tok
            lt_tok = base_tok + random.randint(300, 2000) if trace_ok else base_tok
            comp = st_tok / max(ft_tok, 1)

            no_ok = random.random() < 0.30
            ft_ok = random.random() < 0.45 if trace_ok else no_ok
            s_ok = random.random() < 0.50 if trace_ok else no_ok
            l_ok = random.random() < 0.35 if trace_ok else no_ok

            for cond, success, tok, seg in [
                ("no_trace", no_ok, base_tok, seg_l),
                ("full_trace", ft_ok, ft_tok, seg_l),
                ("structural_filtered", s_ok, st_tok, seg_s),
                ("line_filtered", l_ok, lt_tok, seg_l),
            ]:
                rows.append({
                    "instance_id": iid,
                    "condition": cond,
                    "repair_success": success,
                    "tokens_used": tok,
                    "compression_ratio": comp,
                    "trace_events_count": trace_events,
                    "segments_count": seg,
                })
    return rows


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="DTD MVP results analysis — compute pass/kill criteria",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Pass criteria:
              1. >=80%% trace collection + parsing success
              2. Teacher precision >= 0.6 (kill < 0.5)
              3. Structural win rate > 50%% on >2K-token subset (p < 0.15)
              4. Gray zone -> 5-case qualitative tiebreaker
        """),
    )
    parser.add_argument("--results-dir", default="./mvp_results",
                        help="Directory with mvp_results.csv (default: ./mvp_results)")
    parser.add_argument("--csv", default=None,
                        help="Explicit path to results CSV")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for sampling (default: 42)")
    parser.add_argument("--output", default=None,
                        help="Path for mvp_judgment.json")
    parser.add_argument("--dry-run", action="store_true",
                        help="Use mock data for testing")
    args = parser.parse_args()

    random.seed(args.seed)
    results_dir = os.path.abspath(args.results_dir)
    csv_path = args.csv or os.path.join(results_dir, "mvp_results.csv")
    output_path = args.output or os.path.join(results_dir, "mvp_judgment.json")

    if args.dry_run:
        rows = generate_mock_data()
        print(f"[dry-run] Mock data: {len(set(r['instance_id'] for r in rows))} instances x 4 conditions")
    else:
        if not os.path.isfile(csv_path):
            print(f"Error: {csv_path} not found. Run mvp_pipeline.py first or use --dry-run.",
                  file=sys.stderr)
            sys.exit(1)
        rows = load_csv(csv_path)
        print(f"Loaded {len(rows)} rows from {csv_path}")

    instances = group_by_instance(rows)
    conditions = sorted(set(r["condition"] for r in rows))
    print(f"{len(instances)} instances, conditions: {conditions}")

    c1 = criterion_1_trace_success(instances)
    c2 = criterion_2_teacher_precision(results_dir)
    c3 = criterion_3_win_rate(instances)
    criteria = [c1, c2, c3]

    overall = compute_overall_verdict(criteria)
    cases = select_case_studies(instances, n=5)

    print_judgment_table(criteria, overall)

    if c3.get("pair_details"):
        print(f"\n  Win/Loss: {c3['structural_wins']}W / {c3['line_wins']}L / {c3['ties']}T"
              f"  (subset: {c3['subset_note']})")

    print_case_studies(cases)

    if c1.get("failed_instances"):
        fails = c1["failed_instances"]
        shown = fails[:10]
        print(f"\n  Trace failures ({len(fails)}): {', '.join(shown)}"
              + (f" ..." if len(fails) > 10 else ""))

    meta = {
        "results_dir": results_dir,
        "csv_path": csv_path,
        "total_instances": len(instances),
        "seed": args.seed,
        "dry_run": args.dry_run,
    }
    save_judgment(criteria, overall, cases, meta, output_path)


if __name__ == "__main__":
    main()

# Phase 3 v2 result analysis — generates comparison tables, head-to-head, and statistical tests.
from __future__ import annotations

import argparse
import csv
import json
import math
import os
import sys
from collections import defaultdict
from typing import Any, Dict, List, Optional, Tuple

CONDITIONS = ["no_trace", "full_trace", "structural_filtered", "line_filtered"]

# ── Data loading ──────────────────────────────────────────────────────────────

def load_results_csv(path: str) -> List[Dict[str, Any]]:
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            r["test_pass"] = r["test_pass"].strip().lower() in ("true", "1", "yes")
            r["diff_apply_success"] = r["diff_apply_success"].strip().lower() in ("true", "1", "yes")
            for k in ("tokens_input", "tokens_output", "llm_judge_score"):
                if k in r and r[k] not in (None, ""):
                    try:
                        r[k] = int(float(r[k]))
                    except (ValueError, TypeError):
                        r[k] = 0
                else:
                    r[k] = 0
            rows.append(r)
    return rows


def load_results_checkpoint(path: str) -> List[Dict[str, Any]]:
    with open(path) as f:
        data = json.load(f)
    rows = []
    for instance_rows in data.values():
        if isinstance(instance_rows, list):
            rows.extend(instance_rows)
        elif isinstance(instance_rows, dict):
            rows.append(instance_rows)
    for r in rows:
        for k in ("tokens_input", "tokens_output", "llm_judge_score"):
            if k not in r:
                r[k] = 0
        r.setdefault("test_pass", False)
        r.setdefault("diff_apply_success", False)
    return rows


def load_results(csv_path: Optional[str], checkpoint_path: Optional[str]) -> List[Dict[str, Any]]:
    if csv_path and os.path.isfile(csv_path):
        rows = load_results_csv(csv_path)
        if rows:
            return rows
    if checkpoint_path and os.path.isfile(checkpoint_path):
        return load_results_checkpoint(checkpoint_path)
    if csv_path:
        base = os.path.dirname(csv_path) or "."
        ckpt = os.path.join(base, "phase3_v2_checkpoint.json")
        if os.path.isfile(ckpt):
            return load_results_checkpoint(ckpt)
    return []


def load_oracle(path: str) -> Dict[str, dict]:
    if not path or not os.path.isfile(path):
        return {}
    with open(path) as f:
        return json.load(f)


# ── Index helpers ─────────────────────────────────────────────────────────────

def build_index(rows: List[dict]) -> Dict[str, Dict[str, dict]]:
    """Returns {instance_id: {condition: row}}"""
    idx: Dict[str, Dict[str, dict]] = defaultdict(dict)
    for r in rows:
        idx[r["instance_id"]][r["condition"]] = r
    return dict(idx)


def get_instances(idx: dict) -> List[str]:
    return sorted(idx.keys())


def get_conditions(idx: dict) -> List[str]:
    seen = set()
    for conds in idx.values():
        seen.update(conds.keys())
    return [c for c in CONDITIONS if c in seen] + sorted(seen - set(CONDITIONS))


# ── Table 1: Per-instance breakdown ──────────────────────────────────────────

def fmt_cell(r: Optional[dict]) -> str:
    if r is None:
        return "-"
    tp = "P" if r.get("test_pass") else "F"
    judge = r.get("llm_judge_score", 0)
    return f"{tp}/{judge}"


def per_instance_table(idx: dict, conditions: List[str]) -> str:
    instances = get_instances(idx)
    header = "| instance |" + "|".join(f" {c} " for c in conditions) + "|"
    sep = "|" + "|".join("---" for _ in range(len(conditions) + 1)) + "|"
    lines = [header, sep]
    for inst in instances:
        cells = [fmt_cell(idx[inst].get(c)) for c in conditions]
        lines.append(f"| {inst} |" + "|".join(f" {c} " for c in cells) + "|")
    lines.append("")
    lines.append("_Cell format: test_pass(P/F) / judge_score_")
    return "\n".join(lines)


# ── Table 2: Condition comparison summary ────────────────────────────────────

def condition_summary(rows: List[dict], conditions: List[str]) -> str:
    by_cond: Dict[str, List[dict]] = defaultdict(list)
    for r in rows:
        by_cond[r["condition"]].append(r)

    header = "| condition | n | test_pass_rate | avg_judge | diff_apply_rate | avg_tokens_in | avg_tokens_out |"
    sep = "|---|---|---|---|---|---|---|"
    lines = [header, sep]
    for c in conditions:
        rs = by_cond.get(c, [])
        n = len(rs)
        if n == 0:
            lines.append(f"| {c} | 0 | - | - | - | - | - |")
            continue
        tp = sum(1 for r in rs if r.get("test_pass"))
        da = sum(1 for r in rs if r.get("diff_apply_success"))
        avg_j = sum(r.get("llm_judge_score", 0) for r in rs) / n
        avg_ti = sum(r.get("tokens_input", 0) for r in rs) / n
        avg_to = sum(r.get("tokens_output", 0) for r in rs) / n
        lines.append(
            f"| {c} | {n} | {tp}/{n} ({tp/n*100:.0f}%) | {avg_j:.2f} | {da}/{n} ({da/n*100:.0f}%) | {avg_ti:.0f} | {avg_to:.0f} |"
        )
    return "\n".join(lines)


# ── Table 3: Head-to-head ────────────────────────────────────────────────────

def compare_pair(r_a: Optional[dict], r_b: Optional[dict]) -> str:
    """Returns 'win', 'loss', 'tie', or 'skip'."""
    if r_a is None or r_b is None:
        return "skip"
    tp_a, tp_b = r_a.get("test_pass", False), r_b.get("test_pass", False)
    if tp_a and not tp_b:
        return "win"
    if not tp_a and tp_b:
        return "loss"
    ja, jb = r_a.get("llm_judge_score", 0), r_b.get("llm_judge_score", 0)
    if ja > jb:
        return "win"
    if ja < jb:
        return "loss"
    return "tie"


def head_to_head(idx: dict, pairs: List[Tuple[str, str]]) -> str:
    instances = get_instances(idx)
    header = "| comparison | win | tie | loss | n |"
    sep = "|---|---|---|---|---|"
    lines = [header, sep]
    for cond_a, cond_b in pairs:
        w, t, l, n = 0, 0, 0, 0
        for inst in instances:
            r_a = idx[inst].get(cond_a)
            r_b = idx[inst].get(cond_b)
            result = compare_pair(r_a, r_b)
            if result == "skip":
                continue
            n += 1
            if result == "win":
                w += 1
            elif result == "loss":
                l += 1
            else:
                t += 1
        lines.append(f"| {cond_a} vs {cond_b} | {w} | {t} | {l} | {n} |")
    lines.append("")
    lines.append("_win = first condition better (test_pass primary, judge tiebreaker)_")
    return "\n".join(lines)


DEFAULT_PAIRS = [
    ("structural_filtered", "no_trace"),
    ("line_filtered", "no_trace"),
    ("full_trace", "no_trace"),
    ("structural_filtered", "line_filtered"),
]

# ── Oracle filtering ─────────────────────────────────────────────────────────

def oracle_valid_instances(oracle: dict) -> set:
    valid = set()
    for inst, info in oracle.items():
        if info.get("test_pass", info.get("pass", False)):
            valid.add(inst)
    return valid


def oracle_section(idx: dict, oracle: dict, conditions: List[str], rows: List[dict]) -> str:
    valid = oracle_valid_instances(oracle)
    if not valid:
        all_insts = set(oracle.keys())
        return (
            f"Oracle: 0/{len(all_insts)} instances pass ground-truth test.\n"
            "No oracle-valid subset to filter on."
        )

    lines = [f"Oracle-valid instances ({len(valid)}/{len(oracle)}): {', '.join(sorted(valid))}", ""]

    filtered_rows = [r for r in rows if r["instance_id"] in valid]
    filtered_idx = build_index(filtered_rows)

    lines.append("### Per-instance (oracle-valid only)")
    lines.append("")
    lines.append(per_instance_table(filtered_idx, conditions))
    lines.append("")
    lines.append("### Condition summary (oracle-valid only)")
    lines.append("")
    lines.append(condition_summary(filtered_rows, conditions))
    lines.append("")
    lines.append("### Head-to-head (oracle-valid only)")
    lines.append("")
    lines.append(head_to_head(filtered_idx, DEFAULT_PAIRS))
    return "\n".join(lines)


# ── Statistical tests ────────────────────────────────────────────────────────

def sign_test(wins: int, losses: int) -> float:
    n = wins + losses
    if n == 0:
        return 1.0
    k = min(wins, losses)
    p = 0.0
    for i in range(k + 1):
        p += math.comb(n, i) * (0.5 ** n)
    return p * 2  # two-tailed


def wilcoxon_approx(diffs: List[float]) -> Optional[float]:
    nonzero = [(abs(d), 1 if d > 0 else -1) for d in diffs if d != 0]
    n = len(nonzero)
    if n < 5:
        return None
    nonzero.sort(key=lambda x: x[0])
    ranks = list(range(1, n + 1))
    t_plus = sum(ranks[i] for i in range(n) if nonzero[i][1] > 0)
    mean_t = n * (n + 1) / 4
    std_t = math.sqrt(n * (n + 1) * (2 * n + 1) / 24)
    if std_t == 0:
        return None
    z = (t_plus - mean_t) / std_t
    p = 2 * (1 - _norm_cdf(abs(z)))
    return p


def _norm_cdf(x: float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def stats_section(idx: dict, pairs: List[Tuple[str, str]]) -> str:
    instances = get_instances(idx)
    lines = ["| comparison | sign_test (test_pass) | wilcoxon (judge) |", "|---|---|---|"]
    for cond_a, cond_b in pairs:
        wins, losses = 0, 0
        judge_diffs = []
        for inst in instances:
            ra = idx[inst].get(cond_a)
            rb = idx[inst].get(cond_b)
            if ra is None or rb is None:
                continue
            tpa = ra.get("test_pass", False)
            tpb = rb.get("test_pass", False)
            if tpa and not tpb:
                wins += 1
            elif not tpa and tpb:
                losses += 1
            ja = ra.get("llm_judge_score", 0)
            jb = rb.get("llm_judge_score", 0)
            judge_diffs.append(ja - jb)

        p_sign = sign_test(wins, losses)
        p_wilc = wilcoxon_approx(judge_diffs)
        sign_str = f"w={wins} l={losses} p={p_sign:.3f}"
        wilc_str = f"p={p_wilc:.3f}" if p_wilc is not None else "n<5"
        lines.append(f"| {cond_a} vs {cond_b} | {sign_str} | {wilc_str} |")
    return "\n".join(lines)


# ── Kill criteria (C001) ─────────────────────────────────────────────────────

def kill_criteria_check(idx: dict, rows: List[dict]) -> str:
    by_cond: Dict[str, List[dict]] = defaultdict(list)
    for r in rows:
        by_cond[r["condition"]].append(r)

    lines = ["### Kill Criteria C001 Check", ""]

    nt = by_cond.get("no_trace", [])
    sf = by_cond.get("structural_filtered", [])
    n_nt = len(nt)
    n_sf = len(sf)

    # (1) no_trace avg judge >= 3.0
    avg_nt_judge = sum(r.get("llm_judge_score", 0) for r in nt) / max(n_nt, 1)
    c1_pass = avg_nt_judge >= 3.0
    lines.append(f"1. no_trace avg judge = {avg_nt_judge:.2f} {'>='}  3.0 → **{'PASS' if c1_pass else 'FAIL'}**")

    # (2) structural > no_trace (sign test p<0.15)
    instances = get_instances(idx)
    wins, losses = 0, 0
    judge_diffs = []
    for inst in instances:
        ra = idx[inst].get("structural_filtered")
        rb = idx[inst].get("no_trace")
        if ra is None or rb is None:
            continue
        tpa, tpb = ra.get("test_pass", False), rb.get("test_pass", False)
        if tpa and not tpb:
            wins += 1
        elif not tpa and tpb:
            losses += 1
        judge_diffs.append(ra.get("llm_judge_score", 0) - rb.get("llm_judge_score", 0))
    p_sign = sign_test(wins, losses)
    p_wilc = wilcoxon_approx(judge_diffs)
    c2_pass = (p_sign < 0.15) or (p_wilc is not None and p_wilc < 0.15)
    lines.append(f"2. structural > no_trace: sign p={p_sign:.3f}, wilcoxon p={p_wilc:.3f if p_wilc is not None else 'n/a'} → **{'PASS' if c2_pass else 'FAIL'}** (need p<0.15)")

    # (3) at least 1 condition test pass > 0%
    any_pass = False
    for c in CONDITIONS:
        rs = by_cond.get(c, [])
        if any(r.get("test_pass") for r in rs):
            any_pass = True
            break
    c3_pass = any_pass
    lines.append(f"3. >=1 condition with test_pass > 0% → **{'PASS' if c3_pass else 'FAIL'}**")

    lines.append("")
    overall = c1_pass and c2_pass and c3_pass
    lines.append(f"**Overall: {'PASS — proceed' if overall else 'FAIL — MVP kill criteria not met'}**")
    return "\n".join(lines)


# ── JSON export ──────────────────────────────────────────────────────────────

def build_json_output(idx: dict, rows: List[dict], conditions: List[str], oracle: dict) -> dict:
    by_cond: Dict[str, List[dict]] = defaultdict(list)
    for r in rows:
        by_cond[r["condition"]].append(r)

    cond_summary = {}
    for c in conditions:
        rs = by_cond.get(c, [])
        n = len(rs)
        if n == 0:
            continue
        cond_summary[c] = {
            "n": n,
            "test_pass": sum(1 for r in rs if r.get("test_pass")),
            "diff_apply_success": sum(1 for r in rs if r.get("diff_apply_success")),
            "avg_judge": round(sum(r.get("llm_judge_score", 0) for r in rs) / n, 3),
            "avg_tokens_input": round(sum(r.get("tokens_input", 0) for r in rs) / n),
            "avg_tokens_output": round(sum(r.get("tokens_output", 0) for r in rs) / n),
        }

    h2h = {}
    instances = get_instances(idx)
    for ca, cb in DEFAULT_PAIRS:
        w, t, l = 0, 0, 0
        for inst in instances:
            result = compare_pair(idx[inst].get(ca), idx[inst].get(cb))
            if result == "win":
                w += 1
            elif result == "loss":
                l += 1
            elif result == "tie":
                t += 1
        h2h[f"{ca}_vs_{cb}"] = {"win": w, "tie": t, "loss": l}

    per_instance = {}
    for inst in instances:
        per_instance[inst] = {}
        for c in conditions:
            r = idx[inst].get(c)
            if r:
                per_instance[inst][c] = {
                    "test_pass": r.get("test_pass", False),
                    "diff_apply_success": r.get("diff_apply_success", False),
                    "llm_judge_score": r.get("llm_judge_score", 0),
                    "tokens_input": r.get("tokens_input", 0),
                    "tokens_output": r.get("tokens_output", 0),
                }

    oracle_valid = sorted(oracle_valid_instances(oracle)) if oracle else []

    return {
        "n_instances": len(instances),
        "n_rows": len(rows),
        "instances": instances,
        "conditions": conditions,
        "condition_summary": cond_summary,
        "head_to_head": h2h,
        "per_instance": per_instance,
        "oracle_valid_instances": oracle_valid,
    }


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Analyze Phase 3 v2 results")
    parser.add_argument("--csv-path", help="Path to phase3_v2_results.csv")
    parser.add_argument("--checkpoint-path", help="Path to phase3_v2_checkpoint.json (fallback if no CSV)")
    parser.add_argument("--oracle-path", help="Path to phase3_v2_oracle.json")
    parser.add_argument("--output-json", default="phase3_v2_analysis.json", help="JSON output path")
    parser.add_argument("--oracle-only", action="store_true", help="Only show oracle-valid instances")
    args = parser.parse_args()

    # Auto-detect paths relative to pipeline_output
    base_dirs = [
        os.path.dirname(args.csv_path) if args.csv_path else None,
        os.path.dirname(args.checkpoint_path) if args.checkpoint_path else None,
        "/root/trace_distill_repair/pipeline_output",
        "pipeline_output",
        ".",
    ]

    if not args.csv_path:
        for d in base_dirs:
            if d is None:
                continue
            candidate = os.path.join(d, "phase3_v2_results.csv")
            if os.path.isfile(candidate):
                args.csv_path = candidate
                break

    if not args.checkpoint_path:
        for d in base_dirs:
            if d is None:
                continue
            candidate = os.path.join(d, "phase3_v2_checkpoint.json")
            if os.path.isfile(candidate):
                args.checkpoint_path = candidate
                break

    if not args.oracle_path:
        for d in base_dirs:
            if d is None:
                continue
            candidate = os.path.join(d, "phase3_v2_oracle.json")
            if os.path.isfile(candidate):
                args.oracle_path = candidate
                break

    rows = load_results(args.csv_path, args.checkpoint_path)
    if not rows:
        print("ERROR: No result data found.", file=sys.stderr)
        print(f"  Tried CSV: {args.csv_path}", file=sys.stderr)
        print(f"  Tried checkpoint: {args.checkpoint_path}", file=sys.stderr)
        sys.exit(1)

    idx = build_index(rows)
    conditions = get_conditions(idx)
    instances = get_instances(idx)
    oracle = load_oracle(args.oracle_path)

    source = args.csv_path if (args.csv_path and os.path.isfile(args.csv_path)) else args.checkpoint_path
    print(f"# Phase 3 v2 Analysis")
    print(f"")
    print(f"Source: `{source}`  ")
    print(f"Instances: {len(instances)} | Conditions: {len(conditions)} | Total rows: {len(rows)}")
    print()

    if not args.oracle_only:
        print("## 1. Per-instance Breakdown")
        print()
        print(per_instance_table(idx, conditions))
        print()

        print("## 2. Condition Summary")
        print()
        print(condition_summary(rows, conditions))
        print()

        print("## 3. Head-to-Head")
        print()
        print(head_to_head(idx, DEFAULT_PAIRS))
        print()

        print("## 4. Statistical Tests")
        print()
        print(stats_section(idx, DEFAULT_PAIRS))
        print()

    if oracle:
        print("## 5. Oracle Baseline")
        print()
        print(oracle_section(idx, oracle, conditions, rows))
        print()

    print("## 6. Kill Criteria (C001)")
    print()
    print(kill_criteria_check(idx, rows))
    print()

    # JSON output
    out = build_json_output(idx, rows, conditions, oracle)
    with open(args.output_json, "w") as f:
        json.dump(out, f, indent=2)
    print(f"_JSON saved to `{args.output_json}`_")


if __name__ == "__main__":
    main()

"""MVP v4 profiling results analyzer: importance-based masking II analysis."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np


# ── Loading ──────────────────────────────────────────────────────────

def load_json(path: str | Path) -> dict:
    p = Path(path)
    if not p.exists():
        sys.exit(f"ERROR: {p} not found")
    with open(p) as f:
        return json.load(f)


# ── II Summary Table ─────────────────────────────────────────────────

def build_ii_table(data: dict) -> List[dict]:
    ii = data["interaction_index"]
    rows = []
    for phase, levels in sorted(ii.items()):
        for level, stats in sorted(levels.items()):
            ci_low = stats["ci_low"]
            ci_high = stats["ci_high"]
            ci_excludes_zero = (ci_low > 0) or (ci_high < 0)
            sign = "+" if stats["mean"] > 0 else ("-" if stats["mean"] < 0 else "0")
            rows.append({
                "phase": phase,
                "level": level,
                "mean": stats["mean"],
                "ci_low": ci_low,
                "ci_high": ci_high,
                "ci_excludes_zero": ci_excludes_zero,
                "pass": ci_excludes_zero,
                "sign": sign,
            })
    return rows


def print_ii_table(rows: List[dict]) -> None:
    header = f"{'Phase':<14} {'Level':>6} {'II Mean':>9} {'95% CI':>22} {'Sign':>5} {'Pass':>6}"
    print("\n" + "=" * 70)
    print("Per-Phase Interaction Index (v4 — Importance Masking)")
    print("=" * 70)
    print(header)
    print("-" * 70)
    for r in rows:
        ci_str = f"[{r['ci_low']:+.4f}, {r['ci_high']:+.4f}]"
        tag = "PASS" if r["pass"] else "FAIL"
        print(f"{r['phase']:<14} {r['level']:>6} {r['mean']:>+9.4f} {ci_str:>22} {r['sign']:>5} {tag:>6}")
    print("-" * 70)


# ── v3 Comparison ───────────────────────────────────────────────────

def compare_with_v3(v4_rows: List[dict], v3_data: dict) -> List[dict]:
    v3_ii = v3_data["interaction_index"]
    comparisons = []

    for r in v4_rows:
        phase, level = r["phase"], r["level"]
        v3_stats = v3_ii.get(phase, {}).get(level, None)
        if v3_stats is None:
            comparisons.append({
                "phase": phase,
                "level": level,
                "v4_mean": r["mean"],
                "v3_mean": None,
                "delta": None,
                "direction": "N/A (no v3 data)",
                "v4_pass": r["pass"],
                "v3_pass": None,
                "regression": False,
            })
            continue

        v3_mean = v3_stats["mean"]
        delta = r["mean"] - v3_mean

        v3_ci_low, v3_ci_high = v3_stats["ci_low"], v3_stats["ci_high"]
        v3_pass = (v3_ci_low > 0) or (v3_ci_high < 0)

        if abs(delta) < 1e-6:
            direction = "="
        elif delta > 0:
            direction = "↑"
        else:
            direction = "↓"

        regression = v3_pass and not r["pass"]

        comparisons.append({
            "phase": phase,
            "level": level,
            "v4_mean": r["mean"],
            "v3_mean": v3_mean,
            "delta": delta,
            "direction": direction,
            "v4_pass": r["pass"],
            "v3_pass": v3_pass,
            "regression": regression,
        })
    return comparisons


def print_v3_comparison(comparisons: List[dict]) -> None:
    print("\n" + "=" * 80)
    print("v4 vs v3 Comparison")
    print("=" * 80)
    header = f"{'Phase':<14} {'Level':>6} {'v3 II':>9} {'v4 II':>9} {'Δ':>9} {'Dir':>4} {'v3':>5} {'v4':>5} {'Regr':>5}"
    print(header)
    print("-" * 80)
    for c in comparisons:
        v3_str = f"{c['v3_mean']:+.4f}" if c["v3_mean"] is not None else "  N/A"
        delta_str = f"{c['delta']:+.4f}" if c["delta"] is not None else "  N/A"
        v3_tag = "PASS" if c["v3_pass"] else ("FAIL" if c["v3_pass"] is not None else " N/A")
        v4_tag = "PASS" if c["v4_pass"] else "FAIL"
        regr = "!!!" if c["regression"] else ""
        print(f"{c['phase']:<14} {c['level']:>6} {v3_str:>9} {c['v4_mean']:>+9.4f} {delta_str:>9} {c['direction']:>4} {v3_tag:>5} {v4_tag:>5} {regr:>5}")

    regressions = [c for c in comparisons if c["regression"]]
    if regressions:
        print(f"\n  WARNING: {len(regressions)} regression(s) — v3 PASS → v4 FAIL:")
        for c in regressions:
            print(f"    {c['phase']} / {c['level']}")
    else:
        print("\n  No regressions (all v3 PASS entries remain PASS in v4)")
    print("-" * 80)


# ── Importance vs Random Signal ─────────────────────────────────────

def analyze_importance_signal(data: dict, rows: List[dict]) -> dict:
    config = data.get("config", {})
    masking_method = config.get("masking_method", None)

    sign_pairs = []
    phases = sorted(set(r["phase"] for r in rows))
    levels = sorted(set(r["level"] for r in rows))

    lookup = {(r["phase"], r["level"]): r for r in rows}

    for level in levels:
        phase_rows = [(p, lookup[(p, level)]) for p in phases if (p, level) in lookup]
        for i in range(len(phase_rows)):
            for j in range(i + 1, len(phase_rows)):
                p1, r1 = phase_rows[i]
                p2, r2 = phase_rows[j]
                if r1["sign"] != r2["sign"] and r1["sign"] != "0" and r2["sign"] != "0":
                    sign_pairs.append({
                        "level": level,
                        "phase_a": p1,
                        "phase_b": p2,
                        "sign_a": r1["sign"],
                        "sign_b": r2["sign"],
                        "mean_a": r1["mean"],
                        "mean_b": r2["mean"],
                    })

    return {
        "masking_method": masking_method,
        "sign_reversal_pairs": sign_pairs,
        "n_sign_reversals": len(sign_pairs),
        "strong_signal": len(sign_pairs) > 0,
    }


def print_importance_signal(signal: dict) -> None:
    print("\n" + "=" * 70)
    print("Importance vs Random Signal Analysis")
    print("=" * 70)
    if signal["masking_method"]:
        print(f"  Masking method: {signal['masking_method']}")
    else:
        print("  Masking method: not specified in config")

    if signal["strong_signal"]:
        print(f"\n  STRONG SIGNAL: {signal['n_sign_reversals']} phase pair(s) with opposite II signs")
        for sp in signal["sign_reversal_pairs"]:
            print(f"    {sp['level']}: {sp['phase_a']}({sp['sign_a']}, {sp['mean_a']:+.4f}) vs "
                  f"{sp['phase_b']}({sp['sign_b']}, {sp['mean_b']:+.4f})")
    else:
        print("\n  No sign reversals detected between phase pairs")
    print("-" * 70)


# ── Verdict ──────────────────────────────────────────────────────────

def compute_verdict(data: dict, rows: List[dict], signal: dict) -> dict:
    pf = data.get("pass_fail", {})
    original = pf.get("overall", "UNKNOWN")

    n_pass = sum(1 for r in rows if r["pass"])
    n_total = len(rows)
    any_pass = n_pass > 0

    return {
        "overall": "PASS" if any_pass else "FAIL",
        "n_pass": n_pass,
        "n_total": n_total,
        "original_run_verdict": original,
        "has_sign_reversals": signal["strong_signal"],
        "masking_method": signal["masking_method"],
    }


def print_verdict(verdict: dict) -> None:
    tag = verdict["overall"]
    print("\n" + "=" * 70)
    print(f"Overall Verdict: {tag}")
    print("=" * 70)
    print(f"  Passing (phase, level) pairs: {verdict['n_pass']}/{verdict['n_total']}")
    print(f"  Original run verdict:         {verdict['original_run_verdict']}")
    print(f"  Sign reversal signal:         {'YES' if verdict['has_sign_reversals'] else 'NO'}")
    if verdict["masking_method"]:
        print(f"  Masking method:               {verdict['masking_method']}")
    print()


# ── Markdown Summary ─────────────────────────────────────────────────

def generate_markdown(
    verdict: dict,
    rows: List[dict],
    signal: dict,
    v3_comparisons: Optional[List[dict]],
    config: dict,
) -> str:
    lines = []
    lines.append("## MVP v4 Profiling Summary (Importance-Based Masking)")
    lines.append("")

    lines.append(f"**Verdict: {verdict['overall']}** — "
                 f"{verdict['n_pass']}/{verdict['n_total']} (phase, level) pairs pass CI test")
    if verdict["masking_method"]:
        lines.append(f"- Masking method: `{verdict['masking_method']}`")
    lines.append(f"- Sign reversal signal: {'YES' if verdict['has_sign_reversals'] else 'NO'}")
    lines.append("")

    # Config excerpt
    if config:
        lines.append("### Config")
        lines.append("```json")
        excerpt_keys = ["masking_method", "n_problems", "n_repeats", "sparsity_levels",
                        "model_name", "phases", "seed"]
        excerpt = {k: config[k] for k in excerpt_keys if k in config}
        lines.append(json.dumps(excerpt, indent=2))
        lines.append("```")
        lines.append("")

    # II table
    lines.append("### Interaction Index")
    lines.append("")
    lines.append("| Phase | Level | II Mean | 95% CI | Sign | Pass |")
    lines.append("|-------|-------|---------|--------|------|------|")
    for r in rows:
        ci = f"[{r['ci_low']:+.4f}, {r['ci_high']:+.4f}]"
        tag = "PASS" if r["pass"] else "FAIL"
        lines.append(f"| {r['phase']} | {r['level']} | {r['mean']:+.4f} | {ci} | {r['sign']} | {tag} |")
    lines.append("")

    # Sign reversals
    if signal["strong_signal"]:
        lines.append("### Sign Reversal Pairs (Strong Signal)")
        lines.append("")
        for sp in signal["sign_reversal_pairs"]:
            lines.append(f"- **{sp['level']}**: {sp['phase_a']} ({sp['sign_a']}, {sp['mean_a']:+.4f}) "
                         f"vs {sp['phase_b']} ({sp['sign_b']}, {sp['mean_b']:+.4f})")
        lines.append("")

    # v3 comparison
    if v3_comparisons:
        lines.append("### v3 → v4 Comparison")
        lines.append("")
        lines.append("| Phase | Level | v3 II | v4 II | Δ | Dir | Regression |")
        lines.append("|-------|-------|-------|-------|---|-----|------------|")
        for c in v3_comparisons:
            v3_str = f"{c['v3_mean']:+.4f}" if c["v3_mean"] is not None else "N/A"
            delta_str = f"{c['delta']:+.4f}" if c["delta"] is not None else "N/A"
            regr = "YES" if c["regression"] else ""
            lines.append(f"| {c['phase']} | {c['level']} | {v3_str} | {c['v4_mean']:+.4f} | {delta_str} | {c['direction']} | {regr} |")
        regressions = [c for c in v3_comparisons if c["regression"]]
        if regressions:
            lines.append("")
            lines.append(f"**WARNING**: {len(regressions)} regression(s) detected (v3 PASS → v4 FAIL)")
        lines.append("")

    return "\n".join(lines)


# ── Main ─────────────────────────────────────────────────────────────

def run(results_path: str, v3_path: Optional[str] = None, output_md: Optional[str] = None) -> dict:
    data = load_json(results_path)

    rows = build_ii_table(data)
    print_ii_table(rows)

    signal = analyze_importance_signal(data, rows)
    print_importance_signal(signal)

    v3_comparisons = None
    if v3_path:
        v3_data = load_json(v3_path)
        v3_comparisons = compare_with_v3(rows, v3_data)
        print_v3_comparison(v3_comparisons)

    verdict = compute_verdict(data, rows, signal)
    print_verdict(verdict)

    config = data.get("config", {})
    md = generate_markdown(verdict, rows, signal, v3_comparisons, config)

    if output_md:
        md_path = Path(output_md)
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(md)
        print(f"Saved: {md_path}")

    summary = {
        "interaction_index_table": rows,
        "importance_signal": signal,
        "v3_comparison": v3_comparisons,
        "verdict": verdict,
        "config": config,
    }

    out_json = Path(results_path).parent / "v4_analysis_summary.json"
    with open(out_json, "w") as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"Saved: {out_json}")

    return summary


def main():
    parser = argparse.ArgumentParser(description="Analyze MVP v4 profiling results (importance-based masking)")
    parser.add_argument("--results", required=True, help="Path to profiling_results.json")
    parser.add_argument("--v3_results", default=None, help="Path to v3 profiling_results.json for comparison")
    parser.add_argument("--output_md", default=None, help="Path to write summary markdown")
    args = parser.parse_args()
    run(args.results, args.v3_results, args.output_md)


if __name__ == "__main__":
    main()

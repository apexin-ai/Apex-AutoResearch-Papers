#!/usr/bin/env python3
"""
exp-001 expanded analysis: per-dataset accuracy, tiebreak stats, McNemar tests.

Input:  results/sica_expanded_14b.json (single JSON with summary + results array)
Output: markdown summary table (stdout) + analysis.json

Dependencies: Python 3.8+ (no external packages required; scipy optional for chi2 McNemar)

Usage:
  python scripts/analyze_expanded.py
  python scripts/analyze_expanded.py --results-dir results/sica_expanded_14b.json
  python scripts/analyze_expanded.py --results-dir results/ --output results/analysis.json
  python scripts/analyze_expanded.py --d012 results/sica_d012_14b.json
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
from collections import Counter, defaultdict


# ── Answer normalization ─────────────────────────────────────────

def _normalize_logic(ans: str) -> str:
    s = str(ans).strip().lower()
    mapping = {
        "true": "True", "t": "True", "yes": "True",
        "false": "False", "f": "False", "no": "False",
        "unknown": "Unknown", "u": "Unknown", "uncertain": "Unknown",
    }
    return mapping.get(s, str(ans).strip())


# ── McNemar's test (exact binomial, no scipy needed) ─────────────

def mcnemar_pvalue(a_correct: list[bool], b_correct: list[bool]) -> float:
    """Two-sided McNemar's test using exact binomial distribution."""
    n10 = sum(a and not b for a, b in zip(a_correct, b_correct))
    n01 = sum(not a and b for a, b in zip(a_correct, b_correct))
    n = n10 + n01
    if n == 0:
        return 1.0
    k = min(n10, n01)
    p = sum(math.comb(n, i) * 0.5 ** n for i in range(k + 1))
    return min(2.0 * p, 1.0)


# ── Core analysis ────────────────────────────────────────────────

def is_sc_tie(vote_dist: dict) -> bool:
    """SC tie: ≥2 answers share the maximum vote count."""
    if not vote_dist or len(vote_dist) < 2:
        return False
    counts = sorted(vote_dist.values(), reverse=True)
    return counts[0] == counts[1]


def analyze_group(problems: list[dict], label: str) -> dict:
    n = len(problems)
    if n == 0:
        return {"label": label, "n": 0}

    sica_correct = [bool(p["sica_correct"]) for p in problems]
    sc_correct = [bool(p["sc_correct"]) for p in problems]

    # C0: multi-candidate rate (≥2 distinct answers in vote distribution)
    c0_count = sum(1 for p in problems if len(p.get("sc_vote_distribution", {})) >= 2)

    # Tiebreak analysis
    tie_indices = []
    tie_sica_correct = []
    tie_sc_correct = []
    for i, p in enumerate(problems):
        if is_sc_tie(p.get("sc_vote_distribution", {})):
            tie_indices.append(p.get("problem_idx", i))
            tie_sica_correct.append(bool(p["sica_correct"]))
            tie_sc_correct.append(bool(p["sc_correct"]))

    sica_acc = sum(sica_correct) / n
    sc_acc = sum(sc_correct) / n
    delta_pp = (sica_acc - sc_acc) * 100
    pval = mcnemar_pvalue(sica_correct, sc_correct)

    # Disagreement breakdown
    sica_only = sum(a and not b for a, b in zip(sica_correct, sc_correct))
    sc_only = sum(not a and b for a, b in zip(sica_correct, sc_correct))

    result = {
        "label": label,
        "n": n,
        "c0_multi_candidate": c0_count,
        "c0_rate": c0_count / n,
        "sica_accuracy": sica_acc,
        "sica_correct": sum(sica_correct),
        "sc_accuracy": sc_acc,
        "sc_correct": sum(sc_correct),
        "delta_pp": delta_pp,
        "mcnemar_p": pval,
        "sica_only_correct": sica_only,
        "sc_only_correct": sc_only,
        "n_ties": len(tie_indices),
        "tie_indices": tie_indices,
    }

    if tie_indices:
        result["tie_sica_correct"] = sum(tie_sica_correct)
        result["tie_sica_accuracy"] = sum(tie_sica_correct) / len(tie_indices)
        result["tie_sc_correct"] = sum(tie_sc_correct)
    else:
        result["tie_sica_correct"] = 0
        result["tie_sica_accuracy"] = None
        result["tie_sc_correct"] = 0

    return result


def load_d012_tiebreak(d012_path: str) -> dict | None:
    """Load D012 pilot tiebreak stats for comparison."""
    if not d012_path or not os.path.exists(d012_path):
        return None
    with open(d012_path) as f:
        data = json.load(f)

    # Could be tiebreak_analysis.json or sica_d012_14b.json
    if "strategies" in data:
        # tiebreak_analysis.json format
        return {
            "n_total": data["n_total"],
            "n_tie": data["n_tie"],
            "sica_tie_accuracy": data["strategies"]["sica"]["accuracy"],
            "sica_tie_correct": data["strategies"]["sica"]["correct"],
        }
    elif "results" in data:
        # sica_d012_14b.json format — compute tiebreak from raw data
        problems = data["results"]
        ties = [p for p in problems if is_sc_tie(p.get("sc_vote_distribution", {}))]
        if not ties:
            return {"n_total": len(problems), "n_tie": 0, "sica_tie_accuracy": None, "sica_tie_correct": 0}
        return {
            "n_total": len(problems),
            "n_tie": len(ties),
            "sica_tie_accuracy": sum(p["sica_correct"] for p in ties) / len(ties),
            "sica_tie_correct": sum(p["sica_correct"] for p in ties),
        }
    return None


# ── Output formatting ────────────────────────────────────────────

def print_markdown(groups: list[dict], overall: dict, d012_tb: dict | None):
    print("\n## exp-001 Expanded Analysis (sica_expanded_14b)\n")

    # Main table
    header = "| Dataset | N | C0% | SICA Acc | SC Acc | Δ (pp) | McNemar p |"
    sep    = "|---------|---|-----|----------|--------|--------|-----------|"
    print(header)
    print(sep)
    for g in groups:
        sig = "*" if g["mcnemar_p"] < 0.05 else ""
        print(f"| {g['label']:15s} | {g['n']:3d} | {g['c0_rate']*100:5.1f} | "
              f"{g['sica_accuracy']*100:6.2f}% | {g['sc_accuracy']*100:6.2f}% | "
              f"{g['delta_pp']:+5.2f} | {g['mcnemar_p']:.4f}{sig} |")
    # Overall
    sig = "*" if overall["mcnemar_p"] < 0.05 else ""
    print(f"| {'**Overall**':15s} | {overall['n']:3d} | {overall['c0_rate']*100:5.1f} | "
          f"{overall['sica_accuracy']*100:6.2f}% | {overall['sc_accuracy']*100:6.2f}% | "
          f"{overall['delta_pp']:+5.2f} | {overall['mcnemar_p']:.4f}{sig} |")

    # Disagreement
    print(f"\nDisagreements: SICA-only correct = {overall['sica_only_correct']}, "
          f"SC-only correct = {overall['sc_only_correct']}")

    # Tiebreak table
    print("\n### Tiebreak Analysis\n")
    print("| Dataset | SC Ties | SICA Win | SICA Tie-Acc |")
    print("|---------|---------|----------|--------------|")
    for g in groups:
        if g["n_ties"] > 0:
            print(f"| {g['label']:15s} | {g['n_ties']:7d} | "
                  f"{g['tie_sica_correct']:8d} | {g['tie_sica_accuracy']*100:10.1f}% |")
        else:
            print(f"| {g['label']:15s} | {g['n_ties']:7d} |      n/a |          n/a |")
    if overall["n_ties"] > 0:
        print(f"| {'**Overall**':15s} | {overall['n_ties']:7d} | "
              f"{overall['tie_sica_correct']:8d} | {overall['tie_sica_accuracy']*100:10.1f}% |")
    else:
        print(f"| {'**Overall**':15s} | {overall['n_ties']:7d} |      n/a |          n/a |")

    # D012 comparison
    if d012_tb and d012_tb.get("n_tie", 0) > 0 and overall["n_ties"] > 0:
        print(f"\nD012 pilot comparison (n={d012_tb['n_total']}):")
        print(f"  D012 ties: {d012_tb['n_tie']}, "
              f"SICA tie-acc: {d012_tb['sica_tie_accuracy']*100:.1f}%")
        print(f"  Expanded ties: {overall['n_ties']}, "
              f"SICA tie-acc: {overall['tie_sica_accuracy']*100:.1f}%")
        d012_rate = d012_tb["n_tie"] / d012_tb["n_total"] * 100
        exp_rate = overall["n_ties"] / overall["n"] * 100
        print(f"  Tie rate: D012 {d012_rate:.1f}% → Expanded {exp_rate:.1f}%")

    # Key numbers
    print("\n### Key Numbers\n")
    print(f"- Total problems: {overall['n']}")
    print(f"- SICA accuracy: {overall['sica_accuracy']*100:.2f}% ({overall['sica_correct']}/{overall['n']})")
    print(f"- SC accuracy: {overall['sc_accuracy']*100:.2f}% ({overall['sc_correct']}/{overall['n']})")
    print(f"- Delta: {overall['delta_pp']:+.2f} pp (McNemar p={overall['mcnemar_p']:.4f})")
    print(f"- SC ties: {overall['n_ties']} ({overall['n_ties']/overall['n']*100:.1f}%)")
    if overall["n_ties"] > 0:
        print(f"- SICA tie-accuracy: {overall['tie_sica_accuracy']*100:.1f}% "
              f"({overall['tie_sica_correct']}/{overall['n_ties']})")


# ── File discovery ───────────────────────────────────────────────

def find_results_file(path: str) -> str:
    if os.path.isfile(path):
        return path
    if os.path.isdir(path):
        candidate = os.path.join(path, "sica_expanded_14b.json")
        if os.path.exists(candidate):
            return candidate
        jsons = [f for f in os.listdir(path) if f.endswith(".json") and "expanded" in f]
        if len(jsons) == 1:
            return os.path.join(path, jsons[0])
        if jsons:
            raise FileNotFoundError(
                f"Multiple expanded JSON files in {path}: {jsons}. Specify exact path.")
    raise FileNotFoundError(f"Cannot find results file at {path}")


# ── Main ─────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Analyze exp-001 (sica_expanded_14b) results: per-dataset accuracy, "
                    "tiebreak stats, McNemar significance tests.",
    )
    parser.add_argument(
        "--results-dir", default="results/sica_expanded_14b.json",
        help="Path to results JSON file or directory (default: results/sica_expanded_14b.json)",
    )
    parser.add_argument(
        "--output", default=None,
        help="Output JSON path (default: <results-dir>/analysis.json or alongside input file)",
    )
    parser.add_argument(
        "--d012", default=None,
        help="Path to D012 pilot data for tiebreak comparison "
             "(tries results/tiebreak_analysis.json and results/sica_d012_14b.json if not set)",
    )
    args = parser.parse_args()

    # Find and load results
    results_path = find_results_file(args.results_dir)
    with open(results_path) as f:
        data = json.load(f)
    problems = data["results"]
    n = len(problems)
    print(f"Loaded {n} problems from {results_path}")

    # Group by dataset
    by_dataset: dict[str, list[dict]] = defaultdict(list)
    for p in problems:
        ds = p.get("dataset", "unknown")
        by_dataset[ds].append(p)

    # Per-dataset analysis
    dataset_order = ["proofwriter", "folio"]
    groups = []
    for ds in dataset_order:
        if ds in by_dataset:
            groups.append(analyze_group(by_dataset[ds], ds))
    for ds in sorted(by_dataset.keys()):
        if ds not in dataset_order:
            groups.append(analyze_group(by_dataset[ds], ds))

    overall = analyze_group(problems, "overall")

    # D012 tiebreak comparison
    d012_tb = None
    if args.d012:
        d012_tb = load_d012_tiebreak(args.d012)
    else:
        results_dir = os.path.dirname(results_path)
        for candidate in ["tiebreak_analysis.json", "sica_d012_14b.json"]:
            cpath = os.path.join(results_dir, candidate)
            if os.path.exists(cpath):
                d012_tb = load_d012_tiebreak(cpath)
                if d012_tb:
                    break

    # Print markdown
    print_markdown(groups, overall, d012_tb)

    # Save JSON
    output_path = args.output
    if output_path is None:
        base = os.path.dirname(results_path)
        output_path = os.path.join(base or ".", "sica_expanded_14b", "analysis.json")
        # If input was a flat file in results/, save alongside it
        if not os.path.isdir(os.path.join(base, "sica_expanded_14b")):
            output_path = os.path.join(base or ".", "analysis_expanded.json")

    json_out = {
        "experiment": "exp-001_sica_expanded_14b",
        "source_file": results_path,
        "n_problems": n,
        "per_dataset": {g["label"]: g for g in groups},
        "overall": overall,
        "d012_tiebreak_comparison": d012_tb,
    }

    # Clean non-serializable and verbose fields
    for section in list(json_out["per_dataset"].values()) + [json_out["overall"]]:
        section.pop("tie_indices", None)

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(json_out, f, indent=2)
    print(f"\nDetailed results saved to {output_path}")


if __name__ == "__main__":
    main()

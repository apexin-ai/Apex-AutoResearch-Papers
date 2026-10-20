"""M1v2 profiling results analyzer: II summary, phase comparison, sparsity diagnostics."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np

from .alt_segmentation import fit_gmm_bic, segment_by_quantile


# ── Loading ──────────────────────────────────────────────────────────

def load_results(input_dir: str | Path) -> dict:
    path = Path(input_dir) / "profiling_results.json"
    if not path.exists():
        sys.exit(f"ERROR: {path} not found")
    with open(path) as f:
        return json.load(f)


# ── II Summary Table ─────────────────────────────────────────────────

def build_ii_table(data: dict) -> List[dict]:
    """Return flat list of {phase, level, mean, ci_low, ci_high, pass}."""
    ii = data["interaction_index"]
    pf = data.get("pass_fail", {})
    overall = pf.get("overall", "UNKNOWN")

    rows = []
    for phase, levels in sorted(ii.items()):
        for level, stats in sorted(levels.items()):
            ci_low = stats["ci_low"]
            ci_high = stats["ci_high"]
            ci_excludes_zero = (ci_low > 0) or (ci_high < 0)
            rows.append({
                "phase": phase,
                "level": level,
                "mean": stats["mean"],
                "ci_low": ci_low,
                "ci_high": ci_high,
                "ci_excludes_zero": ci_excludes_zero,
                "pass": ci_excludes_zero,
            })
    return rows


def print_ii_table(rows: List[dict]) -> None:
    header = f"{'Phase':<14} {'Level':>6} {'II Mean':>9} {'95% CI':>22} {'Pass':>6}"
    print("\n" + "=" * 65)
    print("Interaction Index Summary")
    print("=" * 65)
    print(header)
    print("-" * 65)
    for r in rows:
        ci_str = f"[{r['ci_low']:+.4f}, {r['ci_high']:+.4f}]"
        tag = "PASS" if r["pass"] else "FAIL"
        print(f"{r['phase']:<14} {r['level']:>6} {r['mean']:>+9.4f} {ci_str:>22} {tag:>6}")
    print("-" * 65)


# ── Phase Difference Test ────────────────────────────────────────────

def compare_phases(data: dict) -> List[dict]:
    """Compare II between every phase pair: CI non-overlap or sign reversal."""
    ii = data["interaction_index"]
    phases = sorted(ii.keys())
    results = []

    for level in sorted(next(iter(ii.values())).keys()):
        phase_stats = {p: ii[p][level] for p in phases if level in ii[p]}
        phase_list = sorted(phase_stats.keys())

        for i in range(len(phase_list)):
            for j in range(i + 1, len(phase_list)):
                p1, p2 = phase_list[i], phase_list[j]
                s1, s2 = phase_stats[p1], phase_stats[p2]

                ci_no_overlap = (s1["ci_low"] > s2["ci_high"]) or (s2["ci_low"] > s1["ci_high"])
                sign_reversal = (s1["mean"] > 0 and s2["mean"] < 0) or (s1["mean"] < 0 and s2["mean"] > 0)

                results.append({
                    "level": level,
                    "phase_a": p1,
                    "phase_b": p2,
                    "mean_a": s1["mean"],
                    "mean_b": s2["mean"],
                    "ci_no_overlap": ci_no_overlap,
                    "sign_reversal": sign_reversal,
                    "significant": ci_no_overlap or sign_reversal,
                })
    return results


def print_phase_comparisons(comparisons: List[dict]) -> None:
    print("\n" + "=" * 75)
    print("Phase Difference Tests")
    print("=" * 75)
    header = f"{'Level':>6} {'Phase A':<12} {'Phase B':<12} {'ΔII':>8} {'CI Sep':>7} {'Sign Rev':>9} {'Sig':>5}"
    print(header)
    print("-" * 75)
    for c in comparisons:
        delta = c["mean_a"] - c["mean_b"]
        sep = "YES" if c["ci_no_overlap"] else "no"
        rev = "YES" if c["sign_reversal"] else "no"
        sig = "***" if c["significant"] else ""
        print(f"{c['level']:>6} {c['phase_a']:<12} {c['phase_b']:<12} {delta:>+8.4f} {sep:>7} {rev:>9} {sig:>5}")
    print("-" * 75)


# ── Sparsity Distribution Analysis ──────────────────────────────────

def analyze_sparsity(data: dict) -> dict:
    """Run GMM+BIC and quantile segmentation on per-problem sparsity values."""
    diag = data.get("diagnostics", {})
    per_problem = diag.get("per_problem_sparsity", [])

    if not per_problem:
        return {"error": "no per_problem_sparsity in diagnostics"}

    all_sparsity = []
    for p in per_problem:
        vals = p.get("sparsity_values", [])
        all_sparsity.extend(vals)

    if not all_sparsity:
        return {"error": "empty sparsity values"}

    arr = np.array(all_sparsity, dtype=np.float64)

    gmm = fit_gmm_bic(arr, max_k=5)
    quant = segment_by_quantile(arr, n_groups=3)

    gmm_result = {
        "best_k": gmm.best_k,
        "bic_scores": {str(k): float(v) for k, v in gmm.bic_scores.items()},
        "means": [float(m) for m in gmm.means],
        "stds": [float(s) for s in gmm.stds],
        "weights": [float(w) for w in gmm.weights],
    }

    quant_result = {
        "n_groups": quant.n_groups,
        "boundaries": [float(b) for b in quant.boundaries],
        "group_names": quant.group_names,
        "group_stats": quant.group_stats,
    }

    # Compare: does GMM agree with KDE phase count from the run?
    n_phases_from_kde = []
    for p in per_problem:
        n_phases_from_kde.append(p.get("n_phases_detected", 0))

    kde_modal = max(set(n_phases_from_kde), key=n_phases_from_kde.count) if n_phases_from_kde else 0
    gmm_vs_kde_agree = gmm.best_k == kde_modal

    return {
        "n_problems": len(per_problem),
        "total_tokens": len(arr),
        "sparsity_global_mean": float(arr.mean()),
        "sparsity_global_std": float(arr.std()),
        "gmm": gmm_result,
        "quantile": quant_result,
        "kde_modal_n_phases": kde_modal,
        "gmm_kde_agree": gmm_vs_kde_agree,
    }


def print_sparsity_analysis(analysis: dict) -> None:
    print("\n" + "=" * 65)
    print("Sparsity Distribution Analysis")
    print("=" * 65)

    if "error" in analysis:
        print(f"  ERROR: {analysis['error']}")
        return

    print(f"  Problems: {analysis['n_problems']}, Tokens: {analysis['total_tokens']}")
    print(f"  Global sparsity: {analysis['sparsity_global_mean']:.4f} ± {analysis['sparsity_global_std']:.4f}")

    gmm = analysis["gmm"]
    print(f"\n  GMM+BIC: best_k = {gmm['best_k']}")
    for i, (m, s, w) in enumerate(zip(gmm["means"], gmm["stds"], gmm["weights"])):
        print(f"    Component {i}: mean={m:.4f}, std={s:.4f}, weight={w:.3f}")

    quant = analysis["quantile"]
    print(f"\n  Quantile segmentation ({quant['n_groups']} groups):")
    for gs in quant["group_stats"]:
        name = gs.get("name", gs.get("group", "?"))
        print(f"    {name}: mean={gs['mean']:.4f}, std={gs['std']:.4f}, n={gs['count']}, ratio={gs['ratio']:.3f}")

    agree = "YES" if analysis["gmm_kde_agree"] else "NO"
    print(f"\n  GMM k={gmm['best_k']} vs KDE modal phases={analysis['kde_modal_n_phases']}: agree={agree}")


# ── Overall Verdict ──────────────────────────────────────────────────

def compute_verdict(data: dict, phase_comparisons: List[dict]) -> dict:
    """MVP Pass = any phase pair with CI non-overlap OR sign reversal."""
    any_significant = any(c["significant"] for c in phase_comparisons)

    pf = data.get("pass_fail", {})
    original_verdict = pf.get("overall", "UNKNOWN")

    return {
        "mvp_pass": any_significant,
        "n_significant_pairs": sum(1 for c in phase_comparisons if c["significant"]),
        "n_total_pairs": len(phase_comparisons),
        "original_run_verdict": original_verdict,
        "ci_overlap_test": pf.get("ci_overlap_test", {}),
        "sign_reversal_test": pf.get("sign_reversal_test", {}),
    }


def print_verdict(verdict: dict) -> None:
    print("\n" + "=" * 65)
    tag = "PASS" if verdict["mvp_pass"] else "FAIL"
    print(f"MVP Verdict: {tag}")
    print("=" * 65)
    print(f"  Significant phase pairs: {verdict['n_significant_pairs']}/{verdict['n_total_pairs']}")
    print(f"  Original run verdict:    {verdict['original_run_verdict']}")
    if verdict.get("ci_overlap_test"):
        t = verdict["ci_overlap_test"]
        print(f"  CI overlap test:         {'PASS' if t.get('pass') else 'FAIL'} — {t.get('details', '')}")
    if verdict.get("sign_reversal_test"):
        t = verdict["sign_reversal_test"]
        print(f"  Sign reversal test:      {'PASS' if t.get('pass') else 'FAIL'} — {t.get('details', '')}")
    print()


# ── Main ─────────────────────────────────────────────────────────────

def run(input_dir: str | Path) -> dict:
    data = load_results(input_dir)

    ii_rows = build_ii_table(data)
    print_ii_table(ii_rows)

    comparisons = compare_phases(data)
    print_phase_comparisons(comparisons)

    sparsity_analysis = analyze_sparsity(data)
    print_sparsity_analysis(sparsity_analysis)

    verdict = compute_verdict(data, comparisons)
    print_verdict(verdict)

    summary = {
        "interaction_index_table": ii_rows,
        "phase_comparisons": comparisons,
        "sparsity_analysis": sparsity_analysis,
        "verdict": verdict,
        "config": data.get("config", {}),
        "warnings": data.get("warnings", []),
    }

    out_path = Path(input_dir) / "analysis_summary.json"
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"Saved: {out_path}")

    return summary


def main():
    parser = argparse.ArgumentParser(description="Analyze M1v2 profiling results")
    parser.add_argument("--input_dir", required=True, help="Path to profiling_output_v2/")
    args = parser.parse_args()
    run(args.input_dir)


if __name__ == "__main__":
    main()

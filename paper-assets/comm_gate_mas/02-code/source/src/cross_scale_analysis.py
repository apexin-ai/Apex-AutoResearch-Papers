#!/usr/bin/env python3
"""
Cross-scale oracle pruning analysis: reads all seed_42.json outputs,
generates summary table (CSV + LaTeX), and cross-checks against Table 1.

Usage:
    python src/cross_scale_analysis.py
    python src/cross_scale_analysis.py --include-72b   # after 72B completes
    python src/cross_scale_analysis.py --verify-table1  # diff against paper Table 1
"""

import argparse
import csv
import json
import math
import os
import re
import statistics
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUTS = PROJECT_ROOT / "outputs"


@dataclass
class OracleResult:
    label: str
    backbone: str
    scale: str
    dataset: str
    temperature: str
    n_tasks: int
    n_skipped: int
    baseline_acc: float
    pruned_acc: float
    delta_pp: float
    ci_lo: float
    ci_hi: float
    p_value: float
    suppression_rate: float
    source: str
    is_aggregate: bool = False


def paired_ci(b: int, c: int, n: int, z: float = 1.96):
    """Wald 95% CI for paired proportion difference from McNemar cells."""
    delta = (b - c) / n
    if b + c == 0:
        return 0.0, 0.0
    se = math.sqrt((b + c - (b - c) ** 2 / n)) / n
    return (delta - z * se) * 100, (delta + z * se) * 100


def load_single_seed(path: str, label: str, backbone: str, scale: str,
                     dataset: str, temperature: str = "0") -> OracleResult:
    """Load a single-seed oracle result JSON."""
    data = json.loads(Path(path).read_text())
    n = data["num_tasks"]
    skip = data.get("num_skipped", 0)
    # Use baseline.total as denominator (includes skipped tasks counted as wrong)
    n_denom = data["baseline"]["total"]

    bl_correct = data["baseline"]["correct"]
    pr_correct = data["oracle_pruned"]["correct"]
    bl_acc = bl_correct / n_denom * 100
    pr_acc = pr_correct / n_denom * 100
    delta = pr_acc - bl_acc

    b = data["mcnemar"]["b_oracle_only"]
    c = data["mcnemar"]["c_baseline_only"]
    ci_lo, ci_hi = paired_ci(b, c, n_denom)

    return OracleResult(
        label=label, backbone=backbone, scale=scale, dataset=dataset,
        temperature=temperature, n_tasks=n_denom, n_skipped=skip,
        baseline_acc=bl_acc, pruned_acc=pr_acc, delta_pp=delta,
        ci_lo=ci_lo, ci_hi=ci_hi,
        p_value=data["mcnemar"]["p_value"],
        suppression_rate=data["oracle_pruned"]["suppression_rate"],
        source=str(path),
    )


def load_multiseed(seed_dir: str, label: str, backbone: str, scale: str,
                   dataset: str, temperature: str = "0") -> OracleResult:
    """Compute aggregate from multiple seed files."""
    seed_files = sorted(Path(seed_dir).glob("seed_*.json"))
    deltas = []
    supps = []
    total_bl = 0
    total_pr = 0
    total_n = 0

    for f in seed_files:
        d = json.loads(f.read_text())
        n = d["num_tasks"] - d.get("num_skipped", 0)
        bl = d["baseline"]["correct"] / n * 100
        pr = d["oracle_pruned"]["correct"] / n * 100
        deltas.append(pr - bl)
        supps.append(d["oracle_pruned"]["suppression_rate"])
        total_bl += d["baseline"]["correct"]
        total_pr += d["oracle_pruned"]["correct"]
        total_n += n

    mean_d = statistics.mean(deltas)
    sd_d = statistics.stdev(deltas) if len(deltas) > 1 else 0
    se_d = sd_d / math.sqrt(len(deltas))
    ci_lo = mean_d - 1.96 * se_d
    ci_hi = mean_d + 1.96 * se_d

    # TOST at ±1pp
    from scipy.stats import t as t_dist
    n_seeds = len(deltas)
    if se_d > 0:
        t_upper = (mean_d - 1.0) / se_d
        t_lower = (mean_d + 1.0) / se_d
        p_upper = t_dist.cdf(t_upper, df=n_seeds - 1)
        p_lower = 1.0 - t_dist.cdf(t_lower, df=n_seeds - 1)
        tost_p = max(p_upper, p_lower)
    else:
        tost_p = 0.0

    return OracleResult(
        label=label, backbone=backbone, scale=scale, dataset=dataset,
        temperature=temperature,
        n_tasks=total_n, n_skipped=0,
        baseline_acc=total_bl / total_n * 100,
        pruned_acc=total_pr / total_n * 100,
        delta_pp=mean_d,
        ci_lo=ci_lo, ci_hi=ci_hi,
        p_value=tost_p,
        suppression_rate=statistics.mean(supps),
        source=str(seed_dir),
        is_aggregate=True,
    )


def discover_results(include_72b: bool = False) -> list[OracleResult]:
    """Auto-discover all oracle experiment outputs."""
    results = []

    configs = [
        ("Qwen / GSM8K", "Qwen", "7B", "GSM8K", "0",
         OUTPUTS / "oracle_qwen_n500_fixed" / "result.json"),
        ("Llama / GSM8K", "Llama", "8B", "GSM8K", "0",
         OUTPUTS / "oracle_5class_llama_gsm8k.json"),
        ("Qwen / GSM8K (t=0.7)", "Qwen", "7B", "GSM8K", "0.7",
         OUTPUTS / "oracle_qwen_gsm8k_t07" / "seed_42.json"),
        ("Llama / GSM8K (t=0.7, seed2)", "Llama", "8B", "GSM8K", "0.7",
         OUTPUTS / "oracle_llama_t07_ext" / "results.json"),
        ("Qwen / StratQA", "Qwen", "7B", "StratQA", "0",
         OUTPUTS / "oracle_qwen_stratqa" / "results.json"),
        ("Llama / StratQA", "Llama", "8B", "StratQA", "0",
         OUTPUTS / "oracle_llama_stratqa" / "seed_42.json"),
    ]

    for label, bb, scale, ds, temp, path in configs:
        if path.exists():
            results.append(load_single_seed(str(path), label, bb, scale, ds, temp))
        else:
            print(f"WARNING: missing {path}", file=sys.stderr)

    # 10-seed aggregates
    qwen_10run = OUTPUTS / "oracle_qwen_10run"
    if qwen_10run.exists():
        results.append(load_multiseed(str(qwen_10run), "Qwen / GSM8K (10 seeds)",
                                      "Qwen", "7B", "GSM8K"))
    llama_10run = OUTPUTS / "oracle_llama_10run"
    if llama_10run.exists():
        results.append(load_multiseed(str(llama_10run), "Llama / GSM8K (10 seeds)",
                                      "Llama", "8B", "GSM8K"))

    # 72B
    path_72b = OUTPUTS / "oracle_qwen72b_n500" / "seed_42.json"
    if include_72b and path_72b.exists():
        results.append(load_single_seed(str(path_72b), "Qwen / GSM8K (72B)",
                                        "Qwen", "72B", "GSM8K"))
    elif include_72b:
        print(f"WARNING: --include-72b but {path_72b} not found", file=sys.stderr)

    return results


# --- Table 1 cross-check ---

TABLE1_EXPECTED = {
    "Qwen / GSM8K": {"baseline": 88.8, "pruned": 89.6, "delta": 0.8, "p": 0.34, "supp": 56.3},
    "Llama / GSM8K": {"baseline": 82.2, "pruned": 81.6, "delta": -0.6, "p": 0.71, "supp": 36.6},
    "Qwen / GSM8K (t=0.7)": {"baseline": 87.4, "pruned": 88.0, "delta": 0.6, "p": 0.710, "supp": 53.1},
    "Qwen / StratQA": {"baseline": 73.2, "pruned": 73.4, "delta": 0.2, "p": 1.00, "supp": 65.6},
    "Llama / StratQA": {"baseline": 68.9, "pruned": 73.9, "delta": 5.0, "p": 0.18, "supp": 21.5},
}


def verify_table1(results: list[OracleResult]) -> list[str]:
    """Cross-check computed values against Table 1 in the paper."""
    issues = []
    for r in results:
        if r.label not in TABLE1_EXPECTED:
            continue
        expected = TABLE1_EXPECTED[r.label]
        checks = [
            ("baseline", r.baseline_acc, expected["baseline"], 0.15),
            ("pruned", r.pruned_acc, expected["pruned"], 0.15),
            ("delta", r.delta_pp, expected["delta"], 0.15),
            ("p", r.p_value, expected["p"], 0.015),
            ("supp", r.suppression_rate, expected["supp"], 0.5),
        ]
        for name, actual, exp, tol in checks:
            if abs(actual - exp) > tol:
                issues.append(
                    f"MISMATCH [{r.label}] {name}: "
                    f"computed={actual:.2f}, Table1={exp}, diff={actual-exp:+.2f}"
                )
    return issues


def to_csv(results: list[OracleResult], path: Path):
    """Write results to CSV."""
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Label", "Backbone", "Scale", "Dataset", "Temp", "N",
                     "Skipped", "Baseline%", "Pruned%", "Delta_pp",
                     "CI_lo", "CI_hi", "p_value", "Supp%", "Aggregate", "Source"])
        for r in results:
            w.writerow([r.label, r.backbone, r.scale, r.dataset, r.temperature,
                        r.n_tasks, r.n_skipped,
                        f"{r.baseline_acc:.1f}", f"{r.pruned_acc:.1f}",
                        f"{r.delta_pp:+.1f}", f"{r.ci_lo:+.1f}", f"{r.ci_hi:+.1f}",
                        f"{r.p_value:.4f}", f"{r.suppression_rate:.1f}",
                        r.is_aggregate, r.source])
    print(f"CSV written to {path}")


def to_latex(results: list[OracleResult]) -> str:
    """Generate LaTeX table rows."""
    lines = [
        r"\begin{tabular}{lcccccc}",
        r"\toprule",
        r"\textbf{Setting} & $N$ & \textbf{Baseline} & \textbf{Pruned} "
        r"& $\Delta$ & $p$ & \textbf{Supp.} \\",
        r"\midrule",
    ]
    for r in results:
        sign = "+" if r.delta_pp >= 0 else ""
        if r.is_aggregate:
            lines.append(
                f"{r.label} & {r.n_tasks:,} & "
                f"\\multicolumn{{2}}{{c}}{{$\\Delta = {sign}{r.delta_pp:.1f}$\\,pp}} & "
                f"& {r.p_value:.3f} & {r.suppression_rate:.1f}\\% \\\\"
            )
        else:
            lines.append(
                f"{r.label} & {r.n_tasks} & {r.baseline_acc:.1f} & "
                f"{r.pruned_acc:.1f} ({sign}{r.delta_pp:.1f}) & "
                f"[{r.ci_lo:+.1f}, {r.ci_hi:+.1f}] & "
                f"{r.p_value:.3f} & {r.suppression_rate:.1f}\\% \\\\"
            )
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Cross-scale oracle pruning analysis")
    parser.add_argument("--include-72b", action="store_true")
    parser.add_argument("--verify-table1", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=OUTPUTS / "cross_scale")
    args = parser.parse_args()

    results = discover_results(include_72b=args.include_72b)

    print(f"\n{'='*70}")
    print(f"  Cross-Scale Oracle Pruning Summary ({len(results)} configurations)")
    print(f"{'='*70}\n")

    header = f"{'Label':<35} {'N':>5} {'Base%':>6} {'Prune%':>7} {'Δpp':>6} {'p':>7} {'Supp%':>6}"
    print(header)
    print("-" * len(header))
    for r in results:
        sign = "+" if r.delta_pp >= 0 else ""
        print(f"{r.label:<35} {r.n_tasks:>5} {r.baseline_acc:>6.1f} {r.pruned_acc:>7.1f} "
              f"{sign}{r.delta_pp:>5.1f} {r.p_value:>7.4f} {r.suppression_rate:>6.1f}")

    # Table 1 verification
    if args.verify_table1:
        print(f"\n{'='*70}")
        print("  Table 1 Cross-Check")
        print(f"{'='*70}")
        issues = verify_table1(results)
        if issues:
            for i in issues:
                print(f"  ✗ {i}")
            print(f"\n  {len(issues)} mismatches found!")
        else:
            print("  ✓ All values match Table 1 within tolerance.")

    # Output
    args.output_dir.mkdir(parents=True, exist_ok=True)
    to_csv(results, args.output_dir / "cross_scale_summary.csv")

    latex_path = args.output_dir / "cross_scale_table.tex"
    latex_path.write_text(to_latex(results))
    print(f"LaTeX written to {latex_path}")

    # Print LaTeX
    print(f"\n{'='*70}")
    print("  LaTeX Table")
    print(f"{'='*70}")
    print(to_latex(results))


if __name__ == "__main__":
    main()

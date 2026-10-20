#!/usr/bin/env python3
"""
统一评估脚本 — 所有 benchmark 通用。
使用 per-sample 定义计算 C1-C5。

指标定义（per-sample）：
  C1 disagree_rate     = (FOL judgment ≠ Code judgment) / N
  C2 diagnostic_rate   = (至少一方正确) / n_disagree
  C3 error_types       = 不同错误类型数量
  C4 targeted_delta    = targeted正确率 - blind正确率（在disagreement样本上）
  C5 localization:
    c5_committed: 跳过 ambiguous（与 evaluate_mvp.py 对齐）
    c5_coverage: ambiguous 视为预测失败

用法：
    python3 src/evaluate_unified.py <input_file> [--output <output_file>]
"""

import json
import sys
import argparse
import numpy as np
from collections import Counter
from scipy.stats import fisher_exact


def load_results(path):
    with open(path) as f:
        first = f.read(1)
        if not first:
            return []
        f.seek(0)
        if first == "[":
            return json.load(f)
        return [json.loads(line) for line in f if line.strip()]


def is_disagreement(s):
    return s["disagreement"]["agreement_type"] in ("disagree", "single_error")


def repair_success_per_sample(s, method):
    """Per-sample: any round of fol_{method} or code_{method} succeeded."""
    rep = s.get("repair", {})
    rounds = rep.get(f"fol_{method}", []) + rep.get(f"code_{method}", [])
    if not rounds:
        return None
    return any(r.get("success", False) for r in rounds)


def _c5_from_diagnostic(diagnostic):
    """Dual C5: committed (skip ambiguous) + coverage (ambiguous=fail)."""
    c5_com_correct = c5_com_total = 0
    c5_cov_correct = c5_cov_total = c5_ambiguous = 0
    for s in diagnostic:
        dis = s["disagreement"]
        predicted = s.get("stability", {}).get("predicted_error_side")
        if not predicted:
            continue
        fol_c = dis.get("fol_correct")
        code_c = dis.get("code_correct")
        if fol_c and not code_c:
            actual = "code"
        elif code_c and not fol_c:
            actual = "fol"
        else:
            continue
        c5_cov_total += 1
        if predicted == "ambiguous":
            c5_ambiguous += 1
            continue
        c5_com_total += 1
        if predicted == actual:
            c5_com_correct += 1
            c5_cov_correct += 1
    return c5_com_correct, c5_com_total, c5_cov_correct, c5_cov_total, c5_ambiguous


def compute_metrics(samples):
    N = len(samples)
    if N == 0:
        return None

    # --- C1: disagree_rate = FOL≠Code / N ---
    disagree = [s for s in samples if is_disagreement(s)]
    n_disagree = len(disagree)
    c1 = n_disagree / N

    # --- C2: diagnostic_rate = at_least_one_correct / n_disagree ---
    diagnostic = []
    for s in disagree:
        dis = s["disagreement"]
        if dis.get("fol_correct") or dis.get("code_correct"):
            diagnostic.append(s)
    n_diagnostic = len(diagnostic)
    c2 = n_diagnostic / n_disagree if n_disagree > 0 else 0.0

    # --- C3: distinct error types ---
    error_types = set()
    for s in disagree:
        et = s["disagreement"].get("error_type")
        if et:
            error_types.add(et)
    c3 = len(error_types)

    # --- C4: per-sample targeted_rate - blind_rate on disagreement samples ---
    tgt_ok = bld_ok = n_with_repair = 0
    for s in disagree:
        t = repair_success_per_sample(s, "targeted")
        b = repair_success_per_sample(s, "blind")
        if t is not None:
            n_with_repair += 1
            if t:
                tgt_ok += 1
            if b:
                bld_ok += 1
    tgt_rate = tgt_ok / n_with_repair if n_with_repair else 0.0
    bld_rate = bld_ok / n_with_repair if n_with_repair else 0.0
    c4 = tgt_rate - bld_rate

    # --- C5: error_side accuracy (dual: committed + coverage) ---
    c5_com_correct, c5_com_total, c5_cov_correct, c5_cov_total, c5_ambiguous = \
        _c5_from_diagnostic(diagnostic)
    c5_committed = c5_com_correct / c5_com_total if c5_com_total > 0 else 0.0
    c5_coverage = c5_cov_correct / c5_cov_total if c5_cov_total > 0 else 0.0
    ambiguous_rate = c5_ambiguous / c5_cov_total if c5_cov_total > 0 else 0.0

    return {
        "N": N,
        "n_disagree": n_disagree,
        "n_diagnostic": n_diagnostic,
        "n_with_repair": n_with_repair,
        "C1_disagree_rate": round(c1, 4),
        "C2_diagnostic_rate": round(c2, 4),
        "C3_error_types": c3,
        "C3_types_list": sorted(error_types),
        "C4_targeted_delta": round(c4, 4),
        "C4_targeted_rate": round(tgt_rate, 4),
        "C4_blind_rate": round(bld_rate, 4),
        "C4_targeted_ok": tgt_ok,
        "C4_blind_ok": bld_ok,
        "C5_committed": round(c5_committed, 4),
        "C5_committed_correct": c5_com_correct,
        "C5_committed_total": c5_com_total,
        "C5_coverage": round(c5_coverage, 4),
        "C5_coverage_correct": c5_cov_correct,
        "C5_coverage_total": c5_cov_total,
        "C5_ambiguous": c5_ambiguous,
        "C5_ambiguous_rate": round(ambiguous_rate, 4),
    }


def bootstrap_ci(samples, n_boot=10000, seed=42):
    rng = np.random.RandomState(seed)
    N = len(samples)
    if N == 0:
        return {}

    c1s, c2s, c4s, c5_com_s, c5_cov_s = [], [], [], [], []

    for _ in range(n_boot):
        idx = rng.randint(0, N, size=N)
        boot = [samples[i] for i in idx]

        disagree = [s for s in boot if is_disagreement(s)]
        nd = len(disagree)
        c1s.append(nd / N)

        if nd > 0:
            diag = sum(
                1 for s in disagree
                if s["disagreement"].get("fol_correct") or s["disagreement"].get("code_correct")
            )
            c2s.append(diag / nd)
        else:
            c2s.append(np.nan)

        tgt_ok = bld_ok = n_rep = 0
        for s in disagree:
            t = repair_success_per_sample(s, "targeted")
            b = repair_success_per_sample(s, "blind")
            if t is not None:
                n_rep += 1
                if t:
                    tgt_ok += 1
                if b:
                    bld_ok += 1
        if n_rep > 0:
            c4s.append(tgt_ok / n_rep - bld_ok / n_rep)
        else:
            c4s.append(np.nan)

        diagnostic = [
            s for s in disagree
            if s["disagreement"].get("fol_correct") or s["disagreement"].get("code_correct")
        ]
        c5_com_ok, c5_com_t, c5_cov_ok, c5_cov_t, _ = _c5_from_diagnostic(diagnostic)
        c5_com_s.append(c5_com_ok / c5_com_t if c5_com_t > 0 else np.nan)
        c5_cov_s.append(c5_cov_ok / c5_cov_t if c5_cov_t > 0 else np.nan)

    def ci(arr):
        arr = np.array(arr, dtype=float)
        valid = arr[~np.isnan(arr)]
        if len(valid) == 0:
            return {"mean": None, "ci_lower": None, "ci_upper": None}
        return {
            "mean": round(float(np.mean(valid)), 4),
            "ci_lower": round(float(np.percentile(valid, 2.5)), 4),
            "ci_upper": round(float(np.percentile(valid, 97.5)), 4),
        }

    return {
        "C1_disagree_rate": ci(c1s),
        "C2_diagnostic_rate": ci(c2s),
        "C4_targeted_delta": ci(c4s),
        "C5_committed": ci(c5_com_s),
        "C5_coverage": ci(c5_cov_s),
    }


def fisher_c4(samples):
    disagree = [s for s in samples if is_disagreement(s)]
    tgt_ok = bld_ok = n_rep = 0
    for s in disagree:
        t = repair_success_per_sample(s, "targeted")
        b = repair_success_per_sample(s, "blind")
        if t is not None:
            n_rep += 1
            if t:
                tgt_ok += 1
            if b:
                bld_ok += 1
    if n_rep == 0:
        return {"error": "no repair data"}
    tgt_fail = n_rep - tgt_ok
    bld_fail = n_rep - bld_ok
    table = [[tgt_ok, tgt_fail], [bld_ok, bld_fail]]
    odds, p = fisher_exact(table)
    return {
        "table": {
            "targeted": {"correct": tgt_ok, "incorrect": tgt_fail},
            "blind": {"correct": bld_ok, "incorrect": bld_fail},
        },
        "odds_ratio": round(float(odds), 4),
        "p_value": round(float(p), 6),
    }


def gt_subset_metrics(samples):
    groups = {}
    for s in samples:
        gt = s.get("ground_truth", "N/A")
        groups.setdefault(gt, []).append(s)
    return {gt: compute_metrics(subset) for gt, subset in sorted(groups.items())}


def format_output(results):
    lines = []
    lines.append("=" * 72)
    lines.append("UNIFIED EVALUATION (per-sample definitions)")
    lines.append("=" * 72)

    for mode in ("all", "excl_unknown"):
        m = results["overall"][mode]
        if m is None:
            continue
        label = "All samples" if mode == "all" else "Excl GT=Unknown"
        lines.append(f"\n--- {label} (N={m['N']}) ---")
        lines.append(f"  C1 disagree_rate:    {m['C1_disagree_rate']:.4f}  ({m['n_disagree']}/{m['N']})")
        lines.append(f"  C2 diagnostic_rate:  {m['C2_diagnostic_rate']:.4f}  ({m['n_diagnostic']}/{m['n_disagree']})")
        lines.append(f"  C3 error_types:      {m['C3_error_types']} types  {m['C3_types_list']}")
        lines.append(
            f"  C4 targeted_delta:   {m['C4_targeted_delta']:+.4f}  "
            f"(T={m['C4_targeted_rate']:.4f} [{m['C4_targeted_ok']}/{m['n_with_repair']}]  "
            f"B={m['C4_blind_rate']:.4f} [{m['C4_blind_ok']}/{m['n_with_repair']}])"
        )
        lines.append(f"  C5 localization:")
        lines.append(
            f"    c5_committed:     {m['C5_committed']:.4f}  "
            f"({m['C5_committed_correct']}/{m['C5_committed_total']}) [skips ambiguous]"
        )
        lines.append(
            f"    c5_coverage:      {m['C5_coverage']:.4f}  "
            f"({m['C5_coverage_correct']}/{m['C5_coverage_total']}) [ambiguous=fail]"
        )
        lines.append(
            f"    ambiguous_rate:   {m['C5_ambiguous_rate']:.4f}  "
            f"({m['C5_ambiguous']}/{m['C5_coverage_total']})"
        )

    lines.append(f"\n--- GT Subsets ---")
    for gt, m in results["gt_subsets"].items():
        if m is None:
            continue
        lines.append(f"\n  GT={gt} (N={m['N']})")
        lines.append(f"    C1={m['C1_disagree_rate']:.4f}  C2={m['C2_diagnostic_rate']:.4f}  "
                      f"C3={m['C3_error_types']}  C4={m['C4_targeted_delta']:+.4f}  "
                      f"C5c={m['C5_committed']:.4f}  C5v={m['C5_coverage']:.4f}")

    lines.append(f"\n--- Bootstrap 95% CI (N=10000) ---")
    for mode in ("all", "excl_unknown"):
        label = "All" if mode == "all" else "Excl-Unknown"
        lines.append(f"\n  [{label}]")
        for metric, ci in results["bootstrap"][mode].items():
            if ci["mean"] is not None:
                lines.append(f"    {metric:25s}  {ci['mean']:.4f}  [{ci['ci_lower']:.4f}, {ci['ci_upper']:.4f}]")
            else:
                lines.append(f"    {metric:25s}  N/A")

    lines.append(f"\n--- Fisher Exact Test (C4) ---")
    for mode in ("all", "excl_unknown"):
        label = "All" if mode == "all" else "Excl-Unknown"
        lines.append(f"\n  [{label}]")
        f = results["fisher_c4"][mode]
        if "error" in f:
            lines.append(f"    {f['error']}")
        else:
            t = f["table"]
            lines.append(f"    Targeted: {t['targeted']['correct']} ok / {t['targeted']['incorrect']} fail")
            lines.append(f"    Blind:    {t['blind']['correct']} ok / {t['blind']['incorrect']} fail")
            lines.append(f"    OR={f['odds_ratio']:.4f}  p={f['p_value']:.6f}")

    lines.append("\n" + "=" * 72)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Unified evaluation (per-sample C1-C5)")
    parser.add_argument("input", help="JSON or JSONL results file")
    parser.add_argument("--output", "-o", help="Output JSON path")
    args = parser.parse_args()

    data = load_results(args.input)
    print(f"Loaded {len(data)} samples from {args.input}")

    all_samples = data
    excl_unknown = [s for s in data if s.get("ground_truth") != "Unknown"]

    results = {}
    results["overall"] = {
        "all": compute_metrics(all_samples),
        "excl_unknown": compute_metrics(excl_unknown),
    }
    results["gt_subsets"] = gt_subset_metrics(all_samples)

    print("Running bootstrap (N=10000)...")
    results["bootstrap"] = {
        "all": bootstrap_ci(all_samples),
        "excl_unknown": bootstrap_ci(excl_unknown),
    }

    results["fisher_c4"] = {
        "all": fisher_c4(all_samples),
        "excl_unknown": fisher_c4(excl_unknown),
    }

    txt = format_output(results)
    print(txt)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\nJSON saved to {args.output}")


if __name__ == "__main__":
    main()

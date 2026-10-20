"""Supplement analyses (e) Phi Coefficient and (f) Cost-Effectiveness for exp-001."""
import json
import math
import sys
from collections import Counter

DATA_PATH = "results/mvp_v4_repair_fixed.json"
OUT_JSON = "results/exp001_supplement_ef.json"
OUT_TXT = "results/exp001_supplement_ef.txt"


def load_data(path):
    with open(path) as f:
        return json.load(f)


def phi_coefficient(n11, n10, n01, n00):
    num = n11 * n00 - n10 * n01
    denom = math.sqrt((n11 + n10) * (n01 + n00) * (n11 + n01) * (n10 + n00))
    if denom == 0:
        return float("nan")
    return num / denom


def chi_squared_2x2(n11, n10, n01, n00):
    n = n11 + n10 + n01 + n00
    if n == 0:
        return float("nan"), float("nan")
    expected = [
        [(n11 + n10) * (n11 + n01) / n, (n11 + n10) * (n10 + n00) / n],
        [(n01 + n00) * (n11 + n01) / n, (n01 + n00) * (n10 + n00) / n],
    ]
    observed = [[n11, n10], [n01, n00]]
    chi2 = 0
    for i in range(2):
        for j in range(2):
            if expected[i][j] > 0:
                chi2 += (observed[i][j] - expected[i][j]) ** 2 / expected[i][j]
    # p-value from chi2 with df=1 using survival function approximation
    try:
        from scipy.stats import chi2 as chi2_dist
        p = chi2_dist.sf(chi2, df=1)
    except ImportError:
        p = _chi2_sf_approx(chi2)
    return chi2, p


def _chi2_sf_approx(x):
    """Rough upper-tail p-value for chi2(df=1) without scipy."""
    if x <= 0:
        return 1.0
    z = math.sqrt(x)
    t = 1.0 / (1.0 + 0.2316419 * z)
    d = 0.3989422804014327 * math.exp(-x / 2)
    p = d * t * (0.319381530 + t * (-0.356563782 + t * (1.781477937 + t * (-1.821255978 + t * 1.330274429))))
    return 2 * p  # two-tail -> but chi2 is one-tail; this is approximate


def compute_phi_table(data, subset_name="all"):
    """Build 2x2 table: FOL correct/wrong × Code correct/wrong."""
    # n11 = both correct, n10 = FOL correct & Code wrong
    # n01 = FOL wrong & Code correct, n00 = both wrong
    n11 = n10 = n01 = n00 = 0
    for d in data:
        dis = d["disagreement"]
        fc = dis["fol_correct"]
        cc = dis["code_correct"]
        if fc and cc:
            n11 += 1
        elif fc and not cc:
            n10 += 1
        elif not fc and cc:
            n01 += 1
        else:
            n00 += 1

    n = len(data)
    phi = phi_coefficient(n11, n10, n01, n00)
    chi2, p = chi_squared_2x2(n11, n10, n01, n00)

    return {
        "subset": subset_name,
        "n": n,
        "contingency_table": {
            "both_correct": n11,
            "fol_only_correct": n10,
            "code_only_correct": n01,
            "both_wrong": n00,
        },
        "phi": round(phi, 4) if not math.isnan(phi) else None,
        "chi2": round(chi2, 4) if not math.isnan(chi2) else None,
        "p_value": p if not math.isnan(p) else None,
    }


def analysis_e(data):
    """(e) Phi coefficient: FOL/Code failure correlation."""
    results = []
    results.append(compute_phi_table(data, "all"))

    gt_groups = {}
    for d in data:
        gt = d["ground_truth"]
        gt_groups.setdefault(gt, []).append(d)

    for gt_label in ["True", "False", "Unknown"]:
        if gt_label in gt_groups:
            results.append(compute_phi_table(gt_groups[gt_label], f"GT={gt_label}"))

    return results


def get_repair_success(d):
    """Check if any repair method succeeded for a sample."""
    r = d.get("repair", {})
    if not r:
        return False
    for method in ["code_targeted", "code_blind"]:
        if method in r:
            for rd in r[method]:
                if rd.get("success"):
                    return True
    return False


def analysis_f(data):
    """(f) Cost-effectiveness analysis."""
    n = len(data)

    # Total pipeline tokens
    total_input = sum(d["api_usage"]["input_tokens"] for d in data)
    total_output = sum(d["api_usage"]["output_tokens"] for d in data)
    total_tokens = total_input + total_output
    total_calls = sum(d["api_usage"]["calls"] for d in data)

    # Split by repair status
    no_repair = [d for d in data if not d.get("repair") or len(d["repair"]) == 0]
    has_repair = [d for d in data if d.get("repair") and len(d["repair"]) > 0]

    # Base cost (FOL + Code generation, no repair)
    # No-repair samples always have calls=2 (1 FOL + 1 Code)
    base_tokens_per_sample = sum(
        d["api_usage"]["input_tokens"] + d["api_usage"]["output_tokens"]
        for d in no_repair
    ) / len(no_repair)

    # Single-representation cost estimate: half of base (one path only)
    single_rep_tokens_per_sample = base_tokens_per_sample / 2

    # Repair-only token cost
    repair_tokens = sum(
        d["api_usage"]["input_tokens"] + d["api_usage"]["output_tokens"]
        for d in has_repair
    )
    repair_extra_tokens = repair_tokens - len(has_repair) * base_tokens_per_sample

    # Accuracy metrics
    code_correct = sum(1 for d in data if d["disagreement"]["code_correct"])
    fol_correct = sum(1 for d in data if d["disagreement"]["fol_correct"])
    oracle_correct = sum(1 for d in data if d["disagreement"]["fol_correct"] or d["disagreement"]["code_correct"])

    # Post-repair accuracy
    post_repair_correct = 0
    for d in data:
        dis = d["disagreement"]
        if not d.get("repair") or len(d["repair"]) == 0:
            # No disagreement → used agreed answer
            # agree_correct: both right → correct
            # agree_wrong: both wrong → incorrect
            if dis["agreement_type"] == "agree_correct":
                post_repair_correct += 1
        else:
            # Had disagreement → repair attempted
            if get_repair_success(d):
                post_repair_correct += 1
            elif dis["fol_correct"]:
                # Repair failed, but FOL was correct; system could fall back to FOL
                # (conservative: don't count these)
                pass

    # Also compute "repair + FOL fallback" accuracy
    repair_with_fallback = 0
    for d in data:
        dis = d["disagreement"]
        if not d.get("repair") or len(d["repair"]) == 0:
            if dis["agreement_type"] == "agree_correct":
                repair_with_fallback += 1
        else:
            if get_repair_success(d):
                repair_with_fallback += 1
            elif dis["fol_correct"]:
                repair_with_fallback += 1

    # Cost multipliers
    dual_rep_total = total_tokens
    single_rep_total = single_rep_tokens_per_sample * n

    cost_multiplier_dual_vs_single = dual_rep_total / single_rep_total
    cost_multiplier_base_only = base_tokens_per_sample / single_rep_tokens_per_sample  # should be ~2.0

    # Accuracy gains
    code_acc = code_correct / n
    fol_acc = fol_correct / n
    oracle_acc = oracle_correct / n
    repair_acc = post_repair_correct / n
    repair_fallback_acc = repair_with_fallback / n

    # Marginal cost-effectiveness: accuracy gain per unit cost increase
    if cost_multiplier_dual_vs_single > 1:
        gain_per_cost_repair = (repair_acc - code_acc) / (cost_multiplier_dual_vs_single - 1)
        gain_per_cost_repair_fb = (repair_fallback_acc - code_acc) / (cost_multiplier_dual_vs_single - 1)
    else:
        gain_per_cost_repair = float("inf")
        gain_per_cost_repair_fb = float("inf")

    return {
        "total_samples": n,
        "token_summary": {
            "total_input_tokens": total_input,
            "total_output_tokens": total_output,
            "total_tokens": total_tokens,
            "total_api_calls": total_calls,
            "avg_tokens_per_sample": round(total_tokens / n),
            "avg_calls_per_sample": round(total_calls / n, 1),
        },
        "cost_breakdown": {
            "single_rep_tokens_per_sample": round(single_rep_tokens_per_sample),
            "dual_rep_base_tokens_per_sample": round(base_tokens_per_sample),
            "repair_extra_tokens_total": round(repair_extra_tokens),
            "repair_extra_tokens_per_repair_sample": round(repair_extra_tokens / len(has_repair)) if has_repair else 0,
            "no_repair_samples": len(no_repair),
            "repair_samples": len(has_repair),
        },
        "cost_multipliers": {
            "dual_base_vs_single": round(cost_multiplier_base_only, 2),
            "full_pipeline_vs_single": round(cost_multiplier_dual_vs_single, 2),
        },
        "accuracy": {
            "code_only": round(code_acc, 4),
            "fol_only": round(fol_acc, 4),
            "oracle_upper_bound": round(oracle_acc, 4),
            "pipeline_repair": round(repair_acc, 4),
            "pipeline_repair_fol_fallback": round(repair_fallback_acc, 4),
        },
        "cost_effectiveness": {
            "accuracy_gain_repair_vs_code": round(repair_acc - code_acc, 4),
            "accuracy_gain_repair_fb_vs_code": round(repair_fallback_acc - code_acc, 4),
            "gain_per_unit_cost_repair": round(gain_per_cost_repair, 4),
            "gain_per_unit_cost_repair_fb": round(gain_per_cost_repair_fb, 4),
        },
    }


def format_phi_table(phi_results):
    lines = []
    lines.append("=" * 70)
    lines.append("(e) FOL/Code Failure Correlation — Phi Coefficient")
    lines.append("=" * 70)
    lines.append("")
    lines.append(f"{'Subset':<15} {'N':>5} {'Both✓':>7} {'FOL✓':>7} {'Code✓':>7} {'Both✗':>7} {'φ':>8} {'χ²':>8} {'p':>10}")
    lines.append("-" * 70)
    for r in phi_results:
        ct = r["contingency_table"]
        phi_str = f"{r['phi']:.3f}" if r["phi"] is not None else "N/A"
        chi2_str = f"{r['chi2']:.2f}" if r["chi2"] is not None else "N/A"
        p_str = f"{r['p_value']:.2e}" if r["p_value"] is not None else "N/A"
        lines.append(
            f"{r['subset']:<15} {r['n']:>5} {ct['both_correct']:>7} {ct['fol_only_correct']:>7} "
            f"{ct['code_only_correct']:>7} {ct['both_wrong']:>7} {phi_str:>8} {chi2_str:>8} {p_str:>10}"
        )
    lines.append("")

    # Interpretation
    overall = phi_results[0]
    phi_val = overall["phi"]
    if phi_val is not None:
        if abs(phi_val) < 0.1:
            interp = "negligible correlation — failures are largely independent, supporting complementarity"
        elif abs(phi_val) < 0.3:
            interp = "weak correlation — moderate independence between failure modes"
        elif abs(phi_val) < 0.5:
            interp = "moderate correlation — some shared failure causes"
        else:
            interp = "strong correlation — high co-failure rate, limited complementarity"
        lines.append(f"Interpretation: φ={phi_val:.3f} → {interp}")

        ct = overall["contingency_table"]
        total_errors = ct["fol_only_correct"] + ct["code_only_correct"] + ct["both_wrong"]
        if total_errors > 0:
            complementary = ct["fol_only_correct"] + ct["code_only_correct"]
            lines.append(f"Of {total_errors} total error cases: {complementary} ({complementary/total_errors*100:.1f}%) are complementary (only one fails)")
    lines.append("")
    return "\n".join(lines)


def format_cost(cost_results):
    lines = []
    lines.append("=" * 70)
    lines.append("(f) Cost-Effectiveness Analysis")
    lines.append("=" * 70)
    lines.append("")

    ts = cost_results["token_summary"]
    lines.append("Token Usage:")
    lines.append(f"  Total tokens:        {ts['total_tokens']:>12,}")
    lines.append(f"  Total API calls:     {ts['total_api_calls']:>12,}")
    lines.append(f"  Avg tokens/sample:   {ts['avg_tokens_per_sample']:>12,}")
    lines.append(f"  Avg calls/sample:    {ts['avg_calls_per_sample']:>12}")
    lines.append("")

    cb = cost_results["cost_breakdown"]
    lines.append("Cost Breakdown (tokens per sample):")
    lines.append(f"  Single-rep (Code only, est.): {cb['single_rep_tokens_per_sample']:>10,}")
    lines.append(f"  Dual-rep base (FOL+Code):     {cb['dual_rep_base_tokens_per_sample']:>10,}")
    lines.append(f"  Repair extra (per repair):    {cb['repair_extra_tokens_per_repair_sample']:>10,}")
    lines.append(f"  Samples needing repair:       {cb['repair_samples']:>10} / {cost_results['total_samples']}")
    lines.append("")

    cm = cost_results["cost_multipliers"]
    lines.append("Cost Multipliers (vs single-representation):")
    lines.append(f"  Dual base (FOL+Code) / Single:     {cm['dual_base_vs_single']:.2f}x")
    lines.append(f"  Full pipeline (+ repair) / Single: {cm['full_pipeline_vs_single']:.2f}x")
    lines.append("")

    acc = cost_results["accuracy"]
    lines.append("Accuracy:")
    lines.append(f"  Code only (baseline):        {acc['code_only']:.1%}")
    lines.append(f"  FOL only:                    {acc['fol_only']:.1%}")
    lines.append(f"  Oracle (best of two):        {acc['oracle_upper_bound']:.1%}")
    lines.append(f"  Pipeline (repair only):      {acc['pipeline_repair']:.1%}")
    lines.append(f"  Pipeline (repair+fallback):  {acc['pipeline_repair_fol_fallback']:.1%}")
    lines.append("")

    ce = cost_results["cost_effectiveness"]
    lines.append("Cost-Effectiveness:")
    lines.append(f"  Accuracy gain (repair vs Code):     +{ce['accuracy_gain_repair_vs_code']:.1%}")
    lines.append(f"  Accuracy gain (repair+fb vs Code):  +{ce['accuracy_gain_repair_fb_vs_code']:.1%}")
    lines.append(f"  Gain per unit extra cost (repair):   {ce['gain_per_unit_cost_repair']:.4f}")
    lines.append(f"  Gain per unit extra cost (rep+fb):   {ce['gain_per_unit_cost_repair_fb']:.4f}")
    lines.append("")

    # Interpretation
    multiplier = cm["full_pipeline_vs_single"]
    gain = ce["accuracy_gain_repair_fb_vs_code"]
    lines.append(f"Interpretation: {multiplier:.1f}x cost yields +{gain:.1%} accuracy gain over single-representation baseline.")
    if ce["gain_per_unit_cost_repair_fb"] > 0.05:
        lines.append("The marginal return is favorable — each unit of extra cost buys meaningful accuracy improvement.")
    elif ce["gain_per_unit_cost_repair_fb"] > 0.02:
        lines.append("The marginal return is moderate — cost increase is justified for accuracy-sensitive applications.")
    else:
        lines.append("The marginal return is low — the cost increase may not be justified for all use cases.")
    lines.append("")
    return "\n".join(lines)


def main():
    data = load_data(DATA_PATH)
    print(f"Loaded {len(data)} samples")

    # (e) Phi coefficient
    phi_results = analysis_e(data)
    phi_text = format_phi_table(phi_results)
    print(phi_text)

    # (f) Cost-effectiveness
    cost_results = analysis_f(data)
    cost_text = format_cost(cost_results)
    print(cost_text)

    # Save JSON
    output = {
        "phi_coefficient": phi_results,
        "cost_effectiveness": cost_results,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Saved JSON: {OUT_JSON}")

    # Save TXT
    with open(OUT_TXT, "w") as f:
        f.write(phi_text)
        f.write("\n")
        f.write(cost_text)
    print(f"Saved TXT: {OUT_TXT}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Compute seed-level TOST and Bayesian ROPE for 14B CLS-CWM and CLS-TRAJ.

Decision D169: Training seeds are the true replication unit. All primary
statistical tests use seed-level paired analysis (df = n_seeds - 1).

14B per-seed accuracy (bf16-consistent, from registry):
  CLS: s42=89.21 (bf16 eval), s123=90.79, s456=89.79
  CWM: s42=89.26 (bf16 eval), s123=88.99, s456=90.26
  TRAJ: s42=89.73, s123=88.57, s456=88.28

Data sources:
  CLS s42: cls14b-func-s42-v2-bf16-eval (accuracy=89.21)
  CLS s123: cls14b-func-s123 (accuracy=90.79, dtype=bf16)
  CLS s456: cls14b-func-s456 (accuracy=89.79, dtype=bf16)
  CWM s42: inferred from bf16 eval gap_vs_cwm=-0.05 → 89.26
           (NF4 registry: cwm14b-func-s42 accuracy=89.30)
  CWM s123: cwm14b-func-s123 (accuracy=88.99, dtype=bf16)
  CWM s456: cwm14b-func-s456 (accuracy=90.26, dtype=bf16)
  TRAJ s42: traj14b-func-s42 (accuracy=89.73, dtype=bf16)
  TRAJ s123: traj14b-func-s123 (accuracy=88.57, dtype=bf16)
  TRAJ s456: traj14b-func-s456 (accuracy=88.28, dtype=bf16)
"""

import json
import math
import pathlib
from scipy.stats import t as t_dist

OUTPUT_DIR = pathlib.Path(__file__).parent

# ── 14B per-seed accuracy (bf16-consistent) ──────────────────────────
CLS_14B = [89.21, 90.79, 89.79]   # s42, s123, s456
CWM_14B = [89.26, 88.99, 90.26]   # s42, s123, s456
TRAJ_14B = [89.73, 88.57, 88.28]  # s42, s123, s456
SEEDS = ["s42", "s123", "s456"]

ROPE_MARGIN = 2.0  # ±2pp SESOI


def paired_stats(a, b):
    """Compute paired difference statistics."""
    diffs = [ai - bi for ai, bi in zip(a, b)]
    n = len(diffs)
    mean = sum(diffs) / n
    sd = math.sqrt(sum((d - mean) ** 2 for d in diffs) / (n - 1))
    se = sd / math.sqrt(n)
    return diffs, mean, sd, se, n


def seed_level_tost(diffs, mean, sd, n, margin=ROPE_MARGIN):
    """Paired TOST using seed-level means (D169 primary method).

    Two one-sided t-tests:
      H0_lower: μ ≤ -margin  →  t_lower = (mean - (-margin)) / SE
      H0_upper: μ ≥ +margin  →  t_upper = (mean - margin) / SE
    TOST p = max(p_lower, p_upper)
    """
    df = n - 1
    se = sd / math.sqrt(n)

    if se == 0:
        p_lower = 0.0 if mean > -margin else 1.0
        p_upper = 0.0 if mean < margin else 1.0
    else:
        t_lower = (mean - (-margin)) / se
        t_upper = (mean - margin) / se
        p_lower = 1 - float(t_dist.cdf(t_lower, df=df))
        p_upper = float(t_dist.cdf(t_upper, df=df))

    tost_p = max(p_lower, p_upper)
    equivalent = tost_p < 0.05

    # 90% CI for equivalence
    ci90_lo = mean - float(t_dist.ppf(0.95, df=df)) * se
    ci90_hi = mean + float(t_dist.ppf(0.95, df=df)) * se
    ci90_inside = ci90_lo > -margin and ci90_hi < margin

    # 95% CI for reference
    ci95_lo = mean - float(t_dist.ppf(0.975, df=df)) * se
    ci95_hi = mean + float(t_dist.ppf(0.975, df=df)) * se

    return {
        "method": "seed-level paired TOST (D169)",
        "n_seeds": n,
        "df": df,
        "mean_diff_pp": round(mean, 4),
        "sd_pp": round(sd, 4),
        "se_pp": round(se, 4),
        "margin_pp": margin,
        "t_lower": round(t_lower, 4) if se > 0 else None,
        "t_upper": round(t_upper, 4) if se > 0 else None,
        "p_lower": round(p_lower, 6),
        "p_upper": round(p_upper, 6),
        "tost_p": round(tost_p, 6),
        "equivalent_at_alpha05": equivalent,
        "ci90_pp": [round(ci90_lo, 3), round(ci90_hi, 3)],
        "ci90_inside_rope": ci90_inside,
        "ci95_pp": [round(ci95_lo, 3), round(ci95_hi, 3)],
        "diffs": [round(d, 2) for d in diffs],
    }


def bayesian_rope(mean_diff, sd_diff, n, margin=ROPE_MARGIN):
    """Bayesian ROPE (Kruschke 2013, Jeffreys prior).

    Posterior: t(n-1, x̄, s/√n)
    P(ROPE) = P(-margin < μ < margin | data)
    """
    df = n - 1
    se = sd_diff / math.sqrt(n)

    p_rope = float(
        t_dist.cdf(margin, df=df, loc=mean_diff, scale=se)
        - t_dist.cdf(-margin, df=df, loc=mean_diff, scale=se)
    )
    p_above = float(1 - t_dist.cdf(margin, df=df, loc=mean_diff, scale=se))
    p_below = float(t_dist.cdf(-margin, df=df, loc=mean_diff, scale=se))

    hdi_lo = float(t_dist.ppf(0.025, df=df, loc=mean_diff, scale=se))
    hdi_hi = float(t_dist.ppf(0.975, df=df, loc=mean_diff, scale=se))
    hdi_inside = hdi_lo >= -margin and hdi_hi <= margin

    if p_rope > 0.9:
        decision = "Equivalence supported"
    elif p_rope < 0.1:
        decision = "Reject equivalence"
    else:
        decision = "Inconclusive"

    if hdi_inside:
        hdi_decision = "Accept equivalence (95% HDI inside ROPE)"
    elif hdi_lo > margin or hdi_hi < -margin:
        hdi_decision = "Reject equivalence (95% HDI outside ROPE)"
    else:
        hdi_decision = "Undecided (95% HDI overlaps ROPE boundary)"

    return {
        "method": "Bayesian ROPE (Kruschke 2013, Jeffreys prior)",
        "n": n,
        "df": df,
        "mean_diff_pp": round(mean_diff, 4),
        "sd_pp": round(sd_diff, 4),
        "se_pp": round(se, 4),
        "rope": [-margin, margin],
        "p_rope": round(p_rope, 4),
        "p_above_rope": round(p_above, 4),
        "p_below_rope": round(p_below, 4),
        "hdi_95_lo": round(hdi_lo, 2),
        "hdi_95_hi": round(hdi_hi, 2),
        "hdi_inside_rope": bool(hdi_inside),
        "decision_continuous": decision,
        "decision_hdi": hdi_decision,
    }


def holm_bonferroni_14b(comparisons, alpha=0.05):
    """Holm-Bonferroni for 14B cross-scale family (k=4)."""
    k = len(comparisons)
    sorted_comps = sorted(comparisons, key=lambda x: x["raw_p"])
    rejected = True
    for i, comp in enumerate(sorted_comps):
        rank = i + 1
        comp["adj_p"] = min(comp["raw_p"] * (k - rank + 1), 1.0)
        comp["rank"] = rank
        comp["multiplier"] = k - rank + 1
        threshold = alpha / (k - rank + 1)
        if rejected and comp["raw_p"] <= threshold:
            comp["significant"] = True
        else:
            comp["significant"] = False
            rejected = False
    return sorted_comps


# ── Main computation ─────────────────────────────────────────────────

print("=" * 80)
print("14B SEED-LEVEL STATISTICAL ANALYSIS (D169 compliant)")
print("=" * 80)

results = {}

for comparison_name, group_a, group_b in [
    ("CLS-CWM", CLS_14B, CWM_14B),
    ("CLS-TRAJ", CLS_14B, TRAJ_14B),
]:
    print(f"\n{'─' * 60}")
    print(f"  {comparison_name} (14B, 3 seeds)")
    print(f"{'─' * 60}")

    a_label = "CLS"
    b_label = comparison_name.split("-")[1]

    print(f"  {a_label}: {group_a}  mean={sum(group_a)/len(group_a):.2f}")
    print(f"  {b_label}: {group_b}  mean={sum(group_b)/len(group_b):.2f}")

    diffs, mean, sd, se, n = paired_stats(group_a, group_b)
    print(f"  Diffs ({a_label}-{b_label}): {[round(d,2) for d in diffs]}")
    print(f"  Mean diff: {mean:+.4f}pp, SD: {sd:.4f}pp, SE: {se:.4f}pp, n={n}, df={n-1}")

    # TOST
    tost = seed_level_tost(diffs, mean, sd, n)
    print(f"\n  TOST (±{ROPE_MARGIN}pp):")
    print(f"    t_lower: {tost['t_lower']:.4f}, p_lower: {tost['p_lower']:.6f}")
    print(f"    t_upper: {tost['t_upper']:.4f}, p_upper: {tost['p_upper']:.6f}")
    print(f"    TOST p = {tost['tost_p']:.6f}")
    print(f"    Equivalent at α=0.05: {'YES' if tost['equivalent_at_alpha05'] else 'NO'}")
    print(f"    90% CI: [{tost['ci90_pp'][0]:+.3f}, {tost['ci90_pp'][1]:+.3f}]pp")
    print(f"    95% CI: [{tost['ci95_pp'][0]:+.3f}, {tost['ci95_pp'][1]:+.3f}]pp")

    # Bayesian ROPE
    rope = bayesian_rope(mean, sd, n)
    print(f"\n  Bayesian ROPE (±{ROPE_MARGIN}pp):")
    print(f"    P(ROPE) = {rope['p_rope']:.4f}")
    print(f"    P(above) = {rope['p_above_rope']:.4f}, P(below) = {rope['p_below_rope']:.4f}")
    print(f"    95% HDI: [{rope['hdi_95_lo']:+.2f}, {rope['hdi_95_hi']:+.2f}]pp")
    print(f"    HDI inside ROPE: {rope['hdi_inside_rope']}")
    print(f"    Decision: {rope['decision_continuous']} / {rope['decision_hdi']}")

    results[comparison_name] = {
        "seeds": SEEDS,
        "a_values": group_a,
        "b_values": group_b,
        "tost": tost,
        "bayesian_rope": rope,
    }

# ── Paper value comparison ───────────────────────────────────────────
print(f"\n{'=' * 80}")
print("COMPARISON WITH PAPER VALUES")
print(f"{'=' * 80}")

paper_values = {
    "CLS-CWM": {
        "paper_tost_p": "unknown (conclusion.tex: TOST p=0.0006, but this may be per-test)",
        "note": "conclusion.tex says 'TOST p=0.0006' for CLS-CWM 14B",
    },
    "CLS-TRAJ": {
        "paper_tost_p": 0.043,
        "paper_p_rope": 0.956,
        "paper_adj_p": 0.050,
        "note": "experiments.tex line 104, appendix line 443",
    },
}

for comp_name, paper in paper_values.items():
    r = results[comp_name]
    print(f"\n  {comp_name}:")
    tost_p = r["tost"]["tost_p"]
    print(f"    Seed-level TOST p = {tost_p:.6f}")
    if comp_name == "CLS-TRAJ":
        print(f"    Paper TOST p     = {paper['paper_tost_p']}")
        match_tost = "MATCH" if abs(tost_p - paper["paper_tost_p"]) < 0.005 else "MISMATCH"
        print(f"    → {match_tost}")

        rope_p = r["bayesian_rope"]["p_rope"]
        print(f"    Seed-level P(ROPE) = {rope_p:.4f}")
        print(f"    Paper P(ROPE)      = {paper['paper_p_rope']}")
        match_rope = "MATCH" if abs(rope_p - paper["paper_p_rope"]) < 0.005 else "MISMATCH"
        print(f"    → {match_rope}")
    print(f"    Note: {paper['note']}")

# ── Holm-Bonferroni for 14B cross-scale family ───────────────────────
print(f"\n{'=' * 80}")
print("HOLM-BONFERRONI 14B CROSS-SCALE FAMILY (k=4)")
print(f"{'=' * 80}")

holm_comparisons = [
    {"name": "14B CLS-CWM TOST", "raw_p": results["CLS-CWM"]["tost"]["tost_p"]},
    {"name": "14B CLS-TRAJ TOST", "raw_p": results["CLS-TRAJ"]["tost"]["tost_p"]},
    {"name": "14B CLS-CWM superiority", "raw_p": 0.5,
     "note": "placeholder — superiority not tested at seed level"},
    {"name": "14B CLS-TRAJ superiority", "raw_p": 0.5,
     "note": "placeholder — superiority not tested at seed level"},
]

holm_results = holm_bonferroni_14b(holm_comparisons)
print(f"{'Rank':<5} {'Comparison':<30} {'Raw p':>8} {'×':>3} {'Adj p':>8} {'Sig?':>6}")
print("-" * 65)
for r in holm_results:
    sig = "YES" if r["significant"] else "no"
    print(f"{r['rank']:<5} {r['name']:<30} {r['raw_p']:>8.6f} {r['multiplier']:>3} {r['adj_p']:>8.6f} {sig:>6}")

# ── Save results ─────────────────────────────────────────────────────
output = {
    "title": "14B Seed-Level Statistical Analysis (D169 compliant)",
    "method": "Seed-level paired t-test (training seeds = replication unit)",
    "n_seeds": 3,
    "df": 2,
    "rope_margin_pp": ROPE_MARGIN,
    "data": {
        "CLS_14B": dict(zip(SEEDS, CLS_14B)),
        "CWM_14B": dict(zip(SEEDS, CWM_14B)),
        "TRAJ_14B": dict(zip(SEEDS, TRAJ_14B)),
        "note": "All bf16-consistent. CLS s42=89.21 from bf16 eval (NF4=89.47). CWM s42=89.26 from bf16 eval (NF4=89.30).",
    },
    "results": {
        comp: {
            "tost": r["tost"],
            "bayesian_rope": r["bayesian_rope"],
        }
        for comp, r in results.items()
    },
    "paper_comparison": {
        "CLS-TRAJ": {
            "seed_level_tost_p": results["CLS-TRAJ"]["tost"]["tost_p"],
            "paper_tost_p": 0.043,
            "match": abs(results["CLS-TRAJ"]["tost"]["tost_p"] - 0.043) < 0.005,
            "seed_level_p_rope": results["CLS-TRAJ"]["bayesian_rope"]["p_rope"],
            "paper_p_rope": 0.956,
            "match_rope": abs(results["CLS-TRAJ"]["bayesian_rope"]["p_rope"] - 0.956) < 0.005,
            "diagnosis": "Paper values (p=0.043, P(ROPE)=0.956) are from per-test clustered bootstrap, NOT seed-level. D169 requires seed-level values.",
        },
    },
}

out_path = OUTPUT_DIR / "14b_seed_level_stats.json"
out_path.write_text(json.dumps(output, indent=2) + "\n")
print(f"\nSaved to {out_path}")

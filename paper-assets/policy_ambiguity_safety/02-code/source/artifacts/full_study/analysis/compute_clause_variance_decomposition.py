"""
Clause-level variance decomposition of violation rates.

Quantifies how much violation variance is clause-specific vs model-specific
using ICC, mixed-effects models, and categorical breakdowns.

Input: per_clause_summary.csv (300 clauses × 5 models × 2 conditions)
Output: clause_variance_decomposition.json
"""

import json
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from pathlib import Path

ANALYSIS_DIR = Path(__file__).parent
CSV_PATH = ANALYSIS_DIR / "per_clause_summary.csv"
OUTPUT_PATH = ANALYSIS_DIR / "clause_variance_decomposition.json"

def compute_icc_oneway(df_sub, value_col="violation_rate", group_col="clause_id"):
    """
    Compute ICC(1) using one-way random effects ANOVA.
    ICC(1) = (MS_between - MS_within) / (MS_between + (k-1)*MS_within)
    where k = number of raters per group (models per clause).
    """
    groups = df_sub.groupby(group_col)[value_col]
    n_groups = groups.ngroups
    group_sizes = groups.count()
    k = group_sizes.mean()  # average group size

    grand_mean = df_sub[value_col].mean()
    group_means = groups.mean()

    # SS_between = sum(n_j * (mean_j - grand_mean)^2)
    ss_between = sum(group_sizes[g] * (group_means[g] - grand_mean)**2 for g in group_means.index)
    df_between = n_groups - 1

    # SS_within = sum of (x_ij - mean_j)^2
    ss_within = 0
    for name, grp in groups:
        ss_within += ((grp - group_means[name])**2).sum()
    df_within = len(df_sub) - n_groups

    if df_between == 0 or df_within == 0:
        return np.nan

    ms_between = ss_between / df_between
    ms_within = ss_within / df_within

    denom = ms_between + (k - 1) * ms_within
    if denom == 0:
        return np.nan

    icc = (ms_between - ms_within) / denom
    return icc


def compute_variance_components_mixedlm(df):
    """
    Fit a mixed-effects linear model:
      violation_rate ~ C(model) + C(ambiguity_type) + C(condition)
    with random intercept for clause_id.

    Extract variance components from the fitted model.
    """
    # Fit mixed model with clause_id as random effect
    md = smf.mixedlm(
        "violation_rate ~ C(model) + C(ambiguity_type) + C(condition)",
        data=df,
        groups=df["clause_id"]
    )
    mdf = md.fit(reml=True)

    # Variance of random effect (clause)
    var_clause = float(mdf.cov_re.iloc[0, 0])
    # Residual variance
    var_resid = float(mdf.scale)

    return mdf, var_clause, var_resid


def compute_r2_fixed_effects(df):
    """
    Compute variance explained by each fixed effect using sequential Type I SS.
    Fit OLS models adding one factor at a time.
    """
    import statsmodels.api as sm
    from statsmodels.formula.api import ols

    total_var = df["violation_rate"].var()

    results = {}

    # Model with just condition
    m_cond = ols("violation_rate ~ C(condition)", data=df).fit()
    var_cond = 1 - m_cond.ssr / (total_var * (len(df) - 1))

    # Model with condition + model
    m_cm = ols("violation_rate ~ C(condition) + C(model)", data=df).fit()
    var_model_added = (m_cond.ssr - m_cm.ssr) / (total_var * (len(df) - 1))

    # Model with condition + model + ambiguity_type
    m_cma = ols("violation_rate ~ C(condition) + C(model) + C(ambiguity_type)", data=df).fit()
    var_type_added = (m_cm.ssr - m_cma.ssr) / (total_var * (len(df) - 1))

    # Full model with clause_id (absorbs ambiguity_type since clause->type is deterministic)
    # Use mixed model results for clause variance

    return {
        "condition_r2": float(var_cond),
        "model_r2": float(var_model_added),
        "ambiguity_type_r2": float(var_type_added),
    }


def compute_manual_variance_components(df):
    """
    Manual variance decomposition using sum-of-squares approach.
    Since clause_id nests within ambiguity_type, we compute:
    - var(condition): between-condition variance
    - var(model): between-model variance
    - var(clause within type): between-clause variance (after removing type effect)
    - var(ambiguity_type): between-type variance
    - var(residual): remaining
    """
    y = df["violation_rate"].values
    grand_mean = y.mean()
    ss_total = np.sum((y - grand_mean)**2)
    n = len(y)

    # Condition means
    cond_means = df.groupby("condition")["violation_rate"].mean()
    cond_counts = df.groupby("condition")["violation_rate"].count()
    ss_condition = sum(cond_counts[c] * (cond_means[c] - grand_mean)**2 for c in cond_means.index)

    # Model means
    model_means = df.groupby("model")["violation_rate"].mean()
    model_counts = df.groupby("model")["violation_rate"].count()
    ss_model = sum(model_counts[m] * (model_means[m] - grand_mean)**2 for m in model_means.index)

    # Ambiguity type means
    type_means = df.groupby("ambiguity_type")["violation_rate"].mean()
    type_counts = df.groupby("ambiguity_type")["violation_rate"].count()
    ss_type = sum(type_counts[t] * (type_means[t] - grand_mean)**2 for t in type_means.index)

    # Clause means (nested within type, so clause effect includes type effect)
    clause_means = df.groupby("clause_id")["violation_rate"].mean()
    clause_counts = df.groupby("clause_id")["violation_rate"].count()
    ss_clause_total = sum(clause_counts[c] * (clause_means[c] - grand_mean)**2 for c in clause_means.index)

    # Clause within type = clause_total - type
    ss_clause_within_type = ss_clause_total - ss_type

    # Residual (what's left after all main effects)
    # Using Type III-like approach: fit a model with all factors
    from statsmodels.formula.api import ols

    # Can't include both clause_id and ambiguity_type (collinear: clause determines type)
    # So compute: total = type + clause_within_type + condition + model + interactions + residual

    # Full additive model with clause_id + condition + model
    m_full = ols("violation_rate ~ C(clause_id) + C(condition) + C(model)", data=df).fit()
    ss_resid_full = m_full.ssr

    # Get proper SS for each from ANOVA table
    import statsmodels.api as sm
    anova = sm.stats.anova_lm(m_full, typ=2)

    return ss_total, ss_condition, ss_model, ss_type, ss_clause_within_type, ss_resid_full, anova


def danger_profile(df_amb):
    """
    Classify clauses by how many models violated them (ambiguous condition only).
    """
    # For each clause, count how many models had a violation
    clause_model_violation = df_amb.groupby("clause_id")["violation_rate"].sum()
    clause_type = df_amb.groupby("clause_id")["ambiguity_type"].first()

    n_models_violated = clause_model_violation  # since violation_rate is 0 or 1

    categories = {}
    categories["universally_dangerous"] = (n_models_violated >= 4)
    categories["moderate_danger"] = (n_models_violated == 3)
    categories["model_specific"] = ((n_models_violated >= 1) & (n_models_violated <= 2))
    categories["safe"] = (n_models_violated == 0)

    n_clauses = len(clause_model_violation)

    profile = {}
    for cat, mask in categories.items():
        desc_map = {
            "universally_dangerous": ">=4/5 models violated",
            "moderate_danger": "3 models violated",
            "model_specific": "1-2 models violated",
            "safe": "0 models violated"
        }
        count = int(mask.sum())
        profile[cat] = {
            "count": count,
            "pct": round(count / n_clauses * 100, 1),
            "description": desc_map[cat]
        }

    # Per-type breakdown
    per_type = {}
    for atype in sorted(clause_type.unique()):
        type_clauses = clause_type[clause_type == atype].index
        type_violations = n_models_violated[type_clauses]
        per_type[atype] = {
            "universal": int((type_violations >= 4).sum()),
            "moderate": int((type_violations == 3).sum()),
            "model_specific": int(((type_violations >= 1) & (type_violations <= 2)).sum()),
            "safe": int((type_violations == 0).sum()),
        }

    profile["per_type_breakdown"] = per_type

    # Example clauses for each category
    examples = {}
    for cat, mask in categories.items():
        clause_ids = mask[mask].index.tolist()
        examples[cat] = clause_ids[:5]  # up to 5 examples
    profile["examples"] = examples

    return profile


def main():
    df = pd.read_csv(CSV_PATH)
    print(f"Loaded {len(df)} rows, {df['clause_id'].nunique()} clauses, {df['model'].nunique()} models")

    # violation_rate is already binary (0 or 1) since n_episodes=1
    df["violation"] = df["violation_rate"].astype(float)

    # === Step 1: Overall ICC (ambiguous condition) ===
    df_amb = df[df["condition"] == "ambiguous"].copy()
    print(f"\nAmbiguous condition: {len(df_amb)} rows, {df_amb['clause_id'].nunique()} clauses")

    overall_icc = compute_icc_oneway(df_amb, value_col="violation", group_col="clause_id")
    print(f"Overall ICC (ambiguous): {overall_icc:.4f}")

    # === Step 2: Mixed-effects model (full data) ===
    print("\nFitting mixed-effects model...")
    mdf, var_clause_re, var_resid_re = compute_variance_components_mixedlm(df)
    print(f"  Random effect variance (clause): {var_clause_re:.4f}")
    print(f"  Residual variance: {var_resid_re:.4f}")
    print(f"  ICC from mixed model: {var_clause_re / (var_clause_re + var_resid_re):.4f}")
    print(mdf.summary())

    # === Step 3: Manual variance decomposition ===
    print("\nComputing manual variance decomposition...")
    ss_total, ss_cond, ss_model, ss_type, ss_clause_wt, ss_resid, anova = compute_manual_variance_components(df)

    print(f"  SS_total: {ss_total:.2f}")
    print(f"  SS_condition: {ss_cond:.2f} ({ss_cond/ss_total*100:.1f}%)")
    print(f"  SS_model: {ss_model:.2f} ({ss_model/ss_total*100:.1f}%)")
    print(f"  SS_ambiguity_type: {ss_type:.2f} ({ss_type/ss_total*100:.1f}%)")
    print(f"  SS_clause_within_type: {ss_clause_wt:.2f} ({ss_clause_wt/ss_total*100:.1f}%)")
    print(f"  SS_residual (full model): {ss_resid:.2f} ({ss_resid/ss_total*100:.1f}%)")

    # Proper variance components from ANOVA Type II
    print("\nANOVA Type II results:")
    print(anova)

    # Compute R² decomposition from sequential approach
    r2_fx = compute_r2_fixed_effects(df)
    print(f"\nR² from fixed effects:")
    for k, v in r2_fx.items():
        print(f"  {k}: {v:.4f}")

    # === Step 4: Per-type ICC (ambiguous only) ===
    print("\nPer-type ICC (ambiguous condition):")
    per_type_icc = {}
    for atype in sorted(df_amb["ambiguity_type"].unique()):
        df_type = df_amb[df_amb["ambiguity_type"] == atype]
        icc = compute_icc_oneway(df_type, value_col="violation", group_col="clause_id")
        n_cl = df_type["clause_id"].nunique()
        per_type_icc[atype] = {"icc": round(float(icc), 4), "n_clauses": n_cl}
        print(f"  {atype}: ICC={icc:.4f} (n={n_cl})")

    # === Step 5: Danger profile (ambiguous only) ===
    print("\nDanger profile (ambiguous condition):")
    profile = danger_profile(df_amb)
    for k in ["universally_dangerous", "moderate_danger", "model_specific", "safe"]:
        p = profile[k]
        print(f"  {k}: {p['count']} ({p['pct']}%)")
    print("\n  Per-type breakdown:")
    for atype, counts in sorted(profile["per_type_breakdown"].items()):
        print(f"    {atype}: universal={counts['universal']}, moderate={counts['moderate']}, "
              f"model_specific={counts['model_specific']}, safe={counts['safe']}")

    # === Assemble output ===
    # Variance components using ANOVA SS approach (Type II from full model)
    # Extract from anova table
    anova_ss = {}
    for factor in anova.index:
        if factor != "Residual":
            anova_ss[factor] = float(anova.loc[factor, "sum_sq"])
    ss_resid_anova = float(anova.loc["Residual", "sum_sq"])

    # Compute proper proportions from the full model ANOVA
    # clause_id SS from ANOVA includes type effect; separate them
    clause_id_ss = float(anova.loc["C(clause_id)", "sum_sq"]) if "C(clause_id)" in anova.index else 0
    condition_ss = float(anova.loc["C(condition)", "sum_sq"]) if "C(condition)" in anova.index else 0
    model_ss = float(anova.loc["C(model)", "sum_sq"]) if "C(model)" in anova.index else 0

    total_ss_decomp = clause_id_ss + condition_ss + model_ss + ss_resid_anova

    # For reporting, split clause_id into type + clause_within_type
    # clause_id captures both type and clause effects
    variance_components = {
        "clause_id": {
            "sum_sq": round(float(clause_id_ss), 4),
            "pct": round(clause_id_ss / total_ss_decomp * 100, 1),
            "note": "includes ambiguity_type effect (clause nests within type)"
        },
        "ambiguity_type": {
            "sum_sq": round(float(ss_type), 4),
            "pct": round(ss_type / ss_total * 100, 1),
            "note": "between-type component of clause_id"
        },
        "clause_within_type": {
            "sum_sq": round(float(ss_clause_wt), 4),
            "pct": round(ss_clause_wt / ss_total * 100, 1),
            "note": "clause-specific variance beyond type"
        },
        "model": {
            "sum_sq": round(float(model_ss), 4),
            "pct": round(model_ss / total_ss_decomp * 100, 1)
        },
        "condition": {
            "sum_sq": round(float(condition_ss), 4),
            "pct": round(condition_ss / total_ss_decomp * 100, 1)
        },
        "residual": {
            "sum_sq": round(float(ss_resid_anova), 4),
            "pct": round(ss_resid_anova / total_ss_decomp * 100, 1)
        }
    }

    # Mixed model ICC
    mixed_icc = var_clause_re / (var_clause_re + var_resid_re)

    output = {
        "analysis_name": "Clause-Level Variance Decomposition",
        "motivation": "Quantify how much violation variance is clause-specific vs model-specific",
        "n_clauses": int(df["clause_id"].nunique()),
        "n_models": int(df["model"].nunique()),
        "n_observations": int(len(df)),
        "n_ambiguous_observations": int(len(df_amb)),

        "overall_icc": {
            "icc_clause_oneway_ambiguous": round(float(overall_icc), 4),
            "icc_clause_mixedlm_full": round(float(mixed_icc), 4),
            "interpretation": (
                f"{overall_icc*100:.1f}% of violation variance (ambiguous condition) is explained by clause identity "
                f"(one-way ICC). Mixed-model ICC across all data: {mixed_icc*100:.1f}%."
            ),
            "method": "one-way random effects ANOVA (ambiguous) + MixedLM with random clause intercept (full data)"
        },

        "mixed_model": {
            "random_effect_variance_clause": round(float(var_clause_re), 6),
            "residual_variance": round(float(var_resid_re), 6),
            "icc": round(float(mixed_icc), 4),
            "fixed_effects": {
                name: round(float(mdf.fe_params[name]), 4)
                for name in mdf.fe_params.index
            }
        },

        "variance_components": variance_components,

        "per_type_icc": per_type_icc,

        "clause_danger_profile": profile,

        "conclusion": ""  # filled below
    }

    # Build conclusion
    icc_pct = overall_icc * 100
    clause_pct = variance_components["clause_id"]["pct"]
    model_pct = variance_components["model"]["pct"]
    cond_pct = variance_components["condition"]["pct"]
    resid_pct = variance_components["residual"]["pct"]
    n_universal = profile["universally_dangerous"]["count"]
    n_safe = profile["safe"]["count"]

    output["conclusion"] = (
        f"Clause identity is the dominant source of violation variance: "
        f"ICC={overall_icc:.3f} in ambiguous condition, "
        f"clause_id explains {clause_pct}% of total SS vs model {model_pct}% and condition {cond_pct}% "
        f"(residual {resid_pct}%). "
        f"In the ambiguous condition, {n_universal}/300 clauses are universally dangerous (>=4/5 models violated) "
        f"while {n_safe}/300 are safe (no model violated)."
    )

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\n=== Output saved to {OUTPUT_PATH} ===")
    print(f"\nConclusion: {output['conclusion']}")


if __name__ == "__main__":
    main()

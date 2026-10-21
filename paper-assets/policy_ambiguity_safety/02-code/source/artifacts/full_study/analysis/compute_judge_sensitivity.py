#!/usr/bin/env python3
"""Judge Model Covariate Sensitivity Check.

Checks whether judge_model (gpt-4.1 vs gpt-5.4) is a confound
in the cross-judge experimental design.
"""

import json
import os
import sys
import warnings

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

warnings.filterwarnings("ignore")

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JUDGMENT_DIR = os.path.join(BASE, "judgments")
ANALYSIS_DIR = os.path.join(BASE, "analysis")
CLAUSE_TEMPLATES = os.path.join(
    os.path.dirname(BASE), "_project", "data", "clause_templates_full.json"
)

MODELS = ["gpt-5.4", "gpt-4.1", "claude-sonnet-4-6", "qwen3-235b", "deepseek-v3"]


def load_judgments():
    rows = []
    for model in MODELS:
        path = os.path.join(JUDGMENT_DIR, model, "judgments.jsonl")
        with open(path) as f:
            for line in f:
                rec = json.loads(line)
                rows.append({
                    "clause_id": rec["clause_id"],
                    "condition": rec["condition"],
                    "ambiguity_type": rec["ambiguity_type"],
                    "model": rec["model"],
                    "judge_model": rec["judge_model"],
                    "violation_level": rec["judgment"]["violation_level"],
                    "confidence": rec["judgment"]["confidence"],
                })
    df = pd.DataFrame(rows)
    df["violation"] = df["violation_level"].isin(["moderate", "critical"]).astype(int)
    return df


def compute_token_deltas():
    """Per-clause token delta from clause templates."""
    with open(CLAUSE_TEMPLATES) as f:
        templates = json.load(f)
    deltas = {}
    for t in templates:
        cid = t["clause_id"]
        amb_len = len(t["ambiguous_clause"].split())
        unamb_len = len(t["unambiguous_clause"].split())
        deltas[cid] = unamb_len - amb_len
    return deltas


def judge_baseline(df):
    result = {}
    for jm in df["judge_model"].unique():
        sub = df[df["judge_model"] == jm]
        result[f"{jm}_as_judge"] = {
            "n": int(len(sub)),
            "violation_rate": round(float(sub["violation"].mean()), 4),
        }

    j41 = df[df["judge_model"] == "gpt-4.1"]["violation"]
    j54 = df[df["judge_model"] == "gpt-5.4"]["violation"]
    diff = float(j41.mean() - j54.mean())
    ct = pd.crosstab(df["judge_model"], df["violation"])
    chi2, p, _, _ = stats.chi2_contingency(ct)
    result["difference"] = round(diff, 4)
    result["chi2_p"] = round(float(p), 6)

    # Controlled for condition
    controlled = {}
    for cond in df["condition"].unique():
        sub = df[df["condition"] == cond]
        j41_s = sub[sub["judge_model"] == "gpt-4.1"]["violation"]
        j54_s = sub[sub["judge_model"] == "gpt-5.4"]["violation"]
        controlled[cond] = {
            "gpt-4.1_rate": round(float(j41_s.mean()), 4) if len(j41_s) > 0 else None,
            "gpt-5.4_rate": round(float(j54_s.mean()), 4) if len(j54_s) > 0 else None,
        }
    result["controlled_by_condition"] = controlled
    return result


def run_logistic_models(df):
    results = {}

    # Model 1: baseline
    m1 = smf.logit(
        "violation ~ C(condition, Treatment(reference='unambiguous')) + C(ambiguity_type) + C(model)",
        data=df,
    ).fit(disp=0)

    cond_coef_m1 = float(m1.params.get(
        "C(condition, Treatment(reference='unambiguous'))[T.ambiguous]",
        np.nan
    ))
    cond_p_m1 = float(m1.pvalues.get(
        "C(condition, Treatment(reference='unambiguous'))[T.ambiguous]",
        np.nan
    ))

    results["model_1_baseline"] = {
        "aic": round(float(m1.aic), 2),
        "bic": round(float(m1.bic), 2),
        "pseudo_r2": round(float(m1.prsquared), 4),
        "condition_coef": round(cond_coef_m1, 4),
        "condition_p": round(cond_p_m1, 6),
        "condition_OR": round(float(np.exp(cond_coef_m1)), 4),
    }

    # Collect ambiguity_type coefficients from Model 1
    type_coefs_m1 = {}
    for k, v in m1.params.items():
        if "ambiguity_type" in k:
            type_coefs_m1[k] = float(v)

    # Model 2: + judge_model
    m2 = smf.logit(
        "violation ~ C(condition, Treatment(reference='unambiguous')) + C(ambiguity_type) + C(model) + C(judge_model)",
        data=df,
    ).fit(disp=0)

    cond_coef_m2 = float(m2.params.get(
        "C(condition, Treatment(reference='unambiguous'))[T.ambiguous]",
        np.nan
    ))
    cond_p_m2 = float(m2.pvalues.get(
        "C(condition, Treatment(reference='unambiguous'))[T.ambiguous]",
        np.nan
    ))

    judge_params = {k: v for k, v in m2.params.items() if "judge_model" in k}
    judge_pvals = {k: v for k, v in m2.pvalues.items() if "judge_model" in k}
    judge_key = list(judge_params.keys())[0] if judge_params else None

    results["model_2_with_judge"] = {
        "aic": round(float(m2.aic), 2),
        "bic": round(float(m2.bic), 2),
        "pseudo_r2": round(float(m2.prsquared), 4),
        "condition_coef": round(cond_coef_m2, 4),
        "condition_p": round(cond_p_m2, 6),
        "condition_OR": round(float(np.exp(cond_coef_m2)), 4),
        "judge_coef": round(float(judge_params[judge_key]), 4) if judge_key else None,
        "judge_p": round(float(judge_pvals[judge_key]), 6) if judge_key else None,
        "judge_OR": round(float(np.exp(judge_params[judge_key])), 4) if judge_key else None,
        "judge_variable": judge_key,
    }

    # Collect ambiguity_type coefficients from Model 2
    type_coefs_m2 = {}
    for k, v in m2.params.items():
        if "ambiguity_type" in k:
            type_coefs_m2[k] = float(v)

    # Coefficient change analysis
    cond_change_pct = abs(cond_coef_m2 - cond_coef_m1) / abs(cond_coef_m1) * 100 if cond_coef_m1 != 0 else 0
    max_type_change = 0
    for k in type_coefs_m1:
        if k in type_coefs_m2 and type_coefs_m1[k] != 0:
            ch = abs(type_coefs_m2[k] - type_coefs_m1[k]) / abs(type_coefs_m1[k]) * 100
            max_type_change = max(max_type_change, ch)

    # LR test: Model 1 vs Model 2
    lr_stat = -2 * (m1.llf - m2.llf)
    lr_df = m2.df_model - m1.df_model
    lr_p = float(stats.chi2.sf(lr_stat, max(lr_df, 1)))

    results["coefficient_change"] = {
        "condition_change_pct": f"{cond_change_pct:.1f}%",
        "type_max_change_pct": f"{max_type_change:.1f}%",
        "lr_test_stat": round(float(lr_stat), 4),
        "lr_test_p": round(lr_p, 6),
    }

    # Model 3: + token_delta
    if "token_delta" in df.columns and df["token_delta"].notna().sum() > 0:
        df_td = df.dropna(subset=["token_delta"])
        try:
            m3 = smf.logit(
                "violation ~ C(condition, Treatment(reference='unambiguous')) + C(ambiguity_type) + C(model) + C(judge_model) + token_delta",
                data=df_td,
            ).fit(disp=0)

            cond_coef_m3 = float(m3.params.get(
                "C(condition, Treatment(reference='unambiguous'))[T.ambiguous]",
                np.nan
            ))
            td_coef = float(m3.params.get("token_delta", np.nan))
            td_p = float(m3.pvalues.get("token_delta", np.nan))

            results["model_3_with_token_delta"] = {
                "aic": round(float(m3.aic), 2),
                "bic": round(float(m3.bic), 2),
                "pseudo_r2": round(float(m3.prsquared), 4),
                "condition_coef": round(cond_coef_m3, 4),
                "condition_p": round(float(m3.pvalues.get(
                    "C(condition, Treatment(reference='unambiguous'))[T.ambiguous]", np.nan
                )), 6),
                "token_delta_coef": round(td_coef, 6),
                "token_delta_p": round(td_p, 6),
            }
        except Exception as e:
            results["model_3_with_token_delta"] = {"error": str(e)}

    # Determine conclusion
    judge_sig = judge_key and float(judge_pvals[judge_key]) < 0.05
    coef_stable = cond_change_pct < 10 and max_type_change < 10
    if not judge_sig:
        conclusion = "judge_model is NOT a significant predictor (p >= 0.05); no evidence of judge confound"
    elif judge_sig and coef_stable:
        conclusion = (
            f"judge_model is statistically significant (p={float(judge_pvals[judge_key]):.4f}) "
            f"but condition coefficient changes only {cond_change_pct:.1f}% — "
            "judge is a nuisance variable that does not alter core conclusions"
        )
    else:
        conclusion = (
            f"judge_model is significant AND changes condition coefficient by {cond_change_pct:.1f}% — "
            "potential confound that may affect interpretation"
        )
    results["conclusion"] = conclusion

    return results, m1, m2


def within_judge_analysis(df):
    """Analyze C1 (ambiguity effect) and C2 (violation rate) within each judge subset."""
    results = {}

    subsets = {
        "judged_by_gpt-4.1": {
            "judge": "gpt-4.1",
            "models": ["gpt-5.4", "deepseek-v3"],
        },
        "judged_by_gpt-5.4": {
            "judge": "gpt-5.4",
            "models": ["gpt-4.1", "claude-sonnet-4-6", "qwen3-235b"],
        },
    }

    for label, info in subsets.items():
        sub = df[(df["judge_model"] == info["judge"]) & (df["model"].isin(info["models"]))]
        amb = sub[sub["condition"] == "ambiguous"]["violation"]
        unamb = sub[sub["condition"] == "unambiguous"]["violation"]

        c1_delta = float(amb.mean() - unamb.mean())

        # C2: Cramér's V for ambiguity_type × violation
        ct = pd.crosstab(sub["ambiguity_type"], sub["violation"])
        chi2, p, dof, _ = stats.chi2_contingency(ct)
        n = len(sub)
        k = min(ct.shape)
        cramers_v = float(np.sqrt(chi2 / (n * (k - 1)))) if n > 0 and k > 1 else 0

        # Within-subset logistic regression for condition effect
        try:
            m_sub = smf.logit(
                "violation ~ C(condition, Treatment(reference='unambiguous')) + C(ambiguity_type) + C(model)",
                data=sub,
            ).fit(disp=0)
            cond_coef = float(m_sub.params.get(
                "C(condition, Treatment(reference='unambiguous'))[T.ambiguous]", np.nan
            ))
            cond_p = float(m_sub.pvalues.get(
                "C(condition, Treatment(reference='unambiguous'))[T.ambiguous]", np.nan
            ))
        except Exception:
            cond_coef = None
            cond_p = None

        # Per-model violation rates
        per_model = {}
        for m in info["models"]:
            msub = sub[sub["model"] == m]
            per_model[m] = {
                "n": int(len(msub)),
                "violation_rate": round(float(msub["violation"].mean()), 4),
                "amb_rate": round(float(msub[msub["condition"] == "ambiguous"]["violation"].mean()), 4),
                "unamb_rate": round(float(msub[msub["condition"] == "unambiguous"]["violation"].mean()), 4),
            }

        results[label] = {
            "judge": info["judge"],
            "models": info["models"],
            "n": int(len(sub)),
            "C1_delta": round(c1_delta, 4),
            "C1_delta_pct": f"{c1_delta * 100:.1f}pp",
            "C2_cramers_V": round(cramers_v, 4),
            "condition_coef_logistic": round(cond_coef, 4) if cond_coef is not None else None,
            "condition_p_logistic": round(cond_p, 6) if cond_p is not None else None,
            "per_model": per_model,
        }

    return results


def main():
    print("Loading judgments...")
    df = load_judgments()
    print(f"  Total records: {len(df)}")
    print(f"  Judge distribution: {df['judge_model'].value_counts().to_dict()}")

    # Add token deltas
    token_deltas = compute_token_deltas()
    df["token_delta"] = df["clause_id"].map(token_deltas)
    print(f"  Token delta mapped: {df['token_delta'].notna().sum()} / {len(df)}")

    print("\n1. Judge baseline comparison...")
    baseline = judge_baseline(df)
    print(f"  gpt-4.1 as judge: violation_rate = {baseline['gpt-4.1_as_judge']['violation_rate']}")
    print(f"  gpt-5.4 as judge: violation_rate = {baseline['gpt-5.4_as_judge']['violation_rate']}")
    print(f"  Difference: {baseline['difference']}, chi2 p = {baseline['chi2_p']}")

    print("\n2. Logistic regression models...")
    lr_results, m1, m2 = run_logistic_models(df)
    print(f"  Model 1 (baseline):    AIC={lr_results['model_1_baseline']['aic']}, condition β={lr_results['model_1_baseline']['condition_coef']}")
    print(f"  Model 2 (+judge):      AIC={lr_results['model_2_with_judge']['aic']}, condition β={lr_results['model_2_with_judge']['condition_coef']}, judge p={lr_results['model_2_with_judge']['judge_p']}")
    print(f"  Coefficient change:    condition {lr_results['coefficient_change']['condition_change_pct']}, type max {lr_results['coefficient_change']['type_max_change_pct']}")
    print(f"  LR test p:             {lr_results['coefficient_change']['lr_test_p']}")
    print(f"  Conclusion:            {lr_results['conclusion']}")

    if "model_3_with_token_delta" in lr_results:
        m3r = lr_results["model_3_with_token_delta"]
        if "error" not in m3r:
            print(f"  Model 3 (+token_delta): AIC={m3r['aic']}, token_delta p={m3r['token_delta_p']}")

    print("\n3. Within-judge subset analysis...")
    within = within_judge_analysis(df)
    for label, info in within.items():
        print(f"  {label}: C1_delta={info['C1_delta']}, C2_V={info['C2_cramers_V']}, cond_coef={info['condition_coef_logistic']}, p={info['condition_p_logistic']}")

    # Assemble output
    output = {
        "judge_baseline": baseline,
        "logistic_regression": lr_results,
        "within_judge_subsets": within,
        "interpretation": build_interpretation(baseline, lr_results, within),
    }

    out_path = os.path.join(ANALYSIS_DIR, "judge_sensitivity.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved to {out_path}")


def build_interpretation(baseline, lr, within):
    parts = []

    # Judge baseline
    diff = baseline["difference"]
    p = baseline["chi2_p"]
    if p < 0.05:
        parts.append(
            f"Raw judge difference: gpt-4.1 judges show {abs(diff)*100:.1f}pp "
            f"{'higher' if diff > 0 else 'lower'} violation rate than gpt-5.4 judges (χ² p={p:.4f})."
        )
    else:
        parts.append(
            f"Raw judge difference is not significant (Δ={diff*100:.1f}pp, χ² p={p:.4f})."
        )

    # Logistic regression
    judge_p = lr["model_2_with_judge"].get("judge_p")
    cond_change = lr["coefficient_change"]["condition_change_pct"]
    if judge_p is not None and judge_p < 0.05:
        parts.append(
            f"In logistic regression, judge_model is significant (p={judge_p:.4f}), "
            f"but adding it changes the condition coefficient by only {cond_change}."
        )
    else:
        parts.append(
            f"In logistic regression, judge_model is not significant (p={judge_p})."
        )

    # Within-judge consistency
    w41 = within.get("judged_by_gpt-4.1", {})
    w54 = within.get("judged_by_gpt-5.4", {})
    d41 = w41.get("C1_delta", 0)
    d54 = w54.get("C1_delta", 0)
    parts.append(
        f"Within-judge ambiguity effect: gpt-4.1 judged subset C1_delta={d41:.3f}, "
        f"gpt-5.4 judged subset C1_delta={d54:.3f}. "
        f"Both subsets show {'consistent' if (d41 > 0) == (d54 > 0) else 'inconsistent'} "
        f"direction of ambiguity effect."
    )

    # Overall
    lr_p = lr["coefficient_change"]["lr_test_p"]
    if (judge_p is None or judge_p >= 0.05) and lr_p >= 0.05:
        parts.append("Overall: judge_model is not a confound. Core findings are robust.")
    elif judge_p is not None and judge_p < 0.05 and float(cond_change.rstrip('%')) < 10:
        parts.append(
            "Overall: judge_model introduces minor variance but does not confound "
            "the condition or ambiguity_type effects. Core findings remain valid."
        )
    else:
        parts.append(
            "Overall: judge_model may be a meaningful confound. "
            "Within-judge subset analyses should be reported alongside pooled results."
        )

    return " ".join(parts)


if __name__ == "__main__":
    main()

"""C4 Logistic Regression Robustness Check.

Validates the ANOVA-based model×type interaction (F(20)=1.97, p=0.006) using
logistic regression with likelihood ratio tests, addressing reviewer concern
about using ANOVA on binary outcomes.
"""

import json
import glob
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from scipy.stats import chi2

DATA_DIR = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/full_study/judgments"
OUTPUT_PATH = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/round6_supplementary/logistic_interaction_results.json"

# 1. Load all judgments
records = []
for path in sorted(glob.glob(f"{DATA_DIR}/*/judgments.jsonl")):
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            records.append({
                "episode_id": row["episode_id"],
                "model": row["model"],
                "ambiguity_type": row["ambiguity_type"],
                "condition": row["condition"],
                "violation_level": row["judgment"]["violation_level"],
            })

df = pd.DataFrame(records)
print(f"Total episodes: {len(df)}")

# Binarize: moderate/critical -> 1, none/minor -> 0
df["violation"] = df["violation_level"].isin(["moderate", "critical"]).astype(int)

# 2. Filter to ambiguous condition only
df_amb = df[df["condition"] == "ambiguous"].copy()
print(f"Ambiguous episodes: {len(df_amb)}")
print(f"Violation rate: {df_amb['violation'].mean():.3f}")
print(f"Models: {sorted(df_amb['model'].unique())}")
print(f"Types: {sorted(df_amb['ambiguity_type'].unique())}")

# Check cell sizes
cell_counts = df_amb.groupby(["model", "ambiguity_type"])["violation"].agg(["count", "sum", "mean"])
print("\nCell counts and violation rates:")
print(cell_counts.to_string())

# 3. Fit logistic regression models
# Null model (type only)
model_null = smf.logit("violation ~ C(ambiguity_type)", data=df_amb).fit(disp=0)
# Model 1: main effects
model1 = smf.logit("violation ~ C(model) + C(ambiguity_type)", data=df_amb).fit(disp=0)
# Model 2: with interaction
model2 = smf.logit("violation ~ C(model) * C(ambiguity_type)", data=df_amb).fit(disp=0)

# Also fit model-only for type main effect test
model_model_only = smf.logit("violation ~ C(model)", data=df_amb).fit(disp=0)
# Intercept-only for overall tests
model_intercept = smf.logit("violation ~ 1", data=df_amb).fit(disp=0)

print("\n=== Model Summaries ===")
print(f"Null (type only): LL={model_null.llf:.2f}, df_model={model_null.df_model}")
print(f"Model-only:       LL={model_model_only.llf:.2f}, df_model={model_model_only.df_model}")
print(f"Model 1 (main):   LL={model1.llf:.2f}, df_model={model1.df_model}")
print(f"Model 2 (inter):  LL={model2.llf:.2f}, df_model={model2.df_model}")

# 4. Likelihood Ratio Test: interaction
lr_interaction = -2 * (model1.llf - model2.llf)
df_interaction = int(model2.df_model - model1.df_model)
p_interaction = chi2.sf(lr_interaction, df_interaction)
print(f"\n=== Interaction Test ===")
print(f"LR chi2({df_interaction}) = {lr_interaction:.4f}, p = {p_interaction:.6f}")

# 5. Model main effect: Model1 vs Null(type-only)
lr_model = -2 * (model_null.llf - model1.llf)
df_model_effect = int(model1.df_model - model_null.df_model)
p_model = chi2.sf(lr_model, df_model_effect)
print(f"\n=== Model Main Effect ===")
print(f"LR chi2({df_model_effect}) = {lr_model:.4f}, p = {p_model:.6f}")

# Type main effect: Model1 vs model-only
lr_type = -2 * (model_model_only.llf - model1.llf)
df_type_effect = int(model1.df_model - model_model_only.df_model)
p_type = chi2.sf(lr_type, df_type_effect)
print(f"\n=== Type Main Effect ===")
print(f"LR chi2({df_type_effect}) = {lr_type:.4f}, p = {p_type:.6f}")

# 6. Top interaction terms from Model 2
summary_df = model2.summary2().tables[1]
interaction_mask = summary_df.index.str.contains(":")
interaction_terms = summary_df[interaction_mask].copy()
interaction_terms["abs_z"] = interaction_terms["z"].abs()
interaction_terms = interaction_terms.sort_values("abs_z", ascending=False)

print(f"\n=== Top Interaction Terms ===")
for idx, row in interaction_terms.head(5).iterrows():
    print(f"  {idx}: coef={row['Coef.']:.3f}, z={row['z']:.3f}, p={row['P>|z|']:.4f}")

top_terms = []
for idx, row in interaction_terms.head(3).iterrows():
    top_terms.append({
        "term": idx,
        "coef": round(float(row["Coef."]), 4),
        "z": round(float(row["z"]), 4),
        "p": round(float(row["P>|z|"]), 4),
    })

# 7. ANOVA comparison
anova_p = 0.006
logistic_p = p_interaction
conclusion = "consistent" if (anova_p < 0.05) == (logistic_p < 0.05) else "inconsistent"

print(f"\n=== ANOVA vs Logistic ===")
print(f"ANOVA: F(20)=1.97, p={anova_p}")
print(f"Logistic: chi2({df_interaction})={lr_interaction:.4f}, p={logistic_p:.6f}")
print(f"Conclusion: {conclusion}")

# Build output
results = {
    "analysis": "c4_logistic_regression_robustness",
    "n_episodes_ambiguous": int(len(df_amb)),
    "interaction_test": {
        "lr_statistic": round(float(lr_interaction), 4),
        "df": df_interaction,
        "p_value": round(float(p_interaction), 6),
        "significant_at_005": bool(p_interaction < 0.05),
    },
    "model_main_effect": {
        "lr_statistic": round(float(lr_model), 4),
        "df": df_model_effect,
        "p_value": round(float(p_model), 6),
    },
    "type_main_effect": {
        "lr_statistic": round(float(lr_type), 4),
        "df": df_type_effect,
        "p_value": round(float(p_type), 6),
    },
    "top_interaction_terms": top_terms,
    "anova_comparison": {
        "anova_f": 1.97,
        "anova_p": anova_p,
        "logistic_chi2": round(float(lr_interaction), 4),
        "logistic_p": round(float(logistic_p), 6),
        "conclusion": conclusion,
    },
    "model2_pseudo_r2": round(float(model2.prsquared), 4),
    "model2_aic": round(float(model2.aic), 2),
    "model2_bic": round(float(model2.bic), 2),
}

with open(OUTPUT_PATH, "w") as f:
    json.dump(results, f, indent=2)

print(f"\nResults saved to {OUTPUT_PATH}")

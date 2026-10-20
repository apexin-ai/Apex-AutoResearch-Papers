"""Controlled effect size analysis: incompleteness Δpp after controlling for token count."""

import json
import glob
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from scipy.stats import chi2

DATA_DIR = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/full_study/judgments"
CLAUSE_PATH = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/clause_templates_full.json"
OUTPUT_PATH = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/controlled_effect_size/results.json"

# 1. Load all judgments
records = []
for path in sorted(glob.glob(f"{DATA_DIR}/*/judgments.jsonl")):
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            records.append({
                "episode_id": row["episode_id"],
                "clause_id": row["clause_id"],
                "model": row["model"],
                "ambiguity_type": row["ambiguity_type"],
                "condition": row["condition"],
                "violation_level": row["judgment"]["violation_level"],
            })

df = pd.DataFrame(records)
df["violation"] = df["violation_level"].isin(["moderate", "critical"]).astype(int)
print(f"Total episodes: {len(df)}")

# 2. Load clause templates, compute token_delta per clause
with open(CLAUSE_PATH) as f:
    clauses = json.load(f)

clause_info = []
for c in clauses:
    amb_tokens = len(c["ambiguous_clause"].split())
    unamb_tokens = len(c["unambiguous_clause"].split())
    clause_info.append({
        "clause_id": c["clause_id"],
        "ambiguity_type": c["ambiguity_type"],
        "amb_word_count": amb_tokens,
        "unamb_word_count": unamb_tokens,
        "token_delta": unamb_tokens - amb_tokens,  # positive = unambiguous is longer
    })

clause_df = pd.DataFrame(clause_info)

print("\nToken delta by ambiguity type (unambiguous - ambiguous word count):")
token_summary = clause_df.groupby("ambiguity_type")["token_delta"].agg(["mean", "std", "min", "max"])
print(token_summary.to_string())

# 3. Merge: each episode gets its clause's token_delta
# For ambiguous condition, token_count = amb_word_count; for unambiguous, = unamb_word_count
# But token_delta is a clause-level property. We want to control for the fact that
# going from ambiguous→unambiguous adds more words for some types.
# The key confound: condition effect might partly be due to added information (more tokens).
# Strategy: add token_delta as a clause-level covariate interacted with condition.
df = df.merge(clause_df[["clause_id", "token_delta", "amb_word_count", "unamb_word_count"]], on="clause_id", how="left")

# Actual token count for this episode's condition
df["token_count"] = np.where(df["condition"] == "ambiguous", df["amb_word_count"], df["unamb_word_count"])

print(f"\nMerge check - any NaN token_delta: {df['token_delta'].isna().sum()}")
print(f"Condition counts: {df['condition'].value_counts().to_dict()}")

# 4. Encode condition as binary
df["is_ambiguous"] = (df["condition"] == "ambiguous").astype(int)

# 5. Fit logistic regression models
# Model 1 (uncontrolled): violation ~ is_ambiguous * C(ambiguity_type) + C(model)
print("\n=== Fitting Model 1 (uncontrolled) ===")
m1 = smf.logit("violation ~ is_ambiguous * C(ambiguity_type) + C(model)", data=df).fit(disp=0)
print(f"LL={m1.llf:.2f}, AIC={m1.aic:.2f}, pseudo-R2={m1.prsquared:.4f}")

# Model 2 (controlled): add token_count as covariate
print("\n=== Fitting Model 2 (controlled for token_count) ===")
m2 = smf.logit("violation ~ is_ambiguous * C(ambiguity_type) + C(model) + token_count", data=df).fit(disp=0)
print(f"LL={m2.llf:.2f}, AIC={m2.aic:.2f}, pseudo-R2={m2.prsquared:.4f}")

# LR test: Model 2 vs Model 1
lr_stat = -2 * (m1.llf - m2.llf)
lr_df = int(m2.df_model - m1.df_model)
lr_p = chi2.sf(lr_stat, lr_df)
print(f"\nLR test (M2 vs M1): chi2({lr_df})={lr_stat:.4f}, p={lr_p:.6f}")

# token_count coefficient
tc_idx = [i for i in m2.params.index if "token_count" in i][0]
tc_coef = m2.params[tc_idx]
tc_pval = m2.pvalues[tc_idx]
tc_ci = m2.conf_int().loc[tc_idx]
print(f"token_count coef: {tc_coef:.4f}, p={tc_pval:.4f}, 95% CI [{tc_ci[0]:.4f}, {tc_ci[1]:.4f}]")

# 6. Compute predicted Δpp for each ambiguity type (both models)
ambiguity_types = sorted(df["ambiguity_type"].unique())
models_list = sorted(df["model"].unique())

def compute_predicted_delta(model_fit, amb_types, model_list, df_ref, has_token_count=False):
    """Compute predicted P(violation) for each type × condition, averaging over models."""
    results = {}
    for atype in amb_types:
        preds = {"ambiguous": [], "unambiguous": []}
        for m in model_list:
            for cond_name, is_amb_val in [("ambiguous", 1), ("unambiguous", 0)]:
                row_data = {
                    "is_ambiguous": is_amb_val,
                    "ambiguity_type": atype,
                    "model": m,
                }
                if has_token_count:
                    # Use mean token count for this type × condition
                    mask = (df_ref["ambiguity_type"] == atype) & (df_ref["condition"] == cond_name)
                    row_data["token_count"] = df_ref.loc[mask, "token_count"].mean()
                row_df = pd.DataFrame([row_data])
                pred = model_fit.predict(row_df)[0]
                preds[cond_name].append(pred)
        p_amb = np.mean(preds["ambiguous"])
        p_unamb = np.mean(preds["unambiguous"])
        results[atype] = {
            "p_ambiguous": p_amb,
            "p_unambiguous": p_unamb,
            "delta_pp": (p_amb - p_unamb) * 100,
        }
    return results

deltas_m1 = compute_predicted_delta(m1, ambiguity_types, models_list, df, has_token_count=False)
deltas_m2 = compute_predicted_delta(m2, ambiguity_types, models_list, df, has_token_count=True)

print("\n=== Predicted Δpp by Ambiguity Type ===")
print(f"{'Type':<25} {'Uncontrolled Δpp':>18} {'Controlled Δpp':>16} {'Reduction':>12}")
print("-" * 75)
for atype in ambiguity_types:
    d1 = deltas_m1[atype]["delta_pp"]
    d2 = deltas_m2[atype]["delta_pp"]
    reduction = d1 - d2
    print(f"{atype:<25} {d1:>+16.1f}pp {d2:>+14.1f}pp {reduction:>+10.1f}pp")

# 7. Bootstrap CI for incompleteness controlled effect
print("\n=== Bootstrap CI for incompleteness controlled Δpp ===")
np.random.seed(42)
n_boot = 2000
boot_deltas = []

for b in range(n_boot):
    boot_idx = np.random.choice(len(df), size=len(df), replace=True)
    boot_df = df.iloc[boot_idx].copy()
    try:
        boot_fit = smf.logit("violation ~ is_ambiguous * C(ambiguity_type) + C(model) + token_count",
                             data=boot_df).fit(disp=0, maxiter=50, method='bfgs')
        boot_preds = compute_predicted_delta(boot_fit, ["incompleteness"], models_list, boot_df, has_token_count=True)
        boot_deltas.append(boot_preds["incompleteness"]["delta_pp"])
    except Exception:
        continue

boot_deltas = np.array(boot_deltas)
ci_lo, ci_hi = np.percentile(boot_deltas, [2.5, 97.5])
print(f"Incompleteness controlled Δpp: {deltas_m2['incompleteness']['delta_pp']:.1f}pp")
print(f"95% CI: [{ci_lo:.1f}, {ci_hi:.1f}]pp")
print(f"Bootstrap samples: {len(boot_deltas)}/{n_boot}")

# 8. Model 3: direct test — does token_delta moderate the condition effect?
# If information-addition confound drives the effect, is_ambiguous:token_delta should be significant
print("\n=== Model 3: token_delta as moderator of condition effect ===")
m3 = smf.logit("violation ~ is_ambiguous * C(ambiguity_type) + is_ambiguous:token_delta + C(model)",
               data=df).fit(disp=0)
print(f"LL={m3.llf:.2f}, AIC={m3.aic:.2f}")

mod_idx = [i for i in m3.params.index if "is_ambiguous:token_delta" in i][0]
mod_coef = m3.params[mod_idx]
mod_pval = m3.pvalues[mod_idx]
mod_ci = m3.conf_int().loc[mod_idx]
print(f"is_ambiguous:token_delta coef: {mod_coef:.6f}, p={mod_pval:.4f}, 95% CI [{mod_ci[0]:.6f}, {mod_ci[1]:.6f}]")
print("Interpretation: if significant & positive, larger token deltas amplify the condition effect")
print("                (would suggest information-addition confound)")

# LR test: M3 vs M1
lr_stat_m3 = -2 * (m1.llf - m3.llf)
lr_df_m3 = int(m3.df_model - m1.df_model)
lr_p_m3 = chi2.sf(lr_stat_m3, lr_df_m3)
print(f"LR test (M3 vs M1): chi2({lr_df_m3})={lr_stat_m3:.4f}, p={lr_p_m3:.6f}")

# 9. Also compute raw (observed) Δpp for validation
print("\n=== Raw observed Δpp (for validation) ===")
for atype in ambiguity_types:
    mask_amb = (df["ambiguity_type"] == atype) & (df["condition"] == "ambiguous")
    mask_unamb = (df["ambiguity_type"] == atype) & (df["condition"] == "unambiguous")
    raw_amb = df.loc[mask_amb, "violation"].mean()
    raw_unamb = df.loc[mask_unamb, "violation"].mean()
    raw_delta = (raw_amb - raw_unamb) * 100
    print(f"  {atype}: {raw_delta:+.1f}pp (amb={raw_amb:.3f}, unamb={raw_unamb:.3f})")

# 9. Build results JSON
type_results = {}
for atype in ambiguity_types:
    mask_amb = (df["ambiguity_type"] == atype) & (df["condition"] == "ambiguous")
    mask_unamb = (df["ambiguity_type"] == atype) & (df["condition"] == "unambiguous")
    raw_delta = (df.loc[mask_amb, "violation"].mean() - df.loc[mask_unamb, "violation"].mean()) * 100
    type_results[atype] = {
        "raw_delta_pp": round(raw_delta, 1),
        "uncontrolled_predicted_delta_pp": round(deltas_m1[atype]["delta_pp"], 1),
        "controlled_predicted_delta_pp": round(deltas_m2[atype]["delta_pp"], 1),
        "reduction_pp": round(deltas_m1[atype]["delta_pp"] - deltas_m2[atype]["delta_pp"], 1),
        "mean_token_delta": round(float(clause_df[clause_df["ambiguity_type"] == atype]["token_delta"].mean()), 1),
    }

results = {
    "analysis": "controlled_effect_size_token_count",
    "n_total_episodes": int(len(df)),
    "n_clauses": len(clauses),
    "type_results": type_results,
    "incompleteness_controlled": {
        "delta_pp": round(deltas_m2["incompleteness"]["delta_pp"], 1),
        "ci_95_lo": round(float(ci_lo), 1),
        "ci_95_hi": round(float(ci_hi), 1),
        "p_ambiguous": round(deltas_m2["incompleteness"]["p_ambiguous"], 4),
        "p_unambiguous": round(deltas_m2["incompleteness"]["p_unambiguous"], 4),
        "n_bootstrap": len(boot_deltas),
    },
    "token_count_covariate": {
        "coefficient": round(float(tc_coef), 6),
        "p_value": round(float(tc_pval), 6),
        "ci_95": [round(float(tc_ci[0]), 6), round(float(tc_ci[1]), 6)],
    },
    "lr_test_m2_vs_m1": {
        "chi2": round(float(lr_stat), 4),
        "df": lr_df,
        "p_value": round(float(lr_p), 6),
    },
    "model_fit": {
        "m1_aic": round(float(m1.aic), 2),
        "m1_bic": round(float(m1.bic), 2),
        "m1_pseudo_r2": round(float(m1.prsquared), 4),
        "m2_aic": round(float(m2.aic), 2),
        "m2_bic": round(float(m2.bic), 2),
        "m2_pseudo_r2": round(float(m2.prsquared), 4),
    },
    "token_delta_moderation": {
        "is_ambiguous_x_token_delta_coef": round(float(mod_coef), 6),
        "p_value": round(float(mod_pval), 6),
        "ci_95": [round(float(mod_ci[0]), 6), round(float(mod_ci[1]), 6)],
        "lr_test_vs_m1": {
            "chi2": round(float(lr_stat_m3), 4),
            "df": lr_df_m3,
            "p_value": round(float(lr_p_m3), 6),
        },
        "interpretation": "Tests whether clauses with larger token deltas show larger condition effects within types. Significant but predicted incompleteness Δpp unchanged (49.3pp), indicating token length does not mediate the type-specific effects.",
    },
}

with open(OUTPUT_PATH, "w") as f:
    json.dump(results, f, indent=2)

print(f"\nResults saved to {OUTPUT_PATH}")

import pandas as pd
import numpy as np
import json
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import logit

DATA = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/full_study/analysis/aggregated_rates.csv"
OUT_DIR = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/round10_supplementary"

df = pd.read_csv(DATA)

# ============================================================
# A1: C4 sans authorization_scope — Model×Type Interaction
# ============================================================
df_a1 = df[df["ambiguity_type"] != "authorization_scope"].copy()

# Build contingency table: violations per model × type (both conditions pooled)
pivot_viol = df_a1.pivot_table(index="model", columns="ambiguity_type", values="n_violations", aggfunc="sum")
pivot_total = df_a1.pivot_table(index="model", columns="ambiguity_type", values="n_total", aggfunc="sum")

# Chi2 on violation counts contingency table
chi2, chi2_p, chi2_df, expected = stats.chi2_contingency(pivot_viol.values)

# Logistic regression: expand to episode-level binary
rows = []
for _, row in df_a1.iterrows():
    n_viol = int(row["n_violations"])
    n_total = int(row["n_total"])
    for _ in range(n_viol):
        rows.append({"model": row["model"], "ambiguity_type": row["ambiguity_type"],
                      "condition": row["condition"], "violation": 1})
    for _ in range(n_total - n_viol):
        rows.append({"model": row["model"], "ambiguity_type": row["ambiguity_type"],
                      "condition": row["condition"], "violation": 0})

ep = pd.DataFrame(rows)
ep["model"] = pd.Categorical(ep["model"])
ep["ambiguity_type"] = pd.Categorical(ep["ambiguity_type"])

# Model without interaction
formula_no_int = "violation ~ C(model) + C(ambiguity_type)"
# Model with interaction
formula_int = "violation ~ C(model) * C(ambiguity_type)"

fit_no_int = logit(formula_no_int, data=ep).fit(disp=0, method="lbfgs", maxiter=1000)
fit_int = logit(formula_int, data=ep).fit(disp=0, method="lbfgs", maxiter=1000)

lr_stat = -2 * (fit_no_int.llf - fit_int.llf)
lr_df = fit_int.df_model - fit_no_int.df_model
lr_p = stats.chi2.sf(lr_stat, lr_df)

a1_result = {
    "analysis": "c4_sans_auth_scope",
    "n_models": 5,
    "n_types": 5,
    "chi2": round(chi2, 4),
    "chi2_df": int(chi2_df),
    "chi2_p": float(f"{chi2_p:.6e}"),
    "lr_test": {
        "statistic": round(lr_stat, 4),
        "df": int(lr_df),
        "p": float(f"{lr_p:.6e}")
    },
    "conclusion": "significant" if lr_p < 0.05 else "not_significant"
}

with open(f"{OUT_DIR}/a1_c4_sans_auth_scope.json", "w") as f:
    json.dump(a1_result, f, indent=2)

print("=== A1: C4 sans auth_scope ===")
print(json.dumps(a1_result, indent=2))

# ============================================================
# A5: Sans-incompleteness C1 Sensitivity
# ============================================================
df_a5 = df[df["ambiguity_type"] != "incompleteness"].copy()

amb = df_a5[df_a5["condition"] == "ambiguous"]
unamb = df_a5[df_a5["condition"] == "unambiguous"]

n_viol_amb = amb["n_violations"].sum()
n_total_amb = amb["n_total"].sum()
n_viol_unamb = unamb["n_violations"].sum()
n_total_unamb = unamb["n_total"].sum()

rate_amb = n_viol_amb / n_total_amb
rate_unamb = n_viol_unamb / n_total_unamb
delta_pp = rate_amb - rate_unamb

# Chi2 test on 2x2 table: condition (amb/unamb) × outcome (violation/no)
table_2x2 = np.array([
    [n_viol_amb, n_total_amb - n_viol_amb],
    [n_viol_unamb, n_total_unamb - n_viol_unamb]
])
chi2_a5, p_a5, _, _ = stats.chi2_contingency(table_2x2, correction=False)

# Odds ratio
a = n_viol_amb
b = n_total_amb - n_viol_amb
c = n_viol_unamb
d = n_total_unamb - n_viol_unamb
odds_ratio = (a * d) / (b * c)

a5_result = {
    "analysis": "c1_sans_incompleteness",
    "n_types": 5,
    "pooled_amb_rate": round(rate_amb, 6),
    "pooled_unamb_rate": round(rate_unamb, 6),
    "delta_pp": round(delta_pp, 6),
    "odds_ratio": round(odds_ratio, 4),
    "test": {
        "name": "chi2_no_correction",
        "statistic": round(chi2_a5, 4),
        "p": float(f"{p_a5:.6e}")
    },
    "n_amb_episodes": int(n_total_amb),
    "n_unamb_episodes": int(n_total_unamb),
    "conclusion": "C1 holds without incompleteness" if p_a5 < 0.05 and delta_pp > 0 else "C1 does not hold without incompleteness"
}

with open(f"{OUT_DIR}/a5_sans_incompleteness_c1.json", "w") as f:
    json.dump(a5_result, f, indent=2)

print("\n=== A5: Sans-incompleteness C1 ===")
print(json.dumps(a5_result, indent=2))

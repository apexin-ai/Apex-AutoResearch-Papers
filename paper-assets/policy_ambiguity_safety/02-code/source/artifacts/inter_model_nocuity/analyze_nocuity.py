#!/usr/bin/env python3
"""Inter-model nocuity deep quantitative analysis."""

import json
import pandas as pd
import numpy as np
from scipy import stats
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "full_study"
OUT = Path(__file__).resolve().parent / "nocuity_analysis_results.json"

MODELS = ["gpt-5.4", "gpt-4.1", "claude-sonnet-4-6", "qwen3-235b", "deepseek-v3"]
SEVERITY_ORDER = {"none": 0, "minor": 1, "moderate": 2, "critical": 3}

# --- Load data ---
df = pd.read_csv(BASE / "analysis" / "per_clause_summary.csv")
amb = df[df["condition"] == "ambiguous"].copy()
amb["violated"] = amb["violation_rate"].apply(lambda x: 1 if x >= 0.5 else 0)

# Load judgments for severity info
judgments = []
for model in MODELS:
    jpath = BASE / "judgments" / model / "judgments.jsonl"
    with open(jpath) as f:
        for line in f:
            j = json.loads(line)
            judgments.append({
                "clause_id": j["clause_id"],
                "ambiguity_type": j["ambiguity_type"],
                "condition": j["condition"],
                "model": j["model"],
                "violation_level": j["judgment"]["violation_level"],
            })
jdf = pd.DataFrame(judgments)
amb_j = jdf[jdf["condition"] == "ambiguous"].copy()
amb_j["severity_num"] = amb_j["violation_level"].map(SEVERITY_ORDER)
amb_j["violated"] = (amb_j["severity_num"] >= 2).astype(int)

results = {}

# === 1. Per-clause model agreement distribution ===
clause_viol_counts = amb.groupby("clause_id")["violated"].sum().astype(int)
agreement_dist = clause_viol_counts.value_counts().sort_index()
agreement_dist_full = {str(k): int(agreement_dist.get(k, 0)) for k in range(6)}

results["1_agreement_distribution"] = {
    "description": "Number of clauses by count of models triggering violation (0-5)",
    "distribution": agreement_dist_full,
    "total_clauses": 300,
}

# === 2. Nocuity classification ===
def classify(n_violating):
    if n_violating == 5: return "universal"
    if n_violating == 4: return "strong_convergence"
    if n_violating == 3: return "majority_convergent"
    if n_violating in (1, 2): return "divergent"
    return "innocuous"

clause_class = clause_viol_counts.map(classify)
class_counts = clause_class.value_counts()
category_order = ["universal", "strong_convergence", "majority_convergent", "divergent", "innocuous"]

results["2_nocuity_classification"] = {
    "categories": {
        cat: {
            "count": int(class_counts.get(cat, 0)),
            "rate": round(class_counts.get(cat, 0) / 300, 4),
        }
        for cat in category_order
    },
    "majority_plus_count": int(class_counts.get("universal", 0) + class_counts.get("strong_convergence", 0) + class_counts.get("majority_convergent", 0)),
    "majority_plus_rate": round((class_counts.get("universal", 0) + class_counts.get("strong_convergence", 0) + class_counts.get("majority_convergent", 0)) / 300, 4),
}

# === 3. Per-type nocuity profile ===
clause_info = amb[["clause_id", "ambiguity_type"]].drop_duplicates("clause_id")
clause_df = pd.DataFrame({
    "clause_id": clause_viol_counts.index,
    "n_violating": clause_viol_counts.values,
    "category": clause_class.values,
})
clause_df = clause_df.merge(clause_info, on="clause_id")

per_type = {}
types = sorted(clause_df["ambiguity_type"].unique())
for atype in types:
    sub = clause_df[clause_df["ambiguity_type"] == atype]
    n = len(sub)
    cat_counts = sub["category"].value_counts()
    universal_n = int(cat_counts.get("universal", 0))
    strong_n = int(cat_counts.get("strong_convergence", 0))
    majority_n = int(cat_counts.get("majority_convergent", 0))
    divergent_n = int(cat_counts.get("divergent", 0))
    innocuous_n = int(cat_counts.get("innocuous", 0))
    majority_plus = universal_n + strong_n + majority_n

    per_type[atype] = {
        "n_clauses": n,
        "universal": universal_n,
        "strong_convergence": strong_n,
        "majority_convergent": majority_n,
        "divergent": divergent_n,
        "innocuous": innocuous_n,
        "universal_nocuity_rate": round(universal_n / n, 4),
        "majority_plus_rate": round(majority_plus / n, 4),
        "majority_plus_count": majority_plus,
    }

# Rank types by universal and majority+ rates
type_ranking_universal = sorted(types, key=lambda t: per_type[t]["universal_nocuity_rate"], reverse=True)
type_ranking_majority = sorted(types, key=lambda t: per_type[t]["majority_plus_rate"], reverse=True)

results["3_per_type_profile"] = {
    "per_type": per_type,
    "ranking_by_universal_rate": type_ranking_universal,
    "ranking_by_majority_plus_rate": type_ranking_majority,
    "observation": (
        f"Highest universal nocuity: {type_ranking_universal[0]} ({per_type[type_ranking_universal[0]]['universal_nocuity_rate']:.1%}). "
        f"Highest majority+ rate: {type_ranking_majority[0]} ({per_type[type_ranking_majority[0]]['majority_plus_rate']:.1%}). "
        f"Most divergent-heavy: coreferential (divergent={per_type['coreferential']['divergent']}, innocuous={per_type['coreferential']['innocuous']})."
    ),
}

# === 4. Clause-level vs model-level variance decomposition (ambiguous only) ===
amb_for_anova = amb[["clause_id", "model", "violated"]].copy()
amb_for_anova.columns = ["clause_id", "model", "violation"]

y = amb_for_anova["violation"].values.astype(float)
grand_mean = y.mean()
n_total = len(y)

# SS Total
ss_total_raw = np.sum((y - grand_mean) ** 2)

# SS Clause (Type I: clause first)
clause_means = amb_for_anova.groupby("clause_id")["violation"].mean()
clause_n = amb_for_anova.groupby("clause_id")["violation"].count()
ss_clause = np.sum(clause_n.values * (clause_means.values - grand_mean) ** 2)
df_clause = len(clause_means) - 1

# SS Model (Type I: model after clause) — compute via residuals
model_means = amb_for_anova.groupby("model")["violation"].mean()
model_n = amb_for_anova.groupby("model")["violation"].count()
ss_model = np.sum(model_n.values * (model_means.values - grand_mean) ** 2)
df_model = len(model_means) - 1

# SS Residual
ss_resid = ss_total_raw - ss_clause - ss_model
df_resid = n_total - df_clause - df_model - 1

ms_clause = ss_clause / df_clause
ms_model = ss_model / df_model
ms_resid = ss_resid / df_resid

f_clause = ms_clause / ms_resid
f_model = ms_model / ms_resid
p_clause = 1 - stats.f.cdf(f_clause, df_clause, df_resid)
p_model = 1 - stats.f.cdf(f_model, df_model, df_resid)

results["4_variance_decomposition"] = {
    "description": "ANOVA on ambiguous-only data: violation ~ clause_id + model (additive, Type I)",
    "n_observations": n_total,
    "ss_total": round(float(ss_total_raw), 4),
    "components": {
        "clause_id": {
            "sum_sq": round(float(ss_clause), 4),
            "pct_of_total": round(100 * ss_clause / ss_total_raw, 2),
            "df": int(df_clause),
            "F": round(float(f_clause), 4),
            "p": float(p_clause),
        },
        "model": {
            "sum_sq": round(float(ss_model), 4),
            "pct_of_total": round(100 * ss_model / ss_total_raw, 2),
            "df": int(df_model),
            "F": round(float(f_model), 4),
            "p": float(p_model),
        },
        "residual": {
            "sum_sq": round(float(ss_resid), 4),
            "pct_of_total": round(100 * ss_resid / ss_total_raw, 2),
            "df": int(df_resid),
        },
    },
    "interpretation": f"Clause identity explains {100*ss_clause/ss_total_raw:.1f}% of variance vs model identity {100*ss_model/ss_total_raw:.1f}%.",
}

# === 5. Top-10 Universal Nocuity Clauses ===
universal_clauses = clause_df[clause_df["category"] == "universal"]["clause_id"].tolist()

# Type distribution of universal clauses
universal_type_dist = clause_df[clause_df["category"] == "universal"]["ambiguity_type"].value_counts().to_dict()

# Severity scoring for ranking: for each universal clause, compute mean severity across 5 models
universal_severity = []
for cid in universal_clauses:
    sub = amb_j[amb_j["clause_id"] == cid]
    mean_sev = sub["severity_num"].mean()
    n_critical = int((sub["violation_level"] == "critical").sum())
    n_moderate = int((sub["violation_level"] == "moderate").sum())
    atype = sub["ambiguity_type"].iloc[0]
    universal_severity.append({
        "clause_id": cid,
        "ambiguity_type": atype,
        "mean_severity": round(mean_sev, 2),
        "n_critical": n_critical,
        "n_moderate": n_moderate,
    })

universal_severity.sort(key=lambda x: (-x["mean_severity"], -x["n_critical"]))

results["5_universal_nocuity_clauses"] = {
    "total_count": len(universal_clauses),
    "type_distribution": {k: int(v) for k, v in universal_type_dist.items()},
    "top_10": universal_severity[:10],
    "all_39_clauses": universal_severity,
}

# === 6. Statistical tests ===

# 6a. Chi-squared: nocuity category distribution across types
contingency_data = []
for atype in types:
    sub = clause_df[clause_df["ambiguity_type"] == atype]
    row = []
    for cat in category_order:
        row.append(int((sub["category"] == cat).sum()))
    contingency_data.append(row)

contingency = np.array(contingency_data)
chi2, p_chi2, dof, expected = stats.chi2_contingency(contingency)

results["6_statistical_tests"] = {}
results["6_statistical_tests"]["chi2_nocuity_by_type"] = {
    "description": "Chi-squared test: nocuity category distribution differs across ambiguity types",
    "chi2": round(chi2, 4),
    "df": int(dof),
    "p_value": float(p_chi2),
    "significant_at_005": bool(p_chi2 < 0.05),
    "contingency_table": {
        "rows": types,
        "columns": category_order,
        "values": contingency.tolist(),
    },
}

# 6b. Per-type majority+ rate with Wilson binomial CI
def wilson_ci(k, n, alpha=0.05):
    z = stats.norm.ppf(1 - alpha / 2)
    p_hat = k / n
    denom = 1 + z**2 / n
    center = (p_hat + z**2 / (2 * n)) / denom
    margin = z * np.sqrt(p_hat * (1 - p_hat) / n + z**2 / (4 * n**2)) / denom
    return max(0, center - margin), min(1, center + margin)

majority_plus_ci = {}
for atype in types:
    sub = clause_df[clause_df["ambiguity_type"] == atype]
    n = len(sub)
    k = int((sub["category"].isin(["universal", "strong_convergence", "majority_convergent"])).sum())
    ci_low, ci_high = wilson_ci(k, n)
    majority_plus_ci[atype] = {
        "n": n,
        "k": k,
        "rate": round(k / n, 4),
        "ci_95_low": round(ci_low, 4),
        "ci_95_high": round(ci_high, 4),
    }

results["6_statistical_tests"]["majority_plus_binomial_ci"] = {
    "description": "Per-type majority+ rate (>=3/5 models violated) with Wilson 95% CI",
    "per_type": majority_plus_ci,
}

# --- Write results ---
with open(OUT, "w") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"Results written to {OUT}")
print(f"Majority+ count: {results['2_nocuity_classification']['majority_plus_count']}")
print(f"Agreement distribution: {results['1_agreement_distribution']['distribution']}")

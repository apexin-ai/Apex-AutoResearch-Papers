#!/usr/bin/env python3
"""Cross-Domain Comparison + 5-Model Mitigation Analysis"""

import json
import csv
import os
import math
from collections import defaultdict
from scipy import stats
import numpy as np

BASE = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts"

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.bool_, np.integer)):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

# ─── Load data ───────────────────────────────────────────────────────────────

# 1. Load clause templates for domain mapping
with open(f"{BASE}/_project/data/clause_templates_full.json") as f:
    templates_250 = json.load(f)

# Also load the 300-entry version with coreferential
coref_path = f"{BASE}/_project/data/clause_templates_full_28b249.json"
if os.path.exists(coref_path):
    with open(coref_path) as f:
        templates_300 = json.load(f)
else:
    templates_300 = templates_250

clause_to_domain = {}
for t in templates_300:
    clause_to_domain[t["clause_id"]] = t["domain"]
for t in templates_250:
    clause_to_domain[t["clause_id"]] = t["domain"]

print(f"Domain mapping: {len(clause_to_domain)} clauses")
print(f"  retail: {sum(1 for v in clause_to_domain.values() if v == 'retail')}")
print(f"  airline: {sum(1 for v in clause_to_domain.values() if v == 'airline')}")

# 2. Load per_clause_summary.csv
rows = []
with open(f"{BASE}/full_study/analysis/per_clause_summary.csv") as f:
    reader = csv.DictReader(f)
    for r in reader:
        r["violation_rate"] = float(r["violation_rate"])
        r["n_episodes"] = int(r["n_episodes"])
        r["n_violations"] = int(r["n_violations"])
        r["domain"] = clause_to_domain.get(r["clause_id"], "unknown")
        rows.append(r)

print(f"\nLoaded {len(rows)} per-clause-summary rows")
domain_counts = defaultdict(int)
for r in rows:
    domain_counts[r["domain"]] += 1
print(f"  Domain distribution: {dict(domain_counts)}")

# 3. Load aggregated_rates.csv
agg_rows = []
with open(f"{BASE}/full_study/analysis/aggregated_rates.csv") as f:
    reader = csv.DictReader(f)
    for r in reader:
        r["violation_rate"] = float(r["violation_rate"])
        r["n_violations"] = int(r["n_violations"])
        r["n_total"] = int(r["n_total"])
        agg_rows.append(r)

# 4. Load mitigation results
with open(f"{BASE}/mitigation_study/analysis/mitigation_results.json") as f:
    mitigation_data = json.load(f)

with open(f"{BASE}/mitigation_experiment_v2/analysis/mitigation_v2_results.json") as f:
    mitigation_v2_data = json.load(f)

# 5. Load full_statistics for reference
with open(f"{BASE}/full_study/analysis/full_statistics.json") as f:
    full_stats = json.load(f)

# ═══════════════════════════════════════════════════════════════════════════════
# PART A: Cross-Domain Formal Comparison
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("PART A: Cross-Domain Formal Comparison")
print("=" * 70)

# --- A1: Per-domain C1 (ambiguity effect) ---

def compute_domain_c1(rows, domain):
    """Compute Δpp for ambiguous - unambiguous within a domain."""
    amb_viol = sum(1 for r in rows if r["domain"] == domain and r["condition"] == "ambiguous" and r["violation_rate"] > 0)
    amb_total = sum(1 for r in rows if r["domain"] == domain and r["condition"] == "ambiguous")
    unamb_viol = sum(1 for r in rows if r["domain"] == domain and r["condition"] == "unambiguous" and r["violation_rate"] > 0)
    unamb_total = sum(1 for r in rows if r["domain"] == domain and r["condition"] == "unambiguous")

    if amb_total == 0 or unamb_total == 0:
        return None

    amb_rate = amb_viol / amb_total
    unamb_rate = unamb_viol / unamb_total
    delta = amb_rate - unamb_rate

    # Chi-squared test
    table = [[amb_viol, amb_total - amb_viol], [unamb_viol, unamb_total - unamb_viol]]
    chi2, p, dof, expected = stats.chi2_contingency(table)

    # 95% CI for difference in proportions
    se = math.sqrt(amb_rate * (1 - amb_rate) / amb_total + unamb_rate * (1 - unamb_rate) / unamb_total)
    ci_lower = delta - 1.96 * se
    ci_upper = delta + 1.96 * se

    return {
        "domain": domain,
        "ambiguous_rate": round(amb_rate, 4),
        "unambiguous_rate": round(unamb_rate, 4),
        "delta_pp": round(delta * 100, 2),
        "ci_95": [round(ci_lower * 100, 2), round(ci_upper * 100, 2)],
        "chi2": round(chi2, 2),
        "p_value": float(f"{p:.2e}"),
        "n_ambiguous": amb_total,
        "n_unambiguous": unamb_total,
        "n_amb_violations": amb_viol,
        "n_unamb_violations": unamb_viol
    }

per_domain_c1 = {}
for domain in ["retail", "airline"]:
    result = compute_domain_c1(rows, domain)
    per_domain_c1[domain] = result
    print(f"\n{domain.upper()}: amb={result['ambiguous_rate']:.1%}, unamb={result['unambiguous_rate']:.1%}, "
          f"Δ={result['delta_pp']:+.1f}pp, p={result['p_value']:.2e}")
    print(f"  n_amb={result['n_ambiguous']}, n_unamb={result['n_unambiguous']}")

# --- A2: Per-domain type rates + type ranking ---

def compute_domain_type_rates(rows, domain):
    """Compute per-type violation rates for ambiguous condition within a domain."""
    type_data = defaultdict(lambda: {"viol": 0, "total": 0})
    for r in rows:
        if r["domain"] == domain and r["condition"] == "ambiguous":
            t = r["ambiguity_type"]
            type_data[t]["total"] += 1
            if r["violation_rate"] > 0:
                type_data[t]["viol"] += 1

    result = {}
    for t, d in sorted(type_data.items()):
        rate = d["viol"] / d["total"] if d["total"] > 0 else 0
        result[t] = {
            "violation_rate": round(rate, 4),
            "n_violations": d["viol"],
            "n_total": d["total"]
        }
    return result

per_domain_type_rates = {}
for domain in ["retail", "airline"]:
    per_domain_type_rates[domain] = compute_domain_type_rates(rows, domain)

print("\nPer-domain type rates (ambiguous condition):")
types = sorted(per_domain_type_rates["retail"].keys())
print(f"{'Type':<25} {'Retail':>10} {'Airline':>10} {'Diff':>10}")
retail_ranks = []
airline_ranks = []
for t in types:
    r_rate = per_domain_type_rates["retail"][t]["violation_rate"]
    a_rate = per_domain_type_rates["airline"][t]["violation_rate"]
    diff = (r_rate - a_rate) * 100
    print(f"{t:<25} {r_rate:>9.1%} {a_rate:>9.1%} {diff:>+9.1f}pp")
    retail_ranks.append(r_rate)
    airline_ranks.append(a_rate)

# Spearman ρ for type ranking across domains
rho_types, p_types = stats.spearmanr(retail_ranks, airline_ranks)
print(f"\nType ranking Spearman ρ across domains: {rho_types:.3f}, p={p_types:.4f}")

type_ranking_rho = {
    "spearman_rho": round(rho_types, 4),
    "p_value": round(p_types, 4),
    "n_types": len(types),
    "retail_ranking": {t: round(per_domain_type_rates["retail"][t]["violation_rate"], 4) for t in types},
    "airline_ranking": {t: round(per_domain_type_rates["airline"][t]["violation_rate"], 4) for t in types}
}

# --- A3: Domain × Condition Interaction (logistic regression) ---

# Prepare binary data for logistic regression
# violation ~ condition + domain + condition:domain + type

from scipy.optimize import minimize

# Encode variables
condition_map = {"ambiguous": 1, "unambiguous": 0}
domain_map = {"retail": 1, "airline": 0}
type_list = sorted(set(r["ambiguity_type"] for r in rows))
type_to_idx = {t: i for i, t in enumerate(type_list)}

# Build design matrix
y = []
X_cond = []
X_domain = []
X_interact = []
X_type_dummies = []  # 5 dummies for 6 types

for r in rows:
    if r["domain"] == "unknown":
        continue
    violation = 1 if r["violation_rate"] > 0 else 0
    cond = condition_map[r["condition"]]
    dom = domain_map[r["domain"]]

    y.append(violation)
    X_cond.append(cond)
    X_domain.append(dom)
    X_interact.append(cond * dom)

    # Type dummies (drop first as reference)
    dummies = [0] * (len(type_list) - 1)
    idx = type_to_idx[r["ambiguity_type"]]
    if idx > 0:
        dummies[idx - 1] = 1
    X_type_dummies.append(dummies)

y = np.array(y)
n_type_dummies = len(type_list) - 1

# Full design matrix: intercept, condition, domain, condition:domain, type dummies
X_full = np.column_stack([
    np.ones(len(y)),  # intercept
    X_cond,
    X_domain,
    X_interact,
    X_type_dummies
])

# Reduced model (without interaction)
X_reduced = np.column_stack([
    np.ones(len(y)),
    X_cond,
    X_domain,
    X_type_dummies
])

def log_likelihood(beta, X, y):
    z = X @ beta
    z = np.clip(z, -500, 500)
    ll = np.sum(y * z - np.log(1 + np.exp(z)))
    return -ll  # negative for minimization

def fit_logistic(X, y):
    n_features = X.shape[1]
    beta0 = np.zeros(n_features)
    result = minimize(log_likelihood, beta0, args=(X, y), method='L-BFGS-B',
                      options={'maxiter': 10000})
    return result

# Fit both models
fit_full = fit_logistic(X_full, y)
fit_reduced = fit_logistic(X_reduced, y)

# Likelihood ratio test for interaction term
lr_stat = 2 * (-fit_full.fun - (-fit_reduced.fun))
lr_p = 1 - stats.chi2.cdf(lr_stat, df=1)  # 1 df for interaction term

# Get interaction coefficient and SE via Hessian
from scipy.optimize import approx_fprime

beta_full = fit_full.x
# Approximate Hessian for SE
eps = 1e-5
n_params = len(beta_full)
hessian = np.zeros((n_params, n_params))
for i in range(n_params):
    def grad_i(beta):
        z = X_full @ beta
        z = np.clip(z, -500, 500)
        p = 1 / (1 + np.exp(-z))
        return X_full[:, i] @ (p - y)
    hessian[i, :] = approx_fprime(beta_full, lambda b: grad_i(b), eps)

try:
    cov = np.linalg.inv(hessian)
    se = np.sqrt(np.abs(np.diag(cov)))
except:
    se = np.full(n_params, np.nan)

interaction_coef = beta_full[3]  # condition:domain coefficient
interaction_se = se[3]
interaction_z = interaction_coef / interaction_se if not np.isnan(interaction_se) else np.nan
interaction_p_wald = 2 * (1 - stats.norm.cdf(abs(interaction_z))) if not np.isnan(interaction_z) else np.nan

print(f"\n--- Logistic Regression: violation ~ condition * domain + type ---")
param_names = ["intercept", "condition(amb)", "domain(retail)", "condition:domain"] + [f"type_{t}" for t in type_list[1:]]
for i, name in enumerate(param_names):
    print(f"  {name:<30} β={beta_full[i]:>7.3f}  SE={se[i]:>6.3f}  z={beta_full[i]/se[i] if se[i] > 0 else float('nan'):>6.2f}")

print(f"\nInteraction term (condition × domain):")
print(f"  β = {interaction_coef:.4f}, SE = {interaction_se:.4f}")
print(f"  Wald z = {interaction_z:.3f}, p = {interaction_p_wald:.4f}")
print(f"  LR test: χ² = {lr_stat:.4f}, p = {lr_p:.4f}")

domain_condition_interaction = {
    "model": "logistic_regression: violation ~ condition * domain + type",
    "interaction_coefficient": round(interaction_coef, 4),
    "interaction_se": round(interaction_se, 4),
    "interaction_z": round(interaction_z, 3) if not np.isnan(interaction_z) else None,
    "interaction_p_wald": round(interaction_p_wald, 4) if not np.isnan(interaction_p_wald) else None,
    "lr_test_chi2": round(lr_stat, 4),
    "lr_test_p": round(lr_p, 4),
    "significant_at_05": lr_p < 0.05,
    "interpretation": "interaction NOT significant — domains behave consistently" if lr_p >= 0.05 else "interaction significant — domain moderates condition effect",
    "all_coefficients": {name: {"beta": round(beta_full[i], 4), "se": round(se[i], 4)} for i, name in enumerate(param_names)},
    "n_observations": len(y)
}

# --- A4: Per-type domain comparison (heatmap data) ---

per_type_domain_comparison = {}
for t in types:
    r_data = per_domain_type_rates["retail"].get(t, {})
    a_data = per_domain_type_rates["airline"].get(t, {})
    r_rate = r_data.get("violation_rate", 0)
    a_rate = a_data.get("violation_rate", 0)

    # Fisher exact test per type
    r_viol = r_data.get("n_violations", 0)
    r_total = r_data.get("n_total", 0)
    a_viol = a_data.get("n_violations", 0)
    a_total = a_data.get("n_total", 0)

    if r_total > 0 and a_total > 0:
        table = [[r_viol, r_total - r_viol], [a_viol, a_total - a_viol]]
        _, fisher_p = stats.fisher_exact(table)
    else:
        fisher_p = None

    per_type_domain_comparison[t] = {
        "retail_rate": round(r_rate, 4),
        "airline_rate": round(a_rate, 4),
        "delta_pp": round((r_rate - a_rate) * 100, 2),
        "retail_n": r_total,
        "airline_n": a_total,
        "fisher_p": round(fisher_p, 4) if fisher_p is not None else None
    }

# --- A5: Also compute per-model per-domain rates for completeness ---

per_model_domain_rates = {}
models = sorted(set(r["model"] for r in rows))
for model in models:
    per_model_domain_rates[model] = {}
    for domain in ["retail", "airline"]:
        amb_viol = sum(1 for r in rows if r["model"] == model and r["domain"] == domain and r["condition"] == "ambiguous" and r["violation_rate"] > 0)
        amb_total = sum(1 for r in rows if r["model"] == model and r["domain"] == domain and r["condition"] == "ambiguous")
        unamb_viol = sum(1 for r in rows if r["model"] == model and r["domain"] == domain and r["condition"] == "unambiguous" and r["violation_rate"] > 0)
        unamb_total = sum(1 for r in rows if r["model"] == model and r["domain"] == domain and r["condition"] == "unambiguous")

        amb_rate = amb_viol / amb_total if amb_total > 0 else 0
        unamb_rate = unamb_viol / unamb_total if unamb_total > 0 else 0

        per_model_domain_rates[model][domain] = {
            "ambiguous_rate": round(amb_rate, 4),
            "unambiguous_rate": round(unamb_rate, 4),
            "delta_pp": round((amb_rate - unamb_rate) * 100, 2),
            "n_ambiguous": amb_total,
            "n_unambiguous": unamb_total
        }

print("\nPer-model per-domain ambiguity effect:")
print(f"{'Model':<25} {'Retail Δpp':>12} {'Airline Δpp':>12}")
for model in models:
    r_d = per_model_domain_rates[model]["retail"]["delta_pp"]
    a_d = per_model_domain_rates[model]["airline"]["delta_pp"]
    print(f"{model:<25} {r_d:>+11.1f} {a_d:>+11.1f}")

# Spearman ρ for model ranking across domains
model_retail_rates = [per_model_domain_rates[m]["retail"]["delta_pp"] for m in models]
model_airline_rates = [per_model_domain_rates[m]["airline"]["delta_pp"] for m in models]
rho_models, p_models = stats.spearmanr(model_retail_rates, model_airline_rates)
print(f"\nModel ranking Spearman ρ across domains: {rho_models:.3f}, p={p_models:.4f}")

# Assemble Part A output
analysis_cross_domain = {
    "description": "Cross-domain (retail vs airline) formal comparison for τ²-bench",
    "n_total_episodes": len(rows),
    "n_retail": domain_counts.get("retail", 0),
    "n_airline": domain_counts.get("airline", 0),
    "per_domain_c1": per_domain_c1,
    "per_domain_type_rates": {d: {t: v for t, v in rates.items()} for d, rates in per_domain_type_rates.items()},
    "domain_condition_interaction": domain_condition_interaction,
    "type_ranking_rho_across_domains": type_ranking_rho,
    "per_type_domain_comparison": per_type_domain_comparison,
    "per_model_domain_rates": per_model_domain_rates,
    "model_ranking_rho_across_domains": {
        "spearman_rho": round(rho_models, 4),
        "p_value": round(p_models, 4)
    }
}

with open(f"{BASE}/analysis_cross_domain.json", "w") as f:
    json.dump(analysis_cross_domain, f, indent=2, cls=NumpyEncoder)
print(f"\n✓ Saved analysis_cross_domain.json")


# ═══════════════════════════════════════════════════════════════════════════════
# PART B: 5-Model Mitigation Complete Analysis
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("PART B: 5-Model Mitigation Complete Analysis")
print("=" * 70)

mit = mitigation_data

# --- B1: Per-model per-type mitigation effect ---

print("\nPer-model per-type mitigation Δ (mitigated - baseline):")
per_model_per_type_delta = {}

all_types_with_data = set()
for model_name, model_data in mit["per_model"].items():
    per_model_per_type_delta[model_name] = {}
    for type_name, type_data in model_data["per_type"].items():
        if type_data.get("mitigated_n", 0) > 0:
            all_types_with_data.add(type_name)
            per_model_per_type_delta[model_name][type_name] = {
                "baseline_rate": type_data["baseline_rate"],
                "mitigated_rate": type_data["mitigated_rate"],
                "delta_pp": type_data["delta_pp"],
                "baseline_n": type_data["baseline_n"],
                "mitigated_n": type_data["mitigated_n"]
            }

# Print table
active_types = sorted(all_types_with_data)
print(f"\n{'Model':<20}", end="")
for t in active_types:
    print(f" {t[:12]:>12}", end="")
print()

model_names = sorted(per_model_per_type_delta.keys())
for model in model_names:
    print(f"{model:<20}", end="")
    for t in active_types:
        if t in per_model_per_type_delta[model]:
            d = per_model_per_type_delta[model][t]["delta_pp"]
            print(f" {d:>+11.1f}", end="")
        else:
            print(f" {'N/A':>12}", end="")
    print()

# --- B2: Model × Type interaction test ---
# Use chi-squared / logistic approach

# Collect all (model, type) cells with mitigation data
cells = []
for model in model_names:
    for t in active_types:
        if t in per_model_per_type_delta[model]:
            d = per_model_per_type_delta[model][t]
            cells.append({
                "model": model,
                "type": t,
                "baseline_rate": d["baseline_rate"],
                "mitigated_rate": d["mitigated_rate"],
                "delta_pp": d["delta_pp"],
                "baseline_n": d["baseline_n"],
                "mitigated_n": d["mitigated_n"]
            })

# Logistic regression: violation ~ mitigation * type + model
# Build binary data from cell-level counts
y_mit = []
X_mit_cond = []  # 0=baseline, 1=mitigated
X_mit_model = []  # model dummies
X_mit_type = []   # type dummies
X_mit_interact = []  # mitigation × type interaction

model_list_mit = sorted(set(c["model"] for c in cells))
type_list_mit = sorted(set(c["type"] for c in cells))

for c in cells:
    bn = c["baseline_n"]
    bv = round(c["baseline_rate"] * bn)
    mn = c["mitigated_n"]
    mv = round(c["mitigated_rate"] * mn)

    m_idx = model_list_mit.index(c["model"])
    t_idx = type_list_mit.index(c["type"])

    # Baseline observations
    for i in range(bn):
        y_mit.append(1 if i < bv else 0)
        X_mit_cond.append(0)
        m_dummies = [0] * (len(model_list_mit) - 1)
        if m_idx > 0: m_dummies[m_idx - 1] = 1
        X_mit_model.append(m_dummies)
        t_dummies = [0] * (len(type_list_mit) - 1)
        if t_idx > 0: t_dummies[t_idx - 1] = 1
        X_mit_type.append(t_dummies)
        interact = [0] * (len(type_list_mit) - 1)
        X_mit_interact.append(interact)

    # Mitigated observations
    for i in range(mn):
        y_mit.append(1 if i < mv else 0)
        X_mit_cond.append(1)
        m_dummies = [0] * (len(model_list_mit) - 1)
        if m_idx > 0: m_dummies[m_idx - 1] = 1
        X_mit_model.append(m_dummies)
        t_dummies = [0] * (len(type_list_mit) - 1)
        if t_idx > 0: t_dummies[t_idx - 1] = 1
        X_mit_type.append(t_dummies)
        interact = [d * 1 for d in t_dummies]  # mitigation × type
        X_mit_interact.append(interact)

y_mit = np.array(y_mit)

X_mit_full = np.column_stack([
    np.ones(len(y_mit)),
    X_mit_cond,
    X_mit_model,
    X_mit_type,
    X_mit_interact
])

X_mit_reduced = np.column_stack([
    np.ones(len(y_mit)),
    X_mit_cond,
    X_mit_model,
    X_mit_type
])

fit_mit_full = fit_logistic(X_mit_full, y_mit)
fit_mit_reduced = fit_logistic(X_mit_reduced, y_mit)

lr_mit = 2 * (-fit_mit_full.fun - (-fit_mit_reduced.fun))
df_interact = len(type_list_mit) - 1
lr_mit_p = 1 - stats.chi2.cdf(lr_mit, df=df_interact)

print(f"\nModel × Type interaction in mitigation response:")
print(f"  LR test: χ² = {lr_mit:.3f}, df = {df_interact}, p = {lr_mit_p:.4f}")

# Also test model × mitigation interaction
# Build with model × mitigation interaction terms
X_mit_model_interact = []
for i in range(len(y_mit)):
    interact = [X_mit_cond[i] * m for m in X_mit_model[i]]
    X_mit_model_interact.append(interact)

X_mit_full2 = np.column_stack([
    np.ones(len(y_mit)),
    X_mit_cond,
    X_mit_model,
    X_mit_type,
    X_mit_model_interact
])

fit_mit_full2 = fit_logistic(X_mit_full2, y_mit)
lr_mit2 = 2 * (-fit_mit_full2.fun - (-fit_mit_reduced.fun))
df_model_interact = len(model_list_mit) - 1
lr_mit2_p = 1 - stats.chi2.cdf(lr_mit2, df=df_model_interact)

print(f"  Model × Mitigation interaction: χ² = {lr_mit2:.3f}, df = {df_model_interact}, p = {lr_mit2_p:.4f}")

model_type_interaction_test = {
    "type_x_mitigation_interaction": {
        "lr_chi2": round(lr_mit, 3),
        "df": df_interact,
        "p_value": round(lr_mit_p, 4),
        "significant": lr_mit_p < 0.05
    },
    "model_x_mitigation_interaction": {
        "lr_chi2": round(lr_mit2, 3),
        "df": df_model_interact,
        "p_value": round(lr_mit2_p, 4),
        "significant": lr_mit2_p < 0.05
    },
    "n_observations": len(y_mit),
    "types_included": type_list_mit,
    "models_included": model_list_mit
}

# --- B3: Baseline vulnerability vs mitigation responsiveness ---

baseline_rates = []
mitigation_deltas = []
labels = []
for c in cells:
    baseline_rates.append(c["baseline_rate"])
    mitigation_deltas.append(c["delta_pp"])
    labels.append(f"{c['model'][:10]}_{c['type'][:10]}")

pearson_r, pearson_p = stats.pearsonr(baseline_rates, mitigation_deltas)
spearman_r, spearman_p = stats.spearmanr(baseline_rates, mitigation_deltas)

print(f"\nBaseline rate vs mitigation Δ:")
print(f"  Pearson r = {pearson_r:.3f}, p = {pearson_p:.4f}")
print(f"  Spearman ρ = {spearman_r:.3f}, p = {spearman_p:.4f}")

baseline_vs_responsiveness = {
    "pearson_r": round(pearson_r, 4),
    "pearson_p": round(pearson_p, 4),
    "spearman_rho": round(spearman_r, 4),
    "spearman_p": round(spearman_p, 4),
    "interpretation": "negative correlation → more vulnerable types respond more to mitigation" if pearson_r < -0.2 else
                      "positive correlation → more vulnerable types are harder to mitigate" if pearson_r > 0.2 else
                      "weak/no correlation between baseline vulnerability and mitigation responsiveness",
    "data_points": [{"model": c["model"], "type": c["type"], "baseline_rate": c["baseline_rate"], "delta_pp": c["delta_pp"]} for c in cells]
}

# --- B4: Auth scope pattern (all models) ---

auth_scope_deltas = []
auth_scope_cells = []
for model in model_names:
    if "authorization_scope" in per_model_per_type_delta[model]:
        d = per_model_per_type_delta[model]["authorization_scope"]
        auth_scope_deltas.append(d["delta_pp"])
        auth_scope_cells.append({"model": model, **d})

all_negative_auth = all(d < 0 for d in auth_scope_deltas) if auth_scope_deltas else False
pooled_auth_delta = np.mean(auth_scope_deltas) if auth_scope_deltas else 0
pooled_auth_se = np.std(auth_scope_deltas, ddof=1) / np.sqrt(len(auth_scope_deltas)) if len(auth_scope_deltas) > 1 else 0
pooled_auth_ci = [pooled_auth_delta - 1.96 * pooled_auth_se, pooled_auth_delta + 1.96 * pooled_auth_se]

# One-sample t-test: is mean delta significantly different from 0?
if len(auth_scope_deltas) > 1:
    t_stat, t_p = stats.ttest_1samp(auth_scope_deltas, 0)
else:
    t_stat, t_p = float('nan'), float('nan')

print(f"\nAuth scope mitigation across models:")
for c in auth_scope_cells:
    print(f"  {c['model']:<25} Δ = {c['delta_pp']:>+7.1f}pp")
print(f"  Pooled: {pooled_auth_delta:+.1f}pp ± {pooled_auth_se:.1f}pp, CI=[{pooled_auth_ci[0]:.1f}, {pooled_auth_ci[1]:.1f}]")
print(f"  All negative: {all_negative_auth}")
print(f"  t={t_stat:.2f}, p={t_p:.4f}")

auth_scope_pooled = {
    "per_model_delta": {c["model"]: c["delta_pp"] for c in auth_scope_cells},
    "all_negative": all_negative_auth,
    "pooled_mean_delta_pp": round(pooled_auth_delta, 2),
    "pooled_se": round(pooled_auth_se, 2),
    "pooled_ci_95": [round(pooled_auth_ci[0], 2), round(pooled_auth_ci[1], 2)],
    "t_statistic": round(t_stat, 3) if not np.isnan(t_stat) else None,
    "p_value": round(t_p, 4) if not np.isnan(t_p) else None,
    "n_models": len(auth_scope_deltas)
}

# --- B5: Incompleteness pattern (mixed) ---

incomp_deltas = []
incomp_cells = []
for model in model_names:
    if "incompleteness" in per_model_per_type_delta[model]:
        d = per_model_per_type_delta[model]["incompleteness"]
        incomp_deltas.append(d["delta_pp"])
        incomp_cells.append({"model": model, **d})

n_improve = sum(1 for d in incomp_deltas if d < 0)
n_worsen = sum(1 for d in incomp_deltas if d > 0)
n_neutral = sum(1 for d in incomp_deltas if d == 0)

pooled_incomp = np.mean(incomp_deltas) if incomp_deltas else 0
incomp_se = np.std(incomp_deltas, ddof=1) / np.sqrt(len(incomp_deltas)) if len(incomp_deltas) > 1 else 0

print(f"\nIncompleteness mitigation pattern:")
for c in incomp_cells:
    direction = "↓improve" if c["delta_pp"] < 0 else "↑worsen" if c["delta_pp"] > 0 else "→neutral"
    print(f"  {c['model']:<25} Δ = {c['delta_pp']:>+7.1f}pp  {direction}")
print(f"  Improve: {n_improve}, Worsen: {n_worsen}, Neutral: {n_neutral}")
print(f"  Pooled: {pooled_incomp:+.1f}pp ± {incomp_se:.1f}pp")

incompleteness_pattern = {
    "per_model_delta": {c["model"]: c["delta_pp"] for c in incomp_cells},
    "n_improve": n_improve,
    "n_worsen": n_worsen,
    "n_neutral": n_neutral,
    "pooled_mean_delta_pp": round(pooled_incomp, 2),
    "pooled_se": round(incomp_se, 2),
    "pattern": "mixed",
    "explanation": "Disambiguation prompts may not address gap-filling — models fill incomplete clauses based on parametric knowledge, not clause text"
}

# --- B6: Per-type pooled responsiveness ---

per_type_pooled = {}
for t in active_types:
    deltas = []
    for model in model_names:
        if t in per_model_per_type_delta[model]:
            deltas.append(per_model_per_type_delta[model][t]["delta_pp"])

    if deltas:
        mean_d = np.mean(deltas)
        se_d = np.std(deltas, ddof=1) / np.sqrt(len(deltas)) if len(deltas) > 1 else 0
        ci = [mean_d - 1.96 * se_d, mean_d + 1.96 * se_d]

        if len(deltas) > 1:
            t_stat_type, t_p_type = stats.ttest_1samp(deltas, 0)
        else:
            t_stat_type, t_p_type = float('nan'), float('nan')

        per_type_pooled[t] = {
            "pooled_mean_delta_pp": round(mean_d, 2),
            "se": round(se_d, 2),
            "ci_95": [round(ci[0], 2), round(ci[1], 2)],
            "n_models": len(deltas),
            "all_negative": all(d < 0 for d in deltas),
            "all_positive": all(d > 0 for d in deltas),
            "t_statistic": round(t_stat_type, 3) if not np.isnan(t_stat_type) else None,
            "p_value": round(t_p_type, 4) if not np.isnan(t_p_type) else None,
            "per_model": {model: per_model_per_type_delta[model][t]["delta_pp"]
                         for model in model_names if t in per_model_per_type_delta[model]}
        }

print(f"\nPer-type pooled mitigation responsiveness (across 5 models):")
print(f"{'Type':<25} {'Mean Δpp':>10} {'SE':>8} {'p':>8} {'Direction':>12}")
for t in sorted(per_type_pooled.keys()):
    d = per_type_pooled[t]
    direction = "all↓" if d["all_negative"] else "all↑" if d["all_positive"] else "mixed"
    p_str = f"{d['p_value']:.4f}" if d["p_value"] is not None else "N/A"
    print(f"{t:<25} {d['pooled_mean_delta_pp']:>+9.1f} {d['se']:>7.1f} {p_str:>8} {direction:>12}")

# Assemble Part B output
analysis_mitigation = {
    "description": "5-model mitigation complete analysis (coreferential excluded — no mitigated data)",
    "data_source": "mitigation_study/analysis/mitigation_results.json",
    "models": model_list_mit,
    "types_analyzed": type_list_mit,
    "note": "coreferential excluded because mitigated_n=0 for all models",
    "per_model_per_type_delta": per_model_per_type_delta,
    "model_type_interaction_test": model_type_interaction_test,
    "baseline_vs_responsiveness_correlation": baseline_vs_responsiveness,
    "auth_scope_pooled_effect": auth_scope_pooled,
    "incompleteness_pattern": incompleteness_pattern,
    "per_type_pooled_responsiveness": per_type_pooled
}

with open(f"{BASE}/analysis_mitigation_5model.json", "w") as f:
    json.dump(analysis_mitigation, f, indent=2, cls=NumpyEncoder)
print(f"\n✓ Saved analysis_mitigation_5model.json")


# ═══════════════════════════════════════════════════════════════════════════════
# Summary Report
# ═══════════════════════════════════════════════════════════════════════════════

summary_lines = []
summary_lines.append("# Cross-Domain & 5-Model Mitigation Analysis Summary\n")

summary_lines.append("## Part A: Cross-Domain Comparison (retail vs airline)\n")
summary_lines.append(f"**N = {len(rows)}** episodes: {domain_counts.get('retail', 0)} retail, {domain_counts.get('airline', 0)} airline\n")

summary_lines.append("### C1: Ambiguity effect by domain\n")
for domain in ["retail", "airline"]:
    d = per_domain_c1[domain]
    summary_lines.append(f"- **{domain.capitalize()}**: ambiguous {d['ambiguous_rate']:.1%} vs unambiguous {d['unambiguous_rate']:.1%}, "
                        f"Δ = {d['delta_pp']:+.1f}pp, 95% CI [{d['ci_95'][0]:.1f}, {d['ci_95'][1]:.1f}], "
                        f"χ² = {d['chi2']:.1f}, p = {d['p_value']:.1e}")
summary_lines.append("")

summary_lines.append("### Domain × Condition interaction\n")
summary_lines.append(f"Logistic regression: violation ~ condition × domain + type (N = {domain_condition_interaction['n_observations']})\n")
summary_lines.append(f"- Interaction β = {domain_condition_interaction['interaction_coefficient']:.3f}, "
                    f"SE = {domain_condition_interaction['interaction_se']:.3f}")
summary_lines.append(f"- LR test: χ² = {domain_condition_interaction['lr_test_chi2']:.3f}, "
                    f"p = {domain_condition_interaction['lr_test_p']:.3f}")
summary_lines.append(f"- **{domain_condition_interaction['interpretation']}**\n")

summary_lines.append("### Type ranking concordance across domains\n")
summary_lines.append(f"- Spearman ρ = {type_ranking_rho['spearman_rho']:.3f}, p = {type_ranking_rho['p_value']:.3f}")
summary_lines.append(f"- Model Δpp ranking Spearman ρ = {rho_models:.3f}, p = {p_models:.3f}\n")

summary_lines.append("### Per-type domain comparison\n")
summary_lines.append(f"| Type | Retail | Airline | Δ(R−A) | Fisher p |")
summary_lines.append(f"|------|--------|---------|--------|----------|")
for t in sorted(per_type_domain_comparison.keys()):
    d = per_type_domain_comparison[t]
    p_str = f"{d['fisher_p']:.3f}" if d['fisher_p'] is not None else "N/A"
    summary_lines.append(f"| {t} | {d['retail_rate']:.1%} | {d['airline_rate']:.1%} | {d['delta_pp']:+.1f}pp | {p_str} |")
summary_lines.append("")

summary_lines.append("---\n")
summary_lines.append("## Part B: 5-Model Mitigation Analysis\n")
summary_lines.append(f"**Models**: {', '.join(model_list_mit)}")
summary_lines.append(f"**Types analyzed**: {', '.join(type_list_mit)} (coreferential excluded: no mitigated data)\n")

summary_lines.append("### Per-type pooled responsiveness\n")
summary_lines.append(f"| Type | Pooled Δpp | SE | 95% CI | p | Pattern |")
summary_lines.append(f"|------|-----------|-----|--------|---|---------|")
for t in sorted(per_type_pooled.keys()):
    d = per_type_pooled[t]
    direction = "all improve" if d["all_negative"] else "all worsen" if d["all_positive"] else "mixed"
    p_str = f"{d['p_value']:.3f}" if d["p_value"] is not None else "N/A"
    summary_lines.append(f"| {t} | {d['pooled_mean_delta_pp']:+.1f} | {d['se']:.1f} | [{d['ci_95'][0]:.1f}, {d['ci_95'][1]:.1f}] | {p_str} | {direction} |")
summary_lines.append("")

summary_lines.append("### Auth scope: consistent improvement\n")
summary_lines.append(f"- All {auth_scope_pooled['n_models']} models show negative Δ: {all_negative_auth}")
summary_lines.append(f"- Pooled: {auth_scope_pooled['pooled_mean_delta_pp']:+.1f}pp, "
                    f"95% CI [{auth_scope_pooled['pooled_ci_95'][0]:.1f}, {auth_scope_pooled['pooled_ci_95'][1]:.1f}], "
                    f"p = {auth_scope_pooled['p_value']:.3f}" if auth_scope_pooled['p_value'] else "")
summary_lines.append("")

summary_lines.append("### Incompleteness: mixed response\n")
summary_lines.append(f"- Models improving: {incompleteness_pattern['n_improve']}, worsening: {incompleteness_pattern['n_worsen']}")
summary_lines.append(f"- Pooled: {incompleteness_pattern['pooled_mean_delta_pp']:+.1f}pp ± {incompleteness_pattern['pooled_se']:.1f}")
summary_lines.append(f"- Explanation: {incompleteness_pattern['explanation']}\n")

summary_lines.append("### Baseline vulnerability vs mitigation responsiveness\n")
summary_lines.append(f"- Pearson r = {baseline_vs_responsiveness['pearson_r']:.3f} (p = {baseline_vs_responsiveness['pearson_p']:.3f})")
summary_lines.append(f"- Spearman ρ = {baseline_vs_responsiveness['spearman_rho']:.3f} (p = {baseline_vs_responsiveness['spearman_p']:.3f})")
summary_lines.append(f"- {baseline_vs_responsiveness['interpretation']}\n")

summary_lines.append("### Interaction tests\n")
summary_lines.append(f"- Type × Mitigation: χ² = {model_type_interaction_test['type_x_mitigation_interaction']['lr_chi2']:.1f}, "
                    f"df = {model_type_interaction_test['type_x_mitigation_interaction']['df']}, "
                    f"p = {model_type_interaction_test['type_x_mitigation_interaction']['p_value']:.3f}")
summary_lines.append(f"- Model × Mitigation: χ² = {model_type_interaction_test['model_x_mitigation_interaction']['lr_chi2']:.1f}, "
                    f"df = {model_type_interaction_test['model_x_mitigation_interaction']['df']}, "
                    f"p = {model_type_interaction_test['model_x_mitigation_interaction']['p_value']:.3f}")

summary_text = "\n".join(summary_lines)
with open(f"{BASE}/analysis_cross_domain_mitigation_summary.md", "w") as f:
    f.write(summary_text)
print(f"\n✓ Saved analysis_cross_domain_mitigation_summary.md")

print("\n" + "=" * 70)
print("ALL DONE")
print("=" * 70)

# MF-1: Per-clause info delta analysis — controls for the info delta confound
# in the specification vs linguistic layer comparison.

import json
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from pathlib import Path

ROOT = Path("/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts")
OUT = ROOT / "full_study" / "analysis" / "info_delta_analysis.json"

SPEC_TYPES = {"authorization_scope", "conditional_precedence", "incompleteness"}
LING_TYPES = {"scopal", "lexical", "coreferential"}

# --- Step 1: per-clause info delta ---
with open(ROOT / "clause_templates_full.json") as f:
    clauses = json.load(f)

clause_info = []
for c in clauses:
    amb_wc = len(c["ambiguous_clause"].split())
    unamb_wc = len(c["unambiguous_clause"].split())
    clause_info.append({
        "clause_id": c["clause_id"],
        "ambiguity_type": c["ambiguity_type"],
        "info_delta": unamb_wc - amb_wc,
    })
clause_df = pd.DataFrame(clause_info)

# --- Step 2: per-type info delta distribution ---
per_type = {}
for atype, grp in clause_df.groupby("ambiguity_type"):
    per_type[atype] = {
        "mean": round(grp["info_delta"].mean(), 2),
        "sd": round(grp["info_delta"].std(ddof=1), 2),
        "n": int(len(grp)),
    }

print("Per-type info delta:")
for t, v in sorted(per_type.items(), key=lambda x: -x[1]["mean"]):
    print(f"  {t}: {v['mean']} ± {v['sd']} (n={v['n']})")

# --- Load episodes + judgments ---
episodes = []
for model_dir in (ROOT / "full_study" / "episodes").iterdir():
    with open(model_dir / "episodes.jsonl") as f:
        for line in f:
            ep = json.loads(line)
            episodes.append({
                "episode_id": ep["episode_id"],
                "clause_id": ep["clause_id"],
                "ambiguity_type": ep["ambiguity_type"],
                "condition": ep["condition"],
                "model": ep["model"],
            })
ep_df = pd.DataFrame(episodes)

judgments = []
for model_dir in (ROOT / "full_study" / "judgments").iterdir():
    with open(model_dir / "judgments.jsonl") as f:
        for line in f:
            j = json.loads(line)
            judgments.append({
                "episode_id": j["episode_id"],
                "violation_level": j["judgment"]["violation_level"],
            })
jdg_df = pd.DataFrame(judgments)

df = ep_df.merge(jdg_df, on="episode_id")
df = df.merge(clause_df[["clause_id", "info_delta"]], on="clause_id")

# Filter to ambiguous condition only
df_amb = df[df["condition"] == "ambiguous"].copy()
print(f"\nAmbiguous episodes: {len(df_amb)}")

df_amb["violated"] = df_amb["violation_level"].isin(["moderate", "critical"]).astype(int)
df_amb["layer_binary"] = df_amb["ambiguity_type"].isin(SPEC_TYPES).astype(int)

# --- Step 3: Logistic regression ---
# Model 1: violated ~ layer
X1 = sm.add_constant(df_amb["layer_binary"])
model1 = sm.Logit(df_amb["violated"], X1).fit(disp=0)

# Model 2: violated ~ layer + info_delta
X2 = sm.add_constant(df_amb[["layer_binary", "info_delta"]])
model2 = sm.Logit(df_amb["violated"], X2).fit(disp=0)

def extract_coef(model, name):
    idx = list(model.params.index).index(name)
    return {
        "coef": round(float(model.params[name]), 4),
        "se": round(float(model.bse[name]), 4),
        "p": round(float(model.pvalues[name]), 6),
        "or": round(float(np.exp(model.params[name])), 4),
    }

m1_layer = extract_coef(model1, "layer_binary")
m2_layer = extract_coef(model2, "layer_binary")
m2_info = extract_coef(model2, "info_delta")

layer_change_pct = round(
    (m1_layer["coef"] - m2_layer["coef"]) / abs(m1_layer["coef"]) * 100, 2
)

print(f"\nModel 1 (layer only):  layer coef={m1_layer['coef']}, p={m1_layer['p']}")
print(f"Model 2 (layer+info): layer coef={m2_layer['coef']}, p={m2_layer['p']}")
print(f"  info_delta coef={m2_info['coef']}, p={m2_info['p']}")
print(f"  layer coef change: {layer_change_pct}%")

# Interpretation
if abs(layer_change_pct) < 20:
    interp = (
        f"Adding info_delta changes the layer coefficient by {layer_change_pct}% "
        f"(<20% threshold), indicating info delta is not a major confounder. "
        f"The specification-layer effect remains robust after controlling for "
        f"information content differences."
    )
else:
    interp = (
        f"Adding info_delta changes the layer coefficient by {layer_change_pct}% "
        f"(>=20% threshold), suggesting info delta partially confounds the layer effect."
    )

# --- Step 4: Sensitivity test excluding incompleteness ---
spec_excl = {"authorization_scope", "conditional_precedence"}
df_sens = df_amb[df_amb["ambiguity_type"].isin(spec_excl | LING_TYPES)].copy()
df_sens["is_spec"] = df_sens["ambiguity_type"].isin(spec_excl).astype(int)

spec_sub = df_sens[df_sens["is_spec"] == 1]
ling_sub = df_sens[df_sens["is_spec"] == 0]

spec_n = len(spec_sub)
spec_viol = int(spec_sub["violated"].sum())
spec_rate = round(spec_viol / spec_n * 100, 2)

ling_n = len(ling_sub)
ling_viol = int(ling_sub["violated"].sum())
ling_rate = round(ling_viol / ling_n * 100, 2)

delta_pp = round(spec_rate - ling_rate, 2)

# Chi-squared
ct = pd.crosstab(df_sens["is_spec"], df_sens["violated"])
chi2, p_chi, dof, _ = stats.chi2_contingency(ct, correction=False)
cramers_v = round(np.sqrt(chi2 / len(df_sens)), 4)

# Odds ratio
a = ct.loc[1, 1]  # spec & violated
b = ct.loc[1, 0]  # spec & not violated
c = ct.loc[0, 1]  # ling & violated
d = ct.loc[0, 0]  # ling & not violated
odds_r = (a * d) / (b * c) if (b * c) > 0 else float("inf")
log_or_se = np.sqrt(1/a + 1/b + 1/c + 1/d)
or_ci = [
    round(float(np.exp(np.log(odds_r) - 1.96 * log_or_se)), 4),
    round(float(np.exp(np.log(odds_r) + 1.96 * log_or_se)), 4),
]

# Bootstrap CI for delta_pp
rng = np.random.default_rng(42)
spec_vals = spec_sub["violated"].values
ling_vals = ling_sub["violated"].values
boot_deltas = []
for _ in range(10000):
    s = rng.choice(spec_vals, size=len(spec_vals), replace=True)
    l = rng.choice(ling_vals, size=len(ling_vals), replace=True)
    boot_deltas.append((s.mean() - l.mean()) * 100)
boot_ci = [round(float(np.percentile(boot_deltas, 2.5)), 2),
            round(float(np.percentile(boot_deltas, 97.5)), 2)]

print(f"\nSensitivity (excl incompleteness):")
print(f"  spec ({list(spec_excl)}): {spec_viol}/{spec_n} = {spec_rate}%")
print(f"  ling ({list(LING_TYPES)}): {ling_viol}/{ling_n} = {ling_rate}%")
print(f"  delta_pp={delta_pp}, chi2={chi2:.4f}, p={p_chi:.6f}, V={cramers_v}")
print(f"  OR={odds_r:.4f}, CI={or_ci}, bootstrap CI={boot_ci}")

# --- Step 5: Output ---
result = {
    "per_type_info_delta": per_type,
    "logistic_regression": {
        "model1_layer_only": {
            "layer_coef": m1_layer["coef"],
            "layer_se": m1_layer["se"],
            "layer_p": m1_layer["p"],
            "layer_or": m1_layer["or"],
            "aic": round(float(model1.aic), 2),
            "bic": round(float(model1.bic), 2),
        },
        "model2_layer_info_delta": {
            "layer_coef": m2_layer["coef"],
            "layer_se": m2_layer["se"],
            "layer_p": m2_layer["p"],
            "layer_or": m2_layer["or"],
            "info_delta_coef": m2_info["coef"],
            "info_delta_se": m2_info["se"],
            "info_delta_p": m2_info["p"],
            "info_delta_or": m2_info["or"],
            "aic": round(float(model2.aic), 2),
            "bic": round(float(model2.bic), 2),
        },
        "layer_coef_change_pct": layer_change_pct,
        "interpretation": interp,
    },
    "sensitivity_excl_incompleteness": {
        "spec_types": sorted(spec_excl),
        "ling_types": sorted(LING_TYPES),
        "spec_n": spec_n,
        "spec_violations": spec_viol,
        "spec_rate_pct": spec_rate,
        "ling_n": ling_n,
        "ling_violations": ling_viol,
        "ling_rate_pct": ling_rate,
        "delta_pp": delta_pp,
        "chi2": round(float(chi2), 4),
        "p": round(float(p_chi), 6),
        "cramers_v": cramers_v,
        "or": round(float(odds_r), 4),
        "or_ci_95": or_ci,
        "bootstrap_ci_95": boot_ci,
    },
}

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, "w") as f:
    json.dump(result, f, indent=2)
print(f"\nSaved to {OUT}")

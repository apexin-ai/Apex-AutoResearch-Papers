"""
Compute Cramér's V and NMI statistics for policy_ambiguity_safety project.

Inputs:
  - Judgment files (all models): episode-level violation_level (none/minor/moderate/critical)
  - Failure mode files (all models): episode-level failure_mode (5 categories)

Outputs:
  1. Cramér's V: ambiguity_type → violated (binary)
  2. Cramér's V: ambiguity_type → failure_mechanism (5 categories, violations only)
  3. NMI:        ambiguity_type → violated (binary)
"""

import json
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
from sklearn.metrics import normalized_mutual_info_score
from pathlib import Path

BASE = Path("/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts")

# ── 1. Load all judgment records ──────────────────────────────────────────────
MODELS = ["gpt-4.1", "claude-sonnet-4-6", "deepseek-v3", "gpt-5.4", "qwen3-235b"]
JUDG_BASE = BASE / "full_study" / "judgments"

judgments = []
for m in MODELS:
    fpath = JUDG_BASE / m / "judgments.jsonl"
    with open(fpath) as f:
        for line in f:
            d = json.loads(line)
            judgments.append({
                "episode_id": d["episode_id"],
                "ambiguity_type": d["ambiguity_type"],
                "condition": d["condition"],
                "model": d["model"],
                "violation_level": d["judgment"]["violation_level"],
            })

jdf = pd.DataFrame(judgments)
# Binary: violated = any non-none level
jdf["violated"] = (jdf["violation_level"] != "none").astype(int)

print(f"Total judgment records: {len(jdf)}")
print(f"Conditions: {jdf['condition'].unique()}")
print(f"Ambiguity types: {sorted(jdf['ambiguity_type'].unique())}")
print(f"Violation rate: {jdf['violated'].mean():.3f}")
print()

# ── 2. Load all failure_mode records ─────────────────────────────────────────
FM_FILES = [
    BASE / "_project" / "data" / "failure_modes.jsonl",        # gpt-5.4
    BASE / "_project" / "data" / "failure_modes_gpt41.jsonl",  # gpt-4.1
    BASE / "_project" / "data" / "failure_modes_deepseek.jsonl",
    BASE / "_project" / "data" / "failure_modes_claude.jsonl",
    BASE / "_project" / "data" / "failure_modes_qwen3.jsonl",
]

failure_modes = []
for fpath in FM_FILES:
    with open(fpath) as f:
        for line in f:
            d = json.loads(line)
            failure_modes.append({
                "episode_id": d["episode_id"],
                "ambiguity_type": d["ambiguity_type"],
                "model": d["model"],
                "failure_mode": d["failure_mode"],
            })

fmdf = pd.DataFrame(failure_modes)
print(f"Total failure mode records: {len(fmdf)}")
print(f"Failure modes: {sorted(fmdf['failure_mode'].unique())}")
print()

# ── Helper: Cramér's V ────────────────────────────────────────────────────────
def cramers_v(x, y):
    """Cramér's V from two categorical Series using chi2_contingency."""
    ct = pd.crosstab(x, y)
    chi2, p, dof, expected = chi2_contingency(ct, correction=False)
    n = ct.values.sum()
    r, k = ct.shape
    # min(k-1, r-1) where r = rows, k = cols
    phi2_corrected = chi2 / (n * min(r - 1, k - 1))
    v = np.sqrt(max(phi2_corrected, 0))
    return v, chi2, p, n, r, k, ct

# ── 3. Stat 1: Cramér's V — ambiguity_type → violated (binary) ───────────────
# Use all condition=ambiguous records (the ambiguous condition is the focus of the study)
# But first check if paper uses all records or just ambiguous condition
# Analysis files aggregate per condition, so use ambiguous condition only
jdf_ambig = jdf[jdf["condition"] == "ambiguous"].copy()
print(f"Ambiguous condition records: {len(jdf_ambig)}")

v1, chi2_1, p1, n1, r1, k1, ct1 = cramers_v(jdf_ambig["ambiguity_type"], jdf_ambig["violated"])
print("=== Cramér's V: ambiguity_type → violated (binary) ===")
print(f"  Contingency table shape: {r1} types × {k1} binary")
print(f"  N = {n1}")
print(f"  chi2 = {chi2_1:.4f}, p = {p1:.4e}")
print(f"  Cramér's V = {v1:.4f}")
print()
print("Contingency table (ambig condition only):")
print(ct1)
print()

# ── 4. Stat 2: Cramér's V — ambiguity_type → failure_mechanism (5-cat) ────────
# failure_mode has 8 categories, map to 5 as in the paper
# From analysis_type_mechanism_mapping.json:
#   labels = ['assumption_based_action', 'scope_misapplication', 'unauthorized_escalation',
#             'arbitrary_rule_selection', 'conservative_refusal', 'other']
# Note: 'referent_misidentification' and 'surface_adoption' are original coder labels
# that the paper remaps. Check how they map.

# From the mapping in the JSON: referent_misidentification->scope_misapplication, surface_adoption->assumption_based_action
RAW_TO_5WAY = {
    "assumption_based_action": "assumption_based_action",
    "scope_misapplication": "scope_misapplication",
    "unauthorized_escalation": "unauthorized_escalation",
    "arbitrary_rule_selection": "arbitrary_rule_selection",
    "conservative_refusal": "conservative_refusal",
    "referent_misidentification": "scope_misapplication",
    "surface_adoption": "assumption_based_action",
    "other": "other",
}

fmdf["failure_mechanism"] = fmdf["failure_mode"].map(RAW_TO_5WAY)
unmapped = fmdf["failure_mechanism"].isna().sum()
print(f"Unmapped failure modes: {unmapped}")
if unmapped > 0:
    print(fmdf[fmdf["failure_mechanism"].isna()]["failure_mode"].value_counts())

v2, chi2_2, p2, n2, r2, k2, ct2 = cramers_v(fmdf["ambiguity_type"], fmdf["failure_mechanism"])
print("=== Cramér's V: ambiguity_type → failure_mechanism (5-cat) ===")
print(f"  Contingency table shape: {r2} types × {k2} mechanisms")
print(f"  N = {n2}")
print(f"  chi2 = {chi2_2:.4f}, p = {p2:.4e}")
print(f"  Cramér's V = {v2:.4f}")
print()
print("Contingency table:")
print(ct2)
print()

# ── 5. Stat 3: NMI — ambiguity_type → violated (binary) ─────────────────────
# Use the same ambiguous-condition dataset as Stat 1
nmi_val = normalized_mutual_info_score(
    jdf_ambig["ambiguity_type"],
    jdf_ambig["violated"],
    average_method="arithmetic"
)
print("=== NMI: ambiguity_type → violated (binary) ===")
print(f"  N = {len(jdf_ambig)}")
print(f"  NMI = {nmi_val:.4f}")
print()

# ── Summary ───────────────────────────────────────────────────────────────────
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"  Cramér's V (type → violated binary):      V = {v1:.4f}  (N={n1}, chi2={chi2_1:.1f}, p={p1:.2e})")
print(f"  Cramér's V (type → failure mechanism):    V = {v2:.4f}  (N={n2}, chi2={chi2_2:.1f}, p={p2:.2e})")
print(f"  NMI        (type → violated binary):      NMI = {nmi_val:.4f}  (N={len(jdf_ambig)})")

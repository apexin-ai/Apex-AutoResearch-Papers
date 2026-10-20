"""
Permutation test for clause-level R² from Type III SS decomposition.

Shuffles violation_rate within each (type, condition, model) stratum,
breaking clause-to-outcome correlation while preserving marginals.
Re-fits the OLS model and computes clause_id R². 1000 permutations.

Input: per_clause_summary.csv
Output: artifacts/permutation_clause_r2.json
"""

import json
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from pathlib import Path

ANALYSIS_DIR = Path(__file__).parent
CSV_PATH = ANALYSIS_DIR / "per_clause_summary.csv"
OUTPUT_PATH = Path(__file__).parent.parent.parent / "permutation_clause_r2.json"

N_PERMUTATIONS = 1000

np.random.seed(42)


def compute_clause_r2(df):
    """Compute clause_id R² using Type II ANOVA from OLS model."""
    m = ols("violation_rate ~ C(clause_id) + C(condition) + C(model)", data=df).fit()
    anova = sm.stats.anova_lm(m, typ=2)

    clause_ss = float(anova.loc["C(clause_id)", "sum_sq"])
    total_ss = sum(float(anova.loc[idx, "sum_sq"]) for idx in anova.index)

    return clause_ss / total_ss


def main():
    df = pd.read_csv(CSV_PATH)
    print(f"Loaded {len(df)} rows, {df['clause_id'].nunique()} clauses")

    # Observed R²
    observed_r2 = compute_clause_r2(df)
    print(f"Observed clause R² = {observed_r2:.4f} ({observed_r2*100:.1f}%)")

    # Build strata: (ambiguity_type, condition, model)
    strata_keys = df.groupby(["ambiguity_type", "condition", "model"]).groups

    # Permutation test: shuffle violation_rate within each stratum
    null_r2s = []
    for i in range(N_PERMUTATIONS):
        df_perm = df.copy()

        for key, indices in strata_keys.items():
            vals = df_perm.loc[indices, "violation_rate"].values.copy()
            np.random.shuffle(vals)
            df_perm.loc[indices, "violation_rate"] = vals

        null_r2 = compute_clause_r2(df_perm)
        null_r2s.append(null_r2)

        if (i + 1) % 100 == 0:
            print(f"  Permutation {i+1}/{N_PERMUTATIONS}: null R² = {null_r2:.4f}")

    null_r2s = np.array(null_r2s)
    p_value = float(np.mean(null_r2s >= observed_r2))

    result = {
        "test": "Permutation test for clause-level R²",
        "method": "Shuffle violation_rate within (type, condition, model) strata",
        "n_permutations": N_PERMUTATIONS,
        "observed_r2": round(float(observed_r2), 4),
        "observed_r2_pct": round(float(observed_r2) * 100, 1),
        "null_distribution": {
            "mean": round(float(null_r2s.mean()), 4),
            "mean_pct": round(float(null_r2s.mean()) * 100, 1),
            "std": round(float(null_r2s.std()), 4),
            "percentile_95": round(float(np.percentile(null_r2s, 95)), 4),
            "percentile_95_pct": round(float(np.percentile(null_r2s, 95)) * 100, 1),
            "percentile_99": round(float(np.percentile(null_r2s, 99)), 4),
            "max": round(float(null_r2s.max()), 4),
        },
        "p_value": p_value if p_value > 0 else f"< {1/N_PERMUTATIONS}",
        "conclusion": "",
    }

    if p_value == 0:
        result["conclusion"] = (
            f"Observed clause R² ({observed_r2*100:.1f}%) significantly exceeds the null "
            f"expectation (mean null = {null_r2s.mean()*100:.1f}%, 95th = {np.percentile(null_r2s, 95)*100:.1f}%). "
            f"p < {1/N_PERMUTATIONS} ({N_PERMUTATIONS} permutations, 0 exceeded observed)."
        )
    else:
        result["conclusion"] = (
            f"Observed clause R² ({observed_r2*100:.1f}%) vs null mean = {null_r2s.mean()*100:.1f}%. "
            f"p = {p_value:.4f}."
        )

    with open(OUTPUT_PATH, "w") as f:
        json.dump(result, f, indent=2)

    print(f"\nResult: {result['conclusion']}")
    print(f"Saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

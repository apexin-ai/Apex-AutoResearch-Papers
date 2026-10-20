# Δπ-only Diagnostic AUC Analysis

## Motivation

Reviewer concern: the current diagnostic (Proposition 2) has circular dependency — it requires Δτ (oracle CATE heterogeneity), but estimating CATE is the purpose of EC-HTE. We show that a **Δπ-only diagnostic** that depends solely on misclassification rates (π_s, π̄) achieves equal or better predictive performance.

## Proposition 2 Condition (Δπ-only)

The sufficient condition for HB shrinkage to improve over global correction is:

$$\frac{|\delta_s|}{(1-2\bar\pi)\,\pi_s} > 1$$

where δ_s = π_s − π̄. This depends **only on misclassification rates**, not on Δτ.

## Data Sources

| Experiment | Settings | Description |
|-----------|---------|-------------|
| exp-001 | 36 | Synthetic, K∈{2,4}, n_expert∈{50..2000}, 3 regimes |
| exp-003 | 12 | TweetEval semi-synthetic, K=4, n_expert∈{50..500}, 3 regimes |
| exp-013 | 1 | Boundary condition, K=4, n=50, extreme |
| **Total** | **49** | hb_wins=7 (14.3%), global_wins=42 (85.7%) |

## Setting-level AUC Results

| Diagnostic | AUC | Needs Δτ? |
|-----------|-----|----------|
| **π CV** | **0.968** | No |
| **Δπ-only (Prop 2)** | **0.889** | No |
| Cond-number κ(M̂) | 0.855 | No |
| π range | 0.855 | No |
| Combined (Δπ + eff_n) | 0.820 | No |
| Δπ×Δτ (current) | 0.889 | **Yes** |

**Key finding**: The Δπ-only diagnostic (AUC=0.889) **matches** the current Δπ×Δτ diagnostic (AUC=0.889) at the setting level, while requiring no knowledge of treatment effect heterogeneity. The coefficient of variation of misclassification rates (π CV) achieves the highest AUC of 0.968.

## Subgroup-level AUC Results

| Diagnostic | AUC | Needs Δτ? |
|-----------|-----|----------|
| **Δπ-only (Prop 2)** | **0.865** | No |
| Δπ×Δτ (current) | 0.726 | **Yes** |
| Cond-number κ(M̂) | 0.096 | No |

**Key finding**: At the subgroup level (n=160 data points, 36 with hb_wins=1), the Δπ-only diagnostic **substantially outperforms** the current Δπ×Δτ diagnostic (0.865 vs 0.726). The condition number performs worse than random at subgroup level because high κ(M̂_s) indicates subgroups where misclassification is near 0.5 — these are exactly the subgroups where HB estimation is noisiest and tends to lose.

## Per-experiment Breakdown (Setting-level)

| Diagnostic | exp-001 AUC (n=36) | exp-003 |
|-----------|-------------------|---------|
| Δπ-only (Prop 2) | 0.869 | All global wins (no AUC) |
| Cond-number κ(M̂) | 0.869 | — |
| π CV | 0.958 | — |
| Δπ×Δτ (current) | 0.869 | — |

exp-003 has hb_wins=0 across all 12 settings — the hierarchical method never outperforms global correction in the TweetEval semi-synthetic data, consistent with the relatively small expert budgets (n≤500) and K=4 subgroups yielding insufficient per-subgroup expert labels.

## Stratification by n_expert

| n_expert | Δπ-only AUC | Δπ×Δτ AUC |
|---------|------------|-----------|
| 50 | all global wins | all global wins |
| 100 | 0.875 | 0.875 |
| 250 | 0.875 | 0.875 |
| 500 | 0.875 | 0.875 |
| 1000 | 1.000 | 1.000 |
| 2000 | 1.000 | 1.000 |

Both diagnostics perform identically within n_expert strata, confirming that Δτ adds no discriminative power beyond Δπ when sample size is held constant.

## Diagnostic Score Values

For settings where HB wins (all K=2, extreme, n≥100):
- Δπ-only score = **2.857** (δ_s/((1-2π̄)·π_s) for π_s∈{0.25, 0.05}, π̄=0.15)
- This exceeds the threshold of 1, consistent with Proposition 2

For settings where global wins:
- Homogeneous regime: Δπ-only = 0.000 (all π_s equal → δ_s=0)
- Moderate regime, K=2: Δπ-only = 0.333 (below threshold)
- K=4 settings: Despite high Δπ-only scores (up to 6.2), global still wins at small n because per-subgroup estimation variance dominates

## Interpretation

1. **Δτ is redundant for the diagnostic.** The Δπ-only diagnostic achieves identical setting-level AUC (0.889) and superior subgroup-level AUC (0.865 vs 0.726) compared to the Δπ×Δτ diagnostic. This resolves the circular dependency concern.

2. **π CV is the best single predictor** at the setting level (AUC=0.968), capturing the intuition that HB wins when misclassification heterogeneity (relative to its mean) is large.

3. **The Proposition 2 condition works in practice.** The score |δ_s|/((1-2π̄)·π_s) > 1 correctly identifies the K=2 extreme regime (score=2.86) as the case where HB dominates, while homogeneous (score=0) and moderate-K=2 (score=0.33) correctly predict global wins.

4. **Sample size remains a necessary co-condition.** Even with high Δπ-only scores, K=4 extreme settings need n≥1000 for HB to win, because per-subgroup CM estimation variance overwhelms the shrinkage benefit at small n. A practical guideline would combine the Δπ-only diagnostic with minimum effective sample size per subgroup.

## Files

- ROC curves: `roc_curves.png`
- Setting-level data: `setting_level_data.csv`
- Subgroup-level data: `subgroup_level_data.csv`
- Computation script: `compute_auc.py`

# DiD Parallel Trends Balance Check (B1)

## Overview

Validates the parallel trends assumption for the Difference-in-Differences design by checking pre-treatment (d000) balance between treated items (n=3,540; included in d025 SFT data) and untreated items (n=10,502).

Baseline accuracy computed from 4 d000 models: Llama-3.2-3B, Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B (all seed=42, 0% contamination).

## 1. Baseline Accuracy

| Group | n | Mean | Std | Median |
|-------|---|------|-----|--------|
| Treated | 3,540 | 0.5214 | 0.3429 | 0.50 |
| Untreated | 10,502 | 0.5156 | 0.3458 | 0.50 |
| **Difference** | — | **+0.0058** | — | — |

| Test | Statistic | p-value |
|------|-----------|---------|
| Two-sample t-test | t = 0.858 | 0.391 |
| Mann-Whitney U | U = 18,765,476 | 0.386 |
| Cohen's d | 0.017 | — |
| Kolmogorov-Smirnov | D = 0.014 | 0.639 |

**Interpretation**: Negligible difference (d = 0.017, ~0.6 pp). Not statistically significant.

## 2. Per-Model d000 Accuracy

| Model | Treated Acc | Untreated Acc | Diff | t | p |
|-------|-------------|---------------|------|---|---|
| Llama-3.2-3B | 0.4596 | 0.4528 | +0.0068 | 0.706 | 0.480 |
| Qwen2.5-0.5B | 0.3989 | 0.3975 | +0.0013 | 0.139 | 0.889 |
| Qwen2.5-1.5B | 0.5862 | 0.5850 | +0.0011 | 0.118 | 0.906 |
| Qwen2.5-3B | 0.6410 | 0.6272 | +0.0137 | 1.466 | 0.143 |

**Interpretation**: No model shows a significant treated-untreated gap at baseline. All p > 0.14, all |diff| < 1.4 pp.

## 3. Difficulty Quintile Distribution

Items binned by d000 accuracy (4 discrete levels with 4 models: 0.00, 0.25, 0.50, 0.75, 1.00).

| Quintile | Accuracy | Treated (%) | Untreated (%) | Diff (pp) |
|----------|----------|-------------|---------------|-----------|
| Q1 (hardest) | [0.00–0.25] | 34.7% | 36.2% | −1.4 |
| Q2 | [0.50] | 23.2% | 22.8% | +0.4 |
| Q3 | [0.75] | 22.8% | 21.3% | +1.5 |
| Q4 (easiest) | [1.00] | 19.3% | 19.8% | −0.5 |

- Chi-square: χ² = 4.72, df = 3, p = 0.194
- Cramér's V = 0.018

**Interpretation**: Treated and untreated items have near-identical difficulty profiles. Maximum discrepancy is 1.5 pp.

## 4. Domain Distribution

| Domain | Treated (%) | Untreated (%) | Diff (pp) |
|--------|-------------|---------------|-----------|
| Humanities | 32.7% | 33.8% | −1.1 |
| Other | 23.2% | 21.8% | +1.4 |
| STEM | 22.7% | 22.4% | +0.3 |
| Social Sciences | 21.5% | 22.1% | −0.6 |

- Chi-square: χ² = 3.99, df = 3, p = 0.263
- Cramér's V = 0.017

**Interpretation**: Domain composition is well-balanced. All discrepancies < 1.5 pp.

## 5. Subject Distribution

57 MMLU subjects tested. Top 5 by |diff|:

| Subject | N | Treated (%) | Untreated (%) | Diff (pp) |
|---------|---|-------------|---------------|-----------|
| philosophy | 311 | 2.60% | 2.09% | +0.51 |
| professional_law | 1,534 | 10.56% | 11.05% | −0.48 |
| high_school_macroeconomics | 390 | 2.43% | 2.89% | −0.47 |
| medical_genetics | 100 | 1.05% | 0.60% | +0.45 |
| high_school_computer_science | 100 | 1.02% | 0.61% | +0.41 |

- Chi-square: χ² = 61.37, df = 56, p = 0.290
- Cramér's V = 0.066

**Interpretation**: Subject-level proportions are well-matched. Maximum discrepancy is 0.5 pp and chi-square is non-significant.

## Summary

| Dimension | Test | Statistic | p-value | Effect Size | Verdict |
|-----------|------|-----------|---------|-------------|---------|
| Accuracy | t-test | t = 0.86 | 0.391 | d = 0.017 | ✓ Balanced |
| Accuracy | Mann-Whitney U | U = 18.8M | 0.386 | — | ✓ Balanced |
| Accuracy | KS test | D = 0.014 | 0.639 | — | ✓ Balanced |
| Difficulty quintile | Chi-square | χ² = 4.72 | 0.194 | V = 0.018 | ✓ Balanced |
| Domain | Chi-square | χ² = 3.99 | 0.263 | V = 0.017 | ✓ Balanced |
| Subject (57 subj.) | Chi-square | χ² = 61.4 | 0.290 | V = 0.066 | ✓ Balanced |

## Conclusion

Pre-treatment balance holds across all dimensions. Treated and untreated items are well-matched on:
- **Baseline accuracy**: diff = +0.006, Cohen's d = 0.017 (negligible)
- **Difficulty distribution**: χ² p = 0.194, Cramér's V = 0.018
- **Domain composition**: χ² p = 0.263, Cramér's V = 0.017
- **Subject composition**: χ² p = 0.290, Cramér's V = 0.066

All effect sizes are negligible (d < 0.02, V < 0.07). This is consistent with the random 25% selection mechanism used to construct the treated set. The parallel trends assumption for the DiD design is well-supported.

## Data Source

- Contamination labels: `contamination_labels_mmlu_d025.json` (d025 = 25% of 14,042 MMLU items = 3,540 treated)
- Baseline responses: IRT response matrix (4 d000 respondents × 14,042 items)
- Item metadata: `item_metadata.csv` (subject, domain, difficulty_baseline)
- Script: `analysis/did_balance_check.py` on cqa1-21977

# M1: Gemini 2.5 Flash — Leverage Sensitivity Analysis (Cook's Distance)

**Date**: 2026-05-22  
**Data**: `exp_gemini_flash/part2/results_incremental.jsonl` (6720 samples, 60 batches)  
**Batch groups**: count_8 (25 low + 25 high BCS), count_16 (5 low + 5 high BCS)

---

## 1. Count_16 BCS-Controlled (n=10)

### Full Correlation

| Metric | Value | p-value |
|--------|-------|---------|
| Pearson r | **-0.8043** | 0.005 |
| Spearman ρ | -0.4012 | 0.250 |

### Cook's Distance (threshold = 4/n = 0.400)

| Batch | BCS | Accuracy | Cook's D | Flag |
|-------|-----|----------|----------|------|
| count_16_high_4 | **0.9706** | **0.5990** | **0.4904** | LEVERAGE |
| count_16_high_0 | 0.5814 | 0.6615 | 0.3334 | |
| count_16_high_2 | 0.5890 | 0.8385 | 0.1017 | |
| (7 others) | 0.50–0.62 | 0.79–0.84 | <0.05 | |

### Leverage Point Characterization — count_16_high_4

- **BCS = 0.9706**: 11.2σ above the mean of the other 9 batches (mean=0.553, std=0.037). This is an extreme x-outlier — the other 9 batches cluster in [0.50, 0.62].
- **h_ii = 0.934**: hat value is 4.7× the mean (0.200). This single point captures 93% of the x-axis leverage.
- **Residual = +0.003**: near-zero residual (acc falls exactly on the regression line). The point is influential not because it deviates from the trend, but because it *defines* the trend.
- **Why it matters**: Without this point, the remaining 9 batches span only BCS=[0.50, 0.62] — too narrow a range for meaningful correlation.

### Trimmed Correlation (n=9, removing high_4)

| Metric | Value | p-value |
|--------|-------|---------|
| Pearson r | **-0.4173** | 0.264 |
| Spearman ρ | -0.1757 | 0.651 |

**Conclusion**: count_16 correlation is single-point driven. The claim r=-0.80 is entirely dependent on high_4 (BCS=0.97). Removing it drops Pearson to r=-0.42 (n.s.) and Spearman to ρ=-0.18 (n.s.). This is consistent with the paper's disclosure in Appendix T.

---

## 2. Count_8 BCS-Controlled (n=50)

### Full Correlation

| Metric | Value | p-value |
|--------|-------|---------|
| Pearson r | **-0.8873** | 9.4e-18 |
| Spearman ρ | **-0.7435** | 6.2e-10 |

### Cook's Distance (threshold = 4/n = 0.080)

| Batch | BCS | Accuracy | Residual | Cook's D | Flag |
|-------|-----|----------|----------|----------|------|
| count_8_low_10 | 0.3627 | 0.7917 | -0.1131 | **0.1275** | LEVERAGE |
| count_8_high_14 | 0.7988 | 0.8229 | +0.0940 | **0.0883** | LEVERAGE |
| count_8_high_22 | 0.8053 | 0.6458 | -0.0805 | 0.0670 | |
| count_8_high_8 | 0.7953 | 0.8125 | +0.0821 | 0.0664 | |
| (46 others) | 0.36–0.81 | 0.65–0.98 | <0.08 | |

### Leverage Point Characterization

**count_8_low_10** (Cook's D = 0.128, 1.6× threshold):
- BCS=0.363 (typical for low group), but acc=0.792 — well below the low-group mean (0.905). This is a performance outlier: a low-BCS batch that underperformed.
- h_ii = 0.040 (1.0× mean): no x-leverage. Influential purely from large residual.

**count_8_high_14** (Cook's D = 0.088, 1.1× threshold):
- BCS=0.799 (typical for high group), but acc=0.823 — well above the high-group mean (0.729). This is a performance outlier: a high-BCS batch that overperformed.
- h_ii = 0.040 (1.0× mean): no x-leverage. Influential purely from large residual.

Both leverage points are **residual-driven, not x-driven** — they are accuracy outliers, not BCS outliers. This is fundamentally different from the count_16 case where the leverage comes from an extreme BCS value.

### Trimmed Correlation (n=48, removing 2 leverage points)

| Metric | Value | p-value |
|--------|-------|---------|
| Pearson r | **-0.9127** | 1.7e-19 |
| Spearman ρ | **-0.7535** | 6.4e-10 |

**Conclusion**: count_8 correlation **strengthens** after removing leverage points (r: -0.887 → -0.913). The BCS-accuracy relationship is robust and not dependent on any single batch.

---

## 3. Pooled Analysis (n=60)

### Full Correlation

| Metric | Value | p-value |
|--------|-------|---------|
| Pearson r | **-0.8690** | 2.3e-19 |
| Spearman ρ | **-0.8050** | 9.1e-15 |

### Cook's Distance (threshold = 4/n = 0.067)

3 leverage points identified:
- **count_8_low_10** (D=0.093): accuracy outlier (low-BCS batch underperformed)
- **count_8_high_14** (D=0.082): accuracy outlier (high-BCS batch overperformed)
- **count_16_high_0** (D=0.080): accuracy outlier (acc=0.662, large negative residual)

Notably, **count_16_high_4** (BCS=0.97) is NOT flagged as a leverage point in the pooled analysis (D=0.050 < 0.067). Its extreme BCS is diluted by the 50 count_8 batches that provide adequate BCS range.

### Trimmed Correlation (n=57, removing 3)

| Metric | Value | p-value |
|--------|-------|---------|
| Pearson r | **-0.9102** | 1.0e-22 |
| Spearman ρ | **-0.8382** | 4.2e-16 |

---

## 4. Impact on Cross-Model Generalization Claim

### Summary Table

| Analysis | Full r | Full p | Trimmed r | Trimmed p | Trimmed n | Robust? |
|----------|--------|--------|-----------|-----------|-----------|---------|
| count_8 | -0.887 | 9.4e-18 | **-0.913** | 1.7e-19 | 48 | **YES** |
| count_16 | -0.804 | 5.0e-03 | -0.417 | 0.264 | 9 | **NO** |
| Pooled | -0.869 | 2.3e-19 | **-0.910** | 1.0e-22 | 57 | **YES** |

### Assessment

1. **count_8 claim is robust**: r strengthens from -0.887 to -0.913 after leverage removal. The 2 leverage points are accuracy outliers (not BCS outliers), and their removal tightens the relationship. The Δ=-17.6pp gap (CI [15.1, 20.1]) is the primary Gemini Dim2 evidence and is unaffected.

2. **count_16 claim is fragile**: As the paper correctly discloses, the r=-0.80 is driven by a single point (high_4, BCS=0.97) that is 11.2σ from the BCS mean of the other batches. The remaining 9 batches span only BCS=[0.50, 0.62] — insufficient range for meaningful correlation. This is a design limitation (only 5+5 batches with poor BCS separation), not a contradiction of the BCS effect.

3. **Cross-model generalization**: The overall claim holds. Gemini replicates the BCS-accuracy negative relationship at count_8 (n=50, highly significant, robust to leverage removal). The count_16 fragility is a sample-size and design issue, not evidence against the effect. The paper's framing (count_8 as primary, count_16 as supplementary with caveats) is appropriate.

4. **No additional caveats needed**: The paper already discloses the count_16 leverage issue transparently in Appendix T. The count_8 result (the primary evidence) requires no qualification.

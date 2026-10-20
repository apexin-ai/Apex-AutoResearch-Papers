# R1 Statistical Supplements

## N3.2 — Partial Correlation: BCS controlling for degree centrality

**Question**: Does the BCS–accuracy relationship survive after controlling for degree centrality (a type's average SCS to all other types)?

**Method**: Pearson partial correlation via residualization. Degree centrality = mean off-diagonal SCS row value per type; batch mean degree centrality = average over types in the batch.

### FewRel (80-type pool, N=204 batches)

| Metric | Value |
|--------|-------|
| Zero-order r (BCS vs acc) | −0.570 (p < .0001) |
| Zero-order ρ (Spearman) | −0.434 (p < .0001) |
| **Partial r** (controlling deg centrality) | **−0.537 (p < .0001)** |
| VIF(BCS) | 1.18 |
| BCS–deg centrality r | 0.393 |
| BCS unique R² | 0.288 |

BCS and degree centrality are only moderately correlated (r=0.39) in FewRel. The partial correlation (−0.537) is barely reduced from the zero-order (−0.570), confirming that the BCS–accuracy relationship is **not a confound of degree centrality**. VIF=1.18 indicates no multicollinearity concern.

### DocRED (96-type pool, N=110 batches)

| Metric | Value |
|--------|-------|
| Zero-order r (BCS vs acc) | −0.760 (p < .0001) |
| Zero-order ρ (Spearman) | −0.741 (p < .0001) |
| **Partial r** (controlling deg centrality) | **−0.348 (p = .0002)** |
| VIF(BCS) | 50.9 |
| BCS–deg centrality r | 0.990 |
| BCS unique R² | 0.121 |

In DocRED, BCS and degree centrality are near-collinear (r=0.99, VIF=50.9), which substantially reduces the partial correlation. Nevertheless, the partial r = −0.348 remains **highly significant** (p = .0002), demonstrating that BCS retains a unique predictive contribution even after partialling out degree centrality. The high collinearity is expected: in the DocRED schema, types with high mean SCS (high degree centrality) naturally form high-BCS batches.

**Data sources**: FewRel — eval_exp1+exp2 (164 batches, 80-type pool) + 80pool_16sub (100 batches) + bcs_controlled_70b (20 batches, count_8+16, after filtering BCS>0). DocRED — exp_docred_bcs_expanded (110 batches, count_16+32).

---

## W2 — DocRED Range-Matched MDE

**Question**: What is the minimum detectable effect (MDE) for the DocRED range-matched interaction analysis?

| Parameter | Value |
|-----------|-------|
| n₁ (count_16 matched) | 29 |
| n₂ (count_32) | 55 |
| df | 82 |
| SD_pooled | 0.084 |
| SE | 0.0193 |
| **MDE at 80% power** | **5.47 pp** |
| Observed interaction | 0.93 pp |
| Power at observed | 0.076 |
| 95% CI | [−7.13, 7.44] pp |

**Interpretation**: The MDE (5.5pp) far exceeds the observed interaction (0.9pp). With only 7.6% power at the observed effect, this analysis cannot distinguish between a true null and a small (<5.5pp) interaction. The wide 95% CI [−7.1, 7.4]pp spanning zero is consistent with both interpretations.

---

## W3 — NER (Few-NERD) BCS-Null Power Analysis

**Question**: Is the absence of BCS–accuracy correlation in Few-NERD "evidence of absence" or "absence of evidence"?

### Distribution Comparison

| | Few-NERD (3 seeds) | FewRel (80-type pool) |
|---|---|---|
| N batches | 450 | 204 |
| BCS range | [0.580, 0.936] | [0.458, 0.971] |
| **BCS SD** | **0.027** | **0.141** |
| Accuracy/Recall SD | 0.145 | 0.110 |
| Observed r | 0.025 (p=.60) | −0.570 (p<.0001) |

### Key Finding: BCS variance compression

Few-NERD BCS SD (0.027) is only **19.4%** of FewRel's (0.141). Per-count-level analysis reveals the source:

| Count level | BCS SD | BCS range width |
|-------------|--------|-----------------|
| count_2 | 0.053 | 0.199 |
| count_6 | 0.028 | 0.109 |
| count_12 | 0.016 | 0.072 |
| count_22 | 0.010 | 0.050 |
| count_44 | 0.004 | 0.016 |
| count_66 | 0.000 | 0.000 |

At count_66 (all 66 NER types), every batch has identical BCS. Even at count_22, BCS range spans only 0.05 — too narrow to detect any correlation.

### Range-Restriction Attenuation

Under classical range restriction theory: r_attenuated = r_full × (SD_restricted / SD_full).

- FewRel's r = −0.570 would attenuate to **r = −0.111** in Few-NERD's BCS range
- Minimum detectable |r| at 80% power (n=450): **0.132**
- **Power at attenuated effect: 65.1%** — below the 80% threshold

**Conclusion**: The Few-NERD BCS-null is better attributed to insufficient BCS variance (NER entity types have more homogeneous embeddings) than to a genuine absence of the BCS–accuracy relationship. With BCS SD compressed to ~19% of FewRel's, the expected effect falls below the detection threshold.

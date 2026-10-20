# exp-015/016 Failure Case Deep Dive

## Executive Summary

**Both exp-015 and exp-016 are comprehensive failures: HB EC-HTE loses to global correction in ALL cells for exp-015, and 22/24 cells for exp-016.** The root cause is a combination of (1) low P(Z=1)=0.18 creating tiny per-subgroup minority-class samples, and (2) asymmetric, moderately ill-conditioned CMs that amplify estimation noise through matrix inversion. The HB model does not merely fail to shrink — it *overshoots* global correction, with shrinkage coefficients of 2–9x in the worst cells.

A calibrated diagnostic rule emerges: **use HB EC-HTE only when `cond_number(M_hat_s) ≤ 1.2` AND `effective_minority_n ≥ 25`**. Under this rule, 81–93% of cells show improvement. Outside this region, fall back to global correction.

---

## Part 1: Error Pattern Analysis

### 1.1 Per-Subgroup Bias Amplification

The metric `|bias_hb| / |bias_global|` measures how much HB amplifies bias relative to global correction. A value > 1 means HB is worse.

**exp-015 (GPT-4.1, FNR up to 0.526):**
- HB worse in **8/8 cells at every n_expert level** (100, 250, 500)
- Mean amplification ratio: 3–30x across cells
- Worst cells: S3 z=0 n=500 (30.2x), S3 z=1 n=100 (27.7x)
- Even at n_expert=500, mean RMSE_hb = 0.260 vs RMSE_gl = 0.196

**exp-016 (gpt-3.5-turbo, FPR up to 0.393):**
- HB worse in **8/8 cells at n=100, 7/8 at n=250, 7/8 at n=500**
- Mean amplification ratio: 1.4–38.5x across cells
- Worst cells: S2 z=1 n=250 (38.5x), S3 z=1 n=100 (35.7x)
- S2 (FPR=0.393) is catastrophic: RMSE_hb = 2.66 vs RMSE_gl = 0.48 at n=100

**z=1 cells are systematically worse than z=0:** RMSE differences at z=1 are 5–20x larger than at z=0. This is because P(Z=1)=0.18 makes the minority class both harder to estimate and more sensitive to CM inversion errors.

### 1.2 CM Feature Correlation

Correlations between CM features and amplification ratio (cell-level means):

| Feature | exp-015 Pearson | exp-015 p | exp-016 Pearson | exp-016 p |
|---------|:-:|:-:|:-:|:-:|
| FPR | +0.510 | 0.011 | +0.452 | 0.027 |
| FNR | -0.364 | 0.081 | -0.212 | 0.321 |
| |FPR-FNR| (asymmetry) | -0.419 | 0.042 | +0.455 | 0.025 |
| Condition number | -0.213 | 0.318 | +0.470 | 0.020 |
| det(M) | +0.209 | 0.327 | -0.464 | 0.022 |
| min(TPR,TNR) | +0.364 | 0.081 | -0.460 | 0.024 |
| Expected Z=1 experts | -0.131 | 0.541 | -0.325 | 0.121 |

**Key findings:**
- **FPR consistently amplifies bias** (positive correlation in both experiments)
- **Condition number and det(M)** are strong predictors in exp-016 (where FPR variation is higher)
- **Expected Z=1 experts** has a negative Spearman correlation in both experiments (more data → less amplification), significant at p=0.008 in exp-016

### 1.3 Cross-Experiment Comparison

**Similarities:**
- Both experiments show uniform HB failure (0/8 or near-0/8 wins at every n_expert)
- z=1 cells dominate the RMSE gap in both
- S2 (smallest weight = 0.14) is consistently among the worst cells
- Amplification is worst at n_expert=100, improves toward 500 but never reaches parity

**Differences:**
- exp-015 failure is driven by **high FNR** (S0: FNR=0.526, det=0.420) — the CM nearly loses the Z=1 signal
- exp-016 failure is driven by **high FPR** (S2: FPR=0.393, det=0.453) — the CM contaminates Z=0 with false positives
- exp-015 has lower det(M) for S0 (0.420) but exp-016 has lower det(M) for S2/S3 (0.453/0.474)
- exp-016 shows slightly more concentrated failure in S2/S3 (high-FPR subgroups), while exp-015 failure is more spread

**Common root cause:** Both converge to the same mechanism — **per-subgroup CM estimation with insufficient minority-class data**. When P(Z=1)=0.18 and the smallest subgroup has weight=0.14, the expected Z=1 experts at n=100 is only **2.5 per subgroup**. This is far too few to estimate a 2×2 CM reliably.

---

## Part 2: Improvement Regression

### 2.1 Unified Dataset

Pooled 368 cell-level observations across 5 experiments:

| Experiment | N obs | % HB wins | Mean improvement |
|:--|:-:|:-:|:-:|
| exp-001 (synthetic, symmetric CM, P(Z=1)=0.5) | 216 | 31.9% | -4.859 |
| exp-003 (TweetEval, symmetric CM, P(Z=1)=0.349) | 96 | 7.3% | -0.134 |
| exp-013 (boundary, n=50, extreme) | 8 | 12.5% | -0.156 |
| exp-015 (real CM, asymmetric, P(Z=1)=0.18) | 24 | 0.0% | -0.255 |
| exp-016 (real CM, asymmetric, P(Z=1)=0.18) | 24 | 8.3% | -0.364 |

Overall: HB wins in only 79/368 cells (21.5%).

### 2.2 OLS Regression

The linear OLS model (R²=0.024) is a poor fit due to extreme outliers in exp-001 (very large negative improvements at small n_expert with high misclass). The improvement relationship is fundamentally non-linear.

### 2.3 Logistic Classification (improvement > 0)

Logistic regression achieves **89.4% accuracy** for the binary classification. Feature importances:

| Feature | Coefficient | Direction |
|:--|:-:|:--|
| |FPR-FNR| (asymmetry) | +1.706 | Higher asymmetry → more likely to improve (!) |
| det(M) | +1.664 | Higher det → more likely to improve |
| p_z1 | +0.930 | Higher P(Z=1) → more likely to improve |
| cond_number | -0.913 | Higher condition number → less likely to improve |
| n_expert/K | +0.706 | More data per subgroup → more likely to improve |

### 2.4 Decision Boundary

**Single-variable thresholds:**

| Rule | % HB wins | N observations |
|:--|:-:|:-:|
| det(M) ≥ 0.90 | **84.8%** | 46 |
| det(M) ≥ 0.85 | **84.8%** | 46 |
| cond_number ≤ 1.10 | **92.9%** | 14 |
| cond_number ≤ 1.15 | **84.8%** | 46 |
| max_misclass < 0.05 | **92.9%** | 14 |
| eff_minority_n ≥ 100 | 43.0% | 84 |

**Combined thresholds (most useful):**

| Rule | % HB wins | N obs | Mean improvement |
|:--|:-:|:-:|:-:|
| cond ≤ 1.2 AND eff_n ≥ 10 | **87.5%** | 40 | **+0.024** |
| cond ≤ 1.2 AND eff_n ≥ 25 | **93.3%** | 30 | **+0.027** |
| cond ≤ 1.2 AND eff_n ≥ 50 | **100.0%** | 20 | **+0.031** |
| cond ≤ 1.3 AND eff_n ≥ 25 | **80.9%** | 68 | **+0.012** |
| cond ≤ 1.5 AND eff_n ≥ 50 | **51.1%** | 94 | +0.007 |

**Recommended diagnostic:** `cond_number(M_hat_s) ≤ 1.25` AND `n_expert × P(Z=1) / K ≥ 25`.

### 2.5 Why exp-015/016 Fail the Diagnostic

For exp-015/016 with P(Z=1)=0.18, K=4:
- At n_expert=100: eff_minority_n = 100 × 0.18 / 4 = **4.5** (way below 25)
- At n_expert=250: eff_minority_n = 250 × 0.18 / 4 = **11.25** (still below 25)
- At n_expert=500: eff_minority_n = 500 × 0.18 / 4 = **22.5** (still below 25)

All condition numbers are 1.55–2.38, far above the 1.25 threshold.

**To pass the diagnostic, exp-015/016 would need:** n_expert ≥ 25 × 4 / 0.18 ≈ **556** at a minimum, AND a CM with det(M) ≥ 0.80 (cond ≤ 1.25). Neither condition is met.

---

## Part 3: Method Improvement Analysis

### 3a. Adaptive Shrinkage to Naive

**Oracle-optimal weights (toward HB vs naive):**
- exp-015 mean w* = 0.071 → nearly all weight should go to naive
- exp-016 mean w* = 0.115 → similar

**Shrinking HB to naive recovers most of the damage:**
- exp-015: avg RMSE reduction of 0.364 (from 0.47 average RMSE_hb to 0.13)
- exp-016: avg RMSE reduction of 0.470

However, the shrunk result essentially *is* naive — w* ≈ 0 means HB adds no value at all in these regimes.

### 3b. Adaptive Shrinkage to Global (Why HB Doesn't Shrink)

This is the critical diagnostic finding. The HB model is supposed to implement partial pooling (shrinkage toward global when per-subgroup data is sparse). **It fails to do this.**

**Evidence of overshooting:**

| Cell | Shrinkage coef | Variance ratio | Interpretation |
|:--|:-:|:-:|:--|
| exp015 S1 z=1 n=100 | **+2.96** | 17.1x | HB overshoots 3x past global |
| exp015 S2 z=1 n=100 | **+3.59** | 7.5x | HB overshoots 3.6x past global |
| exp015 S3 z=1 n=100 | **+2.34** | 14.7x | HB overshoots 2.3x past global |
| exp016 S2 z=1 n=250 | **+8.89** | 17.6x | HB overshoots 9x past global |
| exp016 S2 z=1 n=500 | **+6.50** | 8.1x | HB overshoots 6.5x past global (!) |

**The shrinkage coefficient** = (E[HB] - E[naive]) / (E[global] - E[naive]). Values > 1 mean HB goes *further* than global correction; values >> 1 indicate catastrophic overshooting.

**Why the HB model overshoots:**

1. **Prior is too weak.** With hyperprior a0=3, b0=1 (Gamma prior on Dirichlet concentration), the prior is only mildly informative. When per-subgroup minority-class counts are 2–7, the likelihood is noisy but not *that* noisy relative to a weak prior. The posterior follows the noisy likelihood.

2. **CM inversion amplifies noise.** Even with perfect pooling, estimating a 2×2 CM from ~5 observations and then inverting it (with det ≈ 0.4–0.6) amplifies estimation error by 1/det ≈ 1.7–2.4x. This is compounded by the asymmetry of the real CMs.

3. **Hierarchical structure doesn't pool CM estimates.** The HB model pools the *outcome model* (CATE estimates) but each subgroup's CM is estimated from only that subgroup's expert labels. There is no cross-subgroup pooling of the CM itself — which is where the real information deficit lies.

4. **The "right" shrinkage target is global correction, not the prior mean.** The HB partial pooling shrinks toward a shared prior on CATE, not toward the global-correction CATE estimate. When all subgroups have noisy CMs, the prior mean is uninformative, and the pooled estimate is just a noisy average of noisy per-subgroup estimates.

### 3c. CM Quality Diagnostic

**Proposed pre-correction diagnostic:**

```python
def should_use_hb_ec_hte(M_hat_s, n_expert, p_z1, K, 
                          cond_threshold=1.25, eff_n_threshold=25):
    """
    Returns True if subgroup s should use HB EC-HTE correction,
    False if it should fall back to global correction.
    """
    det_M = M_hat_s[0,0] * M_hat_s[1,1] - M_hat_s[0,1] * M_hat_s[1,0]
    cond_number = 1.0 / abs(det_M)
    eff_minority_n = n_expert * p_z1 / K
    
    return (cond_number <= cond_threshold) and (eff_minority_n >= eff_n_threshold)
```

**Calibration from 368 observations across 5 experiments:**

| Threshold pair (cond, eff_n) | Precision (% wins when used) | Coverage (% of cells using HB) |
|:--|:-:|:-:|
| (1.20, 10) | 87.5% | 10.9% |
| (1.20, 25) | 93.3% | 8.2% |
| (1.20, 50) | 100.0% | 5.4% |
| (1.25, 25) | ~90% | ~10% |
| (1.30, 25) | 80.9% | 18.5% |

The conservative rule (cond ≤ 1.2, eff_n ≥ 25) achieves 93% precision: when it says "use HB," HB almost always wins. The trade-off is low coverage — it only applies to cells with very clean CMs and ample data.

**For exp-015/016, the diagnostic correctly says "use global" for every cell.** The condition numbers (1.55–2.38) are all above 1.25, and effective minority samples (2.5–34.2) are mostly below 25.

### 3d. Proposed Shrinkage Weight Function

For a smooth transition, replace the hard threshold with a sigmoid:

```
w_s = sigmoid(k1 * (det_M_s - det_0) + k2 * (log(eff_n_s) - log(eff_n_0)))
```

Where `det_0 ≈ 0.85` and `eff_n_0 ≈ 25` are the crossover points. The final CATE estimate becomes:

```
CATE_final_s = w_s * CATE_hb_s + (1 - w_s) * CATE_global
```

From the oracle-optimal weights in exp-015/016:
- Mean w* = 0.057 overall (essentially 0 in these regimes)
- Only 2 cells have w* > 0.5 (both exp016 S0 z=1 at n≥250, where det=0.646 is the best CM)
- In practice, this degenerates to "use global" for all cells in exp-015/016

---

## Conclusions and Recommendations

### Why exp-015 and exp-016 Failed

1. **P(Z=1) = 0.18 is too low.** The effective minority-class sample per subgroup (2.5–34.2) is far below the ~25–50 needed for reliable per-subgroup CM estimation.

2. **Real CMs are asymmetric and ill-conditioned.** det(M) ranges 0.42–0.67, meaning CM inversion amplifies estimation noise by 1.5–2.4x.

3. **HB partial pooling pools the wrong thing.** It pools CATE estimates but not CM estimates. With 4 subgroups each having noisy CMs, the result is 4 noisy-inverted-CM corrections averaged together — worse than one clean globally-estimated CM correction.

### What Would Make EC-HTE Work Here

- **Minimum P(Z=1) ≈ 0.35** at current n_expert and K levels
- **Or n_expert ≥ 600** at current P(Z=1)=0.18
- **Or pool CM estimates hierarchically** (not just CATE estimates) — this is the architectural fix

### Recommended Next Steps

1. **Implement the CM quality diagnostic** as a pre-check before applying EC-HTE
2. **Explore hierarchical CM pooling** — use a Dirichlet hierarchical model for the CMs themselves, not just for the downstream CATE estimates
3. **Test with P(Z=1) ≥ 0.35** to validate that EC-HTE works in the favorable regime with real CMs (exp-017?)
4. **Consider the sigmoid shrinkage** as a drop-in improvement to the existing HB model

---

## Appendix: Generated Artifacts

| File | Description |
|:--|:--|
| `bias_amplification_scatter.png` | Amplification ratio vs det(M) by cell |
| `amplification_heatmap.png` | Heatmap of amplification ratios |
| `rmse_comparison_bars.png` | RMSE comparison by method and cell |
| `partial_dependence.png` | Partial dependence plots for improvement predictors |
| `predicted_vs_actual.png` | OLS regression: predicted vs actual improvement |
| `improvement_heatmap_2d.png` | 2D scatter: improvement by n/K and cond_number |
| `improvement_key_drivers.png` | Improvement vs effective minority sample and cond_number |
| `diagnostic_threshold_calibration.png` | Threshold calibration curves |
| `unified_improvement_data.csv` | Pooled dataset (368 rows) |
| `exp015_cell_summary.csv` | Cell-level summary for exp-015 |
| `exp016_cell_summary.csv` | Cell-level summary for exp-016 |

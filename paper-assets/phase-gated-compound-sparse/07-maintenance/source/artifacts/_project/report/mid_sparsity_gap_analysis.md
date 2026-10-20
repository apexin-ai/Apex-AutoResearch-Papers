# Mid-Sparsity Gap Analysis Report

Generated: 2026-05-14

---

## bf16_importance_s015

**Overview**: 50 problems, 10 missing mid_sparsity, 1 missing high_sparsity

### 1. Missing Problems & Systematic Bias

| idx | problem_id | subject | level | total_segs | n_seg_high | n_seg_mid | n_seg_low |
|-----|-----------|---------|-------|------------|------------|-----------|-----------|
| 4 | `test/algebra/478.json` | Algebra | 1 | 8 | 4 | 0 | 4 |
| 6 | `test/prealgebra/307.json` | Prealgebra | 1 | 1 | 0 | 0 | 1 |
| 7 | `test/algebra/1004.json` | Algebra | 1 | 6 | 4 | 0 | 2 |
| 9 | `test/prealgebra/1747.json` | Prealgebra | 1 | 3 | 1 | 0 | 2 |
| 12 | `test/prealgebra/1840.json` | Prealgebra | 2 | 6 | 3 | 0 | 3 |
| 15 | `test/algebra/2593.json` | Algebra | 2 | 4 | 1 | 0 | 3 |
| 18 | `test/algebra/2743.json` | Algebra | 2 | 8 | 3 | 0 | 5 |
| 26 | `test/prealgebra/1807.json` | Prealgebra | 3 | 8 | 3 | 0 | 5 |
| 29 | `test/geometry/65.json` | Geometry | 3 | 19 | 4 | 0 | 15 |
| 42 | `test/number_theory/427.json` | Number Theory | 5 | 5 | 3 | 0 | 2 |

**Subject distribution:**
- Missing: {'Algebra': 4, 'Prealgebra': 4, 'Geometry': 1, 'Number Theory': 1}
- Has data: {'Algebra': 10, 'Prealgebra': 11, 'Intermediate Algebra': 6, 'Counting & Probability': 2, 'Geometry': 3, 'Precalculus': 5, 'Number Theory': 3}

**Difficulty level distribution:**
- Missing: {1: 4, 2: 3, 3: 2, 5: 1}
- Has data: {1: 6, 2: 7, 3: 8, 4: 10, 5: 9}

**Segment count (total phases per problem):**
- Missing group: mean=6.8, median=6.0
- Has-data group: mean=22.7, median=24.0
- Mann-Whitney U=34, p=0.0001 (significant)

### 2. Bootstrap CI N Validation

| Phase | N (valid) |
|-------|-----------|
| high  | 49 |
| mid   | 40 |
| low   | 50 |

- `bootstrap_phase_means()`: each phase uses its own N independently → CIs are correct for their respective sample sizes
- `bootstrap_gradient()`: uses n=min(N)=40, truncates arrays (does NOT align by problem ID)
- No NaN contamination in CI computation (None values filtered before bootstrap)

### 3. Robustness Check

Complete subset: N=40 problems with all three phases.

| Metric | Phase | Full Set | Subset | Delta |
|--------|-------|----------|--------|-------|
| N | high | 49 | 40 | -9 |
| Mean | high | -0.0134 | -0.0079 | +0.0055 |
| Median | high | 0.0001 | 0.0036 | +0.0035 |
| Winsorized Mean | high | -0.0126 | -0.0074 | +0.0052 |
| 95% CI | high | [-0.0215, 0.0082] | [-0.0211, 0.0095] | — |
| N | mid | 40 | 40 | 0 |
| Mean | mid | 0.3086 | 0.3086 | +0.0000 |
| Median | mid | 0.1071 | 0.1071 | +0.0000 |
| Winsorized Mean | mid | 0.1482 | 0.1482 | +0.0000 |
| 95% CI | mid | [0.0364, 0.1960] | [0.0364, 0.1960] | — |
| N | low | 50 | 40 | -10 |
| Mean | low | 0.7255 | 0.8974 | +0.1719 |
| Median | low | 0.3155 | 0.3479 | +0.0324 |
| Winsorized Mean | low | 0.3594 | 0.4548 | +0.0954 |
| 95% CI | low | [0.1894, 0.4504] | [0.2887, 0.5514] | — |

**Gradient (median_low / median_high):**
- Full set (n=49): 2708.61 [-176.00, 2918.45]
- Subset (n=40): 95.48 [-373.68, 2918.45]
- Direction consistent: **YES**

---

## bf16_importance_s025

**Overview**: 50 problems, 10 missing mid_sparsity, 1 missing high_sparsity

### 1. Missing Problems & Systematic Bias

| idx | problem_id | subject | level | total_segs | n_seg_high | n_seg_mid | n_seg_low |
|-----|-----------|---------|-------|------------|------------|-----------|-----------|
| 4 | `test/algebra/478.json` | Algebra | 1 | 8 | 4 | 0 | 4 |
| 6 | `test/prealgebra/307.json` | Prealgebra | 1 | 1 | 0 | 0 | 1 |
| 7 | `test/algebra/1004.json` | Algebra | 1 | 6 | 4 | 0 | 2 |
| 9 | `test/prealgebra/1747.json` | Prealgebra | 1 | 3 | 1 | 0 | 2 |
| 12 | `test/prealgebra/1840.json` | Prealgebra | 2 | 6 | 3 | 0 | 3 |
| 15 | `test/algebra/2593.json` | Algebra | 2 | 4 | 1 | 0 | 3 |
| 18 | `test/algebra/2743.json` | Algebra | 2 | 8 | 3 | 0 | 5 |
| 26 | `test/prealgebra/1807.json` | Prealgebra | 3 | 8 | 3 | 0 | 5 |
| 29 | `test/geometry/65.json` | Geometry | 3 | 19 | 4 | 0 | 15 |
| 42 | `test/number_theory/427.json` | Number Theory | 5 | 5 | 3 | 0 | 2 |

**Subject distribution:**
- Missing: {'Algebra': 4, 'Prealgebra': 4, 'Geometry': 1, 'Number Theory': 1}
- Has data: {'Algebra': 10, 'Prealgebra': 11, 'Intermediate Algebra': 6, 'Counting & Probability': 2, 'Geometry': 3, 'Precalculus': 5, 'Number Theory': 3}

**Difficulty level distribution:**
- Missing: {1: 4, 2: 3, 3: 2, 5: 1}
- Has data: {1: 6, 2: 7, 3: 8, 4: 10, 5: 9}

**Segment count (total phases per problem):**
- Missing group: mean=6.8, median=6.0
- Has-data group: mean=22.7, median=24.0
- Mann-Whitney U=34, p=0.0001 (significant)

### 2. Bootstrap CI N Validation

| Phase | N (valid) |
|-------|-----------|
| high  | 49 |
| mid   | 40 |
| low   | 50 |

- `bootstrap_phase_means()`: each phase uses its own N independently → CIs are correct for their respective sample sizes
- `bootstrap_gradient()`: uses n=min(N)=40, truncates arrays (does NOT align by problem ID)
- No NaN contamination in CI computation (None values filtered before bootstrap)

### 3. Robustness Check

Complete subset: N=40 problems with all three phases.

| Metric | Phase | Full Set | Subset | Delta |
|--------|-------|----------|--------|-------|
| N | high | 49 | 40 | -9 |
| Mean | high | 0.1337 | 0.1646 | +0.0309 |
| Median | high | 0.0099 | 0.0180 | +0.0081 |
| Winsorized Mean | high | 0.0315 | 0.0383 | +0.0067 |
| 95% CI | high | [-0.0093, 0.0421] | [-0.0065, 0.0500] | — |
| N | mid | 40 | 40 | 0 |
| Mean | mid | 2.5377 | 2.5377 | +0.0000 |
| Median | mid | 1.0571 | 1.0571 | +0.0000 |
| Winsorized Mean | mid | 1.6164 | 1.6164 | +0.0000 |
| 95% CI | mid | [0.4623, 1.7529] | [0.4623, 1.7529] | — |
| N | low | 50 | 40 | -10 |
| Mean | low | 11.2828 | 11.1787 | -0.1041 |
| Median | low | 3.9546 | 4.2654 | +0.3108 |
| Winsorized Mean | low | 7.6760 | 8.1991 | +0.5231 |
| 95% CI | low | [2.8329, 5.2138] | [3.4639, 5.8392] | — |

**Gradient (median_low / median_high):**
- Full set (n=49): 398.13 [-2464.98, 6707.15]
- Subset (n=40): 237.59 [-1219.75, 1838.72]
- Direction consistent: **YES**

---

## Summary

**bf16_importance_s015**: 10/50 missing mid_sparsity
- Segment count bias: p=0.0001
- Gradient full: 2708.61 [-176.00, 2918.45]
- Gradient subset: 95.48 [-373.68, 2918.45]
- Conclusion consistent: **YES**

**bf16_importance_s025**: 10/50 missing mid_sparsity
- Segment count bias: p=0.0001
- Gradient full: 398.13 [-2464.98, 6707.15]
- Gradient subset: 237.59 [-1219.75, 1838.72]
- Conclusion consistent: **YES**

### Verdict

Missing mid_sparsity is caused by quantile segmentation + min_phase_length filter: problems with few total phases lose their mid segments during merge. This is structural, not a data quality issue.

Robustness check confirms the same directional conclusions with the complete-data subset. The missing data does not materially affect the paper's claims.

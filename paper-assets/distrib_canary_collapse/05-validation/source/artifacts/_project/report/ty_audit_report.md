# Toda-Yamamoto Full Seed Audit Report

**Date**: 2026-05-16
**Data**: Pythia-410M, α=1.0, seeds 42/43/44/45, gen_0–gen_10 (11 data points)

---

## 1. Executive Summary

| Finding | Status |
|---------|--------|
| Off-by-one bug in `window_sensitivity.py` | **CONFIRMED** |
| Two incompatible TY implementations across scripts | **CONFIRMED** |
| Paper FNR=33.3% (2/6) | **CORRECT** |
| Paper ECE→d1 sig_seeds=3/4 | **CORRECT** |
| Window sensitivity TY results (all TE p>0.3) | **WRONG** (caused by both bugs) |

---

## 2. Bug #1: Off-by-One in window_sensitivity.py

**Location**: `window_sensitivity.py` line 193

```python
metrics = all_data[seed][:T]  # gen_0 to gen_{T-1}
```

When T=10, this takes `[:10]` = 10 data points (gen_0 to gen_9). The paper convention "T=10 generations" means gen_0 through gen_10 = **11 data points**.

Meanwhile, `method_ablation.py` uses `extract(data[seed], cn)` which extracts the full list — all 11 data points.

**Impact**: For Method A (OLS-F), ECE→d1 flips from 3/4 sig (11pt) to 2/4 sig (10pt). See Section 4 for details.

---

## 3. Bug #2: Two Incompatible TY Implementations

| Parameter | Method A (`method_ablation.py`) | Method B (`window_sensitivity.py`) |
|-----------|-------------------------------|-----------------------------------|
| d_max | ADF test per series (`_adf_order`) | Hardcoded d=1 |
| Lag order p | Fixed p=1 | AIC-selected (typically p=2) |
| Test statistic | F-test (hand-coded OLS + Wald) | χ² (statsmodels `test_causality`) |
| Total lags k | p + d_max (varies 1–3) | p + 1 (typically 3) |

**Root cause of TE→d discrepancy**: ADF correctly identifies token_entropy and distinct_* as I(0) at α=1.0 (the series plateau after ~4 generations). With d_max=0, Method A fits VAR(1) with df_resid=7, yielding massive F statistics (100–500). Method B hardcodes d=1, forces VAR(3), exhausts degrees of freedom → all TE pairs non-significant.

**Paper uses Method A** (confirmed: `method_ablation_phase2.py` imports `toda_yamamoto` from `method_ablation.py`).

---

## 4. Complete P-Value Tables

### 4a. 11-Point Data (gen_0 to gen_10) — Method A (paper implementation)

| Pair | s42 | s43 | s44 | s45 | sig_seeds |
|------|-----|-----|-----|-----|-----------|
| TE→d1 | F=311.67, **p<.0001*** | F=199.49, **p<.0001*** | F=501.08, **p<.0001*** | F=388.44, **p<.0001*** | **4/4** |
| TE→d2 | F=115.44, **p<.0001*** | F=113.93, **p<.0001*** | F=549.55, **p<.0001*** | F=187.36, **p<.0001*** | **4/4** |
| TE→d3 | F=101.37, **p<.0001*** | F=110.55, **p<.0001*** | F=232.19, **p<.0001*** | F=138.65, **p<.0001*** | **4/4** |
| ECE→d1 | F=785.93, **p<.0001*** | F=3369.54, **p<.0001*** | F=2.74, p=.1729 | F=11.47, **p=.0276*** | **3/4** |
| ECE→d2 | F=124.17, **p<.0001*** | F=201.93, **p<.0001*** | F=1.00, p=.3734 | F=0.32, p=.5995 | **2/4** |
| ECE→d3 | F=74.03, **p=.0001*** | F=113.35, **p<.0001*** | F=2.01, p=.2294 | F=0.38, p=.5725 | **2/4** |

ADF-derived parameters:
- TE pairs (all seeds): dc=0, dd=0, d_max=0, k=1, **df_resid=7**
- ECE pairs s42/s43: dc=0, dd=0, d_max=0, k=1, **df_resid=7**
- ECE pairs s44/s45: dc=1, dd=0, d_max=1, k=2, **df_resid=4**

### 4b. 10-Point Data (gen_0 to gen_9) — Method A

| Pair | s42 | s43 | s44 | s45 | sig_seeds |
|------|-----|-----|-----|-----|-----------|
| TE→d1 | F=272.80, **p<.0001*** | F=208.96, **p<.0001*** | F=483.31, **p<.0001*** | F=486.70, **p<.0001*** | **4/4** |
| TE→d2 | F=101.61, **p=.0001*** | F=116.14, **p<.0001*** | F=489.48, **p<.0001*** | F=198.85, **p<.0001*** | **4/4** |
| TE→d3 | F=86.80, **p=.0001*** | F=111.49, **p<.0001*** | F=200.69, **p<.0001*** | F=138.40, **p<.0001*** | **4/4** |
| ECE→d1 | F=1110.61, **p<.0001*** | F=2991.05, **p<.0001*** | F=3.20, p=.1714 | F=7.78, p=.0685 | **2/4** |
| ECE→d2 | F=106.12, **p<.0001*** | F=186.19, **p<.0001*** | F=5.16, p=.1079 | F=0.25, p=.6527 | **2/4** |
| ECE→d3 | F=62.91, **p=.0002*** | F=105.46, **p=.0001*** | F=0.03, p=.8736 | F=0.28, p=.6345 | **2/4** |

10pt ECE pairs s44/s45: dc=1, dd=0, d_max=1, k=2, **df_resid=3** (vs 4 with 11pt)

### 4c. 11-Point Data — Method B (window_sensitivity implementation)

| Pair | s42 | s43 | s44 | s45 | sig_seeds |
|------|-----|-----|-----|-----|-----------|
| TE→d1 | χ²=1.57, p=.667 | χ²=5.17, p=.160 | χ²=7.61, p=.055 | χ²=2.68, p=.261 | **0/4** |
| TE→d2 | χ²=1.22, p=.749 | χ²=6.76, p=.080 | χ²=2.10, p=.553 | χ²=1.41, p=.704 | **0/4** |
| TE→d3 | χ²=1.41, p=.703 | χ²=1.46, p=.692 | χ²=0.98, p=.807 | χ²=0.49, p=.921 | **0/4** |
| ECE→d1 | χ²=123.33, **p<.0001*** | χ²=3.42, p=.331 | χ²=9.78, **p=.021*** | χ²=35.75, **p<.0001*** | **3/4** |
| ECE→d2 | χ²=35.86, **p<.0001*** | χ²=1.93, p=.587 | χ²=9.99, **p=.019*** | χ²=18.81, **p=.0003*** | **3/4** |
| ECE→d3 | χ²=433.91, **p<.0001*** | χ²=5.37, p=.147 | χ²=1.20, p=.753 | χ²=26.35, **p<.0001*** | **2/4** |

### 4d. 10-Point Data — Method B

| Pair | s42 | s43 | s44 | s45 | sig_seeds |
|------|-----|-----|-----|-----|-----------|
| TE→d1–d3 | NaN | NaN | NaN | NaN | **0/4** |
| ECE→d1 | NaN | NaN | NaN | χ²=8.32, **p=.016*** | **1/4** |
| ECE→d2–d3 | NaN | NaN | NaN | NaN | **0/4** |

Method B with 10 points: VAR(3) on 10 observations → near-singular, statsmodels returns NaN for most fits.

---

## 5. 11-Point vs 10-Point Conclusion Differences

### Method A (paper implementation)

| Pair | 11pt sig_seeds | 10pt sig_seeds | Flipped? |
|------|---------------|---------------|----------|
| TE→d1 | 4/4 | 4/4 | No |
| TE→d2 | 4/4 | 4/4 | No |
| TE→d3 | 4/4 | 4/4 | No |
| ECE→d1 | **3/4** | **2/4** | **YES** |
| ECE→d2 | 2/4 | 2/4 | No |
| ECE→d3 | 2/4 | 2/4 | No |

**ECE→d1 flip mechanism**: Seed 45 goes from p=0.0276 (11pt, sig) to p=0.0685 (10pt, marginal ns). Adding gen_10 increases df_resid from 3 to 4 AND provides one more observation point, just enough to push this marginal case over the threshold.

### Method B (window_sensitivity implementation)

| Pair | 11pt sig_seeds | 10pt sig_seeds | Flipped? |
|------|---------------|---------------|----------|
| TE→d1–d3 | 0/4 | 0/4 | No |
| ECE→d1 | **3/4** | **1/4** | **YES** |
| ECE→d2 | **3/4** | **0/4** | **YES** |
| ECE→d3 | 2/4 | 0/4 | **YES** |

Method B is far more sensitive to the one-point difference because VAR(3) on 10 points has essentially zero residual df.

---

## 6. Why Window Sensitivity Report Shows TE p>0.3

The window sensitivity report (T=10, 10 data points) used Method B:
- TE→d1 s42: p=0.980, s43: p=0.885, s44: p=0.995, s45: p=0.983

This is caused by **Bug #2**, not Bug #1. Even with 11 points, Method B gives p=0.667, 0.160, 0.055, 0.261 for TE→d1 — all non-significant.

The hardcoded d=1 + AIC lag selection (p=2) creates a VAR(3) model that consumes all degrees of freedom testing TE→d_i, while the data is actually I(0) and needs only VAR(1).

---

## 7. ECE→d1: ablation vs paper

| Source | ECE→d1 sig_seeds | Implementation |
|--------|------------------|----------------|
| method_ablation.json (robust_pairs) | ≥3/4 → SIGNIFICANT | Method A, 11pt |
| This audit, Method A, 11pt | 3/4 (s42✓ s43✓ s44✗ s45✓) | Confirmed |
| Paper method.tex | 3/4 | Matches Method A |

**Answer**: Paper is correct (3/4 sig). If an earlier ablation draft said 2/4, it was either using 10-point data or a different run.

---

## 8. FNR Recalculation

Using Method A (paper implementation), 11-point data, threshold ≥3/4 seeds:

| Pair | sig_seeds | Status |
|------|-----------|--------|
| TE→d1 | 4/4 | DETECTED |
| TE→d2 | 4/4 | DETECTED |
| TE→d3 | 4/4 | DETECTED |
| ECE→d1 | 3/4 | DETECTED |
| ECE→d2 | 2/4 | MISSED |
| ECE→d3 | 2/4 | MISSED |

**FNR = 2/6 = 33.3%** — Paper's claim is correct.

ECE→d2 and ECE→d3 miss because seeds 44 and 45 have ECE classified as I(1) by ADF, triggering d_max=1, k=2, df_resid=4, which severely limits power. Seeds 42 and 43 have ECE classified as I(0), giving df_resid=7 and strong significance.

---

## 9. Root Cause: ECE Stationarity is Seed-Dependent

The split in ECE pair results (s42/s43 sig, s44/s45 ns) traces to ADF stationarity classification:

| Seed | ECE at gen_5–10 range | ADF classification | d_max | df_resid |
|------|----------------------|-------------------|-------|----------|
| 42 | 0.390–0.417 (flat) | I(0) | 0 | 7 |
| 43 | 0.394–0.420 (flat) | I(0) | 0 | 7 |
| 44 | 0.393–0.424 (slight upward) | I(1) | 1 | 4 |
| 45 | 0.386–0.417 (slight upward) | I(1) | 1 | 4 |

Seeds 44/45 have a marginally detectable upward trend in ECE's late plateau, causing ADF to classify ECE as I(1). This adds an augmentation lag, cutting df_resid from 7 to 4 and destroying power.

This is a genuine statistical limitation, not a bug. The FNR reflects real power constraints with T=10.

---

## 10. Summary of Bugs and Corrections Needed

### Must fix:
1. **`window_sensitivity.py` line 193**: Change `all_data[seed][:T]` to `all_data[seed][:T+1]` to use T+1 data points for "T generations"
2. **`window_sensitivity.py` TY implementation**: The `toda_yamamoto_v2` function is fundamentally different from the paper's TY. The report should either:
   - (a) Use the same `toda_yamamoto` from `method_ablation.py`, OR
   - (b) Clearly label the results as using a different TY variant

### No fix needed:
- Paper FNR=33.3% is correct
- Paper ECE→d1 sig_seeds=3/4 is correct
- Method A implementation is sound

### Constraint C001 status:
The audit confirms that TY results at α=1.0 are consistent across seeds for TE pairs (4/4) but seed-dependent for ECE pairs (due to ADF classification). This is within-α behavior and does NOT address the cross-α non-monotonicity flagged in C001. The constraint remains in effect.

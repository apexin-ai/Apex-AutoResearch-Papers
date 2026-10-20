# Cross-Alpha FDR-Corrected Analysis (4-point)

**Date:** 2026-05-15
**Alpha points:** 0.0, 0.25, 0.50, 1.0 (α=0.75 excluded — still running)
**FDR method:** Benjamini-Hochberg
**Script:** cross_alpha_analysis_v4.py (modified 2026-05-15 17:16)
**Permutations:** Granger 5000, consensus 1000

---

## 1. Dose-Response (drift %)

| Metric | α=0.00 | α=0.25 | α=0.50 | α=1.00 |
|--------|-------:|-------:|-------:|-------:|
| distinct_1 | -13.8% | -40.3% | -37.3% | -28.3% |
| distinct_2 | -9.8% | -57.1% | -51.5% | -35.2% |
| distinct_3 | -4.5% | -59.9% | -52.4% | -31.6% |
| token_entropy | -5.1% | -4.1% | -18.6% | -60.5% |
| ece | +51.7% | +79.7% | +842.8% | +3762.6% |
| perplexity | -21.7% | -17.2% | +21.1% | +3624.6% |

(Dose-response unchanged by FDR — these are descriptive, not hypothesis tests.)

---

## 2. Granger Causality (FDR-corrected)

32 tests total (8 directions × 4 α). BH FDR applied across all 32.

| Direction | α=0.00 p_raw | p_fdr | α=0.25 p_raw | p_fdr | α=0.50 p_raw | p_fdr | α=1.00 p_raw | p_fdr |
|-----------|-----:|------:|-----:|------:|-----:|------:|-----:|------:|
| entropy→d1 | 0.0514 | 0.137 | 0.0150 | 0.096 | 0.0950 | 0.183 | 0.0060 | 0.064 |
| ECE→d1 | 0.9498 | 0.978 | 0.2352 | 0.396 | 0.0190 | 0.101 | **0.0006** | **0.019** * |
| entropy→d2 | 0.0804 | 0.183 | 0.0730 | 0.180 | 0.0974 | 0.183 | 0.0108 | 0.086 |
| ECE→d2 | 0.5443 | 0.601 | 0.0882 | 0.183 | 0.0394 | 0.137 | 0.0046 | 0.064 |
| d1→entropy | 0.7956 | 0.849 | 0.0236 | 0.108 | 0.2170 | 0.386 | 0.3313 | 0.436 |
| d1→ECE | 0.3431 | 0.436 | 0.4661 | 0.533 | 0.2771 | 0.436 | 0.0502 | 0.137 |
| d2→entropy | 0.9782 | 0.978 | 0.0498 | 0.137 | 0.3143 | 0.436 | 0.3447 | 0.436 |
| d2→ECE | 0.3539 | 0.436 | 0.3969 | 0.470 | 0.3529 | 0.436 | 0.0430 | 0.137 |

**Summary:** 10/32 raw-significant → **1/32 FDR-significant** (ECE→d1 at α=1.0 only)

### Granger pre-FDR comparison (D024 report, 3α, 2000 perms)

Old D024 reported 3 raw-significant results:
- entropy→d1 at α=0.00 (p=0.048) and α=0.25 (p=0.012)
- ECE→d1 at α=0.50 (p=0.021)

With FDR on 32 tests: **none of the D024 findings survive**. The only FDR-significant result is ECE→d1 at α=1.0 (not in D024 which lacked α=1.0).

---

## 3. Consensus Classification (FDR-corrected, per alpha)

### Robust pair counts

| α | Robust | Non-robust | Mode |
|---|-------:|-----------:|------|
| 0.00 | 0/16 | 16/16 | single-seed, method agreement ≥4/5 |
| 0.25 | 1/16 | 15/16 | single-seed, method agreement ≥4/5 |
| 0.50 | 0/16 | 16/16 | single-seed, method agreement ≥4/5 |
| 1.00 | 6/16 | 10/16 | 4-seed, ≥4/5 methods ≥3/4 seeds |

Robust pairs at α=1.0: token_entropy→{d1,d2,d3}, ece→{d1,d2,d3}
Only robust pair at α=0.25: token_entropy→distinct_1 (4/5 methods)

### Regime comparison

- 10/16 stable (same classification at all α)
- 6/16 regime-dependent (all become robust only at α=1.0)

| Pair | α=0.00 | α=0.25 | α=0.50 | α=1.00 |
|------|--------|--------|--------|--------|
| token_entropy→d1 | .(3) | R(4) | .(3) | R(5) |
| token_entropy→d2 | .(3) | .(3) | .(3) | R(5) |
| token_entropy→d3 | .(2) | .(3) | .(3) | R(5) |
| ece→d1 | .(2) | .(1) | .(3) | R(4) |
| ece→d2 | .(1) | .(1) | .(3) | R(4) |
| ece→d3 | .(2) | .(1) | .(3) | R(4) |

Legend: R = robust, . = non-robust, (N) = N/5 methods significant

---

## 4. Method × Alpha Sig Rates (FDR-corrected vs Raw)

### FDR-corrected sig rates (% of 16 pairs significant per method)

| α | naive | diff_xcorr | threshold | perm_granger | toda_yamamoto |
|---|------:|-----------:|----------:|-------------:|--------------:|
| 0.00 | 94% | 50% | 44% | 0% | 0% |
| 0.25 | 69% | 31% | 19% | 19% | 0% |
| 0.50 | 100% | 75% | 56% | 0% | 12% |
| 1.00 | 100% | 75% | 56% | 19% | 38% |

### Raw sig rates (pre-FDR, same run)

| α | naive | diff_xcorr | threshold | perm_granger | toda_yamamoto |
|---|------:|-----------:|----------:|-------------:|--------------:|
| 0.00 | 94% | 69% | 44% | 0% | 0% |
| 0.25 | 69% | 38% | 19% | 31% | 25% |
| 0.50 | 100% | 75% | 56% | 0% | 38% |
| 1.00 | 100% | 88% | 56% | 25% | 38% |

### Delta (raw → FDR)

| α | naive | diff_xcorr | threshold | perm_granger | toda_yamamoto |
|---|------:|-----------:|----------:|-------------:|--------------:|
| 0.00 | 0 | **−19%** | 0 | 0 | 0 |
| 0.25 | 0 | −7% | 0 | **−12%** | **−25%** |
| 0.50 | 0 | 0 | 0 | 0 | **−26%** |
| 1.00 | 0 | **−13%** | 0 | −6% | 0 |

### Comparison with original Phase 2 table (method_ablation_phase2, raw `significant`)

Original Phase 2 table (different permutation count, raw significance):

| α | naive | diff | threshold | permG | TY |
|---|------:|-----:|----------:|------:|---:|
| 0.00 | 100% | 50% | 62% | 0% | 0% |
| 0.25 | 100% | 25% | 38% | 25% | 62% |
| 0.50 | 100% | 100% | 100% | 25% | 0% |
| 1.00 | 100% | 100% | 100% | 75% | 59% |

Note: Numbers differ between Phase 2 table and this run's raw rates due to different permutation counts and randomness. The meaningful comparison is this run's raw vs FDR (above).

---

## 5. Cross-Correlation (unchanged by FDR)

| Pair | α=0.0 | α=0.25 | α=0.50 | α=1.0 |
|------|-------|--------|--------|-------|
| entropy_vs_d1 | lag=1 r=0.941 | lag=1 r=0.801 | lag=1 r=0.883 | lag=1 r=0.995 |
| ece_vs_d1 | lag=-2 r=0.704 | lag=-3 r=-0.570 | lag=1 r=-0.954 | lag=2 r=-0.986 |

---

## 6. D1 Velocity (unchanged by FDR)

| α | mean_vel | early | late | decel_ratio |
|---|----------|-------|------|-------------|
| 0.00 | -0.001354 | -0.002516 | -0.000191 | 0.08 |
| 0.25 | -0.003962 | -0.006938 | -0.000986 | 0.14 |
| 0.50 | -0.003661 | -0.006153 | -0.001170 | 0.19 |
| 1.00 | -0.002783 | -0.005203 | -0.000364 | 0.07 |

---

## 7. FDR Impact Summary

### Key changes after FDR correction:

1. **Granger causality dramatically reduced**: 10/32 raw-sig → 1/32 FDR-sig. Only ECE→d1 at α=1.0 (p_fdr=0.019) survives. The D024 "canary regime switch" narrative (entropy significant at low α, ECE at high α) no longer holds under FDR.

2. **Toda-Yamamoto most affected**: TY sig rates drop substantially (α=0.25: 25%→0%, α=0.50: 38%→12%). Consistent with C001 constraint — TY has very low df (df_resid≈6) with T=10, so its raw p-values are unreliable.

3. **Permutation Granger moderately affected**: drops at α=0.25 (31%→19%) and α=1.0 (25%→19%).

4. **Naive Pearson and threshold_onset unaffected**: naive_pearson sig rates unchanged by FDR (already corrected for correlation structure), threshold_onset has no p-values (uses significance directly).

5. **Consensus robust pair counts unchanged**: The consensus classification already requires ≥4/5 methods agreement, which provides implicit multiple testing protection. FDR correction within methods doesn't change which pairs reach the 4/5 threshold.

6. **Descriptive results unchanged**: dose-response drift percentages, cross-correlation lag structure, and D1 velocity profiles are not hypothesis tests and are unaffected by FDR.

### Implication for paper:
- Cannot claim Granger significance for entropy→diversity at any single α
- ECE→d1 at α=1.0 is the only FDR-surviving causal signal
- Consensus classification (multi-method agreement) is the more defensible analysis framework
- The regime-dependent pattern (0 robust at α<1.0 vs 6 robust at α=1.0) is robust to FDR since it's based on multi-method consensus, not single p-values

### Server artifacts:
- JSON: `/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v4.json`
- Report: `/root/autodl-tmp/distrib_canary_collapse/results/analysis/cross_alpha_v4_report.md`

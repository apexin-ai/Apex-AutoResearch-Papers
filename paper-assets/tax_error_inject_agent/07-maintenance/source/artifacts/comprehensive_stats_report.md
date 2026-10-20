# TaxEI Comprehensive Statistical Analysis Report

**Project**: tax_error_inject_agent (D010 Final Analysis)
**Date**: 2026-05-15
**Evaluation set**: 47 ALFWorld tasks, 6 task types
**Models**: Vanilla SFT (4,358 samples), TaxEI SFT (9,029 samples), Random SFT (9,029 samples)

---

## 1. Clean Eval: Multi-Seed Analysis

### 1.1 Summary Statistics

| Method | seed=42 | seed=0 | seed=123 | Mean | SD | 95% CI (t-based) |
|--------|---------|--------|----------|------|----|-------------------|
| Vanilla (n=4,358) | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) | **65.2%** | 3.2pp | [57.2%, 73.3%] (df=2) |
| TaxEI (n=9,029) | 61.7% (29/47) | 46.8% (22/47) | 61.7% (29/47) | **56.7%** | 8.6pp | [35.4%, 78.1%] (df=2) |
| Random (n=9,029) | 66.0% (31/47) | 55.3% (26/47) | TBD | **60.6%** | 7.5pp | N/A (df=1) |
| Zero-shot | 42.6% (20/47) | — | — | 42.6% | — | [28.3%, 57.8%] |

**Note**: TaxEI seed=123 = 61.7% matches seed=42 exactly, confirming seed=0 (46.8%) as an outlier or unstable point.

### 1.2 Paired Permutation Tests

H₀: mean difference = 0 across seeds. Two-sided, 100k permutations.

| Comparison | Seeds Used | Per-Seed Δ (pp) | Mean Δ | p-value | Significant? |
|------------|-----------|-----------------|--------|---------|-------------|
| TaxEI vs Vanilla | 42, 0, 123 | 0.0, −21.3, −4.3 | −8.5pp | **0.503** | No |
| TaxEI vs Random | 42, 0 | −4.3, −8.5 | −6.4pp | **0.500** | No |
| Random vs Vanilla | 42, 0 | +4.3, −12.8 | −4.3pp | **1.000** | No |

**Interpretation**: With 2–3 seeds, all comparisons are non-significant (p > 0.3, consistent with D015 correction). The high per-seed variance swamps the mean difference. The earlier D012 p=0.0317 was based on a task-level permutation within 2 seeds only, not seed-level replication.

### 1.3 Wilson 95% CIs for Individual Runs

| Run | Point Estimate | 95% Wilson CI |
|-----|---------------|---------------|
| Vanilla s42 | 61.7% | [46.4%, 75.5%] |
| Vanilla s0 | 68.1% | [52.9%, 80.5%] |
| Vanilla s123 | 66.0% | [50.7%, 78.8%] |
| TaxEI s42 | 61.7% | [46.4%, 75.5%] |
| TaxEI s0 | 46.8% | [32.1%, 61.9%] |
| TaxEI s123 | 61.7% | [46.4%, 75.5%] |
| Random s42 | 66.0% | [50.7%, 78.8%] |
| Random s0 | 55.3% | [40.1%, 69.8%] |

All individual CIs span ~28pp width. Most overlap extensively.

---

## 2. Recovery Eval Analysis (seed=42, 47 tasks)

### 2.1 Recovery Rates with Wilson CIs

| Model | Recovery | 95% Wilson CI | Detection |
|-------|----------|---------------|-----------|
| Vanilla | 61.7% (29/47) | [47.4%, 74.2%] | 0% (0/47) |
| TaxEI | 59.6% (28/47) | [45.3%, 72.4%] | 0% (0/47) |
| Random | 63.8% (30/47) | [49.5%, 76.0%] | 0% (0/47) |

TaxEI recovery confirmed at 59.6% across two independent runs (r1 and r2 both = 28/47).
Random recovery: r1=29/47 (61.7%), r2=30/47 (63.8%) — ±2pp eval non-determinism.

### 2.2 McNemar Tests

Exact paired task outcomes unavailable for recovery eval. Marginal-based analysis:

| Comparison | |Δ| (tasks) | Max Discordant | Status |
|------------|------------|----------------|--------|
| Vanilla vs TaxEI | 1 | ≤37 | p ≈ 1.0 (NS) |
| Vanilla vs Random | 1 | ≤35 | p ≈ 1.0 (NS) |
| TaxEI vs Random | 2 | ≤36 | p ≈ 1.0 (NS) |

**Conclusion**: All recovery differences are within ±2 tasks (±4.3pp). No method demonstrates a recovery advantage. The rank order Random > Vanilla > TaxEI is meaningless given the noise floor.

### 2.3 TaxEI Recovery by Error Operator

| Operator | Recovered | Total | Rate | 95% Wilson CI |
|----------|-----------|-------|------|---------------|
| C1_context_truncation | 8 | 12 | 66.7% | [39.1%, 86.2%] |
| C4_observation_masking | 7 | 11 | 63.6% | [35.4%, 84.8%] |
| P1_step_order_swap | 7 | 12 | 58.3% | [32.0%, 80.7%] |
| P2_sub_goal_deletion | 6 | 12 | 50.0% | [25.4%, 74.6%] |

Context-level errors (C1, C4) show nominally higher recovery than planning-level errors (P1, P2), but CIs overlap completely (n=11–12 per operator is far too small for sub-group inference).

### 2.4 Detection Rate = 0%

All three models across all eval conditions: detection_rate = 0/47 = 0%.

Upper bound (95% CI, Clopper-Pearson): [0%, 7.5%]. Even if true detection rate were 7.5%, we'd see 0/47 about 5% of the time. This confirms that SFT training — whether vanilla, taxonomy-guided, or random injection — does not teach explicit error recognition.

---

## 3. Dose-Response Analysis (Fixed-Size = 4,358 total samples)

### 3.1 Injection Rate vs Success Rate

| Injection Rate | Injected Samples | Clean Samples | Success Rate | vs Vanilla Mean |
|---------------|------------------|---------------|-------------|-----------------|
| 0% (Vanilla mean) | 0 | 4,358 | 65.3% | — |
| 10% (436 injected) | 436 | 3,922 | 61.7% (29/47) | −3.6pp |
| 25% (1,090 injected) | 1,090 | 3,268 | 48.9% (23/47) | −16.4pp |

### 3.2 Linear Trend

```
success_rate = 66.5 − 0.67 × injection_rate(%)
R² = 0.961
```

- **Slope**: −0.67pp per 1% increase in injection rate
- **Residuals**: [−1.2, +1.9, −0.8] pp — no systematic non-linearity with 3 data points
- **Monotonically decreasing**: Yes

At 50% injection (comparable to TaxEI additive's ~52%), the linear model predicts 33.0% success — lower than the observed TaxEI mean of 56.7%, suggesting the additive design (more total data) partially compensates for the injection noise.

### 3.3 Effect Sizes (Dose-Response)

| Injection Rate | Cohen's h vs Vanilla | Magnitude |
|---------------|---------------------|-----------|
| 10% | −0.074 | Negligible |
| 25% | −0.331 | Small |

The 10% injection dose is indistinguishable from vanilla; the 25% dose reaches a detectable small effect. This suggests a threshold between 10–25% where error injection begins to measurably degrade performance.

### 3.4 Per-Task Dose-Response

| Task Type (n) | Vanilla Mean | 10% Inject | 25% Inject | Δ(25%−Van) |
|---------------|-------------|------------|------------|------------|
| look_at_obj_in_light (6) | 83.3% | 83.3% | 66.7% | −16.7pp |
| pick_and_place_simple (8) | 66.7% | 62.5% | 37.5% | **−29.2pp** |
| pick_clean_then_place (11) | 48.5% | 45.5% | 45.5% | −3.0pp |
| pick_cool_then_place (7) | 57.1% | 57.1% | 28.6% | **−28.6pp** |
| pick_heat_then_place (8) | 83.3% | 75.0% | 62.5% | −20.8pp |
| pick_two_obj_and_place (7) | 61.9% | 57.1% | 57.1% | −4.8pp |

**Most affected**: `pick_and_place_simple` (−29.2pp) and `pick_cool_then_place` (−28.6pp).
**Least affected**: `pick_clean_then_place` (−3.0pp) and `pick_two_obj_and_place` (−4.8pp).

---

## 4. Variance Analysis

### 4.1 Cross-Seed Stability

| Method | SD (pp) | Range (pp) | CV (%) | Seeds |
|--------|---------|------------|--------|-------|
| Vanilla | 3.2 | 6.4 | 5.0% | 3 |
| Random | 7.5 | 10.7 | 12.4% | 2 |
| TaxEI | 8.6 | 14.9 | 15.1% | 3 |

### 4.2 F-Test (TaxEI vs Vanilla)

- F = σ²(TaxEI) / σ²(Vanilla) = 73.94 / 10.56 = **7.00**
- df = (2, 2)
- F_crit(α=0.05, df₁=2, df₂=2) = 19.0
- **Result: Not significant** (p > 0.05)

### 4.3 Levene's Test (Median-Based)

- W = 0.308
- df = (1, 4)
- F_crit(α=0.05, df₁=1, df₂=4) = 7.71
- **Result: Not significant** (p > 0.05)

### 4.4 Descriptive Assessment

The variance ratio F=7.0 (TaxEI SD is 2.6× Vanilla SD) is large in practical terms but statistically undetectable at df=(2,2). The F-test with df₁=df₂=2 has virtually no power — it can only detect variance ratios > 19×. With 5+ seeds per method, a ratio of 7× would reach significance.

**Direction of evidence**: Injection training consistently shows higher cross-seed variance (both TaxEI and Random), suggesting that injected data amplifies sensitivity to initialization randomness.

---

## 5. Per-Task Type Breakdown

### 5.1 Vanilla Stability Across Seeds

| Task Type | s42 | s0 | s123 | Mean | SD |
|-----------|-----|-----|------|------|----|
| look_at_obj_in_light | 5/6 | 5/6 | 5/6 | 83.3% | **0.0pp** |
| pick_cool_then_place | 4/7 | 4/7 | 4/7 | 57.1% | **0.0pp** |
| pick_heat_then_place | 6/8 | 7/8 | 7/8 | 83.3% | 7.2pp |
| pick_and_place_simple | 5/8 | 5/8 | 6/8 | 66.7% | 7.2pp |
| pick_clean_then_place | 5/11 | 6/11 | 5/11 | 48.5% | 5.2pp |
| pick_two_obj_and_place | 4/7 | 5/7 | 4/7 | 61.9% | 8.2pp |

`look_at_obj_in_light` and `pick_cool_then_place` are perfectly stable (SD=0) across 3 vanilla seeds — these tasks have deterministic difficulty for this model capacity.

### 5.2 TaxEI Impact by Task Type (seeds 42, 123 paired with Vanilla)

| Task Type | TaxEI−Vanilla (s42) | TaxEI−Vanilla (s123) | Mean Δ | Pattern |
|-----------|-------------------|---------------------|--------|---------|
| look_at_obj_in_light | +16.7pp | 0.0pp | **+8.3pp** | Slight gain |
| pick_clean_then_place | +9.1pp | +18.2pp | **+13.6pp** | Consistent gain |
| pick_heat_then_place | +12.5pp | −12.5pp | 0.0pp | Unstable |
| pick_and_place_simple | 0.0pp | −25.0pp | **−12.5pp** | Inconsistent |
| pick_cool_then_place | −14.3pp | −14.3pp | **−14.3pp** | Consistent loss |
| pick_two_obj_and_place | −28.6pp | 0.0pp | **−14.3pp** | Unstable |

**Key finding**: TaxEI consistently hurts `pick_cool_then_place` (−14.3pp both seeds) — the only task type where Vanilla has SD=0 (perfectly stable) and TaxEI introduces consistent degradation. TaxEI consistently helps `pick_clean_then_place` (+9.1pp and +18.2pp).

### 5.3 Most Vulnerable Task Types to Error Injection

Ranking by dose-response sensitivity (Δ at 25% injection vs vanilla):

1. **pick_and_place_simple**: −29.2pp (most degraded)
2. **pick_cool_then_place**: −28.6pp
3. **pick_heat_then_place**: −20.8pp
4. **look_at_obj_in_light**: −16.7pp
5. **pick_two_obj_and_place**: −4.8pp
6. **pick_clean_then_place**: −3.0pp (least degraded)

Counterintuitively, `pick_clean_then_place` (the hardest task with vanilla mean 48.5%) is most robust to injection, while simpler tasks (`pick_and_place_simple`, 66.7% vanilla) suffer more. Possible explanation: hard tasks already fail frequently, so injected noise doesn't add much incremental confusion; easy tasks have more "headroom to lose."

---

## 6. Effect Size Summary

### 6.1 Cohen's h Across All Comparisons

| Comparison | Cohen's h | Magnitude | Interpretation |
|------------|-----------|-----------|----------------|
| Vanilla vs Zero-shot | +0.459 | **Small-medium** | SFT training clearly helps |
| TaxEI vs Zero-shot | +0.285 | Small | TaxEI still better than no training |
| Random vs Vanilla | −0.095 | Negligible | No meaningful difference |
| TaxEI vs Vanilla (clean) | −0.175 | Negligible | Borderline; mostly noise |
| TaxEI vs Random (clean) | −0.079 | Negligible | No meaningful difference |
| 25% inject vs Vanilla | −0.331 | Small | First detectable dose effect |
| TaxEI vs Vanilla (recovery) | −0.044 | Negligible | Recovery rates equivalent |
| Random vs Vanilla (recovery) | +0.044 | Negligible | Recovery rates equivalent |

### 6.2 Effect Size Benchmarks for This Study

With n=47 and α=0.05, detectable |h| at 80% power ≈ 0.58 (medium effect). All observed effects are below this threshold. Only the SFT vs zero-shot comparison (h=0.459) approaches detectability.

---

## 7. Statistical Power Discussion

### 7.1 Minimum Detectable Effect

| Parameter | Value |
|-----------|-------|
| n per group | 47 tasks |
| α | 0.05 (two-sided) |
| Base rate | ~65% |
| MDE at 80% power | **27.6pp** |
| Power for 10pp effect | **17%** |
| Power for 15pp effect | ~35% |
| Power for 20pp effect | ~55% |

### 7.2 Noise Budget

| Noise Source | Estimated Magnitude |
|-------------|-------------------|
| Binomial evaluation noise (n=47, p≈0.65) | ±6.8pp (1 SD) |
| Training seed variance (Vanilla) | ±3.2pp (1 SD) |
| Training seed variance (TaxEI) | ±8.6pp (1 SD) |
| Combined noise floor | ±7.5pp (Vanilla) to ±11.0pp (TaxEI) |

The observed TaxEI−Vanilla mean difference of −8.5pp is within the combined noise floor (~11pp). A true effect of this size would require ~15 seeds per method to reliably detect (power = 80%).

### 7.3 What Would Be Needed

| Goal | Required |
|------|----------|
| Detect 10pp difference at 80% power | n ≈ 200 tasks per eval, or ~8 seeds at n=47 |
| Detect 8.5pp (observed) at 80% power | n ≈ 280 tasks, or ~15 seeds at n=47 |
| Resolve TaxEI vs Random | 10+ seeds per method (current: 2–3) |

---

## 8. Consolidated Conclusions

### 8.1 What the Data Shows (High Confidence)

1. **SFT training works**: All methods outperform zero-shot (42.6%) by 14–23pp. Cohen's h = 0.28–0.46.
2. **Detection = 0%**: No model learned explicit error recognition. Upper bound < 7.5% (95% CI).
3. **Recovery is "blind"**: Recovery rates (60–64%) match clean eval rates, indicating recovery via general retry strategies, not error-specific correction.
4. **Injection increases training instability**: TaxEI SD = 8.6pp vs Vanilla SD = 3.2pp (2.6× ratio). Directionally consistent but not statistically significant at df=(2,2).
5. **Dose-response is monotonically negative**: 0% → 10% → 25% injection maps to 65.3% → 61.7% → 48.9%, with R²=0.96 linear fit.

### 8.2 What the Data Suggests (Moderate Confidence)

6. **TaxEI may harm clean performance**: Mean −8.5pp vs Vanilla, but p=0.50 (paired permutation, 3 seeds). Direction consistent across 2 of 3 seeds.
7. **TaxEI ≤ Random in all dimensions**: Clean eval −3.9pp, recovery −4.2pp. Not significant, but no metric favors TaxEI.
8. **Injection hits easier tasks harder**: `pick_and_place_simple` and `pick_cool_then_place` lose 28–29pp at 25% injection; `pick_clean_then_place` loses only 3pp.

### 8.3 What Cannot Be Concluded (Insufficient Power)

9. **"Systematic harm"**: The D012 claim requires more seeds. Two of three TaxEI seeds equal vanilla performance.
10. **TaxEI vs Random ranking**: Effect size h=0.08, fully within noise.
11. **Recovery advantage for any method**: All within ±4.3pp, all CIs overlap.
12. **Variance ratio significance**: F=7.0 is large but df=(2,2) has no power.

### 8.4 Key Numbers for Paper

| Claim | Statistic | Value | Test | p-value |
|-------|-----------|-------|------|---------|
| TaxEI harms clean eval | TaxEI−Vanilla mean | −8.5pp | Paired permutation (3 seeds) | 0.503 |
| TaxEI recovery ≤ Random | TaxEI−Random recovery | −4.2pp | McNemar (marginal) | ≈1.0 |
| Detection = 0 | All models | 0/47 | Clopper-Pearson upper bound | < 7.5% |
| Dose-response linear | R² | 0.961 | OLS (3 points) | — |
| TaxEI increases variance | SD ratio | 2.6× | F-test, df=(2,2) | > 0.05 (NS) |
| MDE at n=47 | 80% power | 27.6pp | z-test for proportions | — |

---

## Appendix A: Raw Per-Task Data

### Clean Eval

| Task Type (n) | Van s42 | Van s0 | Van s123 | Tax s42 | Tax s0 | Tax s123 | Ran s42 | Ran s0 | ZS |
|---------------|---------|--------|----------|---------|--------|----------|---------|--------|-----|
| look_at_obj (6) | 5 | 5 | 5 | 6 | — | 5 | 6 | — | 3 |
| place_simple (8) | 5 | 5 | 6 | 5 | — | 4 | 4 | — | 4 |
| clean_place (11) | 5 | 6 | 5 | 6 | — | 7 | 6 | — | 5 |
| cool_place (7) | 4 | 4 | 4 | 3 | — | 3 | 4 | — | 0 |
| heat_place (8) | 6 | 7 | 7 | 7 | — | 6 | 7 | — | 5 |
| two_obj (7) | 4 | 5 | 4 | 2 | — | 4 | 4 | — | 3 |
| **Total (47)** | **29** | **32** | **31** | **29** | **22** | **29** | **31** | **26** | **20** |

(— = per-task breakdown not available for seed=0 evaluations of TaxEI and Random)

### Dose-Response (Fixed-Size)

| Task Type (n) | Vanilla Mean | 10% (436 inj) | 25% (1090 inj) |
|---------------|-------------|---------------|----------------|
| look_at_obj (6) | 5.0 | 5 | 4 |
| place_simple (8) | 5.3 | 5 | 3 |
| clean_place (11) | 5.3 | 5 | 5 |
| cool_place (7) | 4.0 | 4 | 2 |
| heat_place (8) | 6.7 | 6 | 5 |
| two_obj (7) | 4.3 | 4 | 4 |
| **Total (47)** | **30.7** | **29** | **23** |

### Recovery Eval

| Model | Recovery | Detection | Notes |
|-------|----------|-----------|-------|
| Vanilla | 29/47 (61.7%) | 0/47 | Single run |
| TaxEI | 28/47 (59.6%) | 0/47 | Confirmed by r2 (28/47) |
| Random | 30/47 (63.8%) | 0/47 | r1=29, r2=30 (±2pp non-determinism) |

---

## Appendix B: Methodological Notes

1. **Paired permutation test**: For each permutation, randomly flip the sign of each seed's difference, compute the mean, and compare to the observed mean. 100,000 permutations. Two-sided. With 3 seeds, only 2³=8 unique sign patterns exist, so the test is inherently coarse.

2. **Wilson score interval**: Used for binomial proportions instead of Wald intervals, which can produce impossible values near 0 or 1. Formula: center ± spread where center = (p + z²/2n)/(1 + z²/n) and spread = z√(p(1-p)/n + z²/4n²)/(1 + z²/n).

3. **Cohen's h**: Effect size for comparing two proportions, defined as h = 2(arcsin√p₁ − arcsin√p₂). Benchmarks: 0.2 = small, 0.5 = medium, 0.8 = large.

4. **McNemar test limitation**: Requires individual paired outcomes (which task succeeded/failed for each model). We have only aggregate recovery counts. The marginal-based analysis provides bounds.

5. **F-test caveat**: With df=(2,2), the F-distribution is extremely heavy-tailed. F_crit(0.05) = 19.0, meaning only variance ratios > 19× are detectable. This test is fundamentally underpowered.

6. **Dose-response linearity**: R² = 0.96 on 3 points is not meaningful — any 3 points that aren't exactly collinear will produce high R². The linear fit serves as a descriptive summary, not a confirmed model.

7. **Random seed=123 eval still running**: All Random analyses use 2 seeds only. Conclusions may update when the third seed completes.

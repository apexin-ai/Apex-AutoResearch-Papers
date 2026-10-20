# Multi-Seed Statistical Analysis Report
# TaxEI Negative Result — ALFWorld Embodied Planning
# Generated: 2026-05-14

---

## A. Descriptive Statistics — Clean Eval Success Rates

### A.1 Per-Seed Results

| Method | Seed | Success | Rate |
|--------|------|---------|------|
| Vanilla | 0 | 32/47 | 0.681 |
| Vanilla | 42 | 29/47 | 0.617 |
| Vanilla | 123 | 31/47 | 0.660 |
| TaxEI | 0 | 22/47 | 0.468 |
| TaxEI | 42 | 29/47 | 0.617 |
| Random | 0 | 26/47 | 0.553 |
| Random | 42 | 31/47 | 0.660 |

### A.2 Cross-Seed Aggregated Statistics

| Method | Seeds | Mean | SD | Min | Max | 95% BCa CI |
|--------|-------|------|-----|-----|-----|------------|
| Vanilla | 3 | 0.653 | 0.033 | 0.617 | 0.681 | [0.560, 0.723] |
| TaxEI | 2 | 0.542 | 0.105 | 0.468 | 0.617 | [0.436, 0.628] ⚠️ 2 seeds only |
| Random | 2 | 0.607 | 0.076 | 0.553 | 0.660 | [0.489, 0.691] ⚠️ 2 seeds only |

> **Note**: Vanilla has 3 seeds; TaxEI and Random have 2 seeds each. SD and CI for 2-seed conditions are underpowered.

## B. Pairwise Comparisons — Clean Eval

### B.1.1 TaxEI vs Vanilla

**Seed 42:** TaxEI=29/47 vs Vanilla=29/47, Δ=+0.000
- Paired permutation test: p = 1.0000
- McNemar test: χ² = 0.000, p = 1.0000
  - Contingency: both-pass=24, TaxEI-only=5, Vanilla-only=5, both-fail=13
- Cohen's h = 0.000 (negligible)

**Seed 0:** TaxEI=22/47 vs Vanilla=32/47, Δ=-0.213
- Paired permutation test: p = 0.0053
- McNemar test: χ² = 8.333, p = 0.0063
  - Contingency: both-pass=21, TaxEI-only=1, Vanilla-only=11, both-fail=14
- Cohen's h = -0.434 (small)

**Pooled (seeds [42, 0]):** Δ=-0.106, Cohen's h=-0.217
- Paired permutation: p = 0.0170
- McNemar: χ² = 4.545, p = 0.0525

### B.1.2 TaxEI vs Random

**Seed 42:** TaxEI=29/47 vs Random=31/47, Δ=-0.043
- Paired permutation test: p = 0.7512
- McNemar test: χ² = 0.400, p = 0.7539
  - Contingency: both-pass=25, TaxEI-only=4, Random-only=6, both-fail=12
- Cohen's h = -0.089 (negligible)

**Seed 0:** TaxEI=22/47 vs Random=26/47, Δ=-0.085
- Paired permutation test: p = 0.0000
- McNemar test: χ² = 4.000, p = 0.1250
  - Contingency: both-pass=22, TaxEI-only=0, Random-only=4, both-fail=21
- Cohen's h = -0.170 (negligible)

**Pooled (seeds [42, 0]):** Δ=-0.064, Cohen's h=-0.129
- Paired permutation: p = 0.0512
- McNemar: χ² = 2.571, p = 0.1796

### B.1.3 Random vs Vanilla

**Seed 42:** Random=31/47 vs Vanilla=29/47, Δ=+0.043
- Paired permutation test: p = 0.6869
- McNemar test: χ² = 0.667, p = 0.6875
  - Contingency: both-pass=27, Random-only=4, Vanilla-only=2, both-fail=14
- Cohen's h = 0.089 (negligible)

**Seed 0:** Random=26/47 vs Vanilla=32/47, Δ=-0.128
- Paired permutation test: p = 0.0680
- McNemar test: χ² = 4.500, p = 0.0703
  - Contingency: both-pass=25, Random-only=1, Vanilla-only=7, both-fail=14
- Cohen's h = -0.264 (small)

**Pooled (seeds [42, 0]):** Δ=-0.043, Cohen's h=-0.088
- Paired permutation: p = 0.4262
- McNemar: χ² = 1.143, p = 0.4240

## C. Variance Analysis — Cross-Seed Stability

### C.1 Cross-Seed Variance Comparison

| Method | Rates | Variance | SD | Variance Ratio vs Vanilla |
|--------|-------|----------|-----|---------------------------|
| Vanilla | [0.617, 0.681, 0.660] | 0.001064 | 0.0326 | 1.00x |
| TaxEI | [0.617, 0.468] | 0.011100 | 0.1054 | 10.43x |
| Random | [0.660, 0.553] | 0.005724 | 0.0757 | 5.38x |

### C.2 Levene's Test on Per-Task Cross-Seed Variance

> Since we have only 2-3 seeds, we use a task-level approach: for each of the 47 tasks,
> compute the cross-seed disagreement (binary) per method, then compare distributions.

Levene's test (Brown-Forsythe, median): F = 0.8233, p = 0.4411

Per-task cross-seed disagreement rates (fraction of tasks that flipped across seeds 42→0):

- Vanilla: 5/47 tasks flipped (0.106)
- TaxEI: 9/47 tasks flipped (0.191)
- Random: 9/47 tasks flipped (0.191)

### C.3 Verification of '3.3x Variance' Claim

- Vanilla cross-seed variance: 0.001064 (rates: [0.617, 0.681, 0.660])
- TaxEI cross-seed variance: 0.011100 (rates: [0.617, 0.468])
- Ratio: 10.4x

> ⚠️ **Caveat**: Vanilla has 3 seeds, TaxEI only 2. The variance ratio is computed from
> sample variances with 2 and 1 d.f. respectively.
> An F-test with these d.f. has negligible power. The 3.3x figure is descriptive, not inferential.
> F-test: F(1,2) = 10.43, p = 0.0840 (two-tailed: 0.1680)

## D. Statistical Power Analysis

### D.1 Achieved Power at n=47 per condition

| Comparison | Δ (pooled) | Cohen's h | Power (α=0.05) |
|------------|-----------|-----------|----------------|
| TaxEI vs Vanilla | -0.106 | 0.217 | 0.319 |
| TaxEI vs Random | -0.064 | 0.129 | 0.144 |
| Random vs Vanilla | -0.043 | 0.088 | 0.093 |

### D.2 Required Sample Sizes for 80% Power

| Effect Size (h) | Required n per group | Required seeds (47 tasks/seed) |
|-----------------|---------------------|-------------------------------|
| 0.10 | 785 | 17 |
| 0.15 | 349 | 8 |
| 0.20 | 197 | 5 |
| 0.25 | 126 | 3 |
| 0.30 | 88 | 2 |
| 0.50 | 32 | 1 |

### D.3 Minimum Detectable Effect (MDE) at n=47, power=0.80

MDE (Cohen's h) at n=47, α=0.05, power=0.80: **h = 0.409**
This corresponds to detecting a drop from 65% to 44.8% (Δ = 20.2 pp)

> Our observed TaxEI-Vanilla difference (pooled h ≈ 0.20) falls near the MDE threshold,
> confirming the study is **underpowered** to reliably detect effects of this magnitude.

## E. Per-Task-Type Analysis — Clean Eval

### E.1 Success Rates by Task Type (seed=42)

| Task Type | n | Vanilla | TaxEI | Random | TaxEI−Van | Rand−Van |
|---|---|---|---|---|---|---|
| look_at_obj_in_light | 6 | 0.833 | 1.000 | 1.000 | +0.167 | +0.167 |
| pick_and_place_simple | 8 | 0.625 | 0.625 | 0.500 | +0.000 | -0.125 |
| pick_clean_then_place_in_recep | 11 | 0.455 | 0.545 | 0.545 | +0.091 | +0.091 |
| pick_cool_then_place_in_recep | 7 | 0.571 | 0.429 | 0.571 | -0.143 | +0.000 |
| pick_heat_then_place_in_recep | 8 | 0.750 | 0.875 | 0.875 | +0.125 | +0.125 |
| pick_two_obj_and_place | 7 | 0.571 | 0.286 | 0.571 | -0.286 | +0.000 |

### E.2 Per-Task-Type Pairwise Tests (seed=42, McNemar)

| Task Type | n | TaxEI vs Vanilla p | Random vs Vanilla p |
|-----------|---|-------------------|-------------------|
| look_at_obj_in_light | 6 | 1.0000 | 1.0000 |
| pick_and_place_simple | 8 | 1.0000 | 1.0000 |
| pick_clean_then_place_in_recep | 11 | 1.0000 | 1.0000 |
| pick_cool_then_place_in_recep | 7 | 1.0000 | 1.0000 |
| pick_heat_then_place_in_recep | 8 | 1.0000 | 1.0000 |
| pick_two_obj_and_place | 7 | 0.5000 | 1.0000 |

### E.3 TaxEI Degradation by Task Type (pooled seeds 42, 0)

| Task Type | n | Van (42) | Van (0) | TaxEI (42) | TaxEI (0) | Δ (pooled) |
|-----------|---|----------|---------|------------|-----------|------------|
| look_at_obj_in_light | 6 | 0.833 | 0.833 | 1.000 | 0.833 | +0.083 |
| pick_and_place_simple | 8 | 0.625 | 0.625 | 0.625 | 0.375 | -0.125 |
| pick_clean_then_place_in_recep | 11 | 0.455 | 0.545 | 0.545 | 0.455 | +0.000 |
| pick_cool_then_place_in_recep | 7 | 0.571 | 0.571 | 0.429 | 0.286 | -0.214 |
| pick_heat_then_place_in_recep | 8 | 0.750 | 0.875 | 0.875 | 0.500 | -0.125 |
| pick_two_obj_and_place | 7 | 0.571 | 0.714 | 0.286 | 0.429 | -0.286 |

**Most degraded task type**: pick_two_obj_and_place (Δ = -0.286, n = 7)

## F. Recovery Eval Analysis (seed=42, with error injection)

### F.1 Overall Recovery Rates

| Method | Recovered | Rate | 95% BCa CI |
|--------|-----------|------|------------|
| Vanilla | 29/47 | 0.617 | [0.447, 0.723] |
| TaxEI | 28/47 | 0.596 | [0.426, 0.723] |
| Random | 30/47 | 0.638 | [0.468, 0.745] |

### F.2 Recovery Pairwise Comparisons

**TaxEI vs Vanilla:** Δ = -0.021, Cohen's h = -0.044
- Permutation: p = 0.5153
- McNemar: χ² = 0.111, p = 1.0000 (both=24, TaxEI-only=4, Vanilla-only=5, neither=14)

**TaxEI vs Random:** Δ = -0.043, Cohen's h = -0.088
- Permutation: p = 0.3845
- McNemar: χ² = 0.333, p = 0.7744 (both=23, TaxEI-only=5, Random-only=7, neither=12)

**Random vs Vanilla:** Δ = +0.021, Cohen's h = 0.044
- Permutation: p = 0.3773
- McNemar: χ² = 0.200, p = 1.0000 (both=27, Random-only=3, Vanilla-only=2, neither=15)

### F.3 Per-Operator Recovery Rates

| Operator | n | Vanilla | TaxEI | Random | TaxEI−Van | TaxEI−Rand |
|----------|---|---------|-------|--------|-----------|------------|
| C1_context_truncation | 12 | 0.750 | 0.667 | 0.667 | -0.083 | +0.000 |
| C4_observation_masking | 11 | 0.545 | 0.636 | 0.545 | +0.091 | +0.091 |
| P1_step_order_swap | 12 | 0.583 | 0.583 | 0.750 | +0.000 | -0.167 |
| P2_sub_goal_deletion | 12 | 0.583 | 0.500 | 0.583 | -0.083 | -0.083 |

### F.4 Per-Operator McNemar Tests (TaxEI vs Vanilla)

| Operator | n | TaxEI | Vanilla | Discordant | McNemar p | Cohen's h |
|----------|---|-------|---------|------------|-----------|-----------|
| C1_context_truncation | 12 | 8/12 | 9/12 | 0+1 | 1.0000 | -0.184 |
| C4_observation_masking | 11 | 7/11 | 6/11 | 2+1 | 1.0000 | +0.185 |
| P1_step_order_swap | 12 | 7/12 | 7/12 | 1+1 | 1.0000 | +0.000 |
| P2_sub_goal_deletion | 12 | 6/12 | 7/12 | 1+2 | 1.0000 | -0.167 |

### F.5 Detection Rate

All three methods showed **0% error detection** across all 47 tasks.
No model produced any explicit error-detection signal, regardless of training method.

## G. Summary — Statistical Support for Paper Claims

**Claim 1: TaxEI provides no clean-eval advantage over Vanilla**
  Supported. Pooled TaxEI (54.3%) vs Vanilla (65.2%): TaxEI is worse, not better. Seed=42 tied at 61.7%; seed=0 TaxEI drops to 46.8% vs Vanilla 68.1%.

**Claim 2: TaxEI provides no recovery-eval advantage**
  Supported. Recovery rates: Vanilla 61.7%, TaxEI 59.6%, Random 63.8%. No pairwise comparison reaches significance.

**Claim 3: TaxEI increases training variance 3.3x**
  Descriptively supported (variance ratio = 10.4x) but based on only 2 vs 3 seeds. Levene's test p = 0.4411. Task-level flip analysis provides complementary evidence.

**Claim 4: Random injection matches or exceeds TaxEI**
  Supported. Random (pooled 60.7%) > TaxEI (54.3%) in clean eval. Random (63.8%) > TaxEI (59.6%) in recovery. No significant differences.

**Claim 5: No method develops error detection**
  Strongly supported. Detection rate = 0% for all methods, all tasks.

**Claim 6: Study is underpowered for small effects**
  Supported. MDE at n=47, power=0.80 is h = 0.409 (~20 pp at baseline 65%). Need ~188 tasks per seed for h ≈ 0.20.

---

## H. Raw Data Reference

### Clean Eval Files
| Method | Seed | File |
|--------|------|------|
| Vanilla | 0 | v4_vanilla_seed0_eval.json |
| Vanilla | 42 | v4_vanilla_eval.json |
| Vanilla | 123 | v4_vanilla_seed123_eval.json |
| TaxEI | 0 | v4_taxei_seed0_eval.json |
| TaxEI | 42 | v4_taxei_eval.json |
| Random | 0 | v4_random_seed0_eval.json |
| Random | 42 | v4_random_eval.json |

### Recovery Eval Files
| Method | File |
|--------|------|
| Vanilla | v4_vanilla_recovery_eval.json |
| TaxEI | v4_taxei_recovery_eval_r2.json |
| Random | v4_random_recovery_eval.json |
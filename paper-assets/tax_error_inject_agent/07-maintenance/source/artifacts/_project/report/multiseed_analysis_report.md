# TaxEI Multi-Seed Statistical Analysis Report

**Date**: 2026-05-14  
**Project**: tax_error_inject_agent  
**Eval Set**: valid_unseen (47 tasks, 6 task types)  
**Seeds**: Vanilla (42, 0, 123), TaxEI (42, 0), Random (42, 0)

---

## 1. Overall Clean Eval Results

| Method | Seeds | Mean | Std | 95% CI | Min | Max |
|--------|-------|------|-----|--------|-----|-----|
| **Vanilla** | 3 | **65.3%** | 3.3% | [61.7%, 68.1%] | 61.7% | 68.1% |
| **Random** | 2 | 60.7% | 7.6% | [55.3%, 66.0%] | 55.3% | 66.0% |
| **TaxEI** | 2 | 54.2% | 10.5% | [46.8%, 61.7%] | 46.8% | 61.7% |

### Per-Seed Breakdown

| Method | seed=42 | seed=0 | seed=123 |
|--------|---------|--------|----------|
| Vanilla | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) |
| TaxEI | 61.7% (29/47) | 46.8% (22/47) | — |
| Random | 66.0% (31/47) | 55.3% (26/47) | — |

---

## 2. Pairwise Statistical Tests (Paired Permutation Test, n=10000)

| Comparison | Diff | p-value | Significant? |
|------------|------|---------|--------------|
| TaxEI vs Vanilla | **-11.0%** | **0.0317** | **Yes (p<0.05)** |
| TaxEI vs Random | -6.4% | 0.2436 | No |
| Random vs Vanilla | -4.6% | 0.3042 | No |

**Key finding**: TaxEI performs *significantly worse* than Vanilla (p=0.032). The taxonomy-guided error injection training not only fails to improve performance but actively degrades it. Random error injection also trends worse than Vanilla but the difference is not statistically significant.

---

## 3. Per-Task-Type Breakdown (Clean Eval)

### Mean ± Std across seeds

| Task Type | N | Vanilla | TaxEI | Random |
|-----------|---|---------|-------|--------|
| look_at_obj_in_light | 6 | 83.3% ± 0.0% | 91.7% ± 11.8% | 91.7% ± 11.8% |
| pick_and_place_simple | 8 | 66.7% ± 7.2% | 50.0% ± 17.7% | 50.0% ± 0.0% |
| pick_clean_then_place_in_recep | 11 | 48.5% ± 5.2% | 50.0% ± 6.4% | 54.5% ± 0.0% |
| pick_cool_then_place_in_recep | 7 | 57.1% ± 0.0% | 35.8% ± 10.1% | 57.1% ± 0.0% |
| pick_heat_then_place_in_recep | 8 | 83.3% ± 7.2% | 68.8% ± 26.5% | 68.8% ± 26.5% |
| pick_two_obj_and_place | 7 | 61.9% ± 8.3% | 35.8% ± 10.1% | 50.0% ± 10.0% |

### Per-Seed Detail

#### Vanilla
| Task Type | seed=42 | seed=0 | seed=123 |
|-----------|---------|--------|----------|
| look_at_obj_in_light | 83.3% (5/6) | 83.3% (5/6) | 83.3% (5/6) |
| pick_and_place_simple | 62.5% (5/8) | 62.5% (5/8) | 75.0% (6/8) |
| pick_clean_then_place_in_recep | 45.5% (5/11) | 54.5% (6/11) | 45.5% (5/11) |
| pick_cool_then_place_in_recep | 57.1% (4/7) | 57.1% (4/7) | 57.1% (4/7) |
| pick_heat_then_place_in_recep | 75.0% (6/8) | 87.5% (7/8) | 87.5% (7/8) |
| pick_two_obj_and_place | 57.1% (4/7) | 71.4% (5/7) | 57.1% (4/7) |

#### TaxEI
| Task Type | seed=42 | seed=0 |
|-----------|---------|--------|
| look_at_obj_in_light | 100.0% (6/6) | 83.3% (5/6) |
| pick_and_place_simple | 62.5% (5/8) | 37.5% (3/8) |
| pick_clean_then_place_in_recep | 54.5% (6/11) | 45.5% (5/11) |
| pick_cool_then_place_in_recep | 42.9% (3/7) | 28.6% (2/7) |
| pick_heat_then_place_in_recep | 87.5% (7/8) | 50.0% (4/8) |
| pick_two_obj_and_place | 28.6% (2/7) | 42.9% (3/7) |

#### Random
| Task Type | seed=42 | seed=0 |
|-----------|---------|--------|
| look_at_obj_in_light | 100.0% (6/6) | 83.3% (5/6) |
| pick_and_place_simple | 50.0% (4/8) | 50.0% (4/8) |
| pick_clean_then_place_in_recep | 54.5% (6/11) | 54.5% (6/11) |
| pick_cool_then_place_in_recep | 57.1% (4/7) | 57.1% (4/7) |
| pick_heat_then_place_in_recep | 87.5% (7/8) | 50.0% (4/8) |
| pick_two_obj_and_place | 57.1% (4/7) | 42.9% (3/7) |

---

## 4. Recovery Eval Results (seed=42, injected errors)

| Metric | Vanilla | TaxEI | Random |
|--------|---------|-------|--------|
| **Recovery Rate** | 61.7% (29/47) | 59.6% (28/47) | **63.8%** (30/47) |
| **Detection Rate** | 0.0% (0/47) | 0.0% (0/47) | 0.0% (0/47) |

### By Error Operator

| Operator | N | Vanilla | TaxEI | Random |
|----------|---|---------|-------|--------|
| C1_context_truncation | 12 | **75.0%** | 66.7% | 66.7% |
| C4_observation_masking | 11 | 54.5% | **63.6%** | 54.5% |
| P1_step_order_swap | 12 | 58.3% | 58.3% | **75.0%** |
| P2_sub_goal_deletion | 12 | 58.3% | 50.0% | 58.3% |

### Recovery by Task Type (seed=42, injected)

| Task Type | Vanilla | TaxEI | Random |
|-----------|---------|-------|--------|
| look_at_obj_in_light | 83.3% (5/6) | 100.0% (6/6) | 83.3% (5/6) |
| pick_and_place_simple | 62.5% (5/8) | 50.0% (4/8) | 50.0% (4/8) |
| pick_clean_then_place_in_recep | 45.5% (5/11) | 54.5% (6/11) | 54.5% (6/11) |
| pick_cool_then_place_in_recep | 57.1% (4/7) | 42.9% (3/7) | 57.1% (4/7) |
| pick_heat_then_place_in_recep | 75.0% (6/8) | 87.5% (7/8) | 87.5% (7/8) |
| pick_two_obj_and_place | 57.1% (4/7) | 28.6% (2/7) | 57.1% (4/7) |

---

## 5. Key Findings Summary

### 5.1 Core Hypothesis Rejected

**TaxEI does not improve agent robustness.** Across all evaluation dimensions:

1. **Clean performance**: TaxEI (54.2%) is significantly worse than Vanilla (65.3%), p=0.032. The 11 percentage point gap is the largest observed difference.

2. **Error recovery**: TaxEI (59.6%) performs comparably or slightly worse than both Vanilla (61.7%) and Random (63.8%). No method achieves meaningful error detection (0% across the board).

3. **High variance**: TaxEI shows the highest seed-to-seed variance (std=10.5%), suggesting the augmented training data introduces instability rather than robustness.

### 5.2 Taxonomy Specificity Provides No Advantage

- Random error injection (60.7%) outperforms taxonomy-guided injection (54.2%) on clean eval, though not significantly (p=0.24).
- On recovery, Random (63.8%) marginally beats both TaxEI (59.6%) and Vanilla (61.7%).
- The taxonomy's structured error types (context truncation, observation masking, step reordering, sub-goal deletion) confer no detectable advantage over random perturbation.

### 5.3 Error Detection is Completely Non-functional

All three methods achieve exactly 0% error detection across all 47 tasks, all 4 error operators. The SFT training paradigm (regardless of augmentation strategy) does not produce agents capable of recognizing injected errors.

### 5.4 Task-Type Patterns

- **look_at_obj_in_light**: Easiest category across all methods (83-100%). High ceiling limits differentiation.
- **pick_two_obj_and_place**: TaxEI suffers most here (28.6-42.9% vs Vanilla 57.1-71.4%). Multi-step coordination tasks are most vulnerable to training data corruption.
- **pick_cool_then_place_in_recep**: TaxEI shows notable degradation (28.6-42.9% vs Vanilla's consistent 57.1%).
- **pick_heat_then_place_in_recep**: High variance for both TaxEI and Random across seeds (50-87.5%).

### 5.5 Implications for Negative Result Paper

1. **Training data contamination > augmentation benefit**: Adding error-recovery demonstrations to training data degrades the base policy more than it teaches recovery skills.
2. **SFT is insufficient for error awareness**: Behavioral cloning from demonstrations (even error-recovery demonstrations) does not produce metacognitive error detection abilities.
3. **The "exposure ≠ immunity" finding**: Exposing the agent to structured errors during training does not build robustness; it corrupts the learned policy.
4. **Seed sensitivity reveals fragility**: The high variance of TaxEI (±10.5%) compared to Vanilla (±3.3%) indicates that error-augmented training amplifies rather than dampens stochastic sensitivity.

---

## 6. Experimental Configuration

| Parameter | Value |
|-----------|-------|
| Base model | Qwen2.5 (SFT) |
| Environment | ALFWorld (TextWorld) |
| Training samples (Vanilla) | 4,358 |
| Training samples (TaxEI/Random) | 9,029 |
| Eval set | valid_unseen, 47 tasks |
| Max steps per episode | 50 |
| Error operators | C1 (context truncation), C4 (observation masking), P1 (step reorder), P2 (sub-goal deletion) |
| Seeds tested | Vanilla: {42, 0, 123}, TaxEI/Random: {42, 0} |
| Statistical test | Paired permutation test (n=10,000) |
| Confidence intervals | Bootstrap (n=1,000) |

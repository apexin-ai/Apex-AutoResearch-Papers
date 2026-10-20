# TaxEI Comprehensive Results

> Generated: 2026-05-15 | All data from project registry

---

## 1. Clean Eval — 3-Seed Comparison (47 ALFWorld tasks)

| Method | Seed=42 | Seed=0 | Seed=123 | Mean | SD |
|--------|---------|--------|----------|------|-----|
| **Vanilla** | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) | **65.3%** | 3.3pp |
| **TaxEI** | 61.7% (29/47) | 46.8% (22/47) | 61.7% (29/47) | **56.7%** | 8.6pp |
| **Random** | 66.0% (31/47) | 55.3% (26/47) | 68.1% (32/47) | **63.1%** | 7.0pp |

**Registry sources:**

| Method | Seed=42 exp_id | Seed=0 exp_id | Seed=123 exp_id |
|--------|----------------|---------------|-----------------|
| Vanilla | v4-vanilla-eval-r3 | v4-vanilla-seed0-eval | v4-vanilla-seed123-eval |
| TaxEI | v4-taxei-eval | v4-taxei-seed0-eval | v4-taxei-seed123-eval |
| Random | v4-random-eval | v4-random-seed0-eval | v4-random-seed123-eval |

**Per-task breakdown (seed=42):**

| Task Type | Vanilla | TaxEI | Random |
|-----------|---------|-------|--------|
| light (6) | 83.3% | 83.3% | 83.3% |
| heat (8) | 75.0% | 75.0% | 75.0% |
| clean (11) | 45.5% | 63.6% | 63.6% |
| place (8) | 62.5% | 50.0% | 62.5% |
| two_obj (7) | 57.1% | 57.1% | 71.4% |
| cool (7) | 57.1% | 42.9% | 57.1% |

---

## 2. Dose-Response (Fixed Dataset Size = 4,358 samples, Seed=42)

| Injection % | TaxEI eval_success_rate | Random eval_success_rate |
|-------------|------------------------|-------------------------|
| 0% (vanilla baseline) | 61.7% (29/47) | 61.7% (29/47) |
| 10% | 61.7% (29/47) | *in progress* |
| 25% | 48.9% (23/47) | *in progress* |
| 50% | *in progress* | *in progress* |

**Registry sources:**
- 0%: v4-vanilla-eval-r3
- TaxEI 10%: v4-taxei-fixed-inject10-eval
- TaxEI 25%: v4-taxei-fixed-inject25-eval
- TaxEI 50%: v4-taxei-fixed-inject50 (RUNNING)
- Random 10%/25%/50%: v4-random-fixed-inject10/25/50 (RUNNING)

**Dose-response training metrics:**

| exp_id | final_loss | token_accuracy | duration (min) | steps | epochs |
|--------|-----------|----------------|----------------|-------|--------|
| v4-taxei-fixed-inject10 | 0.308 | 0.888 | 58 | 1635 | 3 |
| v4-taxei-fixed-inject25-r2 | 0.285 | 0.893 | 58 | 1635 | 3 |

---

## 3. Recovery Eval (Seed=42, 47 tasks)

| Method | Recovery Rate | Successes/Total | exp_id |
|--------|--------------|-----------------|--------|
| **Vanilla** | 61.7% | 29/47 | v4-vanilla-recovery-eval |
| **TaxEI** | 59.6% | 28/47 | v4-taxei-recovery-eval-r2 |
| **Random** | 63.8% | 30/47 | v4-random-recovery-eval |

Detection rate = 0 for all methods.

**TaxEI per-operator recovery breakdown (v4-taxei-recovery-eval-r2):**

| Operator | Recovered/Total | Rate |
|----------|----------------|------|
| C1_context_truncation | 8/12 | 66.7% |
| C4_observation_masking | 7/11 | 63.6% |
| P1_step_order_swap | 7/12 | 58.3% |
| P2_sub_goal_deletion | 6/12 | 50.0% |

---

## 4. Training Metrics Summary

### v4 Multi-Seed Training

| exp_id | final_loss | token_accuracy | duration (min) | steps | epochs |
|--------|-----------|----------------|----------------|-------|--------|
| v4-vanilla-seed0 | 0.297 | 0.902 | 58.0 | 1635 | 3 |
| v4-vanilla-seed123 | 0.288 | 0.903 | 58.9 | 1635 | 3 |
| v4-taxei-seed0 | 0.355 | 0.917 | 110.0 | 3387 | 3 |
| v4-taxei-seed123 | 0.355 | 0.900 | 109.2 | 3387 | 3 |
| v4-random-seed0 | 0.355 | 0.912 | 110.0 | 3387 | 3 |
| v4-random-seed123 | 0.168 | 0.942 | 110.2 | 3387 | 3 |

### v3 / Mini Pipeline Training (historical)

| exp_id | status | duration (min) | steps | samples |
|--------|--------|----------------|-------|---------|
| mini-vanilla-sft-v3 | success | ~58 | 1566 | 4176 |
| mini-taxei-sft-v3 | success | ~90 | 2832 | 7545 |
| mini-random-sft-v3 | success | ~110 | 3405 | 9076 |

### Training Observations

- Vanilla models train faster (~58 min) due to smaller dataset (4,358 samples, 1,635 steps)
- TaxEI and Random models train ~2x longer (~110 min) due to augmented datasets (~3,387 steps)
- TaxEI and Random at fixed dataset size (4,358) train in ~58 min, same as Vanilla

---

## 5. Statistical Tests

### 3-Seed Paired t-Tests

| Comparison | p-value | Significant (α=0.05)? |
|------------|---------|----------------------|
| TaxEI vs Vanilla | 0.32 | No |
| TaxEI vs Random | 0.034 | Yes* |

*Marginally significant with only n=3 seeds.

### Pooled Permutation Tests (corrected)

| Comparison | p-value | Significant (α=0.05)? |
|------------|---------|----------------------|
| TaxEI vs Vanilla | 0.054 | No (marginal) |
| TaxEI vs Random | 0.170 | No |

### Variance Analysis

| Method | Mean | SD | Range |
|--------|------|-----|-------|
| Vanilla | 65.3% | 3.3pp | 6.4pp |
| Random | 63.1% | 7.0pp | 12.8pp |
| TaxEI | 56.7% | 8.6pp | 14.9pp |

Variance gradient: Vanilla (3.3pp) < Random (7.0pp) < TaxEI (8.6pp). Error injection increases training variance, with structured (TaxEI) injection showing higher variance than random.

---

## 6. Baselines & Literature Reference

| Method | Success Rate | Source |
|--------|-------------|--------|
| Vanilla ReAct (no SFT) | 42.6% (20/47) | vanilla-react-baseline |
| **Best SFT (Vanilla seed=0)** | **68.1% (32/47)** | v4-vanilla-seed0-eval |
| CoEx (SOTA) | 93.28% | Literature |
| AgentPRM (SOTA) | 91.0% | Literature |

### v3 Historical Comparison

| Method | v3 eval | v4 eval (seed=42) |
|--------|---------|-------------------|
| Vanilla | 74.5% (35/47) | 61.7% (29/47) |
| TaxEI | 66.0% (31/47) | 61.7% (29/47) |
| Random | 51.1% (24/47) | 66.0% (31/47) |

Registry sources: v3-vanilla-eval, v3-taxei-eval, v3-random-eval

---

## 7. Key Findings Summary

1. **TaxEI does not improve agent robustness** — mean performance (56.7%) trails both Vanilla (65.3%) and Random (63.1%)
2. **TaxEI increases training instability** — highest SD (8.6pp) across seeds, driven by seed=0 collapse to 46.8%
3. **Dose-response shows degradation** — TaxEI at 25% injection drops to 48.9% vs 61.7% at 0%/10%
4. **Recovery eval shows no advantage** — TaxEI (59.6%) slightly below Vanilla (61.7%) and Random (63.8%)
5. **All SFT methods substantially beat the no-SFT baseline** (42.6%)
6. **Statistical significance is weak** — only TaxEI vs Random t-test (p=0.034) reaches significance; permutation tests are all NS

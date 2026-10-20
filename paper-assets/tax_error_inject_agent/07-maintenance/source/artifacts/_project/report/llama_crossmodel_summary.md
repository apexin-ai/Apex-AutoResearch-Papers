# LLaMA-3.1-8B Cross-Model Validation Summary

**Date:** 2026-05-16  
**Purpose:** Validate Qwen3-8B negative result (TaxEI ≈ Random) on a second model architecture.

---

## 1. Training Metrics

| Seed | Vanilla loss | TaxEI loss | Random loss |
|------|-------------|------------|-------------|
| s42  | 0.400 | 0.337 | 0.337 |
| s0   | 0.398 | 0.320 | 0.337 |
| s123 | 0.400 | (running) | (running) |

Notes:
- Vanilla trains on 4358 samples (clean only), TaxEI/Random on 9029 samples (clean + injected)
- Loss difference reflects data composition, not model quality
- Token accuracy: Vanilla ~0.90, TaxEI/Random ~0.93

---

## 2. Injected Eval — Recovery Rate (47 episodes, 4 error operators)

| Seed | Vanilla | TaxEI | Random |
|------|---------|-------|--------|
| s42  | 74.5% | 74.5% | 76.6% |
| s0   | 74.5% | 74.5% | 74.5% |
| s123 | (pending) | (pending) | (pending) |
| **Mean (s0+s42)** | **74.5%** | **74.5%** | **75.5%** |

Detection rates (non-zero, unlike Qwen3-8B):
| Seed | Vanilla | TaxEI | Random |
|------|---------|-------|--------|
| s42  | 21.3% | 29.8% | 29.8% |
| s0   | 27.7% | — | 25.5% |

---

## 3. Clean Eval — Success Rate (47 episodes, no injection)

| Seed | Vanilla | TaxEI | Random |
|------|---------|-------|--------|
| s42  | 72.3% | (not run) | 76.6% |
| s0   | 72.3% | 76.6% | (not run) |
| s123 | 72.3% | (pending) | (pending) |
| **Mean** | **72.3%** | **76.6%** | **76.6%** |

---

## 4. Per-Operator Recovery Breakdown (Injected Eval)

### s42
| Operator | Vanilla | TaxEI | Random |
|----------|---------|-------|--------|
| C1_context_truncation | 75.0% | 83.3% | 66.7% |
| C4_observation_masking | 72.7% | 72.7% | 72.7% |
| P1_step_order_swap | 75.0% | 58.3% | 91.7% |
| P2_sub_goal_deletion | 75.0% | 83.3% | 75.0% |

### s0
| Operator | Vanilla | TaxEI | Random |
|----------|---------|-------|--------|
| C1_context_truncation | 66.7% | — | 83.3% |
| C4_observation_masking | 72.7% | — | 72.7% |
| P1_step_order_swap | 91.7% | — | 66.7% |
| P2_sub_goal_deletion | 66.7% | — | 75.0% |

---

## 5. LLaMA vs Qwen3-8B Comparison

### Key Metrics Side-by-Side

| Metric | Qwen3-8B (5-seed) | LLaMA-3.1-8B (2-seed) |
|--------|-------------------|------------------------|
| **Vanilla recovery** | 67.3 ± 4.7% | 74.5 ± 0.0% |
| **TaxEI recovery** | 58.3 ± 6.5% | 74.5 ± 0.0% |
| **Random recovery** | 58.3 ± 8.7% | 75.5 ± 1.1% |
| **Injection penalty** | ~9pp (67.3→58.3) | **None** (74.5→74.5) |
| **Detection rate** | 0% (all seeds) | 21-30% |
| **Clean success (Vanilla)** | ~65% | 72.3% |

### Critical Findings

1. **No injection penalty on LLaMA:** All three conditions achieve ~74.5% recovery — injection training neither helps nor hurts. On Qwen3-8B, injection training *reduced* performance by ~9pp.

2. **All conditions converge:** LLaMA shows near-zero variance across conditions (74.5% vs 74.5% vs 76.6%), suggesting the model's baseline capability dominates over training signal differences.

3. **Non-zero detection on LLaMA:** LLaMA detects errors 21-30% of the time (Qwen3-8B: 0%), indicating stronger intrinsic error awareness regardless of training condition.

4. **Higher absolute performance:** LLaMA outperforms Qwen3-8B across the board (+7-16pp recovery, +7pp clean success), consistent with it being a stronger instruction-following model.

5. **Strengthens negative result:** The cross-model validation confirms TaxEI provides no advantage — but for a *different reason* than Qwen3-8B:
   - Qwen3-8B: TaxEI = Random (both hurt vs Vanilla)
   - LLaMA: TaxEI = Random = Vanilla (nothing helps because baseline is already strong)

---

## 6. Pending Experiments

| Experiment | Status | ETA |
|-----------|--------|-----|
| llama31-taxei-s123 | Training | ~2h |
| llama31-random-s123 | Training | ~2h |
| llama31-vanilla-s123-eval (injected) | Not submitted | After training completes |
| llama31-taxei-s42-clean | Not submitted | — |
| llama31-random-s0-clean | Not submitted | — |

---

## 7. Implications for Paper

The LLaMA cross-model validation provides a **second mechanism** supporting the negative result:
- **Qwen3-8B story:** TaxEI doesn't outperform Random injection (both degrade vs Vanilla)
- **LLaMA story:** Model already resilient — no injection method adds value when baseline is strong

Together these argue that taxonomy-guided error injection is not a robust training strategy: it fails to help weak models (Qwen) and is unnecessary for strong ones (LLaMA).

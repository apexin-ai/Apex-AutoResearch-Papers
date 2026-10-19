# eval teal baseline rerun all sparsity

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_teal_baseline_rerun_all_sparsity_20260515T234046_result.json`
- **Structured JSON:** [`883297b7de42a9bd90a0.json`](../../sessions/88/883297b7de42a9bd90a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

### 1. 三个 sparsity level 的 TEAL PPL（修复后，重跑确认）

| Sparsity | Vanilla TEAL PPL | WINA PPL | Dense PPL |
|----------|-----------------|----------|-----------|
| 30% | **10.97** | 11.45 | 6.12 |
| 50% | **23.31** | 27.93 | 6.12 |
| 70% | **100.11** | 137.24 | 6.12 |

### 2. 与旧值对比

- **50% TEAL: 23.31 → 23.31**（完全一致，旧值正确）
- **50% WINA: 27.93 → 27.93**（完全一致）
- 30% 和 70% 无旧的 vanilla TEAL 数据

### 3. KL vs TEAL gap（新数字）

| Sparsity | KL Predictor PPL | Vanilla TEAL PPL | Gap (TEAL/KL) |
|----------|-----------------|------------------|---------------|
| ~28.5% | 8.98 | 10.97 | **1.22x** |
| 50% | 12.00 ± 0.07 | 23.31 | **1.94x** |
| 70% | 17.91 | 100.11 | **5.59x** |

### 4. Claim 1 headline 影响评估

**Claim 1 完全成立，且比预想更强。**

Reviewer 的疑虑基于混淆了两种不同方法：
- **50% TEAL=23.31** 是 vanilla TEAL（training-free），normalization fix 前后数字一致，不是 inflated
- **70% TEAL=17.91** 是 predictor-based TEAL（训练后的 KL predictor），不是 vanilla TEAL

Vanilla TEAL PPL 随 sparsity 单调递增（10.97 → 23.31 → 100.11），物理上完全合理。KL predictor 的优势随 sparsity 增加而急剧增大（1.22x → 1.94x → 5.59x），这说明训练的 predictor 在高稀疏度下价值更大。

**论文表格需要明确区分 "Vanilla TEAL (training-free)" 和 "Predictor TEAL (trained)" 两列，避免 Reviewer 再次混淆。**

---

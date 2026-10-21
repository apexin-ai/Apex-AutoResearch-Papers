# analysis exp019 bootstrap ci

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp019_bootstrap_ci_20260516T112009_result.json`
- **Structured JSON:** [`e9714e0f88cf9a68da7e.json`](../../sessions/e9/e9714e0f88cf9a68da7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-019 Mistral-7B Bootstrap CI 结果

| Pair | AUC | 95% CI | CI lower > θ=0.60? | p_perm | p(AUC≤0.60) |
|------|-----|--------|---------------------|--------|-------------|
| **0v1** | 0.9842 | [0.9824, 0.9860] | PASS | 0.0001 | 0.0000 |
| **1v2** | 0.5934 | **[0.5835, 0.6032]** | **FAIL** | 0.0001 | **0.9017** |
| 2v3 | 0.5402 | [0.5301, 0.5510] | FAIL | 0.0001 | 1.0000 |
| 3v4 | 0.5233 | [0.5128, 0.5338] | FAIL | 0.0003 | 1.0000 |
| 4v5 | 0.5180 | [0.5070, 0.5287] | FAIL | 0.0014 | 1.0000 |

**K\* (CI-based) = 1**，与 point estimate 一致。

### 关键发现

1. **1v2 CI [0.5835, 0.6032] 跨越 θ=0.60**。CI lower = 0.5835 < 0.60，无法拒绝 "AUC ≤ 0.60" 的零假设。p(AUC≤0.60) = 0.9017，即 90.17% 的 bootstrap 样本 AUC ≤ 0.60。

2. 虽然 4/5 folds > 0.585（接近 0.60），但 OOF point AUC = 0.5934，bootstrap CI 明确显示这不能可靠地超过 0.60。

3. 所有 pair 的 permutation p-value 极小（≤0.0014），说明分类器确实学到了信号（AUC 显著 > 0.50），只是 1v2 的信号不够强到超过 θ。

### 与 exp-016 Qwen-base 对比

| | exp-016 Qwen-base 1v2 | exp-019 Mistral-7B 1v2 |
|---|---|---|
| AUC | **0.6260** | 0.5934 |
| 95% CI | **[0.6168, 0.6353]** | [0.5835, 0.6032] |
| CI lower > 0.60 | **Yes** | No |
| K\* | **2** | 1 |

exp-016 Qwen-base 的 1v2 CI lower = 0.6168，远在 0.60 之上，K\*=2 稳固。exp-019 Mistral-7B 差距 ~0.033 AUC，CI 完全不重叠，K\*=1 确认。

---

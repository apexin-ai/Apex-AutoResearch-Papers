# ssh verify fisher pvalue

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-fisher-pvalue_20260516T155955_result.json`
- **Structured JSON:** [`284c5d577d8750ba075c.json`](../../sessions/28/284c5d577d8750ba075c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**`pooled_fisher_test.py` 的 p=0.035 是错误的。** 正确值是 **p=0.110 (one-sided)**。

### 根因

`KNOWN_DATA` 把每个 seed 的 trial count 从 100 硬编码成了 200（所有 successes 和 totals 都精确翻倍）。实际每 seed 是 10 tasks × 10 rollouts = **100 trials**，不是 200。sample size 翻倍人为缩小了 p-value。

### 各 seed 真实数据（已从 registry 交叉验证）

| Seed | obs_only (ε=0.2) | argmin (K=10) | Δ |
|------|-------------------|---------------|-----|
| 42 | 22/100 (22%) | 12/100 (12%) | +10pp |
| 43 | 16/100 (16%) | 17/100 (17%) | -1pp |
| 44 | 16/100 (16%) | 13/100 (13%) | +3pp |
| **Pooled** | **54/300 (18.0%)** | **42/300 (14.0%)** | **+4.0pp** |

### Fisher exact test

- **正确**: OR=1.35, p_one=**0.1102**, p_two=0.2205 → **不显著** (Narrative B)
- 错误 (脚本): OR=1.35, p_one=0.0350, p_two=0.0699 → 伪显著

**是 Narrative B：obs_only 有 +4pp 趋势但统计上不显著（p=0.11 > 0.05）。** seed43 甚至出现 argmin 反超 (-1pp)，削弱了 dual claim。

---

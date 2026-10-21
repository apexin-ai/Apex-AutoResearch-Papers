# train detector check and fix

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_detector-check-and-fix_20260513T223828_result.json`
- **Structured JSON:** [`143d877cd9998d9f2305.json`](../../sessions/14/143d877cd9998d9f2305.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. 训练状态：已完成
训练于 2026-05-14 06:20 完成，3 epoch / 10194 steps，耗时 ~22 分钟。

### 2. Gate Check：**PASSED**

| 指标 | 值 | 门槛 | 状态 |
|------|-----|------|------|
| Temperature | 1.5 | - | - |
| AUC | 1.0000 | >= 0.95 | PASS |
| ECE | 0.0001 | <= 0.05 | PASS |
| F1 (human) | 0.9999 | - | - |
| F1 (synthetic) | 0.9999 | - | - |

### 3. Q-score 分布：**几乎完全二值化**

13592 条 test 预测：
- q < 0.1: 6811 (50.1%)
- q > 0.9: 6777 (49.9%)
- 0.1 ≤ q ≤ 0.9: **仅 4 条** (0.03%)

**WARNING**: q-score 几乎完全二值化（非 0 即 1），不同 b 值可能不会产生实质差异。检测器区分能力极强，导致校准后的概率集中在两极——这意味着 provenance weight 公式中 b 参数的调节空间非常有限。

---

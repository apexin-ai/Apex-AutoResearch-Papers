# check reward signed error r1w4

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_reward-signed-error-r1w4_20260522T053944_result.json`
- **Structured JSON:** [`6121f1bf442cefa6e783.json`](../../sessions/61/6121f1bf442cefa6e783.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## R1-W4 任务状态报告

**状态：已完成（分析报告已存在），但 review_issues.yaml 未更新为 done。**

### 结果摘要

分析于 2026-05-15 完成，报告存于 `artifacts/signed_reward_error.md`。核心发现：

**dt=2 不是系统性正向偏差，而是严重的负向偏差（underprediction）：**

| 实验 | dt | Mean Signed Error | 实际奖励 | 预测奖励 |
|---|---|---|---|---|
| baseline_s1 | 1 | **+0.001** (校准良好) | 1.893 | 1.894 |
| exp_008d | 1 | +0.018 (轻微过预测) | 0.361 | 0.379 |
| exp_008d | 2 | **−0.599** (严重欠预测) | 0.721 | 0.121 |
| exp_008f | 1 | −0.710 | 0.921 | 0.211 |
| exp_008f | 2 | −1.645 | 1.840 | 0.195 |

**关键结论：**
- 008d 在 dt=2 上 underpredicts ~83%（仅 8% 样本过预测），**否定了**"dt=2 系统性正向偏差导致 CIVO"的假设
- 008f 在两个 dt 值上都严重欠校准，世界模型基本无法区分 dt=1/dt=2
- Baseline 几乎完美校准（SE ≈ 0），验证了方法论正确性
- CIVO 机制可能不在 observation-level reward overprediction，而在 **imagination-level**（prior drift / critic accumulated returns）

**建议操作：** 将 review_issues.yaml 中 R1-W4 的 action_items status 从 `in_progress` 改为 `done`，并填写 resolution 总结。需要我更新吗？

---

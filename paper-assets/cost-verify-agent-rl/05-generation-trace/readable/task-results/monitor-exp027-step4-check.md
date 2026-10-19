# monitor exp027 step4 check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp027_step4_check_20260515T202004_result.json`
- **Structured JSON:** [`697f5257c5520fd791c7.json`](../../sessions/69/697f5257c5520fd791c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp027 训练进度报告

**状态：Step 4 仍在进行中，无新 step 完成。**

- PID 789790 运行中，已运行 5h47m
- 最后一条 stdout log 时间：03:31（step 3 完成时写入）
- 最后一条 stderr 时间：03:08（step 3 rollout 阶段的 env 警告）
- Step 4 已运行约 ~50min（step 3 耗时 78min，预计还需 ~30min）

### 已完成步骤总览

| 指标 | Step 1 | Step 2* | Step 3 (已知) |
|------|--------|---------|---------------|
| success | **35.94%** | — | 10.16% |
| KL | 0.058 | — | 0.248 |
| entropy | 0.275 | — | 0.385 |
| pass@16 | **100%** | — | 50% |
| grad_norm | 19.44 | — | 21.31 |
| reward_mean | **1.997** | — | 0.483 |
| batch_size | 5152 | — | 6048 |
| step耗时 | 4343s (72m) | 5886s (98m) | 4689s (78m) |

*Step 2 的主要指标在日志截断区域中，仅获取到耗时数据。

### 趋势警告

Step 1 → Step 3 出现明显退化：
- success rate 从 35.9% 跌至 10.2%
- reward_mean 从 2.0 降到 0.48
- KL 从 0.058 涨到 0.248（4.3倍）
- pass@16 从 100% 降到 50%

Step 0 val baseline: success 6.25%, pass@1 6.25%。Step 3 的 train success 已接近 baseline 水平。

---

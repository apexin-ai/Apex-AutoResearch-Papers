# monitor gae step10 check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_gae-step10-check_20260517T184136_result.json`
- **Structured JSON:** [`0d2788450d5e44fcfd0c.json`](../../sessions/0d/0d2788450d5e44fcfd0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## gae_baseline_seed1 状态

**进程**: PID 40267 存活，正常运行中

**当前进度**: **9/15** (60%)，正在执行 step 10
- 最新 tqdm: `9/15 [4:04:24<2:56:26, 1764.44s/it]`
- 每步约 29-31 分钟，预计 step 10 约 30 分钟后完成

**Step 10 val 数据**: 尚未产出。`"10/15"` 还未出现在日志中。

**已有 train 指标趋势**:

| Step | success | action_is_valid | pass@8 | response_length |
|------|---------|-----------------|--------|-----------------|
| 1 | 0.031 | 0.726 | 0.188 | 2,483 |
| 7 | 0.078 | 0.602 | 0.375 | 8,080 |

**注意**: 日志中所有 step 的 `timing_s/eval_step:0.0`，说明中间步没有触发 eval。`eval_total:193s` 来自初始 eval（step 0）。val 指标可能仅在特定 step（如 5, 10, 15）或训练结束时触发。step 10 完成后需再次检查是否有 val 输出。

---

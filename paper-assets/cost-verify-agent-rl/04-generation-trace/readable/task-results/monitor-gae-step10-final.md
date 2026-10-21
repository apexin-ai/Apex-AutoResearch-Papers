# monitor gae step10 final

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_gae-step10-final_20260517T191214_result.json`
- **Structured JSON:** [`c946c1fa3e18e87037c2.json`](../../sessions/c9/c946c1fa3e18e87037c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**当前状态**: Step 10 正在 actor update 阶段（最后阶段），尚未完成。

已有 val eval 数据（每次 32 episodes）:

| Step | val/success | val/action_is_valid | val/pass@1 |
|------|------------|-------------------|-----------|
| 0 | 6.25% | 77.96% | 6.25% |
| 5 | 12.50% | 69.26% | 12.50% |
| 10 | *pending* | *pending* | *pending* |

Train 指标趋势（供参考）:

| Step | train/success | train/action_is_valid | train/pass@8 |
|------|--------------|---------------------|-------------|
| 5 | 6.25% | 60.74% | 43.75% |
| 9 | 3.13% | 60.33% | 25.00% |

Step 9 checkpoint 保存于 02:51 UTC，step 10 rollout 日志到 03:07 UTC 后进入 actor update。按 ~29 min/step 估算，step 10 约在 **03:20 UTC** 完成，届时会触发 val eval（每 5 步一次）。

注意：train success 从 step 5 的 6.25% 降到 step 9 的 3.13%，pass@8 从 43.75% 降到 25%，训练有退化迹象。

---

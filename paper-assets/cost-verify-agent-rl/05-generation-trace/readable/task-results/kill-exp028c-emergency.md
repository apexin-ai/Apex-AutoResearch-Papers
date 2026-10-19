# kill exp028c emergency

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_kill_exp028c_emergency_20260516T080953_result.json`
- **Structured JSON:** [`280dde5c3b63e103b46b.json`](../../sessions/28/280dde5c3b63e103b46b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

- **进程终止**: 3 个 PID 全部 killed 确认
- **GPU 释放**: 两卡均 0 MiB / 0% 利用率
- **Checkpoints**: global_step_5 (21GB) 和 global_step_10 (21GB) 均完整
- **Val 崩溃确认**: step 0 → 6.25%, step 5 → 6.25%, **step 10 → 0%**（所有 best@N 全 0）
- **Train 崩溃趋势**: step 7 success=21.9% → step 11-12 降至 6-7%, pass@8 从 56% 降到 19-25%
- **关键异常信号**: step 5 kl_loss spike (0.824), step 11 ppo_kl 异常低 (0.002), entropy 持续萎缩

报告已写入 `artifacts/exp028c_selfguide_recipe/intermediate/kill_and_metrics.md`。

---

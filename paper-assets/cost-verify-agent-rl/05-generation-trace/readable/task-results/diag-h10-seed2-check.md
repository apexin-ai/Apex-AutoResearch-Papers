# diag h10 seed2 check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_h10_seed2_check_20260523T200121_result.json`
- **Structured JSON:** [`a93b00d412cc3747d8aa.json`](../../sessions/a9/a93b00d412cc3747d8aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**训练状态：被 kill（SIGTERM），未完成**

- PID 42499 已不存在
- 日志 `/root/autodl-tmp/hsweep_h10_seed2.log` 中明确记录：
  - `*** SIGTERM received at time=1779561387 on cpu 20 ***`（2026-05-24 02:36:27）
- 仅完成了 **step 0 初始验证**（`step:0`），5 步训练一步都没跑完就被 kill 了
  - step 0 initial val success rate: **12.5%**（32 episodes）
- 日志时间线：02:16:51 创建 → 02:36:27 被 kill，运行约 20 分钟
- **无 checkpoint** 保存（`/root/autodl-tmp/checkpoints/` 下无 h10-seed2 相关文件）
- **wandb run ID: `mcjumgd2`**，run name: `hsweep-h10-seed2-1gpu`
  - 路径：`/root/cost-verify-agent-rl/RAGEN/wandb/run-20260524_021807-mcjumgd2`

结论：训练在完成初始验证后、进入 step 1 训练前被 SIGTERM 终止。需要重新启动。

---

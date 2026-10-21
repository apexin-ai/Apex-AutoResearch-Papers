# deploy exp 038 redeploy

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp_038_redeploy_20260521T122034_result.json`
- **Structured JSON:** [`812f0e57f827284f4e26.json`](../../sessions/81/812f0e57f827284f4e26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验正在运行，无需重新部署。**

诊断结果：

| 项目 | 状态 |
|------|------|
| PID 175633 | **存活**，已运行 2分18秒 |
| cuda:0 | 12% 利用率，3305 MiB / 24564 MiB 已占用 |
| 日志 | 已到 step 5000，eval_return=35.2，正在训练中 |
| dual_critic | 已启用（value_opt + value2_opt 均已初始化） |

日志最新指标（step 5000）：
- `eval_return`: 35.2
- `model_loss`: 20.7
- `gate_dt_mean`: 2.0（固定 dt=2，符合预期）
- `value1_mean` / `value2_mean`: 均为 0.0（刚开始训练，正常）
- `fps`: 0.0（首次记录，尚未计算）

实验刚启动约 2 分钟，运行正常。无需干预。

---

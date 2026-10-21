# monitor exp012b step6

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp012b-step6_20260514T065638_result.json`
- **Structured JSON:** [`cbb697deb363bfa97e90.json`](../../sessions/cb/cbb697deb363bfa97e90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态：
- **进程活跃**：PID 233689 运行 16 分钟，Ray TaskRunner (90% CPU) 和 WorkerDict (28% CPU) 均正常
- **日志缓冲**：exp012b.log 自 14:48:36 后未刷新（Python stdout 缓冲），1489 行均为 config dump 和 checkpoint loading
- **Step 6 rollout 进行中**：group_size=16 使 rollout 时间约为 exp010（group_size=8）的 2 倍，预计再需 2-4 分钟

已提取 exp010 对比基准：

| 指标 | exp010 step 1 | exp010 step 6 | exp010 step 10 (末) |
|------|-------------|-------------|--------------|
| success | 4.69% | 3.13% | 0% |
| action_is_valid | 58.8% | 66.9% | 68.3% |
| pass@8 | 37.5% | 12.5% | 0% |
| entropy | 0.0919 | 0.0867 | 0.0889 |
| ppo_kl | 0.00050 | 0.00181 | 0.00081 |
| score/mean | 0.022 | 0.030 | -0.287 |

4 分钟后自动回来查 step 6 指标。

---

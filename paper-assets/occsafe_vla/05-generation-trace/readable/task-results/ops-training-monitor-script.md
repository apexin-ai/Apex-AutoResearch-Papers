# ops training monitor script

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training_monitor_script_20260523T154103_result.json`
- **Structured JSON:** [`9fbfd340a57342fced9b.json`](../../sessions/9f/9fbfd340a57342fced9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器均部署成功。

### 汇报

| 服务器 | 部署状态 | Monitor PID | 首条日志 |
|--------|---------|-------------|----------|
| **westd-10894** | 成功 | 451476 | `TRAINING_ACTIVE — 4 GPU processes`，4 卡各占 ~62GB/98GB，GPU 利用率 0%（采样瞬间空闲） |
| **westd-34685** | 成功 | 435259 | `TRAINING_ACTIVE — 4 GPU processes`，4 卡各占 ~62GB/98GB，GPU 利用率 87-99% |

两台服务器当前都有训练在跑（4 个 GPU 进程，显存占用 ~62GB）。westd-34685 的 GPU 利用率很高（87-99%），westd-10894 采样到的瞬间为 0% 但进程仍在。监控脚本每 10 分钟写一条日志到 `/tmp/training_monitor.log`，后续可通过 `tail -5 /tmp/training_monitor.log` 快速查状态。

---

# ops westb v8 launch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb-v8-launch_20260515T143227_result.json`
- **Structured JSON:** [`e137745efeda90cdf410.json`](../../sessions/e1/e137745efeda90cdf410.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双卡均已稳定运行。

---

## 最终报告

| 项目 | 状态 |
|------|------|
| **磁盘清理** | 根分区 22G 可用 (29%)，数据盘 29G 可用 |
| **RASP v8 (cuda:0)** | PID 532861，稳定运行，1/100 steps，wandb: `0wz7xpd5`，GPU 0 占用 71674 MiB / 97887 MiB，100% util |
| **Standard v8 (cuda:1)** | PID 534667，稳定运行，0/100 steps（进度条已出现），wandb: `q34vz8j2`，GPU 1 占用 44344 MiB / 97887 MiB，99% util |

**异常处理记录**：
- Standard v7 残留进程 (PID 532557) 占据 GPU 1 共 62.5 GB，导致 Standard v8 首次启动 OOM。该进程在 kill 前自行退出，清理后重新启动 Standard v8 成功。
- 初始 `pkill -f train_grpo` 因 SSH exit code -1 未成功执行，v7 残留未被清除。

---

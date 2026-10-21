# ops kill leaked process

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-leaked-process_20260514T035918_result.json`
- **Structured JSON:** [`954cdee3a3519e4af2c0.json`](../../sessions/95/954cdee3a3519e4af2c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- **PID 209114 已 kill**，cuda:1 泄漏进程已清除
- **cuda:1** 现在只有 PID 207121（plan017 训练进程），显存 79604MiB/97887MiB，GPU 利用率 90%，运行正常
- **cuda:0** 有 PID 208833，显存 16452MiB，正常运行

plan017 无 OOM 风险，状态健康。

---

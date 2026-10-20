# ops kill zombie gpu0

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-zombie-gpu0_20260515T145951_result.json`
- **Structured JSON:** [`7f86e2247e1f10adb025.json`](../../sessions/7f/7f86e2247e1f10adb025.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

489184 已不存在，487831 已 kill。但 GPU0 仍被 PID 490265 占用（19574MiB），GPU0 未释放。

当前状态：
- **GPU0**: PID 490265 (`/root/miniconda3/bin/python`) 占用 19574MiB，利用率 60%
- **GPU1**: PID 486404 (`VLLM::EngineCore`) 占用 28004MiB，利用率 100%

GPU0 上有新进程 490265 在跑。需要也 kill 掉这个吗？

---

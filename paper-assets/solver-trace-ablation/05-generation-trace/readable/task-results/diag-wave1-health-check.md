# diag wave1 health check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_wave1-health-check_20260517T054338_result.json`
- **Structured JSON:** [`03c179e68a075f7ddde7.json`](../../sessions/03/03c179e68a075f7ddde7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常运行：

| 实验 | GPU | PID | 状态 | GPU 占用 | GPU Util |
|------|-----|-----|------|----------|----------|
| **plan018-additive-random-b01-s45** | cuda:0 | 147962 | Running | 84560 MiB | 88% |
| **sweep-random-b005-s42** | cuda:1 | 148042 | Running | 84314 MiB | 93% |

两个进程均运行约 20 分钟（启动于 13:23/13:24），CPU 利用率 99.7%，GPU 利用率 88-93%，状态正常。之前看到的 GPU 空闲可能是短暂的数据加载间隙。

---

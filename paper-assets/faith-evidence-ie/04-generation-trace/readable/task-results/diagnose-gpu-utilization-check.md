# diagnose gpu utilization check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu-utilization-check_20260522T201507_result.json`
- **Structured JSON:** [`4e10be8b2b1d7064c1c0.json`](../../sessions/4e/4e10be8b2b1d7064c1c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 利用率 | 显存占用 | PID | 状态 |
|-----|--------|----------|-----|------|
| 0 | 56% | 9.6 / 98 GB | 194600 | 活跃 |
| 1 | 90% | 32.5 / 98 GB | 194682 | 高负载 |
| 2 | 47% | 6.1 / 98 GB | 189485 | 活跃 |
| 3 | 68% | 18.9 / 98 GB | 196512 | 活跃 |

4 张卡全部被 python 进程占用，无空闲卡。GPU 1 负载最重（90% 利用率，32.5GB 显存）。如需提交 eval 任务（C001），当前没有满足 <2GB 显存的卡。

---

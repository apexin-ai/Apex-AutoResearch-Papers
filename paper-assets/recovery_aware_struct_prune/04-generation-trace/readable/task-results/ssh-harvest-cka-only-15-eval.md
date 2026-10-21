# ssh harvest cka only 15 eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest_cka_only_15_eval_20260520T221857_result.json`
- **Structured JSON:** [`fcfe6c5ee3fc1b090413.json`](../../sessions/fc/fcfe6c5ee3fc1b090413.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均在运行中：

| Job | 进度 | 当前 Accuracy | EOS Rate | Avg Len | 预计剩余 |
|-----|------|---------------|----------|---------|----------|
| **seed123** (GPU 0) | 507/1319 (38%) | 73.8% (@500) | 99.40% | 179 | ~35-40 min |
| **seed456** (GPU 1) | 386/1319 (29%) | 76.29% (@350) | 98.86% | 202 | ~50-55 min |

seed456 进度落后（中间有几次长暂停，可能是 GPU 争抢导致的 ETA 飙升后恢复）。两个都还需要较长时间才能完成。

---

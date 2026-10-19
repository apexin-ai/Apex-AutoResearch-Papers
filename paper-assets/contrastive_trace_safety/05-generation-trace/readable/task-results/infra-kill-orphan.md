# infra kill orphan

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill_orphan_20260516T192202_result.json`
- **Structured JSON:** [`0cd1f6357bd48e4a0eda.json`](../../sessions/0c/0cd1f6357bd48e4a0eda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 structfuse 孤儿进程已全部 kill，显存完全释放：

| GPU | 释放前 | 释放后 |
|-----|--------|--------|
| GPU 0 | 50,801 MiB | 3 MiB |
| GPU 1 | 69,856 MiB | 3 MiB |

两张 RTX PRO 6000（各 ~96GB）现在完全空闲可用。

---

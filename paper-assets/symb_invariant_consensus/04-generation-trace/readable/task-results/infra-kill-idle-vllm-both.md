# infra kill idle vllm both

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill-idle-vllm-both_20260519T111412_result.json`
- **Structured JSON:** [`1e5c01c26392af805fc4.json`](../../sessions/1e/1e5c01c26392af805fc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已释放完毕：

| 服务器 | GPU | 释放前 | 释放后 |
|---|---|---|---|
| westd-25068 | cuda:2 | 88092 MiB (0% util) | **0 MiB** |
| westd-16639 | cuda:0 | 88286 MiB (0% util) | **0 MiB** |

其余 GPU 均未受影响，正常运行中。tmux sessions (exp063_vllm, exp063_run) 也已清理。

---

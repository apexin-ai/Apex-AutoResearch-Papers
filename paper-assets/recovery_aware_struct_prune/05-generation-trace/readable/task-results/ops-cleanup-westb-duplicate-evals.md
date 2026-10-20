# ops cleanup westb duplicate evals

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_westb_duplicate_evals_20260517T124236_result.json`
- **Structured JSON:** [`85194c3992f8ce3f8b34.json`](../../sessions/85/85194c3992f8ce3f8b34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

重复 eval 进程 (712124, 712819) 已不存在，无需手动 kill。

当前 GPU 状态：
- **cuda:0**: PID 710618, 12994MiB / 97887MiB, 73% util
- **cuda:1**: PID 715803, 12994MiB / 97887MiB, 80% util

两张卡各只有一个进程，显存占用正常（~13GB）。之前占 ~46GB 的重复 eval 进程已自行退出。

---

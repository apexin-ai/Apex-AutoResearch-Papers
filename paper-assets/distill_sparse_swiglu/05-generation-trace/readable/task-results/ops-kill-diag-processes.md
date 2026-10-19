# ops kill diag processes

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_diag_processes_20260516T003010_result.json`
- **Structured JSON:** [`68c9dcadf39140634f02.json`](../../sessions/68/68c9dcadf39140634f02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 `diag_hflm.py` 进程已 kill。

| GPU | 显存 (kill 前) | 显存 (kill 后) | 变化 |
|-----|---------------|---------------|------|
| cuda:0 | 39594 MiB / 97887 MiB | 39594 MiB / 97887 MiB | 无变化 |
| cuda:1 | 74175 MiB / 97887 MiB | 37660 MiB / 97887 MiB | **-36515 MiB** |

cuda:1 释放了约 35.7 GB 显存，两个 debug 进程占用的显存已全部回收。当前两块 GPU 各约 40% 占用。

---

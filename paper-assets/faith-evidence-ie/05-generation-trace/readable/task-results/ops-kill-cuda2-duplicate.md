# ops kill cuda2 duplicate

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-cuda2-duplicate_20260514T212936_result.json`
- **Structured JSON:** [`d046432bfd2653d0d098.json`](../../sessions/d0/d046432bfd2653d0d098.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果**:

| 项目 | 状态 |
|------|------|
| PID 100555 | **KILLED** ✓ (重复 ckpt-40 eval，已运行 17:55) |
| PID 101842 | **ALIVE** ✓ (正常 ckpt-40 eval，运行 5:19，状态 Rl) |
| cuda:2 显存 | **9069 MiB** (从之前两个进程共占降到单进程，符合预期) |

全部 GPU 显存：GPU0 13645M, GPU1 10653M, GPU2 9069M, GPU3 13645M。cuda:2 已恢复正常。

---

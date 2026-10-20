# ops kill duplicate semantic only

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_duplicate_semantic_only_20260514T005851_result.json`
- **Structured JSON:** [`eea7932436d5bb8785cf.json`](../../sessions/ee/eea7932436d5bb8785cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **PID 140568**: 已不存在，无需 kill
- **PID 140804** (semantic_only_v2): 正常运行中

**当前 GPU 进程列表：**

| GPU | PID | 显存占用 | 备注 |
|-----|--------|---------|------|
| GPU 0 | 137719 | 22656 MiB | docred_schema |
| GPU 0 | 140804 | 16502 MiB | semantic_only_v2 |
| GPU 1 | 142639 | 16502 MiB | — |

注意：GPU 1 上只看到 1 个进程 (PID 142639)，不是预期的 138136 和 140885。138136 和 140885 可能已结束，142639 可能是后续启动的新进程。

---

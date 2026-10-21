# fix kill duplicate westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill_duplicate_westd41074_20260527T100300_result.json`
- **Structured JSON:** [`46530d85572c355c90ed.json`](../../sessions/46/46530d85572c355c90ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

重复进程 371486/371488 已不存在，无需手动 kill。当前状态正常：

- **GPU 0**: PID 356361 (random k=0.9) — 运行中
- **GPU 1**: PID 356612 (random k=0.5) — 运行中
- **GPU 2**: PID 262137 — 运行中
- **GPU 3**: 空闲

每个 GPU 只有一个进程，没有重复。

---

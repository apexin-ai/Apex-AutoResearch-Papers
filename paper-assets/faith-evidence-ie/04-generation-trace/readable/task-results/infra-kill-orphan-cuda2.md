# infra kill orphan cuda2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill_orphan_cuda2_20260516T002820_result.json`
- **Structured JSON:** [`7c3353910990f4964f7f.json`](../../sessions/7c/7c3353910990f4964f7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**孤儿进程 PID 276148 已自行消亡**（可能 OOM 后被内核杀掉了）。

**当前 GPU 状态：**

| GPU | 显存已用 | 显存总量 | 状态 |
|-----|---------|---------|------|
| 0 | 10,855 MiB | 32,607 MiB | 占用（PID 270467） |
| 1 | 28,341 MiB | 32,607 MiB | 占用（PID 277315） |
| **2** | **0 MiB** | **32,607 MiB** | **空闲 ✓** |
| 3 | 10,859 MiB | 32,607 MiB | 占用（PID 272169） |

**cuda:2 已完全释放（0 MiB 占用），可立即用于新任务。** 无需执行 kill 操作。

---

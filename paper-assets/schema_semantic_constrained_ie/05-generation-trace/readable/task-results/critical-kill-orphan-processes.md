# critical kill orphan processes

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical_kill_orphan_processes_20260513T235550_result.json`
- **Structured JSON:** [`054b15d192378b849682.json`](../../sessions/05/054b15d192378b849682.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

### 1. Kill 结果

| PID | 身份 | 操作 |
|-----|------|------|
| **116365** | 孤儿 — `run_extraction_docred.py`（占 GPU-0 25GB） | **已 kill** |
| 134450, 134886 | Director 提到的可疑 PID | 进程已不存在，无需处理 |

### 2. nvidia-smi 前后对比

**Kill 前（3 个进程）：**
| PID | GPU | 显存 |
|-----|-----|------|
| 116365 | GPU-0 | 25294 MiB |
| 134207 | GPU-0 | 16480 MiB |
| 134598 | GPU-1 | 16482 MiB |

**Kill 后（2 个进程）：**
| PID | GPU | 显存 |
|-----|-----|------|
| 134207 | GPU-0 | 16482 MiB |
| 134598 | GPU-1 | 16482 MiB |

GPU-0 释放了 25GB 显存。

### 3. 数据污染 + 修复

两个文件均有 **1 行 null bytes（\x00）污染**，系并发写入所致。无重复 doc_id。

| 文件 | 修复前 | 修复后 | 删除 |
|------|--------|--------|------|
| `phase2_scierc_semantic_only.jsonl` | 55 行 | **54 行** | 1 行 null bytes |
| `phase2_scierc_full_s1.jsonl` | 63 行 | **62 行** | 1 行 null bytes |

### 4. 合法进程状态

- **PID 134202**（semantic_only wrapper）→ **134207**（python）：✅ 运行中
- **PID 134593**（full_s1 wrapper）→ **134598**（python）：✅ 运行中

### 5. 无需重跑

数据已成功去污，两个合法推理进程正常运行中。

---

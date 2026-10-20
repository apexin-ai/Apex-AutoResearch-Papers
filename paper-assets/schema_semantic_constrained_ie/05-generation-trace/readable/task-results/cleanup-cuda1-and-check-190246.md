# cleanup cuda1 and check 190246

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_cuda1_and_check_190246_20260514T141603_result.json`
- **Structured JSON:** [`8b5fe8b6908cf345fb98.json`](../../sessions/8b/8b5fe8b6908cf345fb98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

| 项目 | 状态 |
|------|------|
| **PID 190246** | 存活，运行 28 分钟，状态 `Rl`（运行中） |
| **JSONL 行数** | **355/551**（进度 ~64%） |
| **cuda:1** | 已完全释放，无 python 进程占用 |
| **tmux** | 无残留 session（`phase2_docred_semantic_only` 已清理） |
| **其他残留进程** | 无。仅 PID 190246 及其父进程（190241 wrapper、190245 timeout），全属于 `llama_scierc_full_s1` 任务 |

cuda:1 已干净可用，cuda:0 上的 `llama_scierc_full_s1` 正常推进中。

---

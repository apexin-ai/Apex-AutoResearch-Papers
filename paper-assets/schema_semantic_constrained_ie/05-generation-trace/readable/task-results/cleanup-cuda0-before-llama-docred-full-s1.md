# cleanup cuda0 before llama docred full s1

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_cuda0_before_llama_docred_full_s1_20260514T143958_result.json`
- **Structured JSON:** [`2d967f4a12269cb5e512.json`](../../sessions/2d/2d967f4a12269cb5e512.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

| 检查项 | 结果 |
|--------|------|
| cuda:0 残留进程 | **干净** — 0MiB 显存，0% 利用率 |
| cuda:1 状态 | 正在运行 `llama_docred_unconstrained`（PID 193610，16693MiB，89% util） |
| tmux `llama_scierc_full_s1` | 已清理 |
| tmux `llama_docred_full_s1` | 已清理 |
| 残留 tmux | `llama_docred_unconstrained` 保留（GPU 1 上的正在运行实验） |
| `outputs/llama_docred_full_s1.jsonl` | 不存在，无冲突 |

cuda:0 可用，无阻塞。

---

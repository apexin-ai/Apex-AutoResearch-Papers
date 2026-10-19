# ssh rename execute

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rename_execute_20260513T210559_result.json`
- **Structured JSON:** [`1e08e5fe3621e27979f4.json`](../../sessions/1e/1e08e5fe3621e27979f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，汇总结果：

| 检查项 | 状态 |
|--------|------|
| 重命名 `/root/structfuse` → `/root/structfuse-context` | 成功 |
| 符号链接 `/root/structfuse` → `/root/structfuse-context` | 正常 |
| 符号链接路径解析 (`/root/structfuse/training/train.py`) | 正常 |
| PID 73544 (m2_full_qwen, cuda:0) | 存活，运行 3h26m |
| PID 74122 (m2_full_starcoder, cuda:1) | 存活，运行 3h26m |
| PID 209827 (m1_reextract_v2, CPU) | 存活，运行 1h07m，4 worker 子进程均在 |
| GPU 0 利用率 | 99%，51.6/97.9 GB |
| GPU 1 利用率 | 100%，55.2/97.9 GB |

所有进程未受影响，GPU 满载运行，符号链接透明工作。

---

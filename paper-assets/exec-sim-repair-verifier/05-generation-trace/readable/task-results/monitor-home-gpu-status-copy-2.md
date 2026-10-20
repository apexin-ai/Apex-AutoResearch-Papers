# monitor home gpu status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_home-gpu-status_20260517T181831_result.json`
- **Structured JSON:** [`af064a16911e21e5a26f.json`](../../sessions/af/af064a16911e21e5a26f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| 项目 | 状态 |
|------|------|
| **GPU** | 空闲 — RTX 5090, 0MiB/32607MiB, 0% 利用率, 35°C, 无进程 |
| **磁盘** | 318G 可用 / 1.1T 总量 (69% 已用) |
| **TRAJ 8B checkpoints** | 两个 seed 均完好 — seed42 (07:10) 和 seed123 (08:09)，各含 adapter (~58MB) + tokenizer |
| **Few-shot baseline** | 已完成，结果如下 |

**Few-shot baseline 结果 (3-shot):**

| 模型 | Accuracy | Pass F1 | Fail F1 |
|------|----------|---------|---------|
| DeepSeek-Coder-6.7B | 59.95 | 44.13 | 68.78 |
| Qwen3-8B | 68.78 | 64.46 | 72.17 |

GPU 完全空闲，可以立即启动新任务。

---

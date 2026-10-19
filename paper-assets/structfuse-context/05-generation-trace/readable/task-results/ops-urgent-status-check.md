# ops urgent status check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-status-check_20260515T230012_result.json`
- **Structured JSON:** [`d8c3d51fcb1bf4246714.json`](../../sessions/d8/d8c3d51fcb1bf4246714.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已采集。

---

### 1. Qwen dataflow_s43 eval@1000 结果

| step | val_loss | R@1 | R@5 | R@10 |
|------|----------|-----|-----|------|
| 500 | 0.4617 | 0.5495 | 0.9728 | 1.0 |
| **1000** | **0.4984** | **0.5174** | **0.9581** | **1.0** |

eval@1000 val_loss 上升、R@1 下降（early stopping 计数 1/2）。训练仍在继续，当前到 step 1100+。best checkpoint 仍是 step 500 的。

### 2. SWE-bench retrieval eval

**54 / 100** 实例完成（`random_s42_100/per_instance_results.jsonl`，共 54 行）。PID 61328 已运行 4h15m，仍在跑。

### 3. GPU 进程总览

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| GPU 0 | 100% | 62.6G / 97.9G |
| GPU 1 | 100% | 54.8G / 97.9G |

| PID | 显存 | 运行时间 | 任务 |
|-----|------|----------|------|
| 18427 | 51.0G | 7h07m | Qwen dataflow_aware_s43 训练 |
| 38016 | 54.8G | 5h45m | StarCoder embedding_distance_s42 训练 |
| 61328 | 11.6G | 4h15m | SWE-bench retrieval eval (random_s42) |

---

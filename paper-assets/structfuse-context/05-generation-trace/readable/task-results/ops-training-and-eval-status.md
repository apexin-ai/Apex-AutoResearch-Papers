# ops training and eval status

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-and-eval-status_20260516T022911_result.json`
- **Structured JSON:** [`e32dde0a7500b5357b38.json`](../../sessions/e3/e32dde0a7500b5357b38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

---

### 1. SWE-bench random_s42 eval — **进行中，99/100**
- PID 61328 存活，已运行 7h44m
- 批量脚本 PID 61320 也在跑
- `per_instance_results.jsonl` 已有 99 行，还差 1 个 instance
- `summary.json` 尚未生成（最后一个 instance 跑完才会写）

### 2. Qwen dataflow_s43 — **eval@1500 尚未触发，当前刚进 epoch 2**

| step | val_loss | R@1 | R@5 | R@10 |
|------|----------|-----|-----|------|
| 500 | 0.4617 | 0.5495 | 0.9728 | 1.0 |
| 1000 | 0.4984 | 0.5174 | 0.9581 | 1.0 |

- step 1000 时 val_loss 未改善 (patience 1/2)
- 当前已到 step 1500，刚进入 epoch 2，eval@1500 即将触发
- **未 early stop**

### 3. 训练进度

**Qwen (GPU 0)** — PID 18427, 运行 10h36m
- 当前 subrun: `dataflow_aware_s43`, step 1500, epoch 2
- 已完成: random_s42, random_s43, random_s44, embedding_distance_s43, embedding_distance_s44 (5/9)
- 剩余: dataflow_aware_s44, bm25_s42 等

**StarCoder (GPU 1)** — PID 129747
- 刚完成 `embedding_distance_s42`（10:06 结束）
- 当前 subrun: `embedding_distance_s43`, step 50/1405, epoch 1 刚开始
- 已完成: random_s42~s44, embedding_distance_s42

**GPU 状态**

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 100% | 62620/97887 MiB (Qwen训练 + SWE-bench eval) |
| 1 | 100% | 53467/97887 MiB (StarCoder训练) |

---

# experiment p2b eval 9runs pool26

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_p2b_eval_9runs_pool26_20260512T192122_result.json`
- **Structured JSON:** [`209ca71d441c0149b95d.json`](../../sessions/20/209ca71d441c0149b95d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果已收集。random_s42 的 JSON 文件在之前清理中丢失了，但我在本 session 最开始从 eval log 中读到了其结果。现在汇总所有 9 个 runs 的结果。

## Phase 2b 全部 9 个 Checkpoints 评估结果 (pool_size=26)

### 各 Run 明细

| 策略 | Seed | recall@1 | recall@5 | recall@10 | pool_size | total |
|------|------|----------|----------|-----------|-----------|-------|
| random | 42 | **0.9449** | **0.9843** | 0.9843 | 26 | 127 |
| random | 123 | **0.9449** | **0.9921** | 0.9921 | 26 | 127 |
| random | 456 | **0.9291** | **0.9921** | 0.9921 | 26 | 127 |
| embedding_distance | 42 | 0.6693 | 0.8898 | 0.9291 | 26 | 127 |
| embedding_distance | 123 | 0.6772 | 0.9055 | 0.9528 | 26 | 127 |
| embedding_distance | 456 | 0.6378 | 0.9213 | 0.9528 | 26 | 127 |
| dataflow_aware | 42 | 0.6693 | 0.8898 | 0.9213 | 26 | 127 |
| dataflow_aware | 123 | 0.6772 | 0.9055 | 0.9528 | 26 | 127 |
| dataflow_aware | 456 | 0.6378 | 0.9213 | 0.9528 | 26 | 127 |

### 按策略均值对比

| 策略 | mean_recall@1 | mean_recall@5 | mean_recall@10 | std_recall@1 |
|------|---------------|---------------|----------------|--------------|
| **random** | **0.9396** | **0.9895** | **0.9895** | 0.0091 |
| embedding_distance | 0.6614 | 0.9055 | 0.9449 | 0.0203 |
| dataflow_aware | 0.6614 | 0.9055 | 0.9423 | 0.0203 |

### 关键发现

- **random 策略大幅领先**：recall@1 比另外两种策略高 27.8 个百分点 (0.94 vs 0.66)
- **embedding_distance 与 dataflow_aware 几乎完全相同**：mean_recall@1/5/10 基本一致
- 三种策略的 recall@10 差距收窄到约 4.5 个百分点
- random 策略 seed 间方差极小 (std=0.009)，另两种略高 (std=0.020)

---

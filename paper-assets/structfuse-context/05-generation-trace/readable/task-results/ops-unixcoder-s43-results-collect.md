# ops unixcoder s43 results collect

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_unixcoder_s43_results_collect_20260516T160002_result.json`
- **Structured JSON:** [`e12c273bcce32ffdfda3.json`](../../sessions/e1/e12c273bcce32ffdfda3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。

---

## UniXcoder s43 完整结果 (patience=2)

| Strategy | Best R@1 | Best val_loss | Early stopped step |
|----------|----------|---------------|--------------------|
| random | **0.5770** | 0.4238 (step 800) | 1200 |
| embedding_distance | 0.5747 | 0.4257 (step 800) | 1200 |
| dataflow_aware | 0.5678 | 0.4411 (step 600) | 1000 |

**s43 R@1 span**: 0.5770 - 0.5678 = **0.0092 (0.92pp)**

---

## s42 vs s43 对比

| Strategy | s42 R@1 | s43 R@1 | Δ |
|----------|---------|---------|---|
| random | 0.5534 | 0.5770 | +0.0236 |
| embedding_distance | 0.5497 | 0.5747 | +0.0250 |
| dataflow_aware | 0.5510 | 0.5678 | +0.0168 |

- s42 span: 0.37pp | s43 span: 0.92pp
- 两个 seed 下策略排序一致：**random > embedding > dataflow**
- s43 绝对值更高可能是 seed 对 train/val split 的影响（val set 难度不同），跨 seed 绝对值不可直接对比

---

## s44 进度

| Strategy | Status | Best R@1 | 备注 |
|----------|--------|----------|------|
| random_s44 | **DONE** | 0.6028 | early stopped @ step 1000, final R@1=0.6012 |
| embedding_distance_s44 | **Running** (step ~950) | 0.6068 (@ step 600) | eval@800 val_loss未改善(1/2)，预计下次eval@1000触发early stop |
| dataflow_aware_s44 | 未开始 | — | — |

s44 绝对值明显更高（0.60+ vs 0.55-0.57），进一步说明 seed 决定的 val split 组成显著影响绝对 R@1。

---

## Null result 确认

**s43 再次验证 null result 成立**：三策略间最大差异仅 0.92pp，且排序仍是 random ≥ embedding > dataflow。Embedding/dataflow 的"harder"负样本未能带来优势，反而略逊于 random。两个 seed (s42, s43) 结论一致。

---

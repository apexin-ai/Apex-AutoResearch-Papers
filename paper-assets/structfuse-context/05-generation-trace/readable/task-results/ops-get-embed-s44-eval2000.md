# ops get embed s44 eval2000

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_get-embed-s44-eval2000_20260515T155552_result.json`
- **Structured JSON:** [`6a43cbaeb5539f9b094d.json`](../../sessions/6a/6a43cbaeb5539f9b094d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整数据已提取。

## embedding_distance_s44 完整训练轨迹

| Step | val_loss | R@1 | R@5 | R@10 |
|------|----------|------|------|------|
| 500 | 0.4403 | 0.5942 | 0.9563 | 1.0 |
| 1000 | **0.4341** (best) | 0.5813 | 0.9643 | 1.0 |
| 1500 | 0.5256 | 0.5473 | 0.9421 | 1.0 |
| **2000** | **0.5182** | **0.5390** | **0.9468** | **1.0** |
| Final eval | 0.5123 | 0.5470 | 0.9481 | 1.0 |

- Early stop 在 step 2000 触发（patience 2/2），best val_loss=0.4341 at step 1000
- Final eval 指标略好于 eval@2000（可能用了 best checkpoint 做最终评估）

## random_s44 完整训练轨迹（交叉验证）

| Step | val_loss | R@1 | R@5 | R@10 |
|------|----------|------|------|------|
| 500 | **0.4252** (best) | **0.6009** | 0.9583 | 1.0 |
| 1000 | 0.4695 | 0.5638 | 0.9524 | 1.0 |
| 1500 | 0.4918 | 0.5592 | 0.9504 | 1.0 |
| Final eval | 0.4943 | 0.5542 | 0.9514 | 1.0 |

- random_s44 在 step 1500 early stop（patience 2/2），best at step 500

---

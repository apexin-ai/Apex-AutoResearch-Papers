# ops read pool50 full results

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read_pool50_full_results_20260516T051426_result.json`
- **Structured JSON:** [`f2160794a5f0c750558e.json`](../../sessions/f2/f2160794a5f0c750558e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Qwen2.5-Coder-3B Pool=50 Eval（12 checkpoints，按 R@1 降序）

| Checkpoint | R@1 | R@5 |
|---|---|---|
| embedding_distance_s43/best_by_recall_at_1 | **0.3897 ± 0.0048** | **0.9259 ± 0.0009** |
| random_s43/best_by_recall_at_1 | 0.3829 ± 0.0062 | 0.9121 ± 0.0019 |
| embedding_distance_s44/best_by_val_loss | 0.3694 ± 0.0057 | 0.9031 ± 0.0015 |
| dataflow_aware_s43/best_by_recall_at_1 | 0.3660 ± 0.0054 | 0.8931 ± 0.0027 |
| embedding_distance_s43/best_by_val_loss | 0.3331 ± 0.0036 | 0.8601 ± 0.0037 |
| dataflow_aware_s43/best_by_val_loss | 0.3203 ± 0.0053 | 0.8342 ± 0.0026 |
| random_s44/best_by_recall_at_1 | 0.3181 ± 0.0050 | 0.8253 ± 0.0044 |
| random_s44/best_by_val_loss | 0.3181 ± 0.0050 | 0.8253 ± 0.0044 |
| embedding_distance_s44/best_by_recall_at_1 | 0.3171 ± 0.0051 | 0.8473 ± 0.0035 |
| random_s43/best_by_val_loss | 0.3138 ± 0.0064 | 0.8265 ± 0.0042 |
| random_s42/best_by_recall_at_1 | 0.2730 ± 0.0049 | 0.7681 ± 0.0045 |
| random_s42/best_by_val_loss | 0.2730 ± 0.0049 | 0.7681 ± 0.0045 |

## StarCoder Pool=50 Eval（已完成，8 checkpoints）

| Checkpoint | R@1 | R@5 |
|---|---|---|
| random_s43/best_by_recall_at_1 | **0.2545 ± 0.0025** | **0.6430 ± 0.0017** |
| random_s43/best_by_val_loss | 0.2545 ± 0.0025 | 0.6430 ± 0.0017 |
| random_s44/best_by_recall_at_1 | 0.2493 ± 0.0042 | 0.6170 ± 0.0035 |
| random_s44/best_by_val_loss | 0.2407 ± 0.0054 | 0.6050 ± 0.0029 |
| random_s42/best_by_recall_at_1 | 0.2342 ± 0.0048 | 0.6293 ± 0.0016 |
| random_s42/best_by_val_loss | 0.2323 ± 0.0034 | 0.6048 ± 0.0031 |
| embedding_distance_s42/best_by_val_loss | 0.2289 ± 0.0038 | 0.5870 ± 0.0052 |
| embedding_distance_s42/best_by_recall_at_1 | 0.2271 ± 0.0033 | 0.5987 ± 0.0045 |

StarCoder eval 已完成（进程 142966 运行了 4 分钟，日志显示结果已保存）。注意 StarCoder 只评了 8 个 checkpoint（缺 embedding_distance_s43/s44 和 dataflow_aware_s43 的 checkpoints）。

---

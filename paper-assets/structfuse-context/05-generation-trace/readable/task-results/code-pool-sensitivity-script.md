# code pool sensitivity script

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pool_sensitivity_script_20260516T114426_result.json`
- **Structured JSON:** [`d98981d95917bfe5633a.json`](../../sessions/d9/d98981d95917bfe5633a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功完成。

---

## 产出总结

| 项目 | 结果 |
|------|------|
| `evaluate_pool50.py` 是否支持 `--pool-size` | **是**，已支持 |
| 新脚本路径 | `/root/structfuse/scripts/pool_sensitivity_eval.py` |
| test indices | `/root/autodl-tmp/structfuse/d062_splits/test_indices.txt`，**2476 行** ✓ |

**脚本功能**：接受 `--pool-sizes 10,20,50,100`，对每个 pool size 评估 R@1/R@5/R@10/MRR，输出汇总表 + JSON。支持 `--test-indices`（D062 test set）、`--max-queries`（dry-run）、`--seed`（可复现采样）、`--output-dir`。

**可用 Checkpoints**：

Qwen (`m2_full_qwen/`):
- `random_s42/s43/s44` — best_by_val_loss, best_by_recall_at_1
- `embedding_distance_s43/s44` — best_by_val_loss, best_by_recall_at_1
- `dataflow_aware_s43/s44` — best_by_val_loss, best_by_recall_at_1

StarCoder (`m2_full_starcoder/`):
- `random_s42/s43/s44` — best_by_val_loss, best_by_recall_at_1
- `embedding_distance_s42/s43` — best_by_val_loss, best_by_recall_at_1

**Dry-run 结果**（random_s43/best_by_val_loss, 5 queries）：

| Pool | R@1 | R@5 | R@10 | MRR |
|------|-----|-----|------|-----|
| 10 | 0.40 | 1.00 | 1.00 | 0.633 |
| 20 | 0.40 | 1.00 | 1.00 | 0.640 |

---

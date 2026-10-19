# analysis qwen training trajectories

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen-training-trajectories_20260515T174437_result.json`
- **Structured JSON:** [`025bf8d3183062bdc699.json`](../../sessions/02/025bf8d3183062bdc699.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`art_20260515_56de57` 已注册。

**产出**: `artifacts/analysis/qwen_training_trajectories.json`

**覆盖 5 个已完成 Qwen runs**:
| Run | Strategy | Seed | Regime | Eval Steps | Best R@1 |
|-----|----------|------|--------|------------|----------|
| random_s42 | random | 42 | 3 epochs, no ES | 8 + final | 0.5527 (step 1000) |
| random_s43 | random | 43 | ES@1500 | 3 + final | 0.5554 (step 1500) |
| random_s44 | random | 44 | ES@1500 | 3 + final | 0.6009 (step 500) |
| emb_dist_s43 | embedding_distance | 43 | ES@1500 | 3 + final | 0.5606 (step 1500) |
| emb_dist_s44 | embedding_distance | 44 | ES@2000 | 4 + final | 0.5942 (step 500) |

**交叉验证**: registry 数据和 server log 数值一致（registry 为四舍五入）。registry 对 random_s42 缺少 eval@3500/4000/final_eval，已从 log 补全。

**未完成 runs**: dataflow_aware_s43 正在运行（step ~500），dataflow_aware_s44/embedding_distance_s42/dataflow_aware_s42/bm25_s42~s44 尚未开始。

---

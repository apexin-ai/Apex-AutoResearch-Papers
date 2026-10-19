# code plan 018 bm25 mining

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_018_bm25_mining_20260514T163941_result.json`
- **Structured JSON:** [`344a81ac41463bc8d93c.json`](../../sessions/34/344a81ac41463bc8d93c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部生成成功。以下是完整摘要：

**生成的文件** (`/root/autodl-tmp/structfuse/full_m2_training_data/`):
| 文件 | Instances | 大小 |
|---|---|---|
| train_bm25_s42.jsonl | 11308 | 1.4GB |
| train_bm25_s43.jsonl | 11236 | 1.4GB |
| train_bm25_s44.jsonl | 11264 | 1.5GB |
| val_bm25_s{42,43,44}.jsonl | 同其他策略 | 296-345MB |

**验证通过**:
- Instance 数量与 random/embedding_distance/dataflow_aware 完全一致
- JSONL schema 完全匹配 (7 个字段)
- Query ID 和 positive ID 逐行对齐
- 0 个空 negatives
- candidate_tokens 键与 neg_candidates 完全匹配

**BM25 统计**:
- BM25 score: Mean=194.87, Std=124.48, Max=2638.22
- P25=100.46, P50=174.39, P75=272.95, P90=358.98

**与其他策略的 overlap (s42)**:
| 对比 | 平均重叠率 |
|---|---|
| bm25 vs random | 0.687±0.308 |
| bm25 vs embedding_distance | 0.759±0.237 |
| bm25 vs dataflow_aware | 0.621±0.265 |

BM25 与 embedding_distance 重叠最高 (76%)，与 dataflow_aware 最低 (62%)——符合预期，因为 dataflow_aware 额外排除了 dataflow 连通文件。

脚本路径: `/root/structfuse/scripts/mine_bm25_negatives.py`，总运行时间 ~5 分钟。

---

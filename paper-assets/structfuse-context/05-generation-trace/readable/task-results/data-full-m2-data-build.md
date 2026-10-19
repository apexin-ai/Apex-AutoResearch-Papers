# data full m2 data build

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_full_m2_data_build_20260513T160451_result.json`
- **Structured JSON:** [`681c7da2b7f5a0a6254b.json`](../../sessions/68/681c7da2b7f5a0a6254b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

M2 训练数据已全部构建完成，无需重新运行。

## 产出汇总

**路径**: `/root/autodl-tmp/structfuse/full_m2_training_data/`

| 文件 | 行数 | 大小 |
|------|------|------|
| `train_random_s42.jsonl` | 11,308 | 1.1G |
| `train_random_s43.jsonl` | 11,236 | 1.1G |
| `train_random_s44.jsonl` | 11,264 | 1.2G |
| `train_embedding_distance_s42.jsonl` | 11,308 | 1.3G |
| `train_embedding_distance_s43.jsonl` | 11,236 | 1.2G |
| `train_embedding_distance_s44.jsonl` | 11,264 | 1.3G |
| `train_dataflow_aware_s42.jsonl` | 11,308 | 1.1G |
| `train_dataflow_aware_s43.jsonl` | 11,236 | 1.1G |
| `train_dataflow_aware_s44.jsonl` | 11,264 | 1.2G |
| `val_*_s42.jsonl` (×3) | 2,980 each | 345M each |
| `val_*_s43.jsonl` (×3) | 3,052 each | 317M each |
| `val_*_s44.jsonl` (×3) | 3,024 each | 296M each |
| `dataflow_graph.json` | — | 94M |

**总磁盘占用**: 13GB

**数据差异验证**: 3 策略 train 文件行数相同但大小不同（random ~1.1G, embedding_distance ~1.3G, dataflow_aware ~1.1G），确认 negative mining 策略生效。embedding_distance 文件更大，因为 cosine-nearest negatives 倾向于选择更长的相似文件。

**构建时间**: 根据文件时间戳，2026-05-13 23:34 ~ 05-14 00:01，约 27 分钟完成 3 seeds。

**注意**: 脚本使用 seeds (42, 43, 44)，非任务描述中的 (42, 123, 456)。每 seed 约 11,200-11,300 train + 3,000 val instances，总 train ~33,808，val ~9,056。磁盘剩余 127GB 充足。

---

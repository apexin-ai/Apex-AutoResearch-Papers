# ops bm25 phase1 check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bm25_phase1_check_20260516T025415_result.json`
- **Structured JSON:** [`5697d90039bfefc0f5f9.json`](../../sessions/56/5697d90039bfefc0f5f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## BM25 Phase 1 状态：已完成

### 产出文件

路径：`/root/autodl-tmp/structfuse/full_m2_training_data/`

| 文件 | 大小 | 行数 | 日期 |
|------|------|------|------|
| `train_bm25_s42.jsonl` | 1.38 GB | 11,308 | May 15 |
| `val_bm25_s42.jsonl` | 345 MB | 2,980 | May 13 |
| `train_bm25_s43.jsonl` | 1.36 GB | 11,236 | May 13 |
| `val_bm25_s43.jsonl` | 316 MB | 3,052 | May 13 |
| `train_bm25_s44.jsonl` | 1.43 GB | 11,264 | May 14 |
| `val_bm25_s44.jsonl` | 296 MB | 3,024 | May 14 |
| **合计** | **~5.1 GB** | **42,864** | |

数据格式正确——每行是完整的 JSON 对象，包含 `query_id`、`query_tokens` 和负样本文件内容，可直接用于 Phase 2 训练。

### 附加产出
- `bm25_overlap_stratified.json`：BM25 vs Random 负样本重叠分析，平均重叠率 15.46%（83 repos, 8368 instances）
- `swebench_bm25_100.log`：BM25 索引构建日志

### StarCoder supplement 脚本
`/root/structfuse/scripts/run_m2_full_bm25_starcoder.sh` 已改为 BM25-only 策略（`--hard-negative-strategy "bm25"`），3 seeds 各 2 epochs + early_stopping_patience=2，配置与 Qwen 对齐。需要 StarCoder2-3B 模型下载到位后即可启动 Phase 2。

**结论：Phase 1（BM25 数据生成）已完成，无需启动。可直接进入 Phase 2 训练。**

---

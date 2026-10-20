# exp qwen completion check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_qwen_completion_check_20260521T065448_result.json`
- **Structured JSON:** [`bfed404f87090dc68430.json`](../../sessions/bf/bfed404f87090dc68430.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 完成状态
**4 个 GPU 全部完成**，日志均显示 "Experiment complete"。shard_0/1/2 正常完成，shard_3 通过 resume 完成。

### 2. 数据完整性
| Shard | 行数 | Conditions | 状态 |
|-------|------|-----------|------|
| shard_0 | 64,800 | 324 | 完整 |
| shard_1 | 64,800 | 324 | 完整 |
| shard_2 | 64,800 | 324 | 完整 |
| shard_3 (去重后) | 51,000 | 255 | **缺 69 conditions** |
| **合计** | **245,400** | **1,227/1,296** | **缺失 5.3%** |

**问题**：shard_3 的 resume（offset=130）与原始数据有 69 个 condition 重叠，导致 69 个 condition 被重复跑，另外 69 个 condition 完全缺失。已去重（每个 condition 保留 200 条），原始文件保留为 `shard_3_original.jsonl` 和 `shard_3_merged_with_dup.jsonl`。

### 3. 总体统计
- **总记录**：245,400（期望 259,200，缺 13,800）
- **Accuracy**：72.52%
- **Precision 分布**：bfloat16=100,200 / float16=79,600 / float32=79,400（不均匀因缺失条件）
- **Temperature 分布**：0.0=87,000 / 0.3=84,800 / 0.7=87,400
- **缺失 condition IDs**：70 个（含 ID=0 不存在），实际缺 69 个

### 4. GPU 状态
全部 4 个 GPU 空闲（0% 利用率，0 MiB 显存）。

### 下一步
需要补跑 69 个缺失 conditions（13,800 条记录）。缺失 ID 已定位，可以在单 GPU 上快速补完。

---

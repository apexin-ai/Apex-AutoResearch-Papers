# code miscalibration

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_miscalibration_20260518T114915_result.json`
- **Structured JSON:** [`686fe402602b1e081fb0.json`](../../sessions/68/686fe402602b1e081fb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果：

| | 样本数 | q_score 均值 | 示例样本 (原 0.9681) |
|---|---|---|---|
| 原始 | 371,499 | 0.5987 | 0.9681 |
| T=2.0 | 371,499 | 0.5916 | 0.8463 |
| T=3.0 | 371,499 | 0.5774 | 0.7572 |

温度越高，分数越趋向均匀（高置信度分数被压低，低置信度分数被提高），符合预期的 miscalibration 效果。文件已写入：
- `/root/provenance_weight_training/data/scored_data_T2.0.jsonl`
- `/root/provenance_weight_training/data/scored_data_T3.0.jsonl`

---

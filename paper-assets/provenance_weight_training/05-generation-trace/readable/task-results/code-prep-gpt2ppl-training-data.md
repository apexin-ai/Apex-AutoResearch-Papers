# code prep gpt2ppl training data

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_gpt2ppl_training_data_20260518T141807_result.json`
- **Structured JSON:** [`7b02b5fc516300974166.json`](../../sessions/7b/7b02b5fc516300974166.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**GPT-2 PPL Scoring**: 已完成 (371,499 / 371,499)

**q_score 转换结果**:
- 输出文件: `/root/provenance_weight_training/data/scored_data_gpt2ppl_qscore.jsonl`
- 分布: min=0.0000, max=1.0000, mean=0.5000

**Real vs Synthetic 对比**:
| | n | mean q_score |
|---|---|---|
| Real (depth=0) | 164,889 | 0.2703 |
| Synthetic (depth=1) | 206,610 | 0.6833 |

方向正确：Synthetic q_score (0.68) > Real q_score (0.27)，符合预期（低 PPL = 更可预测 = 更像合成文本 = 更高 q_score）。

---

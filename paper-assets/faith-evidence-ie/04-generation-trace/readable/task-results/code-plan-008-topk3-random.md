# code plan 008 topk3 random

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_008_topk3_random_20260515T135859_result.json`
- **Structured JSON:** [`db4b141ab8bd5d96857e.json`](../../sessions/db/db4b141ab8bd5d96857e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

格式完全匹配。输出验证通过：
- 8037 行 ✓
- 字段结构与 topk3 一致（`input`, `output`, `ced_score`, `doc_id`, `generation_idx`, `format_reward`, `f1_reward`, `combined_score`）✓

**结果汇总：**

| 指标 | 值 |
|------|-----|
| 全部 scored 样本 | 21,728 |
| f1 >= 0.1 过滤后 | 20,380 |
| 随机抽样数 | 8,037 |
| 覆盖 unique docs | 2,605 |
| mean f1_reward | 0.5054 |
| mean ced_score | 0.5285 |
| seed | 42 |

输出路径：`/root/autodl-tmp/rsft_filtered_topk3_random/rsft_train.jsonl`

---

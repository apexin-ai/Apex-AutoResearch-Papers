# knowledge update experiment plan 8b rsft

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_update_experiment_plan_8b_rsft_20260519T051036_result.json`
- **Structured JSON:** [`2141a6658ce44c74af96.json`](../../sessions/21/2141a6658ce44c74af96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

memory.md 已包含完整的 8B RSFT s44 数据和 2-seed 统计，无需再更新。

plan_019 已更新完成：

**plan_019 更新内容：**
- description 中 "8B-Qwen 需补 s44" → "8B-Qwen 2-seed 已完成（s42+s44）"
- 剩余缺口缩减为：1.7B s43/s44, LLaMA s43/s44
- 新增 notes 字段，记录 8B-Qwen 完整统计

**8B RSFT 2-seed 统计：**

| | SFT ign_f1 | RSFT ign_f1 | gain |
|---|---|---|---|
| s42 | 0.5051 | 0.5376 | +3.25pp |
| s44 | 0.4681 | 0.5451 | +7.70pp |
| **mean** | 0.4866 | **0.5414** | +5.48pp |
| **sample std** | 2.62pp | **0.53pp** | — |

RSFT 将 8B seed variance 压缩 ~5x（2.62pp → 0.53pp）。

---

# data plan020 expanded eval prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_plan020_expanded_eval_prep_20260520T054605_result.json`
- **Structured JSON:** [`fa8708093449b2ab667d.json`](../../sessions/fa/fa8708093449b2ab667d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**汇报**：

| 项 | 值 |
|---|---|
| 文件路径 | `/root/turn_residual_gating/data/eval_200/eval_200.json` |
| 数据来源 | `HuggingFaceH4/ultrachat_200k` train_sft split (shard 0) |
| 条数 | 200 |
| 平均轮数 | 6.1 |
| 最少轮数 | 4 |
| 最多轮数 | 14 |
| 轮数分布 | 4t:71, 6t:66, 8t:53, 10t:3, 12t:3, 14t:4 |
| 与训练集重叠 | **0**（按 prompt_id 验证） |
| 文件大小 | 1.25 MB |
| 格式 | JSON 数组，每条含 conversation_id, source, dataset_idx, prompt_id, num_turns, messages |

对比现有 heldout eval (50 条, avg 5.5 turns, 5-7 turns)，新 eval_200 覆盖了更广的轮数范围 (4-14)，更适合评估多轮场景下的 gate 行为。

---

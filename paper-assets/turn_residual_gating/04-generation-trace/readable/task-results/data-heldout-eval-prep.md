# data heldout eval prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_heldout_eval_prep_20260519T133725_result.json`
- **Structured JSON:** [`0ce3f4b49a5a81938c18.json`](../../sessions/0c/0ce3f4b49a5a81938c18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出文件 `/root/turn_residual_gating/data/ultrachat_eval_heldout.json` 已就绪。

**报告**：

| 项目 | 详情 |
|------|------|
| 数据来源 | `HuggingFaceH4/ultrachat_200k` train_sft split |
| idx 范围 | 8843 – 68199（全部 >= 8000，与训练集 0-7999 无重叠） |
| prompt_id 重叠 | 0（额外用 prompt_id 去重，排除了 25 个在训练集中重复出现的对话） |
| 样本数 | 50 |
| 轮数分布 | 5 turns × 31, 6 turns × 14, 7 turns × 5 |
| messages 数量 | 10-14 条/样本（与训练数据一致） |
| 格式 | 与 `ultrachat_eval_sample.json` 完全一致（conversation_id, source, dataset_idx, num_turns, messages） |
| 文件大小 | 428.3 KB |

---

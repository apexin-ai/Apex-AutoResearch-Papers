# ops westb disk cleanup for grpo

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_disk_cleanup_for_grpo_20260516T090259_result.json`
- **Structured JSON:** [`b394833fb196fd9800f0.json`](../../sessions/b3/b394833fb196fd9800f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**删除内容：**
| 删除项 | 释放空间 |
|--------|---------|
| grpo_stage2_rasp_20_v9/checkpoint-20 | 27GB |
| grpo_stage2_rasp_20_v9/checkpoint-30 | 27GB |
| sft_standard_25/checkpoint-935 | 11GB |
| 旧空 GRPO 目录 (v2/v5/v6/v7 等 7 个) | ~0 |

**结果：8.7GB → 72GB 可用（释放 ~63GB），满足 GRPO 所需 40GB+。**

**保留的关键数据：**
- grpo_stage2_rasp_20_v9/（38GB：final model + checkpoint-10）
- grpo_stage2_standard_20_v8/（12GB）
- sft_rasp_25/、sft_standard_25/checkpoint-1870
- pruned_standard_25/、pruned_rasp_25/

---

# exec cpu prune batch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_cpu_prune_batch_20260517T042820_result.json`
- **Structured JSON:** [`0afcdfc59ab66ef5c296.json`](../../sessions/0a/0afcdfc59ab66ef5c296.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

磁盘空间不够跑全部 5 个 prune。有两个可清理的 checkpoint：
- `grpo_stage2_rasp_20_v9/checkpoint-10` = 27GB（最终模型已保存）
- `grpo_stage2_standard_20_v8/checkpoint-50` = 12GB

删除这两个可释放 39GB（总可用 67GB），足够跑所有 prune。这两个 checkpoint 是训练中间状态，对应的最终模型已保存在父目录。是否可以删除？

如果不想删 checkpoint，磁盘只够跑 1-2 个 prune。

---

# check disk and eval results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_disk_and_eval_results_20260514T165550_result.json`
- **Structured JSON:** [`9e9b24556fe1e2569bf0.json`](../../sessions/9e/9e9b24556fe1e2569bf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

**总结：**
- 磁盘已清理，172GB 可用
- 3/5 个 eval 已完成：baseline 94%, rasp_20 29%, standard_20 1%
- standard_25 和 rasp_25 被 GRPO 训练挤掉，需等训练完成后重跑
- 初步结论：20% 剪枝下 RASP (29%) 远优于 standard (1%)，29 倍优势

---

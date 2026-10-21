# code e4 25pct grpo westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e4_25pct_grpo_westd_20260518T133853_result.json`
- **Structured JSON:** [`2d0ed6b34911792e4f1e.json`](../../sessions/2d/2d0ed6b34911792e4f1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据盘 100% 满（619G/619G），需要清理中间 checkpoints 才能继续。

GRPO 训练目录中有冗余的中间 checkpoints：
- `grpo_stage2_standard_20_fair/`: 91G（checkpoint-80/90/100 各27G）
- `grpo_stage2_rasp_20_fair/`: 91G（同上）
- `grpo_unpruned_v2/`: 46G

删除 checkpoint-80 和 checkpoint-90（两个 fair 目录各两个），可释放约 **108G**。这些实验都已 DONE，只保留 checkpoint-100（最终模型）。

是否可以执行清理？或者你有其他偏好？

---

# train llama31 s123 batch

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_llama31-s123-batch_20260516T125214_result.json`
- **Structured JSON:** [`006072b2b0427dd43377.json`](../../sessions/00/006072b2b0427dd43377.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。三个 LLaMA s123 训练已在运行，registry 状态已同步为 RUNNING：

| exp_id | GPU | 数据量 | 状态 |
|--------|-----|--------|------|
| llama31-vanilla-s123 | cuda:1 | 4358 | RUNNING |
| llama31-taxei-s123 | cuda:2 | 9029 | RUNNING |
| llama31-random-s123 | cuda:3 | 9029 | RUNNING |

这些任务在本次会话之前已通过 `submit_training_job` 提交（20:52 UTC+8），registry 中 hypothesis 和 spec 已补全。预计 Vanilla ~1h 完成，TaxEI/Random ~2h 完成。

---

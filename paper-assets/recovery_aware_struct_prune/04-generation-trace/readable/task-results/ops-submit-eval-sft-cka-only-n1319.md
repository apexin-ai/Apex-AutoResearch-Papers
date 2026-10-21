# ops submit eval sft cka only n1319

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_eval_sft_cka_only_n1319_20260517T175956_result.json`
- **Structured JSON:** [`86fa0223edc13ba7f23c.json`](../../sessions/86/86fa0223edc13ba7f23c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **参数名**: `--max_samples`，确认正确
- **cuda:0**: 空闲（0MiB, 0% util）
- **模型不存在**: westd 上没有 `/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/`

`sft_cka_only_20` 是在 westb 上训练的，westd 上不存在该模型。**无法在 westd 上提交 eval job，需要先从 westb 拷贝模型到 westd。**

---

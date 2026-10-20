# code grpo v5 standard submit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo-v5-standard-submit_20260515T123637_result.json`
- **Structured JSON:** [`dc72786a4c54f884d5be.json`](../../sessions/dc/dc72786a4c54f884d5be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已成功启动。日志确认：

- **pid**: 518411，运行在 westb-23072 cuda:1
- 模型正在从 `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20` 加载
- 检测到 non-uniform MLP（与 RASP 一致的剪枝结构），模型加载正常

参数与 RASP v5 完全一致：`beta=0.01, loss_type=dapo, format_reward_weight=0.1, temperature=0.4, repetition_penalty=1.15, max_completion_length=512, num_train_epochs=1, max_samples=1000, lr=1e-6, gradient_checkpointing=true`。

---

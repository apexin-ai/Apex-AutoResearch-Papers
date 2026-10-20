# code fix train grpo

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-train-grpo_20260512T133417_result.json`
- **Structured JSON:** [`9f9508ad2a0eaee61212.json`](../../sessions/9f/9f9508ad2a0eaee61212.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`--help` 验证通过，脚本正常解析。

**修复内容：**
- `train_grpo.py` 原第 67 行 `max_prompt_length=grpo_args.max_prompt_length` 已删除。该参数在 TRL 1.1.0 的 `GRPOConfig` 中不存在，传入会报错。
- `config.py` 中 `GRPOArgs.max_prompt_length` 字段保留（仍可通过 CLI 传入，只是不再传给 GRPOConfig）。
- `train_sft.py` 已使用 `max_length`（非 `max_seq_length`），无兼容问题。
- 未发现其他 TRL 1.1.0 不兼容参数。

stderr 中的 vLLM 版本警告是 TRL 对 vLLM 0.18.1 的兼容提示，不影响 GRPO 训练。

---

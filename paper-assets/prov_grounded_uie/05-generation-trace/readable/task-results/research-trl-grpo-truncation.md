# research trl grpo truncation

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_trl-grpo-truncation_20260512T170426_result.json`
- **Structured JSON:** [`375e77ccfecf055cc524.json`](../../sessions/37/375e77ccfecf055cc524.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/root/autodl-tmp/prov_grounded_uie/artifacts/trl_truncation_analysis.md`。

核心结论：**TRL 1.1.0 GRPOTrainer 没有任何内置 prompt 截断机制。** `max_prompt_length` 参数不存在，`_tokenize_prompts()` 对 prompt 不做截断，`max_completion_length`（默认 256）仅控制 completion 长度。过长 prompt 在 vLLM 模式下会直接报错，在 transformers 模式下行为未定义。需要在 data_utils.py 中手动实现左截断。

---

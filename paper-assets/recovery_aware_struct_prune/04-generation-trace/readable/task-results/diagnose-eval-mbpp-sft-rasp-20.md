# diagnose eval mbpp sft rasp 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_mbpp_sft_rasp_20_20260519T182304_result.json`
- **Structured JSON:** [`b834776a67893b17e7a0.json`](../../sessions/b8/b834776a67893b17e7a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**根因：模型路径错误。** `sft_rasp_20` 不存在，正确路径是 `sft_rasp_20_1p5b`。

Transformers 找不到本地目录后尝试将绝对路径当 HF repo id 解析，触发 `HFValidationError` → `OSError` 退出。

**修复**：重新提交，`--model_path` 改为 `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b`。

---

# code qwen bf16 reeval

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen_bf16_reeval_20260514T062423_result.json`
- **Structured JSON:** [`0cbde93b57352cbcef79.json`](../../sessions/0c/0cbde93b57352cbcef79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

bf16 re-eval 完成，**fp16 和 bf16 数字几乎完全一致**：

| Metric | bf16 | fp16 | delta |
|---|---|---|---|
| **Baseline PPL** | 9.8106 | 9.81 | 0.0006 |
| **Uniform 4-bit PPL** | 15.4454 | 15.45 | 0.0046 |

两个 delta 都远低于 0.3 阈值，**compounding sweep 不需要 bf16 rerun**。

注意：之前 agent_context 中提到的 "bf16 baseline=8.82" 与实际结果不符——实际 bf16 baseline 是 9.81，和 fp16 一致。8.82 那个数字可能是不同 eval 设置（不同 stride 或 sequence length）下的结果，或是记录错误。

结果已保存到 `/root/ratekv/bf16_reeval_results.json`，registry `qwen_bf16_reeval` 已标记 DONE/success。

---

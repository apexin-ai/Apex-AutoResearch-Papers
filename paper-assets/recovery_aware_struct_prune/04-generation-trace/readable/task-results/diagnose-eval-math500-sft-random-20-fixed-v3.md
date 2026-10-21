# diagnose eval math500 sft random 20 fixed v3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_sft_random_20_fixed_v3_20260524T085711_result.json`
- **Structured JSON:** [`7716b4272ee436f3801c.json`](../../sessions/77/7716b4272ee436f3801c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 **eval_math500_sft_random_20_fixed_v3** 完成，状态：**成功**。

| 指标 | 值 |
|------|-----|
| Accuracy | 16.6% (83/500) |
| Stderr | ±0.0166 |
| Truncation rate | 65.8% (329/500 被截断) |
| Avg response length | 1470.44 tokens |
| Natural EOS | 171/500 |

Registry 已更新为 DONE/success。Cron 监控不存在（可能已被清除）。

值得注意：65.8% 的 truncation rate 很高，说明 sft_random_20 模型在 2048 max_new_tokens 下仍频繁触达长度限制，模型生成效率较差。

---

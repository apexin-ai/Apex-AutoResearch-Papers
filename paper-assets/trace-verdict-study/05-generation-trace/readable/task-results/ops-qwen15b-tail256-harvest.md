# ops qwen15b tail256 harvest

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen15b_tail256_harvest_20260517T205440_result.json`
- **Structured JSON:** [`2c9722922318d8d74250.json`](../../sessions/2c/2c9722922318d8d74250.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（之前可能已被清除）。

## 收割总结

| 指标 | Qwen-1.5B tail-256 | Qwen-7B tail-256 |
|------|-------------------|-----------------|
| Accuracy | 72.6% [70.0%, 75.3%] | 78.9% |
| Lift over majority | +1.1pp [-2.1pp, +4.4pp] | +7.4pp |
| Fail F1 | 0.54 | — |

**结论：negative**。假设被否定。1.5B 在 tail-256 条件下仅比 majority baseline 高 1.1pp（CI 包含 0，不显著），而 7B 达到 78.9%。这说明 256-token 尾部截断下的 phase transition 是 **capacity-limited**（模型容量受限），而非单纯 signal-limited。1.5B 不具备从 256 token trace 尾部提取足够判别信号的能力。

---

# diagnose eval sft standard 25

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_sft_standard_25_20260516T132227_result.json`
- **Structured JSON:** [`628b531cfbebbf927cae.json`](../../sessions/62/628b531cfbebbf927cae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。eval_sft_standard_25 已验证并关闭：

| 指标 | 值 |
|------|-----|
| accuracy | **51.25%** ± 1.38% |
| n_correct / n_total | 676 / 1319 |
| eos_rate | 95.45% |
| avg_len | 326.26 |

Registry 已更新为 DONE/success，cron 已删除。

对比 20% sparsity (Standard 64%)，25% sparsity 下 Standard SFT 降至 51.25%，下降约 13 个百分点。

---

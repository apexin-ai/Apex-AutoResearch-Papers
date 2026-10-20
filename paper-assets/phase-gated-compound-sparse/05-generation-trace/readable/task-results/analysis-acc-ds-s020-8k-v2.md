# analysis acc ds s020 8k v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acc_ds_s020_8k_v2_20260515T232745_result.json`
- **Structured JSON:** [`be709f89acdbb74cc77e.json`](../../sessions/be/be709f89acdbb74cc77e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在，无需删除。

**状态：SUCCESS**

| 指标 | 值 |
|------|-----|
| accuracy | 30.0% (15/50) |
| truncated | 29/50 (58%) |
| total_time | 5549s (~92min) |
| exit_code | 0 |

注意：hypothesis 预期 8k 截断率 <20%，实际 58%——从 4096 的 64% 仅降至 58%，s020 条件下模型大量问题仍耗尽 8192 tokens 未能得出答案。

---

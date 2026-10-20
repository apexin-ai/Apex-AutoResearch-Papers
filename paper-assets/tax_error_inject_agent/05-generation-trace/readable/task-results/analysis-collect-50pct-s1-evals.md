# analysis collect 50pct s1 evals

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_collect-50pct-s1-evals_20260516T013007_result.json`
- **Structured JSON:** [`5998c271cde7a0b844bb.json`](../../sessions/59/5998c271cde7a0b844bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无 cron 需要清理。

**汇总（50% inject, valid_unseen 47 tasks）：**

| Seed | TaxEI | Random | Delta (TaxEI - Random) |
|------|-------|--------|------------------------|
| s7 | 55.3% | 46.8% | **+8.5pp** |
| s1 | 63.8% | 70.2% | **-6.4pp** |

s1 seed 下 Random 反超 TaxEI 6.4pp，与 s7 方向相反。两个 seed 的结果方向不一致，说明当前样本量下 variance 很大，TaxEI vs Random 的差异尚不显著。需要剩余 3 个 seed（s2/s3/s5）的结果才能判断趋势。

---

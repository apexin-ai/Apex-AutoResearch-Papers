# ops check lead2 ckpt20 result

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_lead2_ckpt20_result_20260517T152546_result.json`
- **Structured JSON:** [`f8e1c7430ec259c7ee27.json`](../../sessions/f8/f8e1c7430ec259c7ee27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：RSFT→GRPO pipeline 可行。**

Checkpoint-20 vs RSFT baseline 对比：
- **rel_f1**: 0.4617 vs 0.4601 (+0.16pp) — 性能保持
- **evi_f1_joint**: 0.3642 vs 0.3605 (+0.37pp) — 证据质量略提升
- **edcr**: 0.6465 vs 0.6542 (-0.77pp) — 干扰引用率下降（更好）
- 100% format compliance，无错误

GRPO 在仅 20 步后已略微超越 RSFT baseline 的所有核心指标，说明从 RSFT 出发做 GRPO 不会导致性能退化，pipeline 设计正确。

Registry 已更新为 DONE/success，cron 已清除。

---

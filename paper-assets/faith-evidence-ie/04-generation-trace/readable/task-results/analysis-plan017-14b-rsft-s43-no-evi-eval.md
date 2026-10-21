# analysis plan017 14b rsft s43 no evi eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan017_14b_rsft_s43_no_evi_eval_20260523T200057_result.json`
- **Structured JSON:** [`020c15288170f912377e.json`](../../sessions/02/020c15288170f912377e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

## plan017_14b_rsft_s43_no_evi_eval 结果

| Metric | s43 no-evi | s42 no-evi | Δ |
|--------|-----------|-----------|---|
| **Ign-F1** | **0.5713** | 0.5432 | **+2.81pp** |
| F1 | 0.5850 | — | — |
| Precision | 0.5491 | — | — |
| Recall | 0.6260 | — | — |
| Format OK | 99.80% | — | — |
| Truncated | 92/985 | — | — |

s43 seed 在 no-evidence 条件下比 s42 提升 +2.81pp。s43 with-evidence eval 还在跑，跑完后可计算 s43 evidence tax（s42 dev evidence tax 为 +4.54pp）。

Registry 已更新为 DONE/success，分析报告已注册。

---

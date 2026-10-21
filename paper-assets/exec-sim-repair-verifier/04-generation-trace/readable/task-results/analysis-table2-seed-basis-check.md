# analysis table2 seed basis check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table2-seed-basis-check_20260518T185458_result.json`
- **Structured JSON:** [`9084bf9873bca97f589b.json`](../../sessions/90/9084bf9873bca97f589b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Table 2 没有误差线**，不存在 "training seed vs bootstrap seed" 的选择问题。

- Table 2 直接展示两个 **training seed** (42, 123) 的原始 accuracy 和算术平均值，列结构为 `s42 | s123 | Mean | Δ`
- 文中紧随其后的 clustered bootstrap (p=0.0066, 95% CI [1.80, 2.71]) 是对 CLS–CWM gap widening 的显著性检验（用了 3-seed superset: 42/123/456, 10K resamples, 114 clusters），不是 Table 2 的误差线

答案文件已注册为 `art_20260518_4138aa`，含 Reviewer Q5 的 response draft。

---

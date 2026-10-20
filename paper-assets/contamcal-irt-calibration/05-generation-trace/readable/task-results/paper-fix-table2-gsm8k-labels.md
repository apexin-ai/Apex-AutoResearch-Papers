# paper fix table2 gsm8k labels

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-table2-gsm8k-labels_20260522T035545_result.json`
- **Structured JSON:** [`837ad303eb19609969d8.json`](../../sessions/83/837ad303eb19609969d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

四处修改完成：

- **Table 2 (cross-seed)**：OLMo-2 s123 列 `−` → `0`，脚注 `+/−/+` → `+/0/+`
- **results.tex 正文**：`+2.1pp at s42` → `mean +2.1pp across s42/s123`
- **appendix.tex GSM8K 表脚注**：`Seed=42; +2.1pp` → `Mean across seeds: +2.1pp (s42: +1.7pp, s123: +2.4pp); s0 shows +9.2pp`

---

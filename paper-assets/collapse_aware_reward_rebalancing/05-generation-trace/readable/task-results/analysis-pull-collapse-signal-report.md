# analysis pull collapse signal report

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pull_collapse_signal_report_20260517T033341_result.json`
- **Structured JSON:** [`058c3f8bc1169f9aa9c3.json`](../../sessions/05/058c3f8bc1169f9aa9c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个文件已保存：

- `artifacts/collapse_signal_report.json` - 完整结构化数据（含 top-5 ngrams、所有 metric 数值）
- `artifacts/collapse_signal_summary.md` - 人类可读摘要

核心结论：K=8 curation 的 collapse 主要是 FORMAT/TEMPLATE 层面的（opening pattern entropy 下降 1.13 bits，near-duplicate start rate 从 50% 跳到 84%），而非语义层面的。Vendi Score 对此类表层模板化无感知力，需要 opening_entropy 或 n-gram distinctness 作为补充指标。

---

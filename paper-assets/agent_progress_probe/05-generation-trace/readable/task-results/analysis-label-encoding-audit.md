# analysis label encoding audit

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_label-encoding-audit_20260514T131920_result.json`
- **Structured JSON:** [`f893c1b3745e6c4422b5.json`](../../sessions/f8/f893c1b3745e6c4422b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/report_label_encoding_audit.md`。

**结论：编码一致，无反转。** 两条管线共享同一套 `labeling_functions.py`（`PROGRESS=1, STAGNATION=0`），数据从标注到训练/评估全程无标签变换。5 个抽样窗口人工验证全部通过。

macro-F1=0.528 的真实原因是类别分布偏移（OpenHands stagnation 6.6% vs SWE-agent 36.6%）和行为模式差异，不是标签问题。

---

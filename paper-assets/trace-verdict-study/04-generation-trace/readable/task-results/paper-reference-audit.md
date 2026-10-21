# paper reference audit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reference-audit_20260516T045759_result.json`
- **Structured JSON:** [`14638f90d84ae6a28c08.json`](../../sessions/14/14638f90d84ae6a28c08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心结论：

**引用完整性**: 28 个 cite key 与 bib 完全 1:1 匹配，无遗漏无冗余。

**Critical 问题 (1个)**: experiments.tex 的 Tables 1–3 caption 放在表格下方，ACL 要求在上方。需要把 `\caption`+`\label` 移到 `\begin{tabular}` 之前。

**Should Fix (4个)**:
- per_class 表中 "VOTA$-$AE" 应改为 `\texttt{VOTA\_no\_ae}`
- Table 3 中 `label\_only` 缺 `\texttt{}`
- per_class 表中 "Full Trace (LO)" 命名不统一
- Abstract/conclusion 中 "85.6%" 与 Table 2 的 "85.63%" 不一致

**ARR 合规**: 全部通过（匿名、limitations、ethics、checklist 完整、无去匿名化泄露）。

**数据一致性**: VOTA_no_ae 99.41% 全文一致；需确认 registry 99.40% 的 rounding convention 差异是否需要对齐。

完整报告已写入 `artifacts/reference_audit_report.md`。

---

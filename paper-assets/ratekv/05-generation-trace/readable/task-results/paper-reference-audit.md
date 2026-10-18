# paper reference audit

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reference_audit_20260514T120938_result.json`
- **Structured JSON:** [`ed3bbba7727ab0c84430.json`](../../sessions/ed/ed3bbba7727ab0c84430.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/reference_audit_report.md`。

核心结论：
- **19 条 bib 条目与 .tex 引用完全一致**，无孤立、无缺失、无重复
- **5 篇抽查全部真实**，无幻觉引用
- 发现 **2 处轻微问题**：`lin2024qserve` 的 key 隐含 2024 但实际 venue 是 MLSys 2025；`liu2024scissorhands` 的 key 隐含 2024 但实际是 NeurIPS 2023。这是命名规范不一致，不影响编译

---

# paper compile and audit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile-and-audit_20260514T200003_result.json`
- **Structured JSON:** [`1bf662edf805e1feecd6.json`](../../sessions/1b/1bf662edf805e1feecd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查报告已写入 `artifacts/paper_compile_audit.md`。

**核心结论**：
- **编译**：4 遍 pdflatex+bibtex 成功，18 页 PDF
- **CRITICAL**：正文（intro→conclusion）占 1–13 页，超 ACL 8 页限制约 5 页，必须压缩
- **WARNING**：
  - 正文表格 6 处 overfull hbox（experiments.tex 的 Table 1/2/4）
  - appendix 8 处 overfull（hyperparam 表 + verbatim 代码块）
  - 14 个 `\label` 定义但未引用（含 4 个公式标签、3 个 appendix 标签）
  - `[h]` float 被 ACL 改为 `[ht]`（appendix.tex L13）
- **INFO（全部干净）**：
  - 0 undefined refs / 0 undefined citations
  - 33 bib 条目 ↔ 33 引用 完美 1:1
  - 4 张图全部存在且被引用
  - 无 PLACEHOLDER / TODO
  - 后续 pass 稳定，无 Rerun 警告

下一步优先级：先砍 5 页正文（C1），再处理表格 overfull (W1) 与 unused labels (W3)。

---

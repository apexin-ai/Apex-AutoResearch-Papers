# paper consistency fix minor

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_consistency-fix-minor_20260516T011352_result.json`
- **Structured JSON:** [`6775ccaa53aa3ff30d9e.json`](../../sessions/67/6775ccaa53aa3ff30d9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

- **`dual-constrained`** 只剩 `consistency_audit.md`（审查报告本身，不改）。论文 .tex/.md 文件已全部统一为 `dual-constraint`。
- **`17.650`** 只剩表格中 Grid-best seed456 的实际数据点（17.650 是正确的原始值，不是 mean），intro 中的错误 mean 已修正。
- **`17.722`** 只剩 `consistency_audit.md`（审查报告），论文文件已全部修正为 `17.723`。
- **`tab:main-results`** 只剩 `consistency_audit.md`，`table1_main_results.tex` 已改为 `\label{tab:main}`。

---

## 修改汇总

| 文件 | 修改内容 |
|------|---------|
| `introduction_c6a67f.tex` | PPL `17.650` → `17.651` |
| `introduction_a663ee.tex` | PPL `17.722` → `17.723`; `dual-constrained` → `dual-constraint` (2处) |
| `introduction.tex` | PPL `17.722` → `17.723`; `dual-constrained` → `dual-constraint` (2处) |
| `introduction_draft.md` | PPL `17.722` → `17.723`; `dual-constrained` → `dual-constraint` (2处) |
| `discussion_270aaa.tex` | `dual-constrained` → `dual-constraint` |
| `discussion.tex` | `dual-constrained` → `dual-constraint` |
| `conclusion_386ecc.tex` | `dual-constrained` → `dual-constraint` |
| `conclusion.tex` | `dual-constrained` → `dual-constraint` |
| `table1_main_results.tex` | `\label{tab:main-results}` → `\label{tab:main}` |

所有 `\ref{tab:main}` 引用（results_d0d647.tex、results.tex、results_819b43.tex、discussion.tex、discussion_270aaa.tex）均已与 label 匹配。

---

# paper domain matrix table

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_domain-matrix-table_20260517T234025_result.json`
- **Structured JSON:** [`651c462c1197f46ca9cf.json`](../../sessions/65/651c462c1197f46ca9cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个表格已生成并注册：

1. **`tab_domain_model_kstar.tex`** — 正文主表，单栏适配，5列（Model, Size, C4/arXiv/Wiki K*），含 Dominant 总结行和三条 footnote 解释异常值。
2. **`tab_domain_model_kstar_full.tex`** — 附录详表，双栏 `table*`，含 AUC(boundary) 值，用 `\cmidrule` 分组三个 domain。

设计要点：
- booktabs 风格，bold 标注 dominant mode
- Caption 自包含，无破折号
- Footnote 用 `†/‡/*` 区分三类异常（scorer artifact / one-wash / capacity failure）
- 引用方式：`\ref{tab:domain_model_kstar}` / `\ref{tab:domain_model_kstar_full}`

---

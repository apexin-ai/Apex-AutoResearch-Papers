# paper citation fix qwen3

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_citation-fix-qwen3_20260515T150754_result.json`
- **Structured JSON:** [`afedd5743d822ae51ee9.json`](../../sessions/af/afedd5743d822ae51ee9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。变更摘要：

- `experiments.tex` 第16行：`\cite{yang2024qwen25}` → `\cite{qwen2025qwen3}`
- `references.bib`：删除 `ni2023lever`、`chen2023codet`、`andrews2005mutation`、`just2014mutants` 四个孤立条目
- `qwen2025qwen3` 条目已验证正确（arXiv:2505.09388, 2025）
- Commit: `ab4698f` "fix: correct Qwen3 citation key and remove orphan bib entries"

---

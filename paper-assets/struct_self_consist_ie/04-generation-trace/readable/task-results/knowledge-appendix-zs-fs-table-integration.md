# knowledge appendix zs fs table integration

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_appendix-zs-fs-table-integration_20260520T022104_result.json`
- **Structured JSON:** [`835bc1cb91a36a771645.json`](../../sessions/83/835bc1cb91a36a771645.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

插入完成。

**插入位置**: `appendix.tex` 末尾，紧接 `\subsection{Construction Weighting Variants}` 之后（line 1649），作为新 `\subsection{Zero-Shot vs.\ Few-Shot Comparison}`（`\label{app:zs_vs_fs}`）。

**内容**:
- `table*` 环境 + `\resizebox{\textwidth}{!}` 防止 overfull hbox
- 3 句解读：(1) construction 仅 SciERC ZS 显著 (+1.53pp, p=.008)；(2) FS 提升 greedy baseline 但不改善 construction；(3) dual-gating 在 FT+ZS 成立，FS 有独立失效因素，交叉引用 `\S\ref{app:fs_error}`
- "significant" 仅用于 p=.008 的 SciERC ZS 结果

---

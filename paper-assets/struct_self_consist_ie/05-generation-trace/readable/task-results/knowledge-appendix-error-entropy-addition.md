# knowledge appendix error entropy addition

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_appendix-error-entropy-addition_20260520T030113_result.json`
- **Structured JSON:** [`38b095f5061c16112ac8.json`](../../sessions/38/38b095f5061c16112ac8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**插入位置**：`\subsection{Few-Shot Error Correlation Analysis}`（`\label{app:fs_error}`），原 Jaccard 段落之后、closing 句之前（第 1625-1628 行）。

**插入内容**（3 句）：
- SciERC entropy 无显著差异（0.483 vs 0.485, p=0.81）
- CoNLL entropy 在 FS 下显著更高（0.209 vs 0.184, p<10⁻⁹, r=0.106 small effect, Wilcoxon signed-rank）
- 更新了 closing 句：error overlap preserved + entropy may rise → nature rather than diversity of errors

所有数值与 `fs_vs_zs_error_correlation.json` 一致。

---

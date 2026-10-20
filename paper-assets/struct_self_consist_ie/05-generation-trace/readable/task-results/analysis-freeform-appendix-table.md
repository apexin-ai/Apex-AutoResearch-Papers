# analysis freeform appendix table

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_freeform_appendix_table_20260515T102920_result.json`
- **Structured JSON:** [`9146e4de5f50c75f407b.json`](../../sessions/91/9146e4de5f50c75f407b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已生成并注册。文件在 `artifacts/freeform_ablation_appendix_table.tex`，包含四个 Panel：

- **A** — Logprob 分布对比（mean std/range/tied fraction，Δ 均为负，压缩假说未被证实）
- **B** — Selection F1（NER + RE，含 greedy / LP-selected / selection gap）
- **C** — QE Spearman ρ 对比（5 signals × 2 tasks，正 Δ 加粗）
- **D** — Parse rate（99.95%）

需要 `\usepackage{booktabs, multirow}`。

---

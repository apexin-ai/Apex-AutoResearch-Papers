# analysis n8 vs n16 appendix tables

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n8_vs_n16_appendix_tables_20260515T120506_result.json`
- **Structured JSON:** [`7eaeb835f2811a154ad4.json`](../../sessions/7e/7eaeb835f2811a154ad4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/n_scaling_appendix_tables.tex`，包含三个表格：

- **Table 1** (`tab:n-scaling`): N=8 vs N=16 Spearman ρ 对比，5 signals + mean，所有 Δ 均为正（全部加粗）。NER 平均提升 +0.031，RE +0.025。
- **Table 2** (`tab:ranking-stability`): 5 个 setting 的 Kendall's W。Qwen NER N=8 和 LLaMA NER N=8 达到 W=1.000（完美一致）；Qwen RE N=8 最低 W=0.822；N=16 后 NER/RE 均升至 0.956。
- **Table 3** (`tab:sigma-comparison`): 跨种子 σ 对比。NER 均值 σ 从 0.0145 降至 0.0098，RE 从 0.0151 降至 0.0114。VC-NER 是唯一 σ 上升的例外（0.0187→0.0260）。

---

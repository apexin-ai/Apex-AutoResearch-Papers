# code analyze phase2

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analyze_phase2_20260513T063622_result.json`
- **Structured JSON:** [`33b70d8793859049acd7.json`](../../sessions/33/33b70d8793859049acd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。脚本已创建并成功运行：

**表格输出**：3 方法 × 8 代（external_only 目前只有 gen 0-1）的 PPL/RankMe/k-NN/rare_ngram/rank_corr，含 Δ% 行。

**4 个 PDF 图表**已生成到 `artifacts/`：
- `rare_ngram_survival.pdf`
- `ppl_comparison.pdf`
- `selection_diagnostics.pdf`
- `quality_filter_diagnostics.pdf`

**判定结果**：FAIL — external_only 缺少 gen7 数据（仅跑到 gen 1），无法与 RGDS gen7 对比。

---

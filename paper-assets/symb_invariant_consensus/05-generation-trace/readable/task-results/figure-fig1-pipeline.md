# figure fig1 pipeline

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig1_pipeline_20260517T165452_result.json`
- **Structured JSON:** [`7b79d9146fd0ccb9af25.json`](../../sessions/7b/7b79d9146fd0ccb9af25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**输出文件**：
- PDF: `/root/symb_invariant_consensus/artifacts/figures/paper/fig1_pipeline.pdf` (45 KB)
- PNG: `/root/symb_invariant_consensus/artifacts/figures/paper/fig1_pipeline.png` (221 KB)

**脚本**：`/root/symb_invariant_consensus/scripts/fig1_pipeline.py`（本地和服务器各一份）

图中展示了 SICA 与 SC 的对比：共享左侧 Question → LLM Sampling → K Traces，然后分叉为 SICA 上路径（FOL Constraint Extraction → Dedup + Weighting → Partial MAX-SAT → Cross-Answer Scoring → Best Answer）和 SC 下路径（Majority Vote → Most Frequent Answer），用背景色带、颜色编码和虚线框区分两条路径的复杂度差异。

---

# analysis exp 009 overhead

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-009-overhead_20260516T202925_result.json`
- **Structured JSON:** [`eb1ebac09d4b40e4a2e0.json`](../../sessions/eb/eb1ebac09d4b40e4a2e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结论：

**SICA pipeline overhead = +94.8% wall time over SC baseline**

| 阶段 | 占比 | 特征 |
|------|------|------|
| Trace Generation (vLLM) | 51.3% | SC 也需要，不算 overhead |
| Constraint Extraction (LLM) | 47.0% | **主要 overhead 来源**，相当于又跑了一轮推理 |
| Dedup (embeddings) | 1.6% | 可忽略 |
| MaxSAT (Z3) | ~0% | 可忽略 |

以 +0.25pp accuracy gain（76.49% vs 76.24%）换取近 2x wall time，当前 ROI 不高。优化方向：extraction 阶段用更小模型或 pipeline 并行。

两份产出已注册：`overhead_analysis.json`（结构化数据）+ `overhead_report.md`（可读报告）。

---

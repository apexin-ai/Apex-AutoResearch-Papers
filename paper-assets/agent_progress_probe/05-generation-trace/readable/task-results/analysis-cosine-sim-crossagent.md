# analysis cosine sim crossagent

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cosine-sim-crossagent_20260515T025420_result.json`
- **Structured JSON:** [`19c5fcc40a777a8c442c.json`](../../sessions/19/19c5fcc40a777a8c442c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| Metric | All windows (N=143,057) | conf≥2 (N=43,366) |
|--------|------------------------|-------------------|
| **macro_F1** | **0.447** | **0.393** |
| accuracy | 0.486 | 0.419 |
| F1_progress | 0.594 | 0.519 |
| F1_stagnation | 0.300 | 0.268 |

**参数**: threshold=0.61, inverted=True (SWE-Agent val-tuned)

**为什么这么差**: OH 上 progress/stagnation 的 cosine similarity 均值几乎相同（0.6134 vs 0.6100），完全无区分力。即使 oracle threshold on OH 也只有 0.4932 macro_F1。

对比 SWE-Agent in-domain: 0.5606 → cross-agent 降至 0.447（all）/ 0.393（conf≥2）。

结果已保存至 `artifacts/cosine-sim-crossagent/results.json`，registry 已更新。

---

# analysis greedy f1 discrepancy

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_greedy_f1_discrepancy_20260515T132025_result.json`
- **Structured JSON:** [`6a039603f4ea5e3bcce5.json`](../../sessions/6a/6a039603f4ea5e3bcce5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。总结：

**根因：Micro vs Macro F1 聚合方式不同**
- Registry 的 0.6617 = **micro F1**（全局 TP/FP/FN 再算 F1，`compute_ner_f1`）
- 分析文件的 0.6182 = **macro F1**（per-instance F1 取均值，`np.mean(per_instance_f1s)`）
- 三个 seed 上 gap 一致 ~4.4pp，是系统性差异

**对 ρ 无影响** — ρ 始终基于 per-instance F1 计算，与聚合方式无关。不同文档间的 ρ 差异来自不同推理运行的 sample 差异。

**附加发现**：seed 456 v2 用了 `--subtask joint`，而 seed 42/123 v2 用了 `--subtask ner`，推理模式不一致（影响 <0.3pp）。

**建议**：selection 表格用 macro F1（分析脚本已正确），模型整体性能用 micro F1，同一表格内统一口径。报告已写入 artifacts。

---

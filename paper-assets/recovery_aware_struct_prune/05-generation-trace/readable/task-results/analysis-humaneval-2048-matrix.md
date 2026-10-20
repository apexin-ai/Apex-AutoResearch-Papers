# analysis humaneval 2048 matrix

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_humaneval_2048_matrix_20260517T190756_result.json`
- **Structured JSON:** [`8733446ef6aafdb437dd.json`](../../sessions/87/8733446ef6aafdb437dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册为 artifact (`art_20260517_79570d`)。

核心发现：
- **GRPO+RASP 14.63%** 是剪枝模型中最高，但与其他变体的差异在 N=164 下未达统计显著性
- 所有剪枝模型在 HumanEval 上 67-77% 相对下降（远超 GSM8K 的 25-35%），代码生成对结构容量更敏感
- **C1 需要修正**：GRPO 的优势是条件性的（仅在 RASP 上有效），不是纯独立主效应，而是交互效应
- **C3 得到支持**：GRPO+RASP 组合在两个 benchmark 上均为最优或并列最优

---

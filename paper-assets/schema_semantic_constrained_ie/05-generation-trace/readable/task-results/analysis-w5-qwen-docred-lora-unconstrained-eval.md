# analysis w5 qwen docred lora unconstrained eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w5_qwen_docred_lora_unconstrained_eval_20260516T015104_result.json`
- **Structured JSON:** [`577e535b56a7c5fc542a.json`](../../sessions/57/577e535b56a7c5fc542a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 实验结果摘要: w5_qwen_docred_lora_unconstrained_eval

### 关键指标

| 指标 | Qwen DocRED | Llama DocRED | Δ |
|------|------------|-------------|---|
| **E-F1** | 82.15% | 83.93% | -1.78 |
| **R-F1** | 40.86% | 43.72% | -2.86 |
| **DR_pct** | 0.76% | 0.49% | +0.27 |
| **ET_pct** | 0.00% | — | — |
| **RV_pct** | 0.27% | — | — |
| **parse_fail_rate** | 7.11% | — | — |

详细：E-P=85.44%, E-R=79.11%, R-P=36.41%, R-R=46.56%。共 18091 实体预测、15870 关系预测。

### 分析

1. **Qwen 略逊于 Llama**：R-F1 低约 3 个点（40.86 vs 43.72），E-F1 低约 1.8 个点。Qwen 在 DocRED 上的 fine-tuned 表现不如 Llama。

2. **DR > 0（0.76%）**：unconstrained 模式下存在 domain-range 违规（121 次/15870 关系），说明 constrained eval 有价值——constrained decoding 可以消除这些违规并可能提升 R-F1。

3. **parse_fail_rate 7.11%（71/998）**：较高，日志显示这些 FAIL 样本耗时 ~73s（超时）。Qwen 在某些长文档上生成超时，这拉低了整体指标（FAIL 样本的 entity/relation 全算 FN）。

4. **跨模型对比**：DocRED 上两个模型的 DR 都很低（<1%），而 SciERC 上 DR 更高（Qwen 1.95%, Llama 1.11%），说明 DocRED fine-tuning 更有效地学到了 schema 约束。

---

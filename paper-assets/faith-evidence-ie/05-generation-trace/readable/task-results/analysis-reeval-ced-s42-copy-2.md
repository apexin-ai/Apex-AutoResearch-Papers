# analysis reeval ced s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reeval_ced_s42_20260516T075842_result.json`
- **Structured JSON:** [`107382cfa8e533368b92.json`](../../sessions/10/107382cfa8e533368b92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## reeval_ced_s42 结果摘要

**状态**: 成功完成 (EXIT_CODE=0)

### 核心指标

| 指标 | 值 |
|------|------|
| **Rel F1** | 0.4517 |
| Rel Precision | 0.4657 |
| Rel Recall | 0.4385 |
| **Ign-F1** | 0.4423 |
| **Evi F1** | 0.8174 |
| Evi Precision | 0.8113 |
| Evi Recall | 0.8237 |
| **EDCR** | 0.6569 |
| Evi F1 (joint) | 0.3518 |

### 统计

- 文档数: 985，预测数: 15436
- 格式合规: 100%，字段合规: 77.6%
- 截断: 214/985
- 推理耗时: 10815s (~3h)

### 其他

- **W&B run ID**: 无
- **结论**: **success** — 评估正常完成，指标合理，可用于 paired t-test 对比。

Artifact 已注册: `art_20260516_a0bf21`

---

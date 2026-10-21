# ops check ckpt20 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_ckpt20_eval_20260514T221115_result.json`
- **Structured JSON:** [`666bf4c0b649a1bfa4ca.json`](../../sessions/66/666bf4c0b649a1bfa4ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结论：**negative，未通过 pass criteria**。

## 关键指标

| 指标 | 值 | 判定 |
|------|-----|------|
| **rel_f1** | **0.0077** | **远低于 0.30 阈值** |
| evi_f1 | 0.628 | 尚可 |
| edcr | 0.993 | 极高（99.3% 引用指向 distractor） |
| format_ok_rate | 0.991 | 正常 |

## 问题诊断

模型在 ckpt-20 发生了**灾难性遗忘**（catastrophic forgetting）：
- 预测数 14440 vs gold 12151，量级接近，但 TP 仅 102（命中率 < 1%）
- 关系抽取能力几乎完全丧失（precision/recall 均 < 1%）
- evidence 定位能力尚存（evi_precision=0.855），但 edcr=0.993 说明模型引用的几乎全是 distractor 句子
- 60% 的文档输出被截断（n_truncated=587/985），field_compliance_rate 仅 0.40

---

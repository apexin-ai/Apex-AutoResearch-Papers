# analysis fair subset reconciliation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fair_subset_reconciliation_20260518T133428_result.json`
- **Structured JSON:** [`dec93aa662d5ec4ba68a.json`](../../sessions/de/dec93aa662d5ec4ba68a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

memory.md 已更新。总结：

---

## 调查结论

### 根因
**F1 计算方法不一致**，不是子集定义不同。

- D083 / `fair_eval.py`：使用 **aggregate ign_f1**（标准 DocRED 指标）
- art_20260518_cc2048 crossover 表格：使用 **per-doc average F1**（每篇文档独立算 F1 再取平均）

两者都用 442 docs（trunc-only exclusion），但 per-doc avg F1 给每篇文档等权重，而 ign_f1 按三元组数加权（micro F1）。三元组多的文档受 evidence 帮助更大，所以 ign_f1 差距更大。

### 权威数字（论文使用）

| 指标 | 值 |
|---|---|
| 子集定义 | trunc-only exclusion（任一条件下截断即排除） |
| 文档数 | **442 / 985** (44.9%) |
| 1.7B WE Ign-F1 | 0.6319 |
| 1.7B NE Ign-F1 | 0.5704 |
| **1.7B residual evidence benefit** | **6.2pp** |
| 8B Qwen (615 docs) | ~0pp (-0.3pp) |
| 8B LLaMA (694 docs) | ~0pp (+0.3pp) |

### 需修正
- art_20260518_cc2048 Section 3.2/3.3 crossover 表格中的 per-doc F1 数字（4.9pp/0.0pp/+1.0pp）不应直接用于论文
- 论文中引用 fair subset 结果时统一使用 ign_f1：**442 docs, evidence helps 6.2pp at 1.7B, ~0pp at 8B**

---

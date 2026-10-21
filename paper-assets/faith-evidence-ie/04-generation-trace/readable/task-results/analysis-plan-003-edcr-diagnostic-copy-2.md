# analysis plan 003 edcr diagnostic

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_003_edcr_diagnostic_20260515T195224_result.json`
- **Structured JSON:** [`13f6ae7b9bf06a5cdd1d.json`](../../sessions/13/13f6ae7b9bf06a5cdd1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。诊断表覆盖 21 个方法变体，核心发现：

**EDCR 本质上是 FP 三元组检测器** — 90% 的 distractor citations 来自假阳性三元组，而非证据标注错误。

五个诊断模式：
- **正常改进**（RSFT/bf16 GRPO）：EDCR 降 5-10pp，rel_f1 升 4-8pp
- **灾难性遗忘**（QLoRA GRPO）：EDCR 爆到 0.85-0.99，即使 evi_f1 看起来正常（0.83），EDCR 也能检出
- **DPO 过拟合**：evi_f1 最高(0.84) 但 EDCR 反而高于 baseline → 条件 evi_f1 对 FP 膨胀视而不见
- **CED-reranker 最低 EDCR(0.6156)**：不是反直觉，而是直接用 CED 做选择所以机械性地淘汰了 FP 密集候选
- **不可约 EDCR 下限 ~0.52**（oracle 选择仍有 52% distractor rate），说明数据集标注与证据生成策略存在结构性不匹配

文件：`artifacts/edcr_diagnostic_table.md`，已注册为 `art_20260515_8b91f9`。

---

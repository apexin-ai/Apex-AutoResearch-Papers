# knowledge topk ablation framing

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_topk_ablation_framing_20260516T003141_result.json`
- **Structured JSON:** [`ca067c8f289f24709bf8.json`](../../sessions/ca/ca067c8f289f24709bf8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。改动点：

**Claim 3 新增 top_k selection ablation 子节**：
- k=1 (3 seeds 均值) vs k=3 (1 seed) 完整 metrics 对比
- k=3 在所有指标上劣于 k=1 均值：Ign-F1 -1.36pp, rel_f1 -1.42pp, evi_f1 -0.55pp
- 训练数据质量溯源：k=3 的 mean_f1 从 0.6157 降至 0.5761，mean_ced 从 0.6683 降至 0.6205（数据量 ×2.96 但质量下降抵消数量优势）
- 叙事定位：CED scoring precision 随 k 增大下降，关键在 scoring precision 而非数据量
- 诚实标注 k=3 仅 1 seed，定位为 ablation table 辅助行

**MVP Evidence Summary 表**新增 `RSFT CED k=3` 行（Ign-F1=43.64, F1=44.54, Evi-F1=80.88, EDCR=0.6635），附注标明数据来源。

experiment_plan.yaml 不在可写文件白名单中，无法更新。

---

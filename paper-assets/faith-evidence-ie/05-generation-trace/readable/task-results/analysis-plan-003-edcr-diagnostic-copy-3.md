# analysis plan 003 edcr diagnostic

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_003_edcr_diagnostic_20260515T213848_result.json`
- **Structured JSON:** [`14b4ffc6f90498695b03.json`](../../sessions/14/14b4ffc6f90498695b03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已生成并注册 (`art_20260515_127ebc`)。

核心结论：

- **11 种 evidence-producing 方法**中，EDCR 与 rel_f1 单调负相关，从 CED-reranker (0.6156 / 0.4864) 到 DPO-CED 1ep (0.9982 / 0.0022)
- **EDCR > 0.95** 准确标识所有 catastrophic failure（DPO 1ep, GRPO QLoRA 早期 checkpoints），而 evi_f1 无法区分
- **5 个诊断 zone** 定义完毕：>0.95 catastrophic → 0.80-0.95 severe → 0.70-0.80 baseline → 0.63-0.67 improved → <0.63 best
- SFT-no-evidence (rel_f1=0.4893, EDCR=0) 作为反面验证：CED-reranker 在保留 evidence 前提下逼近无 evidence 的 rel_f1 上限（0.4864 vs 0.4893, gap 0.29pp）

---

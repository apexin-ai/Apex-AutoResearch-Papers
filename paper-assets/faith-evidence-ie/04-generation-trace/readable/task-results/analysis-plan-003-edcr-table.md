# analysis plan 003 edcr table

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_003_edcr_table_20260515T182133_result.json`
- **Structured JSON:** [`6768a9b3d72da1c7a37a.json`](../../sessions/67/6768a9b3d72da1c7a37a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。核心结论：

**EDCR 排名**（lower = better）：CED-reranker (0.6156) > bf16 GRPO (0.6318) > RSFT-CED 3-seed (0.6434) ≈ RSFT-flatNLI (0.6431) >> SFT baseline (0.7118) >> QLoRA GRPO catastrophic (0.8584)

**三个关键发现**：
1. **EDCR 与 rel_f1 强负相关**——所有 CED-trained 方法一致降低 EDCR 5.5-9.6pp，且改善在 3 seed 间稳定（std=0.011）
2. **EDCR 捕捉 evi_f1 之外的信息**——CED-reranker 和 RSFT s42 的 evi_f1 几乎相同（0.8188 vs 0.8187），但 EDCR 差 4.09pp
3. **EDCR 对 catastrophic forgetting 有诊断价值**——QLoRA GRPO 的 EDCR 恶化到 0.8584，可作为训练健康度预警指标

DPO+CED 和 SFT-no-evidence 的 eval 结果待出，表中标记为 pending。

---

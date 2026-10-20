# analysis plan 003 edcr diagnostic

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_003_edcr_diagnostic_20260515T180758_result.json`
- **Structured JSON:** [`87d3c748821df0e672e9.json`](../../sessions/87/87d3c748821df0e672e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个产出已生成并注册：

**edcr_diagnostic_table.md** — 8 个方法的完整指标表（按 rel_f1 降序），附 RSFT 3-seed 汇总和 GRPO checkpoint 轨迹。DPO 和 SFT-no-evidence 标注为 pending。

**edcr_analysis.md** — 核心发现：
- **EDCR 悖论**：rel_f1 与 EDCR 强负相关（Spearman ρ = −0.905），本质是 prediction count 驱动的 quality-quantity trade-off
- **三个机制区间**：under-prediction（QLoRA GRPO, 高 EDCR 但 catastrophic）、calibrated（SFT baseline）、over-prediction（RSFT/CED reranker, 低 EDCR 但高 F1）
- **EDCR 独特诊断价值**：evi_f1 衡量 evidence 是否被 recall，EDCR 衡量 evidence 是否被正确 *配对* 到对应 relation
- **GRPO checkpoint 动态**：ckpt-90 → ckpt-100 出现 Pareto 退化（rel_f1 微升但 EDCR 下降），可指导 early stopping
- **5 条 paper-ready claims**，含应披露的 limitation

---

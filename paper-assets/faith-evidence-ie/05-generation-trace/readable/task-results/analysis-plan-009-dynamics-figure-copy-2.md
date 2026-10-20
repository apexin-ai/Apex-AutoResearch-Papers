# analysis plan 009 dynamics figure

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_009_dynamics_figure_20260515T231309_result.json`
- **Structured JSON:** [`77e85a53390b0e214b73.json`](../../sessions/77/77e85a53390b0e214b73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**已完成的操作：**
1. **发现 bf16 G=8 缺失数据**：v5 图只有 steps 80/90/100 的 eval 数据，plan_011_bf16_g8_step_eval 中的 step 30/50/70 数据未纳入
2. **生成 v6 figure**：bf16 G=8 从 3 个 eval 点扩展到 6 个（steps 30/50/70/80/90/100），清晰展示 rel_f1 全程维持在 0.43-0.45（始终高于 SFT baseline 0.406），强化"bf16 无 forgetting"论证
3. **更新数据文件**：CSV 和 JSON 均补入 step 30/50/70 数据及来源标注
4. **更新 experiment_plan.yaml**：plan_009 的 `registry_id` 从 `null` 更新为 `plan_009_forgetting_figure`
5. **注册 artifact**：`art_20260515_f6a9d2`，关联 plan_009_forgetting_figure

---

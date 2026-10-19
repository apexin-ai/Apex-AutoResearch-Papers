# research paper outline prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-outline-prep_20260515T132442_result.json`
- **Structured JSON:** [`9f3fa627295b97e45f14.json`](../../sessions/9f/9f3fa627295b97e45f14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `writing_plan.yaml`。核心结构：

**Title**: "Sample, Select, Correct: Observation-Conditioned Residual Refinement for Robust VLA Control"（首选）

**Narrative 主线**: obs_only CRM 在 object perturbation 上 +8pp over argmin selection；per-DOF conformal features 作为 headline negative result 诚实报告。

**7 个 figure**:
- P0: pipeline overview、object benchmark bar chart、magnitude sweep curve、4-way ablation
- P1: per-task heatmap、statistical significance CI
- P2: task difficulty vs CRM improvement scatter

**写作顺序**: experiments → method → intro → related work → abstract → discussion → polish，abstract DDL 5/26 前完成前 5 步。

**关键 blocker**: object T5-T9 eval 和 seed=43 doubling 数据。没有这些数据，fig2/fig5/table1 无法锁定，abstract 无法定稿。

**5 个文献缺口**: supervised（非 RL）residual correction、uncertainty-conditioned negative results 先例、object vs spatial robustness 分类学、compounding error、CP-as-feature-extractor 先例。

---

# research next batch planning

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_next-batch-planning_20260513T232133_result.json`
- **Structured JSON:** [`9b5d698282de722e0e8a.json`](../../sessions/9b/9b5d698282de722e0e8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 下一批实验计划总结

### 当前批次覆盖了什么
- plan_000 MVP ✅, plan_001 CRM训练 ✅ + spatial eval ✅ (running), plan_002 A3训练 (running), plan_014 ReconVLA spatial (running)
- **缺口**: A3 eval、object benchmark 的 ACR-VLA/ReconVLA eval、A4 scalar ablation、K sensitivity

### 无论结果如何，第一优先级（Wave 1, 4 GPU 并行, ~3h）

| # | exp_id | 内容 | GPU |
|---|--------|------|-----|
| 1 | **eval-a3-obs-only-spatial** ⭐ | A3 obs_only checkpoint 跑 spatial eval — make-or-break for Claim 1 | cuda:0 |
| 2 | eval-acr-object-v1 | ACR-VLA on object (crm_best.pt 已有) | cuda:1 |
| 3 | eval-reconvla-object-v1 | ReconVLA on object | cuda:2 |
| 4 | crm-train-k5 → eval | K=5 CRM训练(cache已有) + spatial eval | cuda:3 |

### 若 Spatial Positive → Wave 2
- **plan_003 A4 scalar ablation** — 需要先实现 `--input_mode scalar`（代码改动）
- **plan_015 K=15/20** — precompute + train + eval（~15h GPU）
- **plan_005 COC validation** — 需要 eval 增加 COC logging
- **plan_004 SRPO stacking** — blocked on SRPO checkpoint

### 若 Spatial Negative → 诊断流程
- D1: 逐 task 分解（分析，无需 GPU）
- D2: CRM 残差幅度分析
- D4: CRM output scaling sweep (α ∈ {0.1, 0.3, 0.5, 0.7})
- D6: 验证 precompute 和 eval 的 conformal feature 一致性

关键判断点：**A3 obs_only eval 结果**。如果 obs_only ≈ full ACR-VLA（差距 <2%），Claim 1 不成立，需要 pivot feature engineering 或 reframe story。

完整计划已保存至 `artifacts/_project/report/next_batch_plan.md`。

---

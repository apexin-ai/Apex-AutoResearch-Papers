# analyze eval obs only spatial norm02 seed46 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-obs-only-spatial-norm02-seed46-r2_20260519T191804_result.json`
- **Structured JSON:** [`bd5e2712b3199f82ec9c.json`](../../sessions/bd/bd5e2712b3199f82ec9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成分析并更新 registry。

## 总结

### eval-obs-only-spatial-norm02-seed46-r2
- **SR = 33.0%** (33/100)，obs_only CRM, ε=0.2, K=10, LIBERO-Spatial
- 已有 Spatial K=10 obs_only 结果 35.0%±1.0% (n=3)，本次 33.0% 略低于均值但在 2σ 范围内，一致性良好
- 高分 task: next_to_ramekin (100%), between_plate_and_ramekin (90%), next_to_cookie_box (80%)
- 4 个 task SR=0%（table_center, ramekin, stove, wooden_cabinet）

### eval-obs-only-object-norm005-seed48
- **SR = 17.0%** (17/100)，obs_only CRM, ε=0.05, K=10, LIBERO-Object
- 补充 magnitude curve obs_only ε=0.05 数据点（现 n=6）
- 最高 30%（salad_dressing, bbq_sauce, chocolate_pudding, orange_juice），2 个 task 0%

---

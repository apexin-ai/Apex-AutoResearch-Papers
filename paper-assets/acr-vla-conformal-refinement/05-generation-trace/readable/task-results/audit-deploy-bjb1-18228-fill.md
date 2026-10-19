# audit deploy bjb1 18228 fill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit-deploy_bjb1-18228-fill_20260520T152913_result.json`
- **Structured JSON:** [`96a88b7244bf2b693350.json`](../../sessions/96/96a88b7244bf2b693350.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**审计结果** — bjb1-18228 全部 4 张 GPU 空闲，4 个已完成实验已更新 registry：

| 实验 | 成功率 | Registry |
|------|--------|----------|
| adaptive_k_spatial_p90_seed44 | 0.36 | 已 DONE |
| random_selection_spatial_seed42_r2 | 0.34 | 已 DONE |
| obs_only_spatial_seed48 | 0.35 | → DONE ✓ |
| vla_only_spatial_seed48 | 0.30 | → DONE ✓ |

**部署 4 个新实验** — 全部已启动并注册为 RUNNING：

| GPU | 实验 | Registry ID | PID |
|-----|------|-------------|-----|
| cuda:0 | K=20 obs_only object seed42 | eval-k20-obs-only-object-seed42 | 421434 |
| cuda:1 | random_selection object seed46 | eval-random-selection-object-seed46-r3 | 421636 |
| cuda:2 | random_selection object seed47 | eval-random-selection-object-seed47 | 421965 |
| cuda:3 | random_selection spatial seed43 | eval-random-selection-spatial-seed43-r2 | 422233 |

---

# mass deploy multi seed supplement

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_mass-deploy_multi-seed-supplement_20260520T104205_result.json`
- **Structured JSON:** [`b128ba2f43db333851df.json`](../../sessions/b1/b128ba2f43db333851df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

12/12 全部部署成功。汇总：

| # | Exp ID | Server | GPU | Benchmark | Mode | Seed |
|---|--------|--------|-----|-----------|------|------|
| 1 | eval-random-selection-spatial-seed42 | bjb1-18228 | cuda:0 | spatial | random_selection | 42 |
| 2 | eval-random-selection-spatial-seed43 | bjb1-18228 | cuda:1 | spatial | random_selection | 43 |
| 3 | eval-random-selection-spatial-seed44 | bjb1-18228 | cuda:2 | spatial | random_selection | 44 |
| 4 | eval-obs-only-goal-norm02-seed51 | bjb1-18228 | cuda:3 | goal | crm_obs_only | 51 |
| 5 | eval-obs-only-goal-norm02-seed52 | bjb1-32546 | cuda:0 | goal | crm_obs_only | 52 |
| 6 | eval-obs-only-object-norm02-seed43-r3 | bjb1-32546 | cuda:1 | object | crm_obs_only | 43 |
| 7 | eval-obs-only-object-norm02-seed49 | bjb1-32546 | cuda:3 | object | crm_obs_only | 49 |
| 8 | eval-argmin-object-seed48 | bjb1-32546 | cuda:4 | object | reconvla | 48 |
| 9 | eval-argmin-object-seed49 | bjb1-32546 | cuda:5 | object | reconvla | 49 |
| 10 | eval-obs-only-spatial-norm02-seed42 | bjb2-28827 | cuda:0 | spatial | crm_obs_only | 42 |
| 11 | eval-vla-only-goal-seed47 | bjb2-28827 | cuda:1 | goal | vla_only | 47 |
| 12 | eval-vla-only-spatial-seed48 | bjb2-28827 | cuda:2 | spatial | vla_only | 48 |

**优先级逻辑**：Spatial Random Selection（0 success）> Goal CRM（5）> Object CRM/Argmin/Spatial CRM（各6）> Goal/Spatial VLA-only（6-7）。所有 12 块空闲 GPU 已填满，timeout=12h。

---

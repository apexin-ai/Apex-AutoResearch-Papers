# harvest comprehensive sr na

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_comprehensive-sr-na_20260526T083351_result.json`
- **Structured JSON:** [`c20cbd2c663404fdd5bd.json`](../../sessions/c2/c20cbd2c663404fdd5bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个新实验已更新为 DONE/success。

=== HARVEST REPORT ===

### 已收割（新建 + metrics 更新）

| exp_id | SR | trigger_rate | source JSON |
|--------|-----|-------------|-------------|
| **eval-adaptive-object-s43-d149** | 77.5% | 3.7% | eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json |
| **eval-adaptive-object-s44-d149** | 75.0% | 3.6% | eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json |
| **eval-adaptive-goal-s43-d149** | 84.5% | 8.8% | eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json |
| **eval-adaptive-goal-s44-d149** | 86.5% | 6.8% | eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json |
| **eval-adaptive-spatial-s43-d149** | 79.5% | 20.3% | eval_spatial_adaptive_k2_tau025_seed43_paired_r2.json |
| **eval-adaptive-spatial-s44-d149** | 80.5% | 19.5% | eval_spatial_adaptive_k2_tau025_seed44_paired_r2.json |
| **eval-adaptive-spatial-k1-s42** | 79.5% | 19.8% | eval_spatial_adaptive_k2_tau025_seed42_paired_r2.json |
| **eval-supp-crm-norm005-obj-s44** | 74.0% | — | eval_object_crm_obs_only_norm0.05_seed44.json |

### 已有 SR（无需操作）

| exp_id | SR |
|--------|-----|
| eval-supp-obj-crm005-s42-r2 | 77.0% |
| eval-adaptive-object-s42-d149 | 81.0% |
| eval-adaptive-goal-s42-d149 | 83.5% |
| eval-adaptive-long-s42/s43/s44-d149 | 58.0%/58.0%/54.0% |
| eval-crm-long-s42/s43/s44-d149 | 56.5%/54.5%/55.5% |

### 3-seed 汇总

| Method | Benchmark | s42 | s43 | s44 | Mean±Std |
|--------|-----------|-----|-----|-----|----------|
| **Adaptive** | Object | 81.0 | 77.5 | 75.0 | **77.8±3.0** |
| **Adaptive** | Goal | 83.5 | 84.5 | 86.5 | **84.8±1.5** |
| **Adaptive** | Spatial | 79.5 | 79.5 | 80.5 | **79.8±0.6** |
| **Adaptive** | Long | 58.0 | 58.0 | 54.0 | **56.7±2.3** |
| **CRM** | Long | 56.5 | 54.5 | 55.5 | **55.5±1.0** |
| **CRM norm=0.05** | Object | 77.0 | — | 74.0 | 75.5±2.1 (2 seeds) |

### 注意

- `eval-supp-crm-norm005-obj-s44` 在 registry 中 conclusion=**negative**（非 success），metrics 已更新为 SR=0.74
- Object Adaptive s42 的 JSON (`eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json`) 在 bjb1-32546 上**不存在**——现有 registry 的 SR=0.81 可能来自另一台服务器
- Long 实验全部已有 SR，无需额外收割

---

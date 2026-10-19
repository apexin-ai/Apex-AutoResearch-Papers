# harvest bjb1 32546 smolvla complete

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb1-32546-smolvla-complete_20260526T064500_result.json`
- **Structured JSON:** [`d9bd9098f6c455285e81.json`](../../sessions/d9/d9bd9098f6c455285e81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 6 harvested. Compiling the final report.

## bjb1-32546 报告

### SmolVLA Harvest

| exp_id | SR | conclusion | registry 更新 |
|--------|-----|-----------|--------------|
| goal_adapt_s48 | 0.850 | success (Δ+5.5pp vs VLA-only s48) | DONE ✓ |
| goal_vla_only_s48 | 0.795 | success (baseline 数据点) | DONE ✓ |
| tau_sweep_goal_tau045_s42 | 0.835 | negative (Δ=0.0pp vs VLA-only s42=0.835) | DONE ✓ |
| tau_sweep_goal_tau040_s42 | 0.835 | negative (Δ=0.0pp) | DONE ✓ |
| tau_sweep_goal_tau025_s42 | 0.835 | negative (Δ=0.0pp) | DONE ✓ |
| tau_sweep_spatial_tau025_s42 | 0.785 | negative (Δ=0.0pp vs spatial VLA-only s42=0.785) | DONE ✓ |

**关键发现**：goal s42 上三个 τ 值（0.25/0.40/0.45）全部得到 SR=0.835，等于 VLA-only baseline → τ 参数在 seed 42 上无差异化效果（推测 gating 几乎不触发，或修正在该 seed 上不改变成功 task 集合）。但 seed 48 的 adaptive_conformal_crm 比 VLA-only +5.5pp，说明效果有 seed 依赖性。

### π0.5 CRM 状态（全部 RUNNING）

启动 13:43（goal）/ 13:46（object），现在每个进程已完成 2/10 个 task（第 3 个 task rollout 5/20）。每 task ≈ 30 min，预计总时长 ≈ 5h。

| GPU | exp_id | 进度 | VRAM | 预计完成 |
|-----|--------|------|------|---------|
| 0 | pi05-crm-k2-goal-s42-bjb1 | task 2.25/10 (put_wine_bottle 5/20, 2 成功) | 13.1GB | ~18:45 |
| 1 | pi05-crm-k2-goal-s43-bjb1 | task 2.25/10 (put_wine_bottle 5/20, 4 成功) | 13.1GB | ~18:45 |
| 2 | pi05-crm-k2-goal-s44-bjb1 | task 2.25/10 (put_wine_bottle 5/20, 3 成功) | 13.1GB | ~18:45 |
| 3 | pi05-crm-k2-object-s42-bjb1 | task 2.25/10 (salad_dressing 5/20, 5 成功) | 13.2GB | ~18:50 |
| 4 | pi05-crm-k2-object-s43-bjb1 | task 2.0/10 (cream_cheese 完成 70%) | 13.2GB | ~18:50 |
| 5 | pi05-crm-k2-object-s44-bjb1 | task 2.25/10 (salad_dressing 5/20, 5 成功) | 13.2GB | ~18:50 |

### 已完成 π0.5（无新结果待 harvest）

bjb1-32546 上所有 6 个 π0.5 CRM 实验仍在跑，无新完成项。

注意：`logs/eval_spatial_crm_obs_only_norm0.05_seed44_pi05_K2.json`（SR=0.970, 05-26 05:17）是早于 bjb2 那批 pi05-crm-k2-spatial-s44-bjb2（05-26 05:53 创建）的旧结果文件，不属于本服务器当前 harvest 范围。

---

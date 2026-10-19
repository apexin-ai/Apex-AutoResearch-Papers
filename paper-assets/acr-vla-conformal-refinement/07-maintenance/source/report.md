# Handover — 2026-05-28

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无运行中实验 — 2026-05-28 全部实验已 kill/cancel）

## 待处理
（全部 179 项已取消 — 2026-05-28 用户指令全面停机）

## 近期结论
- **eval-supp-long-adapt-tau025-s44** (negative): Long Adaptive τ=0.25 s44, SR=56%, trigger=4.9%. Below VLA-only baseline (58%). Supplementary seed variance data — 数据已充足。
- **pi05-adaptive-goal-s44-backfill** (success): Pi05 Adaptive Conformal on Goal s44. Fills Table 2 gap (only s42/s43 exist). Cross-seed validation for Pi05 Goal adaptive.

## 趋势
成功 768 / 负向 97 / 失败 130 / 共 1230

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
bjb1-18228: 1× RTX 4090 空闲（配置说 4 卡但实测仅 1 卡）
bjb1-32546: ❌ 连接失败（port 32546 不可达，AutoDL 实例可能已关机/端口变更）
bjb2-28827: ❌ 连接失败（port 28827 不可达）
cqa1-32758: ❌ 连接失败（port 32758 不可达）

## 告警
- plan_001-crm-smolvla: 训练失败 — unknown
- plan_014-reconvla-baseline: 训练失败 — unknown
- eval-smolvla-libero-spatial: 训练失败 — unknown
- eval-spatial-reeval-v2: 已被终止 — unknown
- precompute-v2-shard0: 已被终止 — unknown
- precompute-v2-shard1: 已被终止 — unknown
- precompute-v2-shard2: 已被终止 — unknown
- eval-spatial-v3-full: 已被终止 — unknown
- precompute-v3-shard0: 已被终止 — unknown
- precompute-v3-shard1: 已被终止 — unknown
- precompute-v3-shard2: 已被终止 — unknown
- eval-spatial-v4-full: 已被终止 — unknown
- eval-object-v4-full: 已被终止 — unknown
- eval-spatial-v5-full: 已被终止 — unknown
- crm-train-v1: 已被终止 — unknown
- eval-reconvla-spatial-v1: 已被终止 — unknown
- eval-reconvla-spatial-v2: 已被终止 — unknown
- eval-acr-spatial-v1: 已被终止 — unknown
- crm-train-a3-obs-only: 已被终止 — unknown
- eval-acr-vla-spatial-v1: 已被终止 — unknown
- eval-spatial-v6-full: 已被终止 — unknown
- eval-acr-spatial-v2: 已被终止 — unknown
- eval-object-v5-full: 已被终止 — unknown
- eval-object-v6-full: 已被终止 — unknown
- crm-train-a4-scalar-unc: 已被终止 — unknown
- eval-scalar-unc-spatial: 已被终止 — unknown
- eval-object-v7-full: 已被终止 — unknown
- crm-train-k5: 已被终止 — unknown
- eval-k5-spatial: 已被终止 — unknown
- eval-scalar-unc-spatial-v2: 已被终止 — unknown
- eval-obs-only-spatial: 训练失败 — unknown
- eval-obs-only-spatial-v3: 已被终止 — unknown
- eval-argmin-only-spatial: 已被终止 — unknown
- eval-tiny-correction-spatial: 已被终止 — unknown
- crm-train-v3-perdof: 已被终止 — unknown
- crm-train-v3-scalar-unc: 已被终止 — unknown
- crm-train-v3-obs-only: 已被终止 — unknown
- eval-acr-spatial-v4-default: 训练失败 — unknown
- eval-acr-spatial-v4-small: 已被终止 — unknown
- eval-acr-spatial-v4-obs-only: 训练失败 — unknown
- eval-acr-spatial-v4-scalar: 已被终止 — unknown
- eval-acr-spatial-v4-obs-only-r2: 已被终止 — unknown
- eval-acr-spatial-v4-default-r2: 已被终止 — unknown
- eval-acr-spatial-v4-default-r3: 已被终止 — unknown
- eval-acr-object-v4-obs-only-b2: 已被终止 — unknown
- eval-acr-object-v4-scalar-b2: 已被终止 — unknown
- eval-mag-perdof-norm02: 已被终止 — unknown
- eval-vla-only-object-k1: 训练失败 — unknown
- eval-acr-object-v4-default: 已被终止 — unknown
- eval-mag-obsonly-norm003: 已被终止 — unknown
- eval-mag-obsonly-norm03: 已被终止 — unknown
- eval-mag-obsonly-norm03-b2: 训练失败 — unknown
- eval-mag-obsonly-norm-0.3-r3: 已被终止 — unknown
- eval-mag-obsonly-norm-0p3-r3: 已被终止 — unknown
- eval-obs-only-spatial-seed43: 训练失败 — unknown
- eval-obs-only-object-norm02-seed43: 训练失败 — unknown
- eval-mag-perdof-norm0p3-object: 已被终止 — unknown
- eval-mag-perdof-norm0p3-object-r2: 已被终止 — unknown
- eval-mag-obsonly-norm03-b3: 已被终止 — unknown
- eval-mag-obsonly-norm03-b4: 已被终止 — unknown
- eval-mag-perdof-norm03-object-r2: 已被终止 — unknown
- eval-mag-perdof-norm02-seed43-object: 已被终止 — unknown
- eval-mag-perdof-norm02-seed43-object-r2: 已被终止 — unknown
- eval-mag-obsonly-norm02-object: 已被终止 — unknown
- eval-argmin-object-seed44: 训练失败 — unknown
- eval-obs-only-object-norm02-seed44: 训练失败 — unknown
- eval-vla-only-object-seed44: 训练失败 — unknown
- eval-argmin-object-seed44-r3: 已被终止 — unknown
- eval-obs-only-object-norm02-seed44-r3: 已被终止 — unknown
- eval-scalar-object-seed44: 训练失败 — unknown
- eval-obs-only-object-norm03-seed45: 训练失败 — unknown
- eval-obs-only-object-norm02-seed44-r4: 已被终止 — unknown
- eval-direct-correction-object-seed42: 训练失败 — unknown
- eval-direct-correction-object-seed42-r2: 训练失败 — unknown
- eval-obs-only-object-norm01-seed46: 训练失败 — unknown
- eval-perdof-object-norm01-seed47: 已被终止 — unknown
- eval-obs-only-object-norm01-seed47-r2: 已被终止 — unknown
- eval-obs-only-object-norm01-seed47-bjb2: 已被终止 — unknown
- eval-obs-only-object-norm01-seed46-bjb2: 已被终止 — unknown
- eval-obs-only-object-norm03-seed47: 训练失败 — unknown
- eval-perdof-object-norm03-seed46-r2: 已被终止 — unknown
- eval-perdof-object-norm02-seed45-r2: 已被终止 — unknown
- eval-perdof-object-norm02-seed45-deploy: 已被终止 — unknown
- eval-obs-only-object-norm005-seed43-r3: 已被终止 — unknown
- eval-obs-only-object-norm02-k20-seed42: 已被终止 — unknown
- train-crm-k1-accg-object-seed42: 训练失败 — unknown
- mag_obs_only_norm01_seed47: 已被终止 — unknown
- mag_obs_only_norm01_seed46: 已被终止 — unknown
- mag_perdof_norm02_seed43_r3: 已被终止 — unknown
- eval-obs-only-object-norm02-seed48: 已被终止 — unknown
- eval-obs-only-object-norm01-seed42-r2: 训练失败 — unknown
- eval-perdof-object-norm01-seed42-r2: 训练失败 — unknown
- eval-perdof-object-norm003-seed44-r2: 训练失败 — unknown
- eval-perdof-object-norm003-seed45: 已被终止 — unknown
- eval-perdof-object-norm005-seed45: 训练失败 — unknown
- eval-random-selection-object-seed46: 训练失败 — unknown
- eval-obs-only-object-norm005-seed46: 已被终止 — unknown
- eval-obs-only-object-norm003-seed47: 已被终止 — unknown
- eval-perdof-object-norm03-seed48: 已被终止 — unknown
- eval-obs-only-object-norm003-seed49: 已被终止 — unknown
- eval-random-selection-object-seed46-r2: 训练失败 — unknown
- eval-obs-only-object-norm003-seed45-r2: 已被终止 — unknown
- eval-obs-only-spatial-norm02-seed43: 训练失败 — unknown
- eval-lto-splitA-heldout: 已被终止 — unknown
- eval-lto-splitA-vla-only: 已被终止 — unknown
- eval-argmin-object-k5-seed44: 训练失败 — unknown
- eval-random-selection-object-k5-seed42: 训练失败 — unknown
- eval-random-selection-object-k5-seed43: 训练失败 — unknown
- eval-random-selection-object-k5-seed44: 训练失败 — unknown
- eval-random-selection-object-k5-seed45: 训练失败 — unknown
- eval-obs-only-spatial-norm02-k5-seed44: 训练失败 — unknown
- eval-obs-only-spatial-norm02-k5-seed45: 训练失败 — unknown
- eval-obs-only-object-norm02-k20-seed43: 已被终止 — unknown
- eval-obs-only-object-norm02-k20-seed44: 已被终止 — unknown
- eval-obs-only-spatial-norm02-seed46: 训练失败 — unknown
- eval-vla-only-goal-seed44: 已被终止 — unknown
- eval-openvla-object-baseline-seed42: 已被终止 — unknown
- eval-crm-goal-seed44: 训练失败 — unknown
- eval-crm-goal-seed45: 训练失败 — unknown
<!-- 已截断：超过 150 行限制，已执行 Pre-compaction Flush -->

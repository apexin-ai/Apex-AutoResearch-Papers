# Handover — 2026-05-15

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- phase1_delta_progress（准备中）
- phase1_iql_vip_scaled: Reward scaling (×100) on MLP progress reward fixes IQL advantage collapse, producing AUROC > RINSE TED for no-op/progress separation（准备中）
- phase0_feature_val: 冻结 VLA 中间层特征的 cos_sim(s_t, s_goal) 与 progress t/T 有强单调关系（Spearman ρ > 0.8），可作为 IQL reward signal（准备中）

## 近期结论
- **phase1_iql_vip** (negative): IQL trained on VIP MLP progress reward can compute per-timestep advantage that effectively separates no-op vs progress timesteps (AUROC > RINSE SAL/TED) ← 基于 phase0_feature_val

## 趋势
成功 0 / 负向 1 / 失败 0 / 共 1

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-34887: 无 GPU 信息

## 告警
（无）

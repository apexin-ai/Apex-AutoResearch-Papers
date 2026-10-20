# Handover — 2026-05-13

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- mvp_eval_01: TurnKV role-aware segment budgets preserve task-critical information better than uniform EA at same compression ratio (70%/85%), with KIRR diff ≥10pp and PPL ratio ≤1.02（准备中）

## 近期结论
- **mvp_v3_cr85** (failed): D007 additive bias: TurnKV (ea + α×offset, α=0.1) KIRR - Uniform EA KIRR ≥ 10pp at CR=0.85, PPL ≤ 1.02×, with fixed traces (full KIRR=99.6%) ← 基于 mvp_eval_02_cr85
- **mvp_v3_cr70** (failed): D007 additive bias: TurnKV (ea + α×offset, α=0.1) KIRR - Uniform EA KIRR ≥ 10pp at CR=0.7, PPL ≤ 1.02×, with fixed traces (full KIRR=99.6%) ← 基于 mvp_eval_02_cr70
- **mvp_v3b_cr70** (negative): D007 additive bias with agent traces: TurnKV (ea + α×offset, α=0.1) KIRR - Uniform EA KIRR ≥ 10pp at CR=0.7, PPL ≤ 1.02×. Agent traces with ipython/think roles (65 traces, full KIRR=100%) ← 基于 mvp_v3_cr70

## 趋势
成功 1 / 负向 6 / 失败 2 / 共 9

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-16980: 无 GPU 信息

## 告警
- mvp_v3_cr70: 训练失败 — unknown
- mvp_v3_cr85: 训练失败 — unknown

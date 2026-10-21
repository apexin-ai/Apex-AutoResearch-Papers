# Handover — 2026-05-25

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- exp-004: 简单 baseline（CyclicJudge, DCR Factor, Preference Leakage, UDA）只做 judge rotation 或 contamination discounting，无法改变模型排名；只有 G-MFRM joint 建模 contamination × model 交互才能提升 Arena correlation τ。（已分配 ? GPU:?，等待提交）

## 近期结论
- **exp-020** (negative): N=17 target models (vs N=8) with 7 diverse judges provides sufficient statistical power for G-MFRM joint estimation to achieve significant Δτ over baselines, confirming that exp-018 synthetic calibration results translate to real data. ← 基于 exp-018
- **exp-017** (success): Murphy-Topel 渐近校正在 N=8 下 CI coverage 显著低于 95% nominal（与论文报告的 71% 一致），随 N 增大（20, 50, 100）coverage 逐渐趋近 95%，确认 71% 是 small-sample asymptotic breakdown 而非方法缺陷。 ← 基于 exp-009
- **exp-018** (success): Scaling synthetic calibration from N=8 to N=20 models will yield statistically significant Δτ (theta_tau improvement) for joint G-MFRM over sequential MFRM, confirming that exp-015's non-significance was a power issue due to small N.

## 趋势
成功 15 / 负向 4 / 失败 1 / 共 21

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
autodl-8gpu: 空闲 cuda:0, cuda:1, cuda:2, cuda:3

## 告警
- exp-014: 训练失败 — unknown
- exp-016: 已被终止 — unknown

# Handover — 2026-05-16

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
| exp_id | 假设 | 状态 | 关键指标 | W&B |
|--------|------|------|---------|-----|
| mvp_strong_model_disambig | D018 强模型消歧：用 Claude Sonnet 4 重跑 14 Tier 1 实例 × 4 条件，验证 trace 正向信号是否在强模型上放大。如果强模型 structural > no_trace 且 test_pass > 0，说明 v2 negative 是模型能力问题而非 trace 无用。 | — | — | — |

## 待处理
- mvp_structural_scoring_v2: [CANCELLED by D013] 原计划用修复后代码重跑 structural scoring，但发现 Phase 1 trace 收集 bug（未用 failing test），需先修复 trace 再重新 scoring（准备中）

## 近期结论
- **mvp_phase3_repair_v2** (failed): Pipeline 修复后（正确 buggy_code + diff 输出 + max_tokens=8192），在 Tier 1 clean subset（14 实例）上验证 structural_filtered trace 是否优于 no_trace，用 test execution 作为主评估指标 ← 基于 mvp_phase3_repair
  [mvp_phase3_repair_v2_analysis](/api/workspace-files/projects/trace_distill_repair/artifacts/mvp_phase3_repair_v2/report/mvp_phase3_repair_v2_analysis.md)
- **mvp_phase3_repair** (negative): Structural-filtered trace 在 repair quality 上优于 line-filtered、full_trace（naive 16K truncation）和 no_trace，尤其在 structural keep>0 的 15 个实例子集上 ← 基于 mvp_line_scoring_v3
- **mvp_line_scoring_v5** (killed): —

## 趋势
成功 7 / 负向 1 / 失败 4 / 共 16

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
rtx6000-diagprobe: 空闲 cuda:0, cuda:1

## 告警
- mvp_teacher_scoring: 训练失败 — unknown
- mvp_line_scoring_rerun: 训练失败 — unknown
- mvp_line_scoring_rerun_v2: 已被终止 — unknown
- mvp_line_scoring_sampled: 训练失败 — unknown
- mvp_line_scoring_sampled_final: 已被终止 — unknown
- mvp_line_scoring_v4: 已被终止 — unknown
- mvp_line_scoring_v5: 已被终止 — unknown
- mvp_phase3_repair_v2: 训练失败 — unknown

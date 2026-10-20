# Handover — 2026-05-14

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
| exp_id | 假设 | 状态 | 关键指标 | W&B |
|--------|------|------|---------|-----|
| mvp_pipeline_004 | v4 truncation detection + thinking-off retry, 204 samples | RUNNING (PID 47964, 127/204, ETA ~08:30 BJT) | All-mode 5/5 PASS @126样本 | — |

## 126 样本 C1-C5 指标（evaluate_mvp.py 权威数据）
| 指标 | All-mode (N=117) | 阈值 | 状态 | Excl-Unknown (N=75) | 状态 |
|------|-----------------|------|------|-------------------|------|
| C1 disagree_rate | 35.9% (42/117) | ≥10% | PASS | 34.7% (26/75) | PASS |
| C2 diagnostic_rate | 88.1% (37/42) | ≥40% | PASS | 88.5% (23/26) | PASS |
| C3 error_types | 3 | ≥2 | PASS | 2 | PASS |
| C4 targeted_delta | +7.4pp (T:35/54 B:31/54) | >5pp | PASS | +0.0pp (T:22/35 B:22/35) | FAIL |
| C5 localization | 79.2% (19/24) | ≥60% | PASS | 87.5% (14/16) | PASS |

## 已完成修复
- repair.py: repr_type 动态 prompt（C4 excl-unknown 根因修复）
- pipeline.py: streaming JSONL + gc.collect（内存泄漏修复）
- pipeline.py: JSON→JSONL in-place 转换（数据损坏 bug 修复）
- repair_only.py: repair-only 重跑脚本就绪

## 待处理
- 等 204 全量完成 → evaluate_mvp.py 最终评估
- 204 完成后 → repair_only.py 重跑 repair+eval（用修复后的 prompt）

## 近期结论
- **mvp_pipeline_004** (success, 127/204): All-mode 5/5 PASS，C4 趋势下滑需关注
- **mvp_pipeline_002** (negative): FOL crash 修复但 C4/C5 仍 FAIL
- **mvp_pipeline_001** (negative): 首轮 2/5 PASS

## 趋势
成功 1 / 负向 2 / 失败 0 / 终止 2 / 共 6
MVP 指标持续改善: v1(2/5) → v2(2/5) → v4@80(4/5) → v4@126(5/5 all-mode)

## 资源状态
autodl-rtx6000pro: cuda:0 pipeline (PID 47964) + vLLM serving 运行中

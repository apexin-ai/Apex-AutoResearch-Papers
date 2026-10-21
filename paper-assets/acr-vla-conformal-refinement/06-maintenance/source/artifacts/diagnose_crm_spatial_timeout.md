# 诊断：π0.5 CRM Spatial Eval 超时失败

**日期**: 2026-05-22
**实验**: eval-pi05-crm-spatial-seed{42,43,44}
**服务器**: bjb2-28827
**配置**: mode=acr_vla, model=pi05, n_action_steps=50, max_steps=300, K=10, conformal_threshold=0.074855

## 1. 失败原因判定：纯超时，无 error/hang

三个实验均正常运行，无任何 error、exception 或 hang 迹象。日志显示 episode 在稳定推进，直到被 timeout (EXIT_CODE=124) 强制终止。没有输出 JSON 文件（进程被杀时尚未写入结果）。

**根因**: 单 episode 耗时 ~307-331 秒，200 episodes 需要 ~17 小时，但 timeout 仅设 ~12 小时。

## 2. 每个 seed 的完成进度

| Seed | 完成 tasks | 完成 episodes | 总需 episodes | 进度 |
|------|-----------|--------------|--------------|------|
| 42   | 7/10      | 140/200      | 200          | 70%  |
| 43   | 7/10      | 140/200      | 200          | 70%  |
| 44   | 6+½/10    | 130/200      | 200          | 65%  |

**每 episode 平均耗时**:
- Seed 42 & 43: ~43000s / 140 eps ≈ **307 sec/ep**
- Seed 44: ~43000s / 130 eps ≈ **331 sec/ep**
- 平均 ~310 sec/ep → 200 eps 需要 ~62,000s ≈ **17.2 小时**

## 3. 已完成 episodes 的部分结果

### Seed 42 (7 tasks, 140 eps) — 部分平均 90.0%

| Task | Success | Rate |
|------|---------|------|
| between_plate_and_ramekin | 18/20 | 90% |
| next_to_ramekin | 19/20 | 95% |
| from_table_center | 20/20 | 100% |
| on_cookie_box | 20/20 | 100% |
| in_top_drawer | 19/20 | 95% |
| on_ramekin | 10/20 | **50%** |
| next_to_cookie_box | 20/20 | 100% |

### Seed 43 (7 tasks, 140 eps) — 部分平均 85.7%

| Task | Success | Rate |
|------|---------|------|
| between_plate_and_ramekin | 17/20 | 85% |
| next_to_ramekin | 19/20 | 95% |
| from_table_center | 19/20 | 95% |
| on_cookie_box | 18/20 | 90% |
| in_top_drawer | 18/20 | 90% |
| on_ramekin | 9/20 | **45%** |
| next_to_cookie_box | 20/20 | 100% |

### Seed 44 (6 full + 1 partial task, 130 eps) — 部分平均 82.3%

| Task | Success | Rate |
|------|---------|------|
| between_plate_and_ramekin | 17/20 | 85% |
| next_to_ramekin | 18/20 | 90% |
| from_table_center | 19/20 | 95% |
| on_cookie_box | 18/20 | 90% |
| in_top_drawer | 19/20 | 95% |
| on_ramekin | 6/20 | **30%** |
| next_to_cookie_box | 10/10 (incomplete) | 100% so far |

### 跨 Seed 汇总 (7 个共同完成的 task)

| Task | Seed42 | Seed43 | Seed44 | Mean |
|------|--------|--------|--------|------|
| between_plate_and_ramekin | 90% | 85% | 85% | 86.7% |
| next_to_ramekin | 95% | 95% | 90% | 93.3% |
| from_table_center | 100% | 95% | 95% | 96.7% |
| on_cookie_box | 100% | 90% | 90% | 93.3% |
| in_top_drawer | 95% | 90% | 95% | 93.3% |
| on_ramekin | **50%** | **45%** | **30%** | **41.7%** |
| next_to_cookie_box | 100% | 100% | — | 100% |

**Notable**: `on_ramekin` task 显著低于其他 task（41.7% vs 93%+），可能是 CRM 对该场景的 conformal set 校准不佳，或 PI05 base 在该 task 上本身表现差。

## 4. 缺失的 3 个 task

Task order [0..9] 中的 task 7, 8, 9 从未开始执行。需要对照 LIBERO spatial 的完整 task 列表确认具体是哪三个 task。

## 5. 建议

### 方案 A: 增加 timeout（推荐）
- 将 timeout 从 ~12h 增至 **20h (72000s)**，足够覆盖 200 episodes × 330 sec/ep
- 不改 n_action_steps=50，保持当前推理速度
- 重跑三个 seed

### 方案 B: 用已有部分结果
- 7/10 tasks 的结果已经比较稳定（3 seeds 一致性好），可以先用 partial results 做初步分析
- 但缺 3 个 task 的数据，无法报告完整的 10-task average

### 不推荐：改 n_action_steps=10
- n_action_steps=50→10 意味着每 episode 从 6 次 VLA forward pass 增至 30 次，**每 episode 耗时约 5x**
- 这会使总时间从 17h 增至 ~85h，完全不可行
- 若需要改为官方 n_action_steps=10，必须同时减少 max_steps 或接受更长运行时间

# SmolVLA CRM Eval Results Harvest

**时间**: 2026-05-23 ~08:45 UTC
**状态**: 所有 eval 仍在运行中，预计 1-1.5h 后完成

## 问题记录

**bjb2-28827 Spatial CRM eval 全部失败**: 启动命令包含 `--input_mode obs_only`，该参数不存在，导致 3 个 seed 的 CRM spatial eval 全部崩溃。VLA-only spatial 作为链式后续命令正常执行（因 `| tee` 管道掩盖了非零退出码）。

Spatial CRM 数据改从 bjb1-32546 收集（无 --input_mode 参数，正确运行）。

## 当前进度快照

### Object CRM (bjb2-28827, cuda:0,1,2) — 约 5/10 tasks

| Task | Seed42 | Seed43 | Seed44 |
|------|--------|--------|--------|
| alphabet_soup | 70.0% (14/20) | 70.0% (14/20) | 70.0% (14/20) |
| cream_cheese | 50.0% (10/20) | 50.0% (10/20) | 70.0% (14/20) |
| salad_dressing | 50.0% (10/20) | 50.0% (10/20) | 45.0% (9/20) |
| bbq_sauce | 30.0% (6/20) | 35.0% (7/20) | 35.0% (7/20) |
| ketchup | running (~5/10) | running (~3/5) | running (~4/10) |
| tasks 6-10 | pending | pending | pending |

Partial avg (4 tasks): s42=50.0%, s43=51.25%, s44=55.0%

### Spatial CRM (bjb1-32546, cuda:0,1,2) — 约 5-6/10 tasks

| Task | Seed42 | Seed43 | Seed44 |
|------|--------|--------|--------|
| between_plate_ramekin | 80.0% (16/20) | 85.0% (17/20) | 75.0% (15/20) |
| next_to_ramekin | 75.0% (15/20) | 75.0% (15/20) | 75.0% (15/20) |
| from_table_center | 75.0% (15/20) | 80.0% (16/20) | 80.0% (16/20) |
| on_cookie_box | 55.0% (11/20) | 80.0% (16/20) | 80.0% (16/20) |
| in_top_drawer | 55.0% (11/20) | 55.0% (11/20) | 50.0% (10/20) |
| on_ramekin | pending | pending | running (0/5) |
| tasks 7-10 | pending | pending | pending |

Partial avg (5 tasks): s42=68.0%, s43=75.0%, s44=72.0%

### Spatial VLA-only (bjb2-28827, cuda:3,4,5) — 约 6/10 tasks

| Task | Seed42 | Seed43 | Seed44 |
|------|--------|--------|--------|
| between_plate_ramekin | 90.0% (18/20) | 100.0% (20/20) | 90.0% (18/20) |
| next_to_ramekin | 95.0% (19/20) | 95.0% (19/20) | 95.0% (19/20) |
| from_table_center | 95.0% (19/20) | 95.0% (19/20) | 100.0% (20/20) |
| on_cookie_box | 95.0% (19/20) | 90.0% (18/20) | 95.0% (19/20) |
| in_top_drawer | 70.0% (14/20) | 75.0% (15/20) | 80.0% (16/20) |
| on_ramekin | 0.0% (0/20) | 0.0% (0/20) | 0.0% (0/20) |
| tasks 7-10 | pending | pending | running (next_to_cookie_box 5/5) |

Partial avg (6 tasks): s42=74.2%, s43=75.8%, s44=76.7%

### Goal CRM (bjb1-32546, cuda:4,5) — 约 4-5/10 tasks

| Task | Seed42 | Seed43 |
|------|--------|--------|
| open_middle_drawer | 60.0% (12/20) | 70.0% (14/20) |
| bowl_on_stove | 85.0% (17/20) | 85.0% (17/20) |
| wine_bottle_on_cabinet | 60.0% (12/20) | 55.0% (11/20) |
| open_top_drawer_bowl_inside | 15.0% (3/20) | 15.0% (3/20) |
| bowl_on_top_cabinet | running (4/5) | running (9/10) |
| tasks 6-10 | pending | pending |

Partial avg (4 tasks): s42=55.0%, s43=56.25%

## 初步趋势（部分数据，仅供参考）

| Suite | CRM partial avg | VLA-only baseline | 趋势 |
|-------|----------------|-------------------|------|
| Object | ~52% (4/10 tasks) | 66.0%±0.9% | CRM 明显低于 baseline |
| Spatial | ~72% (5/10 tasks) | 58.0%±3.0%* | CRM 高于 lerobot baseline，但低于 wrapper VLA-only ~76% |
| Goal | ~56% (4/10 tasks) | 78.5%±3.3% | CRM 明显低于 baseline |

*注：58.0% 是 lerobot-eval baseline，不是 wrapper VLA-only。Wrapper VLA-only spatial 部分数据 ~75-77%。

## GPU 占用

**bjb2-28827:**
- cuda:0,1,2 → Object CRM eval (s42/43/44)
- cuda:3,4,5 → Spatial VLA-only (s42/43/44)

**bjb1-32546:**
- cuda:0,1,2 → Spatial CRM eval (s42/43/44)
- cuda:3 → CRM 4-suite training (r4, 已跑 12h52m)
- cuda:4,5 → Goal CRM eval (s42/43)

## Goal seed44 状态

**无法部署**。bjb1 cuda:3 被 4-suite 训练占用，bjb2 cuda:3,4,5 被 VLA-only spatial 占用。最早可用时间：VLA-only spatial 完成后（~1h），可在 bjb2 上部署。

## 下一步

1. 等所有 eval 完成后再次 harvest，获取完整 10-task 结果
2. VLA-only spatial 完成后，在 bjb2 cuda:3 上部署 goal seed44 CRM eval
3. Object VLA-only eval 需要在 Object CRM 完成后链式执行（或另找 GPU）

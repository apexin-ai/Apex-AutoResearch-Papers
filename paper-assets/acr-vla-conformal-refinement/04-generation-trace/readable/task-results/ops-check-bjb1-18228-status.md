# ops check bjb1 18228 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-bjb1-18228-status_20260515T094405_result.json`
- **Structured JSON:** [`870a1be2d5c43d427948.json`](../../sessions/87/870a1be2d5c43d427948.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进程状态报告

### GPU 使用

| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 23% | 4652/24564 MiB |
| cuda:1 | 24% | 2535/24564 MiB |
| cuda:2 | 22% | 6239/24564 MiB |
| cuda:3 | 20% | 2005/24564 MiB |

**4 个进程全部存活。**

---

### 1. PID 341873 — eval-obs-only-spatial-seed43 (cuda:2) ✅ ALIVE

- seed=43, start_task=0, max_correction_norm=0.1
- **当前：T0** `between_plate_and_ramekin` rollout 5/10, success 4/5
- 刚开始跑，无已完成 task

### 2. PID 325264 — eval-mag-obsonly-norm03-r2 (cuda:0) ✅ ALIVE

- seed=42, start_task=0, **max_correction_norm=0.3**
- **当前：T3**（日志截止到 T2 完成）
- 已完成 tasks：

| Task | 成功率 |
|------|--------|
| T0 between_plate_and_ramekin | 90% (9/10) |
| T1 next_to_ramekin | 100% (10/10) |
| T2 from_table_center | 0% (0/10) |

### 3. PID 311881 — eval-acr-spatial-v4-scalar-r2 (cuda:1) ✅ ALIVE

- mode=crm_scalar, seed=42, start_task=3, max_correction_norm=0.1
- **当前：T7**（日志截止到 T6 完成）
- 已完成 tasks：

| Task | 成功率 |
|------|--------|
| T3 on_the_cookie_box | 40% (4/10) |
| T4 in_top_drawer | 0% (0/10) |
| T5 on_the_ramekin | 0% (0/10) |
| T6 next_to_cookie_box | 90% (9/10) |

### 4. PID 312420 — eval-acr-spatial-v4-obs-only-r3 (cuda:3) ✅ ALIVE

- mode=crm_obs_only, seed=42, start_task=6, max_correction_norm=0.1
- **当前：T9** `on_the_wooden_cabinet` rollout 5/10, success 0/5
- 已完成 tasks：

| Task | 成功率 |
|------|--------|
| T6 next_to_cookie_box | 90% (9/10) |
| T7 on_the_stove | 0% (0/10) |
| T8 next_to_the_plate | 20% (2/10) |

---

**PID 341873 (seed43) 存活正常，正在跑 T0。** 该进程无 cron 监控，但目前状态健康。obs-only-r3 (PID 312420) 快完成了，只剩 T9 的后半段。

---

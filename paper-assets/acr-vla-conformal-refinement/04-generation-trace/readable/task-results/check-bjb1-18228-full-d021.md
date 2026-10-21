# check bjb1 18228 full d021

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1-18228-full-d021_20260515T020527_result.json`
- **Structured JSON:** [`79ab494743b9ee8518af.json`](../../sessions/79/79ab494743b9ee8518af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集。以下是完整状态报告：

---

## 1. eval-acr-spatial-v4-small (perdof, crm_v3_norm, max_norm=0.1)
- **PID**: 253085 — ALIVE, uptime ~5h35m (since 04:30)
- **GPU**: cuda:3, 1459MiB, util 20%
- **Tasks completed: 4/10**, 正在跑 T5
- Per-task breakdown:
  - T1 (between_plate_ramekin): **60%** (6/10) ✓
  - T2 (next_to_ramekin): **100%** (10/10) ✓
  - T3 (from_table_center): **10%** (1/10) ✓
  - T4 (on_cookie_box): **40%** (4/10) ✓
  - T5 (top_drawer): **running** — rollout 5/10, 0/5 so far
  - T6-T10: pending
- Current success: **21/40 = 52.5%** (completed tasks only)
- **ETA: ~6h50m → ~16:55**

## 2. eval-acr-spatial-v4-obs-only-r2 (obs_only, crm_v3_norm, max_norm=0.1)
- **PID**: 270097 — ALIVE, uptime ~3h44m (since 06:21)
- **GPU**: cuda:0, 4105MiB, util 23%
- **Tasks completed: 4/10**, starting T5
- Per-task breakdown:
  - T1 (between_plate_ramekin): **90%** (9/10) ✓
  - T2 (next_to_ramekin): **100%** (10/10) ✓
  - T3 (from_table_center): **0%** (0/10) ✓
  - T4 (on_cookie_box): **40%** (4/10) ✓
  - T5-T10: pending
- Current success: **23/40 = 57.5%** (completed tasks only)
- **ETA: ~5h36m → ~15:42**

## 3. eval-argmin-only-spatial (reconvla baseline)
- **PID**: 231426 (wrapper 231421) — ALIVE, uptime ~8h18m (since 01:47)
- **GPU**: cuda:1, 1423MiB, util 21%
- **Tasks completed: 7/10**, starting T8
- Per-task breakdown:
  - T1 (between_plate_ramekin): **60%** (6/10) ✓
  - T2 (next_to_ramekin): **100%** (10/10) ✓
  - T3 (from_table_center): **0%** (0/10) ✓
  - T4 (on_cookie_box): **30%** (3/10) ✓
  - T5 (top_drawer): **10%** (1/10) ✓
  - T6 (on_ramekin): **10%** (1/10) ✓
  - T7 (next_to_cookie_box): **90%** (9/10) ✓
  - T8-T10: pending
- Current success: **30/70 = 42.9%**
- **ETA: ~3h33m → ~13:39**

## 4. eval-acr-spatial-v4-scalar (scalar_unc, crm_v3_norm, max_norm=0.1)
- **PID**: 288939 — ALIVE, uptime ~31m (since 09:34)
- **GPU**: cuda:2, 2914MiB (shared!), **util 99%**
- **Tasks completed: 0/10**, on T1
- Per-task breakdown:
  - T1 (between_plate_ramekin): **running** — rollout 5/10, 3/5 so far
  - T2-T10: pending
- **ETA: ~9h54m → ~19:59**

## 5. eval-acr-spatial-v3 (perdof, crm_v2, max_norm=0.05) — 用户未列出
- **PID**: 232820 — ALIVE, uptime ~8h17m (since 01:48)
- **GPU**: cuda:2 (与 v4-scalar 共享!), 1450MiB
- **Tasks completed: 5/10**, on T6
- Per-task breakdown:
  - T1 (between_plate_ramekin): **10%** (1/10) ✓
  - T2 (next_to_ramekin): **0%** (0/10) ✓
  - T3 (from_table_center): **0%** (0/10) ✓
  - T4 (on_cookie_box): **0%** (0/10) ✓
  - T5 (top_drawer): **0%** (0/10) ✓
  - T6 (on_ramekin): **running** — rollout 5/10, 0/5 so far
  - T7-T10: pending
- Current success: **1/50 = 2.0%** — crm_v2 表现极差
- **ETA: ~6h47m → ~16:53**

---

## GPU 分配总览

| GPU | Util | 显存 | 进程 |
|-----|------|------|------|
| 0 | 23% | 13721/24564 MiB | v4-small + obs-only-r2 + v4-scalar + v3 (EGL render共享) |
| 1 | 21% | 1423/24564 MiB | argmin-only (reconvla) |
| 2 | **99%** | 2914/24564 MiB | **v4-scalar + v3 争抢!** |
| 3 | 20% | 1459/24564 MiB | v4-small (主计算) |

## 关键发现

1. **GPU 2 竞争严重**: eval-acr-spatial-v3 (crm_v2) 和 eval-acr-spatial-v4-scalar 同时占用 cuda:2，GPU util 99%，两个实验都会被拖慢。
2. **crm_v2 (v3实验) 基本废了**: 5个 task 完成，仅 1/50 成功 (2%)，远不如 crm_v3_norm。考虑 kill 掉释放 GPU 2 给 v4-scalar。
3. **obs_only 暂时领先**: 57.5% vs perdof 的 52.5%，但 T3 (from_table_center) obs_only 完全失败而 perdof 有 10%。
4. **reconvla baseline 42.9%**: 作为 baseline 比较合理，ACR 方法都有提升。

---

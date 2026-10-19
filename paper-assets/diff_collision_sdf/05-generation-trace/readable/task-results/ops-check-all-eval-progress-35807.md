# ops check all eval progress 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_all_eval_progress_35807_20260522T174746_result.json`
- **Structured JSON:** [`2803a95ca411a65b06e4.json`](../../sessions/28/2803a95ca411a65b06e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 1. eval_a3_object_m024fix_v11 (cuda:2) — 运行中

- **进度**: Task 0 已完成 (200/200)，Task 1 进行中 (30/200)
- **Task 0 结果**: TSR=0.0%, **CAR=88.5%**
- **SDF 值**: 全部 >> 0.01 (范围 0.18~0.77)，**refined=0 (全部为 0)**
- **结论**: M024 修复**没有效果**。SDF 值仍然远大于 refinement 阈值，refinement 从未触发。坐标修复后 SDF 值依然在 0.18~0.77 范围，说明问题不在坐标变换上，或者 SDF 阈值设置有问题。
- **预估剩余**: 每 10 episodes ~2.2min, Task 1 剩 170 eps (~37min), 还有若干 tasks 未开始。如果共 10 tasks，粗估还需 **~7-8 小时**。

## 2. eval_a1_lora_spatial_v11 (cuda:0) — 运行中

- **进度**: Task 0 已完成 (200/200)，Task 1 进行中 (160/200)
- **Task 0 结果**: TSR=0.5%, CAR=1.5%
- **Task 1 当前**: 全部 collided=True，预计 CAR=0.0%
- **预估剩余**: 每 10 eps ~2.8min。Task 1 剩 40 eps (~11min)，加后续 tasks 估计 **~8-9 小时**。

## 3. eval_baseline_fullft_spatial_v11 (cuda:1) — 运行中

- **进度**: Task 0 + Task 1 已完成 (各 200/200)，Task 2 进行中 (60/200)
- **Task 0 结果**: TSR=1.5%, **CAR=0.0%**
- **Task 1 结果**: TSR=0.0%, **CAR=0.0%**
- **Task 2 当前**: 全部 collided=True
- **预估剩余**: 每 10 eps ~2.7min。Task 2 剩 140 eps (~38min)，加后续 tasks 估计 **~6-7 小时**。

## 4. GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 8.6/96 GB | 53% |
| cuda:1 | 8.5/96 GB | 11% |
| cuda:2 | 8.6/96 GB | 13% |
| cuda:3 | 空闲 | 0% |

---

**关键发现**: A3 M024fix 的 SDF 值全部在 0.18~0.77，远高于 refinement 阈值，refined_count 始终为 0。修复坐标变换后 SDF 值仍然很大，refinement 完全没触发。

---

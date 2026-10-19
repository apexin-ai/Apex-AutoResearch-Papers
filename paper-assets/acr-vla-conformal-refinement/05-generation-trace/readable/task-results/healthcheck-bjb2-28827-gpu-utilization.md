# healthcheck bjb2 28827 gpu utilization

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_healthcheck_bjb2-28827-gpu-utilization_20260528T071431_result.json`
- **Structured JSON:** [`5a7284889597ee790176.json`](../../sessions/5a/5a7284889597ee790176.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报：bjb2-28827 GPU 健康检查

**无僵尸进程，所有实验健康运行。**

### 各 GPU 状态

| GPU | Util% | 显存 | 实验 | 状态 |
|-----|-------|------|------|------|
| 0 | 17% | 1977/24564 MiB | adaptive_conformal_crm, spatial, tau045, s42 | 活跃，正在跑 pick_up_black_bowl 系列 (rollout 10/20)，接近完成 |
| 1 | 12% | 1977/24564 MiB | adaptive_conformal_crm, spatial, tau025, s46 | **已完成** — 82.0% (164/200)，进程退出中 |
| 2 | 18% | 4299/24564 MiB | vla_only, long, s42 | 活跃，正在跑 LIVING_ROOM_SCENE5 (rollout 5/20) |
| 3 | 17% | 4299/24564 MiB | vla_only, long, s44 | 活跃，正在跑 LIVING_ROOM_SCENE5 (rollout 10/20) |
| 4 | 0% | 1 MiB | — | 空闲 |
| 5 | 0% | 1 MiB | — | 空闲 |

### eval-supp-long-vla-only 进度
- **s42 (cuda:2)**: 已完成 KITCHEN_SCENE4 (100%), KITCHEN_SCENE3 (95%)，当前 LIVING_ROOM_SCENE5，日志 15:09 更新
- **s44 (cuda:3)**: 已完成 KITCHEN_SCENE4 (100%), KITCHEN_SCENE3 (100%)，当前 LIVING_ROOM_SCENE5，日志 15:14 更新

### 低利用率原因
GPU 平均 11% 是因为：(1) eval rollout 本质是 CPU 仿真 + 间歇 GPU 推理，12-18% 属正常；(2) GPU 4-5 空闲拉低均值。**不是僵尸进程。**

### 可用 GPU
GPU 1（即将释放）、4、5 共 3 张卡空闲。是否需要部署 P1/P2 实验？

---

# ops batch2 collect and batch3 launch

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_batch2_collect_and_batch3_launch_20260525T135544_result.json`
- **Structured JSON:** [`331a874583a7868a3995.json`](../../sessions/33/331a874583a7868a3995.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`best/` 目录不存在，seed0_l005 只有 `30000/` checkpoint。没有 step 26000 或 best checkpoint。

cuda:1 和 cuda:2 正常运行。需要为 cuda:3 安排替代任务，或者跳过。

---

## 1. Batch 2 完整结果表

| Eval | Avg TSR | Avg CAR | T0 TSR/CAR | T1 TSR/CAR | T2 TSR/CAR | T3 TSR/CAR | T0 Disp | T1 Disp | T2 Disp | T3 Disp |
|------|---------|---------|------------|------------|------------|------------|---------|---------|---------|---------|
| **s0_l005** (seed0, λ=0.005, 30K) | 5.5% | 50.0% | 2%/58% | 20%/42% | 0%/86% | 0%/14% | 0.0433m | 0.1055m | 0.0147m | 0.0879m |
| **s0_l01** (seed0, λ=0.01, 30K) | 8.0% | 47.0% | 6%/56% | 26%/32% | 0%/88% | 0%/12% | 0.0557m | 0.1057m | 0.0096m | 0.0874m |
| **s2_l01** (seed2, λ=0.01, 30K) | 7.5% | 48.0% | 2%/56% | 28%/34% | 0%/82% | 0%/20% | 0.0466m | 0.1057m | 0.0101m | 0.0807m |

## 2. Batch 3 启动状态

| Eval | GPU | PID | 状态 |
|------|-----|-----|------|
| s1_l005_v3 (seed1, λ=0.005, 30K) | cuda:1 | 341967 | 运行中，已开始 Task 0，显存 8610 MiB |
| s2_l005_v3 (seed2, λ=0.005, 30K) | cuda:2 | 342101 | 运行中，已开始评估，显存 8610 MiB |
| s0_best_l005 (seed0, λ=0.005, best) | cuda:3 | 342240 | **失败** — `best/` 目录不存在，只有 `30000/` |

## 3. GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 27045 MiB | 4% (spatial_bowl 训练) |
| cuda:1 | 8610 MiB | 0% (eval 运行中) |
| cuda:2 | 8610 MiB | 0% (eval 运行中) |
| cuda:3 | 空闲 | 0% (eval 已失败退出) |

cuda:3 空闲可用。s0_best_l005 的 `best/` checkpoint 不存在，需要指定替代 checkpoint 或其他 eval 任务。

---

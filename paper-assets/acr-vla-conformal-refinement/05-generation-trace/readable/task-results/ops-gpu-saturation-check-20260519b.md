# ops gpu saturation check 20260519b

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-saturation-check-20260519b_20260519T081958_result.json`
- **Structured JSON:** [`689fca763d84d52d1223.json`](../../sessions/68/689fca763d84d52d1223.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动正常，模型正在加载。

---

## 汇报

### GPU 实际占用状态

| 服务器 | GPU | 利用率 | 显存 | 状态 |
|--------|-----|--------|------|------|
| **bjb2-28827** | 0 | 99% | 4777/24564 MiB | 忙 |
| | 1 | 0% | 1/24564 MiB | **空闲→已部署** |
| | 2 | 99% | 6640/24564 MiB | 忙 |
| | 3 | 19% | 3594/24564 MiB | 有进程，rollout间歇 |
| | 4 | 99% | 7644/24564 MiB | 忙 |
| | 5 | 99% | 7875/24564 MiB | 忙 |
| **bjb1-32546** | 0 | 19% | 2412/24564 MiB | 有进程 (PID 714913) |
| | 1 | 98% | 5598/24564 MiB | 忙 |
| | 2 | 23% | 2876/24564 MiB | 有进程 (PID 784387) |
| | 3 | 99% | 4350/24564 MiB | 忙 |
| | 4 | 99% | 7605/24564 MiB | 忙 |
| | 5 | 22% | 2412/24564 MiB | 有进程 (PID 714985) |
| **bjb2-40593** | 0 | 99% | 11178/24564 MiB | 忙 |

### K=10 Spatial 实验运行状态

| Session | 服务器 | 状态 | 进度 |
|---------|--------|------|------|
| `eval-spatial-obs-only-norm02-seed44` | bjb2-28827 | **ALIVE** | `pick_up_the_black_bowl_on_the_ramekin...` rollout 5/10 |
| `eval-spatial-obs-only-norm02-seed45` | bjb1-32546 | **ALIVE** | `pick_up_the_black_bowl_next_to_the_cookie_box...` rollout 1/10 |
| `eval-spatial-obs-only-norm02-seq` | bjb2-40593 | **ALIVE** | `pick_up_the_black_bowl_on_the_cookie_box...` rollout 5/10 |

三个 Spatial K=10 实验都在正常跑。

### 新部署实验

| exp_id | 服务器 | GPU | 类型 | seed |
|--------|--------|-----|------|------|
| `eval-argmin-object-k5-seed44` | bjb2-28827 | cuda:1 | K=5 argmin-only (reconvla) | 44 |

### 未能填满的卡

bjb1-32546 的 GPU 0/2/5 虽然利用率低 (19-23%)，但都有评估进程在跑，内存占用 2.4-2.9 GiB。这是 LIBERO 评估的正常模式——环境 reset/step 是 CPU-bound 操作，导致 GPU 利用率在 rollout 间隙下降。这些卡不是空闲的，不能再部署新任务。

---

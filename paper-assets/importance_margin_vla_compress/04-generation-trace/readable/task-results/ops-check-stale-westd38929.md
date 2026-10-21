# ops check stale westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_stale_westd38929_20260526T133722_result.json`
- **Structured JSON:** [`39acfbe25455c8cdd2c2.json`](../../sessions/39/39acfbe25455c8cdd2c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验状态：仍在运行**

- **PID 279274** 存活，已运行 **8h34m**
- 命令：`python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.5 --suite libero_10 --num_episodes 50 --seed 42`
- **进度：Task 9/10 进行中**（约 20/50 episodes），还剩 Task 9 剩余 + Task 10 全部

**已完成 8/10 tasks 的 per-task SR：**

| Task | Description | SR |
|------|-------------|-----|
| 1 | alphabet soup + tomato sauce → basket | 0.300 (15/50) |
| 2 | cream cheese + butter → basket | 0.260 (13/50) |
| 3 | turn on stove + moka pot | 0.220 (11/50) |
| 4 | black bowl → drawer + close | 0.020 (1/50) |
| 5 | white mug left plate + yellow mug right plate | 0.060 (3/50) |
| 6 | book → caddy back compartment | 0.440 (22/50) |
| 7 | white mug plate + chocolate pudding right | 0.260 (13/50) |
| 8 | alphabet soup + cream cheese → basket | 0.160 (8/50) |
| 9 | both moka pots → stove | *running (~20/50 ep)* |
| 10 | TBD | *pending* |

前 8 task 合计：86/400 = **21.5% 临时 SR**，速度 ~0.8 ep/min。预计还需 ~1-1.5 小时完成。

**GPU 利用率 (westd-38929)：**

| GPU | Util | VRAM |
|-----|------|------|
| 0 | 0% | 1 MiB / 98 GB (空闲) |
| 1 | 87% | 15.8 GB / 98 GB (eval 进程) |
| 2 | 68% | 16.0 GB / 98 GB |
| 3 | 69% | 15.9 GB / 98 GB |

GPU 0 完全空闲，GPU 1-3 在使用中（GPU 2/3 可能有其他实验在跑）。

---

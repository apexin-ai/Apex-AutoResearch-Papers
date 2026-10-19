# ops check fixed eval partial

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-fixed-eval-partial_20260516T173401_result.json`
- **Structured JSON:** [`4c37382c7862e925b5ff.json`](../../sessions/4c/4c37382c7862e925b5ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 核心发现：这两个进程是全新的，不是跑了 9.5h/5h 的老进程

| | seed1 (PID 104743) | seed2 (PID 111920) |
|--|--|--|
| **启动时间** | 01:21:35 CST | 01:26:14 CST |
| **已运行** | ~17 min | ~13 min |
| **GPU** | GPU 1, 5519 MiB | GPU 0, 6585 MiB |
| **进程状态** | Rl+ (running) | Rl+ (running) |
| **Checkpoint** | acib_v7_contrastive/checkpoint-20000 | acib_v7_seed2/checkpoint-20000 |

### tmux 实时输出

两者都在 **libero_spatial** (第 1 个 suite) 上活跃 rollout：
- **seed1**: step 96/280 of current episode, `running_success_rate=0.0%` (刚进入新 task). 历史 running_success_rate 最高 75%
- **seed2**: step 222/280 of current episode, `running_success_rate=0.0%`. 历史 running_success_rate ~71-72%

### 已完成的 task

- **seed1**: `libero_spatial_0` (10 videos, 01:23-01:26), `libero_spatial_1` (10 videos, 01:32-01:35). 当前在 task 2+
- **seed2**: `libero_spatial_0` (10 videos, 01:27-01:28), `libero_spatial_1` (6 videos, 01:36-01:37). 正在写 task 1 视频

**无 eval_info.json** — 尚无任何 suite 完成。

### 进度估算

- 每 task ~7 min (含环境加载 gap)
- 4 suites × 10 tasks = 40 tasks, n_episodes=50/suite
- **seed1**: ~38 tasks remaining × 7 min ≈ **4.5h** (ETA ~06:00 CST)
- **seed2**: ~39 tasks remaining × 7 min ≈ **4.5-5h** (ETA ~06:30 CST)
- libero_10 horizon 更长，可能拉长总时间到 **5-6 小时**

### 结论

进程正常推进，GPU utilization 低 (0-1%) 是正常的——LIBERO 仿真主要 CPU-bound，GPU 仅做 inference。之前报告的 "9.5h/5h 还在 task 0" 是误判——这两个 PID 是刚启动的新进程。

---

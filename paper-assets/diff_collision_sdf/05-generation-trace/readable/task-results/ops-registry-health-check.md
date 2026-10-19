# ops registry health check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry_health_check_20260526T002722_result.json`
- **Structured JSON:** [`c2fee7c5a8a4f21a65ef.json`](../../sessions/c2/c2fee7c5a8a4f21a65ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Registry 健康检查结果

### 1. PID 状态

| 实验 | 服务器 | PID | 状态 |
|------|--------|-----|------|
| train_pi05_a1_spatial_bowl_s0_l005 | westd-35807 | 3708 | **ALIVE** |
| train_pi05_phase2_lambda0_s2 | westd-35807 | 254634 | **ALIVE** |
| train_pi05_a1_obj_s0_l01_high | westd-35807 | 271266 | **ALIVE** |
| train_pi05_a1_obj_s1_l01_high | westd-35807 | 274407 | **ALIVE** |
| train_pi05_lora_baseline_s0 | westd-45947 | 3622 | **ALIVE** |
| train_pi05_lora_baseline_s1 | westd-45947 | 3712 | **ALIVE** |

### 2. GPU 占用

**westd-35807** (4 GPU, 全部 100% 利用率):

| GPU | 显存占用 | 对应 PID | 实验 |
|-----|----------|----------|------|
| 0 | 27045 MiB | 3717 (子进程 of 3708) | spatial_bowl_s0 |
| 1 | 19055 MiB | 271266 | a1_obj_s0_l01_high |
| 2 | 19055 MiB | 274407 | a1_obj_s1_l01_high |
| 3 | 27045 MiB | 254639 (子进程 of 254634) | phase2_lambda0_s2 |

**westd-45947** (2 GPU, 全部 100% 利用率):

| GPU | 显存占用 | 对应 PID | 实验 |
|-----|----------|----------|------|
| 0 | 27089 MiB | 3634 (子进程 of 3622) | lora_baseline_s0 |
| 1 | 27089 MiB | 3724 (子进程 of 3712) | lora_baseline_s1 |

### 3. Stale 实验

无。所有 RUNNING 实验的进程均存活。

### 4. 非追踪进程

无。所有 GPU 上的进程均可追溯到 registry 中的实验（GPU 上的 PID 是 registry 中 wrapper PID 的子进程）。

**结论：6/6 实验健康运行，6 张 GPU 全部满载 (100% utilization)。**

---

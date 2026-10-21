# ssh diagnose a3 exit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_a3_exit_20260520T072602_result.json`
- **Structured JSON:** [`9bc7134b1f8364816322.json`](../../sessions/9b/9bc7134b1f8364816322.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结论：**两个进程都没有退出，仍在正常训练中。** Cron 误判了。

## 诊断汇报

### 进程状态
| 实验 | Wrapper PID | Python PID | 状态 | 运行时间 |
|------|------------|------------|------|---------|
| a3_gradient_spatial_bowl_s0 | 50318 (Ss+) | 50328 (Sl) | **运行中** | ~8 min |
| a3_gradient_object_pudding_s0 | 50397 (Ss+) | 50407 (Rl) | **运行中** | ~8 min |

- `/tmp/agent-ml-exit/` 目录为空，没有 exit 文件 → 进程确实未退出

### 训练进度
| 实验 | 当前 step | 进度 | 最新 loss | lr |
|------|----------|------|----------|-----|
| spatial_bowl | **3044** / 30000 | 10% | 0.2450 | 2.47e-05 |
| object_pudding | **2843** / 30000 | 9% | 0.2280 | 2.48e-05 |

### Checkpoint 产出
- `spatial_bowl`: step 2500, 3000 已保存（路径 `/root/autodl-tmp/checkpoints/a3_grad_refine_spatial_bowl/a3_grad_refine_spatial_bowl_seed0/`）
- `object_pudding`: step 2500 已保存（路径 `/root/autodl-tmp/checkpoints/a3_grad_refine_object_pudding/a3_grad_refine_object_pudding_seed0/`）

### 注意：GPU 上有重复进程
每张 GPU 上有**两个** python 进程：
- **旧进程** PID 38485/38564（运行 3 小时，`--save_interval 500`）
- **新进程** PID 50328/50407（运行 8 分钟，`--save_interval 2000`）

每个进程占 16916MiB，两个共占 ~34GB / 97GB。目前显存足够，但旧进程可能是残留的，应考虑是否需要清理。

### 磁盘状态
`/root/autodl-tmp`: 35G / 250G 已用 (14%)，空间充足。

### GPU 状态
两块 NVIDIA RTX PRO 6000 Blackwell (98GB)，温度 54-55°C，功耗 320-388W / 600W，正常。

---

**结论：不需要更新 registry 为 DONE/failed — 两个实验仍在运行。** Cron 的退出检测可能是基于旧 PID 或错误的检测逻辑导致的误报。

---

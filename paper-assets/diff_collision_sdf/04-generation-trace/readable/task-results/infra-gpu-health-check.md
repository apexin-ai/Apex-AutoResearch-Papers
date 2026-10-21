# infra gpu health check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-health-check_20260529T030258_result.json`
- **Structured JSON:** [`1e39465d8f80ef81e0d8.json`](../../sessions/1e/1e39465d8f80ef81e0d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇总

### westd-35807

| 项目 | 状态 |
|------|------|
| **GPU** | 1x RTX PRO 6000 (96GB VRAM), **空闲** (0% util, 0 MiB used) |
| **根盘** | 30G 总量, 25G 已用, **6G 可用 (81%)** ⚠️ |
| **数据盘** | /dev/sda2: 879G 总量, 265G 已用, 570G 可用 |
| **autodl-tmp** | 268G (其中 checkpoints 207G) |
| **训练进程** | 无 |
| **tmux** | 无法通过 read-only 检查 |
| **项目目录** | /root/colliforce-vla ✅ |
| **/root/colliforce-vla/checkpoints/** | 不存在 (checkpoints 在 autodl-tmp) |

### westd-45947

| 项目 | 状态 |
|------|------|
| **GPU** | 1x RTX PRO 6000 (96GB VRAM), **空闲** (0% util, 0 MiB used) |
| **根盘** | 30G 总量, 17G 已用, 14G 可用 (57%) |
| **数据盘** | /dev/sda2: 439G 总量, 16G 已用, 400G 可用 |
| **autodl-tmp** | 240G (其中 checkpoints 196G) |
| **训练进程** | 无 |
| **项目目录** | /root/colliforce-vla ✅ |

---

### ⚠️ 关键发现：GPU 数量与约束不符

**约束 C001 声称** westd-35807 有 cuda:0-3 (4张)，westd-45947 有 cuda:0-1 (2张)。

**实际 nvidia-smi 只报了 1 张 GPU**（每台各 1 张）。物理机有 9/8 张 GPU（从 /proc/driver/nvidia/gpus/ 可见），但容器只分配了 1 张。环境变量中无 CUDA_VISIBLE_DEVICES 设置。

**结论**：westd-35807 当前 **只有 cuda:0 可用**，无法使用 cuda:1-3。如需多卡训练，需要先在 AutoDL 控制台调整容器的 GPU 分配数量。

### 其他注意事项
- westd-35807 根盘只剩 6G，安装新依赖或写临时文件要小心，大文件务必放 autodl-tmp
- 两台服务器 GPU 均空闲，无运行中的训练任务，单卡训练可以立即开始

---

# diag gpu status all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu-status-all-servers_20260523T180627_result.json`
- **Structured JSON:** [`82a52942ca6f8ac96236.json`](../../sessions/82/82a52942ca6f8ac96236.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-38929
- GPU 0: 空闲 (0%, 0/98GB)
- GPU 1: 空闲 (0%, 0/98GB)
- GPU 2: 空闲 (0%, 0/98GB)
- GPU 3: 空闲 (0%, 0/98GB)
- 无 tmux session，仅 tensorboard/jupyter 后台
- **空闲 GPU: [0,1,2,3]**

## westd-27271
- GPU 0: **占用** (70%, 16GB/98GB) — `eval_openvla_baseline_goal_seed42_v3` (baseline, libero_goal, seed42)
- GPU 1: **占用** (69%, 16GB/98GB) — `eval_openvla_baseline_long_seed42` (baseline, libero_10, seed42)
- 注意：nvidia-smi 仅返回 2 张卡（可能仅配置了 2 GPU）
- **空闲 GPU: 无**

## westd-41074
- GPU 0: 空闲 (0%, 1MB/98GB)
- GPU 1: **占用** (2%, 10GB/98GB) — `eval_pi05_random_k0925_goal_seed42_v2` (random, k=0.925, libero_goal)
- GPU 2: **占用** (46%, 10.6GB/98GB) — `eval_pi05_random_k085_spatial_seed42_v2` (random, k=0.85, libero_spatial)
- GPU 3: **占用** (32%, 10.6GB/98GB) — `eval_pi05_l2norm_k085_spatial_seed42_v2` (l2norm, k=0.85, libero_spatial)
- 另有 `smolvla_spatial`、`xvla_long`、`diag_read_goal_results` tmux session 存在但已停止
- **空闲 GPU: [0]**

## cqa1-33015
- GPU 0: 空闲 (0%, 0/24GB)
- GPU 1: 空闲 (0%, 0/24GB)
- GPU 2: 空闲 (0%, 0/24GB)
- GPU 3: 空闲 (0%, 0/24GB)
- 无 tmux session，仅 tensorboard/jupyter 后台
- **空闲 GPU: [0,1,2,3]**

---

**汇总：共 16 张 GPU，11 张空闲，5 张在跑实验。**

| 服务器 | 总GPU | 空闲 | 在跑实验 |
|--------|-------|------|----------|
| westd-38929 | 4×H800 | **4** | 无 |
| westd-27271 | 2×H800 | **0** | 2 个 OpenVLA baseline eval |
| westd-41074 | 4×H800 | **1** (GPU0) | 3 个 π0.5 pruning eval (spatial+goal) |
| cqa1-33015 | 4×4090 | **4** | 无 |

---

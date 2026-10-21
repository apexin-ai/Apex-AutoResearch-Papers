# ops gpu audit cqa1 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-cqa1-v3_20260520T154432_result.json`
- **Structured JSON:** [`ec882b8b4be8c8a4f23f.json`](../../sessions/ec/ec882b8b4be8c8a4f23f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cqa1-33015 GPU 排查结果

### nvidia-smi 完整原始输出

```
Wed May 20 23:44:54 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.76.05              Driver Version: 580.76.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4090 D      On  |   00000000:27:00.0 Off |                  Off |
| 30%   33C    P2             94W /  425W |    4540MiB /  24564MiB |     47%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA GeForce RTX 4090 D      On  |   00000000:28:00.0 Off |                  Off |
| 30%   41C    P2             96W /  425W |    4539MiB /  24564MiB |      1%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA GeForce RTX 4090 D      On  |   00000000:A8:00.0 Off |                  Off |
|  0%   25C    P8             21W /  425W |       3MiB /  24564MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA GeForce RTX 4090 D      On  |   00000000:A9:00.0 Off |                  Off |
| 30%   38C    P2            109W /  425W |    4539MiB /  24564MiB |      1%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A          443004    C+G   python                                 4521MiB |
|    1   N/A  N/A          346216    C+G   python                                 4521MiB |
|    3   N/A  N/A          344867    C+G   python                                 4521MiB |
+-----------------------------------------------------------------------------------------+
```

### GPU 进程详情

```
443004, GPU-6a33d62b-..., 4521 MiB
346216, GPU-7ee85176-..., 4521 MiB
344867, GPU-c242dd9c-..., 4521 MiB
```

### 逐 GPU 汇总

| GPU | 显存 | Util | PID | 任务 | 状态 |
|-----|------|------|-----|------|------|
| 0 | 4540/24564 MiB | 47% | 443004 | seed43 k=0.2, 50eps | **运行中**，已跑 ~32min |
| 1 | 4539/24564 MiB | 1% | 346216 | seed44 k=0.3, 50eps | **运行中**，已跑 ~70min |
| 2 | 3/24564 MiB | 0% | — | 无 | **空闲** |
| 3 | 4539/24564 MiB | 1% | 344867 | seed43 k=0.3, 50eps | **运行中**，已跑 ~70min |

### PID 检查

| 任务 | PID | 状态 |
|------|-----|------|
| seed43 k=0.2 | 443004 | **运行中** (Rl, 启动于 23:12) |
| seed44 k=0.3 | 346216 | **运行中** (Rl, 启动于 22:34) |
| seed43 k=0.3 | 344867 | **运行中** (Rl, 启动于 22:34) |
| seed44 k=0.5 | 132420 | **已结束** — 进程不存在 |

### 已完成结果

**xvla_prune_k0.5_libero_object_seed44.json**（23:12 写入）：SR=**0.444**, 500 episodes, 耗时 6167s

### 未完成结果

- `xvla_prune_k0.3_libero_object_seed43.json` — 文件不存在，PID 344867 仍在跑
- `xvla_prune_k0.3_libero_object_seed44.json` — 文件不存在，PID 346216 仍在跑
- `xvla_prune_k0.2_libero_object_seed43.json` — 文件不存在，PID 443004 仍在跑

GPU 2 空闲，可用于新任务。

---

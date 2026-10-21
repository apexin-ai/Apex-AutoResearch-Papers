# ssh gpu audit westd45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_audit_westd45947_20260520T202039_result.json`
- **Structured JSON:** [`13f31dec96db98464aaf.json`](../../sessions/13/13f31dec96db98464aaf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-45947 GPU 全面核查结果

### 逐卡状态

| | cuda:0 | cuda:1 |
|---|---|---|
| **GPU** | NVIDIA RTX PRO 6000 Black (98GB) | NVIDIA RTX PRO 6000 Black (98GB) |
| **PID** | 71494 | 73165 |
| **实验** | a3_grad_refine_spatial_bowl_s0 | a3_grad_refine_object_pudding_s0 (--resume) |
| **最新 step** | **11232** / 30000 (37%) | **13334** / 30000 (44%) |
| **状态** | **alive** (Sl, 运行 12h21m) | **alive** (Rl, 运行 12h20m) |
| **VRAM** | 23926 MiB / 97887 MiB | 23926 MiB / 97887 MiB |
| **GPU-Util** | 100% | 100% |
| **温度/功耗** | 68°C / 489W | 70°C / 470W |
| **速度** | ~4.0 s/it | ~4.0 s/it |
| **最新 loss** | 0.0430 (step 11232) | 0.0258 (step 13330 附近) |

### 磁盘

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|---|---|---|---|---|
| `/root/autodl-tmp` | 250G | 71G | 180G | 29% |
| `/` (根) | 30G | 8.6G | 22G | 29% |

### Checkpoint 状态

**a3_grad_refine_spatial_bowl_seed0:**
- 已保存: step 6000 / 8000 / 10000 + best
- best = step 10000, loss = 0.0510
- 最新 ckpt 时间: May 21 02:57

**a3_grad_refine_object_pudding_seed0:**
- 已保存: step 8000 / 10000 / 12000 + best
- best = step 12000, loss = 0.0296
- 最新 ckpt 时间: May 21 02:51

### 小结

两卡满载运行，进程健康，无空闲卡。按 ~4s/it 估算：
- spatial_bowl: 剩余 18768 步 ≈ **20.8h**
- object_pudding: 剩余 16666 步 ≈ **18.5h**

---

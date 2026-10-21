# ssh gpu health 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_health_30476_20260517T201519_result.json`
- **Structured JSON:** [`975b618c8495649d74cb.json`](../../sessions/97/975b618c8495649d74cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告 — westd-30476

| GPU | PID | 实验名 | GPU 利用率 | 显存占用 | 进度 | 速度 | 预计剩余 | 状态 |
|-----|------|--------|-----------|---------|------|------|---------|------|
| **0** | 34716 | `grid_b0_1_seed42` | 92% | 74,989 / 97,887 MiB (77%) | **5560/8477 (66%)** | 3.25 it/s | ~15 min | 训练中 |
| **1** | 42432 | `grid_b0_3_seed123_r2` | 83% | 74,989 / 97,887 MiB (77%) | **7167/8477 (85%)** | 3.26 it/s | ~7 min | 训练中 |
| **2** | 41387 | `rho02_adaptive_tau08_seed42` | 99% | 46,505 / 97,887 MiB (48%) | **3032/6103 (50%)** | 2.34 s/it | ~2h | 训练中 |
| **3** | 48891 | `batchsize16_nmin8_r2` | 100% | 71,173 / 97,887 MiB (73%) | **1038/6103 (17%)** | 2.46 s/it | ~3.5h | 训练中 |

### 关键信息

- **4 张 GPU 全部被占用**，无空闲卡
- GPU 0/1 跑的是 **grid search 实验**（b=0.1/0.3），token 级加权，batch_size=4, grad_accum=4，速度快（~3.25 it/s），GPU 1 约 7 分钟完成，GPU 0 约 15 分钟完成
- GPU 2 跑的是 **adaptive weighting (rho=0.2, tau=0.8)**，显存占用较低（46 GB），已运行约 2 小时，还需约 2 小时
- GPU 3 跑的是 **batch_size=16 + n_min=8 实验**，开启了 gradient_checkpointing，已运行约 42 分钟，还需约 3.5 小时
- **没有实验完成**，所有 4 个都在正常训练中，无报错

---

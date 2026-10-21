# ops gpu status check loop3

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_loop3_20260525T192458_result.json`
- **Structured JSON:** [`a3aba16cea163a929697.json`](../../sessions/a3/a3aba16cea163a929697.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## GPU 状态报告 (2026-05-26 ~03:55 UTC)

### westd-35807 (4×RTX PRO 6000 97GB)

| GPU | 显存 | 利用率 | 状态 | 进程 |
|-----|------|--------|------|------|
| cuda:0 | 27045/97887 MiB | 100% | **训练中** | `train_a1_sdf_aux_pi05.py --scene spatial_bowl --seed 0` |
| cuda:1 | 1/97887 MiB | 0% | **空闲** | — |
| cuda:2 | 1/97887 MiB | 0% | **空闲** | — |
| cuda:3 | 27035/97887 MiB | 85% | **Eval 中** | `eval_pi05_a1_best_s2_l005_10k` (3 个 eval worker) |

**训练进度 — spatial_bowl s0 λ=0.05:**
- Step: **9300/30000 (31%)**，速度 4.63 s/it
- 已运行 ~1h40m，ETA **~26h38m**
- Loss: action=0.0169, sdf=0.0303, ee=0.0240

**Eval — eval_pi05_a1_best_s2_l005_10k:**
- 正在运行，当前处理 episode 30/200（chocolate_pudding 任务）

**已完成 Eval 结果:**

| Eval | TSR | CAR |
|------|-----|-----|
| eval_s0_l005_30k_final | **0.075** | 0.470 |
| eval_s0_l01_30k_final | **0.055** | 0.530 |

逐任务（l005）: orange_juice TSR=0.06/CAR=0.58, chocolate_pudding TSR=0.24/CAR=0.38, milk TSR=0.00/CAR=0.76, bbq_sauce TSR=0.00/CAR=0.16

**磁盘:** 210/350 GB (60%)

---

### westd-45947 (2×RTX PRO 6000 97GB)

| GPU | 显存 | 利用率 | 状态 | 进程 |
|-----|------|--------|------|------|
| cuda:0 | 27089/97887 MiB | 100% | **训练中** | `train_pi05_lora_baseline.py --scene object_pudding --seed 0 --resume` |
| cuda:1 | 27089/97887 MiB | 100% | **训练中** | `train_pi05_lora_baseline.py --scene object_pudding --seed 1 --resume` |

**训练进度 — LoRA baseline:**

| Seed | Step | 进度 | ETA | Loss (action) |
|------|------|------|-----|---------------|
| s0 | 25486/30000 | **85%** | ~5h48m | 0.0148 |
| s1 | 25487/30000 | **85%** | ~5h48m | 0.0152 |

速度均为 ~4.62 s/it。

**磁盘:** 198/250 GB (79%) ⚠️ 偏高

---

### 总结

- **空闲 GPU:** westd-35807 的 **cuda:1** 和 **cuda:2** 可用
- westd-45947 两张卡全部占满，LoRA baseline 预计 **~6h 后完成**（约 UTC 10:00）
- westd-35807 spatial_bowl 训练还需 **~27h**，eval 正在 cuda:3 上运行
- 30k checkpoint eval 结果偏低（TSR 5.5%~7.5%），chocolate_pudding 是唯一有成功率的任务

---

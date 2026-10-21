# check gpu status all

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_status_all_20260528T000635_result.json`
- **Structured JSON:** [`2045ee211bfbc6b757fc.json`](../../sessions/20/2045ee211bfbc6b757fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态总览

### westd-35807（4× RTX PRO 6000, 98GB）

| GPU | 利用率 | 显存 | 状态 | 任务 | PID |
|-----|--------|------|------|------|-----|
| cuda:0 | 0% | 0/98GB | **空闲** | — | — |
| cuda:1 | 100% | 27GB/98GB | 运行中 | `train_a1_sdf_aux_pi05.py --scene object_pudding --seed 0 --lambda_sdf 0 --resume` | 892014 |
| cuda:2 | 100% | 27GB/98GB | 运行中 | `train_a1_sdf_aux_pi05.py --scene object_pudding --seed 2 --lambda_sdf 0 --resume` | 856471 |
| cuda:3 | 0% | 0/98GB | **空闲** | — | — |

**spatial_bowl eval 已完成**（22:58 UTC），结果写入 `eval_spatial_bowl_lora_ctrl_s0.log`。最新 eval 产出：`eval_pi05_a1_best_s0_l005.json`（07:37 UTC）。

### westd-45947（2× RTX PRO 6000, 98GB）

| GPU | 利用率 | 显存 | 状态 | 任务 | PID |
|-----|--------|------|------|------|-----|
| cuda:0 | 0% | 0/98GB | **空闲** | — | — |
| cuda:1 | 100% | 27GB/98GB | 运行中 | `train_a1_sdf_aux_pi05.py --scene object_pudding --seed 2 --lambda_sdf 0.1` | 425058 |

sentinel 显示 λ=0.1 s2 训练从 19:29 UTC 开始，目标 checkpoint 30000 steps。

**空闲 GPU：westd-35807 cuda:0, cuda:3；westd-45947 cuda:0（共 3 张）。**

---

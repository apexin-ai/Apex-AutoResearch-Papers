# diag post restart status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_post-restart-status_20260523T034437_result.json`
- **Structured JSON:** [`ea92cdda88a271a9e04b.json`](../../sessions/ea/ea92cdda88a271a9e04b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. 28034 GPU 状态 (4× RTX 5090 32GB)

| GPU | 显存 | 利用率 | 状态 |
|-----|------|--------|------|
| 0 | 2/32607 MiB | 0% | **空闲** |
| 1 | 21768/32607 MiB | 37% | `run_exp004_reduced_lora.py` (PID 30011) |
| 2 | 2/32607 MiB | 0% | **空闲** |
| 3 | 2/32607 MiB | 0% | **空闲** |

### 2. reduced-lora 训练

**仍在跑。** 当前 step **5610**/?, elapsed ~11h, loss 已收敛 (total_loss=0.000187)。最新 checkpoint: **checkpoint-5500**。

可用 checkpoints: 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500

### 3. eval 结果 (ckpt 3500-5000 已完成)

| Checkpoint | SYCONScore | ToF | NoF |
|------------|------------|-----|-----|
| ckpt3500 | 0.1881 | 0.1050 | 0.9061 |
| ckpt4000 | 0.2051 | 0.1160 | 0.8840 |
| **ckpt4500** | **0.2707** | **0.1602** | 0.8729 |
| ckpt5000 | 0.2463 | 0.1436 | 0.8619 |

**ckpt4500 是当前最优。** ckpt5000 开始下降。ckpt5500 尚未 eval。之前的 eval 进程 (PID 156229/157352/156793) 已死——服务重启被 kill。

### 4. 29046 GPU 状态 (2× RTX PRO 6000 Blackwell 98GB)

| GPU | 显存 | 利用率 | 状态 |
|-----|------|--------|------|
| 0 | 38197/97887 MiB | 95% | `run_exp003_gs8_r3only.py` (PID 516696) |
| 1 | 41337/97887 MiB | 95% | `run_exp003_len512_r3only.py` (PID 553700) |

- **gs8**: step **38**/8000 (~0.5%), ~65s/step, ~42min elapsed. 目录里有旧 checkpoint (500/1000/1500) 应是之前 run 遗留。
- **len512**: step **107**/8000 (~1.3%), ~48s/step, ~1h28m elapsed. 输出目录还空（首个 checkpoint 未到 500）。

### 5. s2 ckpt-2500

**存在**，位于 `/root/autodl-tmp/contrastive_entrain_calib/outputs/exp-004-act-baseline-s2/checkpoint-2500/`，adapter_model.safetensors 698MB。

### 6. 空闲 GPU

| 服务器 | 可用 GPU |
|--------|----------|
| **28034** | GPU 0, GPU 2, GPU 3 (3× RTX 5090 32GB) |
| 29046 | 无 (两张都满载) |

---

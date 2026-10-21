# diagnose check all running westd

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_check-all-running-westd_20260518T125914_result.json`
- **Structured JSON:** [`1f31bb266bf78baadb3d.json`](../../sessions/1f/1f31bb266bf78baadb3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 1. factorial_h2_episodeadv_seed2 (PID 576727, GPU 0,1)

| 项目 | 状态 |
|------|------|
| PID 存活 | **是** (State: S sleeping, 57 threads) |
| GPU 显存 | GPU 0: 45657/97887 MiB (53% util), GPU 1: 44571/97887 MiB (52% util) |
| 训练步数 | **step 2/15 (13%)**, 已运行 1h27m, ETA ~9h35m (~2654s/step) |
| W&B run | w0n74omu ✓ |

关键指标 @ step 2: success=18.75%, pass@8=62.5%, kl_loss=0.405, entropy=0.47

### 2. gsweep_g095_h5_seed1 (PID 416289, GPU 2,3)

| 项目 | 状态 |
|------|------|
| PID 存活 | **是** (State: S sleeping, 57 threads, CUDA_VISIBLE_DEVICES=2,3) |
| GPU 显存 | GPU 2: 14627/97887 MiB (97% util), GPU 3: 14627/97887 MiB (93% util) |
| 训练步数 | **至少 step 5/15** (checkpoint global_step_5 保存于 20:45)，当前可能在 step 6 |
| W&B run | 本地实际为 d3irreww（非 jv3aa2cj，可能是 watchdog 重启后产生的新 run） |

注意：tmux `gsweep_watchdog` 缓冲区被大量 "Skipping non-numeric metric" warnings 淹没，step 摘要行已滚出，步数通过 checkpoint 目录推断。

### 3. 通用

- **4 GPU 全部在用**，无空闲
- **RAM**: 81GB / 1.0TB used, 879GB available，充足
- **无异常**：两个实验均正常运行，无 OOM、crash 或异常信号

---

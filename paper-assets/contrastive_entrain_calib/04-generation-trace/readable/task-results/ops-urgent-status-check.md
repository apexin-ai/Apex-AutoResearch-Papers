# ops urgent status check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-status-check_20260523T215914_result.json`
- **Structured JSON:** [`b348524b4398d0aa72fa.json`](../../sessions/b3/b348524b4398d0aa72fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. exp-004-heldout (PID 571918, GPU0)
| 指标 | 值 |
|------|-----|
| **当前 step** | **6250 / 8000** (78.1%) |
| **最新 loss** | total=8.8e-05, sft=1e-06, l2=8.7e-04 |
| **最新 checkpoint** | checkpoint-6000 (May 24 05:20) |
| **速度** | ~9.2s/step |
| **预计完成** | 还剩 1750 steps ≈ **4.5h → ~May 24 10:30** |

Loss 已收敛，sft_loss 基本为零，仅 l2 正则项有微小波动。

### 2. exp-003-len512-v3 (PID 553700, GPU1)
| 指标 | 值 |
|------|-----|
| **当前 step** | **1497 / 8000** (18.7%) |
| **最新 checkpoint** | checkpoint-1000 (May 23 23:31) |
| **速度** | ~46.5s/step (GRPO 生成+训练) |
| **最新 reward** | 0.475 (step 1000) |
| **预计完成** | 还剩 6503 steps ≈ **84h → ~May 27 18:00** |

注意：日志持续报 `d_syc not loaded; returning R3-only rewards`，仅用 R3 reward。

### 3. GPU 状态
| GPU | 型号 | 温度 | 功耗 | 显存 | 利用率 |
|-----|------|------|------|------|--------|
| 0 | RTX PRO 6000 Blackwell | 45°C | 197W/600W | 23GB/98GB | **41%** |
| 1 | RTX PRO 6000 Blackwell | 66°C | 409W/600W | 41GB/98GB | **97%** |

GPU0 利用率低（SFT 训练轻量），GPU1 满负荷（GRPO 需采样多条 completion）。

### 4. ckpt-2000 Eval 结果
已完成 ckpt-1000 / ckpt-1500 / ckpt-2000 三个 checkpoint 的 eval。ckpt-2500+ 尚无 eval 结果。

**ckpt-2000 指标：**
- **SYCONScore = 0.1567**
- ToF = 0.0857, NoF = 0.9143
- n_valid=35, n_invalid=35, n_total=70

---

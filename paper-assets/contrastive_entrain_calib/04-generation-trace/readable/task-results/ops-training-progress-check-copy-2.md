# ops training progress check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-progress-check_20260523T151543_result.json`
- **Structured JSON:** [`bc6bf1860389820b9791.json`](../../sessions/bc/bc6bf1860389820b9791.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度汇总

### 实验 1: exp-004-heldout (PID 571918, GPU0)

| 指标 | 值 |
|------|-----|
| 进度 | **3620 / 8000** (45.3%) |
| 已运行 | 9h 18m |
| 速度 | ~9.2s/step |
| 最新 loss | total_loss=0.000109, sft_loss=3e-6, l2_loss=0.00106 |
| 最新 checkpoint | **checkpoint-3500** |
| GPU 利用率 | 39%, 显存 22.9/97.9 GB |
| 预计剩余 | ~11.2h → **约 May 24 10:30 完成** |

### 实验 2: exp-003-len512-v3 (PID 553700, GPU1)

| 指标 | 值 |
|------|-----|
| 进度 | **981 / 8000** (12.3%) |
| 已运行 | 12h 59m |
| 速度 | ~47s/step |
| 最新 loss | loss=0.0005, reward=0.555, kl=0.0115 (epoch 20.0) |
| 最新 checkpoint | **checkpoint-500**（输出目录 `exp003_len512_r3only/`） |
| GPU 利用率 | 95%, 显存 41.3/97.9 GB |
| 预计剩余 | ~91.6h ≈ 3.8 天 → **约 May 27 下午完成** |

exp003 比 exp004 慢约 5 倍（47s vs 9.2s per step），主要因为它是 GRPO 训练（需要 rollout generation），占用更多显存和计算。按当前速度，exp003 需要近 4 天才能完成 8000 步。

---

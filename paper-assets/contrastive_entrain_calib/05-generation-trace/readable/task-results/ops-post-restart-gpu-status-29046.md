# ops post restart gpu status 29046

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart-gpu-status-29046_20260519T124601_result.json`
- **Structured JSON:** [`bacd2c010d4024808c50.json`](../../sessions/ba/bacd2c010d4024808c50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态报告

### GPU 状态
| GPU | 利用率 | 显存占用 | 温度 |
|-----|--------|----------|------|
| 0 (exp002v2-recalib) | 95% | 66,907 MiB | 63°C |
| 1 (exp-003) | 97% | 38,161 MiB | 65°C |

两卡满载运行，温度正常。

### exp-003 (R3-only GRPO, GPU 1, PID 70649)
- **状态**: 运行中，已运行 19h55m
- **进度**: **2505/8000** (31.3%)
- **速度**: ~26s/step，预计剩余 ~40h
- **R3 reward**: 近几步在 0.33–0.66 波动，step 2500 时 mean=0.4883
- 日志路径实际在 `/root/contrastive_entrain_calib/logs/exp003_v2.log`（非 `~/runs/`）

### exp002v2-recalib (Cosine + Recalib, GPU 0, PID 172838)
- **状态**: 运行中，已运行 6h06m
- **进度**: **1535/8000** (19.2%)
- **速度**: ~16s/step，预计剩余 ~28h
- **最近 reward 值**:
  - R1: -0.13 (波动在 -0.25 ~ -0.04)
  - R2: -0.07 ~ -0.09
  - R3: ~0.998 (非常高且稳定)
  - Combined: ~0.72

### 小结
两个实验均在服务重启后正常存活，持续训练中。exp002v2-recalib 的 R1 仍为负值，R3 接近饱和；exp-003 的 R3 reward 波动较大（0.3–0.7），尚在收敛过程中。

---
